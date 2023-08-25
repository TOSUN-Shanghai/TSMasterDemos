#ifndef _TSMaster_H
#define _TSMaster_H

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

typedef enum { lvlError = 1, lvlWarning = 2, lvlOK = 3, lvlHint = 4, lvlInfo = 5, lvlVerbose = 6 } TLogLevel;

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

#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))

#ifdef DLLTEST_EXPORT
#define TSAPI(ret) __declspec(dllexport) ret __stdcall
#else
#define TSAPI(ret) __declspec(dllimport) ret __stdcall
#endif

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
#define DATABASE_STR_LEN 512
typedef struct _TCANSignal {
	u8     FCANSgnType; // 0 - Unsigned, 1 - Signed, 2 - Single 32, 3 - Double 64
	bool   FIsIntel;
	s32    FStartBit;
	s32    FLength;
	double FFactor;
	double FOffset;
} TCANSignal, * PCANSignal;
// LIN signal record, size = 26
typedef struct _TLINSignal {
	u8     FLINSgnType; // 0 - Unsigned, 1 - Signed, 2 - Single 32, 3 - Double 64
	bool   FIsIntel;
	s32    FStartBit;
	s32    FLength;
	double FFactor;
	double FOffset;
} TLINSignal, * PLINSignal;
// FlexRay signal record, size = 32
typedef struct _TFlexRaySignal {
	u8     FFRSgnType;   // 0 - Unsigned, 1 - Signed, 2 - Single 32, 3 - Double 64
	u8     FCompuMethod; // 0 - Identical, 1 - Linear, 2 - Scale Linear, 3 - TextTable, 4 - TABNoIntp, 5 - Formula
	u8     FReserved;
	bool   FIsIntel;
	s32    FStartBit;
	s32    FUpdateBit;
	s32    FLength;
	double FFactor;
	double FOffset;
	s32    FActualStartBit;
	s32    FActualUpdateBit;
} TFlexRaySignal, * PFlexRaySignal;

typedef struct _TDBProperties {
	s32 FDBIndex;
	s32 FSignalCount;
	s32 FFrameCount;
	s32 FECUCount;
	u64 FSupportedChannelMask;
	char FName[DATABASE_STR_LEN];
	char FComment[DATABASE_STR_LEN];
	u64 FFlags;
} TDBProperties, * PDBProperties;

// TDBECUProperties for database ECU properties, size = 1040
typedef struct _TDBECUProperties {
	s32 FDBIndex;
	s32 FECUIndex;
	s32 FTxFrameCount;
	s32 FRxFrameCount;
	char FName[DATABASE_STR_LEN];
	char FComment[DATABASE_STR_LEN];
} TDBECUProperties, * PDBECUProperties;

typedef struct _TDBFrameProperties {
	s32 FDBIndex;
	s32 FECUIndex;
	s32 FFrameIndex;
	u8  FIsTx;
	u8  FReserved1;
	u8  FReserved2;
	u8  FReserved3;
	s32 FFrameType;
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
} TDBFrameProperties, * PDBFrameProperties;
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
	s32    FSignalType;
	TCANSignal     FCANSignal;
	TLINSignal     FLINSignal;
	TFlexRaySignal FFlexRaySignal;
	s32            FParentFrameId;
	double         FInitValue;
	char FName[DATABASE_STR_LEN];
	char FComment[DATABASE_STR_LEN];
} TDBSignalProperties, * PDBSignalProperties;
typedef struct _TLIBGPSData
{
	u64 FTimeUS;

	u32 UTCTime;
	u32 UTCDate;

	float Latitude;

	float Longitude;

	float Speed;

	float Direct;

	float Altitude;

	u8 N_S;

	u8 E_W;

	u8 Satellite;

	u8 FIdxChn;
}TLIBGPSData, * PLIBGPSData;
// CAN frame type ================================================
typedef struct _TCAN {
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
		}
		else {
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
		}
		else {
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
		}
		else {
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
		}
		else {
			FProperties = FProperties | MASK_CANProp_ERROR;
		}
	}
	// load data bytes -------------------------------------------
	void load_data_array(u8* a) {
		for (u32 i = 0; i < 8; i++) {
			FData[i] = *a++;
		}
	}
	void set_data(const u8 d0, const u8 d1, const u8 d2, const u8 d3, const u8 d4, const u8 d5, const u8 d6, const u8 d7) {
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
} TCAN, * PCAN;

// CAN FD frame type =============================================
typedef struct _TCANFD {
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
		}
		else {
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
		}
		else {
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
		}
		else {
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
		}
		else {
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
		}
		else {
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
		}
		else {
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
		}
		else {
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
	TCAN to_tcan(void) {
		return *(TCAN*)(&FIdxChn);
	}
} TCANFD, * PCANFD;

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
} TLIN, * PLIN;

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
typedef void(__stdcall* TProcedure)(const void* AObj);
typedef void(__stdcall* TProcedureSetInt)(const void* AObj, const s32 AValue);
typedef s32(__stdcall* TIntFunction)(const void* AObj);
typedef void(__stdcall* TProcedureSetDouble)(const void* AObj, const double AValue);
typedef double(__stdcall* TDoubleFunction)(const void* AObj);
typedef void(__stdcall* TProcedureSetString)(const void* AObj, const char* AValue);
typedef char* (__stdcall* TStringFunction)(const void* AObj);
typedef void(__stdcall* TProcedureSetCAN)(const void* AObj, const PCAN AValue);
typedef TCAN(__stdcall* TTCANFunction)(const void* AObj);
typedef void(__stdcall* TProcedureSetCANFD)(const void* AObj, const PCANFD AValue);
typedef TCANFD(__stdcall* TTCANFDFunction)(const void* AObj);
typedef void(__stdcall* TProcedureSetLIN)(const void* AObj, const PLIN AValue);
typedef TLIN(__stdcall* TTLINFunction)(const void* AObj);

// TSMaster application definition ===============================
#define APP_DEVICE_NAME_LENGTH 32
typedef enum {
	BUS_UNKNOWN_TYPE = 0,
	TS_TCP_DEVICE = 1,
	XL_USB_DEVICE = 2,
	TS_USB_DEVICE = 3,
	PEAK_USB_DEVICE = 4,
	KVASER_USB_DEVICE = 5,
	ZLG_USB_DEVICE = 6,
	ICS_USB_DEVICE = 7,
	TS_TC1005_DEVICE = 8
} TLIBBusToolDeviceType, * PLIBBusToolDeviceType;
typedef enum { T_MasterNode = 0, T_SlaveNode = 1, T_MonitorNode=2} TLINNodeType;
typedef enum { LIN_PROTOCL_13 = 0, LIN_PROTOCL_20 = 1, LIN_PROTOCL_21=2, LIN_PROTOCL_J2602=3}TLINProtocol;
typedef enum { APP_CAN = 0, APP_LIN = 1 } TLIBApplicationChannelType;
typedef enum {
	cbsBusLoad = 0, cbsPeakLoad, cbsFpsStdData, cbsAllStdData,
	cbsFpsExtData, cbsAllExtData, cbsFpsStdRemote, cbsAllStdRemote,
	cbsFpsExtRemote, cbsAllExtRemote, cbsFpsErrorFrame, cbsAllErrorFrame
} TLIBCANBusStatistics;
typedef enum { stCANSignal = 0, stLINSignal, stSystemVar, stFlexRay }TSignalType,*PSignalType;
typedef enum { fcmIdentical = 0, fcmLinear, fcmScaleLinear, fcmTextTable, fcmTABNoIntp, fcmFormula }TFlexRayCompuMethod, * PFlexRayCompuMethod;
#define VENDOR_NAME_LENGTH            (32)
#define DEVICE_SERIAL_STRING_LENGTH   (64)
// Hardware Info definition
typedef struct {
	TLIBBusToolDeviceType FDeviceType;
	s32 FDeviceIndex;
	char FVendorName[VENDOR_NAME_LENGTH];
	char FDeviceName[APP_DEVICE_NAME_LENGTH];
	char FSerialString[DEVICE_SERIAL_STRING_LENGTH];
}TLIBHWInfo, * PLIBHWInfo;

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
} TLIBTSMapping, * PLIBTSMapping;
// system var def
typedef enum {
	svtInt32 = 0, svtUInt32, svtInt64, svtUInt64, svtUInt8Array,
	svtInt32Array, svtInt64Array, svtDouble, svtDoubleArray, svtString
} TLIBSystemVarType;
typedef struct {
	char              FName[APP_DEVICE_NAME_LENGTH];
	char              FCategory[APP_DEVICE_NAME_LENGTH];
	char              FComment[APP_DEVICE_NAME_LENGTH];
	TLIBSystemVarType FDataType;
	bool              FIsReadOnly;
	double            FValueMin;
	double            FValueMax;
} TLIBSystemVarDef, * PLIBSystemVarDef;
typedef enum { fdtCAN = 0, fdtISOCANFD = 1, fdtNonISOCANFD = 2 } TCANFDControllerType;
typedef enum { fdmNormal = 0, fdmACKOff = 1, fdmRestricted = 2 } TCANFDControllerMode;
// log def
typedef enum { ortImmediately = 0, ortAsLog = 1, ortDelayed = 2 } TLIBOnlineReplayTimingMode;
typedef enum { orsNotStarted = 0, orsRunning = 1, orsPaused = 2, orsCompleted = 3, orsTerminated = 4 } TLIBOnlineReplayStatus;

#define CANMsgDecl(typ, name, chn, prop, dlc, id) const typ name = {{chn, prop, dlc, 0, id, 0, {0}}};
#define CANSgnDecl(name, typ, isIntel, startBit, len, factor, offset) const TCANSignal name = {typ, isIntel, startBit, len, factor, offset};
// Realtime comment
typedef struct _realtime_comment_t {
	s64 FTimeUs;
	s32 FEventType;
	u32 FCapacity;
	char* FComment;
} Trealtime_comment_t, * Prealtime_comment_t;
typedef enum { rivUseDB = 0, rivUseLast, rivUse0 } TLIBRBSInitValueOptions;
typedef double(__stdcall* TGetCANSignalValue)(const PCANSignal ACANSignal, const pu8 AData);
typedef void(__stdcall* TSetCANSignalValue)(const PCANSignal ACANSignal, const pu8 AData, const double AValue);
typedef void(__stdcall* TCANEvent)(const ps32 AObj, const PCAN ACAN);
typedef void(__stdcall* TCANFDEvent)(const ps32 AObj, const PCANFD ACANFD);
typedef void(__stdcall* TLINEvent)(const ps32 AObj, const PLIN ALIN);
typedef void(__stdcall* TLogger)(const char* AStr, const s32 ALevel);
typedef void(__stdcall* TFlexRayEvent)(const ps32 AObj, const PFlexRay AFlexRay);
typedef void(__stdcall* TGPSEvent)(const ps32 AObj, const PLIBGPSData AGPS);
// imported APIs
#if defined ( __cplusplus )
extern "C" {
#endif
	TSAPI(void) finalize_lib_tsmaster(void);
	TSAPI(s32) initialize_lib_tsmaster(const char* AAppName);
	TSAPI(s32) initialize_lib_tsmaster_with_project(const char* AAppName,const char* ProjectPath);
	TSAPI(s32) tsapp_add_application(const char* AAppName);
	TSAPI(s32) tsapp_add_cyclic_msg_can(const PCAN ACAN, const float APeriodMS);
	TSAPI(s32) tsapp_add_cyclic_msg_canfd(const PCANFD ACANFD, const float APeriodMS);
	TSAPI(s32) tsapp_clear_bus_statistics(void);
	TSAPI(s32) tsapp_configure_baudrate_lin(const s32 AIdxChn, const float ABaudrateKbps, const TLINProtocol AProtocol);
	TSAPI(s32) tsapp_configure_can_regs(const s32 channel, const float AArbBaudrate, const s32 ASEG1, const s32 ASEG2, const s32 APrescaler, const s32 ASJW, const s32 AOnlyListen, const s32 A120OhmConnected);
	TSAPI(s32) tsapp_configure_canfd_regs(const s32 channel, 
		const float AArbBaudrate, const s32 ASEG1, const s32 ASEG2, const s32 APrescaler,const s32 ASJW,
		const float AdataBaudrate, const s32 AdataSEG1, const s32 AdataSEG2, const s32 AdataPrescaler, const s32 AdataSJW,
		const TCANFDControllerType AControllerType, const TCANFDControllerMode AControllerMode, const s32 A120OhmConnected);

	TSAPI(s32) tsapp_configure_baudrate_can(const s32 AIdxChn, const float ABaudrateKbps, const bool AListenOnly, const bool AInstallTermResistor120Ohm);
	TSAPI(s32) tsapp_configure_baudrate_canfd(const s32 AIdxChn, const float ABaudrateArbKbps,
		const float ABaudrateDataKbps, const TCANFDControllerType AControllerType, const TCANFDControllerMode AControllerMode, const bool AInstallTermResistor120Ohm);

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
	TSAPI(s32) tsapp_enumerate_hw_devices(const ps32 ACount);
	TSAPI(s32) tsapp_execute_python_string(const char* AString, const char*AArguments, const bool AIsSync, const bool AIsX64, char** AResultLog);
	TSAPI(s32) tsapp_execute_python_script(const char* AFilePath, const char*AArguments,const bool AIsSync, const bool AIsX64, char** AResultLog);
	TSAPI(s32) tsapp_get_application_list(char** AAppNameList);
	TSAPI(s32) tsapp_get_bus_statistics(const TLIBApplicationChannelType ABusType, const s32 AIdxChn, const TLIBCANBusStatistics AIdxStat, pdouble AStat);
	TSAPI(s32) tsapp_get_can_channel_count(const ps32 ACount);
	TSAPI(s32) tsapp_set_flexray_channel_count(const s32 ACount);
	TSAPI(s32) tsapp_get_flexray_channel_count(const ps32 ACount);
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
	TSAPI(s32) tslin_set_node_funtiontype(const s32 AIndex,const TLINNodeType ATLINNodeType);
	TSAPI(s32) tsapp_get_timestamp(s64* ATimestamp);
	TSAPI(s32) tsapp_get_turbo_mode(const bool* AEnable);
	// tsapp_get_vendor_detect_preferences
	TSAPI(void) tsapp_log(const char* AStr, const TLogLevel ALevel);
	TSAPI(void) tsfifo_enable_receive_error_frames(void);
	TSAPI(void) tsfifo_enable_receive_fifo(void);
	TSAPI(void) tsfifo_disable_receive_error_frames(void);
	TSAPI(void) tsfifo_disable_receive_fifo(void);
	TSAPI(s32) tsfifo_receive_flexray_msgs(PFlexRay AFlexRay,ps32 BufferSize, const s32 AIdxChn, const bool includeTX);


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
	TSAPI(s32) tsapp_start_logging(const char* AFullFileName);
	TSAPI(s32) tsapp_stop_logging(void);
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
	TSAPI(s32) tscom_can_rbs_activate_network_by_name(const s32 AIdxChn, const bool AEnable, const char* ANetworkName, const bool AIncludingChildren);
	TSAPI(s32) tscom_can_rbs_activate_node_by_name(const s32 AIdxChn, const bool AEnable, const char* ANetworkName, const char* ANodeName, const bool AIncludingChildren);
	TSAPI(s32) tscom_can_rbs_activate_message_by_name(const s32 AIdxChn, const bool AEnable, const char* ANetworkName, const char* ANodeName, const char* AMsgName);
	TSAPI(s32) tscom_can_rbs_get_signal_value_by_element(const s32 AIdxChn, const char* ANetworkName, const char* ANodeName, const char* AMsgName, const char* ASignalName, double* AValue);
	TSAPI(s32) tscom_can_rbs_get_signal_value_by_address(const char* ASymbolAddress, double* AValue);
	TSAPI(s32) tscom_can_rbs_set_signal_value_by_element(const s32 AIdxChn, const char* ANetworkName, const char* ANodeName, const char* AMsgName, const char* ASignalName, const double AValue);
	TSAPI(s32) tscom_can_rbs_set_signal_value_by_address(const char* ASymbolAddress, const double AValue);
	
	TSAPI(s32) tscom_lin_rbs_start(void);
	TSAPI(s32) tscom_lin_rbs_stop(void);
	TSAPI(s32) tscom_lin_rbs_activate_all_networks(const bool AEnable, const bool AIncludingChildren);
	TSAPI(s32) tscom_lin_rbs_activate_network_by_name(const s32 AIdxChn, const bool AEnable, const char* ANetworkName, const bool AIncludingChildren);
	TSAPI(s32) tscom_lin_rbs_activate_node_by_name(const s32 AIdxChn, const bool AEnable, const char* ANetworkName, const char* ANodeName, const bool AIncludingChildren);
	TSAPI(s32) tscom_lin_rbs_activate_message_by_name(const s32 AIdxChn, const bool AEnable, const char* ANetworkName, const char* ANodeName, const char* AMsgName);
	TSAPI(s32) tscom_lin_rbs_get_signal_value_by_element(const s32 AIdxChn, const char* ANetworkName, const char* ANodeName, const char* AMsgName, const char* ASignalName, double* AValue);
	TSAPI(s32) tscom_lin_rbs_get_signal_value_by_address(const char* ASymbolAddress, double* AValue);
	TSAPI(s32) tscom_lin_rbs_set_signal_value_by_element(const s32 AIdxChn, const char* ANetworkName, const char* ANodeName, const char* AMsgName, const char* ASignalName, const double AValue);
	TSAPI(s32) tscom_lin_rbs_set_signal_value_by_address(const char* ASymbolAddress, const double AValue);

	//camera
	TSAPI(s32) tsapp_unlock_camera_channel(const s32 AChnIdx);

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

	//gps 
	TSAPI(s32) tsapp_logger_enable_gps_module(s32 AChnIdx, s32 AEnable, s32 ATimeoutMS);
	TSAPI(s32) tsapp_reset_gps_module(s32 AChnIdx, s32 AInitBaudrate, s32 ATargetBaudrate, s32 ATimeoutMS);
	TSAPI(s32) tsapp_get_gps_data_async(s32 AChnIdx, PLIBGPSData GPSData);
	TSAPI(s32) tsapp_register_event_gps(ps32 AObj,const TGPSEvent ACallBack);
	TSAPI(s32) tsapp_unregister_event_gps(ps32 AObj, const TGPSEvent ACallBack);


	//flexray 

	//blf
	TSAPI(s32) tslog_blf_write_start(char* AFileName, ps32 AHandle); //stdcall
	TSAPI(s32) tslog_blf_write_set_max_count(s32 AHandle, u32 ACount);
	TSAPI(s32) tslog_blf_write_can(s32 AHandle, PCAN ACAN);
	TSAPI(s32) tslog_blf_write_can_fd(s32 AHandle, PCANFD ACANFD);
	TSAPI(s32) tslog_blf_write_lin(s32 AHandle, PLIN ALIN);
	TSAPI(s32) tslog_blf_write_realtime_comment(s32 AHandle, s64 ATimeUs, char* AComment);
	TSAPI(s32) tslog_blf_write_end(s32 AHandle);
	TSAPI(s32) tslog_blf_read_start(char* AFileName, ps32 AHandle, ps32 AObjCount);
	TSAPI(s32) tsLog_blf_read_start_verbose(char* AFileName, ps32 AHandle, ps32 AObjCount,
		u16* AYear, u16* AMonth, u16* ADayOfWeek,
		u16* ADay, u16* AHour, u16* AMinute,
		u16* ASecond, u16* AMilliseconds);
	TSAPI(s32) tslog_blf_read_status(s32 AHandle, ps32 AObjReadCount);
	TSAPI(s32) tslog_blf_read_object(s32 AHandle, ps32 AProgressedCnt, ps32 AType/* PSupportedObjType*/, PCAN ACAN,
		PLIN ALIN, PCANFD ACANFD);
	TSAPI(s32) tslog_blf_read_object_w_comment(s32 AHandle, ps32 AProgressedCnt, ps32 AType/* PSupportedObjType*/,
		PCAN ACAN, PLIN ALIN, PCANFD ACANFD, Prealtime_comment_t AComment);
	TSAPI(s32) tslog_blf_read_end(s32 AHandle);
	TSAPI(s32) tslog_blf_seek_object_time(s32 AHandle, const double AProg100, s64* ATime, ps32 AProgressedCnt);
	//TSAPI(s32) tslog_blf_to_asc(char* ABLFFileName, char* AASCFileName, TProgressCallback AProgressCallback);
	//TSAPI(s32) tslog_asc_to_blf(char* AASCFileName, char* ABLFFileName , TProgressCallback AProgressCallback);

	//flexray
	TSAPI(s32) tsapp_register_event_flexray(ps32 obj, const TFlexRayEvent FlexrayEvent);
	TSAPI(s32) tsapp_register_pretx_event_flexray(ps32 obj, const TFlexRayEvent FlexrayEvent);
	TSAPI(s32) tsapp_unregister_event_flexray(ps32 obj, const TFlexRayEvent FlexrayEvent);
	TSAPI(s32) tsapp_unregister_pretx_event_flexray(ps32 obj, const TFlexRayEvent FlexrayEvent);
	TSAPI(s32) tsapp_unregister_events_flexray(ps32 obj);
	TSAPI(s32) tsapp_unregister_pretx_events_flexray(ps32 obj);
	TSAPI(s32) tsapp_transmit_flexray_async(const PFlexRay AFlexray);

	//flexray rbs
	TSAPI(s32) tscom_flexray_rbs_set_signal_value_by_address(const char* AAdrr,const double value);
	TSAPI(s32) tscom_flexray_rbs_get_signal_value_by_address(const char* AAdrr, pdouble value);
	TSAPI(s32) tscom_flexray_rbs_set_signal_value_by_element(const s32 AIdxChn,const char* AClusterName, const char* AECUName, const char* AFrameName,const char* ASignalName, const double value);
	TSAPI(s32) tscom_flexray_rbs_get_signal_value_by_element(const s32 AIdxChn,const char* AClusterName, const char* AECUName, const char* AFrameName, const char* ASignalName, pdouble value);
	TSAPI(s32) tscom_flexray_rbs_start();
	TSAPI(s32) tscom_flexray_rbs_stop();
	TSAPI(s32) tscom_flexray_rbs_is_running(bool* AIsRunning);
	TSAPI(s32) tscom_flexray_rbs_configure(const bool AAutoStart,const bool AAutoSendOnModification, const bool AActivateECUSimulation,const TLIBRBSInitValueOptions AInitValueOptions);
	TSAPI(s32) tscom_flexray_rbs_activate_all_clusters( const bool AEnable, const bool AIncludingChildren);
	TSAPI(s32) tscom_flexray_rbs_activate_cluster_by_name(const s32 AIdxChn, const bool AEnable, const char* AClusterName, const bool AIncludingChildren);
	TSAPI(s32) tscom_flexray_rbs_activate_ecu_by_name(const s32 AIdxChn, const bool AEnable, const char* AClusterName, const char* AECUName, const bool AIncludingChildren);
	TSAPI(s32) tscom_flexray_rbs_activate_frame_by_name(const s32 AIdxChn, const bool AEnable, const char* AClusterName, const char* AECUName, const char* AFrameName);
	TSAPI(s32) tscom_flexray_rbs_enable(const bool AEnable);
	TSAPI(s32) tsdb_unload_flexray_dbs();
	TSAPI(s32) tscom_flexray_get_signal_definition(const char* ASignalAddress, PFlexRaySignal ASignalDef);
	TSAPI(double) tscom_flexray_get_signal_value_in_raw_frame(const PFlexRaySignal ASignal, pu8 data);
	TSAPI(s32) tscom_flexray_set_signal_value_in_raw_frame(const PFlexRaySignal ASignal, pu8 data, double AValue);

	
	//system constant
	TSAPI(s32)tsapp_get_system_constant_count(s32 AIdxType, ps32 ACount);
	TSAPI(s32)tsapp_get_system_constant_value_by_index(s32 AIdxType, s32 AIdxValue,char** AName,pdouble AValue,char**ADesc);

	//Flexray db info
	TSAPI(s32) tsdb_save_settings(void);
	TSAPI(s32) db_get_can_db_index_by_id(u32 AID, ps32 AIdx);
	TSAPI(s32) db_get_lin_db_index_by_id(u32 AID, ps32 AIdx);
	TSAPI(s32) db_get_flexray_db_index_by_id(u32 AID, ps32 AIdx);
	TSAPI(s32) tsdb_load_flexray_db(const char* AFRFile, const char* ASupportedChannels, pu32 AId);
	TSAPI(s32) tsdb_unload_flexray_db(const s32 AId);
	TSAPI(s32) tsdb_unload_flexray_dbs();
	TSAPI(s32) tsdb_get_flexray_db_count(ps32 AId);
	TSAPI(s32) tsdb_get_flexray_db_properties_by_address_verbose(const char* AAddr, ps32 ADBIndex, ps32 ASignalCount, ps32 AFrameCount, ps32 AECUCount, ps64 ASupportedChannelMask, ps64 AFlag, char** AName, char** AComment);
	TSAPI(s32) tsdb_get_flexray_db_properties_by_index_verbose(s32 ADBIndex, ps32 ASignalCount, ps32 AFrameCount, ps32 AECUCount, ps64 ASupportedChannelMask, ps64 AFlag, char** AName, char** AComment);

	TSAPI(s32) tsdb_get_flexray_ecu_properties_by_address_verbose(const char* AAddr, ps32 ADBIndex, ps32 AECUIndex, ps32 ATxFrameCount, ps32 ARxFrameCount, char** AName, char** AComment);
	TSAPI(s32) tsdb_get_flexray_ecu_properties_by_index_verbose(s32 ADBIndex, s32 AECUIndex, ps32 ATxFrameCount, ps32 ARxFrameCount, char** AName, char** AComment);

	TSAPI(s32) tsdb_get_flexray_frame_properties_by_address_verbose(const char* AAddr, ps32 ADBIndex, ps32 AECUIndex, ps32 AFrameIndex, bool* AIsTx, ps32 AFRChannelMask, ps32 AFRBaseCycle, ps32 AFRCycleRepetition, bool* AFRIsStartupFrame, ps32 AFRSlotId, ps64 AFRCycleMask, ps32 ASignalCount, char** AName, char** AComment);
	TSAPI(s32) tsdb_get_flexray_frame_properties_by_index_verbose(s32 ADBIndex, s32 AECUIndex, s32 AFrameIndex, bool AIsTx, ps32 AFRChannelMask, ps32 AFRBaseCycle, ps32 AFRCycleRepetition, bool* AFRIsStartupFrame, ps32 AFRSlotId, ps64 AFRCycleMask, ps32 ASignalCount, char** AName, char** AComment);

	TSAPI(s32) tsdb_get_flexray_signal_properties_by_address_verbose(const char* AAddr, ps32 ADBIndex, ps32 AECUIndex, ps32 AFrameIndex, ps32 ASignalIndex, bool* AIsTx, PSignalType ASignalType, PFlexRayCompuMethod ACompuMethod, bool* AIsIntel, ps32 AStartBit, ps32 AUpdateBit, ps32 ALength, pdouble AFactor, pdouble AOffset, pdouble AInitValue, char** AName, char** AComment);
	TSAPI(s32) tsdb_get_flexray_signal_properties_by_index_verbose(s32 ADBIndex, s32 AECUIndex, s32 AFrameIndex, s32 ASignalIndex, bool AIsTx, PSignalType ASignalType, PFlexRayCompuMethod ACompuMethod, bool* AIsIntel, ps32 AStartBit, ps32 AUpdateBit, ps32 ALength, pdouble AFactor, pdouble AOffset, pdouble AInitValue, char** AName, char** AComment);
	TSAPI(s32) tsdb_get_flexray_db_id(const s32 AIndex, ps32 AId);
	
	TSAPI(s32) tsdb_get_flexray_db_properties_by_address(const char* AAddr, PDBProperties Avalue);
	TSAPI(s32) tsdb_get_flexray_db_properties_by_index(PDBProperties Avalue);

	TSAPI(s32) tsdb_get_flexray_db_ecu_properties_by_address(const char* AAddr, PDBECUProperties Avalue);
	TSAPI(s32) tsdb_get_flexray_db_ecu_properties_by_index(PDBECUProperties Avalue);

	TSAPI(s32) tsdb_get_flexray_db_frame_properties_by_db_index(const s32 AIdxDB, const s32 AIndex, PDBFrameProperties Avalue);
	TSAPI(s32) tsdb_get_flexray_db_frame_properties_by_address(const char* AAddr, PDBFrameProperties Avalue);
	TSAPI(s32) tsdb_get_flexray_db_frame_properties_by_index(PDBFrameProperties Avalue);
	
	TSAPI(s32) tsdb_get_flexray_db_signal_properties_by_db_index(const s32 AIdxDB, const s32 AIndex, PDBSignalProperties Avalue);
	TSAPI(s32) tsdb_get_flexray_db_signal_properties_by_frame_index(const s32 AIdxDB, const s32 Frameidx ,const s32 AIndex, PDBSignalProperties Avalue);
	TSAPI(s32) tsdb_get_flexray_db_signal_properties_by_address(const char* AAddr, PDBSignalProperties Avalue);
	TSAPI(s32) tsdb_get_flexray_db_signal_properties_by_index(PDBSignalProperties Avalue);

	//CAN DB INFO
	TSAPI(s32) tsdb_load_can_db(const char* ADBC, const char* ASupportedChannelsBased0, u32* AId);
	TSAPI(s32) tsdb_unload_can_db(const u32 AId);
	TSAPI(s32) tsdb_unload_can_dbs(void);
	TSAPI(s32) tsdb_get_can_db_count(s32* ACount);
	TSAPI(s32) tsdb_get_can_db_id(const s32 AIndex, u32* AId);
	TSAPI(s32) tsdb_get_can_db_info(const u32 ADatabaseId, const s32 AType, const s32 AIndex, const s32 ASubIndex, char** AValue);

	TSAPI(s32) tsdb_get_can_db_properties_by_address(const char* AAddr, PDBProperties Avalue);
	TSAPI(s32) tsdb_get_can_db_properties_by_index(PDBProperties Avalue);

	TSAPI(s32) tsdb_get_can_db_ecu_properties_by_address(const char* AAddr, PDBECUProperties Avalue);
	TSAPI(s32) tsdb_get_can_db_ecu_properties_by_index(PDBECUProperties Avalue);

	TSAPI(s32) tsdb_get_can_db_frame_properties_by_db_index(const s32 AIdxDB, const s32 AIndex, PDBFrameProperties Avalue);
	TSAPI(s32) tsdb_get_can_db_frame_properties_by_address(const char* AAddr, PDBFrameProperties Avalue);
	TSAPI(s32) tsdb_get_can_db_frame_properties_by_index(PDBFrameProperties Avalue);

	TSAPI(s32) tsdb_get_can_db_signal_properties_by_db_index(const s32 AIdxDB, const s32 AIndex, PDBSignalProperties Avalue);
	TSAPI(s32) tsdb_get_can_db_signal_properties_by_frame_index(const s32 AIdxDB, const s32 Frameidx, const s32 AIndex, PDBSignalProperties Avalue);

	TSAPI(s32) tsdb_get_can_db_signal_properties_by_address(const char* AAddr, PDBSignalProperties Avalue);
	TSAPI(s32) tsdb_get_can_db_signal_properties_by_index(PDBSignalProperties Avalue);

	//LIN DB INFO
	TSAPI(s32) tsdb_load_lin_db(const char* ADBC, const char* ASupportedChannelsBased0, u32* AId);
	TSAPI(s32) tsdb_unload_lin_db(const u32 AId);
	TSAPI(s32) tsdb_unload_lin_dbs(void);
	TSAPI(s32) tsdb_get_lin_db_count(s32* ACount);
	TSAPI(s32) tsdb_get_lin_db_id(const s32 AIndex, u32* AId);
	
	TSAPI(s32) tsdb_get_lin_db_properties_by_address(const char* AAddr, PDBProperties Avalue);
	TSAPI(s32) tsdb_get_lin_db_properties_by_index(PDBProperties Avalue);

	TSAPI(s32) tsdb_get_lin_db_ecu_properties_by_address(const char* AAddr, PDBECUProperties Avalue);
	TSAPI(s32) tsdb_get_lin_db_ecu_properties_by_index(PDBECUProperties Avalue);

	TSAPI(s32) tsdb_get_lin_db_frame_properties_by_db_index(const s32 AIdxDB, const s32 AIndex, PDBFrameProperties Avalue);
	TSAPI(s32) tsdb_get_lin_db_frame_properties_by_address(const char* AAddr, PDBFrameProperties Avalue);
	TSAPI(s32) tsdb_get_lin_db_frame_properties_by_index(PDBFrameProperties Avalue);

	TSAPI(s32) tsdb_get_lin_db_signal_properties_by_db_index(const s32 AIdxDB, const s32 AIndex, PDBSignalProperties Avalue);
	TSAPI(s32) tsdb_get_lin_db_signal_properties_by_frame_index(const s32 AIdxDB, const s32 Frameidx, const s32 AIndex, PDBSignalProperties Avalue);
	TSAPI(s32) tsdb_get_lin_db_signal_properties_by_address(const char* AAddr, PDBSignalProperties Avalue);
	TSAPI(s32) tsdb_get_lin_db_signal_properties_by_index(PDBSignalProperties Avalue);

	//filter

	TSAPI(s32)tsfifo_add_can_canfd_pass_filter(const s32 AIdxDB, const s32 AId, const bool AIsStd);
	TSAPI(s32)tsfifo_delete_can_canfd_pass_filter(const s32 AIdxDB, const s32 AId);
	TSAPI(s32)tsfifo_add_lin_pass_filter(const s32 AIdxDB, const s32 AId);
	TSAPI(s32)tsfifo_delete_lin_pass_filter(const s32 AIdxDB, const s32 AId);


#if defined ( __cplusplus )
}
#endif

#pragma pack(pop)

#endif
