import win32com.client
import pythoncom
import win32api
import time
import os
from win32com.client import VARIANT

class constants:
	APP_CAN                       = 0          # from enum TTSAppChannelType
	APP_LIN                       = 1          # from enum TTSAppChannelType
	BUS_UNKNOWN_TYPE              = 0          # from enum TTSBusToolDeviceType
	TS_TCP_DEVICE                 = 1          # from enum TTSBusToolDeviceType
	TS_USB_DEVICE                 = 3          # from enum TTSBusToolDeviceType
	XL_USB_DEVICE                 = 2          # from enum TTSBusToolDeviceType
	lfdmACKOff                    = 1          # from enum TTSCANFDControllerMode
	lfdmNormal                    = 0          # from enum TTSCANFDControllerMode
	lfdmRestricted                = 2          # from enum TTSCANFDControllerMode
	lfdtCAN                       = 0          # from enum TTSCANFDControllerType
	lfdtISOCAN                    = 1          # from enum TTSCANFDControllerType
	lfdtNonISOCAN                 = 2          # from enum TTSCANFDControllerType
	LVL_ERROR                     = 1
	LVL_WARNING                   = 2
	LVL_OK                        = 3
	LVL_HINT                      = 4
	LVL_INFO                      = 5
	LVL_VERBOSE                   = 6
	
APP_NAME = "TSMaster"
USE_XL_VIRTUAL_DEVICE = False
USE_XL_VN1630_DEVICE = False
USE_XL_VN1640_DEVICE = False
USE_TS_VIRTUAL_DEVICE = True
USE_TS_CANMINI_DEVICE = False

# retrieve TSMaster application management
#pythoncom.CoInitialize() # enable multithread
app = win32com.client.Dispatch("TSMaster.TSApplication")
com = app.TSCOM() # win32com.client.Dispatch("TSMaster.TSCOM")
formMan = app.TSFormManager()
formMan.show_main_form()

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

# init a TCAN record for CAN message transmission
c = win32com.client.Record("TCAN", app)
c.FIdxChn = 0
c.FIsExtendedId = 0
c.FIsRemote = True
c.FIdentifier = 0x123
c.FDLC = 8
c.FDatas = VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_I1, [1, 2, 3, 4, 5, 6, 7, 8])

# get mini program manager
mp = app.TSMP()

# unload all mini programs from TSMaster
mp.unload_all_mps()

# load excel mini program
mp.load_mp(r'.\Data\MPLibraries\Excel\mExcel.mp')
print('Mini program list:', mp.get_mp_list())
print('Mini program "mExcel.mp" function list:', mp.get_mp_function_list('mExcel.mp'))
print('Mini program "mExcel.mp" function "load" prototype:', mp.get_mp_function_prototype('mexcel.mp', 'load'))

mp.dynamic_invoke('mExcel.mp', 'load', r'.\Demo\Excels\ExcelDemo.xlsx')

s = mp.dynamic_invoke('mExcel.mp', 'get_sheet_count', '')
print("excel sheet count =", s);

s = mp.dynamic_invoke('mExcel.mp', 'get_sheet_name', '0')
print("excel first sheet count =", s);

s = mp.dynamic_invoke('mExcel.mp', 'get_cell_count', '0')
ss = s.split(',')
rowCnt = int(ss[0])
colCnt = int(ss[1])
print('excel first sheet row count =', rowCnt, ', column count =', colCnt);

s = mp.dynamic_invoke('mExcel.mp', 'get_cell_value', '0,2,1')
print("excel first sheet row = 2, col = 1, value =", s);

# loop through excel first sheet, column 0, to send out each frame as remote frame
for i in range(rowCnt):
    s = mp.dynamic_invoke('mExcel.mp', 'get_cell_value', '0,' + str(i) + ',0')
    c.FIdentifier = int(s)
    # transmit this classical CAN frame asynchrnously
    com.transmit_can_async(c)
    app.wait(100)

# disconnect application
app.disconnect()
app.log('closing application...', constants.LVL_INFO)

# finalize library
app = None
print("Script finalized")
