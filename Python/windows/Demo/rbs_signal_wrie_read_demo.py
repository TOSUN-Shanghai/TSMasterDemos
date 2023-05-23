from TSMasterAPI import *


_curr_path = os.path.dirname(__file__)



ProjectName = "TSMaster_can".encode("utf8")
# 初始化
initialize_lib_tsmaster(ProjectName)
dbchandle = c_int32(0)

# 0/CAN_FD_Powertrain/Engine/GearBoxInfo/Gear
def connect():
    ret = tsdb_load_can_db(_curr_path+"/CAN_FD_Powertrain.dbc", "0,1", dbchandle)
    print(ret,dbchandle)
    # 设置can通道数
    if (tsapp_set_can_channel_count(2) == 0):
        print("CAN通道设置成功")
    else:
        print("CAN通道设置失败")
    # 设置lin通道数
    if (tsapp_set_lin_channel_count(0) == 0):
        print("CAN通道设置成功")
    else:
        print("CAN通道设置失败")

    # 硬件通道映射至软件通道
    if 0 == tsapp_set_mapping_verbose(ProjectName, TLIBApplicationChannelType.APP_CAN, CHANNEL_INDEX.CHN1,
                                      "TC1026".encode("UTF8"), TLIBBusToolDeviceType.TS_USB_DEVICE,
                                      TLIB_TS_Device_Sub_Type.TC1016,0, CHANNEL_INDEX.CHN1, True):
        print("1通道映射成功")
    else:
        print("1通道映射失败")
    if 0 == tsapp_set_mapping_verbose(ProjectName, TLIBApplicationChannelType.APP_CAN, CHANNEL_INDEX.CHN2,
                                      "TC1026".encode("UTF8"), TLIBBusToolDeviceType.TS_USB_DEVICE,
                                      TLIB_TS_Device_Sub_Type.TC1016, 0,CHANNEL_INDEX.CHN2, True):
        print("2通道映射成功")
    else:
        print("2通道映射失败")
    if 0 == tsapp_configure_baudrate_canfd(CHANNEL_INDEX.CHN1, 500,2000,TLIBCANFDControllerType.lfdtISOCAN,TLIBCANFDControllerMode.lfdmNormal,1)and 0 == tsapp_configure_baudrate_canfd(CHANNEL_INDEX.CHN2, 500,2000,TLIBCANFDControllerType.lfdtISOCAN,TLIBCANFDControllerMode.lfdmNormal,1):
        print("CAN波特率成功")
    else:
        print("CAN波特率失败")
    if 0 == tsapp_connect():
        print("CAN工具连接成功")
        # 硬件开启成功后，开启fifo接收
        tsfifo_enable_receive_fifo()
    else:
        print("LIN工具连接失败")


    ret = tsapp_connect()
    if ret == 0:
        print("连接成功")
        # 开启rbs功能
        ret = tscom_can_rbs_start()
        # 激活network
        tscom_can_rbs_activate_network_by_name(0, True, b"CAN_FD_Powertrain", False)
        # 激活节点
        tscom_can_rbs_activate_node_by_name(0, True, b"CAN_FD_Powertrain", b"Engine", False)
        # 发送指定报文
        ret = tscom_can_rbs_activate_message_by_name(0, True, b"CAN_FD_Powertrain", b"Engine",
                                                    b"GearBoxInfo")
    else:
        print(tsapp_get_error_description(ret),ret)


if __name__ == "__main__":
    connect()
    signalvalue = c_double(0)
    while True:
        key = input("请输入key值")
        if key == "1":
            tscom_can_rbs_set_signal_value_by_element(0, "CAN_FD_Powertrain".encode("utf8"), "Engine".encode("utf8"),
                                                      "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                                      c_double(1.0))

            time.sleep(0.1)
            tscom_can_rbs_get_signal_value_by_element(0, "CAN_FD_Powertrain".encode("utf8"), "Engine".encode("utf8"),
                                                      "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                                      signalvalue)
            print(signalvalue)

        elif key == "2":
            tscom_can_rbs_set_signal_value_by_element(0, "CAN_FD_Powertrain".encode("utf8"), "Engine".encode("utf8"),
                                                      "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                                      c_double(2.0))
            time.sleep(0.1)
            tscom_can_rbs_get_signal_value_by_element(0, "CAN_FD_Powertrain".encode("utf8"), "Engine".encode("utf8"),
                                                      "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                                      signalvalue)
            print(signalvalue)
        elif key == "3":
            tscom_can_rbs_set_signal_value_by_element(0, "CAN_FD_Powertrain".encode("utf8"), "Engine".encode("utf8"),
                                                      "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                                      c_double(3.0))
            time.sleep(0.1)
            tscom_can_rbs_get_signal_value_by_element(0, "CAN_FD_Powertrain".encode("utf8"), "Engine".encode("utf8"),
                                                      "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                                      signalvalue)
            print(signalvalue)
        elif key == "4":
            tscom_can_rbs_set_signal_value_by_element(0, "CAN_FD_Powertrain".encode("utf8"), "Engine".encode("utf8"),
                                                      "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                                      c_double(4.0))
            time.sleep(0.1)
            tscom_can_rbs_get_signal_value_by_element(0, "CAN_FD_Powertrain".encode("utf8"), "Engine".encode("utf8"),
                                                      "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                                      signalvalue)
            print(signalvalue)
        elif key == "5":
            tscom_can_rbs_set_signal_value_by_element(0, "CAN_FD_Powertrain".encode("utf8"), "Engine".encode("utf8"),
                                                      "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                                      c_double(5.0))
            time.sleep(0.1)
            tscom_can_rbs_get_signal_value_by_element(0, "CAN_FD_Powertrain".encode("utf8"), "Engine".encode("utf8"),
                                                      "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                                      signalvalue)
            print(signalvalue)
        elif key == "6":
            tscom_can_rbs_set_signal_value_by_element(0, "CAN_FD_Powertrain".encode("utf8"), "Engine".encode("utf8"),
                                                      "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                                      c_double(6.0))
            time.sleep(0.1)
            tscom_can_rbs_get_signal_value_by_element(0, "CAN_FD_Powertrain".encode("utf8"), "Engine".encode("utf8"),
                                                      "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                                      signalvalue)
            print(signalvalue)
        elif key == "7":
            tscom_can_rbs_set_signal_value_by_element(0, "CAN_FD_Powertrain".encode("utf8"), "Engine".encode("utf8"),
                                                      "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                                      c_double(7.0))
            time.sleep(0.1)
            tscom_can_rbs_get_signal_value_by_element(0, "CAN_FD_Powertrain".encode("utf8"), "Engine".encode("utf8"),
                                                      "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                                      signalvalue)
            print(signalvalue)
        elif key == "8":
            tscom_can_rbs_set_signal_value_by_element(0, "CAN_FD_Powertrain".encode("utf8"), "Engine".encode("utf8"),
                                                      "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                                      c_double(8.0))
            time.sleep(0.1)
            tscom_can_rbs_get_signal_value_by_element(0, "CAN_FD_Powertrain".encode("utf8"), "Engine".encode("utf8"),
                                                      "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                                      signalvalue)
            print(signalvalue)
        elif key == "q":
            tscom_can_rbs_activate_network_by_name(0, False, "CAN_FD_Powertrain".encode("utf8"), True)
            break
        else:
            tscom_can_rbs_set_signal_value_by_element(0, "CAN_FD_Powertrain".encode("utf8"), "Engine".encode("utf8"),
                                                      "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                                      c_double(0.0))
            time.sleep(0.1)
            tscom_can_rbs_get_signal_value_by_element(0, "CAN_FD_Powertrain".encode("utf8"), "Engine".encode("utf8"),
                                                      "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                                      signalvalue)
            print(signalvalue)
    finalize_lib_tsmaster()
