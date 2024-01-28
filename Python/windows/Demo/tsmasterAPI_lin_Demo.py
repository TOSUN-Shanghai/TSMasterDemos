'''
Author: seven 865762826@qq.com
Date: 2023-03-24 11:22:42
LastEditors: seven 865762826@qq.com
LastEditTime: 2023-05-06 16:47:33
FilePath: \TSMasterAPI\TSMasterApi\demo\tsmasterAPI_lin_Demo.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from TSMasterAPI import *
import time

LINmsg = TLIBLIN()
LINmsg.FIdxChn = 0
LINmsg.FProperties = 1  # 1：表示发送 0：表示接收
LINmsg.FDLC = 8
LINmsg.FIdentifier = 0x3c
FData1 = [0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17]
for i in range(len(FData1)):
    LINmsg.FData[i] = FData1[i]
count = 0


def On_LIN_EVENT(OBJ, ACAN):
    global count
    if 1:
        print("回调接收成功", ACAN.contents.FIdentifier)
        for i in ACAN.contents.FData:
            print('%#x' % i, end=' ')
            count += 1
            if (count % len(ACAN.contents.FData) == 0):
                print(end='\n')


OnLINevent = TLINQueueEvent_Win32(On_LIN_EVENT)
obj1 = c_int32(0)

AppName = b'TSMaster_lin'
def connect():
    # 初始化函数，所需所有函数调用的接口
    initialize_lib_tsmaster(AppName)
    # 设置can通道数
    if (tsapp_set_can_channel_count(0) == 0):
        print("CAN通道设置成功")
    else:
        print("CAN通道设置失败")
    # 设置lin通道数
    if (tsapp_set_lin_channel_count(1) == 0):
        print("LIN通道设置成功")
    else:
        print("LIN通道设置失败")
    # 硬件通道映射至软件通道
    if 0 == tsapp_set_mapping_verbose(AppName, TLIBApplicationChannelType.APP_LIN, CHANNEL_INDEX.CHN1,
                                      "TC1026".encode("UTF8"), TLIBBusToolDeviceType.TS_USB_DEVICE,
                                      TLIB_TS_Device_Sub_Type.TC1016,0, 0, True):
        print("1通道映射成功")
    else:
        print("1通道映射失败")
    if 0 == tsapp_configure_baudrate_lin(CHANNEL_INDEX.CHN1, 19.2, TLINProtocol.LIN_PROTOCL_21):
        print("LIN波特率成功")
    else:
        print("LIN波特率失败")

    if 0 == tsapp_register_event_lin(obj1, OnLINevent):
        print("注冊LIN成功")
    if 0 == tsapp_connect():
        print("LIN工具连接成功")
        # 硬件开启成功后，开启fifo接收
        tsfifo_enable_receive_fifo()
        tslin_set_node_functiontype(CHANNEL_INDEX.CHN1, TLINNodeType.T_MasterNode)
    else:
        print("LIN工具连接失败")


def send_LIN_message():
    tsapp_transmit_lin_async(LINmsg)
    TLIN1 = TLIBLIN(FProperties=0)
    # r = tsapp_transmit_header_and_receive_msg(CHANNEL_INDEX.CHN1, 0X3D, 8, TLIN1, c_int(20))

    # listLINmsg = (TLIBLIN*100)
    # size = c_uint32(100)
    # r = tsapp_receive_lin_msgs(listLINmsg, size, CHANNEL_INDEX.CHN1,False)
    # if r == 0:
    #     print("LIN发送接收成功")
    # else:
    #     print(r)
    # #     # print(size)


if __name__ == '__main__':
    connect()
    send_LIN_message()
    finalize_lib_tsmaster()
