'''
Author: seven 865762826@qq.com
Date: 2023-03-24 11:22:42
LastEditors: seven 865762826@qq.com
LastEditTime: 2023-05-06 16:46:41
'''
from TSMasterAPI import *
import libTOSUN

# 回调函数 CAN发送接收事件
def On_CAN_EVENT(OBJ, ACAN):
    print("can_id:", ACAN.contents.FIdentifier, "can报文时间", ACAN.contents.FTimeUs / 1000000)


# 回调函数 CANFD发送接收事件
def On_CANFD_EVENT(OBJ, ACANFD):
    if ACANFD.contents.FFDProperties == 1:
        print("canfd_id:", ACANFD.contents.FIdentifier, "canfd报文时间", ACANFD.contents.FTimeUs / 1000000)


# 预发送事件 CAN预发送事件
def On_CAN_pre_EVENT(OBJ, ACAN):
    # 报文ID为0x100，第一字节将一直为0xFF
    if ACAN.contents.FIdentifier == 0x100:
        ACAN.contents.FData[0] = 0xff

def On_CANFD_pre_EVENT(OBJ, ACANFD):
    # 报文ID为0x101，第一字节将一直为0xFF
    if ACANFD.contents.FIdentifier == 0x101:
        ACANFD.contents.FData[0] = 0xff

# 函数指针
OnCANevent = OnTx_RxFUNC_CAN(On_CAN_EVENT)
OnCANFDevent = OnTx_RxFUNC_CANFD(On_CANFD_EVENT)
OnCANpreEVENT = OnTx_RxFUNC_CAN(On_CAN_pre_EVENT)
OnCANFDpreEVENT = OnTx_RxFUNC_CANFD(On_CANFD_pre_EVENT)

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
tsapp_configure_baudrate_canfd(CHANNEL_INDEX.CHN1, 500, 2000, TLIBCANFDControllerType.lfdtISOCAN,
                               TLIBCANFDControllerMode.lfdmNormal, True)
obj1 = c_int32(0)
obj2 = c_int32(0)
obj3 = c_int32(0)
obj4 = c_int32(0)
if 0 == tsapp_connect():
    print("successful")
    # 注册回调事件 接收发送事件  预发送事件
    if 0 == tsapp_register_event_can(obj1, OnCANevent) and 0 == tsapp_register_event_canfd(obj2, OnCANFDevent) and \
            0 == tsapp_register_pretx_event_can(obj3,OnCANpreEVENT) and 0 == tsapp_register_pretx_event_canfd(obj4,OnCANFDpreEVENT):
        print("回调事件注册成功")
    else:
        print("回调事件注册失败")

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

tsapp_disconnect()

finalize_lib_tsmaster()
