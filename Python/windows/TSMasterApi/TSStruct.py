from ctypes import *
from .TSEnum import *
u8 = c_uint8
pu8 = POINTER(c_uint8)
s8 = c_int8
ps8 = POINTER(c_int8)
u16 = c_uint16
pu16 = POINTER(c_uint16)
s16 = c_int16
ps16 = POINTER(c_int16)
u32 = c_uint32
pu32 = POINTER(c_uint32)
s32 = c_int32
ps32 = POINTER(c_int32)
s64 = c_int64
ps64 = POINTER(c_int64)
u64 = c_uint64
pu64 = POINTER(c_uint64)
double = c_double
pdouble = POINTER(c_double)
pchar = c_char_p
ppchar = POINTER(c_char_p)
char = c_char
single = c_float
psingle = POINTER(c_float)
TObject = c_void_p
pbool = POINTER(c_bool)
pvoid = c_void_p
size_t = c_size_t
psize_t = POINTER(size_t)



DLC_DATA_BYTE_CNT = (
    0, 1, 2, 3, 4, 5, 6, 7,
    8, 12, 16, 20, 24, 32, 48, 64
)

class TLIBCAN(Structure):
    '''
    CAN报文结构体
    关联函数：
    tsapp_transmit_can_async 发送报文
    tsfifo_receive_can_msgs  接收报文
    '''
    _pack_ = 1
    _fields_ = [("FIdxChn", c_uint8),   #通道
                ("FProperties", c_uint8),#属性定义：[7] 0-normal frame, 1-error frame
                                                # [6] 0-not logged, 1-already logged
                                                # [5-3] tbd
                                                # [2] 0-std frame, 1-extended frame
                                                # [1] 0-data frame, 1-remote frame
                                                # [0] dir: 0-RX, 1-TX 

                ("FDLC", c_uint8),           # dlc from 0 to 8
                ("FReserved", c_uint8),
                ("FIdentifier", c_int32),   #ID
                ("FTimeUs", c_int64),      #时间戳
                ("FData", c_uint8 * 8),    #报文数据
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
    
PLIBCAN = POINTER(TLIBCAN)

class TLIBCANFD(Structure):
    '''
    CANFD报文结构体
    关联函数：
    tsapp_transmit_canfd_async 发送报文
    tsfifo_receive_canfd_msgs  接收报文
    '''
    _pack_ = 1
    _fields_ = [("FIdxChn", c_uint8),       #通道
                ("FProperties", c_uint8),   #属性 # [7] 0-normal frame, 1-error frame
                                            # [6] 0-not logged, 1-already logged
                                            # [5-3] tbd
                                            # [2] 0-std frame, 1-extended frame
                                            # [1] 0-data frame, 1-remote frame
                                            # [0] dir: 0-RX, 1-TX
                ("FDLC", c_uint8),          # dlc from 0 to 15
                ("FFDProperties", c_uint8), #FD属性 
                                            # [2] ESI, The E RROR S TATE I NDICATOR (ESI) flag is transmitted dominant by error active nodes, recessive by error passive nodes. ESI does not exist in CAN format frames
                                            # [1] BRS, If the bit is transmitted recessive, the bit rate is switched from the standard bit rate of the A RBITRATION P HASE to the preconfigured alternate bit rate of the D ATA P HASE . If it is transmitted dominant, the bit rate is not switched. BRS does not exist in CAN format frames.
                                            # [0] EDL: 0-normal CAN frame, 1-FD frame, added 2020-02-12, The E XTENDED D 
                ("FIdentifier", c_int32),   #ID
                ("FTimeUs", c_uint64),   #时间戳
                ("FData", c_uint8 * 64),    #数据
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

PLIBCANFD = POINTER(TLIBCANFD)

class TLIBLIN(Structure):
    '''
    LIN报文结构体
    关联函数：
    tsapp_transmit_lin_async 发送报文
    tsfifo_receive_lin_msgs  接收报文
    '''
    _pack_ = 1
    _fields_ = [("FIdxChn", c_uint8),       # channel index starting from 0
                ("FErrStatus", c_uint8),    #  0: normal
                ("FProperties", c_uint8),   # [7] tbd
                                            # [6] 0-not logged, 1-already logged
                                            # [5-4] FHWType #DEV_MASTER,DEV_SLAVE,DEV_LISTENER
                                            # [3] 0-not ReceivedSync, 1- ReceivedSync
                                            # [2] 0-not received FReceiveBreak, 1-Received Break
                                            # [1] 0-not send FReceiveBreak, 1-send Break
                                            # [0] dir: 0-RX, 1-TX
                ("FDLC", c_uint8),          # dlc from 0 to 8
                ("FIdentifier", c_uint8),    #ID
                ("FChecksum", c_uint8),     # LIN checksum
                ("FStatus", c_uint8),       # place holder 1
                ("FTimeUs", c_int64),       # 时间戳
                ("FData", c_uint8 * 8),     # 报文数据
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
    def set_data(self, data):
        lengh = len(data)
        if lengh > DLC_DATA_BYTE_CNT(self.FDLC):
            lengh = DLC_DATA_BYTE_CNT(self.FDLC)
        for i in range(lengh):
            self.FData[i] = data[i]
    def __str__(self):
        field_strings = [f"Timestamp: {self.FTimeUs:>15.6f}"]

        field_strings.append(f"Channel: {self.FIdxChn}")

        FIdentifier = f"ID: {self.FIdentifier:04x}"

        field_strings.append(FIdentifier.rjust(12, " "))
        
        field_strings.append(f"DL: {self.FDLC:2d}")
        data_strings = []
        for i in range(self.FDLC):
            data_strings.append(f"{self.FData[i]:02x}")
        field_strings.append(" ".join(data_strings).ljust(24, " "))
        return "    ".join(field_strings).strip()
    
PLIBLIN = POINTER(TLIBLIN)

class TLIBFlexRay(Structure):
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
        self.FChannelMask = FChannelMask | 0x04
        self.FActualPayloadLength = FActualPayloadLength
        self.FCycleNumber = FCycleNumber  
        self.FPayloadLength = 254  
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
    def __str__(self):
        field_strings = [f"Timestamp: {self.FTimeUs:>15.6f}"]
        FRChannel = str(self.FIdxChn+1) + 'A'
        if (self.FChannelMask & 3) == 1:
            FRChannel = str(self.FIdxChn+1) + 'A'
        elif (self.FChannelMask & 3) == 2:
            FRChannel = str(self.FIdxChn+1) + 'B'
        elif (self.FChannelMask & 3) == 3:
            FRChannel = str(self.FIdxChn+1) + 'AB'
        
        field_strings.append(f"FRChannel: {FRChannel}")

        FIdentifier = f"SlotID: {self.FSlotId}"

        field_strings.append(FIdentifier.rjust(12, " "))
        field_strings.append(str(self.FCycleNumber).rjust(2, " "))
        field_strings.append(f"DL: {self.FActualPayloadLength}")
        data_strings = []
        for i in range(self.FActualPayloadLength):
            data_strings.append(f"{self.FData[i]:02x}")
        field_strings.append(" ".join(data_strings).ljust(24, " "))
        return "    ".join(field_strings).strip()
    
PLIBFlexRay = POINTER(TLIBFlexRay)    
class TLIBFlexray_controller_config(Structure):
    """
    Flexray controller config结构体
    作用:在配置flexray时,需要对硬件参数进行配置
    字段来源:数据库中可获取
    注:在使用该库时,可直接TSMaster加载工程,跳过复杂参数的配置
    关联函数:tsflexray_set_controller_frametrigger
    """
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

    def set_controller_config(self,xml_,is_open_a=True, is_open_b=True, wakeup_chn=0, enable100_a=True, enable100_b=True,is_show_nullframe=True, is_Bridging=False):
        if isinstance(xml_,dict):
            self.NETWORK_MANAGEMENT_VECTOR_LENGTH = xml_['NETWORK_MANAGEMENT_VECTOR_LENGTH']
            self.PAYLOAD_LENGTH_STATIC = xml_['PAYLOAD_LENGTH_STATIC']
            self.LATEST_TX = xml_['LATEST_TX']
            self.T_S_S_TRANSMITTER = xml_['T_S_S_TRANSMITTER']
            self.CAS_RX_LOW_MAX = xml_['CAS_RX_LOW_MAX']
            self.SPEED = xml_['SPEED']
            self.WAKE_UP_SYMBOL_RX_WINDOW = xml_['WAKE_UP_SYMBOL_RX_WINDOW']
            self.WAKE_UP_PATTERN = xml_['WAKE_UP_PATTERN']
            self.WAKE_UP_SYMBOL_RX_IDLE = xml_['WAKE_UP_SYMBOL_RX_IDLE']
            self.WAKE_UP_SYMBOL_RX_LOW = xml_['WAKE_UP_SYMBOL_RX_LOW']
            self.WAKE_UP_SYMBOL_TX_IDLE = xml_['WAKE_UP_SYMBOL_TX_IDLE']
            self.WAKE_UP_SYMBOL_TX_LOW = xml_['WAKE_UP_SYMBOL_TX_LOW']
            self.channelAConnectedNode = 1 if is_open_a else 0
            self.channelBConnectedNode = 1 if is_open_b else 0
            self.channelASymbolTransmitted = 1  
            self.channelBSymbolTransmitted = 1  
            self.ALLOW_HALT_DUE_TO_CLOCK = xml_['ALLOW_HALT_DUE_TO_CLOCK']
            self.SINGLE_SLOT_ENABLED = xml_['SINGLE_SLOT_ENABLED']
            self.wake_up_idx = wakeup_chn
            self.ALLOW_PASSIVE_TO_ACTIVE = xml_['ALLOW_PASSIVE_TO_ACTIVE']
            self.COLD_START_ATTEMPTS = xml_['COLD_START_ATTEMPTS']
            self.synchFrameTransmitted = 1
            self.startupFrameTransmitted = xml_['startupFrameTransmitted']
            self.LISTEN_TIMEOUT = xml_['LISTEN_TIMEOUT']
            self.LISTEN_NOISE = xml_['LISTEN_NOISE']
            self.MAX_WITHOUT_CLOCK_CORRECTION_PASSIVE = xml_['MAX_WITHOUT_CLOCK_CORRECTION_PASSIVE']
            self.MAX_WITHOUT_CLOCK_CORRECTION_FATAL = xml_['MAX_WITHOUT_CLOCK_CORRECTION_FATAL']
            self.MICRO_PER_CYCLE = xml_['MICRO_PER_CYCLE']
            self.Macro_Per_Cycle = xml_['MACRO_PER_CYCLE']
            self.SYNC_NODE_MAX = xml_['SYNC_NODE_MAX']
            self.MICRO_INITIAL_OFFSET_A = xml_['MICRO_INITIAL_OFFSET_A']
            self.MICRO_INITIAL_OFFSET_B = xml_['MICRO_INITIAL_OFFSET_B']
            self.MACRO_INITIAL_OFFSET_A = xml_['MACRO_INITIAL_OFFSET_A']
            self.MACRO_INITIAL_OFFSET_B = xml_['MACRO_INITIAL_OFFSET_B']
            self.N_I_T = xml_['N_I_T']
            self.OFFSET_CORRECTION_START = xml_['OFFSET_CORRECTION_START']
            self.DELAY_COMPENSATION_A = xml_['DELAY_COMPENSATION_A']
            self.DELAY_COMPENSATION_B = xml_['DELAY_COMPENSATION_B']
            self.CLUSTER_DRIFT_DAMPING = xml_['CLUSTER_DRIFT_DAMPING']
            self.DECODING_CORRECTION = xml_['DECODING_CORRECTION']
            self.ACCEPTED_STARTUP_RANGE = xml_['ACCEPTED_STARTUP_RANGE']
            self.MAX_DRIFT = xml_['MAX_DRIFT']
            self.STATIC_SLOT = xml_['STATIC_SLOT']
            self.NUMBER_OF_STATIC_SLOTS = xml_['NUMBER_OF_STATIC_SLOTS']
            self.MINISLOT = xml_['MINISLOT']
            self.NUMBER_OF_MINISLOTS = xml_['NUMBER_OF_MINISLOTS']
            self.DYNAMIC_SLOT_IDLE_PHASE = xml_['DYNAMIC_SLOT_IDLE_PHASE']
            self.ACTION_POINT_OFFSET = xml_['ACTION_POINT_OFFSET']
            self.MINISLOT_ACTION_POINT_OFFSET = xml_['MINISLOT_ACTION_POINT_OFFSET']
            self.OFFSET_CORRECTION_OUT = xml_['OFFSET_CORRECTION_OUT']
            self.RATE_CORRECTION_OUT = xml_['RATE_CORRECTION_OUT']
            self.EXTERN_OFFSET_CORRECTION = xml_['EXTERN_OFFSET_CORRECTION']
            self.EXTERN_RATE_CORRECTION = xml_['EXTERN_RATE_CORRECTION']
            self.config1_byte = 1
                # if
            self.config_byte = 0xc
            if is_Bridging:
                    self.config_byte = 0x3c
            self.config_byte = self.config_byte | (0x1 if enable100_a else 0x00) | (0x2 if enable100_b else 0x00) | (0x40 if is_show_nullframe else 0x00)
        return self
PLIBFlexray_controller_config = POINTER(TLIBFlexray_controller_config) 

class TLIBEthernetHeader(Structure):
    _pack_ = 1
    _fields_ = [
        ('FIdxChn',u8),#app channel index starting from 0 = Network index
        ('FIdxSwitch',u8),#Network's switch index
        ('FIdxPort',u8),# Network's switch's port index, 0~127: measurement port, 128~255: virtual port
        ('FConfig',u8),#  0-1: 0 = Rx, 1 = Tx, 2 = TxRq // 2: crc status, for tx, 0: crc is include in data, 1: crc is not include in data //                for rx, 0: crc is ok, 1: crc is not ok // 3: tx done type, 0: only report timestamp, 1: report full info(header+frame)
        ('FEthernetPayloadLength',u16),# Length of Ethernet payload data in bytes. Max. 1582 Byte(without Ethernet header), 1612 Byte(Inclusive ethernet header)
        ('freserved',u16),#Reserved
        ('FTimeUs',u64),#timestamp in us
        ('FEthernetDataAddr',pu8),#data ps32
        ('FPaddings',u32),#to be compatible with x64
        ]
    def __init__(self, APayloadLength,AEthernetDataAddr) -> None:
        self.FIdxChn = 0
        self.FIdxSwitch = 0
        self.FIdxPort = 0
        self.FConfig = 0
        self.FEthernetPayloadLength = APayloadLength
        self.FReserved = 0
        self.FTimeUs = 0
        self.FEthernetDataAddr = AEthernetDataAddr
        self.FPadding = 0
        n = min(1612 - 14,APayloadLength)
        n += 14
        for i in range(0,n):
            self.FEthernetDataAddr[i] = 0
        self.FEthernetDataAddr[12] = 0
        self.FEthernetDataAddr[13] = 0
        for i in range(6):
            self.FEthernetDataAddr[i] = 0xFF  
        # pu8 p = FEthernetDataAddr
        # s32 n = MIN(1612 - 14, APayloadLength)
        # n += 14
        # for (i=0 i<n i++){
        #     *p++ = 0
        # }
        # *(pu16)(ethernet_type_addr()) = 0x00 // IPV4 = swap(0x0800)
        # p = destination_mac_addr()
        # for (i=0 i<6 i++){
        #     *p++ = 0xFF
        # }

PLIBEthernetHeader = POINTER(TLIBEthernetHeader)


class TLIBFlexRayClusterParameters(Structure):
    _pack_ = 1
    _fields_ = [
        ('FShortName',char * 32),#
        ('FLongName',char * 32),#
        ('FDescription',char * 32),#
        ('FSpeed',char * 32),#
        (' FChannels',char * 32),#
        ('FBitCountingPolicy',char * 32),#
        ('FProtocol',char * 32),#
        ('FProtocolVersion',char * 32),#
        ('FMedium',char * 32),#
        ('FIsHighLowBitOrder',s32),#
        ('FMaxFrameLengthByte',s32),#
        ('FNumberOfCycles',s32),#cycle parameters
        ('FCycle_us',s32),#
        ('FBit_us',double),#
        ('FSampleClockPeriod_us',double),#
        (' FMacrotick_us',double),#
        ('FMacroPerCycle',s32),#
        ('FNumberOfStaticSlots',s32),#
        ('FStaticSlot_MT',s32),#
        ('FActionPointOffset_MT',s32),#
        ('FTSSTransmitter_gdBit',s32),#
        ('FPayloadLengthStatic_WORD',s32),#
        ('FNumberOfMiniSlots',s32),#
        ('FMiniSlot_MT',s32),#
        ('FMiniSlotActionPointOffset_MT',s32),#
        ('FDynamicSlotIdlePhase_MiniSlots',s32),#
        (' FSymbolWindow_MT',s32),#
        ('FNIT_MT',s32),#
        ('FSyncNodeMax',s32),#
        ('FNetworkManagementVectorLength',s32),#Wakeup and startup parameters
        ('FListenNoise',s32),#
        ('FColdStartAttempts',s32),#
        ('FCASRxLowMax_gdBit',s32),#
        ('FWakeupSymbolRxIdle_gdBit',s32),#
        ('FWakeupSymbolRxLow_gdBit',s32),#
        (' FWakeupSymbolRxWindow_gdBit',s32),#
        ('FWakeupSymbolTxIdle_gdBit',s32),#
        ('FWakeupSymbolTxLow_gdBit',s32),#
        ('FMaxInitializationError_us',double),#clock correction parameters
        ('FClusterDriftDamping_uT',s32),#
        ('FOffsetCorrectionStart_MT',s32),#
        ('FMaxWithoutClockCorrectionFatal',s32),#
        ('FMaxWithoutClockCorrectionPassive',s32),#
        ]
PLIBFlexRayClusterParameters = POINTER(TLIBFlexRayClusterParameters)
class TLIBFlexRayControllerParameters(Structure):
    _pack_ = 1
    _fields_ = [
        ('FShortName',char * 32),#
        ('FConnectedChannels',char * 32),#cycle parameters
        ('FMicroPerCycle_uT',s32),#
        ('FMicroPerMacroNom_uT',s32),#
        ('FMicroTick_us',double),#
        ('FSamplesPerMicrotick',s32),#wakeup & startup parameters
        (' FWakeupChannelA',s32),#
        (' FWakeupChannelB',s32),#
        (' FMaxDrift_uT',s32),#
        (' FWakeupPattern',s32),#
        (' FListenTimeout_uT',s32),#
        (' FAcceptedStartupRange_uT',s32),#
        (' FMacroInitialOffsetA_MT',s32),#
        (' FMacroInitialOffsetB_MT',s32),#
        (' FMacroInitialOffsetA_uT',s32),#
        (' FMacroInitialOffsetB_uT',s32),#clock correction parameters
        (' FKeySlotUsage',char * 32),#
        (' FKeySlotID',s32),#
        (' FsingleSlotEnabled',s32),#
        (' FClusterDriftDamping_uT',s32),#
        (' FDocodingCorrection_uT',s32),#
        (' FDelayCompensationA_uT',s32),#
        (' FDelayCompensationB_uT',s32),#
        (' FOffsetCorrectionOut_uT',s32),#
        (' FExternRateCorrection_uT',s32),#
        (' FRateCorrectionOut_uT',s32),#
        (' FExternOffsetCorrection_uT',s32),#
        (' FAllowHaltDueToClock',s32),#
        (' FAllowPassivToActive',s32),#latesttx
        (' FLatestTx',s32),#
        (' FMaxDynamicPayloadLength',s32),#
        ]
PLIBFlexRayControllerParameters = POINTER(TLIBFlexRayControllerParameters)
class TLIBEthernetMAX(Structure):
    _pack_ = 1
    _fields_ = [
        ('FHeader',TLIBEthernetHeader),#
        ('FBytes',u8 * 1612),#starting by destination MAC, source MAC, ethernet type, payload...
        ]
PLIBEthernetMAX = POINTER(TLIBEthernetMAX)
class TLIBTrigger_def(Structure):
    _pack_ = 1
    _fields_ = [
        ('frame_idx',u8),#
        ('slot_id',u8),#
        ('cycle_code',u8),#BASE-CYCLE + CYCLE-REPETITION
        ('config_byte',u8),#//bit 0:是否使能通道A//bit 1:是否使能通道B//bit 2:是否网络管理报文//bit 3:传输模式，0表示连续传输，1表示单次触发//bit 4:是否为冷启动报文，只有缓冲区0可以置1//bit 5:是否为同步报文，只有缓冲区0/1可以置1//bit 6://bit 7:帧类型：0-静态，1-动态
        ]
PLIBTrigger_def = POINTER(TLIBTrigger_def)
class TLIBGPSData(Structure):
    _pack_ = 1
    _fields_ = [
        ('FTimeUS',u64),#timestamp in us
        ('UTCTime',u32),#
        ('UTCDate',u32),#
        ('Latitude',single),#
        ('Longitude',single),#
        ('Speed',single),#
        ('Direct',single),#
        ('Altitude',single),#
        ('N_S',u8),#
        ('E_W',u8),#
        ('Satellite',u8),#
        ('FIdxChn',u8),#
        ]
PLIBGPSData = POINTER(TLIBGPSData)
class TLIBEth_CMD_config(Structure):
    _pack_ = 1
    _fields_ = [
        ('eth_config0',u8),#//bit 0-1 phy_type:2; //0: 100base-Tx/1000Base-T, 1: 100/1000Base-T1, 2,3: rev//bit2 auto_neg : 1;//bit3-4: speed : 2; //0-10mbps, 1-100mbps, 2-1000mbps//bit5: is_master : 1;//bit6-7 loop : 2;//0: no loop, 1: mac_loop, 2: phy-loop, 3: phy_remote loop
        ('eth_config1',u8),#//bit0 wakeup : 1;//0-disable, 1-enable//bit1-4 test_mode : 4;//  0x00 normal operation  other test mode//bit5-6 tx_mode : 2;//  0x00 enable 0x01 disable//bit7  enable : 1;
        ('eth_config2',u8),#//bit0-4 phy_addr : 5;//bit5 accept wrong crc frame:1
        ('eth_config3',u8),#//bit0: disable_promiscuous_mode//bit1: enable_recieve_all//bit2-3: enable_srouce_fileter: 0 disable 1: enable 2 inverse//bit4: inverse_dest_fileter//bit5-6: ControlFrames: 0: block all  1: forward all  2: forward by filter//bit7: enable rx broadcast frame
        ('filter_config0',u8),#//bit0-1: multicast frame filter: 0: no filter  1: perfect 2: hash 3: hash and perfect//bit2-3: unicast frame filter: 0: perfect 1: hash 2: hash and perfect
        ('filter_config1',u8),#
        ('filter_hash_table',u64),#//bit0-47: mac addr For example, if 0x112233445566 is received//          (0x11 in lane 0 of the first column) on the MII as the destination address, then the//          MacAddress0 Register [47:0] is compared with 0x665544332211//          perfect0 is always enable
        ('filter_perfect0',u64),#//bit63: AE: Address Enable, When this bit is set, the address filter module uses the second MAC address for perfect//          filtering. When this bit is reset, the address filter module ignores the address for filtering.//bit62: SA: Source Address://          When this bit is set, the MAC Address1[47:0] is used to compare with the SA fields of the//          received packet. When this bit is reset, the MAC Address x[47:0] is used to compare with the//          DA fields of the received packet.//bit56-61: MBC[5:0]: Mask Byte Control//          These bits are mask control bits for comparing each of the MAC Address bytes. When set//          high, the MAC does not compare the corresponding byte of received DA or SA with the//          contents of MAC Address1 registers. Each bit controls the masking of the bytes as follows://          Bit 29: Register 194[15:8]//          Bit 28: Register 194[7:0]//          Bit 27: Register 195[31:24]//          ..//          Bit 24: Register 195[7:0]//          You can filter a group of addresses (known as group address filtering) by masking one or//          more bytes of the address.//bit0-47:  same as filter_perfect0
        ('filter_perfect1',u64),#
        ('rev',u64 * 6),#48
        ]
PLIBEth_CMD_config = POINTER(TLIBEth_CMD_config)
class Trealtime_comment_t(Structure):
    _pack_ = 1
    _fields_ = [
        ('FTimeUs',s64),#
        ('FEventType',s32),#
        ('FCapacity',s32),#
        ('FComment',pchar),#
        ('FPadding',u32),#to be compatible with x64
        ]
Prealtime_comment_t = POINTER(Trealtime_comment_t)
class TLIBSystemVar(Structure):
    _pack_ = 1
    _fields_ = [
        ('FTimeUs',s64),#
        ('FType',s32),#
        ('FNameCapacity',u32),#
        ('FDataCapacity',u32),#
        ('FName',pchar),#
        ('FData',pu8),#
        ('FPadding',s64),#to be compatible with x64
        ]
PLIBSystemVar = POINTER(TLIBSystemVar)
class TMPCANSignal(Structure):
    _pack_ = 1
    _fields_ = [
        ('FCANSgnType',u8),#0 - Unsigned, 1 - Signed, 2 - single 32, 3 - Double 64
        ('FIsIntel', c_bool),#
        ('FStartBit',s32),#
        ('FLength',s32),#
        ('FFactor',double),#
        ('FOffset',double),#
        ]
PMPCANSignal = POINTER(TMPCANSignal)
class TMPLINSignal(Structure):
    _pack_ = 1
    _fields_ = [
        ('FLINSgnType',u8),#0 - Unsigned, 1 - Signed, 2 - single 32, 3 - Double 64
        ('FIsIntel', c_bool),#
        ('FStartBit',s32),#
        ('FLength',s32),#
        ('FFactor',double),#
        ('FOffset',double),#
        ]
PMPLINSignal = POINTER(TMPLINSignal)
class TMPFlexRaySignal(Structure):
    _pack_ = 1
    _fields_ = [
        ('FFRSgnType',u8),#0 - Unsigned, 1 - Signed, 2 - single 32, 3 - Double 64
        ('FCompuMethod',u8),#0 - Identical, 1 - Linear, 2 - Scale Linear, 3 - TextTable, 4 - TABNoIntp, 5 - Formula
        ('FReserved',u8),#
        ('FIsIntel', c_bool),#
        ('FStartBit',s32),#
        ('FUpdateBit',s32),#
        ('FLength',s32),#
        ('FFactor',double),#
        ('FOffset',double),#
        ('FActualStartBit',s32),#added 2023-07-18
        ('FActualUpdateBit',s32),#added 2023-07-18
        ]
PMPFlexRaySignal = POINTER(TMPFlexRaySignal)
class TMPDBProperties(Structure):
    _pack_ = 1
    _fields_ = [
        ('FDBIndex',s32),#
        ('FSignalCount',s32),#
        ('FFrameCount',s32),#
        ('FECUCount',s32),#
        ('FSupportedChannelMask',u64),#
        ('FName',char * 512),#
        ('FComment',char * 512),#
        ('FFlags',u64),#Bit 0: whether generate mp header
        ]
PMPDBProperties = POINTER(TMPDBProperties)
class TMPDBECUProperties(Structure):
    _pack_ = 1
    _fields_ = [
        ('FDBIndex',s32),#
        ('FECUIndex',s32),#
        ('FTxFrameCount',s32),#
        ('FRxFrameCount',s32),#
        ('FName',char * 512),#
        ('FComment',char * 512),#
        ]
PMPDBECUProperties = POINTER(TMPDBECUProperties)
class TMPDBFrameProperties(Structure):
    _pack_ = 1
    _fields_ = [
        ('FDBIndex',s32),#
        ('FECUIndex',s32),#
        ('FFrameIndex',s32),#
        ('FIsTx',u8),#
        ('FReserved1',u8),#
        ('FCycleTimeMs',u16),#
        ('FFrameType',s32),#
        ('FCANIsDataFrame',u8),#
        ('FCANIsStdFrame',u8),#
        ('FCANIsEdl',u8),#
        ('FCANIsBrs',u8),#
        ('FCANIdentifier',s32),#
        ('FCANDLC',s32),#
        ('FCANDataBytes',s32),#
        ('FLINIdentifier',s32),#
        ('FLINDLC',s32),#
        ('FFRChannelMask',u8),#
        ('FFRBaseCycle',u8),#
        ('FFRCycleRepetition',u8),#
        ('FFRIsStartupFrame',u8),#
        ('FFRSlotId',u16),#
        ('FFRDLC',u16),#
        ('FFRCycleMask',u64),#
        ('FSignalCount',s32),#
        ('FName',char * 512),#
        ('FComment',char * 512),#
        ]
PMPDBFrameProperties = POINTER(TMPDBFrameProperties)
class TMPDBSignalProperties(Structure):
    _pack_ = 1
    _fields_ = [
        ('FDBIndex',s32),#
        ('FECUIndex',s32),#
        ('FFrameIndex',s32),#
        ('FSignalIndex',s32),#
        ('FIsTx',u8),#
        ('FReserved1',u8),#
        ('FReserved2',u8),#
        ('FReserved3',u8),#
        ('FSignalType',s32),#
        ('FCANSignal',TMPCANSignal),#
        ('FLINSignal',TMPLINSignal),#
        ('FFlexRaySignal',TMPFlexRaySignal),#
        ('FParentFrameId',s32),#
        ('FInitValue',double),#
        ('FName',char * 512),#
        ('FComment',char * 512),#
        ]
PMPDBSignalProperties = POINTER(TMPDBSignalProperties)
class TLIBHWInfo(Structure):
    _pack_ = 1
    _fields_ = [
        ('FDeviceType',s32),#
        ('FDeviceIndex',s32),#
        ('FVendorName',char * 32),#
        ('FDeviceName',char * 32),#
        ('FSerialString',char * 64),#
        ]
PLIBHWInfo = POINTER(TLIBHWInfo)
class TLIBTSMapping(Structure):
    _pack_ = 1
    _fields_ = [
        ('FAppName',char * 32),#
        ('FAppChannelIndex',s32),#
        ('FAppChannelType',s32),#
        ('FHWDeviceType',s32),#
        ('FHWIndex',s32),#
        ('FHWChannelIndex',s32),#
        ('FHWDeviceSubType',s32),#
        ('FHWDeviceName',char * 32),#
        ('FMappingDisabled', c_bool),#
        ]
PLIBTSMapping = POINTER(TLIBTSMapping)
class TLIBSystemVarDef(Structure):
    _pack_ = 1
    _fields_ = [
        ('FName',char * 32),#
        ('FCategory',char * 32),#
        ('FComment',char * 32),#
        ('FDataType',s32),#
        ('FIsReadOnly', c_bool),#
        ('FValueMin',double),#
        ('FValueMax',double),#
        ('FUnit',char * 32),#
        ]
PLIBSystemVarDef = POINTER(TLIBSystemVarDef)
class Tip4_addr_t(Structure):
    _pack_ = 1
    _fields_ = [
        ('addr',u32),#
        ]
Pip4_addr_t = POINTER(Tip4_addr_t)
class Tip6_addr_t(Structure):
    _pack_ = 1
    _fields_ = [
        ('addr',u32 * 4),#
        ('zone',u8),#
        ]
Pip6_addr_t = POINTER(Tip6_addr_t)
class Tts_sockaddr(Structure):
    _pack_ = 1
    _fields_ = [
        ('sa_len',u8),#
        ('sa_family',u8),#
        ('sa_data',char * 14),#
        ]
Pts_sockaddr = POINTER(Tts_sockaddr)
class Tts_iovec(Structure):
    _pack_ = 1
    _fields_ = [
        ('iov_base',TObject),#
        ('iov_len',size_t),#
        ]
Pts_iovec = POINTER(Tts_iovec)
class Tts_msghdr(Structure):
    _pack_ = 1
    _fields_ = [
        ('msg_name',TObject),#
        ('msg_namelen',u32),#
        ('msg_iov',Pts_iovec),#
        ('msg_iovlen',s32),#
        ('msg_control',TObject),#
        ('msg_controllen',u32),#
        ('msg_flags',s32),#
        ]
Pts_msghdr = POINTER(Tts_msghdr)
class Tts_fd_set(Structure):
    _pack_ = 1
    _fields_ = [
        ('fd_bits',u8 * 2),#
        ]
Pts_fd_set = POINTER(Tts_fd_set)
class Tts_timeval(Structure):
    _pack_ = 1
    _fields_ = [
        ('tv_sec',u32),#
        ('tv_usec',u32),#
        ]
Pts_timeval = POINTER(Tts_timeval)
class Tts_pollfd(Structure):
    _pack_ = 1
    _fields_ = [
        ('fd',s32),#
        ('events',s16),#
        ('revents',s16),#
        ]
Pts_pollfd = POINTER(Tts_pollfd)
class Tts_sockaddr_in(Structure):
    _pack_ = 1
    _fields_ = [
        ('sin_len',u8),#
        ('sin_family',u8),#
        ('sin_port',u16),#
        ('sin_addr',Tip4_addr_t),#
        ('sin_zero',u8 * 8),#
        ]
Pts_sockaddr_in = POINTER(Tts_sockaddr_in)
class Tip_addr_t(Structure):
    _pack_ = 1
    _fields_ = [
        ('ip4Or6',Tip6_addr_t),#
        ('FType',u32),#
        ]
Pip_addr_t = POINTER(Tip_addr_t)
