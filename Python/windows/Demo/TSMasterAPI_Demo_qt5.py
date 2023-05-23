from TOSUN_Demo import *  # 需要运行的.py文件名
from TSMasterAPI import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
import tkinter as tk
from tkinter import filedialog
AppName = b'TSMaster_gui'
msg = TLIBCAN()
msg.FIdxChn = 0
msg.FIdentifier = 0x100
msg.FProperties = 5  # 表示为扩展帧
msg.FDLC = 8
FData = [0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17]
for i in range(len(FData)):
    msg.FData[i] = FData[i]

LINmsg = TLIBLIN()
LINmsg.FIdxChn = 0
LINmsg.FProperties = 1  # 1：表示发送 0：表示接收
LINmsg.FDLC = 8
LINmsg.FIdentifier = 0x3c
FData1 = [0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17]
for i in range(len(FData1)):
    LINmsg.FData[i] = FData1[i]

FDmsg = TLIBCANFD()
FDmsg.FIdxChn = 0
FDmsg.FIdentifier = 0x101
FDmsg.FProperties = 5
FDmsg.FFDProperties = 0x1
FDmsg.FDLC = 9
FData0 = [0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1A, 0x20]
for i in range(len(FData0)):
    FDmsg.FData[i] = FData0[i]


def On_CAN_EVENT(OBJ, ACAN):
    global count_Event
    if (ACAN.contents.FIdentifier == 0x100 and ACAN.contents.FIdxChn == 0):
        print("CAN回调接收成功")
        for i in ACAN.contents.FData:
            print('%#x' % i, end=' ')


def On_CANFD_EVENT(OBJ, ACAN):
    global count_Event
    if (ACAN.contents.FFIdentifier == 0x1 and ACAN.contents.FIdxChn == 0):
        print("CANFD回调接收成功")
        for i in ACAN.contents.FData:
            print('%#x' % i, end=' ')


def On_LIN_EVENT(OBJ, ACAN):
    if 1:
        print("LIN回调接收成功", ACAN.contents.FIdentifier)
        for i in ACAN.contents.FData:
            print('%#x' % i, end=' ')


OnLINevent = OnTx_RxFUNC_LIN(On_LIN_EVENT)

OnCANevent = OnTx_RxFUNC_CAN(On_CAN_EVENT)
OnCANFDevent = OnTx_RxFUNC_CANFD(On_CANFD_EVENT)


class MyWindows(QMainWindow, Ui_MainWindow):
    ACount = c_int32(0)
    CANobj = c_int32(0)
    CANFDobj = c_int32(0)
    LINobj = c_int32(0)
    udsHandle = c_int32(0)
    dbc_id = c_int32(0)
    blf_id = c_int32(0)
    blf_count = c_int32(0)

    def __init__(self):
        super(MyWindows, self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.timer = QTimer(self)  # 初始化一个定时器

        self.timer.timeout.connect(self.clearTxetBox)  # 每次计时到时间时发出信号

        self.timer.start(3000)  # 设置计时间隔并启动；单位毫秒

        self.btn_getHwNum.clicked.connect(self.get_hw_devices)

        self.btn_configureCAN_LIN.clicked.connect(self.show_Hardware_window)

        self.btn_getHwInfo.clicked.connect(self.get_hw_info)

        self.btn_OnCanEvent.clicked.connect(self.register_event_can)

        self.btn_OnCanFDEvent.clicked.connect(self.register_event_canfd)

        self.btn_UneventCAN.clicked.connect(self.unregister_event_can)

        self.btn_UneventCANFD.clicked.connect(self.unregister_event_canfd)

        self.btn_ONeventLIN.clicked.connect(self.register_event_lin)

        self.btn_UNeventLIN.clicked.connect(self.unregister_event_lin)

        self.btn_Connect.clicked.connect(self.connect_Hardware)

        self.btn_DisConnect.clicked.connect(self.dis_connect_Hardware)

        self.btn_SendCANmsg.clicked.connect(self.send_can_msg)

        self.btn_SendCANFDmsg.clicked.connect(self.send_canfd_msg)

        self.btn_cyclicCANmsg.clicked.connect(self.cyclic_can_msg)

        self.btn_cyclicCANFDmsg.clicked.connect(self.cyclic_canfd_msg)

        self.btn_stopcyclicCANmsg.clicked.connect(self.stop_cyclic_can_msg)

        self.btn_stopcyclicCANFDmsg.clicked.connect(self.stop_cyclic_canfd_msg)

        self.btn_receiveCANmsg.clicked.connect(self.receive_can_msg)

        self.btn_receiveCANFDmsg.clicked.connect(self.receive_canfd_msg)

        self.btn_sendLINmsg.clicked.connect(self.send_lin_msg)

        self.btn_send_HEAD_receiveLINmsg.clicked.connect(self.transmit_header_and_receive_msg)

        self.btn_createuds.clicked.connect(self.creat_uds_module)

        self.btn_req_and_get_res.clicked.connect(self.req_and_get_res)

        self.btn_loadDBC.clicked.connect(self.load_DBC)

        self.btn_ReadDBCsignal.clicked.connect(self.read_dbc_signal_num)

        self.btn_ReadDBCmsg.clicked.connect(self.read_dbc_message_num)

        self.btn_loadBlf.clicked.connect(self.load_blf)

        self.btn_read_blf_Data.clicked.connect(self.read_blf)

    def get_hw_devices(self):
        r = tsapp_enumerate_hw_devices(self.ACount)
        if r == 0:
            self.comboBox.clear()
            for i in range(self.ACount.value):
                self.comboBox.addItem(i.__str__())

    def show_Hardware_window(self):
        tsapp_show_tsmaster_window(b"Hardware",True)
        self.textBrowser.append("硬件配置成功\r\n")
        self.textBrowser.moveCursor(self.textBrowser.textCursor().End)

    def connect_Hardware(self):
        if 0 == tsapp_connect():
            tsfifo_enable_receive_fifo()
            tslin_set_node_funtiontype(CHANNEL_INDEX.CHN1, T_LIN_NODE_FUNCTION.T_MASTER_NODE)
            self.textBrowser.append("连接成功\r\n")
            self.textBrowser.moveCursor(self.textBrowser.textCursor().End)

    def dis_connect_Hardware(self):
        if 0 == tsapp_disconnect():
            self.textBrowser.append("断开连接成功\r\n")
            self.textBrowser.moveCursor(self.textBrowser.textCursor().End)

    def get_hw_info(self):
        PTLIBHWInfo = TLIBHWInfo()
        if self.comboBox.currentText()!='':
            acount = int(self.comboBox.currentText())
            if 0 == tsapp_get_hw_info_by_index(acount, PTLIBHWInfo):
                self.tb_FVendorName.setText(PTLIBHWInfo.FVendorName.decode("utf8"))
                self.tb_FDeviceName.setText(PTLIBHWInfo.FDeviceName.decode("utf8"))
                self.tb_FSerialString.setText(PTLIBHWInfo.FSerialString.decode("utf8"))

            print(PTLIBHWInfo.FDeviceType, PTLIBHWInfo.FDeviceIndex, PTLIBHWInfo.FVendorName.decode("utf8"),
                PTLIBHWInfo.FDeviceName.decode("utf8"),
                PTLIBHWInfo.FSerialString.decode("utf8"))
        else:
            self.textBrowser.append("请先获取在线硬件数量\r\n")

    def register_event_can(self):
        if 0 == tsapp_register_event_can(self.CANobj, OnCANevent):
            self.textBrowser.append("can回调事件注册成功\r\n")
            self.textBrowser.moveCursor(self.textBrowser.textCursor().End)

    def register_event_canfd(self):
        if 0 == tsapp_register_event_canfd(self.CANFDobj, OnCANFDevent):
            self.textBrowser.append("canfd回调事件注册成功\r\n")
            self.textBrowser.moveCursor(self.textBrowser.textCursor().End)

    def unregister_event_can(self):
        if 0 == tsapp_unregister_event_can(self.CANobj, OnCANevent):
            self.textBrowser.append("can回调事件注销成功\r\n")
            self.textBrowser.moveCursor(self.textBrowser.textCursor().End)

    def unregister_event_canfd(self):
        if 0 == tsapp_unregister_event_canfd(self.CANFDobj, OnCANFDevent):
            self.textBrowser.append("canfd回调事件注销成功\r\n")
            self.textBrowser.moveCursor(self.textBrowser.textCursor().End)

    def register_event_lin(self):
        if 0 == tsapp_register_event_lin(self.LINobj, OnLINevent):
            self.textBrowser.append("lin回调事件注册成功\r\n")
            self.textBrowser.moveCursor(self.textBrowser.textCursor().End)

    def unregister_event_lin(self):
        if 0 == tsapp_unregister_event_lin(self.LINobj, OnLINevent):
            self.textBrowser.append("lin回调事件注销成功\r\n")
            self.textBrowser.moveCursor(self.textBrowser.textCursor().End)

    def send_can_msg(self):
        for i in range(10):
            r = tsapp_transmit_can_async(msg)
        if r == 0:
            self.textBrowser.append("CANFD发送成功\r\n")
        else:
            self.textBrowser.append("错误信息" + tsapp_get_error_description(r))

    def send_canfd_msg(self):
        for i in range(10):
            r = tsapp_transmit_canfd_async(FDmsg)
        if r == 0:
            self.textBrowser.append("CANFD发送成功\r\n")
        else:
            self.textBrowser.append("错误信息" + tsapp_get_error_description(r))

    def cyclic_can_msg(self):
        if 0 == tsapp_add_cyclic_msg_can(msg, 100):
            self.textBrowser.append("can报文周期发送成功\r\n")
            self.textBrowser.moveCursor(self.textBrowser.textCursor().End)

    def cyclic_canfd_msg(self):
        if 0 == tsapp_add_cyclic_msg_canfd(FDmsg, 100):
            self.textBrowser.append("canfd报文周期发送成功\r\n")
            self.textBrowser.moveCursor(self.textBrowser.textCursor().End)

    def stop_cyclic_can_msg(self):
        if 0 == tsapp_del_cyclic_msg_can(msg):
            self.textBrowser.append("停止can报文周期发送成功\r\n")
            self.textBrowser.moveCursor(self.textBrowser.textCursor().End)

    def stop_cyclic_canfd_msg(self):
        if 0 == tsapp_del_cyclic_msg_canfd(FDmsg):
            self.textBrowser.append("停止canfd报文周期发送成功\r\n")
            self.textBrowser.moveCursor(self.textBrowser.textCursor().End)

    def receive_can_msg(self):
        listcanmsg = (TLIBCAN*100)()
        size = c_int32(100)
        r = tsfifo_receive_can_msgs(listcanmsg, size, 1, READ_TX_RX_DEF.ONLY_RX_MESSAGES)
        if r == 0:
            for i in range(size.value):
                a = ' '
                str1 = (
                    str(listcanmsg[i].FTimeUs / 1000000), str(listcanmsg[i].FIdxChn), hex(listcanmsg[i].FIdentifier),
                    str(listcanmsg[i].FDLC), hex(listcanmsg[i].FData[0]), hex(listcanmsg[i].FData[1]),
                    hex(listcanmsg[i].FData[2]), hex(listcanmsg[i].FData[3]), hex(listcanmsg[i].FData[4]),
                    hex(listcanmsg[i].FData[5]), hex(listcanmsg[i].FData[6]), hex(listcanmsg[i].FData[7]))
                self.textBrowser.append(a.join(str1) + "\r\n")
                self.textBrowser.moveCursor(self.textBrowser.textCursor().End)
        else:
            self.textBrowser.append("错误信息" + tsapp_get_error_description(r))

    def receive_canfd_msg(self):
        listcanmsg = (TLIBCANFD*100)()
        size = c_int32(100)
        r = tsfifo_receive_canfd_msgs(listcanmsg, size, 1, READ_TX_RX_DEF.ONLY_RX_MESSAGES)
        if r == 0:
            for i in range(size.value):
                a = ' '
                str1 = (
                    str(listcanmsg[i].FTimeUs / 1000000), str(listcanmsg[i].FIdxChn), hex(listcanmsg[i].FIdentifier),
                    str(listcanmsg[i].FDLC), hex(listcanmsg[i].FData[0]), hex(listcanmsg[i].FData[1]),
                    hex(listcanmsg[i].FData[2]), hex(listcanmsg[i].FData[3]), hex(listcanmsg[i].FData[4]),
                    hex(listcanmsg[i].FData[5]), hex(listcanmsg[i].FData[6]), hex(listcanmsg[i].FData[7]))
                self.textBrowser.append(a.join(str1) + "\r\n")
                self.textBrowser.moveCursor(self.textBrowser.textCursor().End)
        else:
            self.textBrowser.append("错误信息" + tsapp_get_error_description(r))

    def send_lin_msg(self):
        for i in range(10):
            tsapp_transmit_lin_async(LINmsg)

    def transmit_header_and_receive_msg(self):
        TLIN1 = TLIBLIN()
        tsapp_transmit_header_and_receive_msg(CHANNEL_INDEX.CHN1, 0X3D, 8, TLIN1, c_int(20))

    def creat_uds_module(self):
        # uds_create_can(self.udsHandle, 0, False, 8, 0X1, False, 0X2, False)

        r = tsdiag_can_create(self.udsHandle, CHANNEL_INDEX.CHN1, 0, 8, 0X1, True, 0X2, True, 0X3, True)

    def req_and_get_res(self):
        AReqDataArray = (c_uint8 * 100)()
        AReqDataArray[0] = c_uint8(0x22)
        AReqDataArray[1] = c_uint8(0xf1)
        AReqDataArray[2] = c_uint8(0x90)
        AResSize = c_int32(100)
        AResponseDataArray = (c_uint8 * 100)()
        r = tstp_can_request_and_get_response(self.udsHandle, AReqDataArray, 3, AResponseDataArray, AResSize)
        if r == 0:
            a = ' '
            self.textBrowser.append(a.join(hex(i) for i in AResponseDataArray[0:AResSize]) + "\r\n")
            self.textBrowser.moveCursor(self.textBrowser.textCursor().End)
        # AReqDataArray = [0x22, 0xf1, 0x90]
        # AResSize = c_int(0)
        # AResponseDataArray = []
        # for i in range(100):
        #     item = 0
        #     AResponseDataArray.append(item)
        # r = tstp_can_request_and_get_response(udsHandle, AReqDataArray, 3, AResponseDataArray, AResSize, 100)
        # print(tsapp_get_error_description(r))
        # for i in range(AResSize.value):
        #     print(AResponseDataArray[i], end="  ")
        #     if i == AResSize.value - 1:
        #         print(end='\n')

    def clearTxetBox(self):
        pass
        # self.textBrowser.clear()

    def load_DBC(self):
        root = tk.Tk()
        root.withdraw()
        filepath = filedialog.askopenfilename()

        if str(filepath).find(".dbc"):
            r = tsdb_load_can_db(filepath, "0,1", self.dbc_id)
            if r == 0:
                self.tb_load_dbc.setText(filepath[filepath.rindex("/") + 1:] + "文件加载成功")
            else:
                self.tb_load_dbc.setText("错误信息" + tsapp_get_error_description(r))

    def read_dbc_signal_num(self):
        r, value = tsdb_get_can_db_info(self.dbc_id, 10, 0, 0)
        if r == 0:
            self.tb_signal_num.setText(value)
        else:
            self.tb_message_num.setText("错误信息" + tsapp_get_error_description(r))

    def read_dbc_message_num(self):
        r, value = tsdb_get_can_db_info(self.dbc_id, 11, 0, 0)
        if r == 0:
            self.tb_message_num.setText(value)
        else:
            self.tb_message_num.setText("错误信息" + tsapp_get_error_description(r))

    def load_blf(self):
        root = tk.Tk()
        root.withdraw()
        filepath = filedialog.askopenfilename()
        if str(filepath).find(".blf"):
            r = tslog_blf_read_start(filepath, self.blf_id, self.blf_count)
        if r == 0:
            self.textBrowser.append(filepath[filepath.rindex("/") + 1:] + "文件加载成功")
        else:
            self.textBrowser.append("错误信息" + tsapp_get_error_description(r))

    def read_blf(self):
        realCount = c_ulong(0)
        messageType = TSupportedObjType.sotUnknown
        CANtemp = TLIBCAN()
        CANFDtemp = TLIBCANFD()
        LINtemp = TLIBLIN()
        a = ' '
        for i in range(self.blf_count.value):
            r = tslog_blf_read_object(self.blf_id, realCount, messageType, CANtemp, LINtemp, CANFDtemp)
            if messageType.value == TSupportedObjType.sotCAN.value:

                str1 = ("CAN",
                        str(CANtemp.FTimeUs / 1000000), str(CANtemp.FIdxChn),
                        hex(CANtemp.FIdentifier),
                        str(CANtemp.FDLC), hex(CANtemp.FData[0]), hex(CANtemp.FData[1]),
                        hex(CANtemp.FData[2]), hex(CANtemp.FData[3]), hex(CANtemp.FData[4]),
                        hex(CANtemp.FData[5]), hex(CANtemp.FData[6]), hex(CANtemp.FData[7]))
                self.textBrowser.append(a.join(str1) + "\r\n")
                self.textBrowser.moveCursor(self.textBrowser.textCursor().End)
            elif messageType.value == TSupportedObjType.sotCANFD.value:
                str1 = ("CANFD",
                        str(CANFDtemp.FTimeUs / 1000000), str(CANFDtemp.FIdxChn),
                        hex(CANFDtemp.FIdentifier),
                        str(CANFDtemp.FDLC), hex(CANFDtemp.FData[0]), hex(CANFDtemp.FData[1]),
                        hex(CANFDtemp.FData[2]), hex(CANFDtemp.FData[3]), hex(CANFDtemp.FData[4]),
                        hex(CANFDtemp.FData[5]), hex(CANFDtemp.FData[6]), hex(CANFDtemp.FData[7]))
                self.textBrowser.append(a.join(str1) + "\r\n")
                self.textBrowser.moveCursor(self.textBrowser.textCursor().End)
            elif messageType.value == TSupportedObjType.sotLIN.value:
                str1 = ("LIN",
                        str(LINtemp.FTimeUs / 1000000), str(LINtemp.FIdxChn),
                        hex(LINtemp.FIdentifier),
                        str(LINtemp.FDLC), hex(LINtemp.FData[0]), hex(LINtemp.FData[1]),
                        hex(LINtemp.FData[2]), hex(LINtemp.FData[3]), hex(LINtemp.FData[4]),
                        hex(LINtemp.FData[5]), hex(LINtemp.FData[6]), hex(LINtemp.FData[7]))
                self.textBrowser.append(a.join(str1) + "\r\n")
                self.textBrowser.moveCursor(self.textBrowser.textCursor().End)
        tslog_blf_read_end(self.blf_id)

    # def closeEvent(self):
    #     finalize_lib_tsmaster()


if __name__ == '__main__':
    initialize_lib_tsmaster(AppName)
    app = QApplication(sys.argv)  # 创建应用程序

    window = MyWindows()

    window.show()

    sys.exit(app.exec_())  # 程序执行循环
