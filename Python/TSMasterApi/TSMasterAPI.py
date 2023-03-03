#!/usr/bin/env python
# @Time   :2023/2/17 10:10
# @Author :SEVEN
# @File   :TSMaterApi.py
# @Comment:use func with TSMaster.dll
# ------------------------------------------------
from ctypes import *
from enum import Enum
import copy
import os
from sys import getsizeof
import time
import winreg
from cantools.database.can import database,message,signal


TSMaster_location = r"Software\TOSUN\TSMaster"

key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, TSMaster_location)

i = 0
dll_path = ''
while True:
    try:
        # 获取注册表对应位置的键和值
        if  winreg.EnumValue(key, i)[0] == 'libTSMaster_x86':
            dll_path = winreg.EnumValue(key, i)[1]
            winreg.CloseKey(key)
            break
        i += 1
    except OSError as error:
        # 一定要关闭这个键
        winreg.CloseKey(key)
        break

if dll_path != '':
    try:
        dll_path = os.path.split(dll_path)[0] + '/TSMaster.dll'
        dll = WinDLL(dll_path)
    except Exception as r:
        print(r"Could not load the TOSUN DLL from '%s'. Error: %s" % (dll_path, r))
else:
    print(r"Could not load the TOSUN DLL Error: Registry not found")


# Enum
class CHANNEL_INDEX(Enum):
    (
        CHN1, CHN2, CHN3, CHN4, CHN5, CHN6, CHN7, CHN8, CHN9, CHN10, CHN11, CHN12, CHN13, CHN14, CHN15, CHN16, CHN17,
        CHN18, CHN19, CHN20, CHN21, CHN22, CHN23, CHN24, CHN25, CHN26, CHN27, CHN28, CHN29, CHN30, CHN31, CHN32) = (
        c_int(0), c_int(1), c_int(2), c_int(3), c_int(4), c_int(5), c_int(6), c_int(7), c_int(8), c_int(9), c_int(10),
        c_int(11), c_int(12), c_int(13), c_int(14), c_int(15), c_int(16), c_int(17), c_int(18), c_int(19), c_int(20),
        c_int(21), c_int(22), c_int(23), c_int(24), c_int(25), c_int(26), c_int(27), c_int(28), c_int(29),
        c_int(30),
        c_int(31)
    )


class TLIB_TS_Device_Sub_Type(Enum):
    TS_UNKNOWN_DEVICE = c_int(0)
    TSCAN_PRO = c_int(1)
    TSCAN_Lite1 = c_int(2)
    TC1001 = c_int(3)
    TL1001 = c_int(4)
    TC1011 = c_int(5)
    TSInterface = c_int(6)
    TC1002 = c_int(7)
    TC1014 = c_int(8)
    TSCANFD2517 = c_int(9)
    TC1026 = c_int(10)
    TC1016 = c_int(11)
    TC1012 = c_int(12)
    TC1013 = c_int(13)


class TLIBBusToolDeviceType(Enum):
    BUS_UNKNOWN_TYPE = c_int(0)
    TS_TCP_DEVICE = c_int(1)
    XL_USB_DEVICE = c_int(2)
    TS_USB_DEVICE = c_int(3)
    PEAK_USB_DEVICE = c_int(4)
    KVASER_USB_DEVICE = c_int(5)
    RESERVED_DEVICE = c_int(6)
    ICS_USB_DEVICE = c_int(7)
    TS_TC1005_DEVICE = c_int(8)


class TLIBApplicationChannelType(Enum):
    APP_CAN = c_int(0)
    APP_LIN = c_int(1)


class READ_TX_RX_DEF():
    ONLY_RX_MESSAGES = False
    TX_RX_MESSAGES = True


class LIN_PROTOCOL(Enum):
    LIN_PROTOCOL_13 = c_int(0)
    LIN_PROTOCOL_20 = c_int(1)
    LIN_PROTOCOL_21 = c_int(2)
    LIN_PROTOCOL_J2602 = c_int(3)


class T_LIN_NODE_FUNCTION(Enum):
    T_MASTER_NODE = c_int(0)
    T_SLAVE_NODE = c_int(1)
    T_MONITOR_NODE = c_int(2)


class TLIBCANFDControllerType(Enum):
    lfdtCAN = c_int(0)
    lfdtISOCAN = c_int(1)
    lfdtNonISOCAN = c_int(2)


class TLIBCANFDControllerMode(Enum):
    lfdmNormal = c_int(0)
    lfdmACKOff = c_int(1)
    lfdmRestricted = c_int(2)


class TSupportedObjType(Enum):
    sotCAN = c_int(0)
    sotLIN = c_int(1)
    sotCANFD = c_int(2)
    sotRealtimeComment = c_int(3)
    sotUnknown = c_int(0xFFFFFFF)




# Struct
class TLIBTSMapping(Structure):
    _pack_ = 1
    _fields_ = [("FAppName", c_char * 32),
                ("FAppChannelIndex", c_int32),
                ("FAppChannelType", c_int),
                ("FHWDeviceType", c_int),
                ("FHWIndex", c_int32),
                ("FHWChannelIndex", c_int32),
                ("FHWDeviceSubType", c_int32),
                ("FHWDeviceName", c_char * 32),
                ("FMappingDisabled", c_bool),
                ]
DLC_DATA_BYTE_CNT = (
    0, 1, 2, 3, 4, 5, 6, 7,
    8, 12, 16, 20, 24, 32, 48, 64
)

class TLIBCAN(Structure):
    _pack_ = 1
    _fields_ = [("FIdxChn", c_uint8),
                ("FProperties", c_uint8),# 0:rx 1:tx
                ("FDLC", c_uint8),
                ("FReserved", c_uint8),
                ("FIdentifier", c_int32),
                ("FTimeUs", c_int64),
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
                ("FProperties", c_uint8),  # 定义canfd数据类型  1:FD标准帧 5:FD扩展帧
                ("FDLC", c_uint8),
                ("FFDProperties", c_uint8),  # 0:普通can数据帧 1：canfd数据帧
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
    _fields_ = [("FIdxChn", c_uint8),
                ("FErrStatus", c_uint8),
                ("FProperties", c_uint8),
                ("FDLC", c_uint8),
                ("FIdentifier", c_int8),
                ("FChecksum", c_uint8),
                ("FStatus", c_uint8),
                ("FTimeUs", c_int64),
                ("FData", c_uint8 * 8),
                ]
    def __init__(self,FIdxChn = 0,FDLC = 8,FIdentifier = 0x1,FProperties = 1,FData=[]):
        self.FIdxChn = FIdxChn
        self.FDLC = FDLC
        if self.FDLC > 8:
            self.FDLC = 8
        self.FIdentifier = FIdentifier
        self.FProperties = FProperties
        for i in range(len(FData)):
            self.FData[i] = FData[i]

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
        self.FChannelMask = FChannelMask
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

# typedef struct _TFlexRaySignal{
#     u8     FFRSgnType;   // 0 - Unsigned, 1 - Signed, 2 - Single 32, 3 - Double 64
#     u8     FCompuMethod; // 0 - Identical, 1 - Linear, 2 - Scale Linear, 3 - TextTable, 4 - TABNoIntp, 5 - Formula
#     u8     FReserved;
#     bool   FIsIntel;
#     s32    FStartBit;
#     s32    FUpdateBit;
#     s32    FLength;
#     double FFactor;
#     double FOffset;
# } TFlexRaySignal, *PFlexRaySignal;
class TFlexRaySignal(Structure):
    _pack_ =1
    _fields_ = [
                ("FFRSgnType",c_uint8),
                ("FCompuMethod",c_uint8),
                ("FReserved",c_uint8),
                ("FIsIntel",c_bool),
                ("FStartBit",c_int32),
                ("FUpdateBit",c_int32),
                ("FLength",c_int32),
                ("FFactor",c_double),
                ("FOffset",c_double),
                ]

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
                ("config_byte", c_uint8),  # bit0: 1：启用cha上终端电阻 0：不启用
                # bit1: 1：启用chb上终端电阻 0：不启用
                # bit2: 1：启用接收FIFO     0：不启用
                # bit4: 1：cha桥接使能    0：不使能
                # bit5: 1：chb桥接使能    0：不使能
                # bit6: 1:not ignore NULL Frame  0: ignore NULL Frame
                ]

    def __init__(self, is_open_a=True, is_open_b=True, wakeup_chn=0, enable100_a=True, enable100_b=True,
                 is_show_nullframe=True, is_Bridging=False):
        '''
        is_open :是否打开通道
        wakeup_chn：唤醒通道 0：通道A ,1:通道B
        enable100: 使能通道 100欧终端电阻
        is_show_nullframe：是否显示空针
        '''
        self.NETWORK_MANAGEMENT_VECTOR_LENGTH = 8
        self.PAYLOAD_LENGTH_STATIC = 16
        self.LATEST_TX = 124
        self.T_S_S_TRANSMITTER = 9
        self.CAS_RX_LOW_MAX = 87
        self.SPEED = 0
        self.WAKE_UP_SYMBOL_RX_WINDOW = 301
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
        self.MICRO_INITIAL_OFFSET_A = 31
        self.MICRO_INITIAL_OFFSET_B = 31
        self.MACRO_INITIAL_OFFSET_A = 11
        self.MACRO_INITIAL_OFFSET_B = 11
        self.N_I_T = 44
        self.OFFSET_CORRECTION_START = 4981
        self.DELAY_COMPENSATION_A = 1
        self.DELAY_COMPENSATION_B = 1
        self.CLUSTER_DRIFT_DAMPING = 2
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
                # bit7: 帧类型：0 - 静态，1 - 动态
                ("recv", c_uint8),
                ]

class TLIBHWInfo(Structure):
    _pack_ = 1
    _fields_ = [("FDeviceType", c_int32),
                ("FDeviceIndex", c_int32),
                ("FVendorName", c_char * 32),
                ("FDeviceName", c_char * 32),
                ("FSerialString", c_char * 64),
                ]
#回调函数
PCANFD = POINTER(TLIBCANFD)
OnTx_RxFUNC_CANFD = WINFUNCTYPE(None, POINTER(c_int32), PCANFD)

PCAN = POINTER(TLIBCAN)
OnTx_RxFUNC_CAN = WINFUNCTYPE(None, POINTER(c_int32), PCAN)

PLIN = POINTER(TLIBLIN)
OnTx_RxFUNC_LIN = WINFUNCTYPE(None, POINTER(c_int32), PLIN)

PFlexray = POINTER(TLIBFlexray)
OnTx_RxFUNC_Flexray = WINFUNCTYPE(None, POINTER(c_int32), PFlexray)

# 释放
def finalize_lib_tsmaster():
    dll.finalize_lib_tsmaster()


#  TSMasterAPI必须先调用该初始化函数，才可进行后续操作
def initialize_lib_tsmaster(AppName: bytes):
    return dll.initialize_lib_tsmaster(AppName)

def initialize_lib_tsmaster_with_project(AppName:bytes,projectfile:bytes):
    return dll.initialize_lib_tsmaster_with_project(AppName,projectfile)


def tsapp_get_current_application():
    AppName = POINTER(POINTER(c_char))()
    ret = dll.tsapp_get_current_application(byref(AppName))
    if ret ==0:
        return string_at(AppName)
    return tsapp_get_error_description(ret)

def tsapp_set_current_application(AppName:bytes):
    
    return dll.tsapp_set_current_application(AppName)

# 设置can通道数
def tsapp_set_can_channel_count(count: c_int32):
    r = dll.tsapp_set_can_channel_count(count)
    return r


# 获取can通道数
def tsapp_get_can_channel_count(count: c_int32):
    r = dll.tsapp_get_can_channel_count(count)
    return r


# 设置lin通道数
def tsapp_set_lin_channel_count(count: c_int32):
    r = dll.tsapp_set_lin_channel_count(count)
    return r


# 获取lin通道数
def tsapp_get_lin_channel_count(count: c_int32):
    r = dll.tsapp_get_lin_channel_count(count)
    return r


# 按需创建通道映射
def tsapp_set_mapping(mapping: TLIBTSMapping):
    r = dll.tsapp_set_mapping(byref(mapping))
    return r


def tsapp_set_mapping_verbose(AppName: str, TLIBApplicationChannelType: c_uint8, CHANNEL_INDEX: CHANNEL_INDEX,
                              HW_name: str,
                              BusToolDeviceType: c_int32, HW_Type: c_int32, AHardwareChannel: CHANNEL_INDEX,
                              AEnableMapping: c_bool):
    r = dll.tsapp_set_mapping_verbose(AppName, TLIBApplicationChannelType, CHANNEL_INDEX, HW_name, BusToolDeviceType,
                                      HW_Type, 0, AHardwareChannel, AEnableMapping)
    return r


# 删除硬件通道映射
def tsapp_del_mapping_verbose(AppName: bytes, TLIBApplicationChannelType: c_uint8, APP_Channel: CHANNEL_INDEX):
    r = dll.tsapp_del_mapping_verbose(AppName, TLIBApplicationChannelType, APP_Channel)
    return r


# 设置can通道参数 bps
def tsapp_configure_baudrate_can(APP_Channel: CHANNEL_INDEX, ABaudrateKbps: c_float, AListenOnly: c_bool,
                                 AInstallTermResistor120Ohm: c_bool):
    r = dll.tsapp_configure_baudrate_can(APP_Channel, c_float(ABaudrateKbps), AListenOnly, AInstallTermResistor120Ohm)
    return r


# 设置canfd通道波特率
def tsapp_configure_baudrate_canfd(AIdxChn: CHANNEL_INDEX, ABaudrateArbKbps: c_float, ABaudrateDataKbps: c_float,
                                   AControllerType: c_int16, AControllerMode: c_int16,
                                   AInstallTermResistor120Ohm: c_bool):
    r = dll.tsapp_configure_baudrate_canfd(AIdxChn, c_float(ABaudrateArbKbps), c_float(ABaudrateDataKbps),
                                           AControllerType, AControllerMode, AInstallTermResistor120Ohm)
    return r


# can brs 采样率设置  AOnlyListen=0表示只听模式  A120大于0表示激活终端电阻，=0表示不激活
def tsapp_configure_can_regs(AIdxChn: CHANNEL_INDEX, ABaudrateKbps: float, ASEG1: int, ASEG2: int, APrescaler: int,
                             ASJ2: int, AOnlyListen: int, A120: int):
    r = dll.tsapp_configure_can_regs(AIdxChn, c_float(ABaudrateKbps), c_int32(ASEG1), c_int32(ASEG2),
                                     c_int32(APrescaler), c_int32(ASJ2), c_uint32(AOnlyListen), c_int32(A120))
    return r


# canfd brs 采样率设置
def tsapp_configure_canfd_regs(AIdxChn: CHANNEL_INDEX, AArbBaudrateKbps: float, AArbSEG1: int, AArbSEG2: int,
                               AArbPrescaler: int,
                               AArbSJ2: int, ADataBaudrateKbps: float, ADataSEG1: int, ADataSEG2: int,
                               ADataPrescaler: int,
                               ADataSJ2: int, AControllerType: TLIBCANFDControllerType,
                               AControllerMode: TLIBCANFDControllerMode,
                               AInstallTermResistor120Ohm: int):
    r = dll.tsapp_configure_canfd_regs(AIdxChn, c_float(AArbBaudrateKbps), c_int32(AArbSEG1), c_int32(AArbSEG2),
                                       c_int32(AArbPrescaler), c_int32(AArbSJ2),
                                       c_float(ADataBaudrateKbps), c_int32(ADataSEG1),
                                       c_int32(ADataSEG2), c_int32(ADataPrescaler), c_int32(ADataSJ2), AControllerType,
                                       AControllerMode,
                                       c_int32(AInstallTermResistor120Ohm))
    return r


# 设置lin通道波特率
def tsapp_configure_baudrate_lin(AIdxChn: CHANNEL_INDEX, ABaudrateKbps: int, LIN_PROTOCOL: LIN_PROTOCOL):
    r = dll.tsapp_configure_baudrate_lin(AIdxChn, c_float(ABaudrateKbps), LIN_PROTOCOL)
    return r


# 设置LIN模式
def tslin_set_node_funtiontype(AIdxChn: CHANNEL_INDEX, TLINNodeType: T_LIN_NODE_FUNCTION):
    r = dll.tslin_set_node_funtiontype(AIdxChn, TLINNodeType)
    return r


# 程序启动
def tsapp_connect():
    r = dll.tsapp_connect()
    return r


# 程序关闭
def tsapp_disconnect():
    r = dll.tsapp_disconnect()
    return r


def tsapp_add_application(AppName: bytes):
    r = tsapp_add_application(AppName)
    return r


def tsapp_del_application(AppName: bytes):
    r = tsapp_del_application(AppName)
    return r


# 以APeriodMS为周期循环发送can报文
def tsapp_add_cyclic_msg_can(Msg: TLIBCAN, APeriodMS: c_float):
    r = dll.tsapp_add_cyclic_msg_can(byref(Msg), c_float(APeriodMS))
    return r


# 删除循环发送can报文
def tsapp_del_cyclic_msg_can(Msg: TLIBCAN):
    r = dll.tsapp_delete_cyclic_msg_can(byref(Msg))
    return r


# 以APeriodMS为周期循环发送canfd报文
def tsapp_add_cyclic_msg_canfd(Msg: TLIBCANFD, APeriodMS: c_float):
    r = dll.tsapp_add_cyclic_msg_canfd(byref(Msg), c_float(APeriodMS))
    return r


# 删除循环发送canfd报文
def tsapp_del_cyclic_msg_canfd(Msg: TLIBCANFD):
    r = dll.tsapp_delete_cyclic_msg_canfd(byref(Msg))
    return r


# 删除所有循环发送报文
def tsapp_delete_cyclic_msgs():
    r = dll.tsapp_delete_cyclic_msgs()
    return r


# 是否使能总线数据统计
def tsapp_enable_bus_statistics(AEnable: c_bool):
    r = dll.tsapp_enable_bus_statistics(AEnable)
    return r


def tsapp_enumerate_hw_devices(ACount: c_int32):
    r = dll.tsapp_enumerate_hw_devices(byref(ACount))
    return r


def tsapp_get_hw_info_by_index(AIndex: int, PLIBHWInfo: TLIBHWInfo):
    r = dll.tsapp_get_hw_info_by_index(c_int32(AIndex), byref(PLIBHWInfo))
    return r


# 错误信息描述
def tsapp_get_error_description(ACode: c_int32):
    errorcode = POINTER(POINTER(c_char))()
    if ACode == 0:
        return "确定"
    else:
        r = dll.tsapp_get_error_description(c_int32(ACode), byref(errorcode))
        if r == 0:
            ADesc = string_at(errorcode).decode("utf-8")
            return ADesc
        else:
            return r


# 获取can每秒帧数，需要先使能总线统计
def tsapp_get_fps_can(AIdxChn: CHANNEL_INDEX, AIdentifier: c_int32, AFPS: c_int32):
    r = dll.tsapp_get_fps_can(AIdxChn, AIdentifier, byref(AFPS))
    return r


# 获取canfd每秒帧数，需要先使能总线统计
def tsapp_get_fps_canfd(AIdxChn: CHANNEL_INDEX, AIdentifier: c_int32, AFPS: c_int32):
    r = dll.tsapp_get_fps_canfd(AIdxChn, AIdentifier, byref(AFPS))
    return r


# 获取canfd每秒帧数，需要先使能总线统计
def tsapp_get_fps_lin(AIdxChn: CHANNEL_INDEX, AIdentifier: c_int32, AFPS: c_int32):
    r = dll.tsapp_get_fps_lin(AIdxChn, AIdentifier, byref(AFPS))
    return r


# 获取硬件映射信息
def tsapp_get_mapping(AMapping: TLIBTSMapping):
    r = dll.tsapp_get_mapping(byref(AMapping))
    return r


# 获取详细硬件映射信息
def tsapp_get_mapping_verbose(APPName: bytes, ApplicationChannelType: c_int32, AMapping: TLIBTSMapping):
    r = dll.tsapp_get_mapping_verbose(APPName, ApplicationChannelType, byref(AMapping))
    return r


# 获取时间戳
def tsapp_get_timestamp(ATimestamp: c_int32):
    r = dll.tsapp_get_timestamp(byref(ATimestamp))
    return r


# 获取极速模式是否开启
def tsapp_get_turbo_mode(AEnable: c_bool):
    r = dll.tsapp_get_turbo_mode(byref(AEnable))
    return r


# 是否开启极速模式
def tsapp_set_turbo_mode(AEnable: c_bool):
    r = dll.tsapp_set_turbo_mode(AEnable)
    return r


# 开启接受FIFO模式
def tsfifo_enable_receive_fifo():
    dll.tsfifo_enable_receive_fifo()


# 关闭接受FIFO模式
def tsfifo_disable_receive_fifo():
    dll.tsfifo_disable_receive_fifo()


# 关闭错误帧接受模式
def tsfifo_disable_receive_error_frames():
    dll.tsfifo_disable_receive_error_frames()


# 读取通道can缓冲帧数量
def tsfifo_read_can_buffer_frame_count(AIdxChn: CHANNEL_INDEX, ACount: c_int32):
    r = dll.tsfifo_read_can_buffer_frame_count(AIdxChn, byref(ACount))
    return r


# 读取通道can Tx数量
def tsfifo_read_can_tx_buffer_frame_count(AIdxChn: CHANNEL_INDEX, ACount: c_int32):
    r = dll.tsfifo_read_can_tx_buffer_frame_count(AIdxChn, byref(ACount))
    return r


# 读取通道can Rx数量
def tsfifo_read_can_rx_buffer_frame_count(AIdxChn: CHANNEL_INDEX, ACount: c_int32):
    r = dll.tsfifo_read_can_rx_buffer_frame_count(AIdxChn, byref(ACount))
    return r


# 读取通道canfd Tx数量
def tsfifo_read_canfd_tx_buffer_frame_count(AIdxChn: CHANNEL_INDEX, ACount: c_int32):
    r = dll.tsfifo_read_canfd_tx_buffer_frame_count(AIdxChn, byref(ACount))
    return r


# 读取通道canfd Rx数量
def tsfifo_read_canfd_rx_buffer_frame_count(AIdxChn: CHANNEL_INDEX, ACount: c_int32):
    r = dll.tsfifo_read_canfd_rx_buffer_frame_count(AIdxChn, byref(ACount))
    return r


# 读取通道fastlin缓冲帧数量
def tsfifo_read_fastlin_buffer_frame_count(AIdxChn: CHANNEL_INDEX, ACount: c_int32):
    r = dll.tsfifo_read_fastlin_buffer_frame_count(AIdxChn, byref(ACount))
    return r


# 读取通道fastlin Tx数量
def tsfifo_read_fastlin_tx_buffer_frame_count(AIdxChn: CHANNEL_INDEX, ACount: c_int32):
    r = dll.tsfifo_read_fastlin_tx_buffer_frame_count(AIdxChn, byref(ACount))
    return r


# 读取通道fastlin Rx数量
def tsfifo_read_fastlin_rx_buffer_frame_count(AIdxChn: CHANNEL_INDEX, ACount: c_int32):
    r = dll.tsfifo_read_fastlin_rx_buffer_frame_count(AIdxChn, byref(ACount))
    return r


# 读取通道lin缓冲帧数量
def tsfifo_read_lin_buffer_frame_count(AIdxChn: CHANNEL_INDEX, ACount: c_int32):
    r = dll.tsfifo_read_lin_buffer_frame_count(AIdxChn, byref(ACount))
    return r


# 读取通道lin Tx数量
def tsfifo_read_lin_tx_buffer_frame_count(AIdxChn: CHANNEL_INDEX, ACount: c_int32):
    r = dll.tsfifo_read_lin_tx_buffer_frame_count(AIdxChn, byref(ACount))
    return r


# 读取通道lin Rx数量
def tsfifo_read_lin_rx_buffer_frame_count(AIdxChn: CHANNEL_INDEX, ACount: c_int32):
    r = dll.tsfifo_read_lin_rx_buffer_frame_count(AIdxChn, byref(ACount))
    return r


# 清除 通道can_receive_buffers
def tsfifo_clear_can_receive_buffers(AIdxChn: CHANNEL_INDEX):
    r = dll.tsfifo_clear_can_receive_buffers(AIdxChn)
    return r


# 清除 通道canfd_receive_buffers
def tsfifo_clear_canfd_receive_buffers(AIdxChn: CHANNEL_INDEX):
    r = dll.tsfifo_clear_canfd_receive_buffers(AIdxChn)
    return r


# 清除 通道fastlin_receive_buffers
def tsfifo_clear_fastlin_receive_buffers(AIdxChn: CHANNEL_INDEX):
    r = dll.tsfifo_clear_fastlin_receive_buffers(AIdxChn)
    return r


# 清除 通道lin_receive_buffers
def tsfifo_clear_lin_receive_buffers(AIdxChn: CHANNEL_INDEX):
    r = dll.tsfifo_clear_lin_receive_buffers(AIdxChn)
    return r


# 注册canfd预发送事件
def tsapp_register_pretx_event_canfd(obj: c_int32, OnFUNC):
    r = dll.tsapp_register_pretx_event_canfd(byref(obj), OnFUNC)
    return r


# 注册can预发送事件
def tsapp_register_pretx_event_can(obj: c_int32, OnFUNC):
    r = dll.tsapp_register_pretx_event_can(byref(obj), OnFUNC)
    return r


# 注册lin预发送事件
def tsapp_register_pretx_event_lin(obj: c_int32, OnFUNC):
    r = dll.tsapp_register_pretx_event_lin(byref(obj), OnFUNC)
    return r


# 注册canfd发送—接收事件
def tsapp_register_event_canfd(obj: c_int32, OnFUNC):
    r = dll.tsapp_register_event_canfd(byref(obj), OnFUNC)
    return r


# 注册can发送—接收事件
def tsapp_register_event_can(obj: c_int32, OnFUNC):
    r = dll.tsapp_register_event_can(byref(obj), OnFUNC)
    return r


# 注册lin发送—接收事件
def tsapp_register_event_lin(obj: c_int32, OnFUNC):
    r = dll.tsapp_register_event_lin(byref(obj), OnFUNC)
    return r


# 注销canfd预发送事件
def tsapp_unregister_pretx_event_canfd(obj: c_int32, OnFUNC):
    r = dll.tsapp_unregister_pretx_event_canfd(byref(obj), OnFUNC)
    return r


# 注销can预发送事件
def tsapp_unregister_pretx_event_can(obj: c_int32, OnFUNC):
    r = dll.tsapp_unregister_pretx_event_can(byref(obj), OnFUNC)
    return r


# 注销lin预发送事件
def tsapp_unregister_pretx_event_lin(obj: c_int32, OnFUNC):
    r = dll.tsapp_unregister_pretx_event_lin(byref(obj), OnFUNC)
    return r


# 注销canfd发送—接收事件
def tsapp_unregister_event_canfd(obj: c_int32, OnFUNC):
    r = dll.tsapp_unregister_event_canfd(byref(obj), OnFUNC)
    return r


# 注销can发送—接收事件
def tsapp_unregister_event_can(obj: c_int32, OnFUNC):
    r = dll.tsapp_unregister_event_can(byref(obj), OnFUNC)
    return r


# 注销lin发送—接收事件
def tsapp_unregister_event_lin(obj: c_int32, OnFUNC):
    r = dll.tsapp_unregister_event_lin(byref(obj), OnFUNC)
    return r


# 注销canfd预发送事件
def tsapp_unregister_pretx_events_canfd(obj: c_int32):
    r = dll.tsapp_unregister_pretx_events_canfd(byref(obj))
    return r


# 注销can预发送事件
def tsapp_unregister_pretx_events_can(obj: c_int32):
    r = dll.tsapp_unregister_pretx_events_can(byref(obj))
    return r


# 注销lin预发送事件
def tsapp_unregister_pretx_events_lin(obj: int):
    r = dll.tsapp_unregister_pretx_events_lin(byref(obj))
    return r


# 注销canfd发送—接收事件
def tsapp_unregister_events_canfd(obj: c_int32):
    r = dll.tsapp_unregister_events_canfd(byref(obj))
    return r


# 注销can发送—接收事件
def tsapp_unregister_events_can(obj: int):
    r = dll.tsapp_unregister_events_can(byref(obj))
    return r


# 注销lin发送—接收事件
def tsapp_unregister_events_lin(obj: int):
    r = dll.tsapp_unregister_events_lin(byref(obj),)
    return r


# 注销预发送事件
def tsapp_unregister_pretx_events_all():
    r = dll.tsapp_unregister_pretx_events_all()
    return r


# 注销发送—接收事件
def tsapp_unregister_events_all():
    r = dll.tsapp_unregister_events_all()
    return r


# 打开TsMaster窗口
def tsapp_show_tsmaster_window(AWindowName: str,AWaitClose:bool):
    r = dll.tsapp_show_tsmaster_window(AWindowName, AWaitClose)
    return r


# 开始录制报文
def tsapp_start_logging(filename: str):
    r = dll.tsapp_start_logging(filename)
    return r


# 停止录制报文
def tsapp_stop_logging():
    r = dll.tsapp_stop_logging()
    return r


# 异步发送单帧can报文
def tsapp_transmit_can_async(Msg: TLIBCAN):
    r = dll.tsapp_transmit_can_async(byref(Msg))
    return r


# can fifo接收
#ACANBuffers：TLIBCAN数组
def tsfifo_receive_can_msgs(ACANBuffers: TLIBCAN, ACANBufferSize: c_uint, AChn: CHANNEL_INDEX,
                           ARxTx: READ_TX_RX_DEF):

    return dll.tsfifo_receive_can_msgs(ACANBuffers, byref(ACANBufferSize), AChn, ARxTx)



# 发送头帧接收数据
def tsapp_transmit_header_and_receive_msg(AChn: CHANNEL_INDEX, ID: int, FDlc: c_uint8, receivedMsg: TLIBLIN,
                                          Timeout: c_int):
    r = dll.tsapp_transmit_header_and_receive_msg(AChn, ID, FDlc, byref(receivedMsg), c_int32(Timeout))
    return r


# 异步发送单帧canfd报文
def tsapp_transmit_canfd_async(Msg: TLIBCANFD):
    r = dll.tsapp_transmit_canfd_async(byref(Msg))
    return r


# canfd报文接收
#ACANFDBuffers：TLIBCANFD数组
def tsfifo_receive_canfd_msgs(ACANFDBuffers, ACANFDBufferSize: c_uint32, AChn: CHANNEL_INDEX,
                             ARxTx: READ_TX_RX_DEF):

    return dll.tsfifo_receive_canfd_msgs(ACANFDBuffers, byref(ACANFDBufferSize), AChn, ARxTx)



# 异步发送单帧lin报文
def tsapp_transmit_lin_async(Msg: TLIBLIN):
    r = dll.tsapp_transmit_lin_async(byref(Msg))
    return r


# lin报文接收
#ALINBuffers：TLIBLIN数组
def tsapp_receive_lin_msgs(ALINBuffers, ALINBufferSize: c_int, AChn: CHANNEL_INDEX,
                           ARxTx: READ_TX_RX_DEF):

    r = dll.tsfifo_receive_lin_msgs(ALINBuffers, byref(ALINBufferSize), AChn, ARxTx)

    return r


def tsfifo_receive_fastlin_msgs(ALINBuffers: TLIBLIN, ALINBufferSize: c_int, AChn: CHANNEL_INDEX,
                                ARxTx: READ_TX_RX_DEF):
    temp = copy.copy(c_uint32(ALINBufferSize))
    data = POINTER(TLIBLIN * len(ALINBuffers))((TLIBLIN * len(ALINBuffers))(*ALINBuffers))
    r = dll.tsfifo_receive_fastlin_msgs(data, byref(temp), AChn, ARxTx)
    for i in range(len(data.contents)):
        ALINBuffers[i] = data.contents[i]
    return r, temp


# 同步发送单帧can报文
def tsapp_transmit_can_sync(Msg: TLIBCAN, ATimeoutMS: c_int32):
    r = dll.tsapp_transmit_can_sync(byref(Msg), c_int32(ATimeoutMS))
    return r


# 同步发送单帧canfd报文
def tsapp_transmit_canfd_sync(Msg: TLIBCANFD, ATimeoutMS: c_int32):
    r = dll.tsapp_transmit_canfd_sync(byref(Msg), c_int32(ATimeoutMS))
    return r


# 同步发送单帧lin报文
def tsapp_transmit_lin_sync(Msg: TLIBLIN, ATimeoutMS: c_int32):
    r = dll.tsapp_transmit_lin_sync(byref(Msg), c_int32(ATimeoutMS))
    return r


# 开启rbs
def tscom_can_rbs_start():
    r = dll.tscom_can_rbs_start()
    return r


# 停止rbs
def tscom_can_rbs_stop():
    r = dll.tscom_can_rbs_stop()
    return r


# rbs是否开启
def tscom_can_rbs_is_running(AIsRunning: c_bool):
    r = dll.tscom_can_rbs_is_running(byref(AIsRunning))
    return r


# rbs配置
def tscom_can_rbs_configure(AAutoStart: c_bool, AAutoSendOnModification: c_bool, AActivateNodeSimulation: c_bool,
                            TLIBRBSInitValueOptions: c_int):
    r = dll.tscom_can_rbs_configure(AAutoStart, AAutoSendOnModification, AActivateNodeSimulation,
                                    TLIBRBSInitValueOptions)
    return r


def tscom_can_rbs_activate_network_by_name(AIdxChn:c_int32,AEnable: bool, ANetworkName: str, AIncludingChildren: bool):
    return dll.tscom_can_rbs_activate_network_by_name(AIdxChn,AEnable, ANetworkName, AIncludingChildren)


def tscom_can_rbs_activate_node_by_name(AIdxChn:c_int32,AEnable: bool, ANetworkName: str, NodeName: str, AIncludingChildren: bool):
    return dll.tscom_can_rbs_activate_node_by_name(AIdxChn,AEnable, ANetworkName, NodeName, AIncludingChildren)


def tscom_can_rbs_activate_message_by_name(AIdxChn:c_int32,AEnable: bool, ANetworkName: str, NodeName: str, MessageName: str):
    return dll.tscom_can_rbs_activate_message_by_name(AIdxChn,AEnable, ANetworkName, NodeName, MessageName)


def tscom_can_rbs_activate_all_networks(AEnable: bool, AIncludingChildren: bool):
    return dll.tscom_can_rbs_activate_all_networks(AEnable, AIncludingChildren)


def tscom_can_rbs_enable(AEnable: bool):
    return dll.tscom_can_rbs_enable(AEnable)


def tscom_can_rbs_get_signal_value_by_address(ASymboladdress: str, Avalue: c_double):
    return dll.tscom_can_rbs_get_signal_value_by_address(ASymboladdress, byref(Avalue))


def tscom_can_rbs_get_signal_value_by_element(AIdchn: c_int32, ANetwork: str, ANodeName: str, AMessageName: str,
                                              ASignalName: str, Avalue: c_double):
    return dll.tscom_can_rbs_get_signal_value_by_element(AIdchn, ANetwork, ANodeName, AMessageName, ASignalName, byref(Avalue))


def tscom_can_rbs_set_message_cycle_by_name(AIntervalMs:c_float,ANetwork: str, ANodeName: str, AMessageName: str):
    return dll.tscom_can_rbs_set_message_cycle_by_name(AIntervalMs,ANetwork,ANodeName,AMessageName)


def tscom_can_rbs_set_signal_value_by_address(ASymboladdress: str, Avalue: c_double):
    return dll.tscom_can_rbs_set_signal_value_by_address(ASymboladdress, Avalue)


def tscom_can_rbs_set_signal_value_by_element(AIdchn: c_int32, ANetwork: str, ANodeName: str, AMessageName: str,
                                              ASignalName: str, Avalue: c_double):
    return dll.tscom_can_rbs_set_signal_value_by_element(AIdchn, ANetwork, ANodeName, AMessageName, ASignalName, Avalue)


# 获取can信号值
def tsdb_get_signal_value_can(ACAN: TLIBCAN, AMsgName: str, ASgnName: str, AValue: c_double):
    r = dll.tsdb_get_signal_value_can(byref(ACAN), AMsgName, ASgnName, byref(AValue))
    return r


# 获取canfd信号值
def tsdb_get_signal_value_canfd(ACANFD: TLIBCANFD, AMsgName: str, ASgnName: str, AValue: c_double):
    r = dll.tsdb_get_signal_value_canfd(byref(ACANFD), AMsgName, ASgnName, byref(AValue))
    return r


# 设置can信号值
def tsdb_set_signal_value_can(ACAN: TLIBCAN, AMsgName: str, ASgnName: str, AValue: c_double):
    r = dll.tsdb_set_signal_value_can(byref(ACAN), AMsgName.encode, ASgnName, AValue)
    return r


# 设置canfd信号值
def tsdb_set_signal_value_canfd(ACANFD: TLIBCANFD, AMsgName: str, ASgnName: str, AValue: c_double):
    r = dll.tsdb_set_signal_value_canfd(byref(ACANFD), AMsgName, ASgnName, AValue)
    return r


# 加载dbc并绑定通道 注意idDBC 必须是c_uint32类型
def tsdb_load_can_db(DBC_ADDRESS, ASupportedChannelsBased, idDBC: c_uint32):
    r = dll.tsdb_load_can_db(DBC_ADDRESS.encode("utf8"), ASupportedChannelsBased.encode("utf8"), byref(idDBC))
    return r


# 解绑所有dbc
def tsdb_unload_can_dbs():
    r = dll.tsdb_unload_can_dbs()
    return r


# 获取dbc数量
def tsdb_get_can_db_count(ACount: c_uint32):
    r = dll.tsdb_get_can_db_count(byref(ACount))
    return r


# 获取dbc AId
def tsdb_get_can_db_id(AIndex: c_int32, AId: c_uint32):
    r = dll.tsdb_get_can_db_id(AIndex, byref(AId))
    return r


# 获取dbc信息
def tsdb_get_can_db_info(ADatabaseId: c_int32, AType: c_int32, AIndex: c_int32, ASubIndex: c_int32):
    AValue = POINTER(POINTER(c_char))()
    r = dll.tsdb_get_can_db_info(ADatabaseId, c_int32(AType), c_int32(AIndex), c_uint32(ASubIndex), byref(AValue))
    AValue = string_at(AValue).decode("utf8")
    return r, AValue


# 添加在线回放配置
def tslog_add_online_replay_config(AFileName: str, AIndex: c_int32):
    r = dll.tslog_add_online_replay_config(AFileName.encode("utf8"), byref(AIndex))
    return r


# 设置在线回放配置
def tslog_set_online_replay_config(AIndex: c_int32, AName: str, AFileName: str, AAutoStart: c_bool,
                                   AIsRepetitiveMode: c_bool, AStartTimingMode: c_int32, AStartDelayTimeMs: c_int32,
                                   ASendTx: c_bool, ASendRx: c_bool, AMappings: c_char * 32):
    r = dll.tslog_set_online_replay_config(AIndex, AName, AFileName, AAutoStart, AIsRepetitiveMode, AStartTimingMode,
                                           AStartDelayTimeMs, ASendTx, ASendRx, AMappings)
    return r


# 获取在线回放文件数量
def tslog_get_online_replay_count(ACount: c_int32):
    r = dll.tslog_get_online_replay_count(byref(ACount))
    return r


# 获取在线回放配置
def tslog_get_online_replay_config(AIndex: c_int32, AName: str, AFileName: str, AAutoStart: c_bool,
                                   AIsRepetitiveMode: c_bool, AStartTimingMode: c_int32, AStartDelayTimeMs: c_int32,
                                   ASendTx: c_bool, ASendRx: c_bool, AMappings: c_char * 32):
    r = dll.tslog_get_online_replay_config(AIndex, byref(AName), byref(AFileName), byref(AAutoStart),
                                           byref(AIsRepetitiveMode), byref(AStartTimingMode), byref(AStartDelayTimeMs),
                                           byref(ASendTx), byref(ASendRx), byref(AMappings))
    return r


# 删除在线回放配置
def tslog_del_online_replay_config(AIndex: c_int32):
    r = dll.tslog_del_online_replay_config(AIndex)
    return r


# 删除所有在线回放配置
def tslog_del_online_replay_configs():
    r = dll.tslog_del_online_replay_configs()
    return r


# 开始在线回放
def tslog_start_online_replay(AInde: c_int32):
    r = dll.tslog_del_online_replay_configs(AInde)
    return r


# 所有文件开始回放
def tslog_start_online_replays():
    r = dll.tslog_start_online_replays()
    return r


# 暂停在线回放
def tslog_pause_online_replay(AInde: c_int32):
    r = dll.tslog_pause_online_replay(AInde)
    return r


# 所有文件暂停回放
def tslog_pause_online_replays():
    r = dll.tslog_pause_online_replays()
    return r


# 停止在线回放
def tslog_stop_online_replay(AInde: c_int32):
    r = dll.tslog_stop_online_replay(AInde)
    return r


# 所有文件停止回放
def tslog_stop_online_replays():
    r = dll.tslog_stop_online_replays()
    return r


# 获取在线回放状态
def tslog_get_online_replay_status(AIndex: c_int32, AStatus: c_int32, AProgressPercent100: c_float):
    r = dll.tslog_get_online_replay_status(AIndex, byref(AStatus), byref(AProgressPercent100))
    return r


# 开始读取blf
def tslog_blf_read_start(Pathfile: str, AHeadle: c_int32, ACount: c_int32):
    r = dll.tslog_blf_read_start(Pathfile.encode("utf8"), byref(AHeadle), byref(ACount))
    return r


def tslog_blf_read_object(AHandle: c_int32, AProgressedCnt: c_int32, AType: TSupportedObjType, ACAN: TLIBCAN,
                          ALIN: TLIBLIN, ACANFD: TLIBCANFD):
    r = dll.tslog_blf_read_object(AHandle, byref(AProgressedCnt), byref(AType), byref(ACAN), byref(ALIN), byref(ACANFD))
    return r


def tslog_blf_read_end(AHeadle: c_int64):
    r = dll.tslog_blf_read_end(AHeadle)
    return r


def tslog_blf_write_start(Pathfile: str, AHeadle: c_int32):
    r = dll.tslog_blf_write_start(Pathfile, byref(AHeadle))
    return r


def tslog_blf_write_can(AHeadle: c_int32, ACAN: TLIBCAN):
    r = dll.tslog_blf_write_can(AHeadle, byref(ACAN))
    return r


def tslog_blf_write_canfd(AHeadle: c_int32, ACANFD: TLIBCANFD):
    r = dll.tslog_blf_write_canfd(AHeadle, byref(ACANFD))
    return r


def tslog_blf_write_lin(AHeadle: c_int32, ALIN: TLIBLIN):
    r = dll.tslog_blf_write_lin(AHeadle, byref(ALIN))
    return r


def tslog_blf_write_end(AHeadle: c_int64):
    r = dll.tslog_blf_write_end(AHeadle)
    return r


# 诊断相关API

# 创建诊断服务
def tsdiag_can_create(udsHandle: c_int8, ChnIndex: CHANNEL_INDEX, ASupportFD: c_byte, AMaxdlc: c_byte, reqID: c_int32,
                      ARequestIDIsStd: c_bool,
                      resID: c_int32, resIsStd: c_bool, AFctID: c_int32, fctIsStd: c_bool):
    r = dll.tsdiag_can_create(byref(udsHandle), ChnIndex, c_byte(ASupportFD), c_byte(AMaxdlc), reqID,
                              c_bool(ARequestIDIsStd), resID, c_bool(resIsStd), AFctID, c_bool(fctIsStd))
    return r

def tsdiag_set_p2_extended(pDiagModuleIndex: c_int8,TimeOut):
    r = dll.tsdiag_set_p2_extended(pDiagModuleIndex,c_int32(TimeOut))
    return r

def tsdiag_set_p2_timeout(pDiagModuleIndex: c_int8,TimeOut):
    r = dll.tsdiag_set_p2_timeout(pDiagModuleIndex,c_int32(TimeOut))
    return r

def tsdiag_set_s3_clienttime(pDiagModuleIndex: c_int8,TimeOut):
    r = dll.tsdiag_set_s3_clienttime(pDiagModuleIndex,c_int32(TimeOut))
    return r

def tsdiag_set_s3_servertime(pDiagModuleIndex: c_int8,TimeOut):
    r = dll.tsdiag_set_s3_servertime(pDiagModuleIndex,c_int32(TimeOut))
    return r


def tsdiag_can_delete(pDiagModuleIndex: c_int8):
    r = tsdiag_can_delete(pDiagModuleIndex)
    return r


def tsdiag_can_delete_all():
    r = dll.tsdiag_can_delete_all()
    return r


def tstp_can_send_functional(pDiagModuleIndex: c_int8, AReqDataArray: bytearray, AReqDataSize: c_int32):
    data = POINTER(c_ubyte * len(AReqDataArray))((c_ubyte * len(AReqDataArray))(*AReqDataArray))
    r = dll.tstp_can_send_functional(pDiagModuleIndex, data, AReqDataSize)
    return r


def tstp_can_send_request(pDiagModuleIndex: c_int8, AReqDataArray: bytearray, AReqDataSize: c_int32
                          ):
    data = POINTER(c_ubyte * len(AReqDataArray))((c_ubyte * len(AReqDataArray))(*AReqDataArray))
    r = dll.tstp_can_send_request(pDiagModuleIndex, data, AReqDataSize)
    return r


def tstp_can_request_and_get_response(udsHandle: c_int8, dataIn: bytearray, ReqSize: c_int32, dataOut: bytearray,
                                      resSize: c_int32):
    r = dll.tstp_can_request_and_get_response(udsHandle, dataIn, ReqSize, dataOut, byref(resSize))
    return r


# AReqDataArray = [0x22,0xf1,0x90]
# size = c_int32(100)
# AResponseDataArray = []
# for i in range(100):
#     item = 0
#     AResponseDataArray.append(item)
# tstp_can_request_and_get_response_s(udsHandle,AReqDataArray,3,AResponseDataArray,size,100)
def tstp_can_request_and_get_response_s(pDiagModuleIndex: c_int8, AReqDataArray: bytearray, AReqDataSize: c_int32,
                                        AResponseDataArray: bytearray, AResponseDataSize: c_int32):
    AReqdata = POINTER(c_ubyte * len(AReqDataArray))((c_ubyte * len(AReqDataArray))(*AReqDataArray))
    AResdata = POINTER(c_ubyte * len(AResponseDataArray))((c_ubyte * len(AResponseDataArray))(*AResponseDataArray))
    r = dll.tstp_can_request_and_get_response(pDiagModuleIndex, AReqdata, AReqDataSize, AResdata,
                                              byref(AResponseDataSize))
    if r == 0:
        for i in range(AResponseDataSize.value):
            AResponseDataArray[i] = AResdata.contents[i]
    return r


# 诊断服务

def tsdiag_can_session_control(pDiagModuleIndex: c_int8, ASubSession: c_byte):
    r = dll.tsdiag_can_session_control(pDiagModuleIndex, ASubSession)
    return r


def tsdiag_can_routine_control(pDiagModuleIndex: c_int8, ARoutineControlType: c_byte, ARoutintID: c_uint16,
                               ):
    r = dll.tsdiag_can_routine_control(pDiagModuleIndex, ARoutineControlType, ARoutintID)
    return r


def tsdiag_can_communication_control(pDiagModuleIndex: c_int8, AControlType: c_byte):
    r = dll.tsdiag_can_communication_control(pDiagModuleIndex, AControlType)
    return r


def tsdiag_can_security_access_request_seed(pDiagModuleIndex: c_int8, ALevel: c_int32, ARecSeed: bytearray,
                                            ARecSeedSize: c_int32):
    AReqdata = POINTER(c_ubyte * len(ARecSeed))((c_ubyte * len(ARecSeed))(*ARecSeed))
    r = dll.tsdiag_can_security_access_request_seed(pDiagModuleIndex, ALevel, AReqdata, byref(ARecSeedSize))
    return r


def tsdiag_can_security_access_send_key(pDiagModuleIndex: c_int8, ALevel: c_int32, AKeyValue: bytearray,
                                        AKeySize: c_int32):
    AReqdata = POINTER(c_ubyte * len(AKeyValue))((c_ubyte * len(AKeyValue))(*AKeyValue))
    r = dll.tsdiag_can_security_access_send_key(pDiagModuleIndex, ALevel, AReqdata, AKeySize)
    return r


def tsdiag_can_request_download(pDiagModuleIndex: c_int8, AMemAddr: c_uint32, AMemSize: c_uint32):
    r = dll.tsdiag_can_request_download(pDiagModuleIndex, AMemAddr, AMemSize)
    return r


def tsdiag_can_request_upload(pDiagModuleIndex: c_int8, AMemAddr: c_uint32, AMemSize: c_uint32):
    r = dll.tsdiag_can_request_upload(pDiagModuleIndex, AMemAddr, AMemSize)
    return r


def tsdiag_can_transfer_data(pDiagModuleIndex: c_int8, ASourceDatas: bytearray, ADataSize: c_int32, AReqCase: c_int32):
    AReqdata = POINTER(c_ubyte * len(ASourceDatas))((c_ubyte * len(ASourceDatas))(*ASourceDatas))
    r = dll.tsdiag_can_transfer_data(pDiagModuleIndex, AReqdata, ADataSize, AReqCase)


def tsdiag_can_request_transfer_exit(pDiagModuleIndex: c_int8):
    r = dll.tsdiag_can_request_transfer_exit(pDiagModuleIndex)
    return r


def tsdiag_can_write_data_by_identifier(pDiagModuleIndex: c_int8, ADataIdentifier: c_uint16, AWriteData: bytearray,
                                        AWriteDataSize: c_int32):
    AReqdata = POINTER(c_ubyte * len(AWriteData))((c_ubyte * len(AWriteData))(*AWriteData))
    r = dll.tsdiag_can_write_data_by_identifier(pDiagModuleIndex, ADataIdentifier, AReqdata, AWriteDataSize)
    return r


def tsdiag_can_read_data_by_identifier(pDiagModuleIndex: c_int8, ADataIdentifier: c_uint16, AReturnArray: bytearray,
                                       AReturnArraySize: c_int32):
    AReqdata = POINTER(c_ubyte * len(AReturnArray))((c_ubyte * len(AReturnArray))(*AReturnArray))
    r = dll.tsdiag_can_read_data_by_identifier(pDiagModuleIndex, ADataIdentifier, AReqdata, byref(AReturnArraySize))
    return r




# LIN诊断
def tstp_lin_master_request(AChnIdx: CHANNEL_INDEX, ANAD: c_int8, AData: bytearray, ADataNum: c_int,
                            ATimeoutMs: c_int32):
    AReqdata = POINTER(c_ubyte * len(AData))((c_ubyte * len(AData))(*AData))
    r = dll.tstp_lin_master_request(AChnIdx, ANAD, byref(AReqdata), c_int32(ADataNum), c_int32(ATimeoutMs))
    return r


def tstp_lin_master_request_intervalms(AChnIdx: CHANNEL_INDEX, AData: c_int8):
    r = dll.tstp_lin_master_request_intervalms(AChnIdx, AData)
    return r


def tstp_lin_reset(AChnIdx: CHANNEL_INDEX):
    r = dll.tstp_lin_reset(AChnIdx)
    return r


def tstp_lin_slave_response_intervalms(AChnIdx: CHANNEL_INDEX, AData: c_int8):
    r = dll.tstp_lin_slave_response_intervalms(AChnIdx, AData)
    return r


def tsdiag_lin_read_data_by_identifier(AChnIdx: CHANNEL_INDEX, ANAD: c_int8, AId: c_ushort, AResNAD: c_byte,
                                       AResData: bytearray, AResDataNum: c_int32, ATimeoutMS: c_int32):
    Resdata = POINTER(c_ubyte * len(AResData))((c_ubyte * len(AResData))(*AResData))
    r = dll.tsdiag_lin_read_data_by_identifier(AChnIdx, c_int8(ANAD), c_ushort(AId), byref(AResNAD), Resdata,
                                               byref(AResDataNum), ATimeoutMS)
    return r


def tsdiag_lin_write_data_by_identifier(AChnIdx: CHANNEL_INDEX, ANAD: c_int8, AId: c_ushort, AReqData: bytearray,
                                        AReqDataNum: c_int32,
                                        AResNAD: c_byte, AResData: bytearray, AResDataNum: c_int32,
                                        ATimeoutMS: c_int32):
    Reqdata = POINTER(c_ubyte * len(AReqData))((c_ubyte * len(AReqData))(*AReqData))
    Resdata = POINTER(c_ubyte * len(AResData))((c_ubyte * len(AResData))(*AResData))

    r = dll.tsdiag_lin_write_data_by_identifier(AChnIdx, c_int8(ANAD), c_ushort(AId), Reqdata, c_int32(AReqDataNum),
                                                byref(AResNAD), Resdata, byref(AResDataNum), ATimeoutMS)
    return r


def tsdiag_lin_session_control(AChnIdx: CHANNEL_INDEX, ANAD: c_int8, ANewSession: c_byte, ATimeoutMS: c_int32):
    r = dll.tsdiag_lin_session_control(AChnIdx, c_int8(ANAD), c_byte(ANewSession), c_int32(ATimeoutMS))
    return r


def tsdiag_lin_fault_memory_read(AChnIdx: CHANNEL_INDEX, ANAD: c_int8, ANewSession: c_byte, ATimeoutMS: c_int32):
    r = dll.tsdiag_lin_fault_memory_read(AChnIdx, c_int8(ANAD), c_byte(ANewSession), c_int32(ATimeoutMS))
    return r


def tsdiag_lin_fault_memory_clear(AChnIdx: CHANNEL_INDEX, ANAD: c_int8, ANewSession: c_byte, ATimeoutMS: c_int32):
    r = dll.tsdiag_lin_fault_memory_clear(AChnIdx, c_int8(ANAD), c_byte(ANewSession), c_int32(ATimeoutMS))
    return r

#TLIBFlxeRay API
def tsapp_transmit_flexray_sync(AFlexRay:TLIBFlexray,ATimeout:c_int32):
    return dll.tsapp_transmit_flexray_sync(byref(AFlexRay),ATimeout)

def tsapp_transmit_flexray_async(AFlexRay:TLIBFlexray):
    return dll.tsapp_transmit_flexray_async(byref(AFlexRay))

def tsfifo_clear_flexray_receive_buffers(chn: c_int):
    return dll.tsfifo_clear_flexray_receive_buffers(chn)

def tsfifo_read_flexray_buffer_frame_count(AIdxChn: c_int, ACount: c_int):
    return dll.tsfifo_read_flexray_buffer_frame_count(AIdxChn, byref(ACount))

def tsfifo_read_flexray_tx_buffer_frame_count( AIdxChn: c_int, ACount: c_int):
    return dll.tsfifo_read_flexray_tx_buffer_frame_count(AIdxChn, byref(ACount))

def tsfifo_read_flexray_rx_buffer_frame_count(AIdxChn: c_int, ACount: c_int):
    return dll.tsfifo_read_flexray_rx_buffer_frame_count( AIdxChn, byref(ACount))

def tsfifo_receive_flexray_msgs(ADataBuffers: TLIBFlexray, ADataBufferSize: c_int, chn: c_int,
                                ARxTx: c_int8):
    return dll.tsfifo_receive_flexray_msgs(ADataBuffers, byref(ADataBufferSize), chn, ARxTx)


def tsflexray_start_net(AChnIdx: CHANNEL_INDEX,ATimeout:c_int32):
    return dll.tsflexray_start_net(AChnIdx,ATimeout)

def tsflexray_stop_net(AChnIdx: CHANNEL_INDEX,ATimeout:c_int32):
    return dll.tsflexray_stop_net(AChnIdx,ATimeout)

def tsflexray_wakeup_pattern(AChnIdx: CHANNEL_INDEX,ATimeout:c_int32):
    return dll.tsflexray_wakeup_pattern(AChnIdx,ATimeout)

#tsdb_Flexray api
def tsdb_load_flexray_db(AFliepath:str,ASupportedChannels:str,AId:c_int32):
    if not isinstance(AFliepath,bytes):
        AFliepath = bytes(AFliepath)
    if not isinstance(ASupportedChannels,bytes):
        ASupportedChannels = bytes(ASupportedChannels)
    ret = dll.tsdb_load_flexray_db(AFliepath,ASupportedChannels,byref(AId))
    # if ret == 0:
    #     try:
    #         ret = flexray_db_parse((AId.value-1)) 
    #     except:
    #         return ret  
    return ret


def tsdb_unload_flexray_db(AId:c_int32):
    return dll.tsdb_unload_flexray_db(AId)

def tsdb_unload_flexray_dbs():
    return dll.tsdb_unload_flexray_dbs()

def tsdb_get_flexray_db_count(Acount:c_int32):
    return dll.tsdb_get_flexray_db_count(byref(Acount))

def tsdb_get_flexray_db_properties_by_address_verbose(AAddr:str):
    if not isinstance(AAddr,bytes):
        AAddr = bytes(AAddr)
    ADBIndex =c_int32(0)
    AFrameCount = c_int32(0)
    ASignalCount = c_int32(0)
    AECUCount = c_int32(0)
    ASupportedChannelMask = c_int32(0)
    AName = POINTER(POINTER(c_char))()
    AComment= POINTER(POINTER(c_char))()

    ret = dll.tsdb_get_flexray_db_properties_by_address_verbose(AAddr,byref(ADBIndex),byref(ASignalCount),byref(AFrameCount),byref(AECUCount),byref(ASupportedChannelMask),byref(AName),byref(AComment))
    if ret ==0:
        try:
            AComment = string_at(AComment).decode('utf8')
        except:
            AComment = ''
        return ADBIndex,AFrameCount,ASignalCount,AECUCount,ASupportedChannelMask,string_at(AName).decode('utf8'),AComment
    print(tsapp_get_error_description(ret))
    return AECUCount,AFrameCount,ASignalCount,ASupportedChannelMask,string_at(AName),AComment                                                                          
def tsdb_get_flexray_db_properties_by_index_verbose(ADBIndex:c_int32):
    AFrameCount = c_int32(0)
    ASignalCount = c_int32(0)
    AECUCount = c_int32(0)
    ASupportedChannelMask = c_int64(0)
    AName = POINTER(POINTER(c_char))()
    AComment = POINTER(POINTER(c_char))()

    ret = dll.tsdb_get_flexray_db_properties_by_index_verbose(ADBIndex,byref(ASignalCount),byref(AFrameCount),byref(AECUCount),byref(ASupportedChannelMask),byref(AName),byref(AComment))

    if ret ==0:
        try:
            AComment = string_at(AComment).decode('utf8')
        except:
            AComment = ''
        return AECUCount,AFrameCount,ASignalCount,ASupportedChannelMask,string_at(AName),AComment
    print(tsapp_get_error_description(ret))
    return AECUCount,AFrameCount,ASignalCount,ASupportedChannelMask,string_at(AName),AComment

def tsdb_get_flexray_ecu_properties_by_address_verbose(AAddr:str):
    if not isinstance(AAddr,bytes):
        AAddr = bytes(AAddr)
    ADBIndex =c_int32(0)
    AECUIndex = c_int32(0)
    ATxFrameCount = c_int32(0)
    ARxFrameCount = c_int32(0)
    AName = POINTER(POINTER(c_char))()
    AComment= POINTER(POINTER(c_char))()

    ret = dll.tsdb_get_flexray_ecu_properties_by_address_verbose(AAddr,byref(ADBIndex),byref(AECUIndex),byref(ATxFrameCount),byref(ARxFrameCount),byref(AName),byref(AComment))
    if ret ==0:
        try:
            AComment = string_at(AComment).decode('utf8')
        except:
            AComment = ''
        return ADBIndex,AECUIndex,ATxFrameCount,ARxFrameCount,string_at(AName).decode('utf8'),AComment
    print(tsapp_get_error_description(ret))
    return ADBIndex,AECUIndex,ATxFrameCount,ARxFrameCount,string_at(AName).decode('utf8'),AComment

def tsdb_get_flexray_ecu_properties_by_index_verbose(ADBIndex:c_int32,AECUIndex:c_int32):
    ATxFrameCount = c_int32(0)
    ARxFrameCount = c_int32(0)
    AName = POINTER(POINTER(c_char))()
    AComment= POINTER(POINTER(c_char))()

    ret = dll.tsdb_get_flexray_ecu_properties_by_index_verbose(ADBIndex,AECUIndex,byref(ATxFrameCount),byref(ARxFrameCount),byref(AName),byref(AComment))
    if ret ==0:
        try:
            AComment = string_at(AComment).decode('utf8')
        except:
            AComment = ''
        return ATxFrameCount,ARxFrameCount,string_at(AName).decode('utf8'),AComment
    print(tsapp_get_error_description(ret)) 
    return ATxFrameCount,ARxFrameCount,string_at(AName).decode('utf8'),AComment

def tsdb_get_flexray_frame_properties_by_address_verbose(AAddr:str):
    if not isinstance(AAddr,bytes):
        AAddr = bytes(AAddr)
    ADBIndex= c_int32(0)
    AECUIndex= c_int32(0)
    AFrameIndex= c_int32(0)
    AIsTx= c_bool()
    AFRChannelMask= c_int32(0)
    AFRBaseCycle= c_int32(0)
    AFRCycleRepetition= c_int32(0)
    AFRIsStartupFrame= c_bool()
    AFRSlotId= c_int32(0)
    AFRCycleMask= c_int64(0)
    ASignalCount= c_int32(0)
    AFRDLC = c_int32(0)
    AName = POINTER(POINTER(c_char))()
    AComment= POINTER(POINTER(c_char))()

    ret = dll.tsdb_get_flexray_frame_properties_by_address_verbose(AAddr,byref(ADBIndex),byref(AECUIndex),byref(AFrameIndex),byref(AIsTx),byref(AFRChannelMask),byref(AFRBaseCycle),byref(AFRCycleRepetition),byref(AFRIsStartupFrame),byref(AFRSlotId),byref(AFRCycleMask),byref(ASignalCount),byref(AFRDLC),byref(AName),byref(AComment))
    if ret ==0:
        try:
            AComment = string_at(AComment).decode('utf8')
        except:
            AComment = ''
        return ADBIndex,AECUIndex,AFrameIndex,AIsTx,AFRChannelMask,AFRBaseCycle,AFRCycleRepetition,AFRIsStartupFrame,AFRSlotId,AFRCycleMask,ASignalCount,AFRDLC,string_at(AName).decode('utf8'),AComment
    print(tsapp_get_error_description(ret)) 
    return ADBIndex,AECUIndex,AFrameIndex,AIsTx,AFRChannelMask,AFRBaseCycle,AFRCycleRepetition,AFRIsStartupFrame,AFRSlotId,AFRCycleMask,ASignalCount,AFRDLC,string_at(AName).decode('utf8'),AComment
def tsdb_get_flexray_frame_properties_by_index_verbose(ADBIndex:c_int32,AECUIndex:c_int32,AFrameIndex:c_int32,AIsTx:c_bool):
    AFRChannelMask= c_int32(0)
    AFRBaseCycle= c_int32(0)
    AFRCycleRepetition= c_int32(0)
    AFRIsStartupFrame= c_bool()
    AFRSlotId= c_int32(0)
    AFRCycleMask= c_int64(0)
    ASignalCount= c_int32(0)
    AFRDLC = c_int32(0)
    AName = POINTER(POINTER(c_char))()
    AComment= POINTER(POINTER(c_char))()
    ret = dll.tsdb_get_flexray_frame_properties_by_index_verbose(ADBIndex,AECUIndex,AFrameIndex,AIsTx,byref(AFRChannelMask),byref(AFRBaseCycle),byref(AFRCycleRepetition),byref(AFRIsStartupFrame),byref(AFRSlotId),byref(AFRCycleMask),byref(ASignalCount),byref(AFRDLC),byref(AName),byref(AComment))
    if ret ==0:
        try:
            AComment = string_at(AComment).decode('utf8')
        except:
            AComment = ''
        return AFRChannelMask,AFRBaseCycle,AFRCycleRepetition,AFRIsStartupFrame,AFRSlotId,AFRCycleMask,ASignalCount,AFRDLC,string_at(AName).decode('utf8'),AComment
    print(tsapp_get_error_description(ret)) 
    return AFRChannelMask,AFRBaseCycle,AFRCycleRepetition,AFRIsStartupFrame,AFRSlotId,AFRCycleMask,ASignalCount,AFRDLC,string_at(AName).decode('utf8'),AComment
def tsdb_get_flexray_signal_properties_by_address_verbose(AAddr:str):
    if not isinstance(AAddr,bytes):
        AAddr = bytes(AAddr)
    ADBIndex= c_int32(0)
    AECUIndex= c_int32(0)
    AFrameIndex= c_int32(0)
    ASignalIndex = c_int32(0)
    AIsTx= c_bool()
    ASignalType = c_int(0)
    ACompuMethod = c_int(0)
    AIsIntel = c_bool()
    AStartBit = c_int32(0)
    AUpdateBit = c_int32(0)
    ALength = c_int32(0)
    AFactor = c_double(0)
    AOffset = c_double(0)
    AInitValue = c_double(0)
    AName = POINTER(POINTER(c_char))()
    AComment= POINTER(POINTER(c_char))()

    ret = dll.tsdb_get_flexray_signal_properties_by_address_verbose(AAddr,byref(ADBIndex),byref(AECUIndex),byref(AFrameIndex),byref(ASignalIndex),byref(AIsTx),byref(ASignalType),byref(ACompuMethod),byref(AIsIntel),byref(AStartBit),byref(AUpdateBit),byref(ALength),byref(AFactor),byref(AOffset),byref(AInitValue),byref(AName),byref(AComment))
    if ret ==0:
        try:
            # AName = string_at(AName).encode('utf8')
            AComment = string_at(AComment).decode('utf8')
        except:
            AComment = ''
        return ADBIndex,AECUIndex,AFrameIndex,ASignalIndex,AIsTx,ASignalType,ACompuMethod,AIsIntel,AStartBit,AUpdateBit,ALength,AFactor,AOffset,AInitValue,string_at(AName).decode('utf8'),AComment
    print(tsapp_get_error_description(ret))
    return ADBIndex,AECUIndex,AFrameIndex,ASignalIndex,AIsTx,ASignalType,ACompuMethod,AIsIntel,AStartBit,AUpdateBit,ALength,AFactor,AOffset,AInitValue,AName,AComment
def tsdb_get_flexray_signal_properties_by_index_verbose(ADBIndex:c_int32,AECUIndex:c_int32,AFrameIndex:c_int32,ASignalIndex:c_int32,AIsTx:c_bool):
    ASignalType = c_int(0)
    ACompuMethod = c_int(0)
    AIsIntel = c_bool()
    AStartBit = c_int32(0)
    AUpdateBit = c_int32(0)
    ALength = c_int32(0)
    AFactor = c_double(0)
    AOffset = c_double(0)
    AInitValue = c_double(0)
    AName = POINTER(POINTER(c_char))()
    AComment= POINTER(POINTER(c_char))()

    ret = dll.tsdb_get_flexray_signal_properties_by_index_verbose(ADBIndex,AECUIndex,AFrameIndex,ASignalIndex,AIsTx,byref(ASignalType),byref(ACompuMethod),byref(AIsIntel),byref(AStartBit),byref(AUpdateBit),byref(ALength),byref(AFactor),byref(AOffset),byref(AInitValue),byref(AName),byref(AComment))
    try:
        # AName = string_at(AName).decode('utf8')
        AComment = string_at(AComment).decode('utf8')
    except:
        AComment = ''
        # AName = ''
        # print(AName)
    if ret ==0:
        return ASignalType,ACompuMethod,AIsIntel,AStartBit,AUpdateBit,ALength,AFactor,AOffset,AInitValue,string_at(AName).decode('utf8'),AComment
    print(tsapp_get_error_description(ret))
    return ASignalType,ACompuMethod,AIsIntel,AStartBit,AUpdateBit,ALength,AFactor,AOffset,AInitValue,AName,AComment

def tsdb_get_flexray_db_id(AIndex:c_int32):
    Aid = c_int32(0)
    ret = dll.tsdb_get_flexray_db_id(AIndex,byref(Aid))
    if ret == 0 :
        return Aid
    return tsapp_get_error_description(ret)

def tscom_flexray_rbs_start():
    return dll.tscom_flexray_rbs_start()

def tscom_flexray_rbs_stop():
    return dll.tscom_flexray_rbs_stop()

def tscom_flexray_rbs_is_running():
    AIsRunning = c_bool()
    ret = dll.tscom_flexray_rbs_is_running(byref(AIsRunning))
    if ret == 0 :
        return AIsRunning
    return tsapp_get_error_description(ret)

def tscom_flexray_rbs_configure(AAutoStart:c_bool,AAutoSendOnModification:c_bool,AActivateECUSimulation:c_bool,AInitValueOptions:c_int):
    return dll.tscom_flexray_rbs_configure(AAutoStart,AAutoSendOnModification,AActivateECUSimulation,AInitValueOptions)

def tscom_flexray_rbs_activate_all_clusters(AEnable:c_bool,AIncludingChildren:c_bool):
    return dll.tscc_flexray_rbs_activate_all_clusters(AEnable,AIncludingChildren)

def tscom_flexray_rbs_activate_cluster_by_name(AIdxChn:c_int,AEnable:c_bool,AClusterName:bytes,AIncludingChildren:c_bool):
    return dll.tscom_flexray_rbs_activate_cluster_by_name(AIdxChn,AEnable,AClusterName,AIncludingChildren)

def tscom_flexray_rbs_activate_ecu_by_name(AIdxChn:c_int,AEnable:c_bool,AClusterName:bytes,AECUName:bytes,AIncludingChildren:c_bool):
    return dll.tscom_flexray_rbs_activate_ecu_by_name(AIdxChn,AEnable,AClusterName,AECUName,AIncludingChildren)

def tscom_flexray_rbs_activate_frame_by_name(AIdxChn:c_int,AEnable:c_bool,AClusterName:bytes,AECUName:bytes,AFrameName:bytes):
    return dll.tscom_flexray_rbs_activate_frame_by_name(AIdxChn,AEnable,AClusterName,AECUName,AFrameName)

def tscom_flexray_rbs_get_signal_value_by_element(AIdxChn:c_int32,AClusterName:bytes,AECUName:bytes,AFrameName:bytes,ASignalName:bytes):
    if not isinstance(AClusterName,bytes):
        AClusterName = bytes(AClusterName)
    if not isinstance(AECUName,bytes):
        AECUName = bytes(AECUName)
    if not isinstance(AFrameName,bytes):
        AFrameName = bytes(AFrameName)
    if not isinstance(ASignalName,bytes):
        ASignalName = bytes(ASignalName)
    AValue = c_double(0)
    ret = dll.tscom_flexray_rbs_get_signal_value_by_element(AIdxChn,AClusterName,AECUName,AFrameName,ASignalName,byref(AValue))
    if ret == 0:
        return AValue.value
    return tsapp_get_error_description(ret)

def tscom_flexray_rbs_get_signal_value_by_address(AAddr:bytes):
    AValue = c_double(0)
    ret = dll.tscom_flexray_rbs_get_signal_value_by_address(AAddr,byref(AValue))
    if ret == 0:
        return AValue.value
    return tsapp_get_error_description(ret)

def tscom_flexray_rbs_set_signal_value_by_element(AIdxChn:c_int32,AClusterName:bytes,AECUName:bytes,AFrameName:bytes,ASignalName:bytes,AValue:c_double):
    if not isinstance(AClusterName,bytes):
        AClusterName = bytes(AClusterName)
    if not isinstance(AECUName,bytes):
        AECUName = bytes(AECUName)
    if not isinstance(AFrameName,bytes):
        AFrameName = bytes(AFrameName)
    if not isinstance(ASignalName,bytes):
        ASignalName = bytes(ASignalName)
    return dll.tscom_flexray_rbs_set_signal_value_by_element(AIdxChn,AClusterName,AECUName,AFrameName,ASignalName,AValue)

def tscom_flexray_rbs_set_signal_value_by_address(AAddr:bytes,AValue:c_double):
    # if not isinstance(AAddr,bytes):
    #     AAddr = bytes(AAddr)
    return dll.tscom_flexray_rbs_set_signal_value_by_address(AAddr,AValue)

def tscom_flexray_rbs_enable(AEnable:c_bool):
    return dll.tscom_flexray_rbs_enable(AEnable)

def tscom_flexray_rbs_batch_set_start():
    return dll.tscom_flexray_rbs_batch_set_start()

def tscom_flexray_rbs_batch_set_end():
    return dll.tscom_flexray_rbs_batch_set_end()

def tscom_flexray_rbs_batch_set_signal(AAddr:bytes,AValue:c_double):
    if not isinstance(AAddr,bytes):
        AAddr = bytes(AAddr)
    return dll.tscom_flexray_rbs_batch_set_signal(AAddr,AValue)

def tscom_flexray_rbs_set_frame_direction(AIdxChn:c_int32,AIsTx:c_bool,AClusterName:bytes,AECUName:bytes,AFrameName:bytes):
    if not isinstance(AClusterName,bytes):
        AClusterName = bytes(AClusterName)
    if not isinstance(AECUName,bytes):
        AECUName = bytes(AECUName)
    if not isinstance(AFrameName,bytes):
        AFrameName = bytes(AFrameName)
    return dll.tscom_flexray_rbs_set_frame_direction(AIdxChn,AIsTx,AClusterName,AECUName,AFrameName)

def tscom_flexray_rbs_set_normal_signal(ASymbolAddress:bytes):
    if not isinstance(ASymbolAddress,bytes):
        ASymbolAddress = bytes(ASymbolAddress)
    return dll.tscom_flexray_rbs_set_normal_signal(ASymbolAddress)

def tscom_flexray_rbs_set_rc_signal(ASymbolAddress:bytes):
    if not isinstance(ASymbolAddress,bytes):
        ASymbolAddress = bytes(ASymbolAddress)
    return dll.tscom_flexray_rbs_set_rc_signal(ASymbolAddress)

def tscom_flexray_rbs_set_rc_signal_with_limit(ASymbolAddress:bytes,ALowerLimit:c_int32,AUpperLimit:c_int32):
    if not isinstance(ASymbolAddress,bytes):
        ASymbolAddress = bytes(ASymbolAddress)
    return dll.tscom_flexray_rbs_set_rc_signal(ASymbolAddress,ALowerLimit,AUpperLimit)

def tscom_flexray_rbs_set_crc_signal(ASymbolAddress:bytes,AAlgorithmName:bytes,AIdxByteStart:c_int32,AByteCount:c_int32):
    if not isinstance(ASymbolAddress,bytes):
        ASymbolAddress = bytes(ASymbolAddress)
    if not isinstance(AAlgorithmName,bytes):
        AAlgorithmName = bytes(AAlgorithmName)
    return dll.tscom_flexray_rbs_set_crc_signal(ASymbolAddress,AAlgorithmName,AIdxByteStart,AByteCount)

#Flexray config 
def tsflexray_set_controller_frametrigger(ANodeIndex: c_uint,
                                        AControllerConfig: TLibFlexray_controller_config,
                                        AFrameLengthArray: bytearray,
                                        AFrameNum: c_int, AFrameTrigger: TLibTrigger_def,AFrameTriggerNum: c_int,
                                        ATimeoutMs: c_int):
    r = dll.tsflexray_set_controller_frametrigger(ANodeIndex, byref(AControllerConfig),
                                                AFrameLengthArray, AFrameNum, AFrameTrigger,
                                                AFrameTriggerNum, ATimeoutMs)
    return r


#Flexray 回调事件

def tsapp_register_event_flexray(obj:c_int32,FUNC:OnTx_RxFUNC_Flexray):
    return dll.tsapp_register_event_flexray(byref(obj),FUNC)

def tsapp_unregister_event_flexray(obj:c_int32,FUNC:OnTx_RxFUNC_Flexray):
    return dll.tsapp_unregister_event_flexray(byref(obj),FUNC)

def tsapp_unregister_events_flexray(obj:c_int32):
    return dll.tsapp_unregister_events_flexray(byref(obj))

def tsapp_register_pretx_event_flexray(obj:c_int32,FUNC:OnTx_RxFUNC_Flexray):
    return dll.tsapp_register_pretx_event_flexray(byref(obj),FUNC)

def tsapp_unregister_pretx_event_flexray(obj:c_int32,FUNC:OnTx_RxFUNC_Flexray):
    return dll.tsapp_unregister_pretx_event_flexray(byref(obj),FUNC)

def tsapp_unregister_pretx_events_flexray(obj:c_int32):
    return dll.tsapp_unregister_pretx_events_flexray(byref(obj))

def tscom_flexray_get_signal_definition(ASignalAddress:bytes):
    ASignalDef=TFlexRaySignal()
    ret = dll.tscom_flexray_get_signal_definition(ASignalAddress,byref(ASignalDef))
    if ret == 0:
        return ASignalDef
    return None

tscom_flexray_get_signal_value_in_raw_frame = dll.tscom_flexray_get_signal_value_in_raw_frame #函数对象
tscom_flexray_get_signal_value_in_raw_frame.argtypes = [POINTER(TFlexRaySignal),c_char_p] #指定参数类型
tscom_flexray_get_signal_value_in_raw_frame.restype = c_double 

# tscom_flexray_set_signal_value_in_raw_frame = dll.tscom_flexray_set_signal_value_in_raw_frame #函数对象
# tscom_flexray_set_signal_value_in_raw_frame.argtypes = [POINTER(TFlexRaySignal),c_char_p,c_double] #指定参数类型
# tscom_flexray_set_signal_value_in_raw_frame.restype = c_int32 



def tscom_flexray_set_signal_value_in_raw_frame(AFlexRaySignal:TFlexRaySignal,AData:bytes,AValue:c_double):
    return dll.tscom_flexray_set_signal_value_in_raw_frame(byref(AFlexRaySignal),AData,AValue)

def flexray_db_parse(index):
    ecu_list = {}
    ecuCount, fmeCount, sgnCount, supportedChannelMask, sName, sComment = tsdb_get_flexray_db_properties_by_index_verbose(index)
    for idxECU in range(ecuCount.value):
        message_list = []
        ATxFrameCount, ARxFrameCount, ecuName, sComment = tsdb_get_flexray_ecu_properties_by_index_verbose(index, idxECU)
        # print("ECUName = ",ecuName)
        for idxFme in range(ATxFrameCount.value):
            chnMask, baseCycle, cycleRep, isStartup, slotId, cycleMask, sgnCount, AFRDLC,sName, sComment= ret = tsdb_get_flexray_frame_properties_by_index_verbose(index, idxECU, idxFme, True)
            # print('Tx Frame', sName, ', comment:', sComment, ', base cycle:', baseCycle, ', cycle repetition:', cycleRep, ', slot Id:', slotId, ', cycle mask:', hex(cycleMask.value), ', signal count:', sgnCount)
            _message = message.Message(frame_id=(slotId.value<<16)+(baseCycle.value<<8)+cycleRep.value,name=sName,length= AFRDLC.value,signals=[],is_extended_frame = True,unused_bit_pattern=0xff)
            for idxSgn in range(sgnCount.value):
                    sgnType, compuMethod, isIntel, startBit, updateBit, sgnLen, factor, offset, initValue, sName, sComment = tsdb_get_flexray_signal_properties_by_index_verbose(index, idxECU, idxFme, idxSgn, True)
                    _message.signals.append(signal.Signal(sName,startBit.value,sgnLen.value,byte_order='little_endian' if isIntel else 'big_endian',scale=factor.value,offset=offset.value,initial=initValue.value)) 
            _message = message.Message(_message.frame_id,_message.name,_message.length,_message.signals,is_extended_frame=True,unused_bit_pattern=0xff)
            message_list.append(_message)
                    # print('     Tx Signal', sName, ', comment:', sComment, ', start bit:', startBit, ', len:', sgnLen, ', factor:', factor, ', offset:', offset)
        for idxFme in range(ARxFrameCount.value):   
            chnMask, baseCycle, cycleRep, isStartup, slotId, cycleMask, sgnCount,AFRDLC, sName, sComment = tsdb_get_flexray_frame_properties_by_index_verbose(index, idxECU, idxFme, False)
            # print('Rx Frame', sName, ', comment:', sComment, ', base cycle:', baseCycle, ', cycle repetition:', cycleRep, ', slot Id:', slotId, ', cycle mask:', hex(cycleMask.value), ', signal count:', sgnCount)
            _message = message.Message(frame_id=(slotId.value<<16)+(baseCycle.value<<8)+cycleRep.value,name=sName,length= AFRDLC.value,signals=[],is_extended_frame = True,unused_bit_pattern=0xff)
            for idxSgn in range(sgnCount.value):
                    sgnType, compuMethod, isIntel, startBit, updateBit, sgnLen, factor, offset, initValue, sName, sComment = tsdb_get_flexray_signal_properties_by_index_verbose(index, idxECU, idxFme, idxSgn, False)
                    _message.signals.append(signal.Signal(sName,startBit.value,sgnLen.value,byte_order='little_endian' if isIntel else 'big_endian',scale=factor.value,offset=offset.value,initial=initValue.value)) 
            _message = message.Message(_message.frame_id,_message.name,_message.length,_message.signals,is_extended_frame=True,unused_bit_pattern=0xff)
            message_list.append(_message)
                    # print('     Rx Signal', sName, ', comment:', sComment, ', start bit:', startBit, ', len:', sgnLen, ', factor:', factor, ', offset:', offset)
        ecu_list[ecuName] = message_list
    return ecu_list



