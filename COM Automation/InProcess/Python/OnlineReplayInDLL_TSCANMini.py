import win32com.client
import pythoncom
import win32api
import time
from win32com.client import VARIANT

class constants:
	APP_CAN                       =0          # from enum TTSAppChannelType
	APP_LIN                       =1          # from enum TTSAppChannelType
	BUS_UNKNOWN_TYPE              =0          # from enum TTSBusToolDeviceType
	TS_TCP_DEVICE                 =1          # from enum TTSBusToolDeviceType
	TS_USB_DEVICE                 =3          # from enum TTSBusToolDeviceType
	XL_USB_DEVICE                 =2          # from enum TTSBusToolDeviceType
	cbsAllErrorFrame              =11         # from enum TTSCANBusStatistics
	cbsAllExtData                 =5          # from enum TTSCANBusStatistics
	cbsAllExtRemote               =9          # from enum TTSCANBusStatistics
	cbsAllStdData                 =3          # from enum TTSCANBusStatistics
	cbsAllStdRemote               =7          # from enum TTSCANBusStatistics
	cbsBusLoad                    =0          # from enum TTSCANBusStatistics
	cbsFpsErrorFrame              =10         # from enum TTSCANBusStatistics
	cbsFpsExtData                 =4          # from enum TTSCANBusStatistics
	cbsFpsExtRemote               =8          # from enum TTSCANBusStatistics
	cbsFpsStdData                 =2          # from enum TTSCANBusStatistics
	cbsFpsStdRemote               =6          # from enum TTSCANBusStatistics
	cbsPeakLoad                   =1          # from enum TTSCANBusStatistics
	lfdmACKOff                    =1          # from enum TTSCANFDControllerMode
	lfdmNormal                    =0          # from enum TTSCANFDControllerMode
	lfdmRestricted                =2          # from enum TTSCANFDControllerMode
	lfdtCAN                       =0          # from enum TTSCANFDControllerType
	lfdtISOCAN                    =1          # from enum TTSCANFDControllerType
	lfdtNonISOCAN                 =2          # from enum TTSCANFDControllerType
	orsCompleted                  =3          # from enum TTSOnlineReplayStatus
	orsNotStarted                 =0          # from enum TTSOnlineReplayStatus
	orsPaused                     =2          # from enum TTSOnlineReplayStatus
	orsRunning                    =1          # from enum TTSOnlineReplayStatus
	orsTerminated                 =4          # from enum TTSOnlineReplayStatus
	ortAsLog                      =1          # from enum TTSOnlineReplayTimingMode
	ortDelayed                    =2          # from enum TTSOnlineReplayTimingMode
	ortImmediately                =0          # from enum TTSOnlineReplayTimingMode
	LVL_ERROR                     = 1
	LVL_WARNING                   = 2
	LVL_OK                        = 3
	LVL_HINT                      = 4
	LVL_INFO                      = 5
	LVL_VERBOSE                   = 6
	LogStatus = ['Not started', 'Running', 'Paused', 'Completed', 'Terminated']

APP_NAME = "TestCOMTSMaster"
USE_XL_VIRTUAL_DEVICE = False
USE_XL_VN1630_DEVICE = False
USE_XL_VN1640_DEVICE = False
USE_TS_VIRTUAL_DEVICE = False
USE_TS_CANMINI_DEVICE = True

print("Script started")

# retrieve TSMaster application management
#pythoncom.CoInitialize() # enable multithread
app = win32com.client.Dispatch("comTSMaster.TSApplication")
app.disconnect()

# set current application name
app.set_current_application(APP_NAME)
print("current application is:", app.get_current_application())

# get all application in a list separated by ";"
print("application list is:", app.get_application_list())

# set CAN channel count to 2
app.set_can_channel_count(2)

# set LIN channel count to 2
app.set_lin_channel_count(0)

# read CAN channel count
print("CAN channel count =", app.get_can_channel_count())

# read LIN channel count
print("LIN channel count =", app.get_lin_channel_count())

# delete mapping of application CAN channel 1 and 2
app.del_mapping(constants.APP_CAN, 0)
app.del_mapping(constants.APP_CAN, 1)

# map application channel 1 to hw index 0, channel 0 of Vector virtual channel
r = win32com.client.Record("TTSMapping", app)
r.FAppName = APP_NAME
r.FAppChannelIndex = 0
r.FAppChannelType = constants.APP_CAN
if USE_XL_VIRTUAL_DEVICE:
	r.FHWDeviceType = constants.XL_USB_DEVICE
	r.FHWDeviceSubType = 1
if USE_XL_VN1630_DEVICE:
	r.FHWDeviceType = constants.XL_USB_DEVICE
	r.FHWDeviceSubType = 57
if USE_XL_VN1640_DEVICE:
	r.FHWDeviceType = constants.XL_USB_DEVICE
	r.FHWDeviceSubType = 59
if USE_TS_VIRTUAL_DEVICE:
	r.FHWDeviceType = constants.TS_TCP_DEVICE
	r.FHWDeviceSubType = -1
if USE_TS_CANMINI_DEVICE:
	r.FHWDeviceType = constants.TS_USB_DEVICE
	r.FHWDeviceSubType = 3
r.FHWIndex = 0
r.FHWChannelIndex = 0
r.FHWDeviceName = "TSCANMini"
r.FMappingDisabled = False
app.set_mapping(r)

# map application channel 2 to hw index 0, channel 1 of Vector virtual channel
r.FHWIndex = 1
r.FAppChannelIndex = 1
r.FHWChannelIndex = 0
app.set_mapping(r)

# print application CAN channel mappings
print("Application CAN channel 1 mapping to:", app.get_mapping(constants.APP_CAN, 0))
print("Application CAN channel 2 mapping to:", app.get_mapping(constants.APP_CAN, 1))

# configure CAN channel baudrates before connection: Arb = 500K, Data = 2M
app.configure_baudrate_can(0, 500, False, True)
app.configure_baudrate_can(1, 500, False, True)

# connect application
app.log('connecting application...', constants.LVL_HINT)
app.connect()

# retrieve application timestamp
print("Current timestamp(s) is", app.get_timestamp() / 1000000.0)

# retrieve tslog to perform online replay
tslog = app.TSLog()
# delete all engines
tslog.del_online_replay_configs()
# create one engine from file
i = tslog.add_online_replay_config(r'..\..\..\Data\Demo\Logs\CANSystem_CAN2.blf')
# configure the newly added engine if needed
tslog.set_online_replay_config(i, 'Replay1', r'..\..\..\Data\Demo\Logs\CANSystem_CAN2.blf', False, False, constants.ortImmediately, 0, True, True, '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32')
# check the replay status - not running
stat, percent100 = tslog.get_online_replay_status(i)
# display the replay progress
print('Current online replay status is', constants.LogStatus[stat], ', percentage is', percent100, '%')
# start online replay of current engine
tslog.start_online_replay(i)
# wait some time for eg. 500ms
app.wait(500)
# check the replay status - running
stat, percent100 = tslog.get_online_replay_status(i)
# display the replay progress
print('Current online replay status is', constants.LogStatus[stat], ', percentage is', percent100, '%')
# wait some time for log replay update
app.wait(10000)
# you can pause the replay if needed
tslog.pause_online_replay(i)
print('Current replay is paused')
# check the replay status again
stat, percent100 = tslog.get_online_replay_status(i)
# display the replay progress - paused
print('Current online replay status is', constants.LogStatus[stat], ', percentage is', percent100, '%')
# you can resume the replay using the same "start_online_replay" command
tslog.start_online_replay(i)
print('Current replay is resumed')
# wait some time for eg. 5000ms for the log replay complete
app.wait(5000)
# check the replay status again
stat, percent100 = tslog.get_online_replay_status(i)
# display the replay progress - completed
print('Current online replay status is', constants.LogStatus[stat], ', percentage is', percent100, '%')
# stop the replay
tslog.stop_online_replay(i)

# disconnect application
app.log('closing application...', constants.LVL_INFO)
app.disconnect()

# finalize library
app = None
print("Script finalized")
#input("press any key to continue...")
