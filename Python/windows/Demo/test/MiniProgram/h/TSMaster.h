#ifndef _TSMaster_MP_H
#define _TSMaster_MP_H

/*
  Note: 
  [1] Definitions of TCAN, TCANFD, TLIN, TFlexRay can be found in this header
  [2] channel index is always starting from 0
  [3] for error codes of API, please see bottem area of this file
  [4] F3 for fast locating: _TTSApp _TTSCOM _TTSTest
*/

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
typedef signed __int32** pps32;
typedef unsigned __int64* pu64;
typedef signed __int64* ps64;
typedef float* pfloat;
typedef double* pdouble;
typedef char* pchar;

#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
#define DLLEXPORT extern "C" _declspec(dllexport)

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
#define PROPERTY(t,n)  __declspec( property ( put = property__set_##n, get = property__get_##n ) ) t n;\
    typedef t property__tmp_type_##n
#define READONLY_PROPERTY(t,n) __declspec( property (get = property__get_##n) ) t n;\
    typedef t property__tmp_type_##n
#define WRITEONLY_PROPERTY(t,n) __declspec( property (put = property__set_##n) ) t n;\
    typedef t property__tmp_type_##n
#define GET(n) property__tmp_type_##n property__get_##n() 
#define SET(n) void property__set_##n(const property__tmp_type_##n& value)   

const u8 DLC_DATA_BYTE_CNT[16] = {
    0, 1, 2, 3, 4, 5, 6, 7,
    8, 12, 16, 20, 24, 32, 48, 64
};
        
// CAN frame type ================================================
typedef struct _TCAN{
    u8 FIdxChn;
    u8 FProperties;
    u8 FDLC;
    u8 FReserved;
    s32 FIdentifier;
    s64 FTimeUs;
    u8  FData[8];
    // is_tx -----------------------------------------------------
    PROPERTY(bool, is_tx);
    GET(is_tx)  
    { 
        return (FProperties & MASK_CANProp_DIR_TX) != 0;
    }
    SET(is_tx)
    {
        if (value) {
            FProperties = FProperties | MASK_CANProp_DIR_TX;
        } else {
            FProperties = FProperties & (~MASK_CANProp_DIR_TX);
        }
    }
    // is_data ----------------------------------------------------
    PROPERTY(bool, is_data);
    GET(is_data) 
    { 
        return (FProperties & MASK_CANProp_REMOTE) == 0;
    }
    SET(is_data)
    {
        if (value) {
            FProperties = FProperties & (~MASK_CANProp_REMOTE);
        } else {
            FProperties = FProperties | MASK_CANProp_REMOTE;
        }
    }
    // is_std -----------------------------------------------------
    PROPERTY(bool, is_std);
    GET(is_std) 
    { 
        return (FProperties & MASK_CANProp_EXTEND) == 0;
    }
    SET(is_std)
    {
        if (value) {
            FProperties = FProperties & (~MASK_CANProp_EXTEND);
        } else {
            FProperties = FProperties | MASK_CANProp_EXTEND;
        }
    }
    // is_err ----------------------------------------------------
    PROPERTY(bool, is_err);
    GET(is_err) 
    { 
        return (FProperties & MASK_CANProp_ERROR) != 0;
    }
    SET(is_err)
    {
        if (value) {
            FProperties = FProperties & (~MASK_CANProp_ERROR);
        } else {
            FProperties = FProperties | MASK_CANProp_ERROR;
        }
    }
    // load data bytes -------------------------------------------
    void load_data(u8* a) {
        for (u32 i = 0; i < 8; i++) {
            FData[i] = *a++;
        }
    }
    void set_data(const u8 d0, const u8 d1, const u8 d2, const u8 d3, const u8 d4, const u8 d5, const u8 d6, const u8 d7){
        FData[0] = d0;
        FData[1] = d1;
        FData[2] = d2;
        FData[3] = d3;
        FData[4] = d4;
        FData[5] = d5;
        FData[6] = d6;
        FData[7] = d7;
    }
    // initialize with standard identifier -----------------------
    void init_w_std_id(s32 AId, s32 ADLC) {
        FIdxChn = 0;
        FIdentifier = AId;
        FDLC = ADLC;
        FReserved = 0;
        FProperties = 0;
        is_tx = false;
        is_std = true;
        is_data = true;
        *(u64*)(&FData[0]) = 0;
        FTimeUs = 0;
    }
    // initialize with extended identifier -----------------------
    void init_w_ext_id(s32 AId, s32 ADLC) {
        FIdxChn = 0;
        FIdentifier = AId;
        FDLC = ADLC;
        FReserved = 0;
        FProperties = 0;
        is_tx = false;
        is_std = false;
        is_data = true;
        *(u64*)(&FData[0]) = 0;
        FTimeUs = 0;
    }
} TCAN, *PCAN;

// CAN FD frame type =============================================
typedef struct _TCANFD{
    u8 FIdxChn;
    u8 FProperties;
    u8 FDLC;
    u8 FFDProperties;
    s32 FIdentifier;
    s64 FTimeUs;
    u8  FData[64];
    // is_tx -----------------------------------------------------
    PROPERTY(bool, is_tx);
    GET(is_tx)  
    { 
        return (FProperties & MASK_CANProp_DIR_TX) != 0;
    }
    SET(is_tx)
    {
        if (value) {
            FProperties = FProperties | MASK_CANProp_DIR_TX;
        } else {
            FProperties = FProperties & (~MASK_CANProp_DIR_TX);
        }
    }
    // is_data ---------------------------------------------------
    PROPERTY(bool, is_data);
    GET(is_data) 
    { 
        return (FProperties & MASK_CANProp_REMOTE) == 0;
    }
    SET(is_data)
    {
        if (value) {
            FProperties = FProperties & (~MASK_CANProp_REMOTE);
        } else {
            FProperties = FProperties | MASK_CANProp_REMOTE;
        }
    }
    // is_std ----------------------------------------------------
    PROPERTY(bool, is_std);
    GET(is_std) 
    { 
        return (FProperties & MASK_CANProp_EXTEND) == 0;
    }
    SET(is_std)
    {
        if (value) {
            FProperties = FProperties & (~MASK_CANProp_EXTEND);
        } else {
            FProperties = FProperties | MASK_CANProp_EXTEND;
        }
    }
    // is_err ----------------------------------------------------
    PROPERTY(bool, is_err);
    GET(is_err) 
    { 
        return (FProperties & MASK_CANProp_ERROR) != 0;
    }
    SET(is_err)
    {
        if (value) {
            FProperties = FProperties & (~MASK_CANProp_ERROR);
        } else {
            FProperties = FProperties | MASK_CANProp_ERROR;
        }
    }
    // is_edl ----------------------------------------------------
    PROPERTY(bool, is_edl);
    GET(is_edl) 
    { 
        return (FFDProperties & MASK_CANFDProp_IS_FD) != 0;
    }
    SET(is_edl)
    {
        if (value) {
            FFDProperties = FFDProperties | MASK_CANFDProp_IS_FD;
        } else {
            FFDProperties = FFDProperties & (~MASK_CANFDProp_IS_FD);
        }
    }
    // is_brs ----------------------------------------------------
    PROPERTY(bool, is_brs);
    GET(is_brs) 
    { 
        return (FFDProperties & MASK_CANFDProp_IS_BRS) != 0;
    }
    SET(is_brs)
    {
        if (value) {
            FFDProperties = FFDProperties | MASK_CANFDProp_IS_BRS;
        } else {
            FFDProperties = FFDProperties & (~MASK_CANFDProp_IS_BRS);
        }
    }
    // is_esi ----------------------------------------------------
    PROPERTY(bool, is_esi);
    GET(is_esi) 
    { 
        return (FFDProperties & MASK_CANFDProp_IS_ESI) != 0;
    }
    SET(is_esi)
    {
        if (value) {
            FFDProperties = FFDProperties | MASK_CANFDProp_IS_ESI;
        } else {
            FFDProperties = FFDProperties & (~MASK_CANFDProp_IS_ESI);
        }
    }    
    // load data bytes -------------------------------------------
    void load_data(u8* a) {
        for (u32 i = 0; i < 64; i++) {
            FData[i] = *a++;
        }
    }
    // initialize with standard identifier -----------------------
    void init_w_std_id(s32 AId, s32 ADLC) {
        s32 i;
        FIdxChn = 0;
        FIdentifier = AId;
        FDLC = ADLC;
        FProperties = 0;
        FFDProperties = MASK_CANFDProp_IS_FD;
        is_tx = false;
        is_std = true;
        is_data = true;
        for (i = 0; i < 64; i++) FData[i] = 0;
        FTimeUs = 0;
    }
    // initialize with extended identifier -----------------------
    void init_w_ext_id(s32 AId, s32 ADLC) {
        s32 i;
        FIdxChn = 0;
        FIdentifier = AId;
        FDLC = ADLC;
        FFDProperties = MASK_CANFDProp_IS_FD;
        FProperties = 0;
        is_tx = false;
        is_std = false;
        is_data = true;
        for (i = 0; i < 64; i++) FData[i] = 0;
        FTimeUs = 0;
    }
    // get fd data length ----------------------------------------
    s32 get_data_length() {
        s32 l = MIN(FDLC, 15);
        l = MAX(l, 0);
        return DLC_DATA_BYTE_CNT[l];
    }
    // to CAN struct ---------------------------------------------
    TCAN to_tcan(void){
        return *(TCAN*)(&FIdxChn);
    }
} TCANFD, *PCANFD;

// LIN frame type ================================================
typedef struct _LIN {
    u8  FIdxChn;
    u8  FErrStatus;
    u8  FProperties;
    u8  FDLC;
    u8  FIdentifier;
    u8  FChecksum;
    u8  FStatus;
    s64 FTimeUs;
    u8  FData[8];
    // is_tx -----------------------------------------------------
    PROPERTY(bool, is_tx);
    GET(is_tx)
    {
        return (FProperties & MASK_LINProp_DIR_TX) != 0;
    }
    SET(is_tx)
    {
        if (value) {
            FProperties = FProperties | MASK_LINProp_DIR_TX;
        }
        else {
            FProperties = FProperties & (~MASK_LINProp_DIR_TX);
        }
    }
    // load data bytes -------------------------------------------
    void load_data(u8* a) {
        for (u32 i = 0; i < 8; i++) {
            FData[i] = *a++;
        }
    }
    // initialize with identifier --------------------------------
    void init_w_id(const s32 AId, const s32 ADLC) {
        FIdxChn = 0;
        FErrStatus = 0;
        FProperties = 0;
        FDLC = ADLC;
        FIdentifier = AId;
        *(__int64*)(&FData[0]) = 0;
        FChecksum = 0;
        FStatus = 0;
        FTimeUs = 0;
    }
}TLIN, *PLIN;

// FlexRay Frame Type ============================================
typedef struct _TFlexRay {
	u8  FIdxChn;               // channel index starting from 0
	u8  FChannelMask;          // 0: reserved, 1: A, 2: B, 3: AB
	u8  FDir;                  // 0: Rx, 1: Tx, 2: Tx Request
	u8  FPayloadLength;        // payload length in bytes
	u8  FActualPayloadLength;  // actual data bytes
	u8  FCycleNumber;          // cycle number: 0~63
	u8  FCCType;               // 0 = Architecture independent, 1 = Invalid CC type, 2 = Cyclone I, 3 = BUSDOCTOR, 4 = Cyclone II, 5 = Vector VN interface, 6 = VN - Sync - Pulse(only in Status Event, for debugging purposes only)
	u8  FFrameType;            // 0 = raw flexray frame, 1 = error event, 2 = status, 3 = start cycle
	u16 FHeaderCRCA;           // header crc A
	u16 FHeaderCRCB;           // header crc B
	u16 FFrameStateInfo;       // bit 0~15, error flags
	u16 FSlotId;               // static seg: 0~1023
	u32 FFrameFlags;           // bit 0~22
                               // 0 1 = Null frame.
                               // 1 1 = Data segment contains valid data
                               // 2 1 = Sync bit
                               // 3 1 = Startup flag
                               // 4 1 = Payload preamble bit
                               // 5 1 = Reserved bit
                               // 6 1 = Error flag(error frame or invalid frame)
                               // 7 Reserved
                               // 15 1 = Async.monitoring has generated this event
                               // 16 1 = Event is a PDU
                               // 17 Valid for PDUs only.The bit is set if the PDU is valid(either if the PDU has no update bit, or the update bit for the PDU was set in the received frame).
                               // 18 Reserved
                               // 19 1 = Raw frame(only valid if PDUs are used in the configuration).A raw frame may contain PDUs in its payload
                               // 20 1 = Dynamic segment	0 = Static segment
                               // 21 This flag is only valid for frames and not for PDUs.	1 = The PDUs in the payload of this frame are logged in separate logging entries. 0 = The PDUs in the payload of this frame must be extracted out of this frame.The logging file does not contain separate  // PDU - entries.
                               // 22 Valid for PDUs only.The bit is set if the PDU has an update bit
	u32 FFrameCRC;             // frame crc
	u64 FReserved1;            // 8 reserved bytes
	u64 FReserved2;            // 8 reserved bytes
	u64 FTimeUs;               // timestamp in us
	u8  FData[254];            // 254 data bytes
    // is_tx -----------------------------------------------------
    PROPERTY(bool, is_tx);
    GET(is_tx){
        return FDir != 0;
    }
    SET(is_tx){
        if (value) {
            FDir = 1;
        } else {
            FDir = 0;
        }
    }
    // is_null ---------------------------------------------------
    PROPERTY(bool, is_null);
    GET(is_null){
        return (FFrameFlags & ((u32)1 << 0)) != 0;
    }
    SET(is_null){
        if (value) {
            FFrameFlags |= ((u32)1 << 0);
        } else {
            FFrameFlags &= ~((u32)1 << 0);
        }
    }
    // is_data ---------------------------------------------------
    PROPERTY(bool, is_data);
    GET(is_data){
        return (FFrameFlags & ((u32)1 << 1)) != 0;
    }
    SET(is_data){
        if (value) {
            FFrameFlags |= ((u32)1 << 1);
        } else {
            FFrameFlags &= ~((u32)1 << 1);
        }
    }
    // is_sync ---------------------------------------------------
    PROPERTY(bool, is_sync);
    GET(is_sync){
        return (FFrameFlags & ((u32)1 << 2)) != 0;
    }
    SET(is_sync){
        if (value) {
            FFrameFlags |= ((u32)1 << 2);
        } else {
            FFrameFlags &= ~((u32)1 << 2);
        }
    }
    // is_startup ------------------------------------------------
    PROPERTY(bool, is_startup);
    GET(is_startup){
        return (FFrameFlags & ((u32)1 << 3)) != 0;
    }
    SET(is_startup){
        if (value) {
            FFrameFlags |= ((u32)1 << 3);
        } else {
            FFrameFlags &= ~((u32)1 << 3);
        }
    }
    // is_pp -----------------------------------------------------
    PROPERTY(bool, is_pp);
    GET(is_pp){
        return (FFrameFlags & ((u32)1 << 4)) != 0;
    }
    SET(is_pp){
        if (value) {
            FFrameFlags |= ((u32)1 << 4);
        } else {
            FFrameFlags &= ~((u32)1 << 4);
        }
    }
    // is_err ----------------------------------------------------
    PROPERTY(bool, is_err);
    GET(is_err){
        return (FFrameFlags & ((u32)1 << 6)) != 0;
    }
    SET(is_err){
        if (value) {
            FFrameFlags |= ((u32)1 << 6);
        } else {
            FFrameFlags &= ~((u32)1 << 6);
        }
    }
    // is_static_segment -----------------------------------------
    PROPERTY(bool, is_static_segment);
    GET(is_static_segment){
        return (FFrameFlags & ((u32)1 << 20)) != 0;
    }
    SET(is_static_segment){
        if (value) {
            FFrameFlags |= ((u32)1 << 20);
        } else {
            FFrameFlags &= ~((u32)1 << 20);
        }
    }
    // initialize with slot id -----------------------------------
    void init_w_slot_id(const s32 ASlotId, const s32 ADLC) {
        FIdxChn = 0;
        FChannelMask = 1;
        FDir = 0;
        FPayloadLength = ADLC;
        FActualPayloadLength = ADLC;
        FCycleNumber = 0;
        FCCType = 5;
        FFrameType = 0;
        FHeaderCRCA = 0;
        FHeaderCRCB = 0;
        FFrameStateInfo = 0;
        FFrameFlags = 1 << 1; // data frame
        FSlotId = ASlotId;
        FFrameCRC = 0;
        FReserved1 = 0;
        FReserved2 = 0;
        FTimeUs = 0;
        for (u32 i = 0; i < 254; i++) {
            FData[i] = 0;
        }
    }
    // load data bytes -------------------------------------------
    void load_data(u8* a) {
        for (u32 i = 0; i < 254; i++) {
            FData[i] = *a++;
        }
    }
} TFlexRay, *PFlexRay;

// Generic definitions ===========================================
typedef void (__stdcall* TProcedure)(const void* AObj);
typedef void (__stdcall* TProcedureSetInt)(const void* AObj, const s32 AValue);
typedef s32 (__stdcall* TIntFunction)(const void* AObj);
typedef void (__stdcall* TProcedureSetDouble)(const void* AObj, const double AValue);
typedef double (__stdcall* TDoubleFunction)(const void* AObj);
typedef void (__stdcall* TProcedureSetString)(const void* AObj, const char* AValue);
typedef char* (__stdcall* TStringFunction)(const void* AObj);
typedef void (__stdcall* TProcedureSetCAN)(const void* AObj, const PCAN AValue);
typedef TCAN (__stdcall* TTCANFunction)(const void* AObj);
typedef void (__stdcall* TProcedureSetCANFD)(const void* AObj, const PCANFD AValue);
typedef TCANFD (__stdcall* TTCANFDFunction)(const void* AObj);
typedef void (__stdcall* TProcedureSetLIN)(const void* AObj, const PLIN AValue);
typedef TLIN (__stdcall* TTLINFunction)(const void* AObj);
typedef void(__stdcall* TWriteAPIDocumentFunc)(const void* AOpaque, const char* AName, const char* AGroup, const char* ADesc, const char* AExample, const s32 AParaCount);
typedef void(__stdcall* TWriteAPIParaFunc)(const void* AOpaque, const s32 AIdx, const char* AAPIName, const char* AParaName, const bool AIsConst, const char* AParaType, const char* ADesc);                            

// TSMaster variable =============================================
typedef struct _TMPVarInt {
    void* FObj;
    TIntFunction internal_get;
    TProcedureSetInt internal_set;
    s32 get(void) {
        return internal_get(FObj);
    }
    void set(const s32 AValue) {
        internal_set(FObj, AValue);
    }
}TMPVarInt;

typedef struct _TMPVarDouble {
    void* FObj;
    TDoubleFunction internal_get;
    TProcedureSetDouble internal_set;
    double get(void) {
        return internal_get(FObj);
    }
    void set(const double AValue) {
        internal_set(FObj, AValue);
    }
}TMPVarDouble;

typedef struct _TMPVarString {
    void* FObj;
    TStringFunction internal_get;
    TProcedureSetString internal_set;
    char* get(void) {
        return internal_get(FObj);
    }
    void set(const char* AValue) {
        internal_set(FObj, AValue);
    }
}TMPVarString;

typedef struct _TMPVarCAN {
    void* FObj;
    TTCANFunction internal_get;
    TProcedureSetCAN internal_set;
    TCAN get(void) {
        return internal_get(FObj);
    }
    void set(TCAN AValue) {
        internal_set(FObj, &AValue);
    }
}TMPVarCAN;

typedef struct _TMPVarCANFD {
    void* FObj;
    TTCANFDFunction internal_get;
    TProcedureSetCANFD internal_set;
    TCANFD get(void) {
        return internal_get(FObj);
    }
    void set(TCANFD AValue) {
        internal_set(FObj, &AValue);
    }
}TMPVarCANFD;

typedef struct _TMPVarLIN {
    void* FObj;
    TTLINFunction internal_get;
    TProcedureSetLIN internal_set;
    TLIN get(void) {
        return internal_get(FObj);
    }
    void set(TLIN AValue) {
        internal_set(FObj, &AValue);
    }
}TMPVarLIN;

// TSMaster timer ================================================
typedef struct _TMPTimerMS {
    void* FObj;
    TProcedure internal_start;
    TProcedure internal_stop;
    TProcedureSetInt internal_set_interval;
    TIntFunction internal_get_interval;
    void start(void) {
        internal_start(FObj);
    }
    void stop(void) {
        internal_stop(FObj);
    }
    void set_interval(const s32 AInterval) {
        internal_set_interval(FObj, AInterval);
    }
    s32 get_interval(void) {
        return internal_get_interval(FObj);
    }
}TMPTimerMS;

// TSMaster application definition ===============================
#define APP_DEVICE_NAME_LENGTH 32
typedef enum _TLIBBusToolDeviceType{
    BUS_UNKNOWN_TYPE           = 0, 
    TS_TCP_DEVICE              = 1, 
    XL_USB_DEVICE              = 2, 
    TS_USB_DEVICE              = 3, 
    PEAK_USB_DEVICE            = 4,
    KVASER_USB_DEVICE          = 5,
    ZLG_USB_DEVICE             = 6,
    ICS_USB_DEVICE             = 7,
    TS_TC1005_DEVICE           = 8,
    CANABLE_USB_DEVICE         = 9
} TLIBBusToolDeviceType;
typedef enum _TLIBApplicationChannelType{APP_CAN = 0, APP_LIN = 1, APP_FlexRay = 2, APP_Ethernet = 3} TLIBApplicationChannelType;
typedef enum _TReplayPhase{rppInit = 0, rppReplaying, rppEnded} TReplayPhase;
typedef enum _TLIBCANBusStatistics{
    cbsBusLoad = 0, cbsPeakLoad, cbsFpsStdData, cbsAllStdData,
    cbsFpsExtData, cbsAllExtData, cbsFpsStdRemote, cbsAllStdRemote,
    cbsFpsExtRemote, cbsAllExtRemote, cbsFpsErrorFrame, cbsAllErrorFrame    
} TLIBCANBusStatistics;
struct _TLIBTSMapping {
    char                       FAppName[APP_DEVICE_NAME_LENGTH];
    s32                        FAppChannelIndex;
    TLIBApplicationChannelType FAppChannelType;
    TLIBBusToolDeviceType      FHWDeviceType;
    s32                        FHWIndex;
    s32                        FHWChannelIndex;
    s32                        FHWDeviceSubType;
    char                       FHWDeviceName[APP_DEVICE_NAME_LENGTH];
    bool                       FMappingDisabled;
    void init(void) {
        s32 i;
        for (i = 0; i < APP_DEVICE_NAME_LENGTH; i++) {
            FAppName[i] = 0;
            FHWDeviceName[i] = 0;
        }
        FAppChannelIndex = 0;
        FAppChannelType = APP_CAN;
        FHWDeviceType = TS_USB_DEVICE;
        FHWIndex = 0;
        FHWChannelIndex = 0;
        FHWDeviceSubType = 0;
        FMappingDisabled = false;
    }
};
typedef struct _TLIBTSMapping TLIBTSMapping, * PLIBTSMapping;
// system var def
typedef enum _TLIBSystemVarType{svtInt32 = 0, svtUInt32, svtInt64, svtUInt64, svtUInt8Array,
    svtInt32Array, svtInt64Array, svtDouble, svtDoubleArray, svtString} TLIBSystemVarType;
typedef struct {
    char              FName[APP_DEVICE_NAME_LENGTH];
    char              FCategory[APP_DEVICE_NAME_LENGTH];
    char              FComment[APP_DEVICE_NAME_LENGTH];
    TLIBSystemVarType FDataType;
    bool              FIsReadOnly;
    double            FValueMin;
    double            FValueMax;
    char              FUnit[APP_DEVICE_NAME_LENGTH];
} TLIBSystemVarDef, *PLIBSystemVarDef;
typedef enum _TCANFDControllerType{fdtCAN = 0, fdtISOCANFD = 1, fdtNonISOCANFD = 2} TCANFDControllerType;
typedef enum _TCANFDControllerMode{fdmNormal = 0, fdmACKOff = 1, fdmRestricted = 2} TCANFDControllerMode;
// log def
typedef enum _TLIBOnlineReplayTimingMode{ortImmediately = 0, ortAsLog = 1, ortDelayed = 2} TLIBOnlineReplayTimingMode;
typedef enum _TLIBOnlineReplayStatus{orsNotStarted = 0, orsRunning = 1, orsPaused = 2, orsCompleted = 3, orsTerminated = 4} TLIBOnlineReplayStatus;
typedef enum _TSupportedBLFObjType {sotCAN = 0, sotLIN = 1, sotCANFD = 2, sotRealtimeComment = 3, sotSystemVar = 4, sotFlexRay = 5, sotEthernet = 6} TSupportedBLFObjType;
// database utilities
#define DATABASE_STR_LEN 512
// CAN signal record, size = 26
typedef struct _TCANSignal{
    u8     FCANSgnType; // 0 - Unsigned, 1 - Signed, 2 - Single 32, 3 - Double 64
    bool   FIsIntel;
    s32    FStartBit;
    s32    FLength;    
    double FFactor;
    double FOffset;    
} TCANSignal, *PCANSignal;
// LIN signal record, size = 26
typedef struct _TLINSignal{
    u8     FLINSgnType; // 0 - Unsigned, 1 - Signed, 2 - Single 32, 3 - Double 64
    bool   FIsIntel;
    s32    FStartBit;
    s32    FLength;    
    double FFactor;
    double FOffset;    
} TLINSignal, *PLINSignal;
// FlexRay signal record, size = 32
typedef struct _TFlexRaySignal{
    u8     FFRSgnType;   // 0 - Unsigned, 1 - Signed, 2 - Single 32, 3 - Double 64
    u8     FCompuMethod; // 0 - Identical, 1 - Linear, 2 - Scale Linear, 3 - TextTable, 4 - TABNoIntp, 5 - Formula
    u8     FReserved;
    bool   FIsIntel;
    s32    FStartBit;
    s32    FUpdateBit;
    s32    FLength;
    double FFactor;
    double FOffset;
} TFlexRaySignal, *PFlexRaySignal;
#define CANMsgDecl(typ, name, chn, prop, dlc, id) const typ name = {{chn, prop, dlc, 0, id, 0, {0}}};
#define CANFDMsgDecl(typ, name, chn, prop, dlc, id) const typ name = {{chn, prop, dlc, 1, id, 0, {0}}};
#define FlexRayFrameDecl(typ, name, chn, chnmask, prop, dlc, cycle, slot) const typ name = {{chn, chnmask, 0, dlc, dlc, cycle, 5, 0, 0, 0, 0, slot, prop, 0, 0, 0, 0, {0}}};
#define LINMsgDecl(typ, name, chn, prop, dlc, id) const typ name = {{chn, 0, prop, dlc, id, 0, 0, 0, {0}}};
#define CANSgnDecl(name, typ, isIntel, startBit, len, factor, offset) const TCANSignal name = {typ, isIntel, startBit, len, factor, offset};
#define FlexRaySgnDecl(name, typ, isIntel, compuMethod, startBit, updateBit, len, factor, offset) const TFlexRaySignal name = {typ, compuMethod, 0, isIntel, startBit, updateBit, len, factor, offset};
typedef enum _TSignalType {stCANSignal, stLINSignal, stSystemVar, stFlexRay, stEthernet} TSignalType;
typedef enum _TSignalCheckKind {sckAlways, sckAppear, sckStatistics, sckRisingEdge, sckFallingEdge, sckMonotonyRising, sckMonotonyFalling, sckFollow, sckJump, sckNoChange} TSignalCheckKind;
typedef enum _TSignalStatisticsKind {sskMin, sskMax, sskAverage} TSignalStatisticsKind;
typedef enum _TLIBRBSInitValueOptions{rivUseDB = 0, rivUseLast, rivUse0} TLIBRBSInitValueOptions;
typedef enum _TSymbolMappingDirection{smdBiDirection = 0, smdSgnToSysVar, smdSysVarToSgn} TSymbolMappingDirection;
typedef void(__stdcall* TProgressCallback)(const void* AObj, const double AProgress100);
typedef bool(__stdcall* TCheckResultCallback)(void);
// TDBProperties for database properties, size = 1048
typedef struct _TDBProperties {
    s32 FDBIndex;
    s32 FSignalCount;
    s32 FFrameCount;
    s32 FECUCount;
    u64 FSupportedChannelMask;
    char FName[DATABASE_STR_LEN];
    char FComment[DATABASE_STR_LEN];
} TDBProperties, *PDBProperties;
// TDBECUProperties for database ECU properties, size = 1040
typedef struct _TDBECUProperties {
    s32 FDBIndex;
    s32 FECUIndex;
    s32 FTxFrameCount;
    s32 FRxFrameCount;
    char FName[DATABASE_STR_LEN];
    char FComment[DATABASE_STR_LEN];
} TDBECUProperties, *PDBECUProperties;
// TDBFrameProperties for database Frame properties, size = 1088
typedef struct _TDBFrameProperties {
    s32 FDBIndex;
    s32 FECUIndex;
    s32 FFrameIndex;
    u8  FIsTx;    
    u8  FReserved1;
    u8  FReserved2;
    u8  FReserved3;
    TSignalType FFrameType;
    // CAN
    u8  FCANIsDataFrame;
    u8  FCANIsStdFrame;
    u8  FCANIsEdl;
    u8  FCANIsBrs;
    s32 FCANIdentifier;
    s32 FCANDLC;
    s32 FCANDataBytes;
    // LIN
    s32 FLINIdentifier;
    s32 FLINDLC;
    // FlexRay
    u8  FFRChannelMask;
    u8  FFRBaseCycle;
    u8  FFRCycleRepetition;
    u8  FFRIsStartupFrame;
    u16 FFRSlotId;  
    u16 FFRDLC;
    u64 FFRCycleMask;
    s32 FSignalCount;
    char FName[DATABASE_STR_LEN];
    char FComment[DATABASE_STR_LEN];
} TDBFrameProperties, *PDBFrameProperties;
// TDBSignalProperties for database signal properties, size = 1144
typedef struct _TDBSignalProperties {
    s32 FDBIndex;
    s32 FECUIndex;
    s32 FFrameIndex;
    s32 FSignalIndex;
    u8  FIsTx;    
    u8  FReserved1;
    u8  FReserved2;
    u8  FReserved3;
    TSignalType    FSignalType;    
    TCANSignal     FCANSignal;
    TLINSignal     FLINSignal;
    TFlexRaySignal FFlexRaySignal;
    s32            FParentFrameId;
    double         FInitValue;
    char FName[DATABASE_STR_LEN];
    char FComment[DATABASE_STR_LEN];
} TDBSignalProperties, *PDBSignalProperties;
// Realtime comment
typedef struct _realtime_comment_t {
	s64 FTimeUs;
	s32 FEventType;
	u32 FCapacity;
	char* FComment;
} Trealtime_comment_t, *Prealtime_comment_t;
// IP
typedef void(__stdcall* TOnIoIPData)(const pu8 APointer, const s32 ASize);
// Automation Module
typedef enum _TAutomationModuleRunningState {amrsNotRun, amrsPrepareRun, amrsRunning, amrsPaused, amrsStepping, amrsFinished} TAutomationModuleRunningState, *PAutomationModuleRunningState;
// stim
typedef enum _TSTIMSignalStatus {sssStopped, sssRunning, sssPaused} TSTIMSignalStatus, *PSTIMSignalStatus;

// =========================== APP ===========================
typedef s32 (__stdcall* TTSAppSetCurrentApplication)(const char* AAppName);
typedef s32 (__stdcall* TTSAppGetCurrentApplication)(char** AAppName);
typedef s32 (__stdcall* TTSAppDelApplication)(const char* AAppName);
typedef s32 (__stdcall* TTSAppAddApplication)(const char* AAppName);
typedef s32 (__stdcall* TTSAppGetApplicationList)(char** AAppNameList);
typedef s32 (__stdcall* TTSAppSetCANChannelCount)(const s32 ACount);
typedef s32 (__stdcall* TTSAppSetLINChannelCount)(const s32 ACount);
typedef s32 (__stdcall* TTSAppGetCANChannelCount)(const ps32 ACount);
typedef s32 (__stdcall* TTSAppGetLINChannelCount)(const ps32 ACount);
typedef s32 (__stdcall* TTSAppGetFlexRayChannelCount)(const ps32 ACount);
typedef s32 (__stdcall* TTSAppSetFlexRayChannelCount)(const s32 ACount);
typedef s32 (__stdcall* TTSAppSetMapping)(const PLIBTSMapping AMapping);
typedef s32 (__stdcall* TTSAppGetMapping)(const PLIBTSMapping AMapping);
typedef s32 (__stdcall* TTSAppDeleteMapping)(const PLIBTSMapping AMapping);
typedef s32 (__stdcall* TTSAppConnectApplication)(void);
typedef s32 (__stdcall* TTSAppDisconnectApplication)(void);
typedef s32 (__stdcall* TTSAppIsConnected)(void);
typedef s32 (__stdcall* TTSAppLogger)(const char* AStr, const TLogLevel ALevel);
typedef s32 (__stdcall* TTSDebugLog)(const void* AObj, const char* AFile, const char* AFunc, const s32 ALine, const char* AStr, const TLogLevel ALevel);
typedef s32 (__stdcall* TTSAppSetTurboMode)(const bool AEnable);
typedef s32 (__stdcall* TTSAppGetTurboMode)(const bool* AEnable);
typedef s32 (__stdcall* TTSAppGetErrorDescription)(const s32 ACode, char** ADesc);
typedef s32 (__stdcall* TTSAppConfigureBaudrateCAN)(const s32 AIdxChn, const float ABaudrateKbps, const bool AListenOnly, const bool AInstallTermResistor120Ohm);
typedef s32 (__stdcall* TTSAppConfigureBaudrateCANFD)(const s32 AIdxChn, const float ABaudrateArbKbps, const float ABaudrateDataKbps, const TCANFDControllerType AControllerType, const TCANFDControllerMode AControllerMode, const bool AInstallTermResistor120Ohm);
typedef s32 (__stdcall* TTSAppTerminate)(const void* AObj);
typedef s32 (__stdcall* TTSWaitTime)(const void* AObj, const s32 ATimeMs, const char* AMsg);
typedef s32 (__stdcall* TTSCheckError)(const void* AObj, const s32 AErrorCode);
typedef s32 (__stdcall* TTSStartLog)(const void* AObj);
typedef s32 (__stdcall* TTSEndLog)(const void* AObj);
typedef s32 (__stdcall* TTSCheckTerminate)(const void* AObj);
typedef s32 (__stdcall* TTSGetTimestampUs)(s64* ATimestamp);
typedef s32 (__stdcall* TTSShowConfirmDialog)(const char* ATitle, const char* APrompt, const char* AImage, const s32 ATimeoutMs, const bool ADefaultOK);
typedef s32 (__stdcall* TTSPause)(void);
typedef s32 (__stdcall* TTSSetCheckFailedTerminate)(const void* AObj, const s32 AToTerminate);
typedef s32 (__stdcall* TTSAppSplitString)(const char* ASplitter, const char* AStr, char** AArray, const s32 ASingleStrSize, const s32 AArraySize, s32* AActualCount);
typedef s32 (__stdcall* TTSAppGetConfigurationFileName)(char** AFileName);
typedef s32 (__stdcall* TTSAppGetConfigurationFilePath)(char** AFilePath);
typedef s32 (__stdcall* TTSAppSetDefaultOutputDir)(const char* APath);
typedef s32 (__stdcall* TTSAppSaveScreenshot)(const char* AFormCaption, const char* AFilePath);
typedef s32 (__stdcall* TTSAppRunForm)(const char* AFormCaption);
typedef s32 (__stdcall* TTSAppStopForm)(const char* AFormCaption);
typedef s32 (__stdcall* TClearMeasurementForm)(const char* AFormCaption);
// system var def
typedef s32 (__stdcall* TTSAppGetSystemVarCount)(s32* AInternalCount, s32* AUserCount);
typedef s32 (__stdcall* TTSAppGetSystemVarDefByIndex)(const bool AIsUser, const s32 AIndex, const PLIBSystemVarDef AVarDef);
typedef s32 (__stdcall* TTSAppFindSystemVarDefByName)(const bool AIsUser, const char* ACompleteName, const PLIBSystemVarDef AVarDef);
typedef s32 (__stdcall* TTSAppCreateSystemVar)(const char* ACompleteName, const TLIBSystemVarType AType, const char* ADefaultValue, const char* AComment);
typedef s32 (__stdcall* TTSAppDeleteSystemVar)(const char* ACompleteName);
typedef s32 (__stdcall* TTSAppSetSystemVarUnit)(const char* ACompleteName, const char* AUnit);
typedef s32 (__stdcall* TTSAppSetSystemVarValueTable)(const char* ACompleteName, const char* ATable);
typedef s32 (__stdcall* TTSAppGetSystemVarAddress)(const char* ACompleteName, ps32 AAddress);
typedef s32 (__stdcall* TTSAppSetSystemVarLogging)(const char* ACompleteName, const bool AIsLogging);
typedef s32 (__stdcall* TTSAppGetSystemVarLogging)(const char* ACompleteName, bool* AIsLogging);
typedef s32 (__stdcall* TTSAppLogSystemVarValue)(const void* AObj, const char* ACompleteName);
// system var get
typedef s32 (__stdcall* TTSAppGetSystemVarDouble)(const char* ACompleteName, double* AValue);
typedef s32 (__stdcall* TTSAppGetSystemVarInt32)(const char* ACompleteName, s32* AValue);
typedef s32 (__stdcall* TTSAppGetSystemVarUInt32)(const char* ACompleteName, u32* AValue);
typedef s32 (__stdcall* TTSAppGetSystemVarInt64)(const char* ACompleteName, s64* AValue);
typedef s32 (__stdcall* TTSAppGetSystemVarUInt64)(const char* ACompleteName, u64* AValue);
typedef s32 (__stdcall* TTSAppGetSystemVarUInt8Array)(const char* ACompleteName, const s32 ACapacity, s32* AVarCount, u8* AValue);
typedef s32 (__stdcall* TTSAppGetSystemVarInt32Array)(const char* ACompleteName, const s32 ACapacity, s32* AVarCount, s32* AValue);
typedef s32 (__stdcall* TTSAppGetSystemVarInt64Array)(const char* ACompleteName, const s32 ACapacity, s32* AVarCount, s64* AValue);
typedef s32 (__stdcall* TTSAppGetSystemVarDoubleArray)(const char* ACompleteName, const s32 ACapacity, s32* AVarCount, double* AValue);
typedef s32 (__stdcall* TTSAppGetSystemVarString)(const char* ACompleteName, const s32 ACapacity, char* AString);
typedef s32 (__stdcall* TTSAppGetSystemVarGerneric)(const char* ACompleteName, const s32 ACapacity, char* AValue);
typedef s32 (__stdcall* TTSWaitSystemVariable)(const char* ACompleteName, const char* AValue, const s32 ATimeoutMs);
// system var sync set
typedef s32 (__stdcall* TTSAppSetSystemVarDouble)(const char* ACompleteName, double AValue);
typedef s32 (__stdcall* TTSAppSetSystemVarInt32)(const char* ACompleteName, s32 AValue);
typedef s32 (__stdcall* TTSAppSetSystemVarUInt32)(const char* ACompleteName, u32 AValue);
typedef s32 (__stdcall* TTSAppSetSystemVarInt64)(const char* ACompleteName, s64 AValue);
typedef s32 (__stdcall* TTSAppSetSystemVarUInt64)(const char* ACompleteName, u64 AValue);
typedef s32 (__stdcall* TTSAppSetSystemVarUInt8Array)(const char* ACompleteName, const s32 ACapacity, u8* AValue);
typedef s32 (__stdcall* TTSAppSetSystemVarInt32Array)(const char* ACompleteName, const s32 ACapacity, s32* AValue);
typedef s32 (__stdcall* TTSAppSetSystemVarInt64Array)(const char* ACompleteName, const s32 ACapacity, s64* AValue);
typedef s32 (__stdcall* TTSAppSetSystemVarDoubleArray)(const char* ACompleteName, const s32 ACapacity, double* AValue);
typedef s32 (__stdcall* TTSAppSetSystemVarString)(const char* ACompleteName, char* AString);
typedef s32 (__stdcall* TTSAppSetSystemVarGeneric)(const char* ACompleteName, char* AValue);
// system var async set
typedef s32 (__stdcall* TTSAppSetSystemVarDoubleAsync)(const char* ACompleteName, double AValue);
typedef s32 (__stdcall* TTSAppSetSystemVarInt32Async)(const char* ACompleteName, s32 AValue);
typedef s32 (__stdcall* TTSAppSetSystemVarUInt32Async)(const char* ACompleteName, u32 AValue);
typedef s32 (__stdcall* TTSAppSetSystemVarInt64Async)(const char* ACompleteName, s64 AValue);
typedef s32 (__stdcall* TTSAppSetSystemVarUInt64Async)(const char* ACompleteName, u64 AValue);
typedef s32 (__stdcall* TTSAppSetSystemVarUInt8ArrayAsync)(const char* ACompleteName, const s32 ACapacity, u8* AValue);
typedef s32 (__stdcall* TTSAppSetSystemVarInt32ArrayAsync)(const char* ACompleteName, const s32 ACapacity, s32* AValue);
typedef s32 (__stdcall* TTSAppSetSystemVarInt64ArrayAsync)(const char* ACompleteName, const s32 ACapacity, s64* AValue);
typedef s32 (__stdcall* TTSAppSetSystemVarDoubleArrayAsync)(const char* ACompleteName, const s32 ACapacity, double* AValue);
typedef s32 (__stdcall* TTSAppSetSystemVarStringAsync)(const char* ACompleteName, char* AString);
typedef s32 (__stdcall* TTSAppSetSystemVarGenericAsync)(const char* ACompleteName, char* AValue);
// system var utils
typedef s32 (__stdcall* TTSAppLogSystemVar)(const char* ACompleteName);
typedef s32 (__stdcall* TTSAppWaitSystemVarExistance)(const char* ACompleteName, const s32 ATimeOutMs);
typedef s32 (__stdcall* TTSAppWaitSystemVarDisappear)(const char* ACompleteName, const s32 ATimeOutMs);
// excel
typedef s32 (__stdcall* Texcel_load)(const char* AFileName, void** AObj);
typedef s32 (__stdcall* Texcel_get_sheet_count)(const void* AObj, s32* ACount);
typedef s32 (__stdcall* Texcel_set_sheet_count)(const void* AObj, const s32 ACount);
typedef s32 (__stdcall* Texcel_get_sheet_name)(const void* AObj, const s32 AIdxSheet, char** AName);
typedef s32 (__stdcall* Texcel_set_sheet_name)(const void* AObj, const s32 AIdxSheet, const char* AName);
typedef s32 (__stdcall* Texcel_get_cell_count)(const void* AObj, const s32 AIdxSheet, s32* ARowCount, s32* AColCount);
typedef s32 (__stdcall* Texcel_get_cell_value)(const void* AObj, const s32 AIdxSheet, const s32 AIdxRow, const s32 AIdxCol, char** AValue);
typedef s32 (__stdcall* Texcel_set_cell_count)(const void* AObj, const s32 AIdxSheet, const s32 ARowCount, const s32 AColCount);
typedef s32 (__stdcall* Texcel_set_cell_value)(const void* AObj, const s32 AIdxSheet, const s32 AIdxRow, const s32 AIdxCol, char* AValue);
typedef s32 (__stdcall* Texcel_unload)(const void* AObj);
typedef s32 (__stdcall* Texcel_unload_all)(void);
// text file write
typedef s32 (__stdcall* TWriteTextFileStart)(const char* AFileName, s32* AHandle);
typedef s32 (__stdcall* TWriteTextFileLine)(const s32 AHandle, const char* ALine);
typedef s32 (__stdcall* TWriteTextFileLineWithDoubleArray)(const s32 AHandle, const double* AArray, const s32 ACount);
typedef s32 (__stdcall* TWriteTextFileLineWithStringArray)(const s32 AHandle, const char** AArray, const s32 ACount);
typedef s32 (__stdcall* TWriteTextFileEnd)(const s32 AHandle);
// text file read
typedef s32 (__stdcall* TReadTextFileStart)(const char* AFileName, s32* AHandle);
typedef s32 (__stdcall* TReadTextFileLine)(const s32 AHandle, const s32 ACapacity, ps32 AReadCharCount, char* ALine);
typedef s32 (__stdcall* TReadTextFileEnd)(const s32 AHandle);
// mat file
typedef s32 (__stdcall* TWriteMatFileStart)(const char* AFileName, s32* AHandle);
typedef s32 (__stdcall* TWriteMatFileVariableDouble)(const s32 AHandle, const char* AVarName, const double AValue);
typedef s32 (__stdcall* TWriteMatFileVariableString)(const s32 AHandle, const char* AVarName, const char* AValue);
typedef s32 (__stdcall* TWriteMatFileVariableDoubleArray)(const s32 AHandle, const char* AVarName, const double* AArray, const s32 ACount);
typedef s32 (__stdcall* TWriteMatFileEnd)(const s32 AHandle);
typedef s32 (__stdcall* TReadMatFileStart)(const char* AFileName, s32* AHandle);
typedef s32 (__stdcall* TReadMatFileVariableCount)(const s32 AHandle, const char* AVarName, ps32 ACount);
typedef s32 (__stdcall* TReadMatFileVariableString)(const s32 AHandle, const char* AVarName, char* AValue, const s32 ACapacity);
typedef s32 (__stdcall* TReadMatFileVariableDouble)(const s32 AHandle, const char* AVarName, const double* AValue, const s32 AStartIdx, const s32 ACount);
typedef s32 (__stdcall* TReadMatFileEnd)(const s32 AHandle);
// ini file
typedef s32 (__stdcall* TIniCreate)(const char* AFileName, s32* AHandle);
typedef s32 (__stdcall* TIniWriteInt32)(const s32 AHandle, const char* ASection, const char* AKey, const s32 AValue);
typedef s32 (__stdcall* TIniWriteInt64)(const s32 AHandle, const char* ASection, const char* AKey, const s64 AValue);
typedef s32 (__stdcall* TIniWriteBool)(const s32 AHandle, const char* ASection, const char* AKey, const bool AValue);
typedef s32 (__stdcall* TIniWriteFloat)(const s32 AHandle, const char* ASection, const char* AKey, const double AValue);
typedef s32 (__stdcall* TIniWriteString)(const s32 AHandle, const char* ASection, const char* AKey, const char* AValue);
typedef s32 (__stdcall* TIniReadInt32)(const s32 AHandle, const char* ASection, const char* AKey, const s32* AValue, const s32 ADefault);
typedef s32 (__stdcall* TIniReadInt64)(const s32 AHandle, const char* ASection, const char* AKey, const s64* AValue, const s64 ADefault);
typedef s32 (__stdcall* TIniReadBool)(const s32 AHandle, const char* ASection, const char* AKey, const bool* AValue, const bool ADefault);
typedef s32 (__stdcall* TIniReadFloat)(const s32 AHandle, const char* ASection, const char* AKey, const double* AValue, const double ADefault);
typedef s32 (__stdcall* TIniReadString)(const s32 AHandle, const char* ASection, const char* AKey, const char* AValue, s32* ACapacity, const char* ADefault);
typedef s32 (__stdcall* TIniSectionExists)(const s32 AHandle, const char* ASection);
typedef s32 (__stdcall* TIniKeyExists)(const s32 AHandle, const char* ASection, const char* AKey);
typedef s32 (__stdcall* TIniDeleteKey)(const s32 AHandle, const char* ASection, const char* AKey);
typedef s32 (__stdcall* TIniDeleteSection)(const s32 AHandle, const char* ASection);
typedef s32 (__stdcall* TIniClose)(const s32 AHandle);
// automation module
typedef s32 (__stdcall* TAMGetRunningState)(const char* AModuleName, PAutomationModuleRunningState AState, char** ASubModuleName, char** ACurrentParameterGroupName);
typedef s32 (__stdcall* TAMRun)(const char* AModuleName, const char* ASubModuleName, const char* AParameterGroupName, const bool AIsSync);
typedef s32 (__stdcall* TAMStop)(const char* AModuleName, const bool AIsSync);
typedef s32 (__stdcall* TAMSelectSubModule)(const bool AIsSelect, const char* AModuleName, const char* ASubModuleName, const char* AParameterGroupName);
// panel set
typedef s32 (__stdcall* TPanelSetEnable)(const char* APanelName, const char* AControlName, const bool AEnable);
typedef s32 (__stdcall* TPanelSetPositionX)(const char* APanelName, const char* AControlName, const float AX);
typedef s32 (__stdcall* TPanelSetPositionY)(const char* APanelName, const char* AControlName, const float AY);
typedef s32 (__stdcall* TPanelSetPositionXY)(const char* APanelName, const char* AControlName, const float AX, const float AY);
typedef s32 (__stdcall* TPanelSetOpacity)(const char* APanelName, const char* AControlName, const float AOpacity);
typedef s32 (__stdcall* TPanelSetWidth)(const char* APanelName, const char* AControlName, const float AWidth);
typedef s32 (__stdcall* TPanelSetHeight)(const char* APanelName, const char* AControlName, const float AHeight);
typedef s32 (__stdcall* TPanelSetWidthHeight)(const char* APanelName, const char* AControlName, const float AWidth, const float AHeight);
typedef s32 (__stdcall* TPanelSetRotationAngle)(const char* APanelName, const char* AControlName, const float AAngleDegree);
typedef s32 (__stdcall* TPanelSetRotationCenter)(const char* APanelName, const char* AControlName, const float ARatioX, const float ARatioY);
typedef s32 (__stdcall* TPanelSetScaleX)(const char* APanelName, const char* AControlName, const float AScaleX);
typedef s32 (__stdcall* TPanelSetScaleY)(const char* APanelName, const char* AControlName, const float AScaleY);
typedef s32 (__stdcall* TPanelSetBkgdColor)(const char* APanelName, const char* AControlName, const u32 AAlphaColor);
typedef s32 (__stdcall* TPanelSetSelectorItems)(const char* APanelName, const char* AControlName, const char* AItemsList);
// panel get
typedef s32 (__stdcall* TPanelGetEnable)(const char* APanelName, const char* AControlName, bool* AEnable);
typedef s32 (__stdcall* TPanelGetPositionXY)(const char* APanelName, const char* AControlName, float* AX, float* AY);
typedef s32 (__stdcall* TPanelGetOpacity)(const char* APanelName, const char* AControlName, float* AOpacity);
typedef s32 (__stdcall* TPanelGetWidthHeight)(const char* APanelName, const char* AControlName, float* AWidth, float* AHeight);
typedef s32 (__stdcall* TPanelGetRotationAngle)(const char* APanelName, const char* AControlName, float* AAngleDegree);
typedef s32 (__stdcall* TPanelGetRotationCenter)(const char* APanelName, const char* AControlName, float* ARatioX, float* ARatioY);
typedef s32 (__stdcall* TPanelGetScaleXY)(const char* APanelName, const char* AControlName, float* AScaleX, float* AScaleY);
typedef s32 (__stdcall* TPanelGetBkgdColor)(const char* APanelName, const char* AControlName, pu32 AAlphaColor);
typedef s32 (__stdcall* TPanelGetSelectorItems)(const char* APanelName, const char* AControlName, char** AItemsList);
// stim
typedef s32 (__stdcall* TSTIMSetSignalStatus)(const char* ASTIMName, const char* AUserLabel, TSTIMSignalStatus AStatus);
typedef s32 (__stdcall* TSTIMGetSignalStatus)(const char* ASTIMName, const char* AUserLabel, PSTIMSignalStatus AStatus);
// Atomic
typedef s32 (__stdcall* TAtomicIncrement32)(const ps32 AAddr, const s32 AValue, ps32 AResult);
typedef s32 (__stdcall* TAtomicIncrement64)(const ps64 AAddr, const s64 AValue, ps64 AResult);
typedef s32 (__stdcall* TAtomicSet32)(const ps32 AAddr, const s32 AValue);
typedef s32 (__stdcall* TAtomicSet64)(const ps64 AAddr, const s64 AValue);
// symbol mapping
typedef s32 (__stdcall* TAddDirectMappingCAN)(const char* ADestinationVarName, const char* ASignalAddress, const TSymbolMappingDirection ADirection);
typedef s32 (__stdcall* TAddDirectMappingWithFactorOffsetCAN)(const char* ADestinationVarName, const char* ASignalAddress, const TSymbolMappingDirection ADirection, const double AFactor, const double AOffset);
typedef s32 (__stdcall* TAddExpressionMapping)(const char* ADestinationVarName, const char* AExpression, const char* AArguments);
typedef s32 (__stdcall* TDeleteSymbolMappingItem)(const char* ADestinationVarName);
typedef s32 (__stdcall* TDeleteSymbolMappingItems)(void);
typedef s32 (__stdcall* TEnableSymbolMappingItem)(const char* ADestinationVarName, const bool AEnable);
typedef s32 (__stdcall* TEnableSymbolMappingEngine)(const bool AEnable);
typedef s32 (__stdcall* TSaveSymbolMappingSettings)(const char* AFileName);
typedef s32 (__stdcall* TLoadSymbolMappingSettings)(const char* AFileName);
// database
typedef s32 (__stdcall* TDBGetCANDBCount)(ps32 ACount);
typedef s32 (__stdcall* TDBGetLINDBCount)(ps32 ACount);
typedef s32 (__stdcall* TDBGetFlexRayDBCount)(ps32 ACount);
typedef s32 (__stdcall* TDBGetCANDBPropertiesByIndex)(PDBProperties AValue);
typedef s32 (__stdcall* TDBGetLINDBPropertiesByIndex)(PDBProperties AValue);
typedef s32 (__stdcall* TDBGetFlexRayDBPropertiesByIndex)(PDBProperties AValue);
typedef s32 (__stdcall* TDBGetCANDBECUPropertiesByIndex)(PDBECUProperties AValue);
typedef s32 (__stdcall* TDBGetLINDBECUPropertiesByIndex)(PDBECUProperties AValue);
typedef s32 (__stdcall* TDBGetFlexRayDBECUPropertiesByIndex)(PDBECUProperties AValue);
typedef s32 (__stdcall* TDBGetCANDBFramePropertiesByIndex)(PDBFrameProperties AValue);
typedef s32 (__stdcall* TDBGetLINDBFramePropertiesByIndex)(PDBFrameProperties AValue);
typedef s32 (__stdcall* TDBGetFlexRayDBFramePropertiesByIndex)(PDBFrameProperties AValue);
typedef s32 (__stdcall* TDBGetCANDBSignalPropertiesByIndex)(PDBSignalProperties AValue);
typedef s32 (__stdcall* TDBGetLINDBSignalPropertiesByIndex)(PDBSignalProperties AValue);
typedef s32 (__stdcall* TDBGetFlexRayDBSignalPropertiesByIndex)(PDBSignalProperties AValue);
typedef s32 (__stdcall* TDBGetCANDBPropertiesByAddress)(const char* AAddr, PDBProperties AValue);
typedef s32 (__stdcall* TDBGetLINDBPropertiesByAddress)(const char* AAddr, PDBProperties AValue);
typedef s32 (__stdcall* TDBGetFlexRayDBPropertiesByAddress)(const char* AAddr, PDBProperties AValue);
typedef s32 (__stdcall* TDBGetCANDBECUPropertiesByAddress)(const char* AAddr, PDBECUProperties AValue);
typedef s32 (__stdcall* TDBGetLINDBECUPropertiesByAddress)(const char* AAddr, PDBECUProperties AValue);
typedef s32 (__stdcall* TDBGetFlexRayDBECUPropertiesByAddress)(const char* AAddr, PDBECUProperties AValue);
typedef s32 (__stdcall* TDBGetCANDBFramePropertiesByAddress)(const char* AAddr, PDBFrameProperties AValue);
typedef s32 (__stdcall* TDBGetLINDBFramePropertiesByAddress)(const char* AAddr, PDBFrameProperties AValue);
typedef s32 (__stdcall* TDBGetFlexRayDBFramePropertiesByAddress)(const char* AAddr, PDBFrameProperties AValue);
typedef s32 (__stdcall* TDBGetCANDBSignalPropertiesByAddress)(const char* AAddr, PDBSignalProperties AValue);
typedef s32 (__stdcall* TDBGetLINDBSignalPropertiesByAddress)(const char* AAddr, PDBSignalProperties AValue);
typedef s32 (__stdcall* TDBGetFlexRayDBSignalPropertiesByAddress)(const char* AAddr, PDBSignalProperties AValue);
// misc
typedef s32 (__stdcall* TTSAppMakeToast)(const char* AString, const TLogLevel ALevel);
typedef s32 (__stdcall* TTSAppMakeToastUntil)(const char* AString, const TLogLevel ALevel, const bool* ACloseCriteria, const bool AUserCanBreak);
typedef s32 (__stdcall* TTSAppMakeToastWithCallback)(const char* AString, const TLogLevel ALevel, const TCheckResultCallback ACallback, const bool AUserCanBreak);
typedef s32 (__stdcall* TTSAppExecutePythonString)(const char* AString, const char* AArguments, const bool AIsSync, const bool AIsX64, char** AResultLog);
typedef s32 (__stdcall* TTSAppExecutePythonScript)(const char* AFilePath, const char* AArguments, const bool AIsSync, const bool AIsX64, char** AResultLog);
typedef s32 (__stdcall* TTSAppExecuteApp)(const char* AAppPath,  const char* AWorkingDir, const char* AParameter, const s32 AWaitTimeMS);
typedef s32 (__stdcall* TTSAppTerminateAppByName)(const char* AImageName);
typedef s32 (__stdcall* TTSAppCallMPAPI)(const char* ALibName, const char* AFuncName, const char* AInParameters, char** AOutParameters);
typedef s32 (__stdcall* TTSAppSetAnalysisTimeRange)(const s64 ATimeStartUs, const s64 ATimeEndUs);
typedef s32 (__stdcall* TTSAppEnableAllGraphics)(const bool AEnable, const char* AExceptCaptions);
typedef s32 (__stdcall* TTSAppGetTSMasterVersion)(ps32 AYear, ps32 AMonth, ps32 ADay, ps32 ABuildNumber);
typedef s32 (__stdcall* TUIShowPageByIndex)(const s32 AIndex);
typedef s32 (__stdcall* TUIShowPageByName)(const char* AName);
typedef s32 (__stdcall* TWriteRealtimeComment)(const void* AObj, const char* AName);
typedef s32 (__stdcall* TTSAppSetThreadPriority)(const void* AObj, const s32 APriority);
typedef s32 (__stdcall* TTSAppForceDirectory)(const char* ADir);
typedef s32 (__stdcall* TTSAppDirectoryExists)(const char* ADir);
typedef s32 (__stdcall* TTSAppOpenDirectoryAndSelectFile)(const char* AFileName);
typedef s32 (__stdcall* TTSMiniDelayCPU)(void);
typedef s32 (__stdcall* TPromptUserInputValue)(const char* APrompt, double* AValue);
typedef s32 (__stdcall* TPromptUserInputString)(const char* APrompt, char* AValue, const s32 ACapacity);
typedef s32 (__stdcall* TTSAppGetDocPath)(char** AFilePath);
typedef s32 (__stdcall* TTSAppGetHWIDString)(char** AIDString);
typedef s32 (__stdcall* TTSAppGetHWIDArray)(pu8 AArray8B);
typedef s32 (__stdcall* TPlaySound)(const bool AIsSync, const char* AWaveFileName);
typedef s32 (__stdcall* TUILoadPlugin)(const char* APluginName);
typedef s32 (__stdcall* TUIUnloadPlugin)(const char* APluginName);
typedef s32 (__stdcall* TUIGetMainWindowHandle)(ps32 AHandle);
typedef s32 (__stdcall* TPrintDeltaTime)(const char* AInfo);
typedef s32 (__stdcall* TGetConstantDouble)(const char* AName, double* AValue);
typedef s32 (__stdcall* TWaitWithDialog)(const void* AObj, const char* ATitle, const char* AMessage, const bool* ApResult, const float* ApProgress100);
typedef s32 (__cdecl* TRunPythonFunction)(const void* AObj, const char* AModuleName, const char* AFuncName, const char* AArgFormat, ...);
typedef char* (__stdcall* TGetCurrentMpName)(const void* AObj);

typedef struct _TTSApp {
    void*                                     FObj;
    // >>> mp app start <<<
    TTSAppSetCurrentApplication               set_current_application;
    TTSAppGetCurrentApplication               get_current_application;
    TTSAppDelApplication                      del_application;
    TTSAppAddApplication                      add_application;
    TTSAppGetApplicationList                  get_application_list;
    TTSAppSetCANChannelCount                  set_can_channel_count;
    TTSAppSetLINChannelCount                  set_lin_channel_count;
    TTSAppGetCANChannelCount                  get_can_channel_count;
    TTSAppGetLINChannelCount                  get_lin_channel_count;
    TTSAppSetMapping                          set_mapping;
    TTSAppGetMapping                          get_mapping;
    TTSAppDeleteMapping                       del_mapping;
    TTSAppConnectApplication                  connect;
    TTSAppDisconnectApplication               disconnect;
    TTSAppLogger                              log_text;
    TTSAppConfigureBaudrateCAN                configure_can_baudrate;
    TTSAppConfigureBaudrateCANFD              configure_canfd_baudrate;
    TTSAppSetTurboMode                        set_turbo_mode;
    TTSAppGetTurboMode                        get_turbo_mode;
    TTSAppGetErrorDescription                 get_error_description;
    TTSAppTerminate                           internal_terminate_application;
    TTSWaitTime                               internal_wait;                 
    TTSCheckError                             internal_check;                
    TTSStartLog                               internal_start_log;            
    TTSEndLog                                 internal_end_log;              
    TTSCheckTerminate                         internal_check_terminate;      
    TTSGetTimestampUs                         get_timestamp;
    TTSShowConfirmDialog                      show_confirm_dialog;
    TTSPause                                  pause;
    TTSSetCheckFailedTerminate                internal_set_check_failed_terminate;
    TTSAppGetSystemVarCount                   get_system_var_count;
    TTSAppGetSystemVarDefByIndex              get_system_var_def_by_index;
    TTSAppFindSystemVarDefByName              get_system_var_def_by_name;
    TTSAppGetSystemVarDouble                  get_system_var_double;
    TTSAppGetSystemVarInt32                   get_system_var_int32;
    TTSAppGetSystemVarUInt32                  get_system_var_uint32;
    TTSAppGetSystemVarInt64                   get_system_var_int64;
    TTSAppGetSystemVarUInt64                  get_system_var_uint64;
    TTSAppGetSystemVarUInt8Array              get_system_var_uint8_array;
    TTSAppGetSystemVarInt32Array              get_system_var_int32_array;
    TTSAppGetSystemVarInt64Array              get_system_var_int64_array;
    TTSAppGetSystemVarDoubleArray             get_system_var_double_array;
    TTSAppGetSystemVarString                  get_system_var_string;
    TTSAppSetSystemVarDouble                  set_system_var_double;
    TTSAppSetSystemVarInt32                   set_system_var_int32;
    TTSAppSetSystemVarUInt32                  set_system_var_uint32;
    TTSAppSetSystemVarInt64                   set_system_var_int64;
    TTSAppSetSystemVarUInt64                  set_system_var_uint64;
    TTSAppSetSystemVarUInt8Array              set_system_var_uint8_array;
    TTSAppSetSystemVarInt32Array              set_system_var_int32_array;
    TTSAppSetSystemVarInt64Array              set_system_var_int64_array;
    TTSAppSetSystemVarDoubleArray             set_system_var_double_array;
    TTSAppSetSystemVarString                  set_system_var_string;
    TTSAppMakeToast                           make_toast;
    TTSAppExecutePythonString                 execute_python_string;
    TTSAppExecutePythonScript                 execute_python_script;
    TTSAppExecuteApp                          execute_app;
    TTSAppTerminateAppByName                  terminate_app_by_name;
    Texcel_load                               excel_load           ;
    Texcel_get_sheet_count                    excel_get_sheet_count;
    Texcel_set_sheet_count                    excel_set_sheet_count;
    Texcel_get_sheet_name                     excel_get_sheet_name ;
    Texcel_get_cell_count                     excel_get_cell_count ;
    Texcel_get_cell_value                     excel_get_cell_value ;
    Texcel_set_cell_count                     excel_set_cell_count ;
    Texcel_set_cell_value                     excel_set_cell_value ;
    Texcel_unload                             excel_unload         ;
    Texcel_unload_all                         excel_unload_all     ;
    TTSAppLogSystemVar                        log_system_var       ;
    Texcel_set_sheet_name                     excel_set_sheet_name ;
    TTSAppCallMPAPI                           call_mini_program_api;
    TTSAppSplitString                         split_string         ;
    TTSAppWaitSystemVarExistance              wait_system_var_existance;
    TTSAppWaitSystemVarDisappear              wait_system_var_disappear;
    TTSAppSetAnalysisTimeRange                set_analysis_time_range;
    TTSAppGetConfigurationFileName            get_configuration_file_name;
    TTSAppGetConfigurationFilePath            get_configuration_file_path;
    TTSAppSetDefaultOutputDir                 set_default_output_dir;
    TTSAppSaveScreenshot                      save_screenshot;
    TTSAppEnableAllGraphics                   enable_all_graphics;
    TTSAppGetTSMasterVersion                  get_tsmaster_version;
    TUIShowPageByIndex                        ui_show_page_by_index;
    TUIShowPageByName                         ui_show_page_by_name;
    TWriteRealtimeComment                     internal_write_realtime_comment;
    TTSAppSetThreadPriority                   internal_set_thread_priority;
    TTSAppGetSystemVarGerneric                get_system_var_generic;
    TTSAppSetSystemVarGeneric                 set_system_var_generic;
    TWriteTextFileStart                       write_text_file_start;
    TWriteTextFileLine                        write_text_file_line;
    TWriteTextFileLineWithDoubleArray         write_text_file_line_double_array;
    TWriteTextFileLineWithStringArray         write_text_file_line_string_array;
    TWriteTextFileEnd                         write_text_file_end;
    TTSAppForceDirectory                      force_directory;
    TTSAppDirectoryExists                     directory_exists;
    TTSAppOpenDirectoryAndSelectFile          open_directory_and_select_file;
    TTSMiniDelayCPU                           mini_delay_cpu;
    TTSWaitSystemVariable                     wait_system_var;
    TWriteMatFileStart                        write_mat_file_start;
    TWriteMatFileVariableDouble               write_mat_file_variable_double;
    TWriteMatFileVariableString               write_mat_file_variable_string;
    TWriteMatFileVariableDoubleArray          write_mat_file_variable_double_array;
    TWriteMatFileEnd                          write_mat_file_end;
    TReadMatFileStart                         read_mat_file_start;
    TReadMatFileVariableCount                 read_mat_file_variable_count;
    TReadMatFileVariableString                read_mat_file_variable_string;
    TReadMatFileVariableDouble                read_mat_file_variable_double;
    TReadMatFileEnd                           read_mat_file_end;
    TPromptUserInputValue                     prompt_user_input_value;
    TPromptUserInputString                    prompt_user_input_string;
    TIniCreate                                ini_create;
    TIniWriteInt32                            ini_write_int32;
    TIniWriteInt64                            ini_write_int64;
    TIniWriteBool                             ini_write_bool;
    TIniWriteFloat                            ini_write_float;
    TIniWriteString                           ini_write_string;
    TIniReadInt32                             ini_read_int32;
    TIniReadInt64                             ini_read_int64;
    TIniReadBool                              ini_read_bool;
    TIniReadFloat                             ini_read_float;
    TIniReadString                            ini_read_string;
    TIniSectionExists                         ini_section_exists;
    TIniKeyExists                             ini_key_exists;
    TIniDeleteKey                             ini_delete_key;
    TIniDeleteSection                         ini_delete_section;
    TIniClose                                 ini_close;
    TTSAppMakeToastUntil                      make_toast_until;
    TTSAppMakeToastWithCallback               make_toast_with_callback;
    TTSAppGetDocPath                          get_doc_path;
    TTSAppGetHWIDString                       get_hardware_id_string;
    TTSAppGetHWIDArray                        get_hardware_id_array;
    TTSAppCreateSystemVar                     create_system_var;
    TTSAppDeleteSystemVar                     delete_system_var;
    TTSAppRunForm                             run_form;
    TTSAppStopForm                            stop_form;
    TReadTextFileStart                        read_text_file_start;
    TReadTextFileLine                         read_text_file_line;
    TReadTextFileEnd                          read_text_file_end;
    TPlaySound                                play_sound;
    TTSAppSetSystemVarUnit                    set_system_var_unit;
    TTSAppSetSystemVarValueTable              set_system_var_value_table;
    TUILoadPlugin                             load_plugin;
    TUIUnloadPlugin                           unload_plugin;
    TTSAppSetSystemVarDoubleAsync             set_system_var_double_async;
    TTSAppSetSystemVarInt32Async              set_system_var_int32_async;
    TTSAppSetSystemVarUInt32Async             set_system_var_uint32_async;
    TTSAppSetSystemVarInt64Async              set_system_var_int64_async;
    TTSAppSetSystemVarUInt64Async             set_system_var_uint64_async;
    TTSAppSetSystemVarUInt8ArrayAsync         set_system_var_uint8_array_async;
    TTSAppSetSystemVarInt32ArrayAsync         set_system_var_int32_array_async;
    TTSAppSetSystemVarInt64ArrayAsync         set_system_var_int64_array_async;
    TTSAppSetSystemVarDoubleArrayAsync        set_system_var_double_array_async;
    TTSAppSetSystemVarStringAsync             set_system_var_string_async;
    TTSAppSetSystemVarGenericAsync            set_system_var_generic_async;
    TAMGetRunningState                        am_get_running_state;
    TAMRun                                    am_run;
    TAMStop                                   am_stop;
    TAMSelectSubModule                        am_select_sub_module;
    TPanelSetEnable                           panel_set_enable;
    TPanelSetPositionX                        panel_set_position_x;
    TPanelSetPositionY                        panel_set_position_y;
    TPanelSetPositionXY                       panel_set_position_xy;
    TPanelSetOpacity                          panel_set_opacity;
    TPanelSetWidth                            panel_set_width;
    TPanelSetHeight                           panel_set_height;
    TPanelSetWidthHeight                      panel_set_width_height;
    TPanelSetRotationAngle                    panel_set_rotation_angle;
    TPanelSetRotationCenter                   panel_set_rotation_center;
    TPanelSetScaleX                           panel_set_scale_x;
    TPanelSetScaleY                           panel_set_scale_y;
    TPanelGetEnable                           panel_get_enable;
    TPanelGetPositionXY                       panel_get_position_xy;
    TPanelGetOpacity                          panel_get_opacity;
    TPanelGetWidthHeight                      panel_get_width_height;
    TPanelGetRotationAngle                    panel_get_rotation_angle;
    TPanelGetRotationCenter                   panel_get_rotation_center;
    TPanelGetScaleXY                          panel_get_scale_xy;
    TSTIMSetSignalStatus                      stim_set_signal_status;
    TSTIMGetSignalStatus                      stim_get_signal_status;
    TPanelSetBkgdColor                        panel_set_bkgd_color;
    TPanelGetBkgdColor                        panel_get_bkgd_color;
    TClearMeasurementForm                     clear_measurement_form;
    TTSAppGetSystemVarAddress                 get_system_var_address;
    TTSAppSetSystemVarLogging                 set_system_var_logging;
    TTSAppGetSystemVarLogging                 get_system_var_logging;
    TTSAppLogSystemVarValue                   internal_log_system_var_value;
    TUIGetMainWindowHandle                    get_main_window_handle;
    TPrintDeltaTime                           print_delta_time;
    TAtomicIncrement32                        atomic_increment32;
    TAtomicIncrement64                        atomic_increment64;
    TAtomicSet32                              atomic_set_32;
    TAtomicSet64                              atomic_set_64;
    TGetConstantDouble                        get_constant_double;
    TAddDirectMappingCAN                      add_direct_mapping_can;
    TAddExpressionMapping                     add_expression_mapping;
    TDeleteSymbolMappingItem                  delete_symbol_mapping_item;
    TEnableSymbolMappingItem                  enable_symbol_mapping_item;
    TEnableSymbolMappingEngine                enable_symbol_mapping_engine;
    TDeleteSymbolMappingItems                 delete_symbol_mapping_items;
    TSaveSymbolMappingSettings                save_symbol_mapping_settings;
    TLoadSymbolMappingSettings                load_symbol_mapping_settings;
    TAddDirectMappingWithFactorOffsetCAN      add_direct_mapping_with_factor_offset_can;
    TTSDebugLog                               internal_debug_log;
    TWaitWithDialog                           internal_wait_with_dialog;
    TTSAppIsConnected                         is_connected;
    TTSAppGetFlexRayChannelCount              get_flexray_channel_count;
    TTSAppSetFlexRayChannelCount              set_flexray_channel_count;
    TDBGetCANDBCount                          db_get_can_database_count;
    TDBGetLINDBCount                          db_get_lin_database_count;
    TDBGetFlexRayDBCount                      db_get_flexray_database_count;
    TDBGetCANDBPropertiesByIndex              db_get_can_database_properties_by_index;
    TDBGetLINDBPropertiesByIndex              db_get_lin_database_properties_by_index;
    TDBGetFlexRayDBPropertiesByIndex          db_get_flexray_database_properties_by_index;
    TDBGetCANDBECUPropertiesByIndex           db_get_can_ecu_properties_by_index;
    TDBGetLINDBECUPropertiesByIndex           db_get_lin_ecu_properties_by_index;
    TDBGetFlexRayDBECUPropertiesByIndex       db_get_flexray_ecu_properties_by_index;
    TDBGetCANDBFramePropertiesByIndex         db_get_can_frame_properties_by_index;
    TDBGetLINDBFramePropertiesByIndex         db_get_lin_frame_properties_by_index;
    TDBGetFlexRayDBFramePropertiesByIndex     db_get_flexray_frame_properties_by_index;
    TDBGetCANDBSignalPropertiesByIndex        db_get_can_signal_properties_by_index;
    TDBGetLINDBSignalPropertiesByIndex        db_get_lin_signal_properties_by_index;
    TDBGetFlexRayDBSignalPropertiesByIndex    db_get_flexray_signal_properties_by_index;
    TDBGetCANDBPropertiesByAddress            db_get_can_database_properties_by_address;
    TDBGetLINDBPropertiesByAddress            db_get_lin_database_properties_by_address;
    TDBGetFlexRayDBPropertiesByAddress        db_get_flexray_database_properties_by_address;
    TDBGetCANDBECUPropertiesByAddress         db_get_can_ecu_properties_by_address;
    TDBGetLINDBECUPropertiesByAddress         db_get_lin_ecu_properties_by_address;
    TDBGetFlexRayDBECUPropertiesByAddress     db_get_flexray_ecu_properties_by_address;
    TDBGetCANDBFramePropertiesByAddress       db_get_can_frame_properties_by_address;
    TDBGetLINDBFramePropertiesByAddress       db_get_lin_frame_properties_by_address;
    TDBGetFlexRayDBFramePropertiesByAddress   db_get_flexray_frame_properties_by_address;
    TDBGetCANDBSignalPropertiesByAddress      db_get_can_signal_properties_by_address;
    TDBGetLINDBSignalPropertiesByAddress      db_get_lin_signal_properties_by_address;
    TDBGetFlexRayDBSignalPropertiesByAddress  db_get_flexray_signal_properties_by_address;
    TRunPythonFunction                        run_python_function;
    TGetCurrentMpName                         internal_get_current_mp_name;
    TPanelSetSelectorItems                    panel_set_selector_items;
    TPanelGetSelectorItems                    panel_get_selector_items;
    // >>> mp app end <<<
    // place holder
    s32                                       FDummy[816];
    void terminate_application(void){
        internal_terminate_application(FObj);
    }
    s32 wait(const s32 ATimeMs, const char* AMsg){
        return internal_wait(FObj, ATimeMs, AMsg);
    }
    s32 check(const s32 AErrorCode){
        return internal_check(FObj, AErrorCode);
    }
    s32 debug_log(const char* AFile, const char* AFunc, const s32 ALine, const char* AStr, const TLogLevel ALevel){
        return internal_debug_log(FObj, AFile, AFunc, ALine, AStr, ALevel);
    }
    s32 start_log(void){
        return internal_start_log(FObj);
    }
    s32 end_log(void){
        return internal_end_log(FObj);
    }
    s32 write_realtime_comment(const char* AName){
        return internal_write_realtime_comment(FObj, AName);
    }
    s32 check_terminate(void){
        return internal_check_terminate(FObj);
    }
    s32 set_check_failed_terminate(const s32 AToTerminate){
        return internal_set_check_failed_terminate(FObj, AToTerminate);
    }
    s32 set_thread_priority(const s32 APriority){
        return internal_set_thread_priority(FObj, APriority);
    }
    s32 log_system_var_value(const char* ACompleteName){
        return internal_log_system_var_value(FObj, ACompleteName);
    }
    s32 wait_with_dialog(const char* ATitle, const char* AMessage, const bool* ApResult, const float* ApProgress100){
        return internal_wait_with_dialog(FObj, ATitle, AMessage, ApResult, ApProgress100);
    }
    char* get_current_mp_name(void){
        return internal_get_current_mp_name(FObj);
    }
}TTSApp, * PTSApp;

// =========================== COM ===========================
typedef s32 (__stdcall* TTransmitCANAsync)(const PCAN ACAN);
typedef s32 (__stdcall* TTransmitCANFDAsync)(const PCANFD ACANFD);
typedef s32 (__stdcall* TTransmitLINAsync)(const PLIN ALIN);
typedef s32 (__stdcall* TTransmitCANSync)(const PCAN ACAN, const s32 ATimeoutMS);
typedef s32 (__stdcall* TTransmitCANFDSync)(const PCANFD ACANFD, const s32 ATimeoutMS);
typedef s32 (__stdcall* TTransmitLINSync)(const PLIN ALIN, const s32 ATimeoutMS);
typedef s32 (__stdcall* TTransmitFlexRayASync)(const PFlexRay AFlexRay);
typedef s32 (__stdcall* TTransmitFlexRaySync)(const PFlexRay AFlexRay, const s32 ATimeoutMS);
typedef double (__stdcall* TGetCANSignalValue)(const PCANSignal ACANSignal, const pu8 AData);
typedef void (__stdcall* TSetCANSignalValue)(const PCANSignal ACANSignal, const pu8 AData, const double AValue);
typedef double (__stdcall* TGetFlexRaySignalValue)(const PFlexRaySignal AFlexRaySignal, const pu8 AData);
typedef void (__stdcall* TSetFlexRaySignalValue)(const PFlexRaySignal AFlexRaySignal, const pu8 AData, const double AValue);
typedef void (__stdcall* TCANEvent)(const ps32 AObj, const PCAN ACAN);
typedef void (__stdcall* TCANFDEvent)(const ps32 AObj, const PCANFD ACANFD);
typedef void (__stdcall* TLINEvent)(const ps32 AObj, const PLIN ALIN);
typedef void (__stdcall* TFlexRayEvent)(const ps32 AObj, const PFlexRay AFlexRay);
typedef s32 (__stdcall* TRegisterCANEvent)(const ps32 AObj, const TCANEvent AEvent);
typedef s32 (__stdcall* TUnregisterCANEvent)(const ps32 AObj, const TCANEvent AEvent);
typedef s32 (__stdcall* TRegisterCANFDEvent)(const ps32 AObj, const TCANFDEvent AEvent);
typedef s32 (__stdcall* TUnregisterCANFDEvent)(const ps32 AObj, const TCANFDEvent AEvent);
typedef s32 (__stdcall* TRegisterLINEvent)(const ps32 AObj, const TLINEvent AEvent);
typedef s32 (__stdcall* TUnregisterLINEvent)(const ps32 AObj, const TLINEvent AEvent);
typedef s32 (__stdcall* TRegisterFlexRayEvent)(const ps32 AObj, const TFlexRayEvent AEvent);
typedef s32 (__stdcall* TUnregisterFlexRayEvent)(const ps32 AObj, const TFlexRayEvent AEvent);
typedef s32 (__stdcall* TUnregisterCANEvents)(const ps32 AObj);
typedef s32 (__stdcall* TUnregisterLINEvents)(const ps32 AObj);
typedef s32 (__stdcall* TUnregisterCANFDEvents)(const ps32 AObj);
typedef s32 (__stdcall* TUnregisterFlexRayEvents)(const ps32 AObj);
typedef s32 (__stdcall* TUnregisterALLEvents)(const ps32 AObj);
typedef s32 (__stdcall* TRegisterPreTxCANEvent)(const ps32 AObj, const TCANEvent AEvent);
typedef s32 (__stdcall* TUnregisterPreTxCANEvent)(const ps32 AObj, const TCANEvent AEvent);
typedef s32 (__stdcall* TRegisterPreTxCANFDEvent)(const ps32 AObj, const TCANFDEvent AEvent);
typedef s32 (__stdcall* TUnregisterPreTxCANFDEvent)(const ps32 AObj, const TCANFDEvent AEvent);
typedef s32 (__stdcall* TRegisterPreTxLINEvent)(const ps32 AObj, const TLINEvent AEvent);
typedef s32 (__stdcall* TUnregisterPreTxLINEvent)(const ps32 AObj, const TLINEvent AEvent);
typedef s32 (__stdcall* TRegisterPreTxFlexRayEvent)(const ps32 AObj, const TFlexRayEvent AEvent);
typedef s32 (__stdcall* TUnregisterPreTxFlexRayEvent)(const ps32 AObj, const TFlexRayEvent AEvent);
typedef s32 (__stdcall* TUnregisterPreTxCANEvents)(const ps32 AObj);
typedef s32 (__stdcall* TUnregisterPreTxLINEvents)(const ps32 AObj);
typedef s32 (__stdcall* TUnregisterPreTxCANFDEvents)(const ps32 AObj);
typedef s32 (__stdcall* TUnregisterPreTxFlexRayEvents)(const ps32 AObj);
typedef s32 (__stdcall* TUnregisterPreTxALLEvents)(const ps32 AObj);
typedef s32 (__stdcall* TEnableBusStatistics)(const bool AEnable);
typedef s32 (__stdcall* TClearBusStatistics)(void);
typedef s32 (__stdcall* TGetBusStatistics)(const TLIBApplicationChannelType ABusType, const s32 AIdxChn, const TLIBCANBusStatistics AIdxStat, pdouble AStat);
typedef s32 (__stdcall* TGetFPSCAN)(const s32 AIdxChn, const s32 AIdentifier, ps32 AFPS);
typedef s32 (__stdcall* TGetFPSCANFD)(const s32 AIdxChn, const s32 AIdentifier, ps32 AFPS);
typedef s32 (__stdcall* TGetFPSLIN)(const s32 AIdxChn, const s32 AIdentifier, ps32 AFPS);
typedef s32 (__stdcall* TWaitCANMessage)(const void* AObj, const PCAN ATxCAN, const PCAN ARxCAN, const s32 ATimeoutMS);
typedef s32 (__stdcall* TWaitCANFDMessage)(const void* AObj, const PCANFD ATxCANFD, const PCANFD ARxCANFD, const s32 ATimeoutMS);
typedef s32 (__stdcall* TAddCyclicMsgCAN)(const PCAN ACAN, const float APeriodMS);
typedef s32 (__stdcall* TAddCyclicMsgCANFD)(const PCANFD ACANFD, const float APeriodMS);
typedef s32 (__stdcall* TDeleteCyclicMsgCAN)(const PCAN ACAN);
typedef s32 (__stdcall* TDeleteCyclicMsgCANFD)(const PCANFD ACANFD);
typedef s32 (__stdcall* TDeleteCyclicMsgs)(void);
typedef s32 (__stdcall* Tadd_precise_cyclic_message)(const s32 AIdentifier, const u8 AChn, const u8 AIsExt, const float APeriodMS, const s32 ATimeoutMS);
typedef s32 (__stdcall* Tdelete_precise_cyclic_message)(const s32 AIdentifier, const u8 AChn, const u8 AIsExt, const s32 ATimeoutMS);
typedef s32 (__stdcall* TInjectCANMessage)(const PCANFD ACANFD);
typedef s32 (__stdcall* TInjectLINMessage)(const PLIN ALIN);
typedef s32 (__stdcall* TInjectFlexRayFrame)(const PFlexRay AFlexRay);
typedef s32 (__stdcall* TGetCANSignalDefinitionVerbose)(const s32 AIdxChn, const char* ANetworkName, const char* AMsgName, const char* ASignalName, ps32 AMsgIdentifier, PCANSignal ASignalDef);
typedef s32 (__stdcall* TGetCANSignalDefinition)(const char* ASignalAddress, ps32 AMsgIdentifier, PCANSignal ASignalDef);
typedef s32 (__stdcall* TGetFlexRaySignalDefinition)(const char* ASignalAddress, PFlexRaySignal ASignalDef);
// online replay functions
typedef s32 (__stdcall* Ttslog_add_online_replay_config)(const char* AFileName, s32* AIndex);
typedef s32 (__stdcall* Ttslog_set_online_replay_config)(const s32 AIndex, const char* AName, const char* AFileName, const bool AAutoStart, const bool AIsRepetitiveMode, const TLIBOnlineReplayTimingMode AStartTimingMode, const s32 AStartDelayTimeMs, const bool ASendTx, const bool ASendRx, const char* AMappings);
typedef s32 (__stdcall* Ttslog_get_online_replay_count)(s32* ACount);
typedef s32 (__stdcall* Ttslog_get_online_replay_config)(const s32 AIndex, char** AName, char** AFileName, bool* AAutoStart, bool* AIsRepetitiveMode, TLIBOnlineReplayTimingMode* AStartTimingMode, s32* AStartDelayTimeMs, bool* ASendTx, bool* ASendRx, char** AMappings);
typedef s32 (__stdcall* Ttslog_del_online_replay_config)(const s32 AIndex);
typedef s32 (__stdcall* Ttslog_del_online_replay_configs)(void);
typedef s32 (__stdcall* Ttslog_start_online_replay)(const s32 AIndex);
typedef s32 (__stdcall* Ttslog_start_online_replays)(void);
typedef s32 (__stdcall* Ttslog_pause_online_replay)(const s32 AIndex);
typedef s32 (__stdcall* Ttslog_pause_online_replays)(void);
typedef s32 (__stdcall* Ttslog_stop_online_replay)(const s32 AIndex);
typedef s32 (__stdcall* Ttslog_stop_online_replays)(void);
typedef s32 (__stdcall* Ttslog_get_online_replay_status)(const s32 AIndex, TLIBOnlineReplayStatus* AStatus, float* AProgressPercent100);
// CAN rbs functions
typedef s32 (__stdcall* TCANRBSStart)(void);
typedef s32 (__stdcall* TCANRBSStop)(void);
typedef s32 (__stdcall* TCANRBSIsRunning)(bool* AIsRunning);
typedef s32 (__stdcall* TCANRBSConfigure)(const bool AAutoStart, const bool AAutoSendOnModification, const bool AActivateNodeSimulation, const TLIBRBSInitValueOptions AInitValueOptions);
typedef s32 (__stdcall* TCANRBSEnable)(const bool AEnable);
typedef s32 (__stdcall* TCANRBSActivateAllNetworks)(const bool AEnable, const bool AIncludingChildren);
typedef s32 (__stdcall* TCANRBSActivateNetworkByName)(const s32 AIdxChn, const bool AEnable, const char* ANetworkName, const bool AIncludingChildren);
typedef s32 (__stdcall* TCANRBSActivateNodeByName)(const s32 AIdxChn, const bool AEnable, const char* ANetworkName, const char* ANodeName, const bool AIncludingChildren);
typedef s32 (__stdcall* TCANRBSActivateMessageByName)(const s32 AIdxChn, const bool AEnable, const char* ANetworkName, const char* ANodeName, const char* AMsgName);
typedef s32 (__stdcall* TCANRBSSetMessageCycleByName)(const s32 AIdxChn, const s32 AIntervalMs, const char* ANetworkName, const char* ANodeName, const char* AMsgName);
typedef s32 (__stdcall* TCANRBSGetSignalValueByElement)(const s32 AIdxChn, const char* ANetworkName, const char* ANodeName, const char* AMsgName, const char* ASignalName, double* AValue);
typedef s32 (__stdcall* TCANRBSGetSignalValueByAddress)(const char* ASymbolAddress, double* AValue);
typedef s32 (__stdcall* TCANRBSSetSignalValueByElement)(const s32 AIdxChn, const char* ANetworkName, const char* ANodeName, const char* AMsgName, const char* ASignalName, const double AValue);
typedef s32 (__stdcall* TCANRBSSetSignalValueByAddress)(const char* ASymbolAddress, const double AValue);
typedef s32 (__stdcall* TCANRBSBatchSetStart)(void);
typedef s32 (__stdcall* TCANRBSBatchSetEnd)(void);
typedef s32 (__stdcall* TCANRBSBatchSetSignal)(const char* ASymbolAddress, const double AValue);
typedef s32 (__stdcall* TCANRBSSetMessageDirection)(const s32 AIdxChn, const bool AIsTx, const char* ANetworkName, const char* ANodeName, const char* AMsgName);
typedef s32 (__stdcall* TCANRBSFaultInjectionClear)(void);
typedef s32 (__stdcall* TCANRBSFaultInjectionMessageLost)(const bool AEnable, const s32 AIdxChn, const s32 AIdentifier);
typedef s32 (__stdcall* TCANRBSFaultInjectionSignalAlter)(const bool AEnable, const char* ASymbolAddress, const double AAlterValue);
typedef s32 (__stdcall* TCANRBSSetNormalSignal)(const char* ASymbolAddress);
typedef s32 (__stdcall* TCANRBSSetRCSignal)(const char* ASymbolAddress);
typedef s32 (__stdcall* TCANRBSSetRCSignalWithLimit)(const char* ASymbolAddress, const s32 ALowerLimit, const s32 AUpperLimit);
typedef s32 (__stdcall* TCANRBSSetCRCSignal)(const char* ASymbolAddress, const char* AAlgorithmName, const s32 AIdxByteStart, const s32 AByteCount);
// FlexRay rbs functions
typedef s32 (__stdcall* TFlexRayRBSStart)(void);
typedef s32 (__stdcall* TFlexRayRBSStop)(void);
typedef s32 (__stdcall* TFlexRayRBSIsRunning)(bool* AIsRunning);
typedef s32 (__stdcall* TFlexRayRBSConfigure)(const bool AAutoStart, const bool AAutoSendOnModification, const bool AActivateECUSimulation, const TLIBRBSInitValueOptions AInitValueOptions);
typedef s32 (__stdcall* TFlexRayRBSEnable)(const bool AEnable);
typedef s32 (__stdcall* TFlexRayRBSActivateAllClusters)(const bool AEnable, const bool AIncludingChildren);
typedef s32 (__stdcall* TFlexRayRBSActivateClusterByName)(const s32 AIdxChn, const bool AEnable, const char* AClusterName, const bool AIncludingChildren);
typedef s32 (__stdcall* TFlexRayRBSActivateECUByName)(const s32 AIdxChn, const bool AEnable, const char* AClusterName, const char* AECUName, const bool AIncludingChildren);
typedef s32 (__stdcall* TFlexRayRBSActivateFrameByName)(const s32 AIdxChn, const bool AEnable, const char* AClusterName, const char* AECUName, const char* AFrameName);
typedef s32 (__stdcall* TFlexRayRBSGetSignalValueByElement)(const s32 AIdxChn, const char* AClusterName, const char* AECUName, const char* AFrameName, const char* ASignalName, double* AValue);
typedef s32 (__stdcall* TFlexRayRBSGetSignalValueByAddress)(const char* ASymbolAddress, double* AValue);
typedef s32 (__stdcall* TFlexRayRBSSetSignalValueByElement)(const s32 AIdxChn, const char* AClusterName, const char* AECUName, const char* AFrameName, const char* ASignalName, const double AValue);
typedef s32 (__stdcall* TFlexRayRBSSetSignalValueByAddress)(const char* ASymbolAddress, const double AValue);
typedef s32 (__stdcall* TFlexRayRBSBatchSetStart)(void);
typedef s32 (__stdcall* TFlexRayRBSBatchSetEnd)(void);
typedef s32 (__stdcall* TFlexRayRBSBatchSetSignal)(const char* ASymbolAddress, const double AValue);
typedef s32 (__stdcall* TFlexRayRBSSetFrameDirection)(const s32 AIdxChn, const bool AIsTx, const char* AClusterName, const char* AECUName, const char* AFrameName);
typedef s32 (__stdcall* TFlexRayRBSSetNormalSignal)(const char* ASymbolAddress);
typedef s32 (__stdcall* TFlexRayRBSSetRCSignal)(const char* ASymbolAddress);
typedef s32 (__stdcall* TFlexRayRBSSetRCSignalWithLimit)(const char* ASymbolAddress, const s32 ALowerLimit, const s32 AUpperLimit);
typedef s32 (__stdcall* TFlexRayRBSSetCRCSignal)(const char* ASymbolAddress, const char* AAlgorithmName, const s32 AIdxByteStart, const s32 AByteCount);
// log file functions
typedef s32 (__stdcall* Ttslog_blf_write_start)(const char* AFileName, s32* AHandle);
typedef s32 (__stdcall* Ttslog_blf_write_start_w_timestamp)(const char* AFileName, s32* AHandle, u16* AYear, u16* AMonth, u16* ADay, u16* AHour, u16* AMinute, u16* ASecond, u16* AMilliseconds);
typedef s32 (__stdcall* Ttslog_blf_write_set_max_count)(const s32 AHandle, const u32 ACount);
typedef s32 (__stdcall* Ttslog_blf_write_can)(const s32 AHandle, const PCAN ACAN);
typedef s32 (__stdcall* Ttslog_blf_write_can_fd)(const s32 AHandle, const PCANFD ACANFD);
typedef s32 (__stdcall* Ttslog_blf_write_lin)(const s32 AHandle, const PLIN ALIN);
typedef s32 (__stdcall* Ttslog_blf_write_flexray)(const s32 AHandle, const PFlexRay AFlexRay);
typedef s32 (__stdcall* Ttslog_blf_write_realtime_comment)(const s32 AHandle, const s64 ATimeUs, const char* AComment);
typedef s32 (__stdcall* Ttslog_blf_write_end)(const s32 AHandle);
typedef s32 (__stdcall* Ttslog_blf_read_start)(const char* AFileName, s32* AHandle, s32* AObjCount);
typedef s32 (__stdcall* Ttslog_blf_read_status)(const s32 AHandle, s32* AObjReadCount);
typedef s32 (__stdcall* Ttslog_blf_read_object)(const s32 AHandle, s32* AProgressedCnt, TSupportedBLFObjType* AType, PCAN ACAN, PLIN ALIN, PCANFD ACANFD);
typedef s32 (__stdcall* Ttslog_blf_read_object_w_comment)(const s32 AHandle, s32* AProgressedCnt, TSupportedBLFObjType* AType, PCAN ACAN, PLIN ALIN, PCANFD ACANFD, Prealtime_comment_t AComment);
typedef s32 (__stdcall* Ttslog_blf_read_end)(const s32 AHandle);
typedef s32 (__stdcall* Ttslog_blf_seek_object_time)(const s32 AHandle, const double AProg100, s64* ATime, s32* AProgressedCnt);
typedef s32 (__stdcall* Ttslog_blf_to_asc)(const void* AObj, const char* ABLFFileName, const char* AASCFileName, const TProgressCallback AProgressCallback);
typedef s32 (__stdcall* Ttslog_asc_to_blf)(const void* AObj, const char* AASCFileName, const char* ABLFFileName, const TProgressCallback AProgressCallback);
// IP functions
typedef s32 (__stdcall* TIoIPCreate)(const void* AObj, const u16 APortTCP, const u16 APortUDP, const TOnIoIPData AOnTCPDataEvent, const TOnIoIPData AOnUDPDataEvent, s32* AHandle);
typedef s32 (__stdcall* TIoIPDelete)(const void* AObj, const s32 AHandle);
typedef s32 (__stdcall* TIoIPEnableTCPServer)(const void* AObj, const s32 AHandle, const bool AEnable);
typedef s32 (__stdcall* TIoIPEnableUDPServer)(const void* AObj, const s32 AHandle, const bool AEnable);
typedef s32 (__stdcall* TIoIPConnectTCPServer)(const void* AObj, const s32 AHandle, const char* AIpAddress, const u16 APort);
typedef s32 (__stdcall* TIoIPConnectUDPServer)(const void* AObj, const s32 AHandle, const char* AIpAddress, const u16 APort);
typedef s32 (__stdcall* TIoIPDisconnectTCPServer)(const void* AObj, const s32 AHandle);
typedef s32 (__stdcall* TIoIPSendBufferTCP)(const void* AObj, const s32 AHandle, const pu8 APointer, const s32 ASize);
typedef s32 (__stdcall* TIoIPSendBufferUDP)(const void* AObj, const s32 AHandle, const pu8 APointer, const s32 ASize);
typedef s32 (__stdcall* TIoIPRecvTCPClientResponse)(const void* AObj, const s32 AHandle, const s32 ATimeoutMs, const pu8 ABufferToReadTo, ps32 AActualSize);
typedef s32 (__stdcall* TIoIPSendTCPServerResponse)(const void* AObj, const s32 AHandle, const pu8 ABufferToWriteFrom, const s32 ASize);
typedef s32 (__stdcall* TIoIPSendUDPBroadcast)(const void* AObj, const s32 AHandle, const u16 APort, const pu8 ABufferToWriteFrom, const s32 ASize);
typedef s32 (__stdcall* TIoIPSetUDPServerBufferSize)(const void* AObj, const s32 AHandle, const s32 ASize);
typedef s32 (__stdcall* TIoIPRecvUDPClientResponse)(const void* AObj, const s32 AHandle, const s32 ATimeoutMs, const pu8 ABufferToReadTo, ps32 AActualSize);
typedef s32 (__stdcall* TIoIPSendUDPServerResponse)(const void* AObj, const s32 AHandle, const pu8 ABufferToWriteFrom, const s32 ASize);
// signal server
typedef s32 (__stdcall* TSgnSrvRegisterCANSignalByMsgId)(const s32 AIdxChn, const s32 AMsgId, const char* ASgnName, ps32 AClientId);
typedef s32 (__stdcall* TSgnSrvRegisterLINSignalByMsgId)(const s32 AIdxChn, const s32 AMsgId, const char* ASgnName, ps32 AClientId);
typedef s32 (__stdcall* TSgnSrvRegisterCANSignalByMsgName)(const s32 AIdxChn, const char* ANetworkName, const char* AMsgName, const char* ASgnName, ps32 AClientId);
typedef s32 (__stdcall* TSgnSrvRegisterLINSignalByMsgName)(const s32 AIdxChn, const char* ANetworkName, const char* AMsgName, const char* ASgnName, ps32 AClientId);
typedef s32 (__stdcall* TSgnSrvGetCANSignalPhyValueLatest)(const s32 AIdxChn, const s32 AClientId, pdouble AValue, ps64 ATimeUs);
typedef s32 (__stdcall* TSgnSrvGetLINSignalPhyValueLatest)(const s32 AIdxChn, const s32 AClientId, pdouble AValue, ps64 ATimeUs);
typedef s32 (__stdcall* TSgnSrvGetCANSignalPhyValueInMsg)(const s32 AIdxChn, const s32 AClientId, const PCANFD AMsg, pdouble AValue, ps64 ATimeUs);
typedef s32 (__stdcall* TSgnSrvGetLINSignalPhyValueInMsg)(const s32 AIdxChn, const s32 AClientId, const PLIN AMsg, pdouble AValue, ps64 ATimeUs);
typedef s32 (__stdcall* TSgnSrvRegisterFlexRaySignalByFrame)(const s32 AIdxChn, const u8 AChnMask, const u8 ACycleNumber, const s32 ASlotId, const char* ASgnName, ps32 AClientId);
typedef s32 (__stdcall* TSgnSrvRegisterFlexRaySignalByFrameName)(const s32 AIdxChn, const char* ANetworkName, const char* AFrameName, const char* ASgnName, ps32 AClientId);
typedef s32 (__stdcall* TSgnSrvGetFlexRaySignalPhyValueLatest)(const s32 AIdxChn, const s32 AClientId, pdouble AValue, ps64 ATimeUs);
typedef s32 (__stdcall* TSgnSrvGetFlexRaySignalPhyValueInFrame)(const s32 AIdxChn, const s32 AClientId, const PFlexRay AFrame, pdouble AValue, ps64 ATimeUs);
// pdu container
typedef s32 (__stdcall* TPDUContainerSetCycleCount)(const s32 AIdxChn, const s32 AMsgId, const s32 ACount);
typedef s32 (__stdcall* TPDUContainerSetCycleByIndex)(const s32 AIdxChn, const s32 AMsgId, const s32 AIdxCycle, const pchar ASignalGroupIdList);
typedef s32 (__stdcall* TPDUContainerGetCycleCount)(const s32 AIdxChn, const s32 AMsgId, ps32 ACount);
typedef s32 (__stdcall* TPDUContainerGetCycleByIndex)(const s32 AIdxChn, const s32 AMsgId, const s32 AIdxCycle, char** ASignalGroupIdList);
typedef s32 (__stdcall* TPDUContainerRefresh)(const s32 AIdxChn, const s32 AMsgId);
// j1939
typedef s32 (__stdcall* TJ1939MakeId)(const s32 APGN, const u8 ASource, const u8 ADestination, const u8 APriority, ps32 AIdentifier);
typedef s32 (__stdcall* TJ1939ExtractId)(const s32 AIdentifier, ps32 APGN, pu8 ASource, pu8 ADestination, pu8 APriority);
typedef s32 (__stdcall* TJ1939GetPGN)(const s32 AIdentifier, ps32 APGN);
typedef s32 (__stdcall* TJ1939GetSource)(const s32 AIdentifier, pu8 ASource);
typedef s32 (__stdcall* TJ1939GetDestination)(const s32 AIdentifier, pu8 ADestination);
typedef s32 (__stdcall* TJ1939GetPriority)(const s32 AIdentifier, pu8 APriority);
typedef s32 (__stdcall* TJ1939GetR)(const s32 AIdentifier, pu8 AR);
typedef s32 (__stdcall* TJ1939GetDP)(const s32 AIdentifier, pu8 ADP);
typedef s32 (__stdcall* TJ1939GetEDP)(const s32 AIdentifier, pu8 AEDP);
typedef s32 (__stdcall* TJ1939SetPGN)(const ps32 AIdentifier, const s32 APGN);
typedef s32 (__stdcall* TJ1939SetSource)(const ps32 AIdentifier, const u8 ASource);
typedef s32 (__stdcall* TJ1939SetDestination)(const ps32 AIdentifier, const u8 ADestination);
typedef s32 (__stdcall* TJ1939SetPriority)(const ps32 AIdentifier, const u8 APriority);
typedef s32 (__stdcall* TJ1939SetR)(const ps32 AIdentifier, const u8 AR);
typedef s32 (__stdcall* TJ1939SetDP)(const ps32 AIdentifier, const u8 ADP);
typedef s32 (__stdcall* TJ1939SetEDP)(const ps32 AIdentifier, const u8 AEDP);
typedef s32 (__stdcall* TJ1939GetLastPDU)(const u8 AIdxChn, const s32 AIdentifier, const bool AIsTx, const s32 APDUBufferSize, pu8 APDUBuffer, ps32 APDUActualSize, ps64 ATimeUs);
typedef s32 (__stdcall* TJ1939GetLastPDUAsString)(const u8 AIdxChn, const s32 AIdentifier, const bool AIsTx, char** APDUData, ps32 APDUActualSize, ps64 ATimeUs);
typedef s32 (__stdcall* TJ1939TransmitPDUAsync)(const u8 AIdxChn, const s32 APGN, const u8 APriority, const u8 ASource, const u8 ADestination, const pu8 APDUData, const s32 APDUSize);
typedef s32 (__stdcall* TJ1939TransmitPDUSync)(const u8 AIdxChn, const s32 APGN, const u8 APriority, const u8 ASource, const u8 ADestination, const pu8 APDUData, const s32 APDUSize, const s32 ATimeoutMs);
typedef s32 (__stdcall* TJ1939TransmitPDUAsStringAsync)(const u8 AIdxChn, const s32 APGN, const u8 APriority, const u8 ASource, const u8 ADestination, const char* APDUData);
typedef s32 (__stdcall* TJ1939TransmitPDUAsStringSync)(const u8 AIdxChn, const s32 APGN, const u8 APriority, const u8 ASource, const u8 ADestination, const char* APDUData, const s32 ATimeoutMs);

typedef struct _TTSCOM {
    void*                                   FObj;
    // >>> mp com start <<<
    TTransmitCANAsync                       transmit_can_async;
    TTransmitCANSync                        transmit_can_sync;
    TTransmitCANFDAsync                     transmit_canfd_async;
    TTransmitCANFDSync                      transmit_canfd_sync;
    TTransmitLINAsync                       transmit_lin_async;
    TTransmitLINSync                        transmit_lin_sync;
    TGetCANSignalValue                      get_can_signal_value;
    TSetCANSignalValue                      set_can_signal_value;
    TEnableBusStatistics                    enable_bus_statistics;
    TClearBusStatistics                     clear_bus_statistics;
    TGetBusStatistics                       get_bus_statistics;
    TGetFPSCAN                              get_fps_can;
    TGetFPSCANFD                            get_fps_canfd;
    TGetFPSLIN                              get_fps_lin;
    TWaitCANMessage                         internal_wait_can_message;
    TWaitCANFDMessage                       internal_wait_canfd_message;
    TAddCyclicMsgCAN                        add_cyclic_message_can;
    TAddCyclicMsgCANFD                      add_cyclic_message_canfd;
    TDeleteCyclicMsgCAN                     del_cyclic_message_can;
    TDeleteCyclicMsgCANFD                   del_cyclic_message_canfd;
    TDeleteCyclicMsgs                       del_cyclic_messages;    
    TRegisterCANEvent                       internal_register_event_can;
    TUnregisterCANEvent                     internal_unregister_event_can;
    TRegisterCANFDEvent                     internal_register_event_canfd;
    TUnregisterCANFDEvent                   internal_unregister_event_canfd;
    TRegisterLINEvent                       internal_register_event_lin;
    TUnregisterLINEvent                     internal_unregister_event_lin;    
    TUnregisterCANEvents                    internal_unregister_events_can;
    TUnregisterLINEvents                    internal_unregister_events_lin;
    TUnregisterCANFDEvents                  internal_unregister_events_canfd;
    TUnregisterALLEvents                    internal_unregister_events_all;
    Ttslog_add_online_replay_config         tslog_add_online_replay_config ;
    Ttslog_set_online_replay_config         tslog_set_online_replay_config ;
    Ttslog_get_online_replay_count          tslog_get_online_replay_count  ;
    Ttslog_get_online_replay_config         tslog_get_online_replay_config ;
    Ttslog_del_online_replay_config         tslog_del_online_replay_config ;
    Ttslog_del_online_replay_configs        tslog_del_online_replay_configs;
    Ttslog_start_online_replay              tslog_start_online_replay      ;
    Ttslog_start_online_replays             tslog_start_online_replays     ;
    Ttslog_pause_online_replay              tslog_pause_online_replay      ;
    Ttslog_pause_online_replays             tslog_pause_online_replays     ;
    Ttslog_stop_online_replay               tslog_stop_online_replay       ;
    Ttslog_stop_online_replays              tslog_stop_online_replays      ;
    Ttslog_get_online_replay_status         tslog_get_online_replay_status ;
    TCANRBSStart                            can_rbs_start;
    TCANRBSStop                             can_rbs_stop;
    TCANRBSIsRunning                        can_rbs_is_running;
    TCANRBSConfigure                        can_rbs_configure;
    TCANRBSActivateAllNetworks              can_rbs_activate_all_networks;
    TCANRBSActivateNetworkByName            can_rbs_activate_network_by_name;
    TCANRBSActivateNodeByName               can_rbs_activate_node_by_name;
    TCANRBSActivateMessageByName            can_rbs_activate_message_by_name;
    TCANRBSGetSignalValueByElement          can_rbs_get_signal_value_by_element;
    TCANRBSGetSignalValueByAddress          can_rbs_get_signal_value_by_address;
    TCANRBSSetSignalValueByElement          can_rbs_set_signal_value_by_element;
    TCANRBSSetSignalValueByAddress          can_rbs_set_signal_value_by_address;
    TRegisterPreTxCANEvent                  internal_register_pretx_event_can;
    TUnregisterPreTxCANEvent                internal_unregister_pretx_event_can;    
    TRegisterPreTxCANFDEvent                internal_register_pretx_event_canfd;
    TUnregisterPreTxCANFDEvent              internal_unregister_pretx_event_canfd;
    TRegisterPreTxLINEvent                  internal_register_pretx_event_lin;
    TUnregisterPreTxLINEvent                internal_unregister_pretx_event_lin;    
    TUnregisterPreTxCANEvents               internal_unregister_pretx_events_can;
    TUnregisterPreTxLINEvents               internal_unregister_pretx_events_lin;
    TUnregisterPreTxCANFDEvents             internal_unregister_pretx_events_canfd;
    TUnregisterPreTxALLEvents               internal_unregister_pretx_events_all;
    Ttslog_blf_write_start                  tslog_blf_write_start     ;
    Ttslog_blf_write_can                    tslog_blf_write_can       ;
    Ttslog_blf_write_can_fd                 tslog_blf_write_can_fd    ;
    Ttslog_blf_write_lin                    tslog_blf_write_lin       ;
    Ttslog_blf_write_end                    tslog_blf_write_end       ;
    Ttslog_blf_read_start                   tslog_blf_read_start      ;
    Ttslog_blf_read_status                  tslog_blf_read_status     ;
    Ttslog_blf_read_object                  tslog_blf_read_object     ;
    Ttslog_blf_read_end                     tslog_blf_read_end        ;
    Ttslog_blf_seek_object_time             tslog_blf_seek_object_time;
    Ttslog_blf_to_asc                       tslog_blf_to_asc          ;
    Ttslog_asc_to_blf                       tslog_asc_to_blf          ;
    TIoIPCreate                             internal_ioip_create               ;
    TIoIPDelete                             internal_ioip_delete               ;
    TIoIPEnableTCPServer                    internal_ioip_enable_tcp_server    ;
    TIoIPEnableUDPServer                    internal_ioip_enable_udp_server    ;
    TIoIPConnectTCPServer                   internal_ioip_connect_tcp_server   ;
    TIoIPConnectUDPServer                   internal_ioip_connect_udp_server   ;
    TIoIPDisconnectTCPServer                internal_ioip_disconnect_tcp_server;
    TIoIPSendBufferTCP                      internal_ioip_send_buffer_tcp      ;
    TIoIPSendBufferUDP                      internal_ioip_send_buffer_udp      ;
    Ttslog_blf_write_realtime_comment       tslog_blf_write_realtime_comment   ;
    Ttslog_blf_read_object_w_comment        tslog_blf_read_object_w_comment    ;
    TIoIPRecvTCPClientResponse              internal_ioip_receive_tcp_client_response;
    TIoIPSendTCPServerResponse              internal_ioip_send_tcp_server_response;
    TIoIPSendUDPBroadcast                   internal_ioip_send_udp_broadcast;
    TIoIPSetUDPServerBufferSize             internal_ioip_set_udp_server_buffer_size;
    TIoIPRecvUDPClientResponse              internal_ioip_receive_udp_client_response;
    TIoIPSendUDPServerResponse              internal_ioip_send_udp_server_response;
    Ttslog_blf_write_start_w_timestamp      tslog_blf_write_start_w_timestamp;
    Ttslog_blf_write_set_max_count          tslog_blf_write_set_max_count;
    TCANRBSSetMessageCycleByName            can_rbs_set_message_cycle_by_name;
    TSgnSrvRegisterCANSignalByMsgId         sgnsrv_register_can_signal_by_msg_identifier;
    TSgnSrvRegisterLINSignalByMsgId         sgnsrv_register_lin_signal_by_msg_identifier;
    TSgnSrvRegisterCANSignalByMsgName       sgnsrv_register_can_signal_by_msg_name;
    TSgnSrvRegisterLINSignalByMsgName       sgnsrv_register_lin_signal_by_msg_name;
    TSgnSrvGetCANSignalPhyValueLatest       sgnsrv_get_can_signal_phy_value_latest;
    TSgnSrvGetLINSignalPhyValueLatest       sgnsrv_get_lin_signal_phy_value_latest;
    TSgnSrvGetCANSignalPhyValueInMsg        sgnsrv_get_can_signal_phy_value_in_msg;
    TSgnSrvGetLINSignalPhyValueInMsg        sgnsrv_get_lin_signal_phy_value_in_msg;
    TCANRBSEnable                           can_rbs_enable;
    TCANRBSBatchSetStart                    can_rbs_batch_set_start;
    TCANRBSBatchSetEnd                      can_rbs_batch_set_end;
    TInjectCANMessage                       inject_can_message;
    TInjectLINMessage                       inject_lin_message;
    TCANRBSBatchSetSignal                   can_rbs_batch_set_signal;
    TCANRBSSetMessageDirection              can_rbs_set_message_direction;
    Tadd_precise_cyclic_message             add_precise_cyclic_message;
    Tdelete_precise_cyclic_message          delete_precise_cyclic_message;
    TPDUContainerSetCycleCount              pdu_container_set_cycle_count;
    TPDUContainerSetCycleByIndex            pdu_container_set_cycle_by_index;
    TPDUContainerGetCycleCount              pdu_container_get_cycle_count;
    TPDUContainerGetCycleByIndex            pdu_container_get_cycle_by_index;
    TPDUContainerRefresh                    pdu_container_refresh;
    TCANRBSFaultInjectionClear              can_rbs_fault_inject_clear;
    TCANRBSFaultInjectionMessageLost        can_rbs_fault_inject_message_lost;
    TCANRBSFaultInjectionSignalAlter        can_rbs_fault_inject_signal_alter;
    TJ1939MakeId                            j1939_make_id;
    TJ1939ExtractId                         j1939_extract_id;
    TJ1939GetPGN                            j1939_get_pgn;
    TJ1939GetSource                         j1939_get_source;
    TJ1939GetDestination                    j1939_get_destination;
    TJ1939GetPriority                       j1939_get_priority;
    TJ1939GetR                              j1939_get_r;
    TJ1939GetDP                             j1939_get_dp;
    TJ1939GetEDP                            j1939_get_edp;
    TJ1939SetPGN                            j1939_set_pgn;
    TJ1939SetSource                         j1939_set_source;
    TJ1939SetDestination                    j1939_set_destination;
    TJ1939SetPriority                       j1939_set_priority;
    TJ1939SetR                              j1939_set_r;
    TJ1939SetDP                             j1939_set_dp;
    TJ1939SetEDP                            j1939_set_edp;
    TJ1939GetLastPDU                        j1939_get_last_pdu;
    TJ1939GetLastPDUAsString                j1939_get_last_pdu_as_string;
    TJ1939TransmitPDUAsync                  j1939_transmit_pdu_async;
    TJ1939TransmitPDUSync                   j1939_transmit_pdu_sync;
    TJ1939TransmitPDUAsStringAsync          j1939_transmit_pdu_as_string_async;
    TJ1939TransmitPDUAsStringSync           j1939_transmit_pdu_as_string_sync;
    TCANRBSSetNormalSignal                  can_rbs_set_normal_signal;
    TCANRBSSetRCSignal                      can_rbs_set_rc_signal;
    TCANRBSSetCRCSignal                     can_rbs_set_crc_signal;
    TCANRBSSetRCSignalWithLimit             can_rbs_set_rc_signal_with_limit;
    TGetCANSignalDefinitionVerbose          get_can_signal_definition_verbose;
    TGetCANSignalDefinition                 get_can_signal_definition;
    TTransmitFlexRayASync                   transmit_flexray_async;
    TTransmitFlexRaySync                    transmit_flexray_sync;
    TGetFlexRaySignalValue                  get_flexray_signal_value;
    TSetFlexRaySignalValue                  set_flexray_signal_value;
    TRegisterFlexRayEvent                   internal_register_event_flexray;
    TUnregisterFlexRayEvent                 internal_unregister_event_flexray;
    TInjectFlexRayFrame                     inject_flexray_frame;
    TGetFlexRaySignalDefinition             get_flexray_signal_definition;
    Ttslog_blf_write_flexray                tslog_blf_write_flexray;
    TSgnSrvRegisterFlexRaySignalByFrame     sgnsrv_register_flexray_signal_by_frame;
    TSgnSrvRegisterFlexRaySignalByFrameName sgnsrv_register_flexray_signal_by_frame_name;
    TSgnSrvGetFlexRaySignalPhyValueLatest   sgnsrv_get_flexray_signal_phy_value_latest;
    TSgnSrvGetFlexRaySignalPhyValueInFrame  sgnsrv_get_flexray_signal_phy_value_in_frame;
    TUnregisterFlexRayEvents                internal_unregister_events_flexray;
    TRegisterPreTxFlexRayEvent              internal_register_pretx_event_flexray;
    TUnregisterPreTxFlexRayEvent            internal_unregister_pretx_event_flexray;  
    TUnregisterPreTxFlexRayEvents           internal_unregister_pretx_events_flexray;
    TFlexRayRBSStart                        flexray_rbs_start;
    TFlexRayRBSStop                         flexray_rbs_stop;
    TFlexRayRBSIsRunning                    flexray_rbs_is_running;
    TFlexRayRBSConfigure                    flexray_rbs_configure;
    TFlexRayRBSEnable                       flexray_rbs_enable;
    TFlexRayRBSActivateAllClusters          flexray_rbs_activate_all_clusters;
    TFlexRayRBSActivateClusterByName        flexray_rbs_activate_cluster_by_name;
    TFlexRayRBSActivateECUByName            flexray_rbs_activate_ecu_by_name;
    TFlexRayRBSActivateFrameByName          flexray_rbs_activate_frame_by_name;
    TFlexRayRBSGetSignalValueByElement      flexray_rbs_get_signal_value_by_element;
    TFlexRayRBSGetSignalValueByAddress      flexray_rbs_get_signal_value_by_address;
    TFlexRayRBSSetSignalValueByElement      flexray_rbs_set_signal_value_by_element;
    TFlexRayRBSSetSignalValueByAddress      flexray_rbs_set_signal_value_by_address;
    TFlexRayRBSBatchSetStart                flexray_rbs_batch_set_start;
    TFlexRayRBSBatchSetEnd                  flexray_rbs_batch_set_end;
    TFlexRayRBSBatchSetSignal               flexray_rbs_batch_set_signal;
    TFlexRayRBSSetFrameDirection            flexray_rbs_set_frame_direction;
    TFlexRayRBSSetNormalSignal              flexray_rbs_set_normal_signal;
    TFlexRayRBSSetRCSignal                  flexray_rbs_set_rc_signal;
    TFlexRayRBSSetRCSignalWithLimit         flexray_rbs_set_rc_signal_with_limit;
    TFlexRayRBSSetCRCSignal                 flexray_rbs_set_crc_signal;
    // >>> mp com end <<<
    // place holder
    s32                                     FDummy[842];
    // internal functions
    s32 wait_can_message(const PCAN ATxCAN, const PCAN ARxCAN, const s32 ATimeoutMS) {
        return internal_wait_can_message(FObj, ATxCAN, ARxCAN, ATimeoutMS);
    }
    s32 wait_canfd_message(const PCANFD ATxCANFD, const PCANFD ARxCANFD, const s32 ATimeoutMS) {
        return internal_wait_canfd_message(FObj, ATxCANFD, ARxCANFD, ATimeoutMS);
    }
    s32 register_event_can(const ps32 AObj, const TCANEvent AEvent){
        return internal_register_event_can(AObj, AEvent);
    }
    s32 unregister_event_can(const ps32 AObj, const TCANEvent AEvent){
        return internal_unregister_event_can(AObj, AEvent);
    }
    s32 register_event_canfd(const ps32 AObj, const TCANFDEvent AEvent){
        return internal_register_event_canfd(AObj, AEvent);
    }
    s32 unregister_event_canfd(const ps32 AObj, const TCANFDEvent AEvent){
        return internal_unregister_event_canfd(AObj, AEvent);
    }
    s32 register_event_lin(const ps32 AObj, const TLINEvent AEvent){
        return internal_register_event_lin(AObj, AEvent);
    }
    s32 unregister_event_lin(const ps32 AObj, const TLINEvent AEvent){
        return internal_unregister_event_lin(AObj, AEvent);
    }
    s32 unregister_events_can(const ps32 AObj){
        return internal_unregister_events_can(AObj);
    }
    s32 unregister_events_lin(const ps32 AObj){
        return internal_unregister_events_lin(AObj);
    }
    s32 unregister_events_canfd(const ps32 AObj){
        return internal_unregister_events_canfd(AObj);
    }
    s32 unregister_events_all(const ps32 AObj){
        return internal_unregister_events_all(AObj);
    }
    s32 register_pretx_event_can(const ps32 AObj, const TCANEvent AEvent){
        return internal_register_pretx_event_can(AObj, AEvent);
    }
    s32 unregister_pretx_event_can(const ps32 AObj, const TCANEvent AEvent){
        return internal_unregister_pretx_event_can(AObj, AEvent);
    }
    s32 register_pretx_event_canfd(const ps32 AObj, const TCANFDEvent AEvent){
        return internal_register_pretx_event_canfd(AObj, AEvent);
    }
    s32 unregister_pretx_event_canfd(const ps32 AObj, const TCANFDEvent AEvent){
        return internal_unregister_pretx_event_canfd(AObj, AEvent);
    }
    s32 register_pretx_event_lin(const ps32 AObj, const TLINEvent AEvent){
        return internal_register_pretx_event_lin(AObj, AEvent);
    }
    s32 unregister_pretx_event_lin(const ps32 AObj, const TLINEvent AEvent){
        return internal_unregister_pretx_event_lin(AObj, AEvent);
    }
    s32 unregister_pretx_events_can(const ps32 AObj){
        return internal_unregister_pretx_events_can(AObj);
    }
    s32 unregister_pretx_events_lin(const ps32 AObj){
        return internal_unregister_pretx_events_lin(AObj);
    }
    s32 unregister_pretx_events_canfd(const ps32 AObj){
        return internal_unregister_pretx_events_canfd(AObj);
    }
    s32 unregister_pretx_events_all(const ps32 AObj){
        return internal_unregister_pretx_events_all(AObj);
    }
    s32 register_event_flexray(const ps32 AObj, const TFlexRayEvent AEvent){
        return internal_register_event_flexray(AObj, AEvent);
    }
    s32 unregister_event_flexray(const ps32 AObj, const TFlexRayEvent AEvent){
        return internal_unregister_event_flexray(AObj, AEvent);
    }
    s32 unregister_events_flexray(const ps32 AObj){
        return internal_unregister_events_flexray(AObj);
    }
    s32 register_pretx_event_flexray(const ps32 AObj, const TFlexRayEvent AEvent){
        return internal_register_pretx_event_flexray(AObj, AEvent);
    }
    s32 unregister_pretx_event_flexray(const ps32 AObj, const TFlexRayEvent AEvent){
        return internal_unregister_pretx_event_flexray(AObj, AEvent);
    }
    s32 unregister_pretx_events_flexray(const ps32 AObj){
        return internal_unregister_pretx_events_flexray(AObj);
    } 
    // IP functions
    s32 ioip_create(const u16 APortTCP, const u16 APortUDP, const TOnIoIPData AOnTCPDataEvent, const TOnIoIPData AOnUDPEvent, s32* AHandle){
        return internal_ioip_create(FObj, APortTCP, APortUDP, AOnTCPDataEvent, AOnUDPEvent, AHandle);
    }
    s32 ioip_delete(const s32 AHandle){
        return internal_ioip_delete(FObj, AHandle);
    }
    s32 ioip_enable_tcp_server(const s32 AHandle, const bool AEnable){
        return internal_ioip_enable_tcp_server(FObj, AHandle, AEnable);
    }
    s32 ioip_enable_udp_server(const s32 AHandle, const bool AEnable){
        return internal_ioip_enable_udp_server(FObj, AHandle, AEnable);
    }
    s32 ioip_connect_tcp_server(const s32 AHandle, const char* AIpAddress, const u16 APort){
        return internal_ioip_connect_tcp_server(FObj, AHandle, AIpAddress, APort);
    }
    s32 ioip_connect_udp_server(const s32 AHandle, const char* AIpAddress, const u16 APort){
        return internal_ioip_connect_udp_server(FObj, AHandle, AIpAddress, APort);
    }
    s32 ioip_disconnect_tcp_server(const s32 AHandle){
        return internal_ioip_disconnect_tcp_server(FObj, AHandle);
    }
    s32 ioip_send_buffer_tcp(const s32 AHandle, const pu8 APointer, const s32 ASize){
        return internal_ioip_send_buffer_tcp(FObj, AHandle, APointer, ASize);
    }
    s32 ioip_send_buffer_udp(const s32 AHandle, const pu8 APointer, const s32 ASize){
        return internal_ioip_send_buffer_udp(FObj, AHandle, APointer, ASize);
    }
    s32 ioip_receive_tcp_client_response(const s32 AHandle, const s32 ATimeoutMs, const pu8 ABufferToReadTo, ps32 AActualSize){
        return internal_ioip_receive_tcp_client_response(FObj, AHandle, ATimeoutMs, ABufferToReadTo, AActualSize);
    }
    s32 ioip_send_tcp_server_response(const s32 AHandle, const pu8 ABufferToWriteFrom, const s32 ASize){
        return internal_ioip_send_tcp_server_response(FObj, AHandle, ABufferToWriteFrom, ASize);
    }
    s32 ioip_send_udp_broadcast(const s32 AHandle, const u16 APort, const pu8 ABufferToWriteFrom, const s32 ASize){
        return internal_ioip_send_udp_broadcast(FObj, AHandle, APort, ABufferToWriteFrom, ASize);
    }
    s32 ioip_set_udp_server_buffer_size(const s32 AHandle, const s32 ASize){
        return internal_ioip_set_udp_server_buffer_size(FObj, AHandle, ASize);
    }
    s32 ioip_receive_udp_client_response(const s32 AHandle, const s32 ATimeoutMs, const pu8 ABufferToReadTo, ps32 AActualSize){
        return internal_ioip_receive_udp_client_response(FObj, AHandle, ATimeoutMs, ABufferToReadTo, AActualSize);
    }
    s32 ioip_send_udp_server_response(const s32 AHandle, const pu8 ABufferToWriteFrom, const s32 ASize){
        return internal_ioip_send_udp_server_response(FObj, AHandle, ABufferToWriteFrom, ASize);
    }
}TTSCOM, * PTSCOM;

// =========================== Test ===========================
typedef s32 (__stdcall* TTestSetVerdictOK)(const void* AObj, const char* AStr);
typedef s32 (__stdcall* TTestSetVerdictNOK)(const void* AObj, const char* AStr);
typedef s32 (__stdcall* TTestSetVerdictCOK)(const void* AObj, const char* AStr);
typedef s32 (__stdcall* TTestCheckVerdict)(const void* AObj, const char* AName, const double AValue, const double AMin, const double AMax);
typedef s32 (__stdcall* TTestLog)(const void* AObj, const char* AStr, const TLogLevel ALevel);
typedef s32 (__stdcall* TTestLogValue)(const void* AObj, const char* AStr, const double AValue, const TLogLevel ALevel);
typedef s32 (__stdcall* TTestDebugLog)(const void* AObj, const char* AFile, const char* AFunc, const s32 ALine, const char* AStr, const TLogLevel ALevel);
typedef s32 (__stdcall* TTestWriteResultString)(const void* AObj, const char* AName, const char* AValue, const TLogLevel ALevel);
typedef s32 (__stdcall* TTestWriteResultValue)(const void* AObj, const char* AName, const double AValue, const TLogLevel ALevel);
typedef s32 (__stdcall* TTestCheckErrorBegin)(void);
typedef s32 (__stdcall* TTestCheckErrorEnd)(const ps32 AErrorCount);
typedef s32 (__stdcall* TTestWriteResultImage)(const void* AObj, const char* AName, const char* AImageFileFullPath);
typedef s32 (__stdcall* TTestRetrieveCurrentResultFolder)(const void* AObj, char** AFolder);
typedef s32 (__stdcall* TTestCheckTerminate)(void);
typedef s32 (__stdcall* TTestSignalCheckerClear)(void);
typedef s32 (__stdcall* TTestSignalCheckerAddCheckWithTime)(const TSignalType ASgnType, const TSignalCheckKind ACheckKind, const char* ASgnName, const double ASgnMin, const double ASgnMax, const double ATimeStartS, const double ATimeEndS, ps32 ACheckId);
typedef s32 (__stdcall* TTestSignalCheckerAddCheckWithTrigger)(const TSignalType ASgnType, const TSignalCheckKind ACheckKind, const char* ASgnName, const double ASgnMin, const double ASgnMax, const TSignalType ATriggerType, const char* ATriggerName, const double ATriggerMin, const double ATriggerMax, ps32 ACheckId);
typedef s32 (__stdcall* TTestSignalCheckerAddStatisticsWithTime)(const TSignalType ASgnType, const TSignalStatisticsKind AStatisticsKind, const char* ASgnName, const double ATimeStartS, const double ATimeEndS, ps32 ACheckId);
typedef s32 (__stdcall* TTestSignalCheckerAddStatisticsWithTrigger)(const TSignalType ASgnType, const TSignalStatisticsKind AStatisticsKind, const char* ASgnName, const TSignalType ATriggerType, const char* ATriggerName, const double ATriggerMin, const double ATriggerMax, ps32 ACheckId);
typedef s32 (__stdcall* TTestSignalCheckerGetResult)(const void* AObj, const s32 ACheckId, bool* APass, pdouble AResult, char** AResultRepr);
typedef s32 (__stdcall* TTestSignalCheckerEnable)(const s32 ACheckId, const bool AEnable);
typedef s32 (__stdcall* TTestSignalCheckerAddRisingEdgeWithTime)(const TSignalType ASgnType, const char* ASgnName, const double ATimeStartS, const double ATimeEndS, ps32 ACheckId);
typedef s32 (__stdcall* TTestSignalCheckerAddRisingEdgeWithTrigger)(const TSignalType ASgnType, const char* ASgnName, const TSignalType ATriggerType, const char* ATriggerName, const double ATriggerMin, const double ATriggerMax, ps32 ACheckId);
typedef s32 (__stdcall* TTestSignalCheckerAddFallingEdgeWithTime)(const TSignalType ASgnType, const char* ASgnName, const double ATimeStartS, const double ATimeEndS, ps32 ACheckId);
typedef s32 (__stdcall* TTestSignalCheckerAddFallingEdgeWithTrigger)(const TSignalType ASgnType, const char* ASgnName, const TSignalType ATriggerType, const char* ATriggerName, const double ATriggerMin, const double ATriggerMax, ps32 ACheckId);
typedef s32 (__stdcall* TTestSignalCheckerAddMonotonyRisingWithTime)(const TSignalType ASgnType, const char* ASgnName, const s32 ASampleIntervalMs, const double ATimeStartS, const double ATimeEndS, ps32 ACheckId);
typedef s32 (__stdcall* TTestSignalCheckerAddMonotonyRisingWithTrigger)(const TSignalType ASgnType, const char* ASgnName, const s32 ASampleIntervalMs, const TSignalType ATriggerType, const char* ATriggerName, const double ATriggerMin, const double ATriggerMax, ps32 ACheckId);
typedef s32 (__stdcall* TTestSignalCheckerAddMonotonyFallingWithTime)(const TSignalType ASgnType, const char* ASgnName, const s32 ASampleIntervalMs, const double ATimeStartS, const double ATimeEndS, ps32 ACheckId);
typedef s32 (__stdcall* TTestSignalCheckerAddMonotonyFallingWithTrigger)(const TSignalType ASgnType, const char* ASgnName, const s32 ASampleIntervalMs, const TSignalType ATriggerType, const char* ATriggerName, const double ATriggerMin, const double ATriggerMax, ps32 ACheckId);
typedef s32 (__stdcall* TTestSignalCheckerAddFollowWithTime)(const TSignalType ASgnType, const TSignalType AFollowSignalType, const char* ASgnName, const char* AFollowSgnName, const double AErrorRange, const double ATimeStartS, const double ATimeEndS, ps32 ACheckId);
typedef s32 (__stdcall* TTestSignalCheckerAddFollowWithTrigger)(const TSignalType ASgnType, const TSignalType AFollowSignalType, const char* ASgnName, const char* AFollowSgnName, const double AErrorRange, const TSignalType ATriggerType, const char* ATriggerName, const double ATriggerMin, const double ATriggerMax, ps32 ACheckId);
typedef s32 (__stdcall* TTestSignalCheckerAddJumpWithTime)(const TSignalType ASgnType, const char* ASgnName, const bool AIgnoreFrom, const double AFrom, const double ATo, const double ATimeStartS, const double ATimeEndS, ps32 ACheckId);
typedef s32 (__stdcall* TTestSignalCheckerAddJumpWithTrigger)(const TSignalType ASgnType, const char* ASgnName, const bool AIgnoreFrom, const double AFrom, const double ATo, const TSignalType ATriggerType, const char* ATriggerName, const double ATriggerMin, const double ATriggerMax, ps32 ACheckId);
typedef s32 (__stdcall* TTestSignalCheckerAddUnChangeWithTime)(const TSignalType ASgnType, const char* ASgnName, const double ATimeStartS, const double ATimeEndS, ps32 ACheckId);
typedef s32 (__stdcall* TTestSignalCheckerAddUnChangeWithTrigger)(const TSignalType ASgnType, const char* ASgnName, const TSignalType ATriggerType, const char* ATriggerName, const double ATriggerMin, const double ATriggerMax, ps32 ACheckId);
typedef s32 (__stdcall* TTestSignalCheckerCheckStatistics)(const void* AObj, const s32 ACheckId, const double AMin, const double AMax, bool* APass, pdouble AResult, char** AResultRepr);

typedef struct _TTSTest {
    void* FObj;
    // >>> mp test start <<<
    TTestSetVerdictOK                                internal_set_verdict_ok;
    TTestSetVerdictNOK                               internal_set_verdict_nok;
    TTestSetVerdictCOK                               internal_set_verdict_cok;
    TTestLog                                         internal_log_info;
    TTestWriteResultString                           internal_write_result_string;
    TTestWriteResultValue                            internal_write_result_value;
    TTestCheckErrorBegin                             check_error_begin;
    TTestCheckErrorEnd                               check_error_end;
    TTestWriteResultImage                            internal_write_result_image;
    TTestRetrieveCurrentResultFolder                 internal_retrieve_current_result_folder;
    TTestCheckTerminate                              check_test_terminate;
    TTestCheckVerdict                                internal_check_verdict;
    TTestSignalCheckerClear                          signal_checker_clear;
    TTestSignalCheckerAddCheckWithTime               signal_checker_add_check_with_time;
    TTestSignalCheckerAddCheckWithTrigger            signal_checker_add_check_with_trigger;
    TTestSignalCheckerAddStatisticsWithTime          signal_checker_add_statistics_with_time;
    TTestSignalCheckerAddStatisticsWithTrigger       signal_checker_add_statistics_with_trigger;
    TTestSignalCheckerGetResult                      internal_signal_checker_get_result;
    TTestSignalCheckerEnable                         signal_checker_enable;
    TTestDebugLog                                    internal_debug_log_info;
    TTestSignalCheckerAddRisingEdgeWithTime          signal_checker_add_rising_edge_with_time;
    TTestSignalCheckerAddRisingEdgeWithTrigger       signal_checker_add_rising_edge_with_trigger;
    TTestSignalCheckerAddFallingEdgeWithTime         signal_checker_add_falling_edge_with_time;
    TTestSignalCheckerAddFallingEdgeWithTrigger      signal_checker_add_falling_edge_with_trigger;
    TTestSignalCheckerAddMonotonyRisingWithTime      signal_checker_add_monotony_rising_with_time;
    TTestSignalCheckerAddMonotonyRisingWithTrigger   signal_checker_add_monotony_rising_with_trigger;
    TTestSignalCheckerAddMonotonyFallingWithTime     signal_checker_add_monotony_falling_with_time;
    TTestSignalCheckerAddMonotonyFallingWithTrigger  signal_checker_add_monotony_falling_with_trigger;
    TTestSignalCheckerAddFollowWithTime              signal_checker_add_follow_with_time;
    TTestSignalCheckerAddFollowWithTrigger           signal_checker_add_follow_with_trigger;
    TTestSignalCheckerAddJumpWithTime                signal_checker_add_jump_with_time;
    TTestSignalCheckerAddJumpWithTrigger             signal_checker_add_jump_with_trigger;
    TTestSignalCheckerAddUnChangeWithTime            signal_checker_add_unchange_with_time;
    TTestSignalCheckerAddUnChangeWithTrigger         signal_checker_add_unchange_with_trigger;
    TTestSignalCheckerCheckStatistics                internal_signal_checker_check_statistics;
    TTestLogValue                                    internal_log_value;
    // >>> mp test end <<<
    // place holder
    s32                    FDummy[970];
    void set_verdict_ok(const char* AStr) {
        internal_set_verdict_ok(FObj, AStr);
    }
    void set_verdict_nok(const char* AStr) {
        internal_set_verdict_nok(FObj, AStr);
    }
    void set_verdict_cok(const char* AStr) {
        internal_set_verdict_cok(FObj, AStr);
    }
    s32 check_verdict(const char* AName, const double AValue, const double AMin, const double AMax){
        return internal_check_verdict(FObj, AName, AValue, AMin, AMax);
    }
    void log_info(const char* AStr, const TLogLevel ALevel) {
        internal_log_info(FObj, AStr, ALevel);
    }
    void log_value(const char* AStr, const double AValue, const TLogLevel ALevel) {
        internal_log_value(FObj, AStr, AValue, ALevel);
    }
    void debug_log_info(const char* AFile, const char* AFunc, const s32 ALine, const char* AStr, const TLogLevel ALevel) {
        internal_debug_log_info(FObj, AFile, AFunc, ALine, AStr, ALevel);
    }
    void write_result_string(const char* AName, const char* AValue, const TLogLevel ALevel) {
        internal_write_result_string(FObj, AName, AValue, ALevel);
    }
    void write_result_value(const char* AName, const double AValue, const TLogLevel ALevel) {
        internal_write_result_value(FObj, AName, AValue, ALevel);
    }
    s32 write_result_image(const char* AName, const char* AImageFileFullPath) {
        return internal_write_result_image(FObj, AName, AImageFileFullPath);
    }
    s32 retrieve_current_result_folder(char** AFolder) {
        return internal_retrieve_current_result_folder(FObj, AFolder);
    }
    s32 signal_checker_get_result(const s32 ACheckId, bool* APass, pdouble AResult, char** AResultRepr){
        return internal_signal_checker_get_result(FObj, ACheckId, APass, AResult, AResultRepr);
    }
    s32 signal_checker_check_statistics(const s32 ACheckId, const double AMin, const double AMax, bool* APass, pdouble AResult, char** AResultRepr){
        return internal_signal_checker_check_statistics(FObj, ACheckId, AMin, AMax, APass, AResult, AResultRepr);
    }
}TTSTest, * PTSTest;

// TSMaster Configuration ========================================
typedef struct {
    TTSApp  FTSApp;
    TTSCOM  FTSCOM;
    TTSTest FTSTest;
    s32 FDummy[3000];
} TTSMasterConfiguration, *PTSMasterConfiguration;

// Variables definition
extern TTSApp app;
extern TTSCOM com;
extern TTSTest test;

// Utility functions definition
extern void internal_log(const char* AFile, const char* AFunc, const s32 ALine, const TLogLevel ALevel, const char* fmt, ...);
extern void internal_test_log(const char* AFile, const char* AFunc, const s32 ALine, const TLogLevel ALevel, const char* fmt, ...);
extern void test_logCAN(const char* ADesc, PCAN ACAN, const TLogLevel ALevel);
#define log math_log
#if __cplusplus == 201103L
#include <xtgmath.h>
#undef log
#endif
#include <cmath>
#undef log
#include <math.h>
#undef log
#define log(...)           internal_log(__FILE__, __FUNCTION__, __LINE__, lvlInfo, __VA_ARGS__)
#define printf(...)        internal_log(__FILE__, __FUNCTION__, __LINE__, lvlInfo, __VA_ARGS__)
#define log_ok(...)        internal_log(__FILE__, __FUNCTION__, __LINE__, lvlOK, __VA_ARGS__)
#define log_nok(...)       internal_log(__FILE__, __FUNCTION__, __LINE__, lvlError, __VA_ARGS__)
#define log_hint(...)      internal_log(__FILE__, __FUNCTION__, __LINE__, lvlHint, __VA_ARGS__)
#define log_warning(...)   internal_log(__FILE__, __FUNCTION__, __LINE__, lvlWarning, __VA_ARGS__)
#define test_log(...)      internal_test_log(__FILE__, __FUNCTION__, __LINE__, lvlInfo, __VA_ARGS__)
#define test_log_ok(...)   internal_test_log(__FILE__, __FUNCTION__, __LINE__, lvlOK, __VA_ARGS__)
#define test_log_nok(...)  internal_test_log(__FILE__, __FUNCTION__, __LINE__, lvlError, __VA_ARGS__)

#pragma pack(pop)

// API error codes
#define IDX_ERR_OK                                         0    /* OK */ 
#define IDX_ERR_IDX_OUT_OF_RANGE                           1    /* Index out of range */ 
#define IDX_ERR_CONNECT_FAILED                             2    /* Connect failed */ 
#define IDX_ERR_DEV_NOT_FOUND                              3    /* Device not found */ 
#define IDX_ERR_CODE_NOT_VALID                             4    /* Error code not valid */ 
#define IDX_ERR_ALREADY_CONNECTED                          5    /* HID device already connected */ 
#define IDX_ERR_HID_WRITE_FAILED                           6    /* HID write data failed */ 
#define IDX_ERR_HID_READ_FAILED                            7    /* HID read data failed */ 
#define IDX_ERR_HID_TX_BUFF_OVERRUN                        8    /* HID TX buffer overrun */ 
#define IDX_ERR_HID_TX_TOO_LARGE                           9    /* HID TX buffer too large */ 
#define IDX_ERR_PACKET_ID_INVALID                          10   /* HID RX packet report ID invalid */  
#define IDX_ERR_PACKET_LEN_INVALID                         11   /* HID RX packet length invalid */  
#define IDX_ERR_INTERNAL_TEST_FAILED                       12   /* Internal test failed */  
#define IDX_ERR_RX_PACKET_LOST                             13   /* RX packet lost */  
#define IDX_ERR_HID_SETUP_DI                               14   /* SetupDiGetDeviceInterfaceDetai */  
#define IDX_ERR_HID_CREATE_FILE                            15   /* Create file failed */  
#define IDX_ERR_HID_READ_HANDLE                            16   /* CreateFile failed for read handle */  
#define IDX_ERR_HID_WRITE_HANDLE                           17   /* CreateFile failed for write handle */  
#define IDX_ERR_HID_SET_INPUT_BUFF                         18   /* HidD_SetNumInputBuffers */  
#define IDX_ERR_HID_GET_PREPAESED                          19   /* HidD_GetPreparsedData */  
#define IDX_ERR_HID_GET_CAPS                               20   /* HidP_GetCaps */  
#define IDX_ERR_HID_WRITE_FILE                             21   /* WriteFile */  
#define IDX_ERR_HID_GET_OVERLAPPED                         22   /* GetOverlappedResult */  
#define IDX_ERR_HID_SET_FEATURE                            23   /* HidD_SetFeature */  
#define IDX_ERR_HID_GET_FEATURE                            24   /* HidD_GetFeature */  
#define IDX_ERR_HID_DEVICE_IO_CTRL                         25   /* Send Feature Report DeviceIoContro */  
#define IDX_ERR_HID_SEND_FEATURE_RPT                       26   /* Send Feature Report GetOverLappedResult */  
#define IDX_ERR_HID_GET_MANU_STR                           27   /* HidD_GetManufacturerString */  
#define IDX_ERR_HID_GET_PROD_STR                           28   /* HidD_GetProductString */  
#define IDX_ERR_HID_GET_SERIAL_STR                         29   /* HidD_GetSerialNumberString */  
#define IDX_ERR_HID_GET_INDEXED_STR                        30   /* HidD_GetIndexedString */  
#define IDX_ERR_TX_TIMEDOUT                                31   /* Transmit timed out */  
#define IDX_ERR_HW_DFU_WRITE_FLASH_FAILED                  32   /* HW DFU flash write failed */  
#define IDX_ERR_HW_DFU_WRITE_WO_ERASE                      33   /* HW DFU write without erase */  
#define IDX_ERR_HW_DFU_CRC_CHECK_ERROR                     34   /* HW DFU crc check error */  
#define IDX_ERR_HW_DFU_COMMAND_TIMED_OUT                   35   /* HW DFU reset before crc check success */  
#define IDX_ERR_HW_PACKET_ID_INVALID                       36   /* HW packet identifier invalid */  
#define IDX_ERR_HW_PACKET_LEN_INVALID                      37   /* HW packet length invalid */  
#define IDX_ERR_HW_INTERNAL_TEST_FAILED                    38   /* HW internal test failed */  
#define IDX_ERR_HW_RX_FROM_PC_PACKET_LOST                  39   /* HW rx from pc packet lost */  
#define IDX_ERR_HW_TX_TO_PC_BUFF_OVERRUN                   40   /* HW tx to pc buffer overrun */  
#define IDX_ERR_HW_API_PAEAMETER_INVALID                   41   /* HW API parameter invalid */  
#define IDX_ERR_DFU_FILE_LOAD_FAILED                       42   /* DFU file load failed */  
#define IDX_ERR_DFU_HEADER_WRITE_FAILED                    43   /* DFU header write failed */  
#define IDX_ERR_READ_STATUS_TIMEDOUT                       44   /* Read status timed out */  
#define IDX_ERR_CALLBACK_ALREADY_EXISTS                    45   /* Callback already exists */  
#define IDX_ERR_CALLBACK_NOT_EXISTS                        46   /* Callback not exists */  
#define IDX_ERR_FILE_INVALID                               47   /* File corrupted or not recognized */  
#define IDX_ERR_DB_ID_NOT_FOUND                            48   /* Database unique id not found */  
#define IDX_ERR_SW_API_PAEAMETER_INVALID                   49   /* Software API parameter invalid */  
#define IDX_ERR_SW_API_GENERIC_TIMEOUT                     50   /* Software API generic timed out */  
#define IDX_ERR_SW_API_SET_CONF_FAILED                     51   /* Software API set hw config. failed */  
#define IDX_ERR_SW_API_INDEX_OUT_OF_BOUNDS                 52   /* Index out of bounds */  
#define IDX_ERR_SW_API_WAIT_TIMEOUT                        53   /* RX wait timed out */  
#define IDX_ERR_SW_API_GET_IO_FAILED                       54   /* Get I/O failed */  
#define IDX_ERR_SW_API_SET_IO_FAILED                       55   /* Set I/O failed */  
#define IDX_ERR_SW_API_REPLAY_ON_GOING                     56   /* An active replay is already running */  
#define IDX_ERR_SW_API_INSTANCE_NOT_EXISTS                 57   /* Instance not exists */  
#define IDX_ERR_HW_CAN_TRANSMIT_FAILED                     58   /* CAN message transmit failed */  
#define IDX_ERR_HW_NO_RESPONSE                             59   /* No response from hardware */  
#define IDX_ERR_SW_CAN_MSG_NOT_FOUND                       60   /* CAN message not found */  
#define IDX_ERR_SW_CAN_RECV_BUFFER_EMPTY                   61   /* User CAN receive buffer empty */  
#define IDX_ERR_SW_CAN_RECV_PARTIAL_READ                   62   /* CAN total receive count <> desired count */  
#define IDX_ERR_SW_API_LINCONFIG_FAILED                    63   /* LIN config failed */  
#define IDX_ERR_SW_API_FRAMENUM_OUTOFRANGE                 64   /* LIN frame number out of range */  
#define IDX_ERR_SW_API_LDFCONFIG_FAILED                    65   /* LDF config failed */  
#define IDX_ERR_SW_API_LDFCONFIG_CMDERR                    66   /* LDF config cmd error */  
#define IDX_ERR_SW_ENV_NOT_READY                           67   /* TSMaster envrionment not ready */  
#define IDX_ERR_SECURITY_FAILED                            68   /* reserved failed */  
#define IDX_ERR_XL_ERROR                                   69   /* XL driver error */  
#define IDX_ERR_SEC_INDEX_OUTOFRANGE                       70   /* index out of range */  
#define IDX_ERR_STRINGLENGTH_OUTFOF_RANGE                  71   /* string length out of range */  
#define IDX_ERR_KEY_IS_NOT_INITIALIZATION                  72   /* key is not initialized */  
#define IDX_ERR_KEY_IS_WRONG                               73   /* key is wrong */  
#define IDX_ERR_NOT_PERMIT_WRITE                           74   /* write not permitted */  
#define IDX_ERR_16BYTES_MULTIPLE                           75   /* 16 bytes multiple */  
#define IDX_ERR_LIN_CHN_OUTOF_RANGE                        76   /* LIN channel out of range */  
#define IDX_ERR_DLL_NOT_READY                              77   /* DLL not ready */  
#define IDX_ERR_FEATURE_NOT_SUPPORTED                      78   /* Feature not supported */  
#define IDX_ERR_COMMON_SERV_ERROR                          79   /* common service error */  
#define IDX_ERR_READ_PARA_OVERFLOW                         80   /* read parameter overflow */  
#define IDX_ERR_INVALID_CHANNEL_MAPPING                    81   /* Invalid application channel mapping */  
#define IDX_ERR_TSLIB_GENERIC_OPERATION_FAILED             82   /* libTSMaster generic operation failed */  
#define IDX_ERR_TSLIB_ITEM_ALREADY_EXISTS                  83   /* item already exists */  
#define IDX_ERR_TSLIB_ITEM_NOT_FOUND                       84   /* item not found */  
#define IDX_ERR_TSLIB_LOGICAL_CHANNEL_INVALID              85   /* logical channel invalid */  
#define IDX_ERR_FILE_NOT_EXISTS                            86   /* file not exists */  
#define IDX_ERR_NO_INIT_ACCESS                             87   /* no init access, cannot set baudrate */  
#define IDX_ERR_CHN_NOT_ACTIVE                             88   /* the channel is inactive */  
#define IDX_ERR_CHN_NOT_CREATED                            89   /* the channel is not created */  
#define IDX_ERR_APPNAME_LENGTH_OUT_OF_RANGE                90   /* length of the appname is out of range */  
#define IDX_ERR_PROJECT_IS_MODIFIED                        91   /* project is modified */  
#define IDX_ERR_SIGNAL_NOT_FOUND_IN_DB                     92   /* signal not found in database */  
#define IDX_ERR_MESSAGE_NOT_FOUND_IN_DB                    93   /* message not found in database */  
#define IDX_ERR_TSMASTER_IS_NOT_INSTALLED                  94   /* TSMaster is not installed */  
#define IDX_ERR_LIB_LOAD_FAILED                            95   /* Library load failed */  
#define IDX_ERR_LIB_FUNCTION_NOT_FOUND                     96   /* Library function not found */  
#define IDX_ERR_LIB_NOT_INITIALIZED                        97   /* cannot find libTSMaster.dll, use "set_libtsmaster_location" to set its location before calling initialize_lib_tsmaster */  
#define IDX_ERR_PCAN_GENRIC_ERROR                          98   /* PCAN generic operation error */  
#define IDX_ERR_KVASER_GENERIC_ERROR                       99   /* Kvaser generic operation error */  
#define IDX_ERR_ZLG_GENERIC_ERROR                          100  /* ZLG generic operation error */   
#define IDX_ERR_ICS_GENERIC_ERROR                          101  /* ICS generic operation error */   
#define IDX_ERR_TC1005_GENERIC_ERROR                       102  /* TC1005 generic operation error */   
#define IDX_ERR_SYSTEM_VAR_NOT_FOUND                       103  /* System variable not found */   
#define IDX_ERR_INCORRECT_SYSTEM_VAR_TYPE                  104  /* Incorrect system variable type */   
#define IDX_ERR_CYCLIC_MSG_NOT_EXIST                       105  /* Message not existing, update failed */   
#define IDX_ERR_BAUD_NOT_AVAIL                             106  /* Specified baudrate not available */   
#define IDX_ERR_DEV_NOT_SUPPORT_SYNC_SEND                  107  /* Device does not support sync. transmit */   
#define IDX_ERR_MP_WAIT_TIME_NOT_SATISFIED                 108  /* Wait time not satisfied */   
#define IDX_ERR_CANNOT_OPERATE_WHILE_CONNECTED             109  /* Cannot operate while app is connected */   
#define IDX_ERR_CREATE_FILE_FAILED                         110  /* Create file failed */   
#define IDX_ERR_PYTHON_EXECUTE_FAILED                      111  /* Execute python failed */   
#define IDX_ERR_SIGNAL_MULTIPLEXED_NOT_ACTIVE              112  /* Current multiplexed signal is not active */   
#define IDX_ERR_GET_HANDLE_BY_CHANNEL_FAILED               113  /* Get handle by logic channel failed */   
#define IDX_ERR_CANNOT_OPERATE_WHILE_APP_CONN              114  /* Cannot operate while application is connected, please stop application first */   
#define IDX_ERR_FILE_LOAD_FAILED                           115  /* File load failed */   
#define IDX_ERR_READ_LINDATA_FAILED                        116  /* Read LIN Data Failed */   
#define IDX_ERR_FIFO_NOT_ENABLED                           117  /* FIFO not enabled */   
#define IDX_ERR_INVALID_HANDLE                             118  /* Invalid handle */   
#define IDX_ERR_READ_FILE_ERROR                            119  /* Read file error */   
#define IDX_ERR_READ_TO_EOF                                120  /* Read to EOF */   
#define IDX_ERR_CONF_NOT_SAVED                             121  /* Configuration not saved */   
#define IDX_ERR_IP_PORT_OPEN_FAILED                        122  /* IP port open failed */   
#define IDX_ERR_IP_TCP_CONNECT_FAILED                      123  /* TCP connect failed */   
#define IDX_ERR_DIR_NOT_EXISTS                             124  /* Directory not exists */   
#define IDX_ERR_CURRENT_LIB_NOT_SUPPORTED                  125  /* Current library not supported */   
#define IDX_ERR_TEST_NOT_RUNNING                           126  /* Test is not running */   
#define IDX_ERR_SERV_RESPONSE_NOT_RECV                     127  /* Server response not received */   
#define IDX_ERR_CREATE_DIR_FAILED                          128  /* Create directory failed */   
#define IDX_ERR_INCORRECT_ARGUMENT_TYPE                    129  /* Invalid argument type */   
#define IDX_ERR_READ_DATA_PACKAGE_OVERFLOW                 130  /* Read Data Package from Device Failed */   
#define IDX_ERR_REPLAY_IS_ALREADY_RUNNING                  131  /* Precise replay is running */   
#define IDX_ERR_REPALY_MAP_ALREADY_EXIST                   132  /* Replay map is already */   
#define IDX_ERR_USER_CANCEL_INPUT                          133  /* User cancel input */   
#define IDX_ERR_API_CHECK_FAILED                           134  /* API check result is negative */   
#define IDX_ERR_CANABLE_GENERIC_ERROR                      135  /* CANable generic error */   
#define IDX_ERR_WAIT_CRITERIA_NOT_SATISFIED                136  /* Wait criteria not satisfied */   
#define IDX_ERR_REQUIRE_APP_CONNECTED                      137  /* Operation requires application connected */   
#define IDX_ERR_PROJECT_PATH_ALREADY_USED                  138  /* Project path is used by another application */   
#define IDX_ERR_TP_TIMEOUT_AS                              139  /* Timeout for the sender to transmit data to the receiver */   
#define IDX_ERR_TP_TIMEOUT_AR                              140  /* Timeout for the receiver to transmit flow control to the sender */   
#define IDX_ERR_TP_TIMEOUT_BS                              141  /* Timeout for the sender to send first data frame after receiving FC frame */   
#define IDX_ERR_TP_TIMEOUT_CR                              142  /* Timeout for the receiver to receiving first CF frame after sending FC frame */   
#define IDX_ERR_TP_WRONG_SN                                143  /* Serial Number Error */   
#define IDX_ERR_TP_INVALID_FS                              144  /* Invalid flow status of the flow control frame */   
#define IDX_ERR_TP_UNEXP_PDU                               145  /* Unexpected Protocol Data Unit */   
#define IDX_ERR_TP_WFT_OVRN                                146  /* Wait counter of the FC frame out of the maxWFT */   
#define IDX_ERR_TP_BUFFER_OVFLW                            147  /* Buffer of the receiver is overflow */   
#define IDX_ERR_TP_NOT_IDLE                                148  /* TP Module is busy */   
#define IDX_ERR_TP_ERROR_FROM_CAN_DRIVER                   149  /* There is error from CAN Driver */   
#define IDX_ERR_TP_HANDLE_NOT_EXIST                        150  /* Handle of the TP Module is not exist */   
#define IDX_ERR_UDS_EVENT_BUFFER_IS_FULL                   151  /* UDS event buffer is full */   
#define IDX_ERR_UDS_HANDLE_POOL_IS_FULL                    152  /* Handle pool is full, can not add new UDS module */   
#define IDX_ERR_UDS_NULL_POINTER                           153  /* Pointer of UDS module is null */   
#define IDX_ERR_UDS_MESSAGE_INVALID                        154  /* UDS message is invalid */   
#define IDX_ERR_UDS_NO_DATA                                155  /* No uds data received */   
#define IDX_ERR_UDS_MODULE_NOT_EXISTING                    156  /* Handle of uds is not existing */   
#define IDX_ERR_UDS_MODULE_NOT_READY                       157  /* UDS module is not ready */   
#define IDX_ERR_UDS_SEND_DATA_FAILED                       158  /* Transmit UDS frame data failed */   
#define IDX_ERR_UDS_NOT_SUPPORTED                          159  /* This UDS Service is not supported */   
#define IDX_ERR_UDS_TIMEOUT_SENDING_REQUEST                160  /* Timeout to send uds request */   
#define IDX_ERR_UDS_TIMEOUT_GET_RESPONSE                   161  /* Timeout to get uds response */   
#define IDX_ERR_UDS_NEGATIVE_RESPONSE                      162  /* Get uds negative response */   
#define IDX_ERR_UDS_NEGATIVE_WITH_EXPECTED_NRC             163  /* Get uds negative response with expected NRC */   
#define IDX_ERR_UDS_NEGATIVE_UNEXPECTED_NRC                164  /* Get uds negative response with unexpected NRC */   
#define IDX_ERR_UDS_CANTOOL_NOT_READY                      165  /* UDS CAN Tool is not ready */   
#define IDX_ERR_UDS_DATA_OUTOF_RANGE                       166  /* UDS Dta outof range */   
#define IDX_ERR_UDS_UNEXPECTED_FRAME                       167  /* Get Unexpected UDS frame */   
#define IDX_ERR_UDS_UNEXPECTED_POSTIVE_RESPONSE            168  /* Receive unpexted positive response frame */   
#define IDX_ERR_UDS_POSITIVE_REPONSE_WITH_WRONG_DATA       169  /* Receive positive response with wrong data */   
#define IDX_ERR_UDS_GET_POSITIVE_RESPONSE_FAILED           170  /* Failed to get positive response */   
#define IDX_ERR_UDS_MaxNumOfBlockLen_OVER_FLOW             171  /* MaxNumOfBlockLen out of range */   
#define IDX_ERR_UDS_NEGATIVE_RESPONSE_WITH_UNEXPECTED_NRC  172  /* Receive negative response with unexpected NRC */   
#define IDX_ERR_UDS_SERVICE_IS_RUNNING                     173  /* UDS serive is busy */   
#define IDX_ERR_UDS_NEED_APPLY_DOWNLOAD_FIRST              174  /* Apply download first before transfer data */   
#define IDX_ERR_UDS_RESPONSE_DATA_LENGTH_ERR               175  /* Length of the uds reponse is wrong */   
#define IDX_ERR_TEST_CHECK_LOWER                           176  /* Verdict value smaller than specification */   
#define IDX_ERR_TEST_CHECK_UPPER                           177  /* Verdict value greater than specification */   
#define IDX_ERR_TEST_VERDICT_CHECK_FAILED                  178  /* Verdict check failed */
#define IDX_ERR_AM_NOT_LOADED                              179  /* Automation module not loaded, please load it first */
#define IDX_ERR_PANEL_NOT_FOUND                            180  /* Panel not found */
#define IDX_ERR_CONTROL_NOT_FOUND_IN_PANEL                 181  /* Control not found in panel */
#define IDX_ERR_PANEL_NOT_LOADED                           182  /* Panel not loaded, please load it first */
#define IDX_ERR_STIM_SIGNAL_NOT_FOUND                      183  /* STIM signal not found */
#define IDX_ERR_AM_SUB_MODULE_NOT_AVAIL                    184  /* Automation sub module not available */
#define IDX_ERR_AM_VARIANT_GROUP_NOT_FOUND                 185  /* Automation variant group not found */
#define IDX_ERR_PANEL_CONTROL_NOT_FOUND                    186  /* Control not found in panel */
#define IDX_ERR_PANEL_CONTROL_NOT_SUPPORT_THIS             187  /* Panel control does not support this property */
#define IDX_ERR_RBS_NOT_RUNNING                            188  /* RBS engine is not running */
#define IDX_ERR_MSG_NOT_SUPPORT_PDU_CONTAINER              189  /* This message does not support PDU container */
#define IDX_ERR_DATA_NOT_AVAILABLE                         190  /* Data not available */
#define IDX_ERR_J1939_NOT_SUPPORTED                        191  /* J1939 not supported */
#define IDX_ERR_J1939_ANOTHER_PDU_IS_SENDING               192  /* Transmit J1939 PDU failed due to another PDU is already being transmitted */
#define IDX_ERR_J1939_TX_FAILED_PROTOCOL_ERROR             193  /* Transmit J1939 PDU failed due to protocol error */
#define IDX_ERR_J1939_TX_FAILED_NODE_INACTIVE              194  /* Transmit J1939 PDU failed due to node inactive */
#define IDX_ERR_NO_LICENSE                                 195  /* API is called without license support*/
#define IDX_ERR_SIGNAL_CHECK_RANGE_VIOLATION               196  /* Signal range check violation */
#define IDX_ERR_LOG_READ_CATEGORY_FAILED                   197  /* DataLogger read category failed */
#define IDX_ERR_CHECK_BOOT_VERSION_FAILED                  198  /* Check Flash Bootloader Version Failed */
#define IDX_ERR_LOG_FILE_NOT_CREATED                       199  /* Log file not created */
#define IDX_ERR_MODULE_IS_BEING_EDITED_BY_USER             200  /* the current module is being edited by user in dialog */
#define IDX_ERR_LOG_DEVICE_IS_BUSY                         201  /* The Logger device is busy, can not operation at the same time */
#define IDX_ERR_LIN_MASTER_TRANSMIT_N_AS_TIMEOUT           202  /* Master node transmit diagnostic package timeout */
#define IDX_ERR_LIN_MASTER_TRANSMIT_TRANSMIT_ERROR         203  /* Master node transmit frame failed */
#define IDX_ERR_LIN_MASTER_REV_N_CR_TIMEOUT                204  /* Master node receive diagnostic package timeout */
#define IDX_ERR_LIN_MASTER_REV_ERROR                       205  /* Master node receive frame failed */
#define IDX_ERR_LIN_MASTER_REV_INTERLLEAVE_TIMEOUT         206  /* Internal time runs out before reception is completed */
#define IDX_ERR_LIN_MASTER_REV_NO_RESPONSE                 207  /* Master node received no response */
#define IDX_ERR_LIN_MASTER_REV_SN_ERROR                    208  /* Serial Number Error when receiving multi frames */
#define IDX_ERR_LIN_SLAVE_TRANSMIT_N_CR_TIMEOUT            209  /* Slave node transmit diagnostic package timeout */
#define IDX_ERR_LIN_SLAVE_REV_N_CR_TIMEOUT                 210  /* Slave node receive diagnostic pacakge timeout */
#define IDX_ERR_LIN_SLAVE_TRANSMIT_ERROR                   211  /* Slave node transmit frames error */
#define IDX_ERR_LIN_SLAVE_REV_ERROR                        212  /* Slave node receive frames error */
#define IDX_ERR_CLOSE_FILE_FAILED                          213  /* Close file failed */
#define IDX_ERR_CONF_LOG_FILE_FAILED                       214  /* Configure log file failed */
#define IDX_ERR_CONVERT_LOG_FAILED                         215  /* Convert log file failed */
#define IDX_ERR_HALTED_DUE_TO_USER_BREAK                   216  /* Operation halted due to user break */
#define IDX_ERR_WRITE_FILE_FAILED                          217  /* Write file failed */
#define IDX_ERR_UNKNOWN_OBJECT_DETECTED                    218  /* Unknown object detected */
#define IDX_ERR_THIS_FUNC_SHOULD_BE_CALLED_IN_MP           219  /* this function should be called in mini program thread */
#define IDX_ERR_USER_CANCEL_WAIT                           220  /* user canceled wait */
#define IDX_ERR_DECOMPRESS_DATA_FAILED                     221  /* Decompress data failed */
#define IDX_ERR_AUTOMATION_OBJ_NOT_CREATED                 222  /* Automation object not created */
#define IDX_ERR_ITEM_DUPLICATED                            223  /* Item duplicated */
#define IDX_ERR_DIVIDE_BY_ZERO                             224  /* Divide by zero */
#define IDX_ERR_REQUIRE_MINI_PROGRAM_RUNNING               225  /* This operation requires mini program running */
#define IDX_ERR_FORM_NOT_EXIST                             226  /* Form not exists */
#define IDX_ERR_CANNOT_CONFIG_WHEN_DEVICE_RUNNING          227  /* Can not config when the device is running */
#define IDX_ERR_DATA_NOT_READY                             228  /* The data of the device is not ready */
#define IDX_ERR_STOP_DEVICE_FAILED                         229  /* Stop device failed */
#define IDX_ERR_PYTHON_CODE_CRASH                          230  /* Python code crashed */

// Software Constants
#define CONST_LOG_ERROR                                    1    /* error message will be displayed with red color */
#define CONST_LOG_WARNING                                  2    /* warning message will be displayed with blue color */
#define CONST_LOG_OK                                       3    /* OK message will be displayed with green color */
#define CONST_LOG_HINT                                     4    /* hint message will be displayed with yellow color */
#define CONST_LOG_INFO                                     5    /* info. message will be displayed with black color */
#define CONST_LOG_VERBOSE                                  6    /* verbose message will be displayed with gray color */
#define CONST_CH1                                          0    /* Channel 1 index */
#define CONST_CH2                                          1    /* Channel 2 index */
#define CONST_CH3                                          2    /* Channel 3 index */
#define CONST_CH4                                          3    /* Channel 4 index */
#define CONST_CH5                                          4    /* Channel 5 index */
#define CONST_CH6                                          5    /* Channel 6 index */
#define CONST_CH7                                          6    /* Channel 7 index */
#define CONST_CH8                                          7    /* Channel 8 index */
#define CONST_CH9                                          8    /* Channel 9 index */
#define CONST_CH10                                         9    /* Channel 10 index */
#define CONST_CH11                                         10   /* Channel 11 index */
#define CONST_CH12                                         11   /* Channel 12 index */
#define CONST_CH13                                         12   /* Channel 13 index */
#define CONST_CH14                                         13   /* Channel 14 index */
#define CONST_CH15                                         14   /* Channel 15 index */
#define CONST_CH16                                         15   /* Channel 16 index */
#define CONST_CH17                                         16   /* Channel 17 index */
#define CONST_CH18                                         17   /* Channel 18 index */
#define CONST_CH19                                         18   /* Channel 19 index */
#define CONST_CH20                                         19   /* Channel 20 index */
#define CONST_CH21                                         20   /* Channel 21 index */
#define CONST_CH22                                         21   /* Channel 22 index */
#define CONST_CH23                                         22   /* Channel 23 index */
#define CONST_CH24                                         23   /* Channel 24 index */
#define CONST_CH25                                         24   /* Channel 25 index */
#define CONST_CH26                                         25   /* Channel 26 index */
#define CONST_CH27                                         26   /* Channel 27 index */
#define CONST_CH28                                         27   /* Channel 28 index */
#define CONST_CH29                                         28   /* Channel 29 index */
#define CONST_CH30                                         29   /* Channel 30 index */
#define CONST_CH31                                         30   /* Channel 31 index */
#define CONST_CH32                                         31   /* Channel 32 index */
#define CONST_BUS_UNKNOWN_TYPE                             0    /* device type - unknown */ 
#define CONST_TS_TCP_DEVICE                                1    /* device type - TS Virtual Channel */ 
#define CONST_XL_USB_DEVICE                                2    /* device type - XL USB Device */ 
#define CONST_TS_USB_DEVICE                                3    /* device type - TS USB Device */ 
#define CONST_PEAK_USB_DEVICE                              4    /* device type - PEAK USB Device */ 
#define CONST_KVASER_USB_DEVICE                            5    /* device type - Kvaser USB Device */ 
#define CONST_ZLG_USB_DEVICE                               6    /* device type - ZLG USB Device */ 
#define CONST_ICS_USB_DEVICE                               7    /* device type - ICS USB Device */ 
#define CONST_TS_TC1005_DEVICE                             8    /* device type - TS TC1005 Device */ 
#define CONST_STIM_STOPPED                                 0    /* STIM Signal - Stopped State */ 
#define CONST_STIM_RUNNING                                 1    /* STIM Signal - Running State */ 
#define CONST_STIM_PAUSED                                  2    /* STIM Signal - Paused State */ 
#define CONST_AM_NOT_RUN                                   0    /* Automation Module - not running state */
#define CONST_AM_PREPARE_RUN                               1    /* Automation Module - Prepare running state */
#define CONST_AM_RUNNING                                   2    /* Automation Module - Running state */
#define CONST_AM_PAUSED                                    3    /* Automation Module - Paused state */
#define CONST_AM_STEPPING                                  4    /* Automation Module - Stepping state */
#define CONST_AM_FINISHED                                  5    /* Automation Module - Finished state */
#define CONST_SIGNAL_TYPE_CAN                              0    /* Signal Checker - TSignalType.stCANSignal */
#define CONST_SIGNAL_TYPE_LIN                              1    /* Signal Checker - TSignalType.stLINSignal */
#define CONST_SIGNAL_TYPE_SYSTEM_VAR                       2    /* Signal Checker - TSignalType.stSystemVar */
#define CONST_SIGNAL_TYPE_FLEXRAY                          3    /* Signal Checker - TSignalType.stFlexRay */
#define CONST_SIGNAL_TYPE_ETHERNET                         4    /* Signal Checker - TSignalType.stEthernet */
#define CONST_SIGNAL_CHECK_ALWAYS                          0    /* Signal Checker - TSignalCheckKind.sckAlways */
#define CONST_SIGNAL_CHECK_APPEAR                          1    /* Signal Checker - TSignalCheckKind.sckAppear */
#define CONST_SIGNAL_CHECK_STATISTICS                      2    /* Signal Checker - TSignalCheckKind.sckStatistics */
#define CONST_SIGNAL_CHECK_RISING_EDGE                     3    /* Signal Checker - TSignalCheckKind.sckRisingEdge */
#define CONST_SIGNAL_CHECK_FALLING_EDGE                    4    /* Signal Checker - TSignalCheckKind.sckFallingEdge */
#define CONST_SIGNAL_CHECK_MONOTONY_RISING                 5    /* Signal Checker - TSignalCheckKind.sckMonotonyRising */
#define CONST_SIGNAL_CHECK_MONOTONY_FALLING                6    /* Signal Checker - TSignalCheckKind.sckMonotonyFalling */
#define CONST_SIGNAL_CHECK_FOLLOW                          7    /* Signal Checker - TSignalCheckKind.sckFollow */
#define CONST_STATISTICS_MIN                               0    /* Signal Checker - TSignalStatisticsKind.sskMin */
#define CONST_STATISTICS_MAX                               1    /* Signal Checker - TSignalStatisticsKind.sskMax */
#define CONST_STATISTICS_AVERAGE                           2    /* Signal Checker - TSignalStatisticsKind.sskAverage */
#define CONST_SYMBOL_MAPPING_DIR_BIDIRECTION               0    /* Symbol mapping direction - bidirection */
#define CONST_SYMBOL_MAPPING_DIR_SGN_TO_SYSVAR             1    /* Symbol mapping direction - from signal to sys var */
#define CONST_SYMBOL_MAPPING_DIR_SYSVAR_TO_SGN             2    /* Symbol mapping direction - from sys var to signal */

#endif
