from TSMasterAPI import *

_curr_path = os.path.dirname(__file__)
# 本示例基于TC1016
ProjectName = "TSMaster_signal".encode("utf8")
# 初始化
initialize_lib_tsmaster(ProjectName)

key = 0


def On_pre_CANFD_EVENT(OBJ, ACANFD):
    # print(ACANFD.contents.FIdentifier)
    # print(key)
    if ACANFD.contents.FIdentifier == 0x3FC:
        if key == 0:
            tsdb_set_signal_value_canfd(ACANFD.contents, "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                        c_double(10.0))
        elif key == 1:
            tsdb_set_signal_value_canfd(ACANFD.contents, "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                        c_double(10.0))
        elif key == 2:
            tsdb_set_signal_value_canfd(ACANFD.contents, "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                        c_double(20.0))

        elif key == 3:
            tsdb_set_signal_value_canfd(ACANFD.contents, "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                        c_double(30.0))
        elif key == 4:
            tsdb_set_signal_value_canfd(ACANFD.contents, "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                        c_double(40.0))
        elif key == 5:
            tsdb_set_signal_value_canfd(ACANFD.contents, "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                        c_double(50.0))
        elif key == 6:
            tsdb_set_signal_value_canfd(ACANFD.contents, "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                        c_double(60.0))
        elif key == 7:
            tsdb_set_signal_value_canfd(ACANFD.contents, "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                        c_double(70.0))
        elif key == 8:
            tsdb_set_signal_value_canfd(ACANFD.contents, "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                        c_double(80.0))
        else:
            tsdb_set_signal_value_canfd(ACANFD.contents, "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                        c_double(0.0))

signalvalue = c_double(0)
# 回调函数 CANFD发送接收事件
def On_CANFD_EVENT(OBJ, ACANFD):
    if ACANFD.contents.FFDProperties == 1 and ACANFD.contents.FIdentifier == 0X160:

        tsdb_get_signal_value_canfd(ACANFD.contents, "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                    signalvalue)



obj = c_int32(0)

Pre_CANFD_EVENT = TCANFDQueueEvent_Win32(On_pre_CANFD_EVENT)
CANFD_EVENT = TCANFDQueueEvent_Win32(On_CANFD_EVENT)

dbchandle = c_int32(0)


def connect():
    tsdb_load_can_db((_curr_path+"/CAN_FD_Powertrain.dbc").encode('utf8'), "0,1".encode('utf8'), dbchandle)
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
    ret = tsapp_connect()
    if ret == 0:
        print("连接成功")
        if 0 == tsapp_register_pretx_event_canfd(obj, Pre_CANFD_EVENT) and 0 == tsapp_register_event_canfd(obj, CANFD_EVENT):
            print("预发送事件注册成功")
        CANFD_160 = TLIBCANFD()
        CANFD_160.FIdxChn = 0
        CANFD_160.FIdentifier = 0X160
        CANFD_160.FProperties = 1
        CANFD_160.FFDProperties = 1
        CANFD_160.FDLC = 15
        tsapp_add_cyclic_msg_canfd(CANFD_160, 10)
    else:
        error_code = c_char_p()
        tsapp_get_error_description(ret,error_code)
        print(error_code.value)


if __name__ == "__main__":
    connect()
    while True:
        keys = input("请输入key值")
        if keys == "1":
            key += 1
            print(signalvalue)
        elif keys == "2":
            key -= 1
            print(signalvalue)
        elif keys == "q":
            break
    finalize_lib_tsmaster()
