#ifndef _TSMaster_MINGWIN_H
#define _TSMaster_MINGWIN_H

#include <math.h>
#include <stdio.h>

#define CH1 0
#define CH2 1
#define CH3 2
#define CH4 3
#define CH5 4
#define CH6 5
#define CH7 6
#define CH8 7
#define CH9 8
#define CH10 9
#define CH11 10
#define CH12 11
#define CH13 12
#define CH14 13
#define CH15 14
#define CH16 15
#define CH17 16
#define CH18 17
#define CH19 18
#define CH20 19
#define CH21 20
#define CH22 21
#define CH23 22
#define CH24 23
#define CH25 24
#define CH26 25
#define CH27 26
#define CH28 27
#define CH29 28
#define CH30 29
#define CH31 30
#define CH32 31

typedef enum {lvlError = 1, lvlWarning = 2, lvlOK = 3, lvlHint = 4, lvlInfo = 5, lvlVerbose = 6} TLogLevel;

// basic var type definition
typedef unsigned __int8 u8;
typedef signed __int8 s8;
typedef unsigned __int16 u16;
typedef signed __int16 s16;
typedef unsigned __int32 u32;
typedef signed __int32 s32;
typedef unsigned __int64 u64;
typedef signed __int64 s64;
// pointer definition
typedef unsigned __int8* pu8;
typedef signed __int8* ps8;
typedef unsigned __int16* pu16;
typedef signed __int16* ps16;
typedef unsigned __int32* pu32;
typedef signed __int32* ps32;
typedef unsigned __int64* pu64;
typedef signed __int64* ps64;
typedef float* pfloat;
typedef double* pdouble;

typedef enum { true = 1, false = 0 } bool;

#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))

#define TSAPI(ret) __declspec(dllimport) ret __stdcall

#pragma pack(push)
#pragma pack(1)

// CAN definitions
#define MASK_CANProp_DIR_TX 0x01
#define MASK_CANProp_REMOTE 0x02
#define MASK_CANProp_EXTEND 0x04
#define MASK_CANProp_ERROR  0x80
#define MASK_CANProp_LOGGED 0x60

// CAN FD message properties
#define MASK_CANFDProp_IS_FD 0x01
#define MASK_CANFDProp_IS_EDL MASK_CANFDProp_IS_FD
#define MASK_CANFDProp_IS_BRS 0x02
#define MASK_CANFDProp_IS_ESI 0x04

// LIN message properties
#define MASK_LINProp_DIR_TX         0x01
#define MASK_LINProp_SEND_BREAK     0x02
#define MASK_LINProp_RECEIVED_BREAK 0x04
#define MASK_LINProp_SEND_SYNC      0x80
#define MASK_LINProp_RECEIVED_SYNC  0x10

// C++ property definition
//#define PROPERTY(t,n)  __declspec( property ( put = property__set_##n, get = property__get_##n ) ) t n;\
//    typedef t property__tmp_type_##n
//#define READONLY_PROPERTY(t,n) __declspec( property (get = property__get_##n) ) t n;\
//    typedef t property__tmp_type_##n
//#define WRITEONLY_PROPERTY(t,n) __declspec( property (put = property__set_##n) ) t n;\
//    typedef t property__tmp_type_##n
//#define GET(n) property__tmp_type_##n property__get_##n() 
//#define SET(n) void property__set_##n(const property__tmp_type_##n& value)   

const u8 DLC_DATA_BYTE_CNT[16] = {
    0, 1, 2, 3, 4, 5, 6, 7,
    8, 12, 16, 20, 24, 32, 48, 64
};

//Data Dir
#define is_tx(CANMsg)                  (CANMsg->FProperties & MASK_CANProp_DIR_TX)  != 0
#define set_tx(CANMsg)                CANMsg->FProperties |= MASK_CANProp_DIR_TX
#define set_rx(CANMsg)                CANMsg->FProperties &= (~MASK_CANProp_DIR_TX)
//Data Attribute
#define is_data(CANMsg)               (CANMsg->FProperties & MASK_CANProp_REMOTE)  == 0
#define set_remote(CANMsg)         CANMsg->FProperties |= MASK_CANProp_REMOTE
#define set_data(CANMsg)             CANMsg->FProperties &= (~MASK_CANProp_REMOTE)
//Is STD
#define is_standard(CANMsg)               (CANMsg->FProperties & MASK_CANProp_EXTEND)  == 0
#define set_extended(CANMsg)      CANMsg->FProperties |= MASK_CANProp_EXTEND
#define set_standard(CANMsg)      CANMsg->FProperties &= (~MASK_CANProp_EXTEND)
//Is Error
#define is_error(CANMsg)               (CANMsg->FProperties & MASK_CANProp_ERROR)  != 0
#define set_error(CANMsg)            CANMsg->FProperties |= MASK_CANProp_ERROR
#define set_normal(CANMsg)         CANMsg->FProperties &= (~MASK_CANProp_ERROR)

// CAN frame type ================================================
typedef struct _TCAN{
    u8 FIdxChn;
    u8 FProperties;
    u8 FDLC;
    u8 FReserved;
    s32 FIdentifier;
    s64 FTimeUs;
    u8  FData[8];
} TCAN, *PCAN;

//Is EDL: is FD
#define is_FD(CANMsg)                (CANMsg->FFDProperties & MASK_CANFDProp_IS_FD)  != 0
#define set_FD(CANMsg)              CANMsg->FFDProperties |= MASK_CANFDProp_IS_FD
#define set_Classic(CANMsg)        CANMsg->FFDProperties &= (~MASK_CANFDProp_IS_FD)

//Is Brs
#define is_brs(CANMsg)               (CANMsg->FProperties & MASK_CANFDProp_IS_BRS)  != 0
#define set_brs(CANMsg)             CANMsg->FProperties |= MASK_CANFDProp_IS_BRS
#define disable_brs(CANMsg)       CANMsg->FProperties &= (~MASK_CANFDProp_IS_BRS)

//Is Error
#define is_ESI(CANMsg)               (CANMsg->FProperties & MASK_CANFDProp_IS_ESI)  != 0
#define set_ESI(CANMsg)             CANMsg->FProperties |= MASK_CANFDProp_IS_ESI
#define disable_ESI(CANMsg)       CANMsg->FProperties &= (~MASK_CANFDProp_IS_ESI)
// CAN FD frame type =============================================
typedef struct _TCANFD{
    u8 FIdxChn;
    u8 FProperties;
    u8 FDLC;
    u8 FFDProperties;
    s32 FIdentifier;
    s64 FTimeUs;
    u8  FData[64];
} TCANFD, *PCANFD;

//Is Error
#define is_lin_tx(LINMsg)               (CANMsg->FProperties & MASK_LINProp_DIR_TX)  != 0
#define set_lin_tx(LINMsg)             CANMsg->FProperties |= MASK_LINProp_DIR_TX
#define set_lin_rx(LINMsg)             CANMsg->FProperties &= (~MASK_LINProp_DIR_TX)
// LIN frame type ================================================
typedef struct _TLIN {
    u8  FIdxChn;
    u8  FErrStatus;
    u8  FProperties;
    u8  FDLC;
    u8  FIdentifier;
    u8  FChecksum;
    u8  FStatus;
    s64 FTimeUs;
    u8  FData[8];
} TLIN, *PLIN;

// Generic definitions ===========================================
typedef void (__stdcall *TProcedure)(const void* AObj);
typedef void (__stdcall *TProcedureSetInt)(const void* AObj, const s32 AValue);
typedef s32 (__stdcall *TIntFunction)(const void* AObj);
typedef void (__stdcall *TProcedureSetDouble)(const void* AObj, const double AValue);
typedef double (__stdcall *TDoubleFunction)(const void* AObj);
typedef void (__stdcall *TProcedureSetString)(const void* AObj, const char* AValue);
typedef char* (__stdcall *TStringFunction)(const void* AObj);
typedef void (__stdcall *TProcedureSetCAN)(const void* AObj, const PCAN AValue);
typedef TCAN (__stdcall *TTCANFunction)(const void* AObj);
typedef void (__stdcall *TProcedureSetCANFD)(const void* AObj, const PCANFD AValue);
typedef TCANFD (__stdcall *TTCANFDFunction)(const void* AObj);
typedef void (__stdcall *TProcedureSetLIN)(const void* AObj, const PLIN AValue);
typedef TLIN (__stdcall *TTLINFunction)(const void* AObj);

// TSMaster application definition ===============================
#define APP_DEVICE_NAME_LENGTH 32
typedef enum {
    BUS_UNKNOWN_TYPE           = 0, 
    TS_TCP_DEVICE              = 1, 
    XL_USB_DEVICE              = 2, 
    TS_USB_DEVICE              = 3, 
    PEAK_USB_DEVICE            = 4,
    KVASER_USB_DEVICE          = 5,
    ZLG_USB_DEVICE             = 6,
    ICS_USB_DEVICE             = 7,
    TS_TC1005_DEVICE           = 8
} TLIBBusToolDeviceType, *PLIBBusToolDeviceType;
typedef enum {APP_CAN = 0, APP_LIN = 1} TLIBApplicationChannelType;
typedef enum {
    cbsBusLoad = 0, cbsPeakLoad, cbsFpsStdData, cbsAllStdData,
    cbsFpsExtData, cbsAllExtData, cbsFpsStdRemote, cbsAllStdRemote,
    cbsFpsExtRemote, cbsAllExtRemote, cbsFpsErrorFrame, cbsAllErrorFrame    
} TLIBCANBusStatistics;

#define VENDOR_NAME_LENGTH            (32)
#define DEVICE_SERIAL_STRING_LENGTH   (64)
// Hardware Info definition
typedef struct {
    TLIBBusToolDeviceType FDeviceType;
    s32 FDeviceIndex;
    char FVendorName[VENDOR_NAME_LENGTH];
    char FDeviceName[APP_DEVICE_NAME_LENGTH];
    char FSerialString[DEVICE_SERIAL_STRING_LENGTH];
}TLIBHWInfo, *PLIBHWInfo;

typedef struct _TLIBTSMapping {
    char                       FAppName[APP_DEVICE_NAME_LENGTH];
    s32                        FAppChannelIndex;
    TLIBApplicationChannelType FAppChannelType;
    TLIBBusToolDeviceType      FHWDeviceType;
    s32                        FHWIndex;
    s32                        FHWChannelIndex;
    s32                        FHWDeviceSubType;
    char                       FHWDeviceName[APP_DEVICE_NAME_LENGTH];
    bool                       FMappingDisabled;
} TLIBTSMapping, *PLIBTSMapping;
// system var def
typedef enum {svtInt32 = 0, svtUInt32, svtInt64, svtUInt64, svtUInt8Array,
    svtInt32Array, svtInt64Array, svtDouble, svtDoubleArray, svtString} TLIBSystemVarType;
typedef struct {
    char              FName[APP_DEVICE_NAME_LENGTH];
    char              FCategory[APP_DEVICE_NAME_LENGTH];
    char              FComment[APP_DEVICE_NAME_LENGTH];
    TLIBSystemVarType FDataType;
    bool              FIsReadOnly;
    double            FValueMin;
    double            FValueMax;
} TLIBSystemVarDef, *PLIBSystemVarDef;
typedef enum {fdtCAN = 0, fdtISOCANFD = 1, fdtNonISOCANFD = 2} TCANFDControllerType;
typedef enum {fdmNormal = 0, fdmACKOff = 1, fdmRestricted = 2} TCANFDControllerMode;
// log def
typedef enum {ortImmediately = 0, ortAsLog = 1, ortDelayed = 2} TLIBOnlineReplayTimingMode;
typedef enum {orsNotStarted = 0, orsRunning = 1, orsPaused = 2, orsCompleted = 3, orsTerminated = 4} TLIBOnlineReplayStatus;
// database utilities
typedef struct {
    u8     FCANSgnType; // 0 - Unsigned, 1 - Signed, 2 - Single 32, 3 - Double 64
    bool   FIsIntel;
    s32    FStartBit;
    s32    FLength;    
    double FFactor;
    double FOffset;    
} TCANSignal, *PCANSignal;
#define CANMsgDecl(typ, name, chn, prop, dlc, id) const typ name = {{chn, prop, dlc, 0, id, 0, {0}}};
#define CANSgnDecl(name, typ, isIntel, startBit, len, factor, offset) const TCANSignal name = {typ, isIntel, startBit, len, factor, offset};
typedef enum {rivUseDB = 0, rivUseLast, rivUse0} TLIBRBSInitValueOptions;
typedef double (__stdcall* TGetCANSignalValue)(const PCANSignal ACANSignal, const pu8 AData);
typedef void (__stdcall* TSetCANSignalValue)(const PCANSignal ACANSignal, const pu8 AData, const double AValue);
typedef void (__stdcall* TCANEvent)(const ps32 AObj, const PCAN ACAN);
typedef void (__stdcall* TCANFDEvent)(const ps32 AObj, const PCANFD ACANFD);
typedef void (__stdcall* TLINEvent)(const ps32 AObj, const PLIN ALIN);
typedef void (__stdcall* TLogger)(const char* AStr, const s32 ALevel);

// imported APIs
#if defined ( __cplusplus )
extern "C" {
#endif
TSAPI(void) finalize_lib_tsmaster(void);
TSAPI(s32) initialize_lib_tsmaster(const char* AAppName);
TSAPI(s32) tsapp_add_application(const char* AAppName);
TSAPI(s32) tsapp_add_cyclic_msg_can(const PCAN ACAN, const float APeriodMS);
TSAPI(s32) tsapp_add_cyclic_msg_canfd(const PCANFD ACANFD, const float APeriodMS);
TSAPI(s32) tsapp_clear_bus_statistics(void);
TSAPI(s32) tsapp_configure_baudrate_can(const s32 AIdxChn, const float ABaudrateKbps, const bool AListenOnly, const bool AInstallTermResistor120Ohm);
TSAPI(s32) tsapp_configure_baudrate_canfd(const s32 AIdxChn, const float ABaudrateArbKbps, const float ABaudrateDataKbps, const TCANFDControllerType AControllerType, const TCANFDControllerMode AControllerMode, const bool AInstallTermResistor120Ohm);
TSAPI(s32) tsapp_connect(void);
TSAPI(s32) tsapp_del_application(const char* AAppName);
TSAPI(s32) tsapp_del_mapping(const PLIBTSMapping AMapping);
TSAPI(s32) tsapp_del_mapping_verbose(const char* AAppName,
                                     const TLIBApplicationChannelType AAppChannelType,
                                     const s32 AAppChannel);
TSAPI(s32) tsapp_delete_cyclic_msg_can(const PCAN ACAN);
TSAPI(s32) tsapp_delete_cyclic_msg_canfd(const PCANFD ACANFD);
TSAPI(s32) tsapp_delete_cyclic_msgs(void);
TSAPI(s32) tsapp_disconnect(void);
TSAPI(s32) tsapp_enable_bus_statistics(const bool AEnable);
// tsapp_enumerate_hw_devices
TSAPI(s32) tsapp_execute_python_string(const char* AString, const bool AIsSync, const bool AIsX64, char** AResultLog);
TSAPI(s32) tsapp_execute_python_script(const char* AFilePath, const bool AIsSync, const bool AIsX64, char** AResultLog);
TSAPI(s32) tsapp_get_application_list(char** AAppNameList);
TSAPI(s32) tsapp_get_bus_statistics(const TLIBApplicationChannelType ABusType, const s32 AIdxChn, const TLIBCANBusStatistics AIdxStat, pdouble AStat);
TSAPI(s32) tsapp_get_can_channel_count(const ps32 ACount);
TSAPI(s32) tsapp_get_current_application(const char** AAppName);
TSAPI(s32) tsapp_get_error_description(const s32 ACode, char** ADesc);
TSAPI(s32) tsapp_get_fps_can(const s32 AIdxChn, const s32 AIdentifier, ps32 AFPS);
TSAPI(s32) tsapp_get_fps_canfd(const s32 AIdxChn, const s32 AIdentifier, ps32 AFPS);
TSAPI(s32) tsapp_get_fps_lin(const s32 AIdxChn, const s32 AIdentifier, ps32 AFPS);
TSAPI(s32) tsapp_get_hw_info_by_index(const s32 AIndex, const PLIBHWInfo AHWInfo);
TSAPI(s32) tsapp_get_hw_info_by_index_verbose(const s32 AIndex,
                                      PLIBBusToolDeviceType ADeviceType,
                                      char* AVendorNameBuffer, //array[0..31] of AnsiChar;
                                      s32 AVendorNameBufferSize,
                                      char* ADeviceNameBuffer, //array[0..31] of AnsiChar;
                                      s32 ADeviceNameBufferSize,
                                      char* ASerialStringBuffer, //array[0..63] of AnsiChar
                                      s32 ASerialStringBufferSize
                                      );
TSAPI(s32) tsapp_get_lin_channel_count(const ps32 ACount);
TSAPI(s32) tsapp_get_mapping(const PLIBTSMapping AMapping);
TSAPI(s32) tsapp_get_mapping_verbose(const char* AAppName,
                                     const TLIBApplicationChannelType AAppChannelType,
                                     const s32 AAppChannel,
                                     const PLIBTSMapping AMapping); 
TSAPI(s32) tsapp_get_timestamp(s64* ATimestamp);
TSAPI(s32) tsapp_get_turbo_mode(const bool* AEnable);
// tsapp_get_vendor_detect_preferences
TSAPI(void) tsapp_log(const char* AStr, const TLogLevel ALevel);
TSAPI(void) tsfifo_enable_receive_error_frames(void);
TSAPI(void) tsfifo_enable_receive_fifo(void);
TSAPI(void) tsfifo_disable_receive_error_frames(void);
TSAPI(void) tsfifo_disable_receive_fifo(void);
TSAPI(s32) tsfifo_read_can_buffer_frame_count(const s32 AIdxChn, ps32 ACount);
TSAPI(s32) tsfifo_read_can_rx_buffer_frame_count(const s32 AIdxChn, ps32 ACount);
TSAPI(s32) tsfifo_read_can_tx_buffer_frame_count(const s32 AIdxChn, ps32 ACount);
TSAPI(s32) tsfifo_read_canfd_buffer_frame_count(const s32 AIdxChn, ps32 ACount);
TSAPI(s32) tsfifo_read_canfd_rx_buffer_frame_count(const s32 AIdxChn, ps32 ACount);
TSAPI(s32) tsfifo_read_canfd_tx_buffer_frame_count(const s32 AIdxChn, ps32 ACount);
TSAPI(s32) tsfifo_read_fastlin_buffer_frame_count(const s32 AIdxChn, ps32 ACount);
TSAPI(s32) tsfifo_read_fastlin_rx_buffer_frame_count(const s32 AIdxChn, ps32 ACount);
TSAPI(s32) tsfifo_read_fastlin_tx_buffer_frame_count(const s32 AIdxChn, ps32 ACount);
TSAPI(s32) tsfifo_read_lin_buffer_frame_count(const s32 AIdxChn, ps32 ACount);
TSAPI(s32) tsfifo_read_lin_rx_buffer_frame_count(const s32 AIdxChn, ps32 ACount);
TSAPI(s32) tsfifo_read_lin_tx_buffer_frame_count(const s32 AIdxChn, ps32 ACount);
TSAPI(s32) tsfifo_receive_can_msgs(PCAN ACANBuffers, ps32 ACANBufferSize, const s32 AIdxChn, const bool AIncludeTx);
TSAPI(s32) tsfifo_receive_canfd_msgs(PCANFD ACANFDBuffers, ps32 ACANFDBufferSize, const s32 AIdxChn, const bool AIncludeTx);
TSAPI(s32) tsfifo_receive_fastlin_msgs(PLIN ALINBuffers, ps32 ALINBufferSize, const s32 AIdxChn, const bool AIncludeTx);
TSAPI(s32) tsfifo_receive_lin_msgs(PLIN ALINBuffers, ps32 ALINBufferSize, const s32 AIdxChn, const bool AIncludeTx);
TSAPI(s32) tsfifo_clear_can_receive_buffers(const s32 AIdxChn);
TSAPI(s32) tsfifo_clear_canfd_receive_buffers(const s32 AIdxChn);
TSAPI(s32) tsfifo_clear_fastlin_receive_buffers(const s32 AIdxChn);
TSAPI(s32) tsfifo_clear_lin_receive_buffers(const s32 AIdxChn);
TSAPI(s32) tsapp_register_event_can(const ps32 AObj, const TCANEvent AEvent);
TSAPI(s32) tsapp_register_event_canfd(const ps32 AObj, const TCANFDEvent AEvent);
TSAPI(s32) tsapp_register_event_lin(const ps32 AObj, const TLINEvent AEvent);
TSAPI(s32) tsapp_register_pretx_event_can(const ps32 AObj, const TCANEvent AEvent);
TSAPI(s32) tsapp_register_pretx_event_canfd(const ps32 AObj, const TCANFDEvent AEvent);
TSAPI(s32) tsapp_register_pretx_event_lin(const ps32 AObj, const TLINEvent AEvent);
TSAPI(s32) tsapp_set_can_channel_count(const s32 ACount);
TSAPI(s32) tsapp_set_current_application(const char* AAppName);
TSAPI(s32) tsapp_set_lin_channel_count(const s32 ACount);
TSAPI(s32) tsapp_set_logger(const TLogger ALogger);
TSAPI(s32) tsapp_set_mapping(const PLIBTSMapping AMapping);
TSAPI(s32) tsapp_set_mapping_verbose(const char* AAppName,
                                     const TLIBApplicationChannelType AAppChannelType,
                                     const s32 AAppChannel,  
                                     const char* AHardwareName,
                                     const TLIBBusToolDeviceType AHardwareType,
                                     const s32 AHardwareSubType,
                                     const s32 AHardwareIndex,
                                     const s32 AHardwareChannel,  
                                     const bool AEnableMapping); 
TSAPI(s32) tsapp_set_turbo_mode(const bool AEnable);
TSAPI(s32) tsapp_set_vendor_detect_preferences(const bool AScanTOSUN, 
	                                           const bool AScanVector, 
	                                           const bool AScanPeak, 
	                                           const bool AScanKvaser, 
	                                           const bool AScanZLG, 
	                                           const bool AScanIntrepidcs);
// tsapp_show_channel_mapping_window
// tsapp_show_hardware_configuration_window
TSAPI(s32) tsapp_show_tsmaster_window(const char* AWindowName, const bool AWaitClose);
TSAPI(s32) tsapp_start_logging(const void* AObj);
TSAPI(s32) tsapp_stop_logging(const void* AObj);
TSAPI(s32) tsapp_transmit_can_async(const PCAN ACAN);
TSAPI(s32) tsapp_transmit_canfd_async(const PCANFD ACANFD);
TSAPI(s32) tsapp_transmit_lin_async(const PLIN ALIN);
TSAPI(s32) tsapp_transmit_can_sync(const PCAN ACAN, const s32 ATimeoutMS);
TSAPI(s32) tsapp_transmit_canfd_sync(const PCANFD ACANFD, const s32 ATimeoutMS);
TSAPI(s32) tsapp_transmit_lin_sync(const PLIN ALIN, const s32 ATimeoutMS);
// tsapp_transmit_fastlin_async
TSAPI(s32) tsapp_unregister_event_can(const ps32 AObj, const TCANEvent AEvent);
TSAPI(s32) tsapp_unregister_event_canfd(const ps32 AObj, const TCANFDEvent AEvent);
TSAPI(s32) tsapp_unregister_event_lin(const ps32 AObj, const TLINEvent AEvent);
TSAPI(s32) tsapp_unregister_events_can(const ps32 AObj);
TSAPI(s32) tsapp_unregister_events_lin(const ps32 AObj);
TSAPI(s32) tsapp_unregister_events_canfd(const ps32 AObj);
TSAPI(s32) tsapp_unregister_events_all(const ps32 AObj);
TSAPI(s32) tsapp_unregister_pretx_event_can(const ps32 AObj, const TCANEvent AEvent);
TSAPI(s32) tsapp_unregister_pretx_event_canfd(const ps32 AObj, const TCANFDEvent AEvent);
TSAPI(s32) tsapp_unregister_pretx_event_lin(const ps32 AObj, const TLINEvent AEvent);
TSAPI(s32) tsapp_unregister_pretx_events_can(const ps32 AObj);
TSAPI(s32) tsapp_unregister_pretx_events_lin(const ps32 AObj);
TSAPI(s32) tsapp_unregister_pretx_events_canfd(const ps32 AObj);
TSAPI(s32) tsapp_unregister_pretx_events_all(const ps32 AObj);
// tsapp_update_cyclic_msg_can
TSAPI(s32) tscom_can_rbs_start(void);
TSAPI(s32) tscom_can_rbs_stop(void);
TSAPI(s32) tscom_can_rbs_is_running(bool* AIsRunning);
TSAPI(s32) tscom_can_rbs_configure(const bool AAutoStart, const bool AAutoSendOnModification, const bool AActivateNodeSimulation, const TLIBRBSInitValueOptions AInitValueOptions);
TSAPI(s32) tscom_can_rbs_activate_all_networks(const bool AEnable, const bool AIncludingChildren);
TSAPI(s32) tscom_can_rbs_activate_network_by_name(const bool AEnable, const char* ANetworkName, const bool AIncludingChildren);
TSAPI(s32) tscom_can_rbs_activate_node_by_name(const bool AEnable, const char* ANetworkName, const char* ANodeName, const bool AIncludingChildren);
TSAPI(s32) tscom_can_rbs_activate_message_by_name(const bool AEnable, const char* ANetworkName, const char* ANodeName, const char* AMsgName);
TSAPI(s32) tscom_can_rbs_get_signal_value_by_element(const s32 AIdxChn, const char* ANetworkName, const char* ANodeName, const char* AMsgName, const char* ASignalName, double* AValue);
TSAPI(s32) tscom_can_rbs_get_signal_value_by_address(const char* ASymbolAddress, double* AValue);
TSAPI(s32) tscom_can_rbs_set_signal_value_by_element(const s32 AIdxChn, const char* ANetworkName, const char* ANodeName, const char* AMsgName, const char* ASignalName, const double AValue);
TSAPI(s32) tscom_can_rbs_set_signal_value_by_address(const char* ASymbolAddress, const double AValue);
TSAPI(s32) tsdb_get_signal_value_can(const PCAN ACAN, const char* AMsgName, const char* ASgnName, double* AValue);
TSAPI(s32) tsdb_get_signal_value_canfd(const PCANFD ACANFD, const char* AMsgName, const char* ASgnName, double* AValue);
TSAPI(s32) tsdb_set_signal_value_can(const PCAN ACAN, const char* AMsgName, const char* ASgnName, const double AValue);
TSAPI(s32) tsdb_set_signal_value_canfd(const PCANFD ACANFD, const char* AMsgName, const char* ASgnName, const double AValue);
TSAPI(s32) tsdb_load_can_db(const char* ADBC, const char* ASupportedChannelsBased0, u32* AId);
TSAPI(s32) tsdb_unload_can_db(const u32 AId);
TSAPI(s32) tsdb_unload_can_dbs(void);
TSAPI(s32) tsdb_get_can_db_count(s32* ACount);
TSAPI(s32) tsdb_get_can_db_id(const s32 AIndex, u32* AId);
TSAPI(s32) tsdb_get_can_db_info(const u32 ADatabaseId, const s32 AType, const s32 AIndex, const s32 ASubIndex, char** AValue);
TSAPI(s32) tslog_add_online_replay_config(const char* AFileName, s32* AIndex);
TSAPI(s32) tslog_set_online_replay_config(const s32 AIndex, const char* AName, const char* AFileName, const bool AAutoStart, const bool AIsRepetitiveMode, const TLIBOnlineReplayTimingMode AStartTimingMode, const s32 AStartDelayTimeMs, const bool ASendTx, const bool ASendRx, const char* AMappings);
TSAPI(s32) tslog_get_online_replay_count(s32* ACount);
TSAPI(s32) tslog_get_online_replay_config(const s32 AIndex, char** AName, char** AFileName, bool* AAutoStart, bool* AIsRepetitiveMode, TLIBOnlineReplayTimingMode* AStartTimingMode, s32* AStartDelayTimeMs, bool* ASendTx, bool* ASendRx, char** AMappings);
TSAPI(s32) tslog_del_online_replay_config(const s32 AIndex);
TSAPI(s32) tslog_del_online_replay_configs(void);
TSAPI(s32) tslog_start_online_replay(const s32 AIndex);
TSAPI(s32) tslog_start_online_replays(void);
TSAPI(s32) tslog_pause_online_replay(const s32 AIndex);
TSAPI(s32) tslog_pause_online_replays(void);
TSAPI(s32) tslog_stop_online_replay(const s32 AIndex);
TSAPI(s32) tslog_stop_online_replays(void);
TSAPI(s32) tslog_get_online_replay_status(const s32 AIndex, TLIBOnlineReplayStatus* AStatus, float* AProgressPercent100);

#if defined ( __cplusplus )
}
#endif

#pragma pack(pop)

#endif
