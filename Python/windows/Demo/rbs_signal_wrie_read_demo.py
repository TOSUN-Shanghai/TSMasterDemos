from TSMasterAPI import *

ProjectName = "TSMaster".encode("utf8")
# 初始化
initialize_lib_tsmaster(ProjectName)
dbchandle = c_int32(0)

# 0/CAN_FD_Powertrain/Engine/GearBoxInfo/Gear
def connect():
    ret = tsdb_load_can_db(r"CAN_FD_Powertrain.dbc", "0,1", dbchandle)
    print(ret,dbchandle)
    ret = tsapp_connect()
    if ret == 0:
        print("连接成功")
        # 开启rbs功能
        tscom_can_rbs_start()
        # 激活network
        tscom_can_rbs_activate_network_by_name(0, True, "CAN_FD_Powertrain".encode("utf8"), False)
        # 激活节点
        tscom_can_rbs_activate_node_by_name(0, True, "CAN_FD_Powertrain".encode("utf8"), "Engine".encode("utf8"), False)
        # 发送指定报文
        ret = tscom_can_rbs_activate_message_by_name(0, True, "CAN_FD_Powertrain".encode("utf8"), "Engine".encode("utf8"),
                                                     "GearBoxInfo".encode("utf8"))
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
                                                      c_double(10.0))

            time.sleep(0.1)
            tscom_can_rbs_get_signal_value_by_element(0, "CAN_FD_Powertrain".encode("utf8"), "Engine".encode("utf8"),
                                                      "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                                      signalvalue)
            print(signalvalue)

        elif key == "2":
            tscom_can_rbs_set_signal_value_by_element(0, "CAN_FD_Powertrain".encode("utf8"), "Engine".encode("utf8"),
                                                      "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                                      c_double(20.0))
            time.sleep(0.1)
            tscom_can_rbs_get_signal_value_by_element(0, "CAN_FD_Powertrain".encode("utf8"), "Engine".encode("utf8"),
                                                      "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                                      signalvalue)
            print(signalvalue)
        elif key == "3":
            tscom_can_rbs_set_signal_value_by_element(0, "CAN_FD_Powertrain".encode("utf8"), "Engine".encode("utf8"),
                                                      "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                                      c_double(30.0))
            time.sleep(0.1)
            tscom_can_rbs_get_signal_value_by_element(0, "CAN_FD_Powertrain".encode("utf8"), "Engine".encode("utf8"),
                                                      "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                                      signalvalue)
            print(signalvalue)
        elif key == "4":
            tscom_can_rbs_set_signal_value_by_element(0, "CAN_FD_Powertrain".encode("utf8"), "Engine".encode("utf8"),
                                                      "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                                      c_double(40.0))
            time.sleep(0.1)
            tscom_can_rbs_get_signal_value_by_element(0, "CAN_FD_Powertrain".encode("utf8"), "Engine".encode("utf8"),
                                                      "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                                      signalvalue)
            print(signalvalue)
        elif key == "5":
            tscom_can_rbs_set_signal_value_by_element(0, "CAN_FD_Powertrain".encode("utf8"), "Engine".encode("utf8"),
                                                      "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                                      c_double(50.0))
            time.sleep(0.1)
            tscom_can_rbs_get_signal_value_by_element(0, "CAN_FD_Powertrain".encode("utf8"), "Engine".encode("utf8"),
                                                      "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                                      signalvalue)
            print(signalvalue)
        elif key == "6":
            tscom_can_rbs_set_signal_value_by_element(0, "CAN_FD_Powertrain".encode("utf8"), "Engine".encode("utf8"),
                                                      "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                                      c_double(60.0))
            time.sleep(0.1)
            tscom_can_rbs_get_signal_value_by_element(0, "CAN_FD_Powertrain".encode("utf8"), "Engine".encode("utf8"),
                                                      "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                                      signalvalue)
            print(signalvalue)
        elif key == "7":
            tscom_can_rbs_set_signal_value_by_element(0, "CAN_FD_Powertrain".encode("utf8"), "Engine".encode("utf8"),
                                                      "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                                      c_double(70.0))
            time.sleep(0.1)
            tscom_can_rbs_get_signal_value_by_element(0, "CAN_FD_Powertrain".encode("utf8"), "Engine".encode("utf8"),
                                                      "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                                      signalvalue)
            print(signalvalue)
        elif key == "8":
            tscom_can_rbs_set_signal_value_by_element(0, "CAN_FD_Powertrain".encode("utf8"), "Engine".encode("utf8"),
                                                      "GearBoxInfo".encode("utf8"), "Gear".encode("utf8"),
                                                      c_double(80.0))
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
