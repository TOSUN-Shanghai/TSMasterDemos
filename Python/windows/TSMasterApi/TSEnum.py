from enum import IntEnum, IntFlag
from ctypes import *
ps32 = POINTER(c_int32)
TS_AF_INET         = 2
TS_SOCK_STREAM     = 1
TS_SOCK_DGRAM      = 2
TS_SOCK_RAW        = 3
class CEnum(IntEnum):
    @classmethod
    def from_param(cls, self):
        if not isinstance(self, cls):
            raise TypeError
        return self    
class _TLIBBusToolDeviceType(CEnum):
    BUS_UNKNOWN_TYPE = 0
    TS_TCP_DEVICE = 1
    XL_USB_DEVICE = 2
    TS_USB_DEVICE = 3
    PEAK_USB_DEVICE = 4
    KVASER_USB_DEVICE = 5
    ZLG_USB_DEVICE = 6
    ICS_USB_DEVICE = 7
    TS_TC1005_DEVICE = 8
    CANABLE_USB_DEVICE = 9
    TS_WIRELESS_OBD = 10
    TS_USB_DEVICE_EX = 11
    IXXAT_USB_DEVICE = 12
    BUS_DEV_TYPE_COUNT = 13
TLIBBusToolDeviceType = c_int32
PLIBBusToolDeviceType = ps32

class _TLIBApplicationChannelType(CEnum):
    APP_CAN = 0
    APP_LIN = 1
    APP_FlexRay = 2
    APP_Ethernet = 3
TLIBApplicationChannelType = c_int32
PLIBApplicationChannelType = ps32

class _TSignalType(CEnum):
    stCANSignal = 0
    stLINSignal = 1
    stSystemVar = 2
    stFlexRay = 3
    stEthernet = 4
TSignalType = c_int32
PSignalType = ps32

class _TTimeRangeTestMode(CEnum):
    trmRelativeMode = 0
    trmTriggeredMode = 1
    trmAbsoluteMode = 2
TTimeRangeTestMode = c_int32
PTimeRangeTestMode = ps32

class _TTriggerSignalType(CEnum):
    tstCANSignal = 0
    tstLINSignal = 1
    tstSystemVar = 2
    tstFlexRay = 3
    tstExpression = 4
TTriggerSignalType = c_int32
PTriggerSignalType = ps32

class _TSignalCheckKind(CEnum):
    sckAlways = 0
    sckAppear = 1
    sckStatistics = 2
    sckRisingEdge = 3
    sckFallingEdge = 4
    sckMonotonyRising = 5
    sckMonotonyFalling = 6
    sckFollow = 7
    sckJump = 8
    sckNoChange = 9
TSignalCheckKind = c_int32
PSignalCheckKind = ps32

class _TSignalTesterFailReason(CEnum):
    tfrNoError = 0
    tfrCheckSignalNotExistsInDB = 1
    tfrMinBiggerThanMax = 2
    tfrStartTimeBiggerThanEndTime = 3
    tfrTriggerMinBiggerThanMax = 4
    tfrSignalCountIs0 = 5
    tfrFollowSignalNotExistsInDB = 6
    tfrTriggerSignalNotExistsInDB = 7
    tfrSignalFollowViolation = 8
    tfrSignalMonotonyRisingViolation = 9
    tfrSignalMonotonyFallingViolation = 10
    tfrSignalNoChangeViolation = 11
    tfrSignalValueOutOfRange = 12
    tfrCANSignalNotExists = 13
    tfrLINSignalNotExists = 14
    tfrFlexRaySignalNotExists = 15
    tfrSystemVarNotExists = 16
    tfrSignalTesterStartFailedDueToInvalidConf = 17
    tfrSignalValueNotExists = 18
    tfrStatisticsCheckViolation = 19
    tfrTriggerValueNotExists = 20
    tfrFollowValueNotExists = 21
    tfrTriggerValueNeverInRange = 22
    tfrTimeRangeNotTouched = 23
    tfrRisingNotDetected = 24
    tfrFallingNotDetected = 25
    tfrNotAppeared = 26
    tfrJumpNotDetected = 27
TSignalTesterFailReason = c_int32
PSignalTesterFailReason = ps32

class _TSignalStatisticsKind(CEnum):
    sskMin = 0
    sskMax = 1
    sskAverage = 2
    sskStdDeviation = 3
TSignalStatisticsKind = c_int32
PSignalStatisticsKind = ps32

class _TFlexRayCompuMethod(CEnum):
    fcmIdentical = 0
    fcmLinear = 1
    fcmScaleLinear = 2
    fcmTextTable = 3
    fcmTABNoIntp = 4
    fcmFormula = 5
TFlexRayCompuMethod = c_int32
PFlexRayCompuMethod = ps32

class _TLIBCANBusStatistics(CEnum):
    cbsBusLoad = 0
    cbsPeakLoad = 1
    cbsFpsStdData = 2
    cbsAllStdData = 3
    cbsFpsExtData = 4
    cbsAllExtData = 5
    cbsFpsStdRemote = 6
    cbsAllStdRemote = 7
    cbsFpsExtRemote = 8
    cbsAllExtRemote = 9
    cbsFpsErrorFrame = 10
    cbsAllErrorFrame = 11
TLIBCANBusStatistics = c_int32
PLIBCANBusStatistics = ps32

class _TUDPFragmentProcessStatus(CEnum):
    ufpsNotFragment = 0
    ufpsInvalid = 1
    ufpsProcessing = 2
    ufpsDone = 3
TUDPFragmentProcessStatus = c_int32
PUDPFragmentProcessStatus = ps32

class _TLIBSystemVarType(CEnum):
    lsvtInt32 = 0
    lsvtUInt32 = 1
    lsvtInt64 = 2
    lsvtUInt64 = 3
    lsvtUInt8Array = 4
    lsvtInt32Array = 5
    lsvtInt64Array = 6
    lsvtDouble = 7
    lsvtDoubleArray = 8
    lsvtString = 9
TLIBSystemVarType = c_int32
PLIBSystemVarType = ps32

class _TSymbolMappingDirection(CEnum):
    smdBiDirection = 0
    smdSgnToSysVar = 1
    smdSysVarToSgn = 2
TSymbolMappingDirection = c_int32
PSymbolMappingDirection = ps32

class _TReplayPhase(CEnum):
    rppInit = 0
    rppReplaying = 1
    rppEnded = 2
TReplayPhase = c_int32
PReplayPhase = ps32

class _TLIBOnlineReplayTimingMode(CEnum):
    ortImmediately = 0
    ortAsLog = 1
    ortDelayed = 2
TLIBOnlineReplayTimingMode = c_int32
PLIBOnlineReplayTimingMode = ps32

class _TLIBOnlineReplayStatus(CEnum):
    orsNotStarted = 0
    orsRunning = 1
    orsPaused = 2
    orsCompleted = 3
    orsTerminated = 4
TLIBOnlineReplayStatus = c_int32
PLIBOnlineReplayStatus = ps32

class _TLIBRBSInitValueOptions(CEnum):
    rivUseDB = 0
    rivUseLast = 1
    rivUse0 = 2
TLIBRBSInitValueOptions = c_int32
PLIBRBSInitValueOptions = ps32

class _TSupportedObjType(CEnum):
    sotCAN = 0
    sotLIN = 1
    sotCANFD = 2
    sotRealtimeComment = 3
    sotSystemVar = 4
    sotFlexRay = 5
    sotEthernet = 6
    sotUnknown = 268435455
TSupportedObjType = c_int32
PSupportedObjType = ps32

class _TLIBAutomationModuleRunningState(CEnum):
    amrsNotRun = 0
    amrsPrepareRun = 1
    amrsRunning = 2
    amrsPaused = 3
    amrsStepping = 4
    amrsFinished = 5
TLIBAutomationModuleRunningState = c_int32
PLIBAutomationModuleRunningState = ps32

class _TLIBAutomationSignalType(CEnum):
    lastCANSignal = 0
    lastLINSignal = 1
    lastSysVar = 2
    lastLocalVar = 3
    lastConst = 4
    lastFlexRaySignal = 5
    lastImmediateValue = 6
    lastUnknown = 268435455
TLIBAutomationSignalType = c_int32
PLIBAutomationSignalType = ps32

class _TLIBMPFuncSource(CEnum):
    lmfsSystemFunc = 0
    lmfsMPLib = 1
    lmfsInternal = 2
TLIBMPFuncSource = c_int32
PLIBMPFuncSource = ps32

class _TLIBSimVarType(CEnum):
    lvtInteger = 0
    lvtDouble = 1
    lvtString = 2
    lvtCANMsg = 3
    lvtCANFDMsg = 4
    lvtLINMsg = 5
    lvtUnknown = 268435455
TLIBSimVarType = c_int32
PLIBSimVarType = ps32

class _TSTIMSignalStatus(CEnum):
    sssStopped = 0
    sssRunning = 1
    sssPaused = 2
TSTIMSignalStatus = c_int32
PSTIMSignalStatus = ps32

class _TLIBCANFDControllerType(CEnum):
    lfdtCAN = 0
    lfdtISOCAN = 1
    lfdtNonISOCAN = 2
TLIBCANFDControllerType = c_int32
PLIBCANFDControllerType = ps32

class _TLIBCANFDControllerMode(CEnum):
    lfdmNormal = 0
    lfdmACKOff = 1
    lfdmRestricted = 2
    lfdmInternalLoopback = 3
    lfdmExternalLoopback = 4
TLIBCANFDControllerMode = c_int32
PLIBCANFDControllerMode = ps32

class _TLIB_TS_Device_Sub_Type(CEnum):
    TS_UNKNOWN_DEVICE = 0
    TSCAN_PRO = 1
    TSCAN_Lite1 = 2
    TC1001 = 3
    TL1001 = 4
    TC1011 = 5
    TM5011 = 6
    TC1002 = 7
    TC1014 = 8
    TSCANFD2517 = 9
    TC1026 = 10
    TC1016 = 11
    TC1012 = 12
    TC1013 = 13
    TLog1002 = 14
    TC1034 = 15
    TC1018 = 16
    GW2116 = 17
    TC2115 = 18
    MP1013 = 19
    TC1113 = 20
    TC1114 = 21
    TP1013 = 22
    TC1017 = 23
    TP1018 = 24
    TF10XX = 25
    TL1004_FD_4_LIN_2 = 26
    TE1051 = 27
    TP1051 = 28
    TP1034 = 29
    TTS9015 = 30
    TP1026 = 31
    TTS1026 = 32
    TTS1034 = 33
    TTS1018 = 34
TLIB_TS_Device_Sub_Type = c_int32
PLIB_TS_Device_Sub_Type = ps32

class _TLIB_XL_Device_Sub_Type(CEnum):
    XL_NONE = 0
    XL_VIRTUAL = 1
    XL_CANCARDX = 2
    XL_CANAC2PCI = 6
    XL_CANCARDY = 12
    XL_CANCARDXL = 15
    XL_CANCASEXL = 21
    XL_CANCASEXL_LOG_OBSOLETE = 23
    XL_CANBOARDXL = 25
    XL_CANBOARDXL_PXI = 27
    XL_VN2600 = 29
    XL_VN3300 = 37
    XL_VN3600 = 39
    XL_VN7600 = 41
    XL_CANCARDXLE = 43
    XL_VN8900 = 45
    XL_VN8950 = 47
    XL_VN2640 = 53
    XL_VN1610 = 55
    XL_VN1630 = 57
    XL_VN1640 = 59
    XL_VN8970 = 61
    XL_VN1611 = 63
    XL_VN5610 = 65
    XL_VN5620 = 66
    XL_VN7570 = 67
    XL_IPCLIENT = 69
    XL_IPSERVER = 71
    XL_VX1121 = 73
    XL_VX1131 = 75
    XL_VT6204 = 77
    XL_VN1630_LOG = 79
    XL_VN7610 = 81
    XL_VN7572 = 83
    XL_VN8972 = 85
    XL_VN0601 = 87
    XL_VN5640 = 89
    XL_VX0312 = 91
    XL_VH6501 = 94
    XL_VN8800 = 95
    XL_IPCL8800 = 96
    XL_IPSRV8800 = 97
    XL_CSMCAN = 98
    XL_VN5610A = 101
    XL_VN7640 = 102
    XL_VX1135 = 104
    XL_VN4610 = 105
    XL_VT6306 = 107
    XL_VT6104A = 108
    XL_VN5430 = 109
    XL_VN1530 = 112
    XL_VN1531 = 113
TLIB_XL_Device_Sub_Type = c_int32
PLIB_XL_Device_Sub_Type = ps32

class _TLINNodeType(CEnum):
    T_MasterNode = 0
    T_SlaveNode = 1
    T_MonitorNode = 2
TLINNodeType = c_int32
PLINNodeType = ps32

class _TLINProtocol(CEnum):
    LIN_PROTOCL_13 = 0
    LIN_PROTOCL_20 = 1
    LIN_PROTOCL_21 = 2
    LIN_PROTOCL_J2602 = 3
TLINProtocol = c_int32
PLINProtocol = ps32

class _ISO_TP_RESAULT(CEnum):
    N_OK = 0
    N_TP_TIMEOUT_AS = 139
    N_TP_TIMEOUT_AR = 140
    N_TP_TIMEOUT_BS = 141
    N_TP_TIMEOUT_CR = 142
    N_TP_WRONG_SN = 143
    N_TP_INVALID_FS = 144
    N_TP_UNEXP_PDU = 145
    N_TP_WFT_OVRN = 146
    N_TP_BUFFER_OVFLW = 147
    N_TP_NOT_IDLE = 148
    N_TP_ERROR_FROM_CAN_DRIVER = 149
    N_LIN_MASTER_TRANSMIT_N_AS_TIMEOUT = 202
    N_LIN_MASTER_TRANSMIT_TRANSMIT_ERROR = 203
    N_LIN_MASTER_REV_N_CR_TIMEOUT = 204
    N_LIN_MASTER_REV_ERROR = 205
    N_LIN_MASTER_REV_INTERLLEAVE_TIMEOUT = 206
    N_LIN_MASTER_REV_NO_RESPONSE = 207
    N_LIN_MASTER_REV_SN_ERROR = 208
    N_LIN_SLAVE_TRANSMIT_N_CR_TIMEOUT = 209
    N_LIN_SLAVE_REV_N_CR_TIMEOUT = 210
    N_LIN_SLAVE_TRANSMIT_ERROR = 211
    N_LIN_SLAVE_REV_ERROR = 212
    N_ETH_GENERIC_ACK = 234
    N_ETH_VEHILCE_INFO_RES = 235
    N_ETH_ACTIVATE_RES = 236
    N_ETH_ALIVE_RES = 237
    N_ETH_NODE_STATE_RES = 238
    N_ETH_DIAG_POWER_MODE_RES = 239
    N_ETH_DIAG_POSITIVE_ACK = 240
    N_ETH_DIAG_NEGATIVE_ACK = 241
    N_ETH_VEHICLE_REQ_ID = 242
    N_ETH_VEHICLE_REQ_EID_ID = 243
    N_ETH_VEHICLE_REQ_VIN_ID = 244
    N_ETH_ACTIVE_REQ = 245
    N_ETH_ALIVE_REQ = 246
    N_ETH_NODE_STATE_REQ = 247
    N_ETH_DIAG_POWER_MODE_REQ = 248
    N_ETH_DIAG_REQ_RES = 249
    N_ETH_RESERVED0 = 250
    N_ETH_RESERVED1 = 251
ISO_TP_RESAULT = c_int32
PSO_TP_RESAULT = ps32

class _lwip_ip_addr_type(CEnum):
    IPADDR_TYPE_V4 = 0
    IPADDR_TYPE_V6 = 6
    IPADDR_TYPE_ANY = 46
lwip_ip_addr_type = c_int32
Pwip_ip_addr_type = ps32

