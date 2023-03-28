'''
Author: seven 865762826@qq.com
Date: 2022-12-24 12:29:39
LastEditors: seven 865762826@qq.com
LastEditTime: 2023-03-28 13:33:33
FilePath: \window_linux_Repd:\Envs\python39_32\Lib\site-packages\libTOSUN\libTOSUN.py
'''

import time
from ctypes import *
import copy
import platform
from typing import Optional
import cantools
from can.message import Message as Message
import can
import os
import queue

# _curr_path = os.path.split(os.path.realpath(__file__))[0]
_curr_path = os.path.dirname(__file__)
_arch, _os = platform.architecture()
_os = platform.system()
_is_windows, _is_linux = False, False
if 'windows' in _os.lower():
    _is_windows = True
    if _arch == '32bit':
        # os.add_dll_directory(os.path.join(_curr_path, 'windows/x86'))
        os.chdir(os.path.join(_curr_path, 'windows/x86'))
        _lib_path = os.path.join(_curr_path, 'windows/x86/libTSCAN.dll')
    else:
        # os.add_dll_directory(os.path.join(_curr_path, 'windows/x64'))
        os.chdir(os.path.join(_curr_path, 'windows/x64'))
        _lib_path = os.path.join(_curr_path, 'windows/x64/libTSCAN.dll')
    # if not os.path.exists(_lib_path):
    #     _lib_path = r"D:\demo\libtosun\libtosun\windows\X64\libTSCAN.dll"
    dll = windll.LoadLibrary(_lib_path)
elif 'linux' in _os.lower():
    _is_linux = True
    if _arch == '64bit':
        # os.add_dll_directory(os.path.join(_curr_path, 'linux'))
        os.chdir(os.path.join(_curr_path, 'linux'))
        _lib_path = os.path.join(_curr_path, 'linux/libTSCANApiOnLinux.so')
    else:
        _lib_path = None
    if _lib_path:
        dll = cdll.LoadLibrary(_lib_path)
else:
    _library = None


# dll = cdll.LoadLibrary("./libTSCANApiOnLinux.so")


class CHANNEL_INDEX():
    (
        CHN1, CHN2, CHN3, CHN4, CHN5, CHN6, CHN7, CHN8, CHN9, CHN10, CHN11, CHN12, CHN13, CHN14, CHN15, CHN16, CHN17,
        CHN18, CHN19, CHN20, CHN21, CHN22, CHN23, CHN24, CHN25, CHN26, CHN27, CHN28, CHN29, CHN30, CHN31, CHN32) = (
        c_int(0), c_int(1), c_int(2), c_int(3), c_int(4), c_int(
            5), c_int(6), c_int(7), c_int(8), c_int(9), c_int(10),
        c_int(11), c_int(12), c_int(13), c_int(14), c_int(15), c_int(
            16), c_int(17), c_int(18), c_int(19), c_int(20),
        c_int(21), c_int(22), c_int(23), c_int(24), c_int(
            25), c_int(26), c_int(27), c_int(28), c_int(29),
        c_int(30),
        c_int(31)
    )


class READ_TX_RX_DEF():
    ONLY_RX_MESSAGES = c_int(0)
    TX_RX_MESSAGES = c_int(1)


class LIN_PROTOCOL():
    LIN_PROTOCOL_13 = c_int(0)
    LIN_PROTOCOL_20 = c_int(1)
    LIN_PROTOCOL_21 = c_int(2)
    LIN_PROTOCOL_J2602 = c_int(3)


class T_LIN_NODE_FUNCTION():
    T_MASTER_NODE = c_int(0)
    T_SLAVE_NODE = c_int(1)
    T_MONITOR_NODE = c_int(2)


class TLIBCANFDControllerType():
    lfdtCAN = c_int(0)
    lfdtISOCAN = c_int(1)
    lfdtNonISOCAN = c_int(2)


class TLIBCANFDControllerMode():
    lfdmNormal = c_int(0)
    lfdmACKOff = c_int(1)
    lfdmRestricted = c_int(2)


class A120():
    DEABLEA120 = c_int(0)
    ENABLEA120 = c_int(1)


class CONVERTTYPE():
    BLF = 0
    ASC = 1
    CSV = 2
    TXT = 3
    SQL = 4
    LOG = 5


class TLIBCAN(Structure):
    _pack_ = 1
    _fields_ = [("FIdxChn", c_uint8),
                # 定义can数据类型  1:标准数据帄1 7 3:标准远程帄1 7 5:扩展数据帧 7:扩展远程帧
                ("FProperties", c_uint8),
                ("FDLC", c_uint8),
                ("FReserved", c_uint8),
                ("FIdentifier", c_int32),
                ("FTimeUs", c_uint64),
                ("FData", c_uint8 * 8),
                ]

    def __init__(self, FIdxChn=0, FDLC=8, FIdentifier=0x1, FProperties=1, FData=[]):
        self.FIdxChn = FIdxChn
        self.FDLC = FDLC
        if self.FDLC > 8:
            self.FDLC = 8
        self.FIdentifier = FIdentifier
        self.FProperties = FProperties
        for i in range(len(FData)):
            self.FData[i] = FData[i]

    def set_data(self, data):
        lengh = len(data)
        if lengh > self.FDLC:
            lengh = self.FDLC
        for i in range(lengh):
            self.FData[i] = data[i]

    def __str__(self):
        field_strings = [f"Timestamp: {self.FTimeUs:>15.6f}"]

        field_strings.append(f"Channel: {self.FIdxChn}")

        if (self.FProperties >> 2 & 1) == 1:
            FIdentifier = f"ID: {self.FIdentifier:08x}"
        else:
            FIdentifier = f"ID: {self.FIdentifier:04x}"
        field_strings.append(FIdentifier.rjust(12, " "))
        flag_string = " ".join(
            [
                "ext" if (self.FProperties >> 2 & 1) == 1 else "std",
                "Rx" if (self.FProperties & 1) == 0 else "Tx",
                "E" if self.FProperties == 0x80 else " ",
                "R" if (self.FProperties >> 1 & 1) == 1 else " ",
            ]
        )
        field_strings.append(flag_string)
        field_strings.append(f"DL: {self.FDLC:2d}")
        data_strings = []
        for i in range(self.FDLC):
            data_strings.append(f"{self.FData[i]:02x}")
        field_strings.append(" ".join(data_strings).ljust(24, " "))
        return "    ".join(field_strings).strip()


class TLIBCANFD(Structure):
    _pack_ = 1
    _fields_ = [("FIdxChn", c_uint8),
                ("FProperties", c_uint8),  # 定义canfd数据类型  1:FD标准帄1 7 5:FD扩展帄1 7
                ("FDLC", c_uint8),
                ("FFDProperties", c_uint8),  # 0:普  can数据帄1 7 1:canfd数据帄1 7
                ("FIdentifier", c_int32),
                ("FTimeUs", c_ulonglong),
                ("FData", c_ubyte * 64),
                ]

    def __init__(self, FIdxChn=0, FDLC=8, FIdentifier=0x1, FProperties=1, FFDProperties=1, FData=[]):

        self.FIdxChn = FIdxChn
        self.FDLC = FDLC
        if self.FDLC > 15:
            self.FDLC = 15
        self.FIdentifier = FIdentifier
        self.FProperties = FProperties
        self.FFDProperties = FFDProperties
        for i in range(len(FData)):
            self.FData[i] = FData[i]

    def set_data(self, data):
        lengh = len(data)
        if lengh > DLC_DATA_BYTE_CNT(self.FDLC):
            lengh = DLC_DATA_BYTE_CNT(self.FDLC)
        for i in range(lengh):
            self.FData[i] = data[i]

    def __str__(self):
        field_strings = [f"Timestamp: {self.FTimeUs:>15.6f}"]

        field_strings.append(f"Channel: {self.FIdxChn}")

        if (self.FProperties >> 2 & 1) == 1:
            FIdentifier = f"ID: {self.FIdentifier:08x}"
        else:
            FIdentifier = f"ID: {self.FIdentifier:04x}"
        field_strings.append(FIdentifier.rjust(12, " "))
        flag_string = " ".join(
            [
                "ext" if (self.FProperties >> 2 & 1) == 1 else "std",
                "Rx" if (self.FProperties & 1) == 0 else "Tx",
                "E" if self.FProperties == 0x80 else " ",
                "R" if (self.FProperties >> 1 & 1) == 1 else " ",
                "F" if (self.FFDProperties & 1 == 1) else " ",
                "BS" if (self.FFDProperties >> 1 & 1 == 1) else "  ",
                "EI" if (self.FFDProperties >> 2 & 1 == 1) else "  ",
            ]
        )
        field_strings.append(flag_string)
        field_strings.append(f"DL: {self.FDLC:2d}")
        data_strings = []
        for i in range(DLC_DATA_BYTE_CNT[self.FDLC]):
            data_strings.append(f"{self.FData[i]:02x}")
        field_strings.append(" ".join(data_strings).ljust(24, " "))
        return "    ".join(field_strings).strip()


class TLIBLIN(Structure):
    _pack_ = 1
    _fields_ = [("FIdxChn", c_ubyte),
                ("FErrCode", c_ubyte),
                ("FProperties", c_ubyte),
                ("FDLC", c_uint8),
                ("FIdentifier", c_ubyte),
                ("FChecksum", c_ubyte),
                ("FStatus", c_ubyte),
                ("FTimeUs", c_ulonglong),
                ("FData", c_uint8 * 8),
                ]


class TLIBFlexray(Structure):
    _pack_ = 1
    _fields_ = [("FIdxChn", c_uint8),
                ("FChannelMask", c_uint8),
                ("FDir", c_uint8),
                ("FPayloadLength", c_uint8),
                ("FActualPayloadLength", c_uint8),
                ("FCycleNumber", c_uint8),
                ("FCCType", c_uint8),
                ("FReserved0", c_uint8),
                ("FHeaderCRCA", c_uint16),
                ("FHeaderCRCB", c_uint16),
                ("FFrameStateInfo", c_uint16),
                ("FSlotId", c_uint16),
                ("FFrameFlags", c_uint32),
                ("FFrameCRC", c_uint32),
                ("FReserved1", c_uint64),
                ("FReserved2", c_uint64),
                ("FTimeUs", c_uint64),
                ("FData", c_uint8 * 254),
                ]
    def __init__(self,FIdxChn=0,FSlotId=1,FChannelMask=1,FActualPayloadLength=32,FCycleNumber=1,FData=[]):
        self.FIdxChn = FIdxChn
        self.FSlotId = FSlotId
        self.FChannelMask = FChannelMask|0x04
        self.FActualPayloadLength = FActualPayloadLength
        self.FCycleNumber = FCycleNumber    
        datalen = len(FData)
        if datalen>self.FActualPayloadLength:
            datalen = self.FActualPayloadLength
        for i in range(datalen):
            self.FData[i] = FData[i]
    def set_data(self,data):
        datalen = len(data)
        if datalen>self.FActualPayloadLength:
            datalen = self.FActualPayloadLength
        for i in range(datalen):
            self.FData[i] = data[i]
        

class TLibFlexray_controller_config(Structure):
    _pack_ = 1
    _fields_ = [("NETWORK_MANAGEMENT_VECTOR_LENGTH", c_uint8),
                ("PAYLOAD_LENGTH_STATIC", c_uint8),
                ("FReserved", c_uint16),
                ("LATEST_TX", c_uint16),
                ("T_S_S_TRANSMITTER", c_uint16),
                ("CAS_RX_LOW_MAX", c_uint8),
                ("SPEED", c_uint8),
                ("WAKE_UP_SYMBOL_RX_WINDOW", c_uint16),
                ("WAKE_UP_PATTERN", c_uint8),
                ("WAKE_UP_SYMBOL_RX_IDLE", c_uint8),
                ("WAKE_UP_SYMBOL_RX_LOW", c_uint8),
                ("WAKE_UP_SYMBOL_TX_IDLE", c_uint8),
                ("WAKE_UP_SYMBOL_TX_LOW", c_uint8),
                ("channelAConnectedNode", c_uint8),
                ("channelBConnectedNode", c_uint8),
                ("channelASymbolTransmitted", c_uint8),
                ("channelBSymbolTransmitted", c_uint8),
                ("ALLOW_HALT_DUE_TO_CLOCK", c_uint8),
                ("SINGLE_SLOT_ENABLED", c_uint8),
                ("wake_up_idx", c_uint8),
                ("ALLOW_PASSIVE_TO_ACTIVE", c_uint8),
                ("COLD_START_ATTEMPTS", c_uint8),
                ("synchFrameTransmitted", c_uint8),
                ("startupFrameTransmitted", c_uint8),
                ("LISTEN_TIMEOUT", c_uint32),
                ("LISTEN_NOISE", c_uint8),
                ("MAX_WITHOUT_CLOCK_CORRECTION_PASSIVE", c_uint8),
                ("MAX_WITHOUT_CLOCK_CORRECTION_FATAL", c_uint8),
                ("REVERS0", c_uint8),
                ("MICRO_PER_CYCLE", c_uint32),
                ("Macro_Per_Cycle", c_uint16),
                ("SYNC_NODE_MAX", c_uint8),
                ("REVERS1", c_uint8),
                ("MICRO_INITIAL_OFFSET_A", c_uint8),
                ("MICRO_INITIAL_OFFSET_B", c_uint8),
                ("MACRO_INITIAL_OFFSET_A", c_uint8),
                ("MACRO_INITIAL_OFFSET_B", c_uint8),
                ("N_I_T", c_uint16),
                ("OFFSET_CORRECTION_START", c_uint16),
                ("DELAY_COMPENSATION_A", c_uint8),
                ("DELAY_COMPENSATION_B", c_uint8),
                ("CLUSTER_DRIFT_DAMPING", c_uint8),
                ("DECODING_CORRECTION", c_uint8),
                ("ACCEPTED_STARTUP_RANGE", c_uint16),
                ("MAX_DRIFT", c_uint16),
                ("STATIC_SLOT", c_uint16),
                ("NUMBER_OF_STATIC_SLOTS", c_uint16),
                ("MINISLOT", c_uint8),
                ("REVERS2", c_uint8),
                ("NUMBER_OF_MINISLOTS", c_uint16),
                ("DYNAMIC_SLOT_IDLE_PHASE", c_uint8),
                ("ACTION_POINT_OFFSET", c_uint8),
                ("MINISLOT_ACTION_POINT_OFFSET", c_uint8),
                ("REVERS3", c_uint8),
                ("OFFSET_CORRECTION_OUT", c_uint16),
                ("RATE_CORRECTION_OUT", c_uint16),
                ("EXTERN_OFFSET_CORRECTION", c_uint8),
                ("EXTERN_RATE_CORRECTION", c_uint8),
                ("config1_byte", c_uint8),
                ("config_byte", c_uint8),  # bit0: 1:启用cha上终端电阻 0:不启用
                # bit1: 1:启用chb上终端电阻 0:不启用
                # bit2: 1:启用接收FIFO     0:不启用
                # bit4: 1:cha桥接使能    0:不使能
                # bit5: 1:chb桥接使能    0:不使能
                # bit6: 1:not ignore NULL Frame  0: ignore NULL Frame
                ]

    def __init__(self, is_open_a=True, is_open_b=True, wakeup_chn=0, enable100_a=True, enable100_b=True,
                 is_show_nullframe=True, is_Bridging=False):
        '''
        is_open :是否打开通道
        wakeup_chn:唤醒通道 0:通道A ,1:通道B
        enable100: 使能通道 100欧终端电阻
        is_show_nullframe:是否显示空针
        '''
        self.NETWORK_MANAGEMENT_VECTOR_LENGTH = 8
        self.PAYLOAD_LENGTH_STATIC = 16
        self.LATEST_TX = 124
        self.T_S_S_TRANSMITTER = 9
        self.CAS_RX_LOW_MAX = 87
        self.SPEED = 0
        self.WAKE_UP_SYMBOL_RX_WINDOW = 301
        # ecu
        self.WAKE_UP_PATTERN = 43
        
        self.WAKE_UP_SYMBOL_RX_IDLE = 59
        self.WAKE_UP_SYMBOL_RX_LOW = 55
        self.WAKE_UP_SYMBOL_TX_IDLE = 180
        self.WAKE_UP_SYMBOL_TX_LOW = 60
        self.channelAConnectedNode = 0
        if is_open_a:
            self.channelAConnectedNode = 1  # 是否启用通道A,0不启动，1启动
        self.channelBConnectedNode = 0  # 是否启用通道B,0不启动，1启动
        if is_open_b:
            self.channelAConnectedNode = 1
        self.channelASymbolTransmitted = 1  # 是否启用通道A的符号传输功能,0不启动，1启动
        self.channelBSymbolTransmitted = 1  # 是否启用通道B的符号传输功能,0不启动，1启动
        self.ALLOW_HALT_DUE_TO_CLOCK = 1
        self.SINGLE_SLOT_ENABLED = 0  # FALSE_0, TRUE_1
        self.wake_up_idx = wakeup_chn  # 唤醒通道选择， 0_通道A， 1 通道B
        self.ALLOW_PASSIVE_TO_ACTIVE = 2
        self.COLD_START_ATTEMPTS = 10
        self.synchFrameTransmitted = 1  # 本节点是否需要发送同步报文
        self.startupFrameTransmitted = 1  # 本节点是否需要发送启动报文
        self.LISTEN_TIMEOUT = 401202
        self.LISTEN_NOISE = 2  # 2_16
        self.MAX_WITHOUT_CLOCK_CORRECTION_PASSIVE = 10
        self.MAX_WITHOUT_CLOCK_CORRECTION_FATAL = 14
        self.MICRO_PER_CYCLE = 200000
        self.Macro_Per_Cycle = 5000
        self.SYNC_NODE_MAX = 8
        # ECU
        self.MICRO_INITIAL_OFFSET_A = 31
        self.MICRO_INITIAL_OFFSET_B = 31
        self.MACRO_INITIAL_OFFSET_A = 11
        self.MACRO_INITIAL_OFFSET_B = 11

        self.N_I_T = 44
        self.OFFSET_CORRECTION_START = 4981
        #ECU
        self.DELAY_COMPENSATION_A = 1
        self.DELAY_COMPENSATION_B = 1

        self.CLUSTER_DRIFT_DAMPING = 2
        # ECU
        self.DECODING_CORRECTION = 48
        self.ACCEPTED_STARTUP_RANGE = 212
        self.MAX_DRIFT = 601

        self.STATIC_SLOT = 61
        self.NUMBER_OF_STATIC_SLOTS = 60
        self.MINISLOT = 10
        self.NUMBER_OF_MINISLOTS = 129
        self.DYNAMIC_SLOT_IDLE_PHASE = 0
        self.ACTION_POINT_OFFSET = 9
        self.MINISLOT_ACTION_POINT_OFFSET = 3
        # ECU
        self.OFFSET_CORRECTION_OUT = 378
        self.RATE_CORRECTION_OUT = 601
        self.EXTERN_OFFSET_CORRECTION = 0
        self.EXTERN_RATE_CORRECTION = 0

        self.config1_byte = 1
        # if
        self.config_byte = 0xc
        if is_Bridging:
            self.config_byte = 0x3c
        self.config_byte = self.config_byte | (0x1 if enable100_a else 0x00) | (0x2 if enable100_b else 0x00) | (
            0x40 if is_show_nullframe else 0x00)
        # self.config_byte = 0x3f


class TLibTrigger_def(Structure):
    _pack_ = 1
    _fields_ = [("slot_id", c_uint16),
                ("frame_idx", c_uint8),
                ("cycle_code", c_uint8),
                ("config_byte", c_uint8),  # bit0: 是否使能通道A
                # bit1: 是否使能通道B
                # bit2: 是否网络管理报文
                # bit3: 传输模式，0 表示连续传输，1表示单次触发
                # bit4: 是否为冷启动报文，只有缓冲区0可以置1
                # bit5: 是否为同步报文，只有缓冲区0 / 1 可以置1
                # bit6:
                # bit7: 帧类型:0 - 静态，1 - 动态
                ("recv", c_uint8),
                ]
    def __init__(self, frame_idx=0, slot_id=1, cycle_code=1, config_byte=0x33):
        self.frame_idx = frame_idx
        self.slot_id = slot_id
        self.cycle_code = cycle_code
        self.config_byte = config_byte


DLC_DATA_BYTE_CNT = (
    0, 1, 2, 3, 4, 5, 6, 7,
    8, 12, 16, 20, 24, 32, 48, 64
)


def tosun_convert_msg(msg):
    if isinstance(msg, TLIBCAN):
        return Message(
            timestamp=blf_start_time + float(msg.FTimeUs) / 1000000,
            arbitration_id=msg.FIdentifier,
            is_extended_id=msg.FProperties & 0x04,
            is_remote_frame=msg.FProperties & 0x02,
            is_error_frame=msg.FProperties & 0x80,
            channel=msg.FIdxChn,
            dlc=msg.FDLC,
            data=bytes(msg.FData),
            is_fd=False,
            is_rx=False if msg.FProperties & 0x01 else True,
        )
    elif isinstance(msg, TLIBCANFD):
        return Message(
            timestamp=blf_start_time + float(msg.FTimeUs) / 1000000,
            arbitration_id=msg.FIdentifier,
            is_extended_id=msg.FProperties & 0x04,
            is_remote_frame=msg.FProperties & 0x02,
            channel=msg.FIdxChn,
            dlc=DLC_DATA_BYTE_CNT[msg.FDLC],
            data=bytes(msg.FData),
            is_fd=msg.FFDProperties & 0x01,
            is_rx=False if msg.FProperties & 0x01 else True,
            bitrate_switch=msg.FFDProperties & 0x02,
            error_state_indicator=msg.FFDProperties & 0x04,
            is_error_frame=msg.FProperties & 0x80
        )
    elif isinstance(msg, Message):
        return msg
    else:
        raise (f'Unknown message type: {type(msg)}')


def msg_convert_tosun(msg):
    if isinstance(msg, TLIBCAN):
        return msg
    elif isinstance(msg, TLIBCANFD):
        return msg
    elif isinstance(msg, TLIBLIN):
        return msg
    elif isinstance(msg, Message):
        if msg.is_fd:
            result = TLIBCANFD()
            result.FFDProperties = 0x01 | (0x02 if msg.bitrate_switch else 0x00) | \
                (0x04 if msg.error_state_indicator else 0x00)
        else:
            result = TLIBCAN()
        result.FIdxChn = msg.channel
        result.FProperties = 0x01 | (0x00 if msg.is_rx else 0x01) | \
            (0x02 if msg.is_remote_frame else 0x00) | \
            (0x04 if msg.is_extended_id else 0x00)
        try:
            result.FDLC = DLC_DATA_BYTE_CNT.index(msg.dlc)
        except:
            if msg.dlc < 0x10:
                result.FDLC = msg.dlc
            else:
                print("Message DLC input error")

        result.FIdentifier = msg.arbitration_id
        result.FTimeUs = int(msg.timestamp)
        for index, item in enumerate(msg.data):
            result.FData[index] = item
        return result
    else:
        raise (f'Unknown message type: {type(msg)}')


start_time = 0


def finalize_lib_tscan():
    dll.finalize_lib_tscan()


# 初始化函数（是否使能fifo,是否濢 活极速模式）
def initialize_lib_tsmaster(AEnableFIFO: c_bool, AEnableTurbe: c_bool):
    dll.initialize_lib_tscan(AEnableFIFO, AEnableTurbe, True)


# 连接硬件(ADeviceSerial为null为任意硬仄1 7,ADeviceSerial == ""为连接任意设备，不为空时连接指定序列叄1 7 设备)
def tsapp_connect(ADeviceSerial: str, AHandle: c_size_t):
    r = dll.tscan_connect(ADeviceSerial, byref(AHandle))
    return r


def tscan_scan_devices(ADeviceCount: c_uint32):
    r = dll.tscan_scan_devices(byref(ADeviceCount))
    return r


def tscan_get_error_description(ACode: int):
    errorcode = POINTER(POINTER(c_char))()
    if ACode == 0:
        return "确定"
    else:
        r = dll.tscan_get_error_description(c_int32(ACode), byref(errorcode))
        if r == 0:
            ADesc = string_at(errorcode).decode("utf-8")
            return ADesc
        else:
            return r


def tsflexray_set_controller_frametrigger(AHandle: c_size_t, ANodeIndex: c_uint,
                                          AControllerConfig: TLibFlexray_controller_config,
                                          AFrameLengthArray: bytearray,
                                          AFrameNum: c_int, AFrameTrigger: TLibTrigger_def, AFrameTriggerNum: c_int,
                                          ATimeoutMs: c_int):
    r = dll.tsflexray_set_controller_frametrigger(AHandle, ANodeIndex, byref(AControllerConfig),
                                                  AFrameLengthArray, AFrameNum, AFrameTrigger,
                                                  AFrameTriggerNum, ATimeoutMs)
    return r


def tsflexray_cmdreq(AHandle: c_size_t, ANodeIndex: c_int, Action: c_int, ATriggerIndex: c_int, ARegAddr: c_uint32,
                     ARegVal: c_uint32, ATimeoutMs: c_int):
    r = dll.tsflexray_cmdreq(AHandle, ANodeIndex, Action,
                             ATriggerIndex, ARegAddr,   (ARegVal), ATimeoutMs)
    return r


def tsflexray_start_net(AHandle: c_size_t, ANodeIndex: c_int, ATimeoutMs: c_int):
    r = dll.tsflexray_start_net(AHandle, ANodeIndex, ATimeoutMs)
    return r


def tsflexray_stop_net(AHandle: c_size_t, ANodeIndex: c_int, ATimeoutMs: c_int):
    r = dll.tsflexray_stop_net(AHandle, ANodeIndex, ATimeoutMs)
    return r


def tsfifo_clear_flexray_receive_buffers(AHandle: c_size_t, chn: c_int):
    r = dll.tsfifo_clear_flexray_receive_buffers(AHandle, chn)
    return r


def tsflexray_transmit_async(AHandle: c_size_t, AData: TLIBFlexray):
    r = dll.tsflexray_transmit_async(AHandle, byref(AData))
    return r


def tsflexray_transmit_sync(AHandle: c_size_t, AData: TLIBFlexray, ATimeoutMs: c_int):
    r = dll.tsflexray_transmit_sync(AHandle, byref(AData), ATimeoutMs)
    return r


def tsfifo_read_flexray_buffer_frame_count(AHandle: c_size_t, AIdxChn: c_int, ACount: c_int):
    r = dll.tsfifo_read_flexray_buffer_frame_count(
        AHandle, AIdxChn, byref(ACount))
    return r


def tsfifo_read_flexray_tx_buffer_frame_count(AHandle: c_size_t, AIdxChn: c_int, ACount: c_int):
    r = dll.tsfifo_read_flexray_tx_buffer_frame_count(
        AHandle, AIdxChn, byref(ACount))
    return r


def tsfifo_read_flexray_rx_buffer_frame_count(AHandle: c_size_t, AIdxChn: c_int, ACount: c_int):
    r = dll.tsfifo_read_flexray_rx_buffer_frame_count(
        AHandle, AIdxChn, byref(ACount))
    return r


def tsfifo_receive_flexray_msgs(AHandle: c_size_t, ADataBuffers: TLIBFlexray, ADataBufferSize: c_int, chn: c_int,
                                ARxTx: c_int8):
    r = dll.tsfifo_receive_flexray_msgs(
        AHandle, ADataBuffers, byref(ADataBufferSize), chn, ARxTx)
    return r


def tscan_get_device_info(ADeviceCount: c_uint64):
    AFManufacturer = POINTER(POINTER(c_char))()

    AFProduct = POINTER(POINTER(c_char))()
    AFSerial = POINTER(POINTER(c_char))()
    r = dll.tscan_get_device_info(ADeviceCount, byref(
        AFManufacturer), byref(AFProduct), byref(AFSerial))
    if r == 0:
        FManufacturer = string_at(AFManufacturer).decode("utf8")
        FProduct = string_at(AFProduct).decode("utf8")
        FSerial = string_at(AFSerial).decode("utf8")
    else:
        print("查找失败")
        return 0, 0, 0
    return FManufacturer, FProduct, FSerial


# 断开指定硬件连接
def tsapp_disconnect_by_handle(AHandle: c_size_t):
    r = dll.tscan_disconnect_by_handle(AHandle)
    return r


# 断开扢 有硬件连掄1 7
def tsapp_disconnect_all():
    r = dll.tscan_disconnect_all_devices()
    return r


# 设置can参数
def tsapp_configure_baudrate_can(ADeviceHandle: c_size_t, AChnIdx: CHANNEL_INDEX, ARateKbps: c_double,A120: A120):
    if not isinstance(ARateKbps, c_double):
        ARateKbps = c_double(ARateKbps)
    r = dll.tscan_config_can_by_baudrate(
        ADeviceHandle, AChnIdx, ARateKbps, A120)
    return r


# 设置canfd参数
def tsapp_configure_baudrate_canfd(ADeviceHandle: c_size_t, AChnIdx: CHANNEL_INDEX, ARateKbps: c_double,
                                   ADataKbps: c_double,
                                   AControllerType: TLIBCANFDControllerType, AControllerMode: TLIBCANFDControllerMode,
                                   A120: A120):
    if not isinstance(ARateKbps, c_double):
        ARateKbps = c_double(ARateKbps)
    if not isinstance(ADataKbps, c_double):
        ADataKbps = c_double(ADataKbps)
    r = dll.tscan_config_canfd_by_baudrate(ADeviceHandle, AChnIdx, ARateKbps, ADataKbps, AControllerType,
                                           AControllerMode, A120)
    return r


# can brs 采样率设罄1 7
def tsapp_configure_can_regs(ADeviceHandle: c_size_t, AIdxChn: CHANNEL_INDEX, ABaudrateKbps: float, ASEG1: int,
                             ASEG2: int, APrescaler: int,
                             ASJ2: int, AOnlyListen: c_uint32, A120: c_uint32):
    r = dll.tscan_configure_can_regs(ADeviceHandle, AIdxChn, c_float(ABaudrateKbps), c_uint32(ASEG1), c_uint32(ASEG2),
                                     c_uint32(APrescaler), c_uint32(ASJ2), AOnlyListen, A120)
    return r


# canfd brs 采样率设罄1 7
def tsapp_configure_canfd_regs(ADeviceHandle: c_size_t, AIdxChn: CHANNEL_INDEX, AArbBaudrateKbps: float, AArbSEG1: int,
                               AArbSEG2: int,
                               AArbPrescaler: int,
                               AArbSJ2: int, ADataBaudrateKbps: float, ADataSEG1: int, ADataSEG2: int,
                               ADataPrescaler: int,
                               ADataSJ2: int, AControllerType: TLIBCANFDControllerType,
                               AControllerMode: TLIBCANFDControllerMode,
                               AInstallTermResistor120Ohm: c_bool):
    r = dll.tscan_configure_canfd_regs(ADeviceHandle, AIdxChn, c_float(AArbBaudrateKbps), c_uint32(AArbSEG1),
                                       c_uint32(AArbSEG2),
                                       c_uint32(AArbPrescaler), c_uint32(
                                           AArbSJ2),
                                       c_float(ADataBaudrateKbps), c_uint32(
                                           ADataSEG1),
                                       c_uint32(ADataSEG2), c_uint32(
                                           ADataPrescaler), c_uint32(ADataSJ2),
                                       AControllerType,
                                       AControllerMode,
                                       AInstallTermResistor120Ohm)
    return r


# 设置lin参数
def tsapp_configure_baudrate_lin(ADeviceHandle: c_size_t, AChnIdx: CHANNEL_INDEX, ARateKbps: c_double):
    r = dll.tslin_config_baudrate(ADeviceHandle, AChnIdx, ARateKbps)
    return r


# lin设置主节炄1 7
def tsapp_set_node_funtiontype(ADeviceHandle: c_size_t, AChnIdx: CHANNEL_INDEX, AFunctionType: T_LIN_NODE_FUNCTION):
    r = dll.tslin_set_node_funtiontype(ADeviceHandle, AChnIdx, AFunctionType)
    return r


# 下载ldf
def tsapp_apply_download_new_ldf(ADeviceHandle: c_size_t, AChnIdx: CHANNEL_INDEX):
    r = dll.tslin_apply_download_new_ldf(ADeviceHandle, AChnIdx)
    return r


# 异步发  can报文
def tsapp_transmit_can_async(AHandle: c_size_t, Msg: TLIBCAN):
    r = dll.tscan_transmit_can_async(AHandle, byref(Msg))
    if r != 0:
        print("msg send failed")
    return r


# 同步发  can报文
def tsapp_transmit_can_sync(AHandle: c_size_t, Msg: TLIBCAN, ATimeoutMS: c_int32):
    if not isinstance(ATimeoutMS, c_int32):
        ATimeoutMS = c_float(ATimeoutMS)
    r = dll.tscan_transmit_can_sync(AHandle, byref(Msg), ATimeoutMS)
    if r != 0:
        print("msg send failed")
    return r


# 异步发  canfd报文
def tsapp_transmit_canfd_async(AHandle: c_size_t, Msg: TLIBCANFD):
    r = dll.tscan_transmit_canfd_async(AHandle, byref(Msg))
    if r != 0:
        print("msg send failed")
    return r


# 同步发  canfd报文
def tsapp_transmit_canfd_sync(AHandle: c_size_t, Msg: TLIBCANFD, ATimeoutMS: c_int32):
    if not isinstance(ATimeoutMS, c_int32):
        ATimeoutMS = c_float(ATimeoutMS)
    r = dll.tscan_transmit_canfd_sync(AHandle, byref(Msg), ATimeoutMS)
    if r != 0:
        print("msg send failed")
    return r


# 循环发  canfd报文
def tscan_add_cyclic_msg_canfd(AHandle: c_size_t, Msg: TLIBCANFD, ATimeoutMS: c_float):
    if not isinstance(ATimeoutMS, c_float):
        ATimeoutMS = c_float(ATimeoutMS)
    r = dll.tscan_add_cyclic_msg_canfd(AHandle, byref(Msg), ATimeoutMS)
    if r != 0:
        print("msg send failed")
    return r


# 删除循环发  canfd报文
def tscan_delete_cyclic_msg_canfd(AHandle: c_size_t, Msg: TLIBCANFD):
    r = dll.tscan_delete_cyclic_msg_canfd(AHandle, byref(Msg))
    return r


# 周期发  canfd报文
def tscan_add_cyclic_msg_can(AHandle: c_size_t, Msg: TLIBCAN, ATimeoutMS: c_float):
    if not isinstance(ATimeoutMS, c_float):
        ATimeoutMS = c_float(ATimeoutMS)
    r = dll.tscan_add_cyclic_msg_can(AHandle, byref(Msg), ATimeoutMS)
    if r != 0:
        print("msg send failed")
    return r


# 删除循环发  can报文
def tscan_delete_cyclic_msg_can(AHandle: c_size_t, Msg: TLIBCAN):
    r = dll.tscan_delete_cyclic_msg_can(AHandle, byref(Msg))
    return r


# 异步发  lin报文
def tsapp_transmit_lin_async(AHandle: c_size_t, Msg: TLIBLIN):
    r = dll.tslin_transmit_lin_async(AHandle, byref(Msg))
    if r != 0:
        print("msg send failed")
    return r


# 同步发  lin报文
def tsapp_transmit_lin_sync(AHandle: c_size_t, Msg: TLIBLIN, ATimeoutMS: c_int32):
    r = dll.tslin_transmit_lin_sync(AHandle, byref(Msg), ATimeoutMS)
    return r


# can报文接收
def tsapp_receive_can_msgs(AHandle: c_size_t, ACANBuffers: TLIBCAN, ACANBufferSize: c_uint32, AChn: CHANNEL_INDEX,
                           ARxTx: READ_TX_RX_DEF):
    r = dll.tsfifo_receive_can_msgs(
        AHandle, ACANBuffers, byref(ACANBufferSize), AChn, ARxTx)
    return r


# canfd报文接收
def tsapp_receive_canfd_msgs(AHandle: c_size_t, ACANFDBuffers: TLIBCANFD, ACANFDBufferSize: c_uint32,
                             AChn: CHANNEL_INDEX,
                             ARxTx: READ_TX_RX_DEF):
    r = dll.tsfifo_receive_canfd_msgs(
        AHandle, ACANFDBuffers, byref(ACANFDBufferSize), AChn, ARxTx)

    return r


# lin报文接收
def tsapp_receive_lin_msgs(AHandle: c_size_t, ALINBuffers: TLIBLIN, ALINBufferSize: c_uint, AChn: CHANNEL_INDEX,
                           ARxTx: READ_TX_RX_DEF):
    temp = copy.copy(ALINBufferSize)
    data = POINTER(TLIBLIN * len(ALINBuffers)
                   )((TLIBLIN * len(ALINBuffers))(*ALINBuffers))
    r = dll.tsfifo_receive_lin_msgs(AHandle, data, byref(temp), AChn, ARxTx)
    for i in range(len(data.contents)):
        ALINBuffers[i] = data.contents[i]
    return r


# 清除buffer
def tsfifo_clear_can_receive_buffers(AHandle: c_size_t, CHN: CHANNEL_INDEX):
    return dll.tsfifo_clear_can_receive_buffers(AHandle, CHN)


def tsfifo_clear_canfd_receive_buffers(AHandle: c_size_t, CHN: CHANNEL_INDEX):
    return dll.tsfifo_clear_canfd_receive_buffers(AHandle, CHN)


def tsfifo_clear_lin_receive_buffers(AHandle: c_size_t, CHN: CHANNEL_INDEX):
    return dll.tsfifo_clear_lin_receive_buffers(AHandle, CHN)


# 回调事件
PCAN = POINTER(TLIBCAN)
if 'windows' in _os.lower():
    OnTx_RxFUNC_CAN = WINFUNCTYPE(None, PCAN)
else:
    OnTx_RxFUNC_CAN = CFUNCTYPE(None, PCAN)

PFlexray = POINTER(TLIBFlexray)
if 'windows' in _os.lower():
    OnTx_RxFUNC_Flexray = WINFUNCTYPE(None, PFlexray)
else:
    OnTx_RxFUNC_Flexray = CFUNCTYPE(None, PFlexray)

PLIN = POINTER(TLIBLIN)
if 'windows' in _os.lower():
    OnTx_RxFUNC_LIN = WINFUNCTYPE(None, PLIN)
else:
    OnTx_RxFUNC_LIN = CFUNCTYPE(None, PLIN)

PCANFD = POINTER(TLIBCANFD)
if 'windows' in _os.lower():
    OnTx_RxFUNC_CANFD = WINFUNCTYPE(None, PCANFD)
else:
    OnTx_RxFUNC_CANFD = CFUNCTYPE(None, PCANFD)

if 'windows' in _os.lower():
    On_Connect_FUNC = WINFUNCTYPE(None, POINTER(c_int64))
else:
    On_Connect_FUNC = CFUNCTYPE(None, POINTER(c_int64))

if 'windows' in _os.lower():
    On_disConnect_FUNC = WINFUNCTYPE(None, POINTER(c_int64))
else:
    On_disConnect_FUNC = CFUNCTYPE(None, POINTER(c_int64))

blfName = ''
blf_start_time = 0


def blfFile(pathName):
    global blf_start_time
    blf_start_time += time.time()
    blfName = can.BLFWriter(file=pathName, append=False)
    blfName.start_timestamp = blf_start_time
    return blfName


def On_CANFD_EVENT(ACAN):
    global blf_start_time
    msg = tosun_convert_msg(ACAN.contents)
    blfName(msg)


On_LOG_EVENT = OnTx_RxFUNC_CANFD(On_CANFD_EVENT)


def tslog_start(AHandle: c_size_t, filePathName: str):
    global blfName
    blfName = blfFile(filePathName)
    if 0 == tsapp_register_event_canfd(AHandle, On_LOG_EVENT):
        print("start logging")
    else:
        print('start logging failed')


def tslog_stop():
    global blfName
    global blf_start_time
    blfName.stop_timestamp = time.time()
    blfName.stop()
    print("stop logging")
    blf_start_time = 0


def blf_to_convert(oldpathName: str, newpathName: str,
                   convertType: CONVERTTYPE):  # oldpathName:blf location, newpathName: asc location
    if convertType == CONVERTTYPE.ASC:
        with can.BLFReader(oldpathName) as Reader_file:
            with can.ASCWriter(newpathName) as WriterFile:
                for msg in Reader_file:
                    WriterFile(msg)
                WriterFile.stop()
    elif convertType == CONVERTTYPE.CSV:
        with can.BLFReader(oldpathName) as Reader_file:
            with can.CSVWriter(newpathName) as WriterFile:
                for msg in Reader_file:
                    WriterFile(msg)
                WriterFile.stop()
    elif convertType == CONVERTTYPE.LOG:
        with can.BLFReader(oldpathName) as Reader_file:
            with can.CanutilsLogWriter(newpathName) as WriterFile:
                for msg in Reader_file:
                    WriterFile(msg)
                WriterFile.stop()
    elif convertType == CONVERTTYPE.TXT:
        with can.BLFReader(oldpathName) as Reader_file:
            with can.Printer(newpathName) as WriterFile:
                for msg in Reader_file:
                    WriterFile(msg)
                WriterFile.stop()
    elif convertType == CONVERTTYPE.SQL:
        with can.BLFReader(oldpathName) as Reader_file:
            with can.SqliteWriter(newpathName) as WriterFile:
                for msg in Reader_file:
                    WriterFile(msg)
                WriterFile.stop()
    else:
        print("incorrect format")


def tslog_start_online_replay(handle: c_size_t, PathFileName: str, include_rx: bool):
    messagelist = []
    with can.BLFReader(PathFileName) as Reader_file:
        Reader_file.start_timestamp = 0
        for msg in Reader_file:
            for i in range(len(DLC_DATA_BYTE_CNT)):
                if msg.dlc == DLC_DATA_BYTE_CNT[i]:
                    msg.dlc = i
            if include_rx:
                messagelist.append(msg)
            else:
                if msg.is_rx:
                    continue
                messagelist.append(msg)
        listlen = len(messagelist)
        print(listlen)
        for i in range(listlen):
            if messagelist[i].is_fd:
                TCANFD = TLIBCANFD(FIdxChn=messagelist[i].channel, FIdentifier=messagelist[i].arbitration_id,
                                   FFDProperties=1, FDLC=messagelist[i].dlc,
                                   FData=messagelist[i].data)
                # TCANFD.FTimeUs = msg.timestamp
                tsapp_transmit_canfd_async(handle, TCANFD)
                if i == listlen - 1:
                    break
                time.sleep(messagelist[i + 1].timestamp -
                           messagelist[i].timestamp)
            else:
                TCAN = TLIBCAN(FIdxChn=messagelist[i].channel, FIdentifier=messagelist[i].arbitration_id,
                               FDLC=messagelist[i].dlc,
                               FData=messagelist[i].data)
                # TCAN.FTimeUs = msg.timestamp
                tsapp_transmit_can_async(handle, TCAN)
                if i == listlen - 1:
                    break
                time.sleep(messagelist[i + 1].timestamp -
                           messagelist[i].timestamp)


def Reader_file(PathName, convertType: CONVERTTYPE):
    if convertType == CONVERTTYPE.ASC:
        with can.BLFReader(PathName) as Reader_file:
            Reader_file.start_timestamp = 0
            for msg in Reader_file:
                print(msg)
    elif convertType == CONVERTTYPE.CSV:
        with can.CSVReader(PathName) as Reader_file:
            Reader_file.start_timestamp = 0
            for msg in Reader_file:
                print(msg)
    elif convertType == CONVERTTYPE.LOG:
        with can.CanutilsLogReader(PathName) as Reader_file:
            Reader_file.start_timestamp = 0
            for msg in Reader_file:
                print(msg)
    elif convertType == CONVERTTYPE.TXT:
        with can.CSVReader(PathName) as Reader_file:
            Reader_file.start_timestamp = 0
            for msg in Reader_file:
                print(msg)
    elif convertType == CONVERTTYPE.SQL:
        with can.SqliteReader(PathName) as Reader_file:
            Reader_file.start_timestamp = 0
            for msg in Reader_file:
                print(msg)
    elif convertType == CONVERTTYPE.BLF:
        with can.BLFReader(PathName) as Reader_file:
            Reader_file.start_timestamp = 0
            for msg in Reader_file:
                print(msg)
    else:
        print("incorrect format")


# 注册连接事件
def tscan_register_event_connected(ACallback: On_Connect_FUNC):
    ret = dll.tscan_register_event_connected(ACallback)
    return ret


# 注册断开事件
def tscan_register_event_disconnected(ACallback: On_Connect_FUNC):
    ret = dll.tscan_register_event_disconnected(ACallback)
    return ret


# 注册can发  接收事仄1 7
def tsapp_register_event_can(AHandle: c_size_t, ACallback: OnTx_RxFUNC_CAN):
    r = dll.tscan_register_event_can(AHandle, ACallback)
    return r


# 注销can发  接收事仄1 7
def tsapp_unregister_event_can(AHandle: c_size_t, ACallback: OnTx_RxFUNC_CAN):
    r = dll.tscan_unregister_event_can(AHandle, ACallback)
    return r

def tsapp_register_pretx_event_can(AHandle: c_size_t, ACallback: OnTx_RxFUNC_CAN):
    return dll.tscan_register_pretx_event_can(AHandle, ACallback)

def tsapp_unregister_pretx_event_can(AHandle: c_size_t, ACallback: OnTx_RxFUNC_CAN):
    return dll.tscan_unregister_pretx_event_can(AHandle, ACallback)

def tsapp_register_pretx_event_canfd(AHandle: c_size_t, ACallback: OnTx_RxFUNC_CANFD):
    return dll.tscan_register_pretx_event_canfd(AHandle, ACallback)

def tsapp_unregister_pretx_event_canfd(AHandle: c_size_t, ACallback: OnTx_RxFUNC_CANFD):
    return dll.tscan_unregister_pretx_event_canfd(AHandle, ACallback)


# 注册canfd发  接收事仄1 7
def tsapp_register_event_canfd(AHandle: c_size_t, ACallback: OnTx_RxFUNC_CANFD):
    r = dll.tscan_register_event_canfd(AHandle, ACallback)
    return r

# 注销canfd发  接收事仄1 7
def tsapp_unregister_event_canfd(AHandle: c_size_t, ACallback: OnTx_RxFUNC_CANFD):
    r = dll.tscan_unregister_event_canfd(AHandle, ACallback)
    return r

def tsapp_register_event_flexray(AHandle: c_size_t, ACallback: OnTx_RxFUNC_Flexray):
    r = dll.tsflexray_register_event_flexray(AHandle, ACallback)
    return r


# 注销flexray发  接收
def tsapp_unregister_event_flexray(AHandle: c_size_t, ACallback: OnTx_RxFUNC_Flexray):
    r = dll.tsflexray_unregister_event_flexray(AHandle, ACallback)
    return r

def tsapp_register_pretx_event_flexray(AHandle: c_size_t, ACallback: OnTx_RxFUNC_Flexray):
    r = dll.tsflexray_register_pretx_event_flexray(AHandle, ACallback)
    return r


# 注销flexray预发送事件
def tsapp_unregister_pretx_event_flexray(AHandle: c_size_t, ACallback: OnTx_RxFUNC_Flexray):
    r = dll.tsflexray_unregister_pretx_event_flexray(AHandle, ACallback)
    return r


# 注册lin发 接事件
def tsapp_register_event_lin(AHandle: c_size_t, ACallback: OnTx_RxFUNC_LIN):
    r = dll.tslin_register_event_lin(AHandle, ACallback)
    return r


# 注销lin发 接事件
def tsapp_unregister_event_lin(AHandle: c_size_t, ACallback: OnTx_RxFUNC_LIN):
    r = dll.tslin_unregister_event_lin(AHandle, ACallback)
    return r

def tsapp_register_pretx_event_lin(AHandle: c_size_t, ACallback: OnTx_RxFUNC_LIN):
    return dll.tslin_register_pretx_event_can(AHandle, ACallback)

def tsapp_unregister_pretx_event_lin(AHandle: c_size_t, ACallback: OnTx_RxFUNC_LIN):
    return dll.tslin_unregister_pretx_event_lin(AHandle, ACallback)

# normal_rx_msg = queue.Queue(maxsize=0)
# error_rx_msg = queue.Queue(maxsize=0)
# normal_rx_tx_msg = queue.Queue(maxsize=0)
# error_rx_tx_msg = queue.Queue(maxsize=0)
#
# def on_tx_rx_event(ACAN):
#     if ACAN.contents.FProperties == 0x80:
#         msg = Message(timestamp=blf_start_time + float(ACAN.contents.FTimeUs) / 1000000, arbitration_id=0xFFFFFFFF,
#                       is_error_frame=True, data=[0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff])
#         error_rx_msg.put(msg)
#         error_rx_tx_msg.put(msg)
#     elif ACAN.contents.FProperties & 1:
#         msg = tosun_convert_msg(ACAN.contents)
#         error_rx_tx_msg.put(msg)
#         normal_rx_tx_msg.put(msg)
#     else:
#         msg = tosun_convert_msg(ACAN.contents)
#         error_rx_msg.put(msg)
#         error_rx_tx_msg.put(msg)
#         normal_rx_msg.put(msg)
class TSuds():
    msg_list = queue.Queue(maxsize=10000)

    def __init__(self, HwHandle, channel=0, dlc=8, request_id=0x1, respond_id=0x2, is_fd=False, is_std=True,
                 fuction_id=0x3, timeout=0.1, bitrate_switch=False):
        self.HwHandle = HwHandle
        self.channel = channel
        try:
            self.dlc = DLC_DATA_BYTE_CNT.index(dlc)
        except:
            if dlc < 0x10:
                self.dlc = dlc
        self.is_fd = is_fd
        if not self.is_fd and self.dlc > 8:
            self.dlc = 8
        self.is_std = is_std
        self.bitrate_switch = bitrate_switch
        self.FFDProperties = 0x00 | (0x01 if self.is_fd else 0x00) | (
            0x02 if self.bitrate_switch else 0x00)
        self.FProperties = 0x01 | (0x04 if not self.is_std else 0x01)
        self.request_id = request_id
        self.respond_id = respond_id
        self.fuction_id = fuction_id
        self.timeout = timeout
        self.msg_data_size = DLC_DATA_BYTE_CNT[self.dlc]
        self.CANFDMsg = TLIBCANFD(FIdxChn=self.channel, FDLC=self.dlc, FIdentifier=self.request_id,
                                  FFDProperties=self.FFDProperties, FProperties=self.FProperties,
                                  FData=[0X30, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00])
        self.ONRxTx_Event = OnTx_RxFUNC_CANFD(self.on_tx_rx_event)
        tsapp_register_event_canfd(self.HwHandle, self.ONRxTx_Event)

    def on_tx_rx_event(self, ACAN):
        if ACAN.contents.FIdentifier == self.respond_id and ACAN.contents.FIdxChn == self.channel:
            msgdata = []
            for i in range(DLC_DATA_BYTE_CNT[ACAN.contents.FDLC]):
                msgdata.append(ACAN.contents.FData[i])
            self.msg_list.put(msgdata)

    def receive_can_Response(self):
        Datalist = []
        StartTime = time.perf_counter()
        FristDataLength = self.msg_data_size - 2
        DataLength = self.msg_data_size - 1
        while time.perf_counter() - StartTime < self.timeout:
            time.sleep(0.001)
            if not self.msg_list.empty():
                msgs = self.msg_list.get()
                N_PCItype = msgs[0] >> 4
                if 0 == N_PCItype:
                    if len(msgs) <= 8:
                        ResSize = (msgs[0] & 0xf)
                        if msgs[1] == 0x7f and msgs[3] == 0x78:
                            StartTime = time.perf_counter()
                            continue
                        for i in range(ResSize):
                            Datalist.append(msgs[i + 1])
                        return 0, Datalist
                    else:
                        ResSize = (msgs[1] & 0xff)
                        if msgs[2] == 0x7f and msgs[4] == 0x78:
                            StartTime = time.perf_counter()
                            continue
                        for i in range(ResSize):
                            Datalist.append(msgs[i + 2])
                        return 0, Datalist
                elif 1 == N_PCItype:
                    ResSize = (msgs[0] & 0xf) * 256 + msgs[1]
                    for i in range(len(msgs) - 2):
                        Datalist.append(msgs[i + 2])
                    if 0 == tsapp_transmit_canfd_async(self.HwHandle, self.CANFDMsg):
                        snCnt = 0x1
                        rxIndex = len(msgs) - 2
                        while rxIndex < ResSize and time.perf_counter() - StartTime < self.timeout:
                            if not self.msg_list.empty():
                                msgs = self.msg_list.get()
                                N_PCItype = msgs[0] >> 4
                                if N_PCItype != 2:
                                    break
                                rxSN = msgs[0] & 0xf
                                if rxSN != snCnt & 0xf:
                                    break
                                snCnt += 1
                                if len(Datalist) != ResSize:
                                    if len(msgs) - 1 < ResSize - len(Datalist):
                                        for i in range(len(msgs) - 1):
                                            Datalist.append(msgs[i + 1])
                                        StartTime = time.perf_counter()
                                    else:
                                        for i in range(ResSize - len(Datalist)):
                                            Datalist.append(msgs[i + 1])
                                        StartTime = time.perf_counter()
                                else:
                                    return 0, Datalist
        return 161, Datalist

    def tstp_can_send_request(self, SendDatas):
        CANMsg = TLIBCANFD(FIdxChn=self.channel, FDLC=self.dlc, FIdentifier=self.request_id,
                           FFDProperties=self.FFDProperties, FProperties=self.FProperties,
                           )
        txIndex = self.msg_data_size - 2
        Datalengh = self.msg_data_size - 1
        MsgLen = len(SendDatas)
        if MsgLen <= Datalengh:
            if self.msg_data_size == self.dlc:
                CANMsg.FData[0] = MsgLen
                for i in range(MsgLen):
                    CANMsg.FData[i + 1] = SendDatas[i]
                return tsapp_transmit_canfd_async(self.HwHandle, CANMsg)
            else:
                if MsgLen <= Datalengh - 1:
                    for i in range(8, self.dlc):
                        if MsgLen < DLC_DATA_BYTE_CNT[i]:
                            CANMsg.FDLC = i
                            break
                    if CANMsg.FDLC == 8:
                        CANMsg.FData[0] = MsgLen
                        for i in range(MsgLen):
                            CANMsg.FData[i + 1] = SendDatas[i]
                        return tsapp_transmit_canfd_async(self.HwHandle, CANMsg)
                    else:
                        CANMsg.FData[0] = 0x00
                        CANMsg.FData[1] = MsgLen
                        for i in range(MsgLen):
                            CANMsg.FData[i + 2] = SendDatas[i]
                        return tsapp_transmit_canfd_async(self.HwHandle, CANMsg)
        CANMsg.FDLC = self.dlc
        CANMsg.FData[0] = 0x10 + (MsgLen >> 8 & 0xf)
        CANMsg.FData[1] = MsgLen & 0xff
        for i in range(txIndex):
            CANMsg.FData[i + 2] = SendDatas[i]
        if 0 == tsapp_transmit_canfd_async(self.HwHandle, CANMsg):
            Datalist = []
            snCnt = 1
            StartTime = time.perf_counter()
            while time.perf_counter() - StartTime < self.timeout:
                if not self.msg_list.empty():
                    msgs = self.msg_list.get()
                    if msgs[0] == 0x30:
                        while txIndex < MsgLen:
                            CANMsg.FData[0] = (0x20 | (snCnt & 0xf))
                            snCnt += 1
                            txLen = MsgLen - txIndex
                            if txLen > Datalengh:
                                txLen = Datalengh
                            else:
                                for i in range(txLen, Datalengh):
                                    CANMsg.FData[i + 1] = 0xAA
                            for i in range(txLen):
                                CANMsg.FData[i + 1] = SendDatas[i + txIndex]
                            if tsapp_transmit_canfd_async(self.HwHandle, CANMsg) != 0:
                                break
                            txIndex += txLen
                            if txIndex >= MsgLen:
                                return 0
                        return 161
            else:
                return 161

    def tstp_can_request_and_get_response(self, SendDatas):
        self.msg_list.queue.clear()
        ret = self.tstp_can_send_request(SendDatas)
        if ret == 0:
            ret, recv_data = self.receive_can_Response()
        else:
            return ret, []
        return ret, bytes(recv_data)


class DBC_parse():
    dbc_list_by_name = {}
    dbc_signal_list = {}
    filenames = []
    dbc_list_by_id = {}

    def __init__(self, dbcfile=''):
        self.load_dbc(dbcfile)

    def load_dbc(self, dbcfile):
        '''return db index'''
        if dbcfile != '':
            data_path, filename = os.path.split(dbcfile)
            if filename not in self.filenames:
                self.filenames.append(filename)
            else:
                print(filename, " already exists")
                return
            try:
                db = cantools.db.load_file(dbcfile)
                for msg in db.messages:
                    if (msg.name not in self.dbc_list_by_name) and (msg.frame_id not in self.dbc_list_by_id):
                        self.dbc_list_by_name[msg.name] = msg
                        self.dbc_list_by_id[msg.frame_id] = msg
                        self.dbc_signal_list[msg.name] = msg.signals
                    else:
                        print(msg.name, ' already exists')

            except Exception as e:
                print(e)

    def __change_msg(self, msg):
        if msg.data == b'' or msg.dlc != self.dbc_list_by_id[msg.arbitration_id].length:
            datalist = []
            msg.is_fd = self.dbc_list_by_id[msg.arbitration_id]._is_fd
            msg.is_extended_id = self.dbc_list_by_id[msg.arbitration_id]._is_extended_frame
            msg.dlc = self.dbc_list_by_id[msg.arbitration_id]._length
            msg.bitrate_switch = self.dbc_list_by_id[msg.arbitration_id]._bitrate_switch
            for i in range(msg.dlc):
                datalist.append(0)
            msg.data = datalist
            del datalist

    def __change_signal_value(self, msg, signal_dict: dict):
        try:
            self.__change_msg(msg)
            msg_data_dict = self.dbc_list_by_id[msg.arbitration_id].decode(
                data=msg.data)
            for key in signal_dict:
                if key in msg_data_dict:
                    msg_data_dict[key] = signal_dict[key]
                else:
                    print('signal not exist')
                    return msg
            msg.data = self.dbc_list_by_id[msg.arbitration_id].encode(
                msg_data_dict)
            return msg
        except Exception as e:
            print(e)

    def set_signal_value_by_id(self, channel_index, msg_id, signal_dict: dict):
        if msg_id in self.dbc_list_by_id:
            msg = Message(arbitration_id=msg_id, channel=channel_index)
            return msg_convert_tosun(self.__change_signal_value(msg, signal_dict))

    def set_signal_value_by_name(self, channel_index, msgname: str, signal_dict: dict):
        if msgname in self.dbc_list_by_name:
            msg = Message(
                arbitration_id=self.dbc_list_by_name[msgname]._frame_id, channel=channel_index)
            return msg_convert_tosun(self.__change_signal_value(msg, signal_dict))

    def get_signal_value(self, msg, signalname):
        try:
            if isinstance(msg, Message):
                signaldict = self.dbc_list_by_id[msg.arbitration_id].decode(
                    data=msg.data)

            elif isinstance(msg, TLIBCAN) or isinstance(msg, TLIBCANFD):
                signaldict = self.dbc_list_by_id[msg.FIdentifier].decode(
                    data=bytes(msg.FData))
            else:
                signaldict = {}
            if signalname:
                if signalname in signaldict:
                    return signaldict[signalname]
                else:
                    print("signal not exist")
                    return None
            else:
                return signaldict
        except Exception as e:
            print(e)


class TSMasterDevice():
    HwHandle = c_size_t(0)
    channel_list = []
    Rate_baudrate = []
    data_baudrate = []
    enable_120hm = []
    configs = {}
    __hw_isconnect = False
    include_own_message = False
    __include_error_message = False
    msg_list = queue.Queue(maxsize=100000)
    error_code = {1: "Index out of range",
                2: "Connect failed",
                3: "Device not found",
                4: "Error code not valid",
                5: "HID device already connected",
                6: "HID write data failed",
                7: "HID read data failed",
                8: "HID TX buffer overrun",
                9: "HID TX buffer too large",
                10: "HID RX packet report ID invalid",
                11: "HID RX packet length invalid",
                12: "Internal test failed",
                13: "RX packet lost",
                14: "SetupDiGetDeviceInterfaceDetai",
                15: "Create file failed",
                16: "CreateFile failed for read handle",
                17: "CreateFile failed for write handle",
                18: "HidD_SetNumInputBuffers",
                19: "HidD_GetPreparsedData",
                20: "HidP_GetCaps",
                21: "WriteFile",
                22: "GetOverlappedResult",
                23: "HidD_SetFeature",
                24: "HidD_GetFeature",
                25: "Send Feature Report DeviceIoContro",
                26: "Send Feature Report GetOverLappedResult",
                27: "HidD_GetManufacturerString",
                28: "HidD_GetProductString",
                29: "HidD_GetSerialNumberString",
                30: "HidD_GetIndexedString",
                31: "Transmit timed out",
                32: "HW DFU flash write failed",
                33: "HW DFU write without erase",
                34: "HW DFU crc check error",
                35: "HW DFU reset before crc check success",
                36: "HW packet identifier invalid",
                37: "HW packet length invalid",
                38: "HW internal test failed",
                39: "HW rx from pc packet lost",
                40: "HW tx to pc buffer overrun",
                41: "HW API parameter invalid",
                42: "DFU file load failed",
                43: "DFU header write failed",
                44: "Read status timed out",
                45: "Callback already exists",
                46: "Callback not exists",
                47: "File corrupted or not recognized",
                48: "Database unique id not found",
                49: "Software API parameter invalid",
                50: "Software API generic timed out",
                51: "Software API set hw config. failed",
                52: "Index out of bounds",
                53: "RX wait timed out",
                54: "Get I/O failed",
                55: "Set I/O failed",
                56: "An active replay is already running",
                57: "Instance not exists",
                58: "CAN message transmit failed",
                59: "No response from hardware",
                60: "CAN message not found",
                61: "User CAN receive buffer empty",
                62: "CAN total receive count <> desired count",
                63: "LIN config failed",
                64: "LIN frame number out of range",
                65: "LDF config failed",
                66: "LDF config cmd error",
                67: "TSMaster envrionment not ready",
                68: "reserved failed",
                69: "XL driver error",
                70: "index out of range",
                71: "string length out of range",
                72: "key is not initialized",
                73: "key is wrong",
                74: "write not permitted",
                75: "16 bytes multiple",
                76: "LIN channel out of range",
                77: "DLL not ready",
                78: "Feature not supported",
                79: "common service error",
                80: "read parameter overflow",
                81: "Invalid application channel mapping",
                82: "libTSMaster generic operation failed",
                83: "item already exists",
                84: "item not found",
                85: "logical channel invalid",
                86: "file not exists",
                87: "no init access, cannot set baudrate",
                88: "the channel is inactive",
                89: "the channel is not created",
                90: "length of the appname is out of range",
                91: "project is modified",
                92: "signal not found in database",
                93: "message not found in database",
                94: "TSMaster is not installed",
                95: "Library load failed",
                96: "Library function not found",
                97: 'cannot find libTSMaster.dll, use \"set_libtsmaster_location\" to set its location before calling initialize_lib_tsmaster',
                98: "PCAN generic operation error",
                99: "Kvaser generic operation error",
                100: "ZLG generic operation error",
                101: "ICS generic operation error",
                102: "TC1005 generic operation error",
                104: "Incorrect system variable type",
                105: "Message not existing, update failed",
                106: "Specified baudrate not available",
                107: "Device does not support sync. transmit",
                108: "Wait time not satisfied",
                109: "Cannot operate while app is connected",
                110: "Create file failed",
                111: "Execute python failed",
                112: "Current multiplexed signal is not active",
                113: "Get handle by logic channel failed",
                114: "Cannot operate while application is Connected, please stop application first",
                115: "File load failed",
                116: "Read LIN Data Failed",
                117: "FIFO not enabled",
                118: "Invalid handle",
                119: "Read file error",
                120: "Read to EOF",
                121: "Configuration not saved",
                122: "IP port open failed",
                123: "TCP connect failed",
                124: "Directory not exists",
                125: "Current library not supported",
                126: "Test is not running",
                127: "Server response not received",
                128: "Create directory failed",
                129: "Invalid argument type",
                130: "Read Data Package from Device Failed",
                131: "Precise replay is running",
                132: "Replay map is already",
                133: "User cancel input",
                134: "API check result is negative",
                135: "CANable generic error",
                136: "Wait criteria not satisfied",
                137: "Operation requires application connected",
                138: "Project path is used by another application",
                139: "Timeout for the sender to transmit data to the receiver",
                140: "Timeout for the receiver to transmit flow control to the sender",
                141: "Timeout for the sender to send first data frame after receiving FC frame",
                142: "Timeout for the receiver to receiving first CF frame after sending FC frame",
                143: "Serial Number Error",
                144: "Invalid flow status of the flow control frame",
                145: "Unexpected Protocol Data Unit",
                146: "Wait counter of the FC frame out of the maxWFT",
                147: "Buffer of the receiver is overflow",
                148: "TP Module is busy",
                149: "There is error from CAN Driver",
                150: "Handle of the TP Module is not exist",
                151: "UDS event buffer is full",
                152: "Handle pool is full, can not add new UDS module",
                153: "Pointer of UDS module is null",
                154: "UDS message is invalid",
                155: "No uds data received",
                156: "Handle of uds is not existing",
                157: "UDS module is not ready",
                158: "Transmit uds frame data failed",
                159: "This uds Service is not supported",
                160: "Time out to send uds request",
                161: "Time out to get uds response",
                162: "Get uds negative response",
                163: "Get uds negative response with expected NRC",
                164: "Get uds negative response with unexpected NRC",
                165: "UDS can tool is not ready",
                166: "UDS data is out of range",
                167: "Get unexpected UDS frame",
                168: "Receive unexpected positive response frame",
                169: "Receive positive response with wrong data",
                170: "Failed to get positive response",
                171: "Reserved UDS Error Code",
                172: "Receive negative response with unexpected NRC",
                173: "UDS service is busy",
                174: "Request download service must be performed before transfer data",
                175: "Length of the uds reponse is wrong",
                176: "Verdict value smaller than specification",
                177: "Verdict value greater than specification",
                178: "Verdict check failed",
                179: "Automation module not loaded, please load it first",
                180: "Panel not found",
                181: "Control not found in panel",
                182: "Panel not loaded, please load it first",
                183: "STIM signal not found",
                184: "Automation sub module not available",
                185: "Automation variant group not found",
                186: "Control not found in panel",
                187: "Panel control does not support this property",
                188: "RBS engine is not running",
                189: "This message does not support PDU container",
                190: "Data not available",
                191: "J1939 not supported",
                192: "Another J1939 PDU is already being transmitted",
                193: "Transmit J1939 PDU failed due to protocol error",
                194: "Transmit J1939 PDU failed due to node inactive",
                195: "API is called without license support",
                196: "Signal range check violation",
                197: "DataLogger read category failed",
                198: "Check Flash Bootloader Version Failed",
                199: "Log file not created",
                200: "Module is being edited by user",
                201: "The Logger device is busy, can not operation at the same time",
                202: "Master node transmit diagnostic package timeout",
                203: "Master node transmit frame failed",
                204: "Master node receive diagnostic package timeout",
                205: "Master node receive frame failed",
                206: "Internal time runs out before reception is completed ",
                207: "Master node received no response ",
                208: "Serial Number Error when receiving multi frames",
                209: "Slave node transmit diagnostic package timeout",
                210: "Slave node receive diagnostic pacakge timeout",
                211: "Slave node transmit frames error",
                212: "Slave node receive frames error",
                }
    db = None
    onRXTX_EVENT = OnTx_RxFUNC_CANFD()
    start_receive = False

    def __init__(self, configs: [dict], hwserial: bytes = b'',
                # is_recv_error: bool = False,
                is_include_tx: bool = False,
                # is_start_recv: bool = False,
                dbc: bytes = b'',
                filter:dict={}):
        self.filter = filter
        # self.__include_error_message = is_recv_error
        self.include_own_message = is_include_tx
        # self.start_receive = is_start_recv
        self.configs = configs
        self.hwserial = hwserial
        self.dbc = dbc
        # initialize_lib_tsmaster(True, False)
        if isinstance(hwserial, str):
            self.hwserial = hwserial.encode('utf8')
        self.connect()
        # ret = tsapp_connect(hwserial, self.HwHandle)
        # if ret == 0 or ret == 5:
        #     self.__hw_isconnect = True
        #     for index, congfig in enumerate(configs):
        #         self.channel_list.append(
        #             congfig['FChannel'] if 'FChannel' in congfig else index)

        #         self.Rate_baudrate.append(
        #             congfig['rate_baudrate'] if 'rate_baudrate' in congfig else 500)

        #         self.data_baudrate.append(
        #             congfig['data_baudrate'] if 'data_baudrate' in congfig else 2000)

        #         self.enable_120hm.append(
        #             congfig['enable_120hm'] if 'enable_120hm' in congfig else True)

        #         if 'is_fd' in congfig and congfig['is_fd']:
        #             tsapp_configure_baudrate_canfd(self.HwHandle, self.channel_list[index], self.Rate_baudrate[index],
        #                                         self.data_baudrate[index],
        #                                         TLIBCANFDControllerType.lfdtISOCAN,
        #                                         TLIBCANFDControllerMode.lfdmNormal,
        #                                         self.enable_120hm[index])
        #         else:
        #             tsapp_configure_baudrate_can(self.HwHandle, self.channel_list[index], self.Rate_baudrate[index],
        #                                         self.enable_120hm[index])
        #     self.ONRxTx_Event = OnTx_RxFUNC_CANFD(self.on_tx_rx_event)
        #     ret = tsapp_register_event_canfd(self.HwHandle, self.ONRxTx_Event)
        #     self.db = DBC_parse(dbcfile=dbc)
        # else:
        #     self.__hw_isconnect = False
        #     raise "HW CONNECT FAILED"

    def connect(self):
        ret = tsapp_connect(self.hwserial, self.HwHandle)
        if ret == 0 or ret == 5:
            self.__hw_isconnect = True
            for index, congfig in enumerate(self.configs):
                self.channel_list.append(
                    congfig['FChannel'] if 'FChannel' in congfig else index)

                self.Rate_baudrate.append(
                    congfig['rate_baudrate'] if 'rate_baudrate' in congfig else 500)

                self.data_baudrate.append(
                    congfig['data_baudrate'] if 'data_baudrate' in congfig else 2000)

                self.enable_120hm.append(
                    congfig['enable_120hm'] if 'enable_120hm' in congfig else True)

                if 'is_fd' in congfig and congfig['is_fd']:
                    tsapp_configure_baudrate_canfd(self.HwHandle, self.channel_list[index], self.Rate_baudrate[index],
                                                self.data_baudrate[index],
                                                TLIBCANFDControllerType.lfdtISOCAN,
                                                TLIBCANFDControllerMode.lfdmNormal,
                                                self.enable_120hm[index])
                else:
                    tsapp_configure_baudrate_can(self.HwHandle, self.channel_list[index], c_double(self.Rate_baudrate[index]),self.enable_120hm[index])
            # self.ONRxTx_Event = OnTx_RxFUNC_CANFD(self.on_tx_rx_event)
            # tsapp_register_event_canfd(self.HwHandle, self.ONRxTx_Event)
            # self.start_recv_time = time.perf_counter()
            if self.dbc!=b'':
                self.db = DBC_parse(dbcfile=self.dbc)
        else:
            self.__hw_isconnect = False
            raise "HW CONNECT FAILED"


    def load_dbc(self, dbc):
        self.db.load_dbc(dbc)

    def unload_dbc_all(self):
        self.db.dbc_list_by_id.clear()
        self.db.dbc_list_by_name.clear()
        self.db.dbc_signal_list.clear()

    def set_singal_value_by_id(self, channel, message_id, singaldict: [dict]):
        return self.db.set_signal_value_by_id(channel, message_id, singaldict)

    def set_singal_value_by_name(self, channel, message_name, singaldict: [dict]):
        return self.db.set_signal_value_by_name(channel, message_name, singaldict)

    def get_signal_value(self, msg, signal_name):
        return self.db.get_signal_value(msg, signal_name)

    def send_msg(self, msg, timeout: Optional[float] = 0.1, sync: bool = False, is_cyclic: bool = False):
        # timeout = timeout * 1000
        if self.__hw_isconnect:
            if isinstance(msg, TLIBCAN):
                if is_cyclic:
                    # '''timeout is cyclic time when is_cyclic is ture'''
                    tscan_add_cyclic_msg_can(
                        self.HwHandle, msg, timeout * 1000)
                else:
                    if sync:
                        tsapp_transmit_can_sync(
                            self.HwHandle, msg, timeout * 1000)
                    else:
                        tsapp_transmit_can_async(self.HwHandle, msg)
            elif isinstance(msg, TLIBCANFD):
                if is_cyclic:
                    '''timeout is cyclic time when is_cyclic is ture'''
                    tscan_add_cyclic_msg_canfd(
                        self.HwHandle, msg, timeout * 1000)
                else:
                    if sync:
                        tsapp_transmit_canfd_sync(
                            self.HwHandle, msg, timeout * 1000)
                    else:
                        tsapp_transmit_canfd_async(self.HwHandle, msg)
            elif isinstance(msg, Message):
                msg = msg_convert_tosun(msg)
                self.send_msg(msg, timeout, sync, is_cyclic)
            else:
                print("UNKOWN TYRE")
        else:
            raise "HW CONNECT FAILED"

    def recv(self, channel,timeout: Optional[float] = 0.1) -> Message:
        start_time = time.perf_counter()
        while time.perf_counter() - start_time<= timeout:
            ACANFD = (TLIBCANFD*1)()
            buffersize = c_int32(1)
            tsapp_receive_canfd_msgs(self.HwHandle,ACANFD,buffersize,channel,1 if self.include_own_message else 0)
            if buffersize.value==1:
                return tosun_convert_msg(ACANFD[0])
        return None
        return self.msg_list.get() if not self.msg_list.empty() else None

        
    
    def on_tx_rx_event(self, ACAN):
        if self.start_receive:
            msg_channel = self.filter.get('msg_channel',None)
            msg_id = self.filter.get('msg_id',None)
            # pass_no = self.filter.get('pass',True)
            if msg_channel != None and ACAN.contents.FIdxChn != msg_channel:
                return
            if msg_id != None and ACAN.contents.FIdentifier != msg_id:
                return
            if ACAN.contents.FProperties == 0x80:
                msg = Message(timestamp=blf_start_time + float(ACAN.contents.FTimeUs) / 1000000,
                            arbitration_id=0xFFFFFFFF,
                            is_error_frame=True, data=[0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff])
                if self.__include_error_message:
                    if self.msg_list.full():
                        self.msg_list.get()
                    self.msg_list.put(msg)
            elif ACAN.contents.FProperties & 1 == 1:
                if self.include_own_message:
                    msg = tosun_convert_msg(ACAN.contents)
                    if self.msg_list.full():
                        self.msg_list.get()
                    self.msg_list.put(msg)
            else:
                msg = tosun_convert_msg(ACAN.contents)
                if self.msg_list.full():
                    self.msg_list.get()
                self.msg_list.put(msg)

    def tsdiag_can_create(self, pDiagModuleIndex: c_int32, AChnIndex: CHANNEL_INDEX, ASupportFDCAN: c_byte,
                          AMaxDLC: c_byte,
                          ARequestID: c_uint32, ARequestIDIsStd: bool, AResponseID: c_uint32, AResponseIDIsStd: bool,
                          AFunctionID: c_uint32, AFunctionIDIsStd: bool, timeout=0.1):
        self.timeout = c_int32(int(timeout * 1000))
        try:
            dlc = self.DLC_DATA_BYTE_CNT.index(AMaxDLC)
        except:
            dlc = AMaxDLC
        r = dll.tsdiag_can_create(byref(pDiagModuleIndex), AChnIndex, ASupportFDCAN, dlc, ARequestID,
                                  ARequestIDIsStd,
                                  AResponseID, AResponseIDIsStd, AFunctionID, AFunctionIDIsStd)

        dll.tsdiag_can_attach_to_tscan_tool(pDiagModuleIndex, self.HwHandle)
        return r

    def tsdiag_can_delete(self, pDiagModuleIndex: c_int32):
        r = dll.tsdiag_can_delete(pDiagModuleIndex)
        return r

    def tstp_can_request_and_get_response(self, pDiagModuleIndex: c_int32, AReqDataArray, max_len=4095):
        if not isinstance(AReqDataArray, bytes):
            AReqDataArray = bytes(AReqDataArray)
        AResdata = create_string_buffer(max_len)
        AResponseDataSize = c_uint32(len(AResdata))

        r = dll.tstp_can_request_and_get_response(pDiagModuleIndex, c_char_p(AReqDataArray), len(AReqDataArray),
                                                  AResdata, byref(AResponseDataSize), self.timeout)
        return r, bytes(AResdata[:AResponseDataSize.value])

    def tstp_can_send_functional(self, pDiagModuleIndex: c_int32, AReqDataArray: bytearray,
                                 ):
        r = dll.tstp_can_send_functional(pDiagModuleIndex, c_char_p(AReqDataArray), len(AReqDataArray),
                                         self.timeout)
        return r

    def tscan_get_error_description(self, ACode):

        return self.error_code[ACode]

    def shut_down(self):
        tsapp_disconnect_by_handle(self.HwHandle)
        self.msg_list.queue.clear()
        
