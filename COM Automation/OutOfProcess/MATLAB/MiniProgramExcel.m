
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

APP_NAME = "TSMaster";
USE_XL_VIRTUAL_DEVICE = false;
USE_XL_VN1630_DEVICE = false;
USE_XL_VN1640_DEVICE = false;
USE_TS_VIRTUAL_DEVICE = true;
USE_TS_CANMINI_DEVICE = false;

fprintf('Script started\n');

% retrieve TSMaster application management
app = actxserver('TSMaster.TSApplication');
app.disconnect();
formMan = app.TSFormManager();
formMan.show_main_form();

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

% connect application
app.log('connecting application...', LVL_HINT);
app.connect();

% get communication object
com = app.TSCOM();

% MATLAB will convert any single column matrix to a 1 dimensional array when passed to a COM object.
feature('COM_SafeArraySingleDim', 0);
feature('COM_PassSafeArrayByRef', 0);

% init a TCAN record for CAN message transmission
c.FIdxChn = 0;
c.FIsExtendedId = false;
c.FIsRemote = true;
c.FIdentifier = hex2dec('123');
c.FDLC = 8;
c.FDatas = '0, 5, 20, 3, 159, 52, 134, 1';

% get mini program manager
mp = app.TSMP();

% display function prototypes
invoke(mp)
events(mp)

% unload all mini programs from TSMaster
mp.unload_all_mps();

% load excel mini program
mp.load_mp('.\Data\MPLibraries\Excel\mExcel.mp');
fprintf('Mini program list: %s\n', mp.get_mp_list());
fprintf('Mini program "mExcel.mp" function list: %s\n', mp.get_mp_function_list('mExcel.mp'));
fprintf('Mini program "mExcel.mp" function "load" prototype: %s\n', mp.get_mp_function_prototype('mexcel.mp', 'load'));

mp.dynamic_invoke('mExcel.mp', 'load', '.\Data\Demo\Excels\ExcelDemo.xlsx');

s = mp.dynamic_invoke('mExcel.mp', 'get_sheet_count', '');
fprintf("excel sheet count = %s\n", s);

s = mp.dynamic_invoke('mExcel.mp', 'get_sheet_name', '0');
fprintf("excel first sheet count = %s\n", s);

s = mp.dynamic_invoke('mExcel.mp', 'get_cell_count', '0');
ss = split(s, ',');
rowCnt = str2num(ss{1});
colCnt = str2num(ss{2});
fprintf('excel first sheet row count = %d, column count = %d\n', rowCnt, colCnt);

s = mp.dynamic_invoke('mExcel.mp', 'get_cell_value', '0,2,1');
fprintf("excel first sheet row = 2, col = 1, value = %s\n", s);

% loop through excel first sheet, column 0, to send out each frame as remote frame
for i = 0 : rowCnt-1
    s = sprintf('0,%d,0', i); % '0,' + num2str(i) + ',0'
    s = mp.dynamic_invoke('mExcel.mp', 'get_cell_value', s);
    c.FIdentifier = str2num(s);
    % transmit this classical CAN frame asynchrnously
    com.transmit_can_async_verbose(c.FIdxChn, c.FIsRemote, c.FIsExtendedId, ...
    c.FDLC, c.FIdentifier, c.FDatas);
    app.wait(100);
end

% disconnect application
app.disconnect();
app.log('closing application...', LVL_INFO);
 
% finalize library
fprintf("Script finalized\n");
