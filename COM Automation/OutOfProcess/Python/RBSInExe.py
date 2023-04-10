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

APP_NAME = "TSMaster"
USE_XL_VIRTUAL_DEVICE = False
USE_XL_VN1630_DEVICE = False
USE_XL_VN1640_DEVICE = False
USE_TS_VIRTUAL_DEVICE = True
USE_TS_CANMINI_DEVICE = False

print("Script started")

# retrieve TSMaster application management
#pythoncom.CoInitialize() # enable multithread
app = win32com.client.Dispatch("TSMaster.TSApplication")
app.disconnect()
formMan = app.TSFormManager()
formMan.show_main_form()
formMan.load_project(r'.\Data\SDK\examples\COM Automation\Configurations\RBSDemo.T7z', True)

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
r.FHWDeviceName = "Virtual"
r.FMappingDisabled = False
app.set_mapping(r)

# map application channel 2 to hw index 0, channel 1 of Vector virtual channel
r.FAppChannelIndex = 1
r.FHWChannelIndex = 1
app.set_mapping(r)

# print application CAN channel mappings
print("Application CAN channel 1 mapping to:", app.get_mapping(constants.APP_CAN, 0))
print("Application CAN channel 2 mapping to:", app.get_mapping(constants.APP_CAN, 1))

# configure CAN channel baudrates before connection: Arb = 500K, Data = 2M
app.configure_baudrate_canfd(0, 500, 2000, constants.lfdtISOCAN, constants.lfdmNormal, True)
app.configure_baudrate_canfd(1, 500, 2000, constants.lfdtISOCAN, constants.lfdmNormal, True)

# connect application
app.log('connecting application...', constants.LVL_HINT)
app.connect()

# retrieve application timestamp
print("Current timestamp(s) is", app.get_timestamp() / 1000000.0)

com = app.TSCOM()
com.can_rbs_start()

com.can_rbs_set_signal_value_by_address(r'0/CAN_FD_Powertrain/Engine/EngineData/EngSpeed', 1234.56);
com.can_rbs_set_signal_value_by_address(r'0/CAN_FD_Powertrain/Engine/EngineData/Gear', 1);
time.sleep(1)
com.can_rbs_set_signal_value_by_address(r'0/CAN_FD_Powertrain/Engine/EngineData/EngSpeed', 3456.56);
com.can_rbs_set_signal_value_by_address(r'0/CAN_FD_Powertrain/Engine/EngineData/Gear', 3);
time.sleep(1)
com.can_rbs_set_signal_value_by_address(r'0/CAN_FD_Powertrain/Engine/EngineData/EngSpeed', 4567.56);
com.can_rbs_set_signal_value_by_address(r'0/CAN_FD_Powertrain/Engine/EngineData/Gear', 5);
time.sleep(1)

d = com.can_rbs_get_signal_value_by_address(r'0/CAN_FD_Powertrain/Engine/EngineData/EngSpeed');
print("EngSpeed is", d)
d = com.can_rbs_get_signal_value_by_address(r'0/CAN_FD_Powertrain/Engine/EngineData/Gear');
print("Gear is", d)
time.sleep(1)

# disconnect application
app.log('closing application...', constants.LVL_INFO)
app.disconnect()

# finalize library
app = None
print("Script finalized")
#input("press any key to continue...")
