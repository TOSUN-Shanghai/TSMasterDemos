    #!/usr/bin/env python
# @Time   :2022/7/10 11:10
# @Author :SEVEN
# @File   :TSMater.py
# @Comment:use func with TSMaster.dll
# ------------------------------------------------

from TSMasterAPI import *
import time

initialize_lib_tsmaster("TSMaster_demo".encode("utf8"))
tsapp_set_can_channel_count(1)
tsapp_set_lin_channel_count(0)
# tosun其他硬件只需修改第6个参数，找到对应型号即可
tsapp_set_mapping_verbose("TSMaster_demo".encode("utf8"), TLIBApplicationChannelType.APP_CAN,
                          CHANNEL_INDEX.CHN1,
                          "TC1016".encode("utf8"), TLIBBusToolDeviceType.TS_USB_DEVICE,
                          TLIB_TS_Device_Sub_Type.TC1016,0, CHANNEL_INDEX.CHN1, True)
tsapp_configure_baudrate_canfd(CHANNEL_INDEX.CHN1, 500, 2000, TLIBCANFDControllerType.lfdtISOCAN,
                               TLIBCANFDControllerMode.lfdmNormal, True)

if 0 == tsapp_connect():
    print("successful")
    tsfifo_enable_receive_fifo()

idHandle = c_int32(0)
udsHandle = s32(0)

if 0 == tsdiag_can_create(udsHandle, CHANNEL_INDEX.CHN1, 0, 8, 0x1, True, 0X2, True, 0X3, True):
    print("UDS_SUCCESSFUL,udsHandle = ", udsHandle)

AReqDataArray = (c_uint8 * 100)()
AReqDataArray[0] = c_uint8(0x22)
AReqDataArray[1] = c_uint8(0xf1)
AReqDataArray[2] = c_uint8(0x90)
AResSize = c_int(10000)
AResponseDataArray = (c_uint8 * 10000)()

for i in range(10):
    r = tstp_can_request_and_get_response(udsHandle, AReqDataArray, 3, AResponseDataArray, AResSize)
    print(AResSize.value)
    for i in range(AResSize.value):
        print(hex(AResponseDataArray[i]), end="  ")
        if i == AResSize.value - 1:
            print(end='\n')

finalize_lib_tsmaster()
