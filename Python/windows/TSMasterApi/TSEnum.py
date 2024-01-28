from enum import IntEnum, IntFlag


TS_AF_INET = 2
TS_SOCK_STREAM     = 1
TS_SOCK_DGRAM      = 2
TS_SOCK_RAW        = 3

class CHANNEL_INDEX(IntEnum):
    (CHN1, CHN2, CHN3, CHN4, CHN5, CHN6, CHN7, CHN8, CHN9, CHN10, CHN11, CHN12, CHN13, CHN14, CHN15, CHN16, CHN17,
        CHN18, CHN19, CHN20, CHN21, CHN22, CHN23, CHN24, CHN25, CHN26, CHN27, CHN28, CHN29, CHN30, CHN31, CHN32) = (
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 29,
        30,
        31
    )
class READ_TX_RX_DEF(IntEnum):
    '''在接收报文数据时 ONLY_RX_MESSAGES表示只获取接收报文 TX_RX_MESSAGES表示获取发送与接受报文,函数如下：
    tsfifo_receive_can_msgs  接收can报文
    tsfifo_receive_canfd_msgs 接收canfd报文 包括can报文
    tsfifo_receive_lin_msgs   接收lin报文
    tsfifo_receive_flexray_msgs 接受Flexray报文
    '''
    ONLY_RX_MESSAGES = 0
    TX_RX_MESSAGES = 1
class TLIBApplicationChannelType(IntEnum):
    APP_CAN = 0
    APP_LIN = 1
    APP_FlexRay = 2
    APP_Ethernet = 3

class TSignalType(IntEnum):
    stCANSignal = 0
    stLINSignal = 1
    stSystemVar = 2
    stFlexRay = 3
    stEthernet = 4

class TTimeRangeTestMode(IntEnum):
    trmRelativeMode = 0
    trmTriggeredMode = 1
    trmAbsoluteMode = 2

class  TTriggerSignalType(IntEnum):
    tstCANSignal = 0
    tstLINSignal = 1
    tstSystemVar = 2
    tstFlexRay = 3
    tstExpression = 4

class TSignalCheckKind(IntEnum):
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

class TSignalStatisticsKind(IntEnum):
    sskMin = 0
    sskMax = 1
    sskAverage = 2
    sskStdDeviation = 3

class TFlexRayCompuMethod(IntEnum):
    fcmIdentical = 0
    fcmLinear = 1
    fcmScaleLinear = 2
    fcmTextTable = 3
    fcmTABNoIntp = 4
    fcmFormula = 5

class TLIBCANBusStatistics(IntEnum):
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

class TLIBSystemVarType(IntEnum):
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

class TSymbolMappingDirection(IntEnum):
    smdBiDirection = 0
    smdSgnToSysVar = 1
    smdSysVarToSgn = 2

class TReplayPhase(IntEnum):
    rppInit = 0
    rppReplaying = 1
    rppEnded = 2

class TLIBOnlineReplayTimingMode(IntEnum):
    ortImmediately = 0
    ortAsLog = 1
    ortDelayed = 2

class TLIBOnlineReplayStatus(IntEnum):
    orsNotStarted = 0
    orsRunning = 1
    orsPaused = 2
    orsCompleted = 3
    orsTerminated = 4

class TLIBRBSInitValueOptions(IntEnum):
    rivUseDB = 0
    rivUseLast = 1
    rivUse0 = 2

class TSupportedObjType(IntEnum):
    sotCAN = 0
    sotLIN = 1
    sotCANFD = 2
    sotRealtimeComment = 3
    sotSystemVar = 4
    sotFlexRay = 5

class TLIBAutomationModuleRunningState(IntEnum):
    amrsNotRun = 0
    amrsPrepareRun = 1
    amrsRunning = 2
    amrsPaused = 3
    amrsStepping = 4
    amrsFinished = 5

class TLIBAutomationSignalType (IntEnum):
    lastCANSignal = 0
    lastLINSignal = 1
    lastSysVar = 2
    lastLocalVar = 3
    lastConst = 4
    lastFlexRaySignal = 5
    lastImmediateValue = 6
    lastUnknown = 7

class  TLIBMPFuncSource (IntEnum):
    lmfsSystemFunc = 0
    lmfsMPLIB = 1
    lmfsInternal = 2

class TLIBSimVarType(IntEnum):
    lvtInteger = 0
    lvtDouble = 1
    lvtString = 2
    lvtCANMsg = 3
    lvtCANFDMsg = 4
    lvtLINMsg = 5
    lvtUnknown = 6

class TSTIMSignalStatus(IntEnum):
    sssStopped = 0
    sssRunning = 1
    sssPaused = 2

class TLIBCANFDControllerType(IntEnum):
    lfdtCAN = 0
    lfdtISOCAN = 1
    lfdtNonISOCAN = 2

class TLIBCANFDControllerMode(IntEnum):
    lfdmNormal = 0
    lfdmACKOff = 1
    lfdmRestricted = 2
    lfdmInternalLoopback = 3
    lfdmExternalLoopback = 4

class TLIB_TS_Device_Sub_Type(IntEnum):
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

class TLIB_XL_Device_Sub_Type(IntEnum):
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

class TLIBBusToolDeviceType(IntEnum):
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
    BUS_DEV_TYPE_COUNT = 12

class TLINNodeType(IntEnum):
    T_MasterNode = 0
    T_SlaveNode = 1
    T_MonitorNode = 2

class TLINProtocol(IntEnum):
    LIN_PROTOCL_13 = 0
    LIN_PROTOCL_20 = 1
    LIN_PROTOCL_21 = 2
    LIN_PROTOCL_J2602 = 3

