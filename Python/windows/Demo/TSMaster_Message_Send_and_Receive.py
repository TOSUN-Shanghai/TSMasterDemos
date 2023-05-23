from TSMasterAPI import *
import time

# 初始化函数，调用TsMaster.dll 必须先调用初始化函数，否则其他函数无法使用
initialize_lib_tsmaster("TSMaster_demo".encode("utf8"))
# 设置CAN通道
tsapp_set_can_channel_count(1)
# 设置LIN通道数 默认为0  但是还是建议调用函数来设置LIN通道为0
tsapp_set_lin_channel_count(0)

# 此处将TC1016的1通道绑定至软件1通道
# tosun其他硬件只需修改第6个参数，找到对应型号即可
tsapp_set_mapping_verbose("TSMaster_demo".encode("utf8"), TLIBApplicationChannelType.APP_CAN,
                          CHANNEL_INDEX.CHN1,
                          "TC1016".encode("utf8"), TLIBBusToolDeviceType.TS_USB_DEVICE,
                          TLIB_TS_Device_Sub_Type.TC1016,0, CHANNEL_INDEX.CHN1, True)

# 设置1通道波特率
tsapp_configure_baudrate_canfd(CHANNEL_INDEX.CHN1, 500, 2000, TLIBCANFDControllerType.lfdtISOCAN ,
                               TLIBCANFDControllerMode.lfdmNormal, True)

if 0 == tsapp_connect():
    # 开启fifo功能才能使用receive接收函数
    tsfifo_enable_receive_fifo()
    print("successful")

# 发送报文
TCAN1 = TLIBCAN(FIdentifier=0x100, FData=[0, 1, 2, 3, 4, 5, 6, 7])
# 发送CAN报文 （单帧发送 周期发送）
tsapp_transmit_can_async(TCAN1)
tsapp_add_cyclic_msg_can(TCAN1, 10)

# 发送CANFD报文 （单帧发送 周期发送）
TCANFD1 = TLIBCANFD(FIdentifier=0x101, FData=[0, 1, 2, 3, 4, 5, 6, 7])
tsapp_transmit_canfd_async(TCANFD1)
tsapp_add_cyclic_msg_canfd(TCANFD1, 10)

time.sleep(2)
tsapp_delete_cyclic_msgs()

cansize = c_int32(10000)

listcanmsg = (TLIBCAN * 10000)()

r = tsfifo_receive_can_msgs(listcanmsg, cansize, 0, READ_TX_RX_DEF.TX_RX_MESSAGES)
if r == 0:
    for i in range(cansize.value):
        print("canid:", listcanmsg[i].FIdentifier, "can报文时间", listcanmsg[i].FTimeUs / 1000000)

canfdsize = c_int32(10000)
listcanfdmsg = (TLIBCANFD * 10000)()

r = tsfifo_receive_canfd_msgs(listcanfdmsg, canfdsize, 0, READ_TX_RX_DEF.TX_RX_MESSAGES)
if r == 0:
    for i in range(canfdsize.value):
        if listcanfdmsg[i].FFDProperties == 1: #canfd接收会包含can报文, 所以在此处加一个判断 改属性为1表示为CANFD 0表示为CAN
            print("canfdid:", listcanfdmsg[i].FIdentifier, "canfd报文时间", listcanfdmsg[i].FTimeUs / 1000000)

tsapp_disconnect()

finalize_lib_tsmaster()
