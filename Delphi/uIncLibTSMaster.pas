﻿unit uIncLibTSMaster;

interface

const
  // DLL
  DLL_LIB_TSMASTER = 'TSMaster.dll';
  LOGGER_COUNT            = 7; // all count
  LOGGER_NO_OUTPUT        = 0; // disable output
  LOGGER_ERROR            = 1; // critical error, NOK, red
  LOGGER_WARNING          = 2; // warning, COK, blue
  LOGGER_OK               = 3; // success, OK, green
  LOGGER_HINT             = 4; // hint message, yellow
  LOGGER_INFO             = 5; // text message, window text
  LOGGER_VERBOSE          = 6; // debug message, gray
  LOGGER_TYPES: array [0..LOGGER_COUNT-1] of string = (
    'No output',
    'Error',
    'Warning',
    'OK',
    'Hint',
    'Info',
    'Verbose'
  );

type
  // CAN frame definition = 24 B
  PLIBCAN = ^TLIBCAN;
  TLIBCAN = packed record
    FIdxChn: byte;           // channel index starting from 0        = CAN FD
    FProperties: byte;       // default 0, masked status:            = CAN FD
                             // [7] 0-normal frame, 1-error frame
                             // [6] 0-not logged, 1-already logged
                             // [5-3] tbd
                             // [2] 0-std frame, 1-extended frame
                             // [1] 0-data frame, 1-remote frame
                             // [0] dir: 0-RX, 1-TX
    FDLC: byte;              // dlc from 0 to 8                      = CAN FD
    FReserved: byte;         // reserved to keep alignment           <> CAN FD
    FIdentifier: integer;    // CAN identifier                       = CAN FD
    FTimeUS: int64;          // timestamp in us                      = CAN FD
    FData: array[0..7] of Byte; // 8 data bytes to send                 <> CAN FD
    procedure SetStdId(const AId: Int32; const ADLC: UInt32);
    procedure SetExtId(const AId: Int32; const ADLC: UInt32);
    function GetTX: Boolean;
    function GetData: boolean;
    function GetStd: Boolean;
    function GetErr: Boolean;
    procedure SetTX(const AValue: Boolean);
    procedure SetData(const AValue: Boolean);
    procedure SetStd(const AValue: Boolean);
    procedure SetErr(const AValue: Boolean);
    procedure FromString(const AStr: string);
    function GetLogged: boolean;
    procedure SetLogged(const Value: boolean);
    function ToString: string;
    function GetIsErrorFrame: boolean;
    procedure SetIsErrorFrame(const Value: Boolean);
    // properties
    property IsTX: Boolean read GetTX write SetTX;
    property IsData: boolean read GetData write SetData;
    property IsStd: boolean read GetStd write SetStd;
    property IsErrToken: Boolean read GetErr write SetErr;
    property IsLogged: boolean read GetLogged write SetLogged;
    property IsErrorFrame: Boolean read GetIsErrorFrame write SetIsErrorFrame;
  end;

  // CAN FD frame definition = 80 B
  PLIBCANFD = ^TLIBCANFD;
  TLIBCANFD = packed record
    FIdxChn: byte;           // channel index starting from 0        = CAN
    FProperties: byte;       // default 0, masked status:            = CAN
                             // [7] 0-normal frame, 1-error frame
                             // [6] 0-not logged, 1-already logged
                             // [5-3] tbd
                             // [2] 0-std frame, 1-extended frame
                             // [1] 0-data frame, 1-remote frame
                             // [0] dir: 0-RX, 1-TX
    FDLC: byte;              // dlc from 0 to 15                     = CAN
    FFDProperties: byte;     // [7-3] tbd                            <> CAN
                             // [2] ESI, The E RROR S TATE I NDICATOR (ESI) flag is transmitted dominant by error active nodes, recessive by error passive nodes. ESI does not exist in CAN format frames
                             // [1] BRS, If the bit is transmitted recessive, the bit rate is switched from the standard bit rate of the A RBITRATION P HASE to the preconfigured alternate bit rate of the D ATA P HASE . If it is transmitted dominant, the bit rate is not switched. BRS does not exist in CAN format frames.
                             // [0] EDL: 0-normal CAN frame, 1-FD frame, added 2020-02-12, The E XTENDED D ATA L ENGTH (EDL) bit is recessive. It only exists in CAN FD format frames
    FIdentifier: integer;    // CAN identifier                       = CAN
    FTimeUS: int64;          // timestamp in us                      = CAN
    FData: array [0..63] of Byte; // 64 data bytes to send                <> CAN
    procedure SetStdId(const AId: Int32; const ADLC: UInt32);
    procedure SetExtId(const AId: Int32; const ADLC: UInt32);
    function GetTX: Boolean;
    function GetData: boolean;
    function GetStd: Boolean;
    function GetErr: Boolean;
    procedure SetTX(const AValue: Boolean);
    procedure SetData(const AValue: Boolean);
    procedure SetStd(const AValue: Boolean);
    procedure SetErr(const AValue: Boolean);
    procedure FromString(const AStr: string);
    procedure FromTCAN(const ACAN: PLIBCAN);
    function GetLogged: boolean;
    procedure SetLogged(const Value: boolean);
    function ToString: string;
    function GetIsFD: Boolean;
    procedure SetIsFD(const AIsFD: Boolean);
    function GetIsBRS: boolean;
    procedure SetIsBRS(const AValue: Boolean);
    function GetDataLength: integer;
    function GetIsESI: boolean;
    procedure SetIsESI(const AValue: Boolean);
    function GetIsErrorFrame: boolean;
    procedure SetIsErrorFrame(const Value: Boolean);
    // properties
    property IsTX: Boolean read GetTX write SetTX;
    property IsData: boolean read GetData write SetData;
    property IsStd: boolean read GetStd write SetStd;
    property IsErrToken: Boolean read GetErr write SetErr;
    property IsLogged: boolean read GetLogged write SetLogged;
    property IsEDL: boolean read GetIsFD write setisfd;
    property IsBRS: Boolean read GetIsBRS write SetIsBRS;
    property IsESI: Boolean read GetIsESI write SetIsESI;
    property DataLength: integer read GetDataLength;
    property IsErrorFrame: boolean read GetIsErrorFrame write SetIsErrorFrame;
  end;

  // LIN frame definition = 24 B
  PLIBLIN = ^TLIBLIN;
  TLIBLIN = packed record
    FIdxChn: byte;           // channel index starting from 0
    FErrCode: byte;          //  0: normal
    FProperties: byte;       // default 0, masked status:
                             // [7] tbd
                             // [6] 0-not logged, 1-already logged
                             // [5-4] FHWType //DEV_MASTER,DEV_SLAVE,DEV_LISTENER
                             // [3] 0-not ReceivedSync, 1- ReceivedSync
                             // [2] 0-not received FReceiveBreak, 1-Received Break
                             // [1] 0-not send FReceiveBreak, 1-send Break
                             // [0] dir: 0-RX, 1-TX
    FDLC: byte;              // dlc from 0 to 8
    FIdentifier: byte;       // LIN identifier:0--64
    FChecksum: byte;         // LIN checksum
    FStatus: byte;           // place holder 1
    FTimeUS: int64;          // timestamp in us
    FData: array[0..7] of Byte; // 8 data bytes to send
    function GetTX: boolean;
    procedure SetTX(const AValue: Boolean);
    function GetData: boolean;
    procedure FromString(const AStr: string);
    function ToString: string;
    procedure SetId(const AId: integer; const ADLC: Integer);
    function GetIsErrorFrame: boolean;
    // properties
    property IsTX: Boolean read GetTX write SetTX;
    property IsData: boolean read GetData;
    property IsErrorFrame: boolean read GetIsErrorFrame;
  end;

  TCANQueueEvent_API = procedure(const AData: PlibCAN) of object; stdcall;
  TCANQueueEvent_Win32 = procedure(const AObj: Pointer; const AData: PlibCAN); stdcall;
  TCANFDQueueEvent_Win32 = procedure(const AObj: Pointer; const AData: PlibCANFD); stdcall;
  TLINQueueEvent_Win32 = procedure(const AObj: Pointer; const AData: PlibLIN); stdcall;
  TLIBTSMasterLogger = procedure(const AStr: PAnsiChar; const ALevel: Integer); stdcall;
  TFirmwareUpdateCallback = procedure(const AOpaque: TObject; const AStatus: UInt32; const APercentage100: Single); stdcall;
  TOnIoIPData = procedure(const APointer: Pointer; const ASize: Integer); stdcall;

{$Z4}
  // for c type
  PLIBBusToolDeviceType = ^TLIBBusToolDeviceType;
  TLIBBusToolDeviceType = (
    BUS_UNKNOWN_TYPE           = 0,
    TS_TCP_DEVICE              = 1,
    XL_USB_DEVICE              = 2,
    TS_USB_DEVICE              = 3,
    PEAK_USB_DEVICE            = 4,
    KVASER_USB_DEVICE          = 5,
    ZLG_USB_DEVICE             = 6,
    ICS_USB_DEVICE             = 7,
    TS_TC1005_DEVICE           = 8
  );
  TLIBApplicationChannelType = (
    APP_CAN = 0,
    APP_LIN = 1
  );
  // CAN bus statistics
  TLIBCANBusStatistics = (
    cbsBusLoad = 0, cbsPeakLoad, cbsFpsStdData, cbsAllStdData,
    cbsFpsExtData, cbsAllExtData, cbsFpsStdRemote, cbsAllStdRemote,
    cbsFpsExtRemote, cbsAllExtRemote, cbsFpsErrorFrame, cbsAllErrorFrame
  );
  // System variables
  TLIBSystemVarType = (
    lsvtInt32 = 0, lsvtUInt32, lsvtInt64, lsvtUInt64, lsvtUInt8Array,
    lsvtInt32Array, lsvtInt64Array, lsvtDouble, lsvtDoubleArray, lsvtString
  );
  // Online replay
  TLIBOnlineReplayTimingMode = (ortImmediately = 0, ortAsLog, ortDelayed);
  PLIBOnlineReplayTimingMode = ^TLIBOnlineReplayTimingMode;
  TLIBOnlineReplayStatus = (orsNotStarted = 0, orsRunning, orsPaused, orsCompleted, orsTerminated{in case of error});
  PLIBOnlineReplayStatus = ^TLIBOnlineReplayStatus;
  // RBS
  TLIBRBSInitValueOptions = (rivUseDB = 0, rivUseLast, rivUse0);
  // BLF
  TProgressCallback = procedure(const AProgress100: Double); stdcall;
  PSupportedObjType = ^TSupportedObjType; // TSupportedObjType must be 4 bytes aligned
  TSupportedObjType = (sotCAN = 0, sotLIN = 1, sotCANFD = 2, sotUnknown = $FFFFFFF);
  // TS device type
  TLIBCANFDControllerType = (lfdtCAN = 0, lfdtISOCAN = 1, lfdtNonISOCAN = 2);
  TLIBCANFDControllerMode = (lfdmNormal = 0, lfdmACKOff = 1, lfdmRestricted = 2);
  TLIB_TS_Device_Sub_Type = (
    TS_UNKNOWN_DEVICE   = 0,
    TSCAN_PRO           = 1,  // TSCAN_PRO_4_CHs_SJA1000
    TSCAN_Lite1         = 2,  // TSCAN_LITE_2_CHs_INTL_2515
    TC1001              = 3,  // TSCAN_MINI_1_CHs_INTL
    TL1001              = 4,  // TSLIN_MINI_1_CHs           = 4,
    TC1011              = 5,  // TSCAN_FD_MINI_1_CHs_INTL   = 5,  // TSCAN FD Mini
    TSInterface         = 6,  // TSCAN_LIN_IO_2_CHs_F105    = 6,
    TC1002              = 7,  // TSCAN_LITE_2_CHs_F105      = 7,
    TC1014              = 8,  // TSCAN_LIN_DIO_AIO          = 8,  // TSCANLIN
    TSCANFD2517         = 9   // TSCAN_FD_MINI_1_CHs_2517   = 9
  );
  // Vector XL device type
  TLIB_XL_Device_Sub_Type = (
    XL_NONE                      =    0,
    XL_VIRTUAL                   =    1,  // Tested, 1 ~ 8 Channels
    XL_CANCARDX                  =    2,
    XL_CANAC2PCI                 =    6,
    XL_CANCARDY                  =   12,
    XL_CANCARDXL                 =   15,
    XL_CANCASEXL                 =   21,
    XL_CANCASEXL_LOG_OBSOLETE    =   23,
    XL_CANBOARDXL                =   25,
    XL_CANBOARDXL_PXI            =   27,
    XL_VN2600                    =   29,
    XL_VN3300                    =   37,
    XL_VN3600                    =   39,
    XL_VN7600                    =   41,
    XL_CANCARDXLE                =   43,
    XL_VN8900                    =   45,
    XL_VN8950                    =   47,
    XL_VN2640                    =   53,
    XL_VN1610                    =   55,
    XL_VN1630                    =   57,  // Tested, 2 ~ 4 Channels
    XL_VN1640                    =   59,  // Tested, 4 Channels
    XL_VN8970                    =   61,
    XL_VN1611                    =   63,
    XL_VN5610                    =   65,
    XL_VN5620                    =   66,
    XL_VN7570                    =   67,
    XL_IPCLIENT                  =   69,
    XL_IPSERVER                  =   71,
    XL_VX1121                    =   73,
    XL_VX1131                    =   75,
    XL_VT6204                    =   77,
    XL_VN1630_LOG                =   79,
    XL_VN7610                    =   81,
    XL_VN7572                    =   83,
    XL_VN8972                    =   85,
    XL_VN0601                    =   87,
    XL_VN5640                    =   89,  // Tested, 2 Channels: CAN 17, CAN 18
    XL_VX0312                    =   91,
    XL_VH6501                    =   94,
    XL_VN8800                    =   95,
    XL_IPCL8800                  =   96,
    XL_IPSRV8800                 =   97,
    XL_CSMCAN                    =   98,
    XL_VN5610A                   =   101,
    XL_VN7640                    =   102,
    XL_VX1135                    =   104,
    XL_VN4610                    =   105,
    XL_VT6306                    =   107,
    XL_VT6104A                   =   108,
    XL_VN5430                    =   109,
    XL_VN1530                    =   112,
    XL_VN1531                    =   113
  );
{$Z1}
  // Hardware Info definition
  PLIBHWInfo = ^TLIBHWInfo;
  TLIBHWInfo = packed record
    FDeviceType: TLIBBusToolDeviceType;
    FDeviceIndex: integer;
    FVendorName: array[0..31] of AnsiChar;
    FDeviceName: array[0..31] of AnsiChar;
    FSerialString: array[0..63] of AnsiChar;
  end;
  // Mapping definition
  TLIBTSMapping = packed record
    FAppName: array[0..31] of AnsiChar;
    FAppChannelIndex: integer;
    FAppChannelType: TLIBApplicationChannelType;
    FHWDeviceType: TLIBBusToolDeviceType;
    FHWIndex: integer;
    FHWChannelIndex: integer;
    FHWDeviceSubType: Integer;
    FHWDeviceName: array[0..31] of AnsiChar;
    FMappingDisabled: boolean;
    function ToString: string;
    procedure Init;
    function SetMappingInfo(
      const AAppName: string;
      const AIdxLogicalChannel: integer;
      const AChnType: TLIBApplicationChannelType;
      const AHWDeviceType: TLIBBusToolDeviceType;
      const AIdxHW: integer;
      const AIdxHWChn: integer;
      const AHWDeviceSubType: integer;
      const AHWDeviceName: string
    ): Boolean;
  end;
  PLIBTSMapping = ^TLIBTSMapping;
  // system variable def
  TLIBSystemVarDef = packed record
    FName: array [0..31] of AnsiChar;
    FCategory: array [0..31] of AnsiChar;
    FComment: array [0..31] of ansichar;
    FDataType: TLIBSystemVarType;
    FIsReadOnly: Boolean;
    FValueMin: Double;
    FValueMax: double;
  end;
  PLIBSystemVarDef = ^TLIBSystemVarDef;

  //LIN APIs
  TLINNodeType = ({0:}T_MasterNode,{1:}T_SlaveNode,{;2:}T_MonitorNode);

const
  BUS_TOOL_DEVICE_TYPE_COUNT = 9;
  BUS_TOOL_DEVICE_NAMES: array [0..BUS_TOOL_DEVICE_TYPE_COUNT-1] of string = (
    'Unknown bus tool',
    'TS Virtual Device',
    'Vector',
    'TOSUN',
    'PEAK',
    'Kvaser',
    'ZLG',
    'IntrepidCS',
    'TOSUN TC1005'
  );
  TS_HWTYPE_MAX_CNT = 10;
  TS_HWTYPE_NAMES: array [0..TS_HWTYPE_MAX_CNT-1] of string = (
    'Unknown',
    'TS.CAN Pro',
    'TS.CAN Lite1',
    'TC1001', //"TS.CAN Mini",
    'TL1001', //"TS.LIN Mini",
    'TC1011', //"TS.CAN FD Mini",
    'TSInterface', //"TSCANLIN+Interface"
    'TC1002', //"TS.CAN Lite2",
    'TC1014',  //"TS.CANFD.LIN"
    'TS.CAN FD 2517'
  );
  XL_HWTYPE_MAX_CNT = 114;
  XL_HWTYPE_NAMES: array [0..XL_HWTYPE_MAX_CNT-1] of string = (
    'None',             // 0
    'VIRTUAL',             // 1
    'CANCARDX',             // 2
    'None',             // 3
    'None',             // 4
    'None',             // 5
    'CANAC2PCI',             // 6
    'None',             // 7
    'None',             // 8
    'None',             // 9
    'None',             // 10
    'None',             // 11
    'CANCARDY',             // 12
    'None',             // 13
    'None',             // 14
    'CANCARDXL',             // 15
    'None',             // 16
    'None',             // 17
    'None',             // 18
    'None',             // 19
    'None',             // 20
    'CANCASEXL',             // 21
    'None',             // 22
    'CANCASEXL_LOG_OBSOLETE',             // 23
    'None',             // 24
    'CANBOARDXL',             // 25
    'None',             // 26
    'CANBOARDXL_PXI',             // 27
    'None',             // 28
    'VN2600',             // 29
    'None',             // 30
    'None',             // 31
    'None',             // 32
    'None',             // 33
    'None',             // 34
    'None',             // 35
    'None',             // 36
    'VN3300',             // 37
    'None',             // 38
    'VN3600',             // 39
    'None',             // 40
    'VN7600',             // 41
    'None',             // 42
    'CANCARDXLE',             // 43
    'None',             // 44
    'VN8900',             // 45
    'None',             // 46
    'VN8950',             // 47
    'None',             // 48
    'None',             // 49
    'None',             // 50
    'None',             // 51
    'None',             // 52
    'VN2640',             // 53
    'None',             // 54
    'VN1610',             // 55
    'None',             // 56
    'VN1630',             // 57
    'None',             // 58
    'VN1640',             // 59
    'None',             // 60
    'VN8970',             // 61
    'None',             // 62
    'VN1611',             // 63
    'None',             // 64
    'VN5610',             // 65
    'VN5620',             // 66
    'VN7570',             // 67
    'None',             // 68
    'IPCLIENT',             // 69
    'None',             // 70
    'IPSERVER',             // 71
    'None',             // 72
    'VX1121',             // 73
    'None',             // 74
    'VX1131',             // 75
    'None',             // 76
    'VT6204',             // 77
    'None',             // 78
    'VN1630_LOG',             // 79
    'None',             // 80
    'VN7610',             // 81
    'None',             // 82
    'VN7572',             // 83
    'None',             // 84
    'VN8972',             // 85
    'None',             // 86
    'VN0601',             // 87
    'None',             // 88
    'VN5640',             // 89
    'None',             // 90
    'VX0312',             // 91
    'None',             // 92
    'None',             // 93
    'VH6501',             // 94
    'VN8800',             // 95
    'IPCL8800',             // 96
    'IPSRV8800',             // 97
    'CSMCAN',             // 98
    'None',             // 99
    'None',             // 100
    'VN5610A',             // 101
    'VN7640',             // 102
    'None',             // 103
    'VX1135',             // 104
    'VN4610',             // 105
    'None',             // 106
    'VT6306',             // 107
    'VT6104A',             // 108
    'VN5430',             // 109
    'None',             // 110
    'None',             // 111
    'VN1530',             // 112
    'VN1531'             // 113
  );


{$IFNDEF LIBTSMASTER_IMPL}
const
  // error code
  IDX_ERR_OK                         = 0 ;
  IDX_ERR_IDX_OUT_OF_RANGE           = 1 ;
  IDX_ERR_CONNECT_FAILED             = 2 ;
  IDX_ERR_DEV_NOT_FOUND              = 3 ;
  IDX_ERR_CODE_NOT_VALID             = 4 ;
  IDX_ERR_ALREADY_CONNECTED          = 5 ;
  IDX_ERR_HID_WRITE_FAILED           = 6 ;
  IDX_ERR_HID_READ_FAILED            = 7 ;
  IDX_ERR_HID_TX_BUFF_OVERRUN        = 8 ;
  IDX_ERR_HID_TX_TOO_LARGE           = 9 ;
  IDX_ERR_PACKET_ID_INVALID          = 10;
  IDX_ERR_PACKET_LEN_INVALID         = 11;
  IDX_ERR_INTERNAL_TEST_FAILED       = 12;
  IDX_ERR_RX_PACKET_LOST             = 13;
  IDX_ERR_HID_SETUP_DI               = 14;
  IDX_ERR_HID_CREATE_FILE            = 15;
  IDX_ERR_HID_READ_HANDLE            = 16;
  IDX_ERR_HID_WRITE_HANDLE           = 17;
  IDX_ERR_HID_SET_INPUT_BUFF         = 18;
  IDX_ERR_HID_GET_PREPAESED          = 19;
  IDX_ERR_HID_GET_CAPS               = 20;
  IDX_ERR_HID_WRITE_FILE             = 21;
  IDX_ERR_HID_GET_OVERLAPPED         = 22;
  IDX_ERR_HID_SET_FEATURE            = 23;
  IDX_ERR_HID_GET_FEATURE            = 24;
  IDX_ERR_HID_DEVICE_IO_CTRL         = 25;
  IDX_ERR_HID_SEND_FEATURE_RPT       = 26;
  IDX_ERR_HID_GET_MANU_STR           = 27;
  IDX_ERR_HID_GET_PROD_STR           = 28;
  IDX_ERR_HID_GET_SERIAL_STR         = 29;
  IDX_ERR_HID_GET_INDEXED_STR        = 30;
  IDX_ERR_TX_TIMEDOUT                = 31;
  IDX_ERR_HW_DFU_WRITE_FLASH_FAILED  = 32; // hw write flash failed
  IDX_ERR_HW_DFU_WRITE_WO_ERASE      = 33; // hw write data without erase
  IDX_ERR_HW_DFU_CRC_CHECK_ERROR     = 34; // hw crc check error
  IDX_ERR_HW_DFU_COMMAND_TIMED_OUT   = 35; // hw dfu command timed out
  IDX_ERR_HW_PACKET_ID_INVALID       = 36; // hw packet id invalid
  IDX_ERR_HW_PACKET_LEN_INVALID      = 37; // hw packet len invalid
  IDX_ERR_HW_INTERNAL_TEST_FAILED    = 38; // hw internal test failed
  IDX_ERR_HW_RX_FROM_PC_PACKET_LOST  = 39; // hw rx from pc packet lost
  IDX_ERR_HW_TX_TO_PC_BUFF_OVERRUN   = 40; // hw tx to pc buffer overrun
  IDX_ERR_HW_API_PAEAMETER_INVALID   = 41; // hw api parameter invalid
  IDX_ERR_DFU_FILE_LOAD_FAILED       = 42;
  IDX_ERR_DFU_HEADER_WRITE_FAILED    = 43;
  IDX_ERR_READ_STATUS_TIMEDOUT       = 44;
  IDX_ERR_CALLBACK_ALREADY_EXISTS    = 45;
  IDX_ERR_CALLBACK_NOT_EXISTS        = 46;
  IDX_ERR_FILE_INVALID               = 47; // database file corrupted or not recognized
  IDX_ERR_DB_ID_NOT_FOUND            = 48; // database unique id not found
  IDX_ERR_SW_API_PAEAMETER_INVALID   = 49; // software api parameter invalid
  IDX_ERR_SW_API_GENERIC_TIMEOUT     = 50; // software api generic timed out
  IDX_ERR_SW_API_SET_CONF_FAILED     = 51; // software api set hw conf failed
  IDX_ERR_SW_API_INDEX_OUT_OF_BOUNDS = 52; // index out of bounds
  IDX_ERR_SW_API_WAIT_TIMEOUT        = 53; // rx wait timed out
  IDX_ERR_SW_API_GET_IO_FAILED       = 54; // get io failed
  IDX_ERR_SW_API_SET_IO_FAILED       = 55; // set io failed
  IDX_ERR_SW_API_REPLAY_ON_GOING     = 56; // a replay is already on goning
  IDX_ERR_SW_API_INSTANCE_NOT_EXISTS = 57; // instance not exists
  IDX_ERR_HW_CAN_TRANSMIT_FAILED     = 58; // can transmit frame failed
  IDX_ERR_HW_NO_RESPONSE             = 59; // no response from hardware
  IDX_ERR_SW_CAN_MSG_NOT_FOUND       = 60; // can message not found
  IDX_ERR_SW_CAN_RECV_BUFFER_EMPTY   = 61; // user can recv message buffer empty
  IDX_ERR_SW_CAN_RECV_PARTIAL_READ   = 62; // total read count <> desired read count
  IDX_ERR_SW_API_LINCONFIG_FAILED    = 63;
  IDX_ERR_SW_API_FRAMENUM_OUTOFRANGE = 64;
  IDX_ERR_SW_API_LDFCONFIG_FAILED    = 65;
  IDX_ERR_SW_API_LDFCONFIG_CMDERR    = 66;
  IDX_ERR_SW_ENV_NOT_READY           = 67; // key not retrieved
  IDX_ERR_SECURITY_FAILED            = 68;
  IDX_ERR_XL_ERROR                   = 69; // XL driver failed
  IDX_ERR_SEC_INDEX_OUTOFRANGE           = 70;
  IDX_SEC_ERR_STRINGLENGTH_OUTFOF_RANGE  = 71;
  IDX_SEC_ERR_KEY_IS_NOT_INITIALIZATION  = 72;
  IDX_SEC_ERR_KEY_IS_WRONG               = 73;
  IDX_SEC_ERR_NOT_PERMIT_WRITE           = 74;
  IDX_SEC_ERR_16BYTES_MULTIPLE           = 75;
  IDX_ERR_LIN_CHN_OUTOF_RANGE            = 76;
  IDX_ERR_DLL_NOT_READY                  = 77;
  IDX_ERR_FEATURE_NOT_SUPPORTED          = 78;
  IDX_ERR_COMMON_SERV_ERROR              = 79;
  IDX_ERR_READ_PARA_OVERFLOW             = 80;
  IDX_ERR_INVALID_CHANNEL_MAPPING        = 81;
  IDX_ERR_TSLIB_GENERIC_OPERATION_FAILED = 82;
  IDX_ERR_TSLIB_ITEM_ALREADY_EXISTS      = 83;
  IDX_ERR_TSLIB_ITEM_NOT_FOUND           = 84;
  IDX_ERR_TSLIB_LOGICAL_CHANNEL_INVALID  = 85;
  IDX_ERR_FILE_NOT_EXISTS                = 86;
  IDX_ERR_NO_INIT_ACCESS                 = 87;
  IDX_ERR_CHN_NOT_ACTIVE                 = 88;
  IDX_ERR_CHN_NOT_CREATED                = 89;
  IDX_ERR_APPNAME_LENGTH_OUT_OF_RANGE    = 90;
  IDX_ERR_PROJECT_IS_MODIFIED            = 91;
  IDX_ERR_SIGNAL_NOT_FOUND_IN_DB         = 92;
  IDX_ERR_MESSAGE_NOT_FOUND_IN_DB        = 93;
  IDX_ERR_TSMASTER_IS_NOT_INSTALLED      = 94;
  IDX_ERR_LIB_LOAD_FAILED                = 95;
  IDX_ERR_LIB_FUNCTION_NOT_FOUND         = 96;
  IDX_ERR_LIB_NOT_INITIALIZED            = 97;
  IDX_ERR_PCAN_GENRIC_ERROR              = 98;
  IDX_ERR_KVASER_GENERIC_ERROR           = 99;
  IDX_ERR_ZLG_GENERIC_ERROR              = 100;
  IDX_ERR_ICS_GENERIC_ERROR              = 101;
  IDX_ERR_TC1005_GENERIC_ERROR           = 102;
  IDX_ERR_SYSTEM_VAR_NOT_FOUND           = 103;
  IDX_ERR_INCORRECT_SYSTEM_VAR_TYPE      = 104;
  IDX_ERR_CYCLIC_MSG_NOT_EXIST           = 105;
  IDX_ERR_BAUD_NOT_AVAIL                 = 106;
  IDX_ERR_DEV_NOT_SUPPORT_SYNC_SEND      = 107;
  IDX_ERR_MP_WAIT_TIME_NOT_SATISFIED     = 108;
  IDX_ERR_CANNOT_OPERATE_WHILE_CONNECTED = 109;
  IDX_ERR_CREATE_FILE_FAILED             = 110;
  IDX_ERR_PYTHON_EXECUTE_FAILED          = 111;
  IDX_ERR_SIGNAL_MULTIPLEXED_NOT_ACTIVE  = 112;
  IDX_ERR_GET_HANDLE_BY_CHANNEL_FAILED   = 113;
  IDX_ERR_CANNOT_OPERATE_WHILE_APP_CONN  = 114;
  IDX_ERR_FILE_LOAD_FAILED               = 115;
  IDX_ERR_READ_LINDATA_FAILED            = 116;
  IDX_ERR_FIFO_NOT_ENABLED               = 117;
  IDX_ERR_INVALID_HANDLE                 = 118;
  IDX_ERR_READ_FILE_ERROR                = 119;
  IDX_ERR_READ_TO_EOF                    = 120;
  ERR_CODE_COUNT                         = 121;

// Note: Should also update C API!!!

// library initialization and finalization
function set_libtsmaster_location(const AFilePath: PAnsiChar): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function get_libtsmaster_location(const AFilePath: PPAnsiChar): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function initialize_lib_tsmaster(const AAppName: PAnsiChar): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
procedure finalize_lib_tsmaster; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_set_logger(const ALogger: TLIBTSMasterLogger): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}

// application management
procedure tsapp_log(const AStr: pansichar; const ALevel: Integer); stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_set_current_application(const AAppName: PAnsiChar): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_get_current_application(const AAppName: pPAnsiChar): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_del_application(const AAppName: PAnsiChar): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_add_application(const AAppName: PAnsiChar): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_get_application_list(const AAppNameList: PPAnsiChar): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_set_can_channel_count(const ACount: Integer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_set_lin_channel_count(const ACount: Integer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_get_can_channel_count(out ACount: Integer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_get_lin_channel_count(out ACount: Integer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_set_mapping(const AMapping: PLIBTSMapping): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_set_mapping_verbose(const AAppName:PAnsiChar;
                                   const AAppChannelType:TLIBApplicationChannelType;
                                   const AAppChannel:Integer;  //APP_CHANNEL
                                   const AHardwareName:PAnsiChar;
                                   const AHardwareType:TLIBBusToolDeviceType;
                                   const AHardwareSubType:Integer;
                                   const AHardwareIndex:Integer;
                                   const AHardwareChannel:Integer;  //HARDWARE_CHANNEL
                                   const AEnableMapping:Boolean): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_get_mapping(const AMapping: PLIBTSMapping): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_del_mapping(const AMapping: PLIBTSMapping): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_del_mapping_verbose(const AAppName:PAnsiChar;
                                   const AAppChannelType:TLIBApplicationChannelType;
                                   const AAppChannel:Integer):Integer;stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_connect: integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_disconnect(): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_set_turbo_mode(const AEnable: Boolean): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_get_turbo_mode(out AEnable: Boolean): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_get_error_description(const ACode: Integer; ADesc: PPAnsiChar): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_show_channel_mapping_window: integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_show_hardware_configuration_window: integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_show_tsmaster_window(const AWindowName: PAnsiChar; const AWaitClose: Boolean): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_get_timestamp(ATimeUs: PInt64): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_execute_python_string(const AString: PAnsiChar; const AArguments: pansichar; const ASync: boolean; const AIsX64: Boolean; AResultLog: PPAnsiChar): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_execute_python_script(const AFilePath: PAnsiChar; const AArguments: pansichar; const ASync: boolean; const AIsX64: Boolean; AResultLog: PPAnsiChar): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_set_analysis_time_range(const ATimeStartUs: int64; const ATimeEndUs: int64): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_get_tsmaster_version(const AYear: pinteger; const AMonth: pinteger; const ADay: pinteger; const ABuildNumber: pinteger): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
// hardware settings
function tsapp_enumerate_hw_devices(out ACount: Integer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_get_hw_info_by_index(const AIndex: Integer; const AHWInfo: PLIBHWInfo): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_get_hw_info_by_index_verbose(const AIndex: Integer;
                                      ADeviceType: PLIBBusToolDeviceType;
                                      AVendorNameBuffer: PAnsiChar; //array[0..31] of AnsiChar;
                                      AVendorNameBufferSize:Integer;
                                      ADeviceNameBuffer: PAnsiChar; //array[0..31] of AnsiChar;
                                      ADeviceNameBufferSize:Integer;
                                      ASerialStringBuffer: PAnsiChar; //array[0..63] of AnsiChar
                                      ASerialStringBufferSize: Integer
                                      ): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_set_vendor_detect_preferences(const AScanTOSUN, AScanVector, AScanPeak, AScanKvaser, AScanZLG, ADetectIntrepidcs: Boolean): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_get_vendor_detect_preferences(out AScanTOSUN, AScanVector, AScanPeak, AScanKvaser, AScanZLG, ADetectIntrepidcs: Boolean): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_configure_baudrate_lin(const AIdxChn: Integer;const ABaudrateKbps: Single): Integer; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}{Bps:such as 19200 bps}
function tsapp_configure_baudrate_can(const AIdxChn: integer; const ABaudrateKbps: Single; const AListenOnly: boolean; const AInstallTermResistor120Ohm: Boolean): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_configure_baudrate_canfd(const AIdxChn: integer; const AArbRateKbps, ADataRateKbps: Single; const AControllerType: TLIBCANFDControllerType; const AControllerMode: TLIBCANFDControllerMode; const AInstallTermResistor120Ohm: Boolean): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
// communication async functions
function tsapp_transmit_can_async(const ACAN: PLIBCAN): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_transmit_canfd_async(const ACANFD: PLIBCANFD): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_transmit_lin_async(const ALIN: PLIBLIN): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_transmit_fastlin_async(const ALIN: PLIBLIN): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
// communication sync functions
function tsapp_transmit_can_sync(const ACAN: PLIBCAN; const ATimeoutMS: Integer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_transmit_canfd_sync(const ACANfd: PLIBCANfd; const ATimeoutMS: Integer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_transmit_lin_sync(const ALIN: PLIBLIN; const ATimeoutMS: Integer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_upgrade_firmware(const AChn: byte; const AFirmwareFile: string; const AOpaque: tobject; const ACallback: TFirmwareUpdateCallback): integer; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
// communication receive functions
procedure tsfifo_enable_receive_fifo; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
procedure tsfifo_disable_receive_fifo; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
procedure tsfifo_enable_receive_error_frames; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
procedure tsfifo_disable_receive_error_frames; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsfifo_receive_can_msgs(const ACANBuffers: PLIBCAN; const ACANBufferSize: PInteger; const AIdxChn: integer; const AIncludeTx: boolean): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsfifo_receive_canfd_msgs(const ACANFDBuffers: PLIBCANFD; const ACANFDBufferSize: PInteger; const AIdxChn: integer; const AIncludeTx: boolean): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsfifo_receive_lin_msgs(const ALINBuffers: PLIBLIN; const ALINBufferSize: PInteger; const AIdxChn: integer; const AIncludeTx: boolean): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsfifo_receive_fastlin_msgs(const AFastLINBuffers: PLIBLIN; const AFastLINBufferSize: PInteger; const AIdxChn: integer; const AIncludeTx: boolean): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsfifo_clear_can_receive_buffers(const AIdxChn: integer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsfifo_clear_canfd_receive_buffers(const AIdxChn: integer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsfifo_clear_lin_receive_buffers(const AIdxChn: integer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsfifo_clear_fastlin_receive_buffers(const AIdxChn: integer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsfifo_read_can_buffer_frame_count(const AIdxChn: integer; out ACount: Integer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsfifo_read_can_tx_buffer_frame_count(const AIdxChn: integer; out ACount: Integer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsfifo_read_can_rx_buffer_frame_count(const AIdxChn: integer; out ACount: Integer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsfifo_read_canfd_buffer_frame_count(const AIdxChn: integer; out ACount: Integer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsfifo_read_canfd_tx_buffer_frame_count(const AIdxChn: integer; out ACount: Integer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsfifo_read_canfd_rx_buffer_frame_count(const AIdxChn: integer; out ACount: Integer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsfifo_read_lin_buffer_frame_count(const AIdxChn: integer; out ACount: Integer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsfifo_read_lin_tx_buffer_frame_count(const AIdxChn: integer; out ACount: Integer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsfifo_read_lin_rx_buffer_frame_count(const AIdxChn: integer; out ACount: Integer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsfifo_read_fastlin_buffer_frame_count(const AIdxChn: integer; out ACount: Integer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsfifo_read_fastlin_tx_buffer_frame_count(const AIdxChn: integer; out ACount: Integer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsfifo_read_fastlin_rx_buffer_frame_count(const AIdxChn: integer; out ACount: Integer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
// periodic
function tsapp_add_cyclic_msg_can(const ACAN: PLIBCAN; const APeriodMS: Single): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_update_cyclic_msg_can(const ACAN: PLIBCAN): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_add_cyclic_msg_canfd(const ACANFD: PLIBCANFD; const APeriodMS: Single): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_delete_cyclic_msg_can(const ACAN: PLIBCAN): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_delete_cyclic_msg_canfd(const ACANFD: PLIBCANFD): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_delete_cyclic_msgs: Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
// bus statistics
function tsapp_enable_bus_statistics(const AEnable: Boolean): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_clear_bus_statistics(): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_get_bus_statistics(const ABusType: TLIBApplicationChannelType; const AIdxChn: Integer; const AIdxStat: TLIBCANBusStatistics; out AStat: Double): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_get_fps_can(const AIdxChn: Integer; const AIdentifier: Integer; out AFPS: Integer): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_get_fps_canfd(const AIdxChn: Integer; const AIdentifier: Integer; out AFPS: Integer): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_get_fps_lin(const AIdxChn: Integer; const AIdentifier: Integer; out AFPS: Integer): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
// bus callback handler
function tsapp_register_event_can(const AObj: pointer; const AEvent: TCANQueueEvent_Win32): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_unregister_event_can(const AObj: pointer; const AEvent: TCANQueueEvent_Win32): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_register_event_canfd(const AObj: pointer; const AEvent: TCANfdQueueEvent_Win32): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_unregister_event_canfd(const AObj: pointer; const AEvent: TCANfdQueueEvent_Win32): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_register_event_lin(const AObj: pointer; const AEvent: TliNQueueEvent_Win32): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_unregister_event_lin(const AObj: pointer; const AEvent: TliNQueueEvent_Win32): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_unregister_events_can(const AObj: pointer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_unregister_events_lin(const AObj: pointer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_unregister_events_canfd(const AObj: pointer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_unregister_events_all(const AObj: pointer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
// bus pre-tx callback handler
function tsapp_register_pretx_event_can(const AObj: pointer; const AEvent: TCANQueueEvent_Win32): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_unregister_pretx_event_can(const AObj: pointer; const AEvent: TCANQueueEvent_Win32): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_register_pretx_event_canfd(const AObj: pointer; const AEvent: TCANfdQueueEvent_Win32): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_unregister_pretx_event_canfd(const AObj: pointer; const AEvent: TCANfdQueueEvent_Win32): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_register_pretx_event_lin(const AObj: pointer; const AEvent: TliNQueueEvent_Win32): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_unregister_pretx_event_lin(const AObj: pointer; const AEvent: TliNQueueEvent_Win32): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_unregister_pretx_events_can(const AObj: pointer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_unregister_pretx_events_lin(const AObj: pointer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_unregister_pretx_events_canfd(const AObj: pointer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_unregister_pretx_events_all(const AObj: pointer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
// logger
function tsapp_start_logging(const AFileName: PAnsiChar): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_stop_logging(): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
// excel
function tsapp_excel_load(const AFileName: PAnsiChar; const AObj: PPointer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_excel_get_sheet_count(const AObj: Pointer; out ACount: integer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_excel_set_sheet_count(const AObj: Pointer; const ACount: integer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_excel_get_sheet_name(const AObj: Pointer; const AIdxSheet: Integer; const AName: PPAnsiChar): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_excel_set_sheet_name(const AObj: Pointer; const AIdxSheet: Integer; const AName: PAnsiChar): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_excel_get_cell_count(const AObj: Pointer; const AIdxSheet: Integer; out ARowCount: integer; out AColCount: Integer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_excel_get_cell_value(const AObj: Pointer; const AIdxSheet: Integer; const AIdxRow: integer; const AIdxCol: Integer; const AValue: PPAnsiChar): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_excel_set_cell_count(const AObj: Pointer; const AIdxSheet: integer; const ARowCount: integer; const AColCount: integer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_excel_set_cell_value(const AObj: Pointer; const AIdxSheet: Integer; const AIdxRow: integer; const AIdxCol: Integer; const AValue: PAnsiChar): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_excel_unload(const AObj: Pointer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
// system variables
function tsapp_system_vars_reload_settings(): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_get_system_var_count(AinternalCount: pinteger; AUserCount: pinteger): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_get_system_var_def_by_index(const AIsUser: boolean; const AIndex: integer; const AVarDef: PLIBSystemVarDef): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_find_system_var_def_by_name(const AIsUser: boolean; const ACompleteName: PAnsiChar; const AVarDef: PLIBSystemVarDef): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_get_system_var_double(const ACompleteName: PAnsiChar; AValue: Pdouble): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_get_system_var_int32(const ACompleteName: PAnsiChar; AValue: pinteger): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_get_system_var_uint32(const ACompleteName: PAnsiChar; AValue: pcardinal): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_get_system_var_int64(const ACompleteName: PAnsiChar; AValue: pint64): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_get_system_var_uint64(const ACompleteName: PAnsiChar; AValue: puint64): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_get_system_var_uint8_array(const ACompleteName: PAnsiChar; const ACapacity: integer; AVarCount: pinteger; AValue: pbyte): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_get_system_var_int32_array(const ACompleteName: PAnsiChar; const ACapacity: integer; AVarCount: pinteger; AValue: pinteger): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_get_system_var_int64_array(const ACompleteName: PAnsiChar; const ACapacity: integer; AVarCount: pinteger; AValue: pint64): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_get_system_var_double_array(const ACompleteName: PAnsiChar; const ACapacity: integer; AVarCount: pinteger; AValue: Pdouble): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_get_system_var_string(const ACompleteName: PAnsiChar; const ACapacity: integer; AValue: PAnsiChar): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_set_system_var_double(const ACompleteName: PAnsiChar; const AValue: double): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_set_system_var_int32(const ACompleteName: PAnsiChar; const AValue: integer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_set_system_var_uint32(const ACompleteName: PAnsiChar; const AValue: cardinal): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_set_system_var_int64(const ACompleteName: PAnsiChar; const AValue: int64): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_set_system_var_uint64(const ACompleteName: PAnsiChar; const AValue: uint64): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_set_system_var_uint8_array(const ACompleteName: PAnsiChar; const ACapacity: integer; AValue: pbyte): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_set_system_var_int32_array(const ACompleteName: PAnsiChar; const ACapacity: integer; AValue: pinteger): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_set_system_var_int64_array(const ACompleteName: PAnsiChar; const ACapacity: integer; AValue: pint64): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_set_system_var_double_array(const ACompleteName: PAnsiChar; const ACapacity: integer; AValue: Pdouble): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_set_system_var_string(const ACompleteName: PAnsiChar; AValue: PAnsiChar): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsapp_log_system_var(const ACompleteName: PAnsiChar): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
// database parser
function tsdb_reload_settings(out ALoadedDBCount: Integer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsdb_load_can_db(const ADBC: PAnsiChar; const ASupportedChannelsBased0: PAnsiChar; out AId: Cardinal): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsdb_unload_can_db(const AId: Cardinal): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsdb_unload_can_dbs(): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsdb_get_can_db_count(out ACount: Integer): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsdb_get_can_db_id(const AIndex: integer; out AId: Cardinal): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsdb_get_can_db_info(const ADatabaseId: Cardinal; const AType: integer; const AIndex: integer; const ASubIndex: Integer; AValue: PPAnsiChar): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
// database signal
function tsdb_set_signal_value_can(const ACAN: PLIBCAN; const AMsgName: PAnsiChar; const ASgnName: PAnsiChar; const AValue: Double): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsdb_get_signal_value_can(const ACAN: PLIBCAN; const AMsgName: PAnsiChar; const ASgnName: PAnsiChar; out AValue: Double): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsdb_set_signal_value_canfd(const ACANfd: PLIBCANfd; const AMsgName: PAnsiChar; const ASgnName: PAnsiChar; const AValue: Double): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsdb_get_signal_value_canfd(const ACANfd: PLIBCANfd; const AMsgName: PAnsiChar; const ASgnName: PAnsiChar; out AValue: Double): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
// online replay
function tslog_reload_settings(out ALoadedEngineCount: Integer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tslog_add_online_replay_config(const AFileName: PAnsiChar; out AIndex: Integer): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tslog_set_online_replay_config(const AIndex: Integer; const AName: PAnsiChar; const AFileName: PAnsiChar; const AAutoStart: Boolean; const AIsRepetitiveMode: boolean; const AStartTimingMode: TLIBOnlineReplayTimingMode; const AStartDelayTimeMs: integer; const ASendTx: Boolean; const ASendRx: boolean; const AMappings: PAnsiChar): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tslog_get_online_replay_count(out ACount: Integer): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tslog_get_online_replay_config(const AIndex: Integer; AName: PPAnsiChar; AFileName: PPAnsiChar; out AAutoStart: Boolean; out AIsRepetitiveMode: boolean; out AStartTimingMode: TLIBOnlineReplayTimingMode; out AStartDelayTimeMs: integer; out ASendTx: Boolean; out ASendRx: boolean; AMappings: PPAnsiChar): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tslog_del_online_replay_config(const AIndex: Integer): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tslog_del_online_replay_configs(): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tslog_start_online_replay(const AIndex: Integer): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tslog_start_online_replays(): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tslog_pause_online_replay(const AIndex: Integer): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tslog_pause_online_replays(): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tslog_stop_online_replay(const AIndex: Integer): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tslog_stop_online_replays(): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tslog_get_online_replay_status(const AIndex: Integer; out AStatus: TLIBOnlineReplayStatus; out AProgressPercent100:Single): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
// blf
function tslog_blf_write_start(const AFileName: PAnsiChar; AHandle: pinteger): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tslog_blf_write_can(const AHandle: integer; const ACAN: PlibCAN): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tslog_blf_write_can_fd(const AHandle: integer; const ACANFD: PlibCANFD): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tslog_blf_write_lin(const AHandle: integer; const ALIN: PlibLIN): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tslog_blf_write_end(const AHandle: integer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tslog_blf_read_start(const AFileName: PAnsiChar; AHandle: pinteger; AObjCount: pinteger): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tslog_blf_read_status(const AHandle: integer; AObjReadCount: pinteger): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tslog_blf_read_object(const AHandle: integer; AProgressedCnt: pinteger; AType: PSupportedObjType; ACAN: PlibCAN; ALIN: PlibLIN; ACANFD: PlibCANFD): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tslog_blf_read_end(const AHandle: integer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tslog_blf_seek_object_time(const AHandle: integer; const AProg100: Double; var ATime: int64; var AProgressedCnt: integer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tslog_blf_to_asc(const ABLFFileName: PAnsiChar; const AASCFileName: pansichar; const AProgressCallback: TProgressCallback): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tslog_asc_to_blf(const AASCFileName: PAnsiChar; const ABLFFileName: pansichar; const AProgressCallback: TProgressCallback): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
// CAN RBS
function tscom_can_rbs_reload_settings(): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tscom_can_rbs_start(): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tscom_can_rbs_stop(): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tscom_can_rbs_is_running(out AIsRunning: Boolean): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tscom_can_rbs_configure(const AAutoStart: boolean; const AAutoSendOnModification: boolean; const AActivateNodeSimulation: boolean; const AInitValueOptions: TLIBRBSInitValueOptions): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tscom_can_rbs_activate_all_networks(const AEnable: boolean; const AIncludingChildren: Boolean): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tscom_can_rbs_activate_network_by_name(const AEnable: boolean; const ANetworkName: PAnsiChar; const AIncludingChildren: Boolean): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tscom_can_rbs_activate_node_by_name(const AEnable: boolean; const ANetworkName: PAnsiChar; const ANodeName: pansichar; const AIncludingChildren: Boolean): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tscom_can_rbs_activate_message_by_name(const AEnable: boolean; const ANetworkName: PAnsiChar; const ANodeName: pansichar; const AMsgName: PAnsiChar): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tscom_can_rbs_get_signal_value_by_element(const AIdxChn: Integer; const ANetworkName: PAnsiChar; const ANodeName: pansichar; const AMsgName: PAnsiChar; const ASignalName: PAnsiChar; out AValue: Double): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tscom_can_rbs_get_signal_value_by_address(const ASymbolAddress: PAnsiChar; out AValue: Double): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tscom_can_rbs_set_signal_value_by_element(const AIdxChn: Integer; const ANetworkName: PAnsiChar; const ANodeName: pansichar; const AMsgName: PAnsiChar; const ASignalName: PAnsiChar; const AValue: Double): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tscom_can_rbs_set_signal_value_by_address(const ASymbolAddress: PAnsiChar; const AValue: Double): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}

// LIN apis
//function tslin_apply_download_new_ldf(const AChnIdx: Integer): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
//function tslin_download_frames(const AChnIdx: Integer; const ACnt: Integer; const ALINFrames: PConfig_LINFrameStruct): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
//function tslin_download_schedule_tables(const AChnIdx: Integer; const ACnt: Integer; const ALINSchedule: Plin_schedule_struct): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
//function tslin_download_runtime_schedule_table(const AChnIdx: Integer; const ALINSchedule: Plin_schedule_struct): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tslin_enable_runtime_schedule_table(const AChnIdx: Integer): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tslin_set_schedule_table(const AChnIdx: Integer; const ASchIndex: Integer): Integer;stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tslin_stop_lin_channel(const AChnIdx: Integer): Integer;stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tslin_start_lin_channel(const AChnIdx: Integer): Integer;stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tslin_set_node_funtiontype(const AChnIdx: Integer; const AFunctionType: TLINNodeType): Integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
//LIN_Diag_Tp_Layer
function tslin_diag_tp_master_request(const AChnIdx: Integer; const ANAD:Byte; const AData: PByte; const ADataNum: Integer; const ATimeoutMs: Integer): Integer;stdcall;{$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tslin_diag_tp_master_request_intervalms(const AChnIdx: Integer; const AData: Byte): Integer;stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tslin_diag_tp_reset(const AChnIdx: Integer): Integer;stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tslin_diag_tp_slave_response_intervalms(const AChnIdx: Integer; const AData: Byte): Integer;stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
//LIN_Diag_Service_Layer
//ServiceID:0x22
function tslin_diag_sp_read_data_by_identifier(const AChnIdx: Integer;const ANAD:Byte;const AId:uint16;
                             const AResNAD:PByte;const AResData:PByte;const AResDataNum:PNativeInt;
                             const ATimeoutMS:UInt32):Integer;stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}

//ServiceID:0x2E
function tslin_diag_sp_write_data_by_identifier(const AChnIdx: Integer;
                             const AReqNAD:Byte;
                             const AID:UInt16;
                             const AReqData:PByte;
                             const AReqDataNum:NativeInt;
                             const AResNAD:PByte;
                             const AResData:PByte;
                             const AResDataNum:PNativeInt;
                             const ATimeoutMS:UInt32):NativeInt;stdcall;{$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
//Session Control: 0x10
function tslin_diag_sp_session_control(const AChnIdx: Integer;
                                          const ANAD:Byte;
                                          const ANewSession:Byte;
                                          const ATimeoutMS:UInt32):NativeInt;stdcall;{$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
//Service ID 0x19
function tslin_diag_sp_fault_memory_read(const AChnIdx: Integer;
                                            const ANAD:Byte;
                                            const ATimeoutMS:UInt32):NativeInt;stdcall;{$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
//ServiceID 0x14
function tslin_diag_sp_fault_memory_clear(const AChnIdx: Integer;
                                             const ANAD:Byte;
                                             const ATimeoutMS:UInt32):NativeInt;stdcall;{$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
// mini program library
function tsmp_reload_settings(): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsmp_load(const AMPFileName: PAnsiChar; const ARunAfterLoad: boolean): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsmp_unload(const AMPFileName: PAnsiChar): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsmp_unload_all(): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsmp_run(const AMPFileName: PAnsiChar): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsmp_is_running(const AMPFileName: PAnsiChar; out AIsRunning: boolean): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsmp_stop(const AMPFileName: pansichar): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsmp_run_all(): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsmp_stop_all(): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsmp_call_function(const AGroupName: pansichar; const AFuncName: pansichar; const AInParameters: pansichar; const AOutParameters: PPAnsiChar): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsmp_get_function_address(const AGroupName: PAnsiChar; const AFuncName: PAnsiChar; out AAddress: Pointer): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsmp_get_function_prototype(const AGroupName: pansichar; const AFuncName: pansichar; const APrototype: ppansichar): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsmp_get_mp_function_list(const AGroupName: pansichar; const AList: ppansichar): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}
function tsmp_get_mp_list(const AList: ppansichar): integer; stdcall; {$IFNDEF LIBTSMASTER_IMPL} external DLL_LIB_TSMASTER; {$ENDIF}

{$ENDIF}

implementation

uses
  Winapi.Windows,
  System.Types,
  System.Math,
  System.AnsiStrings,
  System.SysUtils,
  System.StrUtils;

const
  // CAN message properties
  MASK_CANProp_DIR_TX  = $01;
  MASK_CANProp_REMOTE  = $02;
  MASK_CANProp_EXTEND  = $04;
  MASK_CANProp_ERROR   = $80;
  MASK_CANProp_LOGGED  = $60;
  // CAN FD message properties
  MASK_CANFDProp_IS_FD = $01;
  MASK_CANFDProp_IS_EDL = MASK_CANFDProp_IS_FD;
  MASK_CANFDProp_IS_BRS = $02;
  MASK_CANFDProp_IS_ESI = $04;
  // LIN message properties
  MASK_LINProp_DIR_TX          = $01;
  MASK_LINProp_SEND_BREAK      = $02;
  MASK_LINProp_RECEIVED_BREAK  = $04;
  MASK_LINProp_SEND_SYNC       = $80;
  MASK_LINProp_RECEIVED_SYNC   = $10;
  // CAN error frame
  CAN_ID_ERROR: Integer   = integer($FFFFFFFF);
  // CAN FD DLC Data Count mapping
  DLC_DATA_BYTE_CNT: array [0..15] of Byte = (
    0,  1,  2,  3,  4,  5,  6, 7,
    8,  12, 16, 20, 24, 32, 48, 64
  );

function GetFDDataLength(const ADLC: Integer): integer;
begin
  result := min(ADLC, 15);
  result := Max(result, 0);
  Result := DLC_DATA_BYTE_CNT[result];

end;

procedure TLIBCAN.FromString(const AStr: string);
var
  ss: TStringDynArray;
begin
  // 100.123456 TX 1 $120 Data 8 12 23 45 56 67 78 89 12
  // 0          1  2 3    4    5 6  7  8  9  10 11 12 13
  ss := SplitString(AStr, ' ');
  if Length(ss) = 14 then begin
    FTimeUS := round(strtofloatdef(ss[0], 0) * 1000000);
    IsTX := ss[1].CompareTo('Tx') = 0;
    FIdxChn := StrToIntDef(ss[2], 1);
    FIdentifier := StrToIntDef(ss[3], 0);
    if ss[4].Equals('D') then begin
      IsData := true;
    end else begin
      IsData := false;
    end;
    FDLC := StrToIntDef(ss[5], 8);
    FDATA[0] := StrToIntDef(ss[6], 0);
    FDATA[1] := StrToIntDef(ss[7], 0);
    FDATA[2] := StrToIntDef(ss[8], 0);
    FDATA[3] := StrToIntDef(ss[9], 0);
    FDATA[4] := StrToIntDef(ss[10], 0);
    FDATA[5] := StrToIntDef(ss[11], 0);
    FDATA[6] := StrToIntDef(ss[12], 0);
    FDATA[7] := StrToIntDef(ss[13], 0);
  end;

end;

function TLIBCAN.GetData: boolean;
begin
  Result := (FProperties and MASK_CANProp_REMOTE) = 0;

end;

function TLIBCAN.GetErr: Boolean;
begin
  Result := (FProperties and MASK_CANProp_ERROR) <> 0;

end;

function TLIBCAN.GetIsErrorFrame: boolean;
begin
  Result := fidentifier = (CAN_ID_ERROR);

end;

function TLIBCAN.GetLogged: boolean;
begin
  Result := (FProperties and MASK_CANProp_LOGGED) <> 0;

end;

function TLIBCAN.GetStd: Boolean;
begin
  Result := (FProperties and MASK_CANProp_EXTEND) = 0;

end;

function TLIBCAN.GetTX: boolean;
begin
  Result := (FProperties and MASK_CANProp_DIR_TX) <> 0;

end;

procedure TLIBCAN.SetData(const AValue: Boolean);
begin
  if avalue then begin
    FProperties := FProperties and (not MASK_CANProp_REMOTE);
  end else begin
    FProperties := FProperties or MASK_CANProp_REMOTE;
  end;

end;

procedure TLIBCAN.SetErr(const AValue: Boolean);
begin
  if not AValue then begin
    FProperties := FProperties and (not MASK_CANProp_ERROR);
  end else begin
    FProperties := FProperties or MASK_CANProp_ERROR;
  end;

end;

procedure TLIBCAN.SetExtId(const AId: Int32; const ADLC: UInt32);
begin
  FIdxChn := 0;
  FIdentifier := AId;
  FDLC := ADLC;
  FProperties := 0;
  SetTX(True);
  SetStd(False);
  SetData(True);
  PUInt64(@FData[0])^ := 0;
  FReserved := 0;
  FTimeUS := 0;

end;

procedure TLIBCAN.SetIsErrorFrame(const Value: Boolean);
begin
  IsErrToken := true;
  fidentifier := (CAN_ID_ERROR);

end;

procedure TLIBCAN.SetLogged(const Value: boolean);
begin
  if not Value then begin
    FProperties := FProperties and (not MASK_CANProp_LOGGED);
  end else begin
    FProperties := FProperties or MASK_CANProp_LOGGED;
  end;

end;

procedure TLIBCAN.SetStd(const AValue: Boolean);
begin
  if avalue then begin
    FProperties := FProperties and (not MASK_CANProp_EXTEND);
  end else begin
    FProperties := FProperties or MASK_CANProp_EXTEND;
  end;

end;

procedure TLIBCAN.SetStdId(const AId: Int32; const ADLC: UInt32);
begin
  FIdxChn := 0;
  FIdentifier := AId;
  FDLC := ADLC;
  FProperties := 0;
  SetTX(True);
  SetStd(True);
  SetData(True);
  PUInt64(@FData[0])^ := 0;
  FReserved := 0;
  FTimeUS := 0;

end;

procedure TLIBCAN.SetTX(const AValue: Boolean);
begin
  if avalue then begin
    FProperties := FProperties or MASK_CANProp_DIR_TX;
  end else begin
    FProperties := FProperties and (not MASK_CANProp_DIR_TX);
  end;

end;

function TLIBCAN.ToString: string;
var
  sDatas: string;
  i: Integer;
begin
  Result := FloatToStr(FTimeUS / 1000000.0);
  if istx then begin
    Result := Result + ' Tx ' + fidxchn.ToString;
  end else begin
    Result := Result + ' Rx ' + fidxchn.ToString;
  end;
  if fidentifier = Byte(-1) then begin
    // error frame
    Result := Result + ' E';
  end else begin
    // normal frame
    if IsStd then begin
      Result := Result + ' $' + IntToHex(fidentifier, 3);
    end else begin
      Result := Result + ' $' + IntToHex(fidentifier, 8);
    end;
    if IsData then begin
      Result := result + ' D ';
    end else begin
      Result := result + ' R ';
    end;
    if FDLC > 8 then begin
      FDLC := 8;
    end;
    Result := Result + fdlc.ToString + ' ';
    sDatas := '';
    for i:=0 to 7 do begin // bug fix: 2020-01-04, data should be 8
      sDatas := sDatas + IntToHex(fdata[i], 2) + ' ';
    end;
    Result := result + sDatas;
  end;

end;

function TLIBLIN.GetTX: boolean;
begin
    Result := (FProperties and MASK_LINProp_DIR_TX) <> 0;

end;

procedure TLIBLIN.SetId(const AId, ADLC: Integer);
begin
  FIdxChn := 0;
  FErrCode := 0;
  FProperties := 0;
  FDLC := ADLC;
  FIdentifier := AId;
  PInt64(@fdata[0])^ := 0;
  FChecksum := 0;
  FStatus := 0;
  FTimeUS := 0;

end;

procedure TLIBLIN.SetTX(const AValue: Boolean);
begin
    if avalue then begin
      FProperties := FProperties or MASK_LINProp_DIR_TX;
    end else begin
      FProperties := FProperties and (not MASK_LINProp_DIR_TX);
    end;

end;

function TLIBLIN.GetData: boolean;
begin
   Result := True;

end;

function TLIBLIN.GetIsErrorFrame: boolean;
begin
  Result := FIdentifier = $FF;

end;

procedure TLIBLIN.FromString(const AStr: string);
var
  ss: TStringDynArray;
begin
  // 100.123456 TX 1 $120 Data 8 12 23 45 56 67 78 89 12
  // 0          1  2 3    4    5 6  7  8  9  10 11 12 13
  ss := SplitString(AStr, ' ');
  if Length(ss) = 14 then begin
    FTimeUS := round(strtofloatdef(ss[0], 0) * 1000000);
    IsTX := ss[1].CompareTo('Tx') = 0;
    FIdxChn := StrToIntDef(ss[2], 1);
    FIdentifier := StrToIntDef(ss[3], 0);
    //IsData := StrToIntDef(ss[4], 1);   //always isdata
    FDLC := StrToIntDef(ss[5], 8);
    FDATA[0] := StrToIntDef(ss[6], 0);
    FDATA[1] := StrToIntDef(ss[7], 0);
    FDATA[2] := StrToIntDef(ss[8], 0);
    FDATA[3] := StrToIntDef(ss[9], 0);
    FDATA[4] := StrToIntDef(ss[10], 0);
    FDATA[5] := StrToIntDef(ss[11], 0);
    FDATA[6] := StrToIntDef(ss[12], 0);
    FDATA[7] := StrToIntDef(ss[13], 0);
  end;

end;

function TLIBLIN.ToString: string;
var
  sDatas: string;
  i, n: Integer;
begin
  Result := FloatToStr(FTimeUS / 1000000.0);
  if istx then begin
    Result := Result + ' Tx ' + fidxchn.ToString;
  end else begin
    Result := Result + ' Rx ' + fidxchn.ToString;
  end;
  if fidentifier = Byte(-1) then begin
    // error frame
    Result := Result + ' E';
  end else begin
    // normal frame
    if FDLC > 8 then begin
      n := 8;
    end else begin
      n := FDLC;
    end;
    sDatas := '';
    for i:=0 to n - 1 do begin
      sDatas := sDatas + IntToHex(fdata[i], 2) + ' ';
    end;
    Result := result + ' $' + IntToHex(FIdentifier, 1) + ' ' + IntToStr(FDLC) + ' ' + sDatas;
  end;

end;

{ TCANFD }

procedure TLIBCANFD.FromString(const AStr: string);
const
  CANFD_CONF_LEN = 70;
var
  i: Integer;
  ss: TStringDynArray;
begin
  // 100.123456 TX 1 $120 Data 8 12 23 45 56 67 78 89 12
  // 0          1  2 3    4    5 6  7  8  9  10 11 12 13
  ss := SplitString(AStr, ' ');
  if Length(ss) = CANFD_CONF_LEN then begin
    FTimeUS := round(strtofloatdef(ss[0], 0) * 1000000);
    IsTX := ss[1].CompareTo('Tx') = 0;
    FIdxChn := StrToIntDef(ss[2], 1);
    FIdentifier := StrToIntDef(ss[3], 0);
    if ss[4].Equals('F') then begin
      IsEDL := true;
    end else if ss[4].Equals('D') then begin
      IsData := true;
    end else begin
      IsData := false;
    end;
    FDLC := StrToIntDef(ss[5], 8);
    for i:=0 to 63 do begin
      FDATA[i] := StrToIntDef(ss[6 + i], 0);
    end;
  end;

end;

procedure TLIBCANFD.FromTCAN(const ACAN: PLIBCAN);
begin
  PLIBCAN(@self)^ := acan^;
  FFDProperties := 0;

end;

function TLIBCANFD.GetData: boolean;
begin
  Result := (FProperties and MASK_CANProp_REMOTE) = 0;

end;

function TLIBCANFD.GetDataLength: integer;
begin
  Result := GetFDDataLength(FDLC);

end;

function TLIBCANFD.GetErr: Boolean;
begin
  Result := (FProperties and MASK_CANProp_ERROR) <> 0;

end;

function TLIBCANFD.GetIsBRS: boolean;
begin
  Result := (FProperties and MASK_CANFDProp_IS_BRS) <> 0;

end;

function TLIBCANFD.GetIsErrorFrame: boolean;
begin
  Result := fidentifier = (CAN_ID_ERROR);

end;

function TLIBCANFD.GetIsESI: boolean;
begin
  Result := (FProperties and MASK_CANFDProp_IS_ESI) <> 0;

end;

function TLIBCANFD.GetIsFD: Boolean;
begin
  Result := (FFDProperties and MASK_CANFDProp_IS_FD) <> 0;

end;

function TLIBCANFD.GetLogged: boolean;
begin
  Result := (FProperties and MASK_CANProp_LOGGED) <> 0;

end;

function TLIBCANFD.GetStd: Boolean;
begin
  Result := (FProperties and MASK_CANProp_EXTEND) = 0;

end;

function TLIBCANFD.GetTX: Boolean;
begin
  Result := (FProperties and MASK_CANProp_DIR_TX) <> 0;

end;

procedure TLIBCANFD.SetData(const AValue: Boolean);
begin
  if avalue then begin
    FProperties := FProperties and (not MASK_CANProp_REMOTE);
  end else begin
    FProperties := FProperties or MASK_CANProp_REMOTE;
  end;

end;

procedure TLIBCANFD.SetErr(const AValue: Boolean);
begin
  if not AValue then begin
    FProperties := FProperties and (not MASK_CANProp_ERROR);
  end else begin
    FProperties := FProperties or MASK_CANProp_ERROR;
  end;

end;

procedure TLIBCANFD.SetExtId(const AId: Int32; const ADLC: UInt32);
begin
  FIdxChn := 0;
  FIdentifier := AId;
  FDLC := ADLC;
  FProperties := 0;
  SetTX(True);
  SetStd(False);
  SetData(True);
  ZeroMemory(@FData[0], Length(FData));
  FFDProperties := MASK_CANFDProp_IS_FD;
  FTimeUS := 0;

end;

procedure TLIBCANFD.SetIsBRS(const AValue: Boolean);
begin
  if AValue then begin
    FFDProperties := FFDProperties or MASK_CANFDProp_IS_BRS;
  end else begin
    FFDProperties := FFDProperties and (not MASK_CANFDProp_IS_BRS);
  end;

end;

procedure TLIBCANFD.SetIsErrorFrame(const Value: Boolean);
begin
  IsErrToken := true;
  fidentifier := (CAN_ID_ERROR);

end;

procedure TLIBCANFD.SetIsESI(const AValue: Boolean);
begin
  if AValue then begin
    FFDProperties := FFDProperties or MASK_CANFDProp_IS_ESI;
  end else begin
    FFDProperties := FFDProperties and (not MASK_CANFDProp_IS_ESI);
  end;

end;

procedure TLIBCANFD.SetIsFD(const AIsFD: Boolean);
begin
  if AIsFD then begin
    FFDProperties := FFDProperties or MASK_CANFDProp_IS_FD;
  end else begin
    FFDProperties := FFDProperties and (not MASK_CANFDProp_IS_FD);
  end;

end;

procedure TLIBCANFD.SetLogged(const Value: boolean);
begin
  if not Value then begin
    FProperties := FProperties and (not MASK_CANProp_LOGGED);
  end else begin
    FProperties := FProperties or MASK_CANProp_LOGGED;
  end;

end;

procedure TLIBCANFD.SetStd(const AValue: Boolean);
begin
  if avalue then begin
    FProperties := FProperties and (not MASK_CANProp_EXTEND);
  end else begin
    FProperties := FProperties or MASK_CANProp_EXTEND;
  end;

end;

procedure TLIBCANFD.SetStdId(const AId: Int32; const ADLC: UInt32);
begin
  FIdxChn := 0;
  FIdentifier := AId;
  FDLC := ADLC;
  FProperties := 0;
  SetTX(True);
  SetStd(True);
  SetData(True);
  ZeroMemory(@FData[0], Length(FData));
  FFDProperties := MASK_CANFDProp_IS_FD;
  FTimeUS := 0;

end;

procedure TLIBCANFD.SetTX(const AValue: Boolean);
begin
  if avalue then begin
    FProperties := FProperties or MASK_CANProp_DIR_TX;
  end else begin
    FProperties := FProperties and (not MASK_CANProp_DIR_TX);
  end;

end;

function TLIBCANFD.ToString: string;
var
  sDatas: string;
  i: Integer;
begin
  Result := FloatToStr(FTimeUS / 1000000.0);
  if istx then begin
    Result := Result + ' Tx ' + fidxchn.ToString;
  end else begin
    Result := Result + ' Rx ' + fidxchn.ToString;
  end;
  if fidentifier = Integer(-1) then begin
    // error frame
    Result := Result + ' E';
  end else begin
    // normal frame
    if IsStd then begin
      Result := Result + ' $' + IntToHex(fidentifier, 3);
    end else begin
      Result := Result + ' $' + IntToHex(fidentifier, 8);
    end;
    if IsEDL then begin
      Result := Result + ' F ';
    end else begin
      if IsData then begin
        Result := result + ' D ';
      end else begin
        Result := result + ' R ';
      end;
    end;
    if FDLC > 15 then begin
      FDLC := 15;
    end;
    Result := Result + fdlc.ToString + ' ';
    sDatas := '';
    for i:=0 to DLC_DATA_BYTE_CNT[FDLC]-1 do begin
      sDatas := sDatas + IntToHex(fdata[i], 2) + ' ';
    end;
    Result := result + sDatas;
  end;

end;

{ TLIBTSMapping }

procedure TLIBTSMapping.Init;
begin
  ZeroMemory(@FAppName[0], Length(FAppName));
  FAppChannelIndex := 0;
  FAppChannelType := TLIBApplicationChannelType.APP_CAN;
  FHWDeviceType := TLIBBusToolDeviceType.BUS_UNKNOWN_TYPE;
  FHWIndex := 0;
  FHWChannelIndex := 0;
  FHWDeviceSubType := 0;
  ZeroMemory(@FHWDeviceName[0], Length(FHWDeviceName));
  FMappingDisabled := False;

end;

function TLIBTSMapping.SetMappingInfo(const AAppName: string;
  const AIdxLogicalChannel: integer; const AChnType: TLIBApplicationChannelType;
  const AHWDeviceType: TLIBBusToolDeviceType; const AIdxHW, AIdxHWChn,
  AHWDeviceSubType: integer; const AHWDeviceName: string): boolean;
begin
  Result := false;
  if Length(AAppName) >= 32 then exit;
  if Length(AHWDeviceName) >= 32 then exit;
  System.AnsiStrings.StrPCopy(@FAppName[0], AnsiString(AAppName));
  FAppChannelIndex := AIdxLogicalChannel;
  FAppChannelType := AChnType;
  FHWDeviceType := AHWDeviceType;
  FHWIndex := AIdxHW;
  FHWChannelIndex := AIdxHWChn;
  FHWDeviceSubType := AHWDeviceSubType;
  System.AnsiStrings.StrPCopy(@FHWDeviceName[0], AnsiString(AHWDeviceName));
  FMappingDisabled := False;
  result := true;

end;

function TLIBTSMapping.ToString: string;
const
  AppChannelTypeNames: array[0..1] of string = (
    'CAN',
    'LIN'
  );
  BUS_TOOL_DEVICE_NAMES: array [0..3] of string = (
    'Unknown bus tool',
    'TS Virtual Device',
    'Vector',
    'TOSUN'
  );
var
  sChannelType: string;
  sHWName: string;
  sDisabled: string;
begin
  sChannelType := AppChannelTypeNames[Integer(FAppChannelType)] + ' Channel ';
  if FHWDeviceType <> BUS_UNKNOWN_TYPE then begin
    if FHWDeviceSubType <> -1 then begin
      sHWName := BUS_TOOL_DEVICE_NAMES[integer(FHWDeviceType)] + ' ' + string(ansistring(FHWDeviceName));
    end else begin
      sHWName := BUS_TOOL_DEVICE_NAMES[integer(FHWDeviceType)];
    end;
    if FMappingDisabled then begin
      sDisabled := '[ Disabled ]';
    end else begin
      sDisabled := '';
    end;
    // device known
    Result := // APP name
              string(ansistring(FAppName)) + ' ' +
              // APP channel type
              sChannelType +
              // APP channel index
              (FAppChannelIndex + 1).ToString + ' - ' +
              // HW type
              sHWName + ' ' +
              // HW index
              (FHWIndex + 1).ToString + ' ' +
              // HW channel index
              sChannelType + (FHWChannelIndex + 1).ToString + ' ' +
              // disabled token
              sDisabled;
  end else begin
    // device unknown
    Result := // APP name
              string(ansistring(FAppName)) + ' ' +
              // APP channel type
              sChannelType +
              // APP channel index
              (FAppChannelIndex + 1).ToString;
  end;

end;

initialization
  Assert(sizeof(TLIBCAN) = 24, 'TLIBCAN.size = 24');

end.
