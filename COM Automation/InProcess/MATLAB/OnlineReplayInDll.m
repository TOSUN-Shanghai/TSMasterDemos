APP_CAN                       =0    ;
APP_LIN                       =1    ;
BUS_UNKNOWN_TYPE              =0    ;
TS_TCP_DEVICE                 =1    ;
TS_USB_DEVICE                 =3    ;
XL_USB_DEVICE                 =2    ;
cbsAllErrorFrame              =11   ;
cbsAllExtData                 =5    ;
cbsAllExtRemote               =9    ;
cbsAllStdData                 =3    ;
cbsAllStdRemote               =7    ;
cbsBusLoad                    =0    ;
cbsFpsErrorFrame              =10   ;
cbsFpsExtData                 =4    ;
cbsFpsExtRemote               =8    ;
cbsFpsStdData                 =2    ;
cbsFpsStdRemote               =6    ;
cbsPeakLoad                   =1    ;
lfdmACKOff                    =1    ;
lfdmNormal                    =0    ;
lfdmRestricted                =2    ;
lfdtCAN                       =0    ;
lfdtISOCAN                    =1    ;
lfdtNonISOCAN                 =2    ;
orsCompleted                  =3    ;
orsNotStarted                 =0    ;
orsPaused                     =2    ;
orsRunning                    =1    ;
orsTerminated                 =4    ;
ortAsLog                      =1    ;
ortDelayed                    =2    ;
ortImmediately                =0    ;
LVL_ERROR                     = 1   ;
LVL_WARNING                   = 2   ;
LVL_OK                        = 3   ;
LVL_HINT                      = 4   ;
LVL_INFO                      = 5   ;
LVL_VERBOSE                   = 6   ;

APP_NAME = "TestCOMTSMaster";
USE_XL_VIRTUAL_DEVICE = false;
USE_XL_VN1630_DEVICE = false;
USE_XL_VN1640_DEVICE = false;
USE_TS_VIRTUAL_DEVICE = true;
USE_TS_CANMINI_DEVICE = false;

fprintf('Script started\n');

% retrieve TSMaster application management
app = actxserver('comTSMaster.TSApplication');
app.disconnect();

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

% retrieve application timestamp
fprintf("Current timestamp(s) is %f\n", app.get_timestamp() / 1000000.0);

% retrieve tslog to perform online replay
tslog = app.TSLog();
% delete all engines
tslog.del_online_replay_configs();
% create one engine from file
i = tslog.add_online_replay_config('..\..\..\Data\Demo\Logs\CANSystem_CAN2.blf');
% configure the newly added engine if needed
tslog.set_online_replay_config(i, 'Replay1', '..\..\..\Data\Demo\Logs\CANSystem_CAN2.blf', false, false, ortImmediately, 0, true, true, '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32');
% check the replay status - not running
[stat, percent100] = tslog.get_online_replay_status(i);
% display the replay progress
fprintf('Current online replay status is %s, percentage is %f%%\n', stat, percent100);
% start online replay of current engine
tslog.start_online_replay(i);
% wait some time for eg. 500ms
app.wait(500);
% check the replay status - running
[stat, percent100] = tslog.get_online_replay_status(i);
% display the replay progress
fprintf('Current online replay status is %s, percentage is %f%%\n', stat, percent100);
% wait some time for log replay update
app.wait(10000);
% you can pause the replay if needed
tslog.pause_online_replay(i);
fprintf('Current replay is paused\n')
% check the replay status again
[stat, percent100] = tslog.get_online_replay_status(i);
% display the replay progress - paused
fprintf('Current online replay status is %s, percentage is %f%%\n', stat, percent100);
% you can resume the replay using the same "start_online_replay" command
tslog.start_online_replay(i);
fprintf('Current replay is resumed\n');
% wait some time for eg. 5000ms for the log replay complete
app.wait(5000);
% check the replay status again
[stat, percent100] = tslog.get_online_replay_status(i);
% display the replay progress - completed
fprintf('Current online replay status is %s, percentage is %f%%\n', stat, percent100);
% stop the replay
tslog.stop_online_replay(i);

% disconnect application
app.disconnect();
app.log('closing application...', LVL_INFO);
 
% finalize library
fprintf("Script finalized\n");
