import win32com.client
import pythoncom
import win32api
import time
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
	
APP_NAME = "TestCOMTSMaster"
USE_XL_VIRTUAL_DEVICE = False
USE_XL_VN1630_DEVICE = False
USE_XL_VN1640_DEVICE = False
USE_TS_VIRTUAL_DEVICE = True
USE_TS_CANMINI_DEVICE = False

class TSMasterEvents:
	def OnRxCAN(self, AIdxChn, AIsTx, AIsRemote, AIsExtended, AIsError, ADLC, AIdentifier, ATimeUs, ADatas):
		print("CAN message received:", AIdxChn, AIdentifier, ADLC, ATimeUs/1000000.0, [ADatas[0], ADatas[1], ADatas[2], ADatas[3], ADatas[4], ADatas[5], ADatas[6], ADatas[7]])
	def OnRxCANFD(self, AIdxChn, AIsTx, AIsExtended, AIsError, AIsEDL, AIsBRS, AIsESI, ADLC, AIdentifier, ATimeUs, ADatas):
		if AIsEDL:
			print("CAN FD message received:", AIdxChn, AIdentifier, ADLC, ATimeUs/1000000.0, [ADatas[0], ADatas[1], ADatas[2], ADatas[3], ADatas[4], ADatas[5], ADatas[6], ADatas[7], ADatas[8], ADatas[9], ADatas[10], ADatas[11], ADatas[12], ADatas[13], ADatas[14], ADatas[15], ADatas[16], ADatas[17], ADatas[18], ADatas[19], ADatas[20], ADatas[21], ADatas[22], ADatas[23], ADatas[24], ADatas[25], ADatas[26], ADatas[27], ADatas[28], ADatas[29], ADatas[30], ADatas[31], ADatas[32], ADatas[33], ADatas[34], ADatas[35], ADatas[36], ADatas[37], ADatas[38], ADatas[39], ADatas[40], ADatas[41], ADatas[42], ADatas[43], ADatas[44], ADatas[45], ADatas[46], ADatas[47], ADatas[48], ADatas[49], ADatas[50], ADatas[51], ADatas[52], ADatas[53], ADatas[54], ADatas[55], ADatas[56], ADatas[57], ADatas[58], ADatas[59], ADatas[60], ADatas[61], ADatas[62], ADatas[63]])
		else:
			print("CAN message received:", AIdxChn, AIdentifier, ADLC, ATimeUs/1000000.0, [ADatas[0], ADatas[1], ADatas[2], ADatas[3], ADatas[4], ADatas[5], ADatas[6], ADatas[7]])
	def OnRxLIN(self, AIdxChn, AIsTx, AIsError, ADLC, AIdentifier, AChecksum, ATimeUs, ADatas):
		print("LIN message received:")
	
print("Script started")

# retrieve TSMaster application management
#pythoncom.CoInitialize() # enable multithread
app = win32com.client.Dispatch("comTSMaster.TSApplication")

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

# get communication object
com = app.TSCOM()
win32com.client.WithEvents(com, TSMasterEvents)

# enable CAN message reception event, select only one entry from CAN and CAN FD events
com.enable_bus_statistics(True);
com.enable_event_can(True)
com.enable_event_canfd(False)

# init a TCAN record for CAN message transmission
c = win32com.client.Record("TCAN", app)
c.FIdxChn = 0
c.FIsExtendedId = 0
c.FIsRemote = False
c.FIdentifier = 0x123
c.FDLC = 8
c.FDatas = VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_I1, [1, 2, 3, 4, 5, 6, 7, 8])

# transmit this classical CAN frame asynchrnously
com.transmit_can_async(c)

# retrieve application timestamp
app.wait(100)
print("Current timestamp(s) is", app.get_timestamp() / 1000000.0)

# enable CAN FD message reception event, select only one entry from CAN and CAN FD events
com.enable_event_can(False)
com.enable_event_canfd(True)

# init a TCANFD record for CAN FD message transmission
cFD = win32com.client.Record("TCANFD", app)
cFD.FIdxChn = 0
cFD.FIsExtendedId = 0
cFD.FIsEDL = True
cFD.FIsBRS = True
cFD.FIsESI = False
cFD.FIdentifier = 0x345
cFD.FDLC = 15
cFD.FDatas = VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_I1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64])

# transmit this CAN FD frame asynchrnously
com.transmit_canfd_async(cFD)

# retrieve application timestamp
app.wait(100)
print("Current timestamp(s) is", app.get_timestamp() / 1000000.0)

# send periodically
com.add_cyclic_msg_can(c, 100)
com.add_cyclic_msg_canfd(cFD, 100)
app.wait(1000)

# update message data
app.log('updating message data...', constants.LVL_OK)
c.FDatas = VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_I1, [8, 7, 6, 5, 4, 3, 2, 1])
cFD.FDatas = VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_I1, [8, 7, 6, 5, 4, 3, 2, 1, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 8, 7, 6, 5, 4, 3, 2, 1])
com.add_cyclic_msg_can(c, 100)
com.add_cyclic_msg_canfd(cFD, 100)
app.wait(1000)

# stop periodic messages
com.delete_cyclic_msgs()
app.wait(1000)

r, s = app.get_system_var_generic('Application.Connected');
if r:
   print('Application.Connected = ' + s)
   
# disconnect application
app.log('closing application...', constants.LVL_INFO)
app.disconnect()

r, s = app.get_system_var_generic('Application.Connected');
if r:
   print('Application.Connected = ' + s)

# finalize library
app = None
print("Script finalized")
#input("press any key to continue...")
