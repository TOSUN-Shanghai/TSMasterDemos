
APP_CAN                       = 0;
APP_LIN                       = 1;
BUS_UNKNOWN_TYPE              = 0;
TS_TCP_DEVICE                 = 1;
TS_USB_DEVICE                 = 3;
XL_USB_DEVICE                 = 2;
lfdmACKOff                    = 1;
lfdmNormal                    = 0;
lfdmRestricted                = 2;
lfdtCAN                       = 0;
lfdtISOCAN                    = 1;
lfdtNonISOCAN                 = 2;
LVL_ERROR                     = 1;
LVL_WARNING                   = 2;
LVL_OK                        = 3;
LVL_HINT                      = 4;
LVL_INFO                      = 5;
LVL_VERBOSE                   = 6;

APP_NAME = "TestCOMTSMaster";
USE_XL_VIRTUAL_DEVICE = false;
USE_XL_VN1630_DEVICE = false;
USE_XL_VN1640_DEVICE = false;
USE_TS_VIRTUAL_DEVICE = true;
USE_TS_CANMINI_DEVICE = false;
DBC_File_CAN = '..\..\..\Data\Demo\Databases\PowerTrain.dbc';

fprintf('Script started\n');
global db

% retrieve TSMaster application management
app = actxserver('comTSMaster.TSApplication');

% set current application name
app.set_current_application(APP_NAME);
fprintf('current application is %s\n', app.get_current_application());

% get all application in a list separated by ";"
fprintf("application list is: %s\n", app.get_application_list());

% set CAN channel count to 2
app.set_can_channel_count(2);

% set LIN channel count to 2
app.set_lin_channel_count(0);

% read CAN channel count
fprintf("CAN channel count = %d\n", app.get_can_channel_count());

% read LIN channel count
fprintf("LIN channel count = %d\n", app.get_lin_channel_count());

% delete mapping of application CAN channel 1 and 2
app.del_mapping(APP_CAN, 0);
app.del_mapping(APP_CAN, 1);

% map application channel 1 to hw index 0, channel 0 of Vector virtual channel
r.FAppName = APP_NAME;
r.FAppChannelIndex = 0;
r.FAppChannelType = APP_CAN;
if USE_XL_VIRTUAL_DEVICE
	r.FHWDeviceType = XL_USB_DEVICE;
	r.FHWDeviceSubType = 1;
elseif USE_XL_VN1630_DEVICE
	r.FHWDeviceType = XL_USB_DEVICE;
	r.FHWDeviceSubType = 57;
elseif USE_XL_VN1640_DEVICE
	r.FHWDeviceType = XL_USB_DEVICE;
	r.FHWDeviceSubType = 59;
elseif USE_TS_VIRTUAL_DEVICE
	r.FHWDeviceType = TS_TCP_DEVICE;
	r.FHWDeviceSubType = -1;
elseif USE_TS_CANMINI_DEVICE
	r.FHWDeviceType = TS_USB_DEVICE;
	r.FHWDeviceSubType = 3;
end
r.FHWIndex = 0;
r.FHWChannelIndex = 0;
r.FHWDeviceName = "Virtual";
r.FMappingDisabled = false;
app.set_mapping_verbose(r.FAppChannelIndex, r.FAppChannelType, ...
    r.FHWDeviceType, r.FHWIndex, r.FHWChannelIndex, r.FHWDeviceSubType, ...
    r.FHWDeviceName, r.FMappingDisabled);

% map application channel 2 to hw index 0, channel 1 of Vector virtual channel
r.FAppChannelIndex = 1;
r.FHWChannelIndex = 1;
app.set_mapping_verbose(r.FAppChannelIndex, r.FAppChannelType, ...
    r.FHWDeviceType, r.FHWIndex, r.FHWChannelIndex, r.FHWDeviceSubType, ...
    r.FHWDeviceName, r.FMappingDisabled);

% print application CAN channel mappings
[r.FHWDeviceType, r.FHWIndex, r.FHWChannelIndex, r.FHWDeviceSubType, ...
    r.FHWDeviceName, r.FMappingDisabled] = app.get_mapping_verbose(APP_CAN, 0);
fprintf("Application CAN channel 1 mapping to: %s of Channel %d\n", r.FHWDeviceName, r.FHWChannelIndex);
[r.FHWDeviceType, r.FHWIndex, r.FHWChannelIndex, r.FHWDeviceSubType, ...
    r.FHWDeviceName, r.FMappingDisabled] = app.get_mapping_verbose(APP_CAN, 1);
fprintf("Application CAN channel 1 mapping to: %s of Channel %d\n", r.FHWDeviceName, r.FHWChannelIndex);

% configure CAN channel baudrates before connection: Arb = 500K, Data = 2M
app.configure_baudrate_canfd(0, 500, 2000, lfdtISOCAN, lfdmNormal, true);
app.configure_baudrate_canfd(1, 500, 2000, lfdtISOCAN, lfdmNormal, true);

% get communication object
com = app.TSCOM();
registerevent(com, {'OnRxCAN', @OnRxCAN});
registerevent(com, {'OnRxCANFD', @OnRxCANFD});
registerevent(com, {'OnRxLIN', @OnRxLIN});

% enable CAN message reception event, select only one entry from CAN and CAN FD events
com.enable_event_can(true);
com.enable_event_canfd(false);

% MATLAB will convert any single column matrix to a 1 dimensional array when passed to a COM object.
feature('COM_SafeArraySingleDim', 0);
feature('COM_PassSafeArrayByRef', 0);

% display function prototypes for com
invoke(com)
events(com)

% init a TCAN record for CAN message transmission
c.FIdxChn = 0;
c.FIsExtendedId = false;
c.FIsRemote = false;
c.FIdentifier = hex2dec('64');
c.FDLC = 8;
c.FDatas = '0, 5, 20, 3, 159, 52, 134, 1';

% retrieve db kernel
db = app.TSDB();
% display function prototypes for com
invoke(db)
events(db)
% parse classical CAN dbc
id = db.load_can_db(DBC_File_CAN, '0,1');
fprintf('CAN/CAN-FD database loaded with Id = %d\n', id);
% set engine speed to 2000rpm
c.FDatas = db.set_signal_value_can_verbose(c.FIdxChn, c.FDatas, 'EngineData', 'EngSpeed', 2000);

% connect application
app.log('connecting application...', LVL_HINT);
app.connect();

% retrieve application timestamp
fprintf("Current timestamp(s) is %f\n", app.get_timestamp() / 1000000.0);

% transmit this classical CAN frame asynchrnously
com.transmit_can_async_verbose(c.FIdxChn, c.FIsRemote, c.FIsExtendedId, ...
    c.FDLC, c.FIdentifier, c.FDatas);

% retrieve application timestamp
app.wait(100);
fprintf("Current timestamp(s) is %f\n", app.get_timestamp() / 1000000.0);

% send periodically
com.add_cyclic_msg_can_verbose(c.FIdxChn, c.FIsExtendedId, c.FIdentifier, ...
    c.FDLC, c.FDatas, 100);
app.wait(1000);

% stop periodic messages
com.delete_cyclic_msgs();
app.wait(1000);

% unregister all events
unregisterallevents(com);

% disconnect application
app.disconnect();
app.log('closing application...', LVL_INFO);
 
% finalize library
fprintf("Script finalized\n");

% Arg. No.
% 1     Object Name
% 2     Event ID
% 3     Start of Event argument list
% end-2 End of event argument list (argument N)
% end-1 event structure
% end   event name
function OnRxCAN(varargin)
    global db
    % 1 * 13, varargin = {1¡Á1 Interface.comTSMaster_ITSCOM}    {[201]}    {' '}    {[0]}    {[0]}    {[0]}    {[0]}    {'}    {[273]}    {[224432829]}    {1¡Á8 uint8}    {1¡Á1 struct}    {'OnRxCAN'}
    s = ['CAN message received, Channel = %d, Id = 0x%3x, DLC = %d, Time = %f, Data = '  repmat('%2x ', 1, 8) '\n'];
    fprintf(s, varargin{4}, varargin{9}, varargin{8}, single(varargin{10})/1000000.0, varargin{11});
    if varargin{9} == hex2dec('64')
        d8 = varargin{11};
        s = '';
        for i = 1 : 8
            s = [s, num2str(d8(i))];
            if i < 8
                s = [s, ','];
            end
        end        
        v = db.get_signal_value_can_verbose(0, s, 'EngineData', 'EngSpeed');
        fprintf("EngineData.EngSpeed = %f\n", v);        
    end
end

function OnRxCANFD(varargin)
    % 1 * 15, varargin = {1¡Á1 Interface.comTSMaster_ITSCOM}    {[202]}    {' '}    {[0]}    {[0]}    {[0]}    {[1]}    {[0]}    {[0]}    {'}    {[273]}    {[217054228]}    {1¡Á64 uint8}    {1¡Á1 struct}    {'OnRxCANFD'}
    s = ['CAN FD message received, Channel = %d, Id = 0x%3x, DLC = %d, Time = %f, Data = '  repmat('%2x ', 1, 64) '\n'];
    fprintf(s, varargin{4}, varargin{11}, varargin{10}, single(varargin{12})/1000000.0, varargin{13});
end

function OnRxLIN(varargin)
    % 1 * 12, varargin = {1¡Á1 Interface.comTSMaster_ITSCOM}    {[201]}    {' '}    {[0]}    {[0]}    {[0]}    {'}    {[273]}    {[224432829]}    {1¡Á8 uint8}    {1¡Á1 struct}    {'OnRxLIN'}
    s = ['LIN message received, Channel = %d, Id = 0x%3x, DLC = %d, Time = %f, Data = '  repmat('%2x ', 1, 8) '\n'];
    fprintf(s, varargin{4}, varargin{8}, varargin{7}, single(varargin{9})/1000000.0, varargin{10});
end


