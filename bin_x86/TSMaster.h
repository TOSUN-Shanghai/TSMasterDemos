#ifndef _TSMaster_H
#define _TSMaster_H

#include <math.h>
#include <stdio.h>
#ifndef __cplusplus
#include <stdbool.h>
#else
#include <cstring>
#endif

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

typedef unsigned __int8** ppu8;
typedef signed __int8** pps8;
typedef unsigned __int16** ppu16;
typedef signed __int16** pps16;
typedef unsigned __int32** ppu32;
typedef signed __int32** pps32;
typedef unsigned __int64** ppu64;
typedef signed __int64** pps64;
typedef size_t native_int;
typedef size_t* pnative_int;
typedef size_t** ppnative_int;

typedef float  single;
typedef float* psingle;
typedef double* pdouble;
typedef char* pchar;
typedef char** ppchar;
typedef void* TObject;
typedef void* pvoid;
typedef bool* pbool; 
typedef size_t* psize_t;

#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
#define SWAP_BYTES(x) (((x) >> 8) | ((x & 0xFF) << 8))

#ifdef DLLTEST_EXPORT
#define TSAPI(ret) __declspec(dllexport) ret __stdcall
#else
#define TSAPI(ret) __declspec(dllimport) ret __stdcall
#endif

#pragma pack(push)
#pragma pack(1)


#define TS_AF_INET  2
#define TS_SOCK_STREAM      1
#define TS_SOCK_DGRAM       2
#define TS_SOCK_RAW         3
#define  TS_MSG_DONTWAIT    0x08 


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

// C++ array property definitino
#define ARRAY_PROPERTY(t,n,s) __declspec( property ( put = property__set_##n, get = property__get_##n ) ) t n[s];\
    typedef t property__tmp_type_##n
#define READONLY_ARRAY_PROPERTY(t,n,s) __declspec( property (get = property__get_##n) ) t n[s];\
    typedef t property__tmp_type_##n
#define WRITEONLY_ARRAY_PROPERTY(t,n,s) __declspec( property (put = property__set_##n) ) t n[s];\
    typedef t property__tmp_type_##n
#define ARRAY_GET(n) property__tmp_type_##n property__get_##n(int index)
#define ARRAY_SET(n) void property__set_##n(int index, const property__tmp_type_##n& value)

const u8 DLC_DATA_BYTE_CNT[16] = {
	0, 1, 2, 3, 4, 5, 6, 7,
	8, 12, 16, 20, 24, 32, 48, 64
};
typedef struct _TLIBCAN
{
    u8 FIdxChn;//channel index starting from 0
    u8 FProperties;//default 0, masked status:  = CAN [7] 0-normal frame, 1-error frame [6] 0-not logged, 1-already logged [5-3] tbd [2] 0-std frame, 1-extended frame [1] 0-data frame, 1-remote frame [0] dir: 0-RX, 1-TX
    u8 FDLC;//dlc from 0 to 15   = CAN
    u8 FReserved;
    s32 FIdentifier;//CAN identifier   = CAN
    s64 FTimeUs;//timestamp in us = CAN
    u8 FData[8];
#ifdef __cplusplus
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
            FProperties = FProperties | MASK_CANProp_ERROR;

        }
        else {
            FProperties = FProperties & (~MASK_CANProp_ERROR);
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
#endif
}TLIBCAN, *PLIBCAN;

typedef struct _TLIBCANFD
{
    u8 FIdxChn;//channel index starting from 0
    u8 FProperties;//default 0, masked status:  = CAN [7] 0-normal frame, 1-error frame [6] 0-not logged, 1-already logged [5-3] tbd [2] 0-std frame, 1-extended frame [1] 0-data frame, 1-remote frame [0] dir: 0-RX, 1-TX
    u8 FDLC;//dlc from 0 to 15   = CAN
    u8 FFDProperties;//[7-3] tbd <> CAN  [2] ESI, The E RROR S TATE I NDICATOR (ESI) flag is transmitted dominant by error active nodes, recessive by error passive nodes. ESI does not exist in CAN format frames [1] BRS, If the bit is transmitted recessive, the bit rate is switched from the standard bit rate of the A RBITRATION P HASE to the preconfigured alternate bit rate of the D ATA P HASE . If it is transmitted dominant, the bit rate is not switched. BRS does not exist in CAN format frames. [0] EDL: 0-normal CAN frame, 1-FD frame, added 2020-02-12, The E XTENDED D ATA L ENGTH (EDL) bit is recessive. It only exists in CAN FD format frames
    s32 FIdentifier;//CAN identifier   = CAN
    s64 FTimeUs;//timestamp in us = CAN
    u8 FData[64] ;
#ifdef __cplusplus
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
			FProperties = FProperties | MASK_CANProp_ERROR;

		}
		else {
			FProperties = FProperties & (~MASK_CANProp_ERROR);
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
	TLIBCAN to_tcan(void) {
		return *(TLIBCAN*)(&FIdxChn);
	}
#endif
}TLIBCANFD, *PLIBCANFD;


typedef struct _TLIBLIN
{
    u8 FIdxChn;//channel index starting from 0
    u8 FErrCode;//0: normal
    u8 FProperties;//default 0, masked status:  [7] tbd [6] 0-not logged, 1-already logged [5-4] FHWType [3] 0-not ReceivedSync, 1- ReceivedSync [2] 0-not received FReceiveBreak, 1-Received Break [1] 0-not send FReceiveBreak, 1-send Break [0] dir: 0-RX, 1-TX
    u8 FDLC;//dlc from 0 to 8
    u8 FIdentifier;//LIN identifier:0--64
    u8 FChecksum;//LIN checksum
    u8 FStatus;//place holder 1
    s64 FTimeUS;//timestamp in us
    u8 FData[8] ;
#ifdef __cplusplus
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
		FErrCode = 0;
		FProperties = 0;
		FDLC = ADLC;
		FIdentifier = AId;
		*(__int64*)(&FData[0]) = 0;
		FChecksum = 0;
		FStatus = 0;
		FTimeUS = 0;
	}
#endif
}TLIBLIN, *PLIBLIN;

typedef struct _TLIBFlexRay
{
    u8 FIdxChn;//channel index starting from 0
    u8 FChannelMask;//0: reserved, 1: A, 2: B, 3: AB
    u8 FDir;//0: Rx, 1: Tx, 2: Tx Request
    u8 FPayloadLength;//payload length in bytes
    u8 FActualPayloadLength;//actual data bytes
    u8 FCycleNumber;//cycle number: 0~63
    u8 FCCType;//0 = Architecture independent, 1 = Invalid CC type, 2 = Cyclone I, 3 = BUSDOCTOR, 4 = Cyclone II, 5 = Vector VN interface, 6 = VN - Sync - Pulse(only in Status Event, for debugging purposes only)
    u8 FFrameType;// 1 reserved byte
    u16 FHeaderCRCA;// header crc A
    u16 FHeaderCRCB;// header crc B
    u16 FFrameStateInfo;// bit 0~15, error flags
    u16 FSlotId;// static seg: 0~1023
    u32 FFrameFlags;// bit 0~22 //0 1 = Null frame //1 1 = Data segment contains valid data //2 1 = Sync bit //3 1 = Startup flag //4 1 = Payload preamble bit //5 1 = Reserved bit, //6 1 = Error flag(error frame or invalid frame) //7..14 Reserved //15 1 = Async.monitoring has generated this event //16 1 = Event is a PDU //17 Valid for PDUs only.The bit is set if the PDU is valid(either if the PDU has no  // update bit, or the update bit for the PDU was set in the received frame). //18 Reserved //19 1 = Raw frame(only valid if PDUs are used in the configuration).A raw frame may  // contain PDUs in its payload //20 1= Dynamic segment 0 = static segment ,21 This flag is only vaild for frames and not for PDUS. 1 = ThePDUs in the payload of // this frame are logged in separate logging entries. 0 = The PDUs in the payload of this  // frame must be extracted out of this frame.The logging file does not contain separate  // PDU - entries. //22 Valid for PDUs only.The bit is set if the PDU has an update bit
    u32 FFrameCRC;//frame crc
    u64 FReserved1;//8 reserved bytes
    u64 FReserved2;//8 reserved bytes
    u64 FTimeUs;// timestamp in us
    u8 FData[254] ;
#ifdef __cplusplus
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
#endif
}TLIBFlexRay, *PLIBFlexRay;

typedef struct _TLIBEthernetHeader
{
    u8 FIdxChn;//app channel index starting from 0 = Network index
    u8 FIdxSwitch;//Network's switch index
    u8 FIdxPort;// Network's switch's port index, 0~127: measurement port, 128~255: virtual port
    u8 FConfig;//  0-1: 0 = Rx, 1 = Tx, 2 = TxRq // 2: crc status, for tx, 0: crc is include in data, 1: crc is not include in data //                for rx, 0: crc is ok, 1: crc is not ok // 3: tx done type, 0: only report timestamp, 1: report full info(header+frame)
    u16 FEthernetPayloadLength;// Length of Ethernet payload data in bytes. Max. 1582 Byte(without Ethernet header), 1612 Byte(Inclusive ethernet header)
    u16 FReserved;//Reserved
    u64 FTimeUs;//timestamp in us
    pu8 FEthernetDataAddr;//data ps32
    #ifdef _WIN32
    u32 FPadding;                // to be compatible with x64
    #endif
#ifdef __cplusplus
    ARRAY_PROPERTY(u8, Payloads, 1500);
    ARRAY_GET(Payloads) {
        return *(ethernet_payload_addr() + index);
    }
    ARRAY_SET(Payloads) {
        *(ethernet_payload_addr() + index) = value;
    }
    inline bool get_tx() {
        return (FConfig & 0x1) != 0;
    }
    inline void set_tx(bool a) {
        if (a) {
            FConfig |= 1;
        } else {
            FConfig &= 0xFC;
        }
    }
    void reset_data_pointer(){
        FEthernetDataAddr = actual_data_pointer();
    }
    void init(const u16 APayloadLength){
        FIdxChn = 0;
        FIdxSwitch = 0;
        FIdxPort = 0;
        FConfig = 0;
        FEthernetPayloadLength = APayloadLength;
        FReserved = 0;
        FTimeUs = 0;
        reset_data_pointer();
#ifndef _WIN64
        FPadding = 0;
#endif
        s32 i;
        pu8 p = FEthernetDataAddr;
        s32 n = MIN(1612 - 14, APayloadLength);
        n += 14;
        for (i=0; i<n; i++){
            *p++ = 0;
        }
        *(pu16)(ethernet_type_addr()) = 0x00; // IPV4 = SWAP_BYTES(0x0800)
        p = destination_mac_addr();
        for (i=0; i<6; i++){
            *p++ = 0xFF;
        }
    }
    bool is_virtual(){
        return FIdxPort >= 128;
    }
    bool is_ip_frame(){
        return ethernet_type() == 0x0800;
    }
    bool is_tcp_frame(){
        u16 o;
        has_vlans(&o);
        return (ethernet_type() == 0x0800) && (0x06 == *(FEthernetDataAddr + 0x17 + o));
    }
    bool is_udp_frame(){
        u16 o;
        has_vlans(&o);
        return (ethernet_type() == 0x0800) && (0x11 == *(FEthernetDataAddr + 0x17 + o));
    }
    pu16 first_vlan_addr(){
        return (pu16)(actual_data_pointer() + 6 + 6);
    }
    bool has_vlans(pu16 AOffsetBytes){
        *AOffsetBytes = 0;
        while (*(pu16)(actual_data_pointer() + 6 + 6 + (*AOffsetBytes)) == 0x0081){
            *AOffsetBytes = *AOffsetBytes + 4;
        }
        return *AOffsetBytes > 0;
    }
    pu8 actual_data_pointer() {
        return &FIdxChn + sizeof(_TLIBEthernetHeader);
    }
    s32 total_ethernet_packet_length() {
        u16 o;
        has_vlans(&o);
        return sizeof(_TLIBEthernetHeader) + 6 + 6 + 2 + o + FEthernetPayloadLength;
    }
    s32 ethernet_data_length(){
        u16 o;
        has_vlans(&o);
        return FEthernetPayloadLength + 6 + 6 + o + 2;
    }
    void set_ethernet_data_length(const u16 ALength) {
        u16 o;
        has_vlans(&o);
        o += 14;
        if (ALength > o){
            FEthernetPayloadLength = ALength - o;
        }
    }
    pu8 ethernet_payload_addr() {
        u16 o;
        has_vlans(&o);
        return FEthernetDataAddr + 6 + 6 + 2 + o;
    }
    pu8 destination_mac_addr() {
        return FEthernetDataAddr;
    }
    pu8 source_mac_addr() {
        return FEthernetDataAddr + 6;
    }
    pu8 destination_ip_addr(){
        if (!is_ip_frame()) return nullptr;
        u16 o;
        has_vlans(&o);
        return FEthernetDataAddr + 0x1E + o;
    }
    pu8 source_ip_addr(){
        if (!is_ip_frame()) return nullptr;
        u16 o;
        has_vlans(&o);
        return FEthernetDataAddr + 0x1A + o;
    }
    u16 destination_port_value(){
        if (!is_ip_frame()) return 0;
        u16 o;
        has_vlans(&o);
        o = *(u16*)(FEthernetDataAddr + 0x24 + o);
        return SWAP_BYTES(o);
    }
    u16 source_port_value(){
        if (!is_ip_frame()) return 0;
        u16 o;
        has_vlans(&o);
        o = *(u16*)(FEthernetDataAddr + 0x22 + o);
        return SWAP_BYTES(o);
    }
    pu16 ethernet_type_addr() {
        u16 o;
        has_vlans(&o);
        pu8 p = FEthernetDataAddr + 6 + 6 + o;
        return (pu16)(p);
    }
    u16 ethernet_type() {
        u16 t = *(pu16)(ethernet_type_addr());
        return SWAP_BYTES(t);
    }
    u16 get_ip_header_checksum(){
        u16 o;
        if (!is_ip_frame()) return 0;
        has_vlans(&o);
        o = *(pu16)(FEthernetDataAddr + 0x18 + o);
        return SWAP_BYTES(o);
    }
    void set_ip_header_checksum(const u16 AValue){
        u16 o;
        if (!is_ip_frame()) return;
        has_vlans(&o);
        *(pu16)(FEthernetDataAddr + 0x18 + o) = SWAP_BYTES(AValue);
    }
    void copy_payload(const pu8 ABuffer, const u16 ALength){
        u16 l = MIN(ALength, FEthernetPayloadLength);
        std::memcpy(ethernet_payload_addr(), ABuffer, l);
    }
    void set_ip_packet_payload_length(const u16 ALength){
        u16 o;
        if (!is_ip_frame()) return;
        has_vlans(&o);
        *(pu16)(FEthernetDataAddr + 16 + o) = SWAP_BYTES(ALength + 20);
    }
    u16 get_ip_packet_payload_length(){
        u16 o;
        if (!is_ip_frame()) return 0;
        has_vlans(&o);
        o = *(pu16)(FEthernetDataAddr + 16 + o);
        return SWAP_BYTES(o) - 20;
    }
    pu8 get_ip_packet_data_addr(){
        u16 o;
        if (!is_ip_frame()) return nullptr;
        has_vlans(&o);
        return FEthernetDataAddr + 0x0E + o;
    }
    pu8 get_ip_packet_payload_addr(){
        u16 o;
        if (!is_ip_frame()) return nullptr;
        has_vlans(&o);
        return FEthernetDataAddr + 0x22 + o;
    }
    void set_udp_payload_length(const u16 ALength){
        u16 o;
        if (!is_udp_frame()) return;
        has_vlans(&o);
        *(pu16)(FEthernetDataAddr + 0x26 + o) = SWAP_BYTES(ALength + 8/*header length*/);
    }
    u16 get_udp_payload_length(){
        u16 o;
        if (!is_udp_frame()) return 0;
        has_vlans(&o);
        o = *(pu16)(FEthernetDataAddr + 0x26 + o);
        return SWAP_BYTES(o) - 8/*header length*/;
    }
    pu8 get_ip_address_destination_addr(){
        u16 o;
        if (!is_ip_frame()) return 0;
        has_vlans(&o);
        return FEthernetDataAddr + 0x1E + o;
    }
    pu8 get_ip_address_source_addr(){
        u16 o;
        if (!is_ip_frame()) return 0;
        has_vlans(&o);
        return FEthernetDataAddr + 0x1A + o;
    }
    u16 get_udp_port_destination(){
        u16 o;
        if (!is_udp_frame()) return 0;
        has_vlans(&o);
        o = *(pu16)(FEthernetDataAddr + 0x24 + o);
        return SWAP_BYTES(o);
    }
    u16 get_udp_port_source(){
        u16 o;
        if (!is_udp_frame()) return 0;
        has_vlans(&o);
        o = *(pu16)(FEthernetDataAddr + 0x22 + o);
        return SWAP_BYTES(o);
    }
    void set_udp_port_destination(const u16 AValue){
        u16 o;
        if (!is_udp_frame()) return;
        has_vlans(&o);
        *(pu16)(FEthernetDataAddr + 0x24 + o) = SWAP_BYTES(AValue);
    }
    void set_udp_port_source(const u16 AValue){
        u16 o;
        if (!is_udp_frame()) return;
        has_vlans(&o);
        *(pu16)(FEthernetDataAddr + 0x22 + o) = SWAP_BYTES(AValue);
    }
    bool check_udp_fragment(pu16 AId, pu16 AOffset){
        u16 o;
        bool r;
        has_vlans(&o);
        r = (0x40 & *(FEthernetDataAddr + 0x14 + o)) == 0;
        if (r) {
            *AOffset = *(pu16)(FEthernetDataAddr + 0x14 + o);
            *AOffset = (SWAP_BYTES(*AOffset) & 0x1FFF) << 3;
            *AId = *(pu16)(FEthernetDataAddr + 0x12 + o);
            *AId = SWAP_BYTES(*AId);
        }
        return r;
    }
    pu8 get_udp_payload_addr(){
        u16 o, id, fo;
        if (!is_udp_frame()) return nullptr;        
        if (check_udp_fragment(&id, &fo)){
            if (fo > 0){
                return get_ip_packet_data_addr();
            }
        }
        has_vlans(&o);
        return FEthernetDataAddr + 0x2A + o;
    }
#endif
}TLIBEthernetHeader, *PLIBEthernetHeader;

typedef struct _TLIBFlexray_controller_config
{
    u8 NETWORK_MANAGEMENT_VECTOR_LENGTH;
    u8 PAYLOAD_LENGTH_STATIC;
    u16 FReserved;
    u16 LATEST_TX;//__ prtc1Control
    u16 T_S_S_TRANSMITTER;
    u8 CAS_RX_LOW_MAX;
    u8 SPEED;//0 for 10m, 1 for 5m, 2 for 2.5m, convert from Database
    u16 WAKE_UP_SYMBOL_RX_WINDOW;
    u8 WAKE_UP_PATTERN;//__ prtc2Control
    u8 WAKE_UP_SYMBOL_RX_IDLE;
    u8 WAKE_UP_SYMBOL_RX_LOW;
    u8 WAKE_UP_SYMBOL_TX_IDLE;
    u8 WAKE_UP_SYMBOL_TX_LOW;//__ succ1Config
    u8 channelAConnectedNode;//Enable ChannelA: 0: Disable 1: Enable
    u8 channelBConnectedNode;//Enable ChannelB: 0: Disable 1: Enable
    u8 channelASymbolTransmitted;//Enable Symble Transmit function of Channel A: 0: Disable 1: Enable
    u8 channelBSymbolTransmitted;//Enable Symble Transmit function of Channel B: 0: Disable 1: Enable
    u8 ALLOW_HALT_DUE_TO_CLOCK;
    u8 single_SLOT_ENABLED;//FALSE_0, TRUE_1
    u8 wake_up_idx;//Wake up channe: 0:ChannelA， 1:ChannelB
    u8 ALLOW_PASSIVE_TO_ACTIVE;
    u8 COLD_START_ATTEMPTS;
    u8 synchFrameTransmitted;//Need to transmit sync frame
    u8 startupFrameTransmitted;//Need to transmit startup frame // __ succ2Config
    u32 LISTEN_TIMEOUT;
    u8 LISTEN_NOISE;//2_16 __ succ3Config
    u8 MAX_WITHOUT_CLOCK_CORRECTION_PASSIVE;
    u8 MAX_WITHOUT_CLOCK_CORRECTION_FATAL;
    u8 REVERS0;//Memory Align // __ gtuConfig //__ gtu01Config
    u32 MICRO_PER_CYCLE;//__ gtu02Config
    u16 Macro_Per_Cycle;
    u8 SYNC_NODE_MAX;
    u8 REVERS1;//Memory Align //__ gtu03Config
    u8 MICRO_INITIAL_OFFSET_A;
    u8 MICRO_INITIAL_OFFSET_B;
    u8 MACRO_INITIAL_OFFSET_A;
    u8 MACRO_INITIAL_OFFSET_B;//__ gtu04Config
    u16 N_I_T;
    u16 OFFSET_CORRECTION_START;//__ gtu05Config
    u8 DELAY_COMPENSATION_A;
    u8 DELAY_COMPENSATION_B;
    u8 CLUSTER_DRIFT_DAMPING;
    u8 DECODING_CORRECTION;//__ gtu06Config
    u16 ACCEPTED_STARTUP_RANGE;
    u16 MAX_DRIFT;//__ gtu07Config
    u16 STATIC_SLOT;
    u16 NUMBER_OF_STATIC_SLOTS;//__ gtu08Config
    u8 MINISLOT;
    u8 REVERS2;//Memory Align
    u16 NUMBER_OF_MINISLOTS;//__ gtu09Config
    u8 DYNAMIC_SLOT_IDLE_PHASE;
    u8 ACTION_POINT_OFFSET;
    u8 MINISLOT_ACTION_POINT_OFFSET;
    u8 REVERS3;//Memory Align __ gtu10Config
    u16 OFFSET_CORRECTION_OUT;
    u16 RATE_CORRECTION_OUT;//__ gtu11Config
    u8 EXTERN_OFFSET_CORRECTION;
    u8 EXTERN_RATE_CORRECTION;
    u8 REVERS4;//Memory Align
    u8 config_byte;//Memory Align //bit0: 1：启用cha上终端电阻  0：不启用 //bit1: 1：启用chb上终端电阻  0：不启用 //bit2: 1：启用接收FIFO    0：不启用 //bit4: 1：cha桥接使能             0：不使能 //bit5: 1：chb桥接使能             0：不使能
}TLIBFlexray_controller_config, *PLIBFlexray_controller_config;

typedef pvoid TMPTacDebugger;
typedef TMPTacDebugger* PMPTacDebugger;
typedef pvoid TMPTacValue;
typedef TMPTacValue* PMPTacValue;
typedef pvoid TMPTacBreakpoint;
typedef TMPTacBreakpoint* PMPTacBreakpoint;
typedef enum {
    TAC_TYPE_NULL = 0,
    TAC_TYPE_INTEGER = 1,
    TAC_TYPE_FLOAT = 2,
    TAC_TYPE_BOOLEAN = 3,
    TAC_TYPE_STRING = 4,
    TAC_TYPE_ARRAY = 5,
    TAC_TYPE_STRUCT = 6,
    TAC_TYPE_FUNCTION = 7,
    TAC_TYPE_UNKNOWN = 8,
}TMPTacValueType, *PMPTacValueType;
typedef enum {
    TAC_EVENT_BREAKPOINT_HIT = 0,
    TAC_EVENT_PAUSED = 1,
    TAC_EVENT_STEP_COMPLETE = 2,
    TAC_EVENT_SCRIPT_END = 3,
    TAC_EVENT_RUNTIME_ERROR = 4,
    TAC_EVENT_TERMINATED = 5,
}TMPTacDebugEvent, *PMPTacDebugEvent;
typedef enum {
    dtInherit = 0,
    dtDouble = 1,
    dtSingle = 2,
    dtHalf = 3,
    dtInt8 = 4,
    dtUInt8 = 5,
    dtInt16 = 6,
    dtUInt16 = 7,
    dtInt32 = 8,
    dtUInt32 = 9,
    dtInt64 = 10,
    dtUInt64 = 11,
    dtBoolean = 12,
    dtString = 13,
    dtFixDt = 14,
    dtEnum = 15,
    dtBus = 16,
    dtValueType = 17,
    dtImage = 18,
}TLIBMBDDataType, *PLIBMBDDataType;
typedef enum {
    mpkPriority = 0,
    mpkFirst = 1,
    mpkLast = 2,
}TMBD_PriorityKind, *PMBD_PriorityKind;
typedef enum {
    AIT_DIAGRAM = 0,
    AIT_JUNCTION = 1,
    AIT_GROUP = 2,
    AIT_STATE = 3,
    AIT_GRAPHIC_FUNCTION = 4,
    AIT_DIAGRAM_FUNCTION = 5,
    AIT_C_FUNCTION = 6,
    AIT_TRUTH_TABLE = 7,
    AIT_COMMENT = 8,
    AIT_IMAGE = 9,
    AIT_HISTORY_JUNCTION = 10,
    AIT_DATA = 11,
    AIT_TRANSITION = 12,
    AIT_EVENT = 13,
}TAiFlowObjectType, *PAiFlowObjectType;
typedef enum {
    DECOMP_OR = 0,
    DECOMP_AND = 1,
    DECOMP_CLUSTER = 2,
}TAiFlowDecomposition, *PAiFlowDecomposition;
typedef enum {
    DRAG_NONE = 0,
    DRAG_TOP_LEFT = 1,
    DRAG_TOP_RIGHT = 2,
    DRAG_BOTTOM_LEFT = 3,
    DRAG_BOTTOM_RIGHT = 4,
    DRAG_TOP = 5,
    DRAG_BOTTOM = 6,
    DRAG_LEFT = 7,
    DRAG_RIGHT = 8,
}TAiFlowDragHandlePosition, *PAiFlowDragHandlePosition;
typedef enum {
    ALIGN_LEFT = 0,
    ALIGN_RIGHT = 1,
    ALIGN_TOP = 2,
    ALIGN_BOTTOM = 3,
    ALIGN_CENTER_H = 4,
    ALIGN_CENTER_V = 5,
}TAiFlowAlignMode, *PAiFlowAlignMode;
typedef enum {
    BUS_UNKNOWN_TYPE = 0,
    TS_TCP_DEVICE = 1,
    XL_USB_DEVICE = 2,
    TS_USB_DEVICE = 3,
    PEAK_USB_DEVICE = 4,
    KVASER_USB_DEVICE = 5,
    ZLG_USB_DEVICE = 6,
    ICS_USB_DEVICE = 7,
    TS_TC1005_DEVICE = 8,
    CANABLE_USB_DEVICE = 9,
    TS_WIRELESS_OBD = 10,
    TS_USB_DEVICE_EX = 11,
    IXXAT_USB_DEVICE = 12,
    TS_ETH_IF_DEVICE = 13,
    TS_USB_IF_DEVICE = 14,
    BUS_DEV_TYPE_COUNT = 15,
}TLIBBusToolDeviceType, *PLIBBusToolDeviceType;
typedef enum {
    APP_CAN = 0,
    APP_LIN = 1,
    APP_FlexRay = 2,
    APP_Ethernet = 3,
    APP_AI = 4,
    APP_AO = 5,
    APP_DI = 6,
    APP_DO = 7,
    APP_GPS = 8,
}TLIBApplicationChannelType, *PLIBApplicationChannelType;
typedef enum {
    stCANSignal = 0,
    stLINSignal = 1,
    stSystemVar = 2,
    stFlexRay = 3,
    stEthernet = 4,
}TSignalType, *PSignalType;
typedef enum {
    trmRelativeMode = 0,
    trmTriggeredMode = 1,
    trmAbsoluteMode = 2,
}TTimeRangeTestMode, *PTimeRangeTestMode;
typedef enum {
    tstCANSignal = 0,
    tstLINSignal = 1,
    tstSystemVar = 2,
    tstFlexRay = 3,
    tstExpression = 4,
}TTriggerSignalType, *PTriggerSignalType;
typedef enum {
    sckAlways = 0,
    sckAppear = 1,
    sckStatistics = 2,
    sckRisingEdge = 3,
    sckFallingEdge = 4,
    sckMonotonyRising = 5,
    sckMonotonyFalling = 6,
    sckFollow = 7,
    sckJump = 8,
    sckNoChange = 9,
}TSignalCheckKind, *PSignalCheckKind;
typedef enum {
    tfrNoError = 0,
    tfrCheckSignalNotExistsInDB = 1,
    tfrMinBiggerThanMax = 2,
    tfrStartTimeBiggerThanEndTime = 3,
    tfrTriggerMinBiggerThanMax = 4,
    tfrSignalCountIs0 = 5,
    tfrFollowSignalNotExistsInDB = 6,
    tfrTriggerSignalNotExistsInDB = 7,
    tfrSignalFollowViolation = 8,
    tfrSignalMonotonyRisingViolation = 9,
    tfrSignalMonotonyFallingViolation = 10,
    tfrSignalNoChangeViolation = 11,
    tfrSignalValueOutOfRange = 12,
    tfrCANSignalNotExists = 13,
    tfrLINSignalNotExists = 14,
    tfrFlexRaySignalNotExists = 15,
    tfrSystemVarNotExists = 16,
    tfrSignalTesterStartFailedDueToInvalidConf = 17,
    tfrSignalValueNotExists = 18,
    tfrStatisticsCheckViolation = 19,
    tfrTriggerValueNotExists = 20,
    tfrFollowValueNotExists = 21,
    tfrTriggerValueNeverInRange = 22,
    tfrTimeRangeNotTouched = 23,
    tfrRisingNotDetected = 24,
    tfrFallingNotDetected = 25,
    tfrNotAppeared = 26,
    tfrJumpNotDetected = 27,
}TSignalTesterFailReason, *PSignalTesterFailReason;
typedef enum {
    sskMin = 0,
    sskMax = 1,
    sskAverage = 2,
    sskStdDeviation = 3,
}TSignalStatisticsKind, *PSignalStatisticsKind;
typedef enum {
    fcmIdentical = 0,
    fcmLinear = 1,
    fcmScaleLinear = 2,
    fcmTextTable = 3,
    fcmTABNoIntp = 4,
    fcmFormula = 5,
}TFlexRayCompuMethod, *PFlexRayCompuMethod;
typedef enum {
    cbsBusLoad = 0,
    cbsPeakLoad = 1,
    cbsFpsStdData = 2,
    cbsAllStdData = 3,
    cbsFpsExtData = 4,
    cbsAllExtData = 5,
    cbsFpsStdRemote = 6,
    cbsAllStdRemote = 7,
    cbsFpsExtRemote = 8,
    cbsAllExtRemote = 9,
    cbsFpsErrorFrame = 10,
    cbsAllErrorFrame = 11,
}TLIBCANBusStatistics, *PLIBCANBusStatistics;
typedef enum {
    ufpsNotFragment = 0,
    ufpsInvalid = 1,
    ufpsProcessing = 2,
    ufpsDone = 3,
}TUDPFragmentProcessStatus, *PUDPFragmentProcessStatus;
typedef enum {
    lsvtInt32 = 0,
    lsvtUInt32 = 1,
    lsvtInt64 = 2,
    lsvtUInt64 = 3,
    lsvtUInt8Array = 4,
    lsvtInt32Array = 5,
    lsvtInt64Array = 6,
    lsvtDouble = 7,
    lsvtDoubleArray = 8,
    lsvtString = 9,
}TLIBSystemVarType, *PLIBSystemVarType;
typedef enum {
    smdBiDirection = 0,
    smdSgnToSysVar = 1,
    smdSysVarToSgn = 2,
}TSymbolMappingDirection, *PSymbolMappingDirection;
typedef enum {
    rppInit = 0,
    rppReplaying = 1,
    rppEnded = 2,
}TReplayPhase, *PReplayPhase;
typedef enum {
    ortImmediately = 0,
    ortAsLog = 1,
    ortDelayed = 2,
}TLIBOnlineReplayTimingMode, *PLIBOnlineReplayTimingMode;
typedef enum {
    orsNotStarted = 0,
    orsRunning = 1,
    orsPaused = 2,
    orsCompleted = 3,
    orsTerminated = 4,
}TLIBOnlineReplayStatus, *PLIBOnlineReplayStatus;
typedef enum {
    rivUseDB = 0,
    rivUseLast = 1,
    rivUse0 = 2,
}TLIBRBSInitValueOptions, *PLIBRBSInitValueOptions;
typedef enum {
    sotCAN = 0,
    sotLIN = 1,
    sotCANFD = 2,
    sotRealtimeComment = 3,
    sotSystemVar = 4,
    sotFlexRay = 5,
    sotEthernet = 6,
    sotUnknown = 268435455,
}TSupportedObjType, *PSupportedObjType;
typedef enum {
    amrsNotRun = 0,
    amrsPrepareRun = 1,
    amrsRunning = 2,
    amrsPaused = 3,
    amrsStepping = 4,
    amrsFinished = 5,
}TLIBAutomationModuleRunningState, *PLIBAutomationModuleRunningState;
typedef enum {
    lastCANSignal = 0,
    lastLINSignal = 1,
    lastSysVar = 2,
    lastLocalVar = 3,
    lastConst = 4,
    lastFlexRaySignal = 5,
    lastImmediateValue = 6,
    lastUnknown = 268435455,
}TLIBAutomationSignalType, *PLIBAutomationSignalType;
typedef enum {
    lmfsSystemFunc = 0,
    lmfsMPLib = 1,
    lmfsInternal = 2,
}TLIBMPFuncSource, *PLIBMPFuncSource;
typedef enum {
    lvtInteger = 0,
    lvtDouble = 1,
    lvtString = 2,
    lvtCANMsg = 3,
    lvtCANFDMsg = 4,
    lvtLINMsg = 5,
    lvtUnknown = 268435455,
}TLIBSimVarType, *PLIBSimVarType;
typedef enum {
    sssStopped = 0,
    sssRunning = 1,
    sssPaused = 2,
}TSTIMSignalStatus, *PSTIMSignalStatus;
typedef enum {
    pstNone = 0,
    pstCANSignal = 1,
    pstLINSignal = 2,
    pstSystemVar = 3,
    pstFlexRaySignal = 4,
    pstAPICall = 5,
}TLIBPanelSignalType, *PLIBPanelSignalType;
typedef enum {
    pctText = 0,
    pctImage = 1,
    pctGroupBox = 2,
    pctPanel = 3,
    pctPathButton = 4,
    pctCheckBox = 5,
    pctTrackBar = 6,
    pctScrollBar = 7,
    pctInputOutputBox = 8,
    pctImageButton = 9,
    pctSelector = 10,
    pctButton = 11,
    pctProgressBar = 12,
    pctRadioButton = 13,
    pctStartStopButton = 14,
    pctSwitch = 15,
    pctLED = 16,
    pctPageControl = 17,
    pctGauge = 18,
    pctGraphics = 19,
    pctPie = 20,
    pctRelationChart = 21,
    pctMemo = 22,
    pctScrollBox = 23,
    pctFileSelector = 24,
}TLIBPanelControlType, *PLIBPanelControlType;
typedef enum {
    lfdtCAN = 0,
    lfdtISOCAN = 1,
    lfdtNonISOCAN = 2,
}TLIBCANFDControllerType, *PLIBCANFDControllerType;
typedef enum {
    lfdmNormal = 0,
    lfdmACKOff = 1,
    lfdmRestricted = 2,
    lfdmInternalLoopback = 3,
    lfdmExternalLoopback = 4,
}TLIBCANFDControllerMode, *PLIBCANFDControllerMode;
typedef enum {
    TS_UNKNOWN_DEVICE = 0,
    TSCAN_PRO = 1,
    TSCAN_Lite1 = 2,
    TC1001 = 3,
    TL1001 = 4,
    TC1011 = 5,
    TM5011 = 6,
    TC1002 = 7,
    TC1014 = 8,
    TSCANFD2517 = 9,
    TC1026 = 10,
    TC1016 = 11,
    TC1012 = 12,
    TC1013 = 13,
    TLog1002 = 14,
    TC1034 = 15,
    TC1018 = 16,
    GW2116 = 17,
    TC2115 = 18,
    MP1013 = 19,
    TC1113 = 20,
    TC1114 = 21,
    TP1013 = 22,
    TC1017 = 23,
    TP1018 = 24,
    TF10XX = 25,
    TL1004_FD_4_LIN_2 = 26,
    TE1051 = 27,
    TP1051 = 28,
    TP1034 = 29,
    TTS9015 = 30,
    TP1026 = 31,
    TTS1026 = 32,
    TTS1034 = 33,
    TTS1018 = 34,
    TL1011 = 35,
    TTS1015_LiAuto = 36,
    TTS1013_LiAuto = 37,
    TTS1016Pro = 38,
    TC1054Pro = 39,
    TC1054 = 40,
    TLog1038 = 41,
    TO1013 = 42,
    TC1034Pro = 43,
    TC1018Pro = 44,
    TC1038Pro = 45,
    TC1014Pro = 46,
    TC1034ProPlus = 47,
    TA1038 = 48,
    TC1055Pro = 49,
    TC1056Pro = 50,
    TC1057Pro = 51,
    TC4016 = 52,
    GW2208 = 53,
    TLog1039 = 54,
    GW1040 = 55,
    TC3014 = 56,
    TP1014 = 57,
    TA825_4 = 58,
    TC1013HV = 59,
    TC1052 = 60,
    TTS1017Pro = 61,
    TLog1057 = 62,
    TC1017Pro = 63,
    GW2202 = 64,
    GW2204 = 65,
    GW2212 = 66,
    TA821 = 67,
    TS_DEV_END = 68,
}TLIB_TS_Device_Sub_Type, *PLIB_TS_Device_Sub_Type;
typedef enum {
    XL_NONE = 0,
    XL_VIRTUAL = 1,
    XL_CANCARDX = 2,
    XL_CANAC2PCI = 6,
    XL_CANCARDY = 12,
    XL_CANCARDXL = 15,
    XL_CANCASEXL = 21,
    XL_CANCASEXL_LOG_OBSOLETE = 23,
    XL_CANBOARDXL = 25,
    XL_CANBOARDXL_PXI = 27,
    XL_VN2600 = 29,
    XL_VN3300 = 37,
    XL_VN3600 = 39,
    XL_VN7600 = 41,
    XL_CANCARDXLE = 43,
    XL_VN8900 = 45,
    XL_VN8950 = 47,
    XL_VN2640 = 53,
    XL_VN1610 = 55,
    XL_VN1630 = 57,
    XL_VN1640 = 59,
    XL_VN8970 = 61,
    XL_VN1611 = 63,
    XL_VN5610 = 65,
    XL_VN5620 = 66,
    XL_VN7570 = 67,
    XL_IPCLIENT = 69,
    XL_IPSERVER = 71,
    XL_VX1121 = 73,
    XL_VX1131 = 75,
    XL_VT6204 = 77,
    XL_VN1630_LOG = 79,
    XL_VN7610 = 81,
    XL_VN7572 = 83,
    XL_VN8972 = 85,
    XL_VN0601 = 87,
    XL_VN5640 = 89,
    XL_VX0312 = 91,
    XL_VH6501 = 94,
    XL_VN8800 = 95,
    XL_IPCL8800 = 96,
    XL_IPSRV8800 = 97,
    XL_CSMCAN = 98,
    XL_VN5610A = 101,
    XL_VN7640 = 102,
    XL_VX1135 = 104,
    XL_VN4610 = 105,
    XL_VT6306 = 107,
    XL_VT6104A = 108,
    XL_VN5430 = 109,
    XL_VN1530 = 112,
    XL_VN1531 = 113,
}TLIB_XL_Device_Sub_Type, *PLIB_XL_Device_Sub_Type;
typedef enum {
    T_MasterNode = 0,
    T_SlaveNode = 1,
    T_MonitorNode = 2,
}TLINNodeType, *PLINNodeType;
typedef enum {
    LIN_PROTOCL_13 = 0,
    LIN_PROTOCL_20 = 1,
    LIN_PROTOCL_21 = 2,
    LIN_PROTOCL_J2602 = 3,
}TLINProtocol, *PLINProtocol;
typedef enum {
    N_OK = 0,
    N_TP_TIMEOUT_AS = 139,
    N_TP_TIMEOUT_AR = 140,
    N_TP_TIMEOUT_BS = 141,
    N_TP_TIMEOUT_CR = 142,
    N_TP_WRONG_SN = 143,
    N_TP_INVALID_FS = 144,
    N_TP_UNEXP_PDU = 145,
    N_TP_WFT_OVRN = 146,
    N_TP_BUFFER_OVFLW = 147,
    N_TP_NOT_IDLE = 148,
    N_TP_ERROR_FROM_CAN_DRIVER = 149,
    N_LIN_MASTER_TRANSMIT_N_AS_TIMEOUT = 202,
    N_LIN_MASTER_TRANSMIT_TRANSMIT_ERROR = 203,
    N_LIN_MASTER_REV_N_CR_TIMEOUT = 204,
    N_LIN_MASTER_REV_ERROR = 205,
    N_LIN_MASTER_REV_INTERLLEAVE_TIMEOUT = 206,
    N_LIN_MASTER_REV_NO_RESPONSE = 207,
    N_LIN_MASTER_REV_SN_ERROR = 208,
    N_LIN_SLAVE_TRANSMIT_N_CR_TIMEOUT = 209,
    N_LIN_SLAVE_REV_N_CR_TIMEOUT = 210,
    N_LIN_SLAVE_TRANSMIT_ERROR = 211,
    N_LIN_SLAVE_REV_ERROR = 212,
    N_ETH_GENERIC_ACK = 234,
    N_ETH_VEHILCE_INFO_RES = 235,
    N_ETH_ACTIVATE_RES = 236,
    N_ETH_ALIVE_RES = 237,
    N_ETH_NODE_STATE_RES = 238,
    N_ETH_DIAG_POWER_MODE_RES = 239,
    N_ETH_DIAG_POSITIVE_ACK = 240,
    N_ETH_DIAG_NEGATIVE_ACK = 241,
    N_ETH_VEHICLE_REQ_ID = 242,
    N_ETH_VEHICLE_REQ_EID_ID = 243,
    N_ETH_VEHICLE_REQ_VIN_ID = 244,
    N_ETH_ACTIVE_REQ = 245,
    N_ETH_ALIVE_REQ = 246,
    N_ETH_NODE_STATE_REQ = 247,
    N_ETH_DIAG_POWER_MODE_REQ = 248,
    N_ETH_DIAG_REQ_RES = 249,
    N_ETH_RESERVED0 = 250,
    N_ETH_RESERVED1 = 251,
}ISO_TP_RESAULT, *PSO_TP_RESAULT;
typedef enum {
    tldt_CAN = 0,
    tldt_LIN = 1,
    tldt_FR = 2,
    tldt_Eth = 3,
    tldt_AI = 4,
    tldt_AO = 5,
    tldt_DI = 6,
    tldt_DO = 7,
    tldt_GPS = 8,
    tldt_Undef = 9,
}TLinkedDataChnType, *PLinkedDataChnType;
typedef enum {
    IPADDR_TYPE_V4 = 0,
    IPADDR_TYPE_V6 = 6,
    IPADDR_TYPE_ANY = 46,
}lwip_ip_addr_type, *Pwip_ip_addr_type;
typedef struct _TLIBFlexrayFrameTrigger{
    u16 slot_id;
    u8 frame_idx;
    u8 cycle_code;
    u8 config_byte;
    u8 rev;
}TLIBFlexrayFrameTrigger, *PLIBFlexrayFrameTrigger, *pLIBFlexrayFrameTrigger, **PPLIBFlexrayFrameTrigger, **ppLIBFlexrayFrameTrigger;

typedef struct _TLIBFlexrayConfigurationPara{
    u8 NETWORK_MANAGEMENT_VECTOR_LENGTH;
    u8 PAYLOAD_LENGTH_STATIC;
    u16 Reserved;
    u16 LATEST_TX;
    u16 T_S_S_TRANSMITTER;
    u8 CAS_RX_LOW_MAX;
    u8 SPEED;
    u16 WAKE_UP_SYMBOL_RX_WINDOW;
    u8 WAKE_UP_PATTERN;
    u8 WAKE_UP_SYMBOL_RX_IDLE;
    u8 WAKE_UP_SYMBOL_RX_LOW;
    u8 WAKE_UP_SYMBOL_TX_IDLE;
    u8 WAKE_UP_SYMBOL_TX_LOW;
    u8 channelAConnectedNode;
    u8 channelBConnectedNode;
}TLIBFlexrayConfigurationPara, *PLIBFlexrayConfigurationPara, *pLIBFlexrayConfigurationPara, **PPLIBFlexrayConfigurationPara, **ppLIBFlexrayConfigurationPara;

typedef struct _TLIBEthernetMAX{
    TLIBEthernetHeader FHeader;
    u8 FBytes[1612];
}TLIBEthernetMAX, *PLIBEthernetMAX, *pLIBEthernetMAX, **PPLIBEthernetMAX, **ppLIBEthernetMAX;

typedef struct _TLIBFlexRayClusterParameters{
    char FShortName[32];
    char FLongName[32];
    char FDescription[32];
    char FSpeed[32];
    char FChannels[32];
    char FBitCountingPolicy[32];
    char FProtocol[32];
    char FProtocolVersion[32];
    char FMedium[32];
    s32 FIsHighLowBitOrder;
    s32 FMaxFrameLengthByte;
    s32 FNumberOfCycles;
    s32 FCycle_us;
    double FBit_us;
    double FSampleClockPeriod_us;
    double FMacrotick_us;
    s32 FMacroPerCycle;
    s32 FNumberOfStaticSlots;
    s32 FStaticSlot_MT;
    s32 FActionPointOffset_MT;
    s32 FTSSTransmitter_gdBit;
    s32 FPayloadLengthStatic_WORD;
    s32 FNumberOfMiniSlots;
    s32 FMiniSlot_MT;
    s32 FMiniSlotActionPointOffset_MT;
    s32 FDynamicSlotIdlePhase_MiniSlots;
    s32 FSymbolWindow_MT;
    s32 FNIT_MT;
    s32 FSyncNodeMax;
    s32 FNetworkManagementVectorLength;
    s32 FListenNoise;
    s32 FColdStartAttempts;
    s32 FCASRxLowMax_gdBit;
    s32 FWakeupSymbolRxIdle_gdBit;
    s32 FWakeupSymbolRxLow_gdBit;
    s32 FWakeupSymbolRxWindow_gdBit;
    s32 FWakeupSymbolTxIdle_gdBit;
    s32 FWakeupSymbolTxLow_gdBit;
    double FMaxInitializationError_us;
    s32 FClusterDriftDamping_uT;
    s32 FOffsetCorrectionStart_MT;
    s32 FMaxWithoutClockCorrectionFatal;
    s32 FMaxWithoutClockCorrectionPassive;
}TLIBFlexRayClusterParameters, *PLIBFlexRayClusterParameters, *pLIBFlexRayClusterParameters, **PPLIBFlexRayClusterParameters, **ppLIBFlexRayClusterParameters;

typedef struct _TLIBFlexRayControllerParameters{
    char FShortName[32];
    char FConnectedChannels[32];
    s32 FMicroPerCycle_uT;
    s32 FMicroPerMacroNom_uT;
    double FMicroTick_us;
    s32 FSamplesPerMicrotick;
    s32 FWakeupChannelA;
    s32 FWakeupChannelB;
    s32 FMaxDrift_uT;
    s32 FWakeupPattern;
    s32 FListenTimeout_uT;
    s32 FAcceptedStartupRange_uT;
    s32 FMacroInitialOffsetA_MT;
    s32 FMacroInitialOffsetB_MT;
    s32 FMicroInitialOffsetA_uT;
    s32 FMicroInitialOffsetB_uT;
    char FKeySlotUsage[32];
    s32 FKeySlotID;
    s32 FSingleSlotEnabled;
    s32 FClusterDriftDamping_uT;
    s32 FDocodingCorrection_uT;
    s32 FDelayCompensationA_uT;
    s32 FDelayCompensationB_uT;
    s32 FOffsetCorrectionOut_uT;
    s32 FExternRateCorrection_uT;
    s32 FRateCorrectionOut_uT;
    s32 FExternOffsetCorrection_uT;
    s32 FAllowHaltDueToClock;
    s32 FAllowPassivToActive;
    s32 FLatestTx;
    s32 FMaxDynamicPayloadLength;
}TLIBFlexRayControllerParameters, *PLIBFlexRayControllerParameters, *pLIBFlexRayControllerParameters, **PPLIBFlexRayControllerParameters, **ppLIBFlexRayControllerParameters;

typedef struct _TLIBTrigger_def{
    u16 slot_id;
    u8 frame_idx;
    u8 cycle_code;
    u8 config_byte;
    u8 rev;
}TLIBTrigger_def, *PLIBTrigger_def, *pLIBTrigger_def, **PPLIBTrigger_def, **ppLIBTrigger_def;

typedef struct _TLIBGPSData{
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
}TLIBGPSData, *PLIBGPSData, *pLIBGPSData, **PPLIBGPSData, **ppLIBGPSData;

typedef struct _TLIBEth_CMD_config{
    u8 eth_config0;
    u8 eth_config1;
    u8 eth_config2;
    u8 eth_config3;
    u8 filter_config0;
    u8 filter_config1;
    u64 filter_hash_table;
    u64 filter_perfect0;
    u64 filter_perfect1;
    u8 params[16];
    u64 rev[4];
}TLIBEth_CMD_config, *PLIBEth_CMD_config, *pLIBEth_CMD_config, **PPLIBEth_CMD_config, **ppLIBEth_CMD_config;

typedef struct _TEMMC_RECORD_DATA{
    u32 FUTCDate;
    u32 FUTCTime;
    u32 FStartSector;
    u32 FSectorSize;
    u32 FOffSetMiniSecond;
}TEMMC_RECORD_DATA, *PEMMC_RECORD_DATA, *pEMMC_RECORD_DATA, **PPEMMC_RECORD_DATA, **ppEMMC_RECORD_DATA;

typedef struct _Trealtime_comment_t{
    s64 FTimeUs;
    s32 FEventType;
    u32 FCapacity;
    char* FComment;
    u32 FPadding;
}Trealtime_comment_t, *Prealtime_comment_t, *prealtime_comment_t, **PPrealtime_comment_t, **pprealtime_comment_t;

typedef struct _TLIBSystemVar{
    s64 FTimeUs;
    TLIBSystemVarType FType;
    u32 FNameCapacity;
    u32 FDataCapacity;
    char* FName;
    pu8 FData;
    s64 FPadding;
}TLIBSystemVar, *PLIBSystemVar, *pLIBSystemVar, **PPLIBSystemVar, **ppLIBSystemVar;

typedef struct _TLIBSystemVarDef{
    char FName[32];
    char FCategory[32];
    char FComment[32];
    TLIBSystemVarType FDataType;
    bool FIsReadOnly;
    double FValueMin;
    double FValueMax;
    char FUnit[32];
}TLIBSystemVarDef, *PLIBSystemVarDef, *pLIBSystemVarDef, **PPLIBSystemVarDef, **ppLIBSystemVarDef;

typedef struct _TMPCANSignal{
    u8 FCANSgnType;
    bool FIsIntel;
    s32 FStartBit;
    s32 FLength;
    double FFactor;
    double FOffset;
}TMPCANSignal, *PMPCANSignal, *pMPCANSignal, **PPMPCANSignal, **ppMPCANSignal;

typedef struct _TMPLINSignal{
    u8 FLINSgnType;
    bool FIsIntel;
    s32 FStartBit;
    s32 FLength;
    double FFactor;
    double FOffset;
}TMPLINSignal, *PMPLINSignal, *pMPLINSignal, **PPMPLINSignal, **ppMPLINSignal;

typedef struct _TMPFlexRaySignal{
    u8 FFRSgnType;
    u8 FCompuMethod;
    u8 FReserved;
    bool FIsIntel;
    s32 FStartBit;
    s32 FUpdateBit;
    s32 FLength;
    double FFactor;
    double FOffset;
    s32 FActualStartBit;
    s32 FActualUpdateBit;
}TMPFlexRaySignal, *PMPFlexRaySignal, *pMPFlexRaySignal, **PPMPFlexRaySignal, **ppMPFlexRaySignal;

typedef struct _TMPDBProperties{
    s32 FDBIndex;
    s32 FSignalCount;
    s32 FFrameCount;
    s32 FECUCount;
    u64 FSupportedChannelMask;
    char FName[512];
    char FComment[512];
    u32 FFlags;
    u32 FDBId;
}TMPDBProperties, *PMPDBProperties, *pMPDBProperties, **PPMPDBProperties, **ppMPDBProperties;

typedef struct _TMPDBECUProperties{
    s32 FDBIndex;
    s32 FECUIndex;
    s32 FTxFrameCount;
    s32 FRxFrameCount;
    char FName[512];
    char FComment[512];
}TMPDBECUProperties, *PMPDBECUProperties, *pMPDBECUProperties, **PPMPDBECUProperties, **ppMPDBECUProperties;

typedef struct _TMPDBFrameProperties{
    s32 FDBIndex;
    s32 FECUIndex;
    s32 FFrameIndex;
    u8 FIsTx;
    u8 FReserved1;
    u16 FCycleTimeMs;
    TSignalType FFrameType;
    u8 FCANIsDataFrame;
    u8 FCANIsStdFrame;
    u8 FCANIsEdl;
    u8 FCANIsBrs;
    s32 FCANIdentifier;
    s32 FCANDLC;
    s32 FCANDataBytes;
    s32 FLINIdentifier;
    s32 FLINDLC;
    u8 FFRChannelMask;
    u8 FFRBaseCycle;
    u8 FFRCycleRepetition;
    u8 FFRIsStartupFrame;
    u16 FFRSlotId;
    u16 FFRDLC;
    u64 FFRCycleMask;
    s32 FSignalCount;
    char FName[512];
    char FComment[512];
}TMPDBFrameProperties, *PMPDBFrameProperties, *pMPDBFrameProperties, **PPMPDBFrameProperties, **ppMPDBFrameProperties;

typedef struct _TMPDBSignalProperties{
    s32 FDBIndex;
    s32 FECUIndex;
    s32 FFrameIndex;
    s32 FSignalIndex;
    u8 FIsTx;
    u8 FReserved1;
    u8 FReserved2;
    u8 FReserved3;
    TSignalType FSignalType;
    TMPCANSignal FCANSignal;
    TMPLINSignal FLINSignal;
    TMPFlexRaySignal FFlexRaySignal;
    s32 FParentFrameId;
    double FInitValue;
    char FName[512];
    char FComment[512];
}TMPDBSignalProperties, *PMPDBSignalProperties, *pMPDBSignalProperties, **PPMPDBSignalProperties, **ppMPDBSignalProperties;

typedef struct _TLIBHWInfo{
    TLIBBusToolDeviceType FDeviceType;
    s32 FDeviceIndex;
    char FVendorName[32];
    char FDeviceName[32];
    char FSerialString[64];
}TLIBHWInfo, *PLIBHWInfo, *pLIBHWInfo, **PPLIBHWInfo, **ppLIBHWInfo;

typedef struct _TLIBTSMapping{
    char FAppName[32];
    s32 FAppChannelIndex;
    TLIBApplicationChannelType FAppChannelType;
    TLIBBusToolDeviceType FHWDeviceType;
    s32 FHWIndex;
    s32 FHWChannelIndex;
    s32 FHWDeviceSubType;
    char FHWDeviceName[32];
    bool FMappingDisabled;
}TLIBTSMapping, *PLIBTSMapping, *pLIBTSMapping, **PPLIBTSMapping, **ppLIBTSMapping;

typedef struct _Tip4_addr_t{
    u32 addr;
}Tip4_addr_t, *Pip4_addr_t, *pip4_addr_t, **PPip4_addr_t, **ppip4_addr_t;

typedef struct _Teth_addr_t{
    u8 addr[6];
}Teth_addr_t, *Peth_addr_t, *peth_addr_t, **PPeth_addr_t, **ppeth_addr_t;

typedef struct _Tts_sockaddr{
    u8 sa_len;
    u8 sa_family;
    char sa_data[14];
}Tts_sockaddr, *Pts_sockaddr, *pts_sockaddr, **PPts_sockaddr, **ppts_sockaddr;

typedef struct _Tts_addrinfo{
    s32 ai_flags;
    s32 ai_family;
    s32 ai_socktype;
    s32 ai_protocol;
    u32 ai_addrlen;
    Pts_sockaddr ai_addr;
    char* ai_canonname;
    struct _Tts_addrinfo* ai_next;
}Tts_addrinfo, *Pts_addrinfo, *pts_addrinfo, **PPts_addrinfo, **ppts_addrinfo;

typedef struct _Tts_hostent{
    char* h_name;
    ppchar h_aliases;
    s32 h_addrtype;
    s32 h_length;
    ppchar h_addr_list;
}Tts_hostent, *Pts_hostent, *pts_hostent, **PPts_hostent, **ppts_hostent;

typedef struct _Tip6_addr_t{
    u32 addr[4];
    u32 zone;
}Tip6_addr_t, *Pip6_addr_t, *pip6_addr_t, **PPip6_addr_t, **ppip6_addr_t;

typedef struct _Tts_net_device{
    Tip4_addr_t ip_addr;
    Tip4_addr_t netmask;
    Tip4_addr_t gw;
    Tip6_addr_t ip6_addr[3];
    u16 mtu;
    u16 mtu6;
    u16 vlan;
    u8 hwaddr[6];
    u8 flags;
    u8 index;
}Tts_net_device, *Pts_net_device, *pts_net_device, **PPts_net_device, **ppts_net_device;

typedef struct _Tip_addr_t{
    Tip6_addr_t ip4Or6;
    u32 FType;
}Tip_addr_t, *Pip_addr_t, *pip_addr_t, **PPip_addr_t, **ppip_addr_t;

typedef struct _Ts_in_addr{
    u32 ts_addr;
}Ts_in_addr, *Ps_in_addr, *ps_in_addr, **PPs_in_addr, **pps_in_addr;

typedef struct _Ts_in6_addr{
    u32 u32_addr[4];
}Ts_in6_addr, *Ps_in6_addr, *ps_in6_addr, **PPs_in6_addr, **pps_in6_addr;

typedef struct _Tts_sockaddr_in{
    u8 sin_len;
    u8 sin_family;
    u16 sin_port;
    Ts_in_addr sin_addr;
    char sin_zero[8];
}Tts_sockaddr_in, *Pts_sockaddr_in, *pts_sockaddr_in, **PPts_sockaddr_in, **ppts_sockaddr_in;

typedef struct _Tts_sockaddr_in6{
    u8 sin6_len;
    u8 sin6_family;
    u16 sin6_port;
    u32 sin6_flowinfo;
    Ts_in6_addr sin6_addr;
    u32 sin6_scope_id;
}Tts_sockaddr_in6, *Pts_sockaddr_in6, *pts_sockaddr_in6, **PPts_sockaddr_in6, **ppts_sockaddr_in6;

typedef struct _Tts_iovec{
    pnative_int iov_base;
    size_t iov_len;
}Tts_iovec, *Pts_iovec, *pts_iovec, **PPts_iovec, **ppts_iovec;

typedef struct _Tts_timeval{
    s32 tv_sec;
    s32 tv_usec;
}Tts_timeval, *Pts_timeval, *pts_timeval, **PPts_timeval, **ppts_timeval;

typedef struct _Tts_fd_set{
    u8 fd_bits[32];
}Tts_fd_set, *Pts_fd_set, *pts_fd_set, **PPts_fd_set, **ppts_fd_set;

typedef struct _Tts_pollfd{
    s32 fd;
    s16 events;
    s16 revents;
}Tts_pollfd, *Pts_pollfd, *pts_pollfd, **PPts_pollfd, **ppts_pollfd;

typedef struct _Tts_msghdr{
    pnative_int msg_name;
    u32 msg_namelen;
    u32 reserved0;
    Pts_iovec msg_iov;
    s32 msg_iovlen;
    u32 reserved1;
    pnative_int msg_control;
    u32 msg_controllen;
    s32 msg_flags;
}Tts_msghdr, *Pts_msghdr, *pts_msghdr, **PPts_msghdr, **ppts_msghdr;

typedef struct _Tts_cmsghdr{
    u32 cmsg_len;
    s32 cmsg_level;
    s32 cmsg_type;
}Tts_cmsghdr, *Pts_cmsghdr, *pts_cmsghdr, **PPts_cmsghdr, **ppts_cmsghdr;

typedef struct _Tts_in_pktinfo{
    u32 ipi_ifindex;
    Ts_in_addr ipi_addr;
}Tts_in_pktinfo, *Pts_in_pktinfo, *pts_in_pktinfo, **PPts_in_pktinfo, **ppts_in_pktinfo;

typedef struct _TTSMetricIntegerSnapshot{
    u64 FCount;
    s64 FMinValue;
    s64 FMaxValue;
    s64 FCurrValue;
    double FMean;
    double FStdDev;
    s64 FModifyTimestamp;
    s64 FMinEventTimestamp;
    s64 FMaxEventTimestamp;
}TTSMetricIntegerSnapshot, *PTSMetricIntegerSnapshot, *pTSMetricIntegerSnapshot, **PPTSMetricIntegerSnapshot, **ppTSMetricIntegerSnapshot;

typedef void(__cdecl*TCProcedure)();
// Arg[0] AData
typedef void(__stdcall*TCANQueueEvent_API)(const PLIBCAN AData);
// Arg[0] AObj
// Arg[1] AData
typedef void(__stdcall*TGPSQueueEvent_Win32)(const pnative_int AObj,const PLIBGPSData AData);
// Arg[0] AObj
// Arg[1] AData
typedef void(__stdcall*TCANQueueEvent_Win32)(const pnative_int AObj,const PLIBCAN AData);
// Arg[0] AObj
// Arg[1] AData
typedef void(__stdcall*TCANFDQueueEvent_Win32)(const pnative_int AObj,const PLIBCANFD AData);
// Arg[0] AObj
// Arg[1] AData
typedef void(__stdcall*TFlexRayQueueEvent_Win32)(const pnative_int AObj,const PLIBFlexRay AData);
// Arg[0] AObj
// Arg[1] AData
typedef void(__stdcall*TEthernetQueueEvent_Win32)(const pnative_int AObj,const PLIBEthernetHeader AData);
// Arg[0] AObj
// Arg[1] AData
typedef void(__stdcall*TLINQueueEvent_Win32)(const pnative_int AObj,const PLIBLIN AData);
// Arg[0] AStr
// Arg[1] ALevel
typedef void(__stdcall*TLIBTSMasterLogger)(const char* AStr,const s32 ALevel);
// Arg[0] APointer
// Arg[1] ASize
typedef void(__stdcall*TOnIoIPData)(const pnative_int APointer,const s32 ASize);
// Arg[0] APointer
// Arg[1] ASize
typedef void(__stdcall*TOnRpcData)(const pnative_int APointer,const size_t ASize);
// Arg[0] ACAN
// Arg[1] ADataId
// Arg[2] AValue
typedef void(__stdcall*TOnAutoSARE2ECanEvt)(const PLIBCANFD ACAN,const u32 ADataId,const pu64 AValue);
// Arg[0] AChnIdx
// Arg[1] APDUName
// Arg[2] ATimestamp
// Arg[3] AIsTx
// Arg[4] AID
// Arg[5] ADataLength
// Arg[6] AData
typedef void(__stdcall*TOnAutoSARPDUQueueEvent)(const s32 AChnIdx,const char* APDUName,const u64 ATimestamp,const u8 AIsTx,const u32 AID,const u32 ADataLength,const pu8 AData);
// Arg[0] AChnIdx
// Arg[1] APDUName
// Arg[2] AID
// Arg[3] ASrcDataLength
// Arg[4] ASrcSecuredDataLength
// Arg[5] ASrcData
typedef s32 (__stdcall*TOnAutoSARPDUPreTxEvent)(const s32 AChnIdx,const char* APDUName,const u32 AID,const u32 ASrcDataLength,const u32 ASrcSecuredDataLength,const pu8 ASrcData);
// Arg[0] ASignalName
// Arg[1] ARawValue
// Arg[2] APhyValue
typedef void(__stdcall*TOnSignalEvent)(const char* ASignalName,const s64 ARawValue,const double APhyValue);
// Arg[0] AVidPid
// Arg[1] ASerial
typedef void(__stdcall*TOnUSBPlugEvent)(const char* AVidPid,const char* ASerial);
// Arg[0] APointer
// Arg[1] ASize
typedef void(__stdcall*TOnIoIPData_API)(const pnative_int APointer,const s32 ASize);
// Arg[0] AIPAddress
// Arg[1] APort
typedef void(__stdcall*TOnIoIPConnection)(const char* AIPAddress,const s32 APort);
// Arg[0] AIPAddress
// Arg[1] APort
typedef void(__stdcall*TOnIoIPConnection_API)(const char* AIPAddress,const s32 APort);
// Arg[0] AObj
// Arg[1] AName
// Arg[2] AGroup
// Arg[3] ADesc
// Arg[4] AExample
// Arg[5] AParaCount
typedef void(__stdcall*TLIBWriteAPIDocumentFunc)(const pnative_int AObj,const char* AName,const char* AGroup,const char* ADesc,const char* AExample,const s32 AParaCount);
// Arg[0] AObj
// Arg[1] AIdx
// Arg[2] AAPIName
// Arg[3] AParaName
// Arg[4] AIsConst
// Arg[5] AParaType
// Arg[6] ADesc
typedef void(__stdcall*TLIBWriteAPIParaFunc)(const pnative_int AObj,const s32 AIdx,const char* AAPIName,const char* AParaName,const bool AIsConst,const char* AParaType,const char* ADesc);
// Arg[0] AObj
// Arg[1] AWriteDoc
// Arg[2] AWritePara
typedef void(__stdcall*TLIBWriteAPIDocument)(const pnative_int AObj,const TLIBWriteAPIDocumentFunc AWriteDoc,const TLIBWriteAPIParaFunc AWritePara);
typedef bool (__stdcall*TLIBCheckResult)();
// Arg[0] ACompleteName
typedef void(__stdcall*TLIBOnSysVarChange)(const char* ACompleteName);
// Arg[0] AObj
// Arg[1] ASocket
// Arg[2] AClientSocket
// Arg[3] AResult
typedef void(__stdcall*TSSocketListenEvent)(const pnative_int AObj,const s32 ASocket,const s32 AClientSocket,const s32 AResult);
// Arg[0] AObj
// Arg[1] ASocket
// Arg[2] AResult
typedef void(__stdcall*TSSocketNotifyEvent)(const pnative_int AObj,const s32 ASocket,const s32 AResult);
// Arg[0] AObj
// Arg[1] ASocket
// Arg[2] AResult
// Arg[3] AAddr
// Arg[4] APort
// Arg[5] AData
// Arg[6] ASize
typedef void(__stdcall*TSSocketReceiveEvent)(const pnative_int AObj,const s32 ASocket,const s32 AResult,const u32 AAddr,const u32 APort,const pu8 AData,const s32 ASize);
// Arg[0] AObj
// Arg[1] ASocket
// Arg[2] AResult
// Arg[3] ARemoteEndPoint
// Arg[4] AData
// Arg[5] ASize
typedef void(__stdcall*TSSocketReceiveEventV2)(const pnative_int AObj,const s32 ASocket,const s32 AResult,const char* ARemoteEndPoint,const pu8 AData,const s32 ASize);
// Arg[0] AObj
// Arg[1] ASocket
// Arg[2] AResult
// Arg[3] ADstEndPoint
// Arg[4] ASrcEndPoint
// Arg[5] AData
// Arg[6] ASize
typedef void(__stdcall*TSSocketReceiveEventV3)(const pnative_int AObj,const s32 ASocket,const s32 AResult,const char* ADstEndPoint,const char* ASrcEndPoint,const pu8 AData,const s32 ASize);
// Arg[0] AObj
// Arg[1] ASocket
// Arg[2] AResult
// Arg[3] AData
// Arg[4] ASize
typedef void(__stdcall*TSSocketTransmitEvent)(const pnative_int AObj,const s32 ASocket,const s32 AResult,const pu8 AData,const s32 ASize);
// Arg[0] AObj
// Arg[1] ASocket
// Arg[2] AClientSocket
// Arg[3] AResult
typedef void(__stdcall*TSSocketListenEvent_Win32)(const pnative_int AObj,const s32 ASocket,const s32 AClientSocket,const s32 AResult);
// Arg[0] AObj
// Arg[1] ASocket
// Arg[2] AResult
typedef void(__stdcall*TSSocketNotifyEvent_Win32)(const pnative_int AObj,const s32 ASocket,const s32 AResult);
// Arg[0] AObj
// Arg[1] ASocket
// Arg[2] AResult
// Arg[3] AAddr
// Arg[4] APort
// Arg[5] AData
// Arg[6] ASize
typedef void(__stdcall*TSSocketReceiveEvent_Win32)(const pnative_int AObj,const s32 ASocket,const s32 AResult,const u32 AAddr,const u32 APort,const pu8 AData,const s32 ASize);
// Arg[0] AObj
// Arg[1] ASocket
// Arg[2] AResult
// Arg[3] ARemoteEndPoint
// Arg[4] AData
// Arg[5] ASize
typedef void(__stdcall*TSSocketReceiveEventV2_Win32)(const pnative_int AObj,const s32 ASocket,const s32 AResult,const char* ARemoteEndPoint,const pu8 AData,const s32 ASize);
// Arg[0] AObj
// Arg[1] ASocket
// Arg[2] AResult
// Arg[3] ADstEndPoint
// Arg[4] ASrcEndPoint
// Arg[5] AData
// Arg[6] ASize
typedef void(__stdcall*TSSocketReceiveEventV3_Win32)(const pnative_int AObj,const s32 ASocket,const s32 AResult,const char* ADstEndPoint,const char* ASrcEndPoint,const pu8 AData,const s32 ASize);
// Arg[0] AObj
// Arg[1] ASocket
// Arg[2] AResult
// Arg[3] AData
// Arg[4] ASize
typedef void(__stdcall*TSSocketTransmitEvent_Win32)(const pnative_int AObj,const s32 ASocket,const s32 AResult,const pu8 AData,const s32 ASize);
// Arg[0] AIdxChn
// Arg[1] ATimestamp
// Arg[2] APackCmd
// Arg[3] AParameter
// Arg[4] AParameterLength
// Arg[5] AData
// Arg[6] ADataLength
typedef void(__stdcall*TDatapackageProcessEvent)(const u8 AIdxChn,const s64 ATimestamp,const u16 APackCmd,const pu8 AParameter,const u16 AParameterLength,const pu8 AData,const s32 ADataLength);
// Arg[0] AIdxChn
// Arg[1] ATimestamp
// Arg[2] APackCmd
// Arg[3] AParameter
// Arg[4] AParameterLength
// Arg[5] AData
// Arg[6] ADataLength
typedef void(__stdcall*TDatapackageProcessEvent_Win32)(const u8 AIdxChn,const s64 ATimestamp,const u16 APackCmd,const pu8 AParameter,const u16 AParameterLength,const pu8 AData,const s32 ADataLength);
// Arg[0] debugger
// Arg[1] AEvent
// Arg[2] file_name
// Arg[3] line
// Arg[4] user_data
typedef s32 (__stdcall*TMPTacDebugCallback)(const pvoid debugger,const TMPTacDebugEvent AEvent,const char* file_name,const s32 line,const pnative_int user_data);
// Arg[0] AObj
// Arg[1] AProgress100
typedef void(__stdcall*TReadProgressCallback)(const pnative_int AObj,const double AProgress100);
// Arg[0] AObj
// Arg[1] AProgress
typedef s32 (__cdecl*TSeekTimeProgressCallback)(const pnative_int AObj,const float AProgress);
// Arg[0] AObj
// Arg[1] AComment
// Arg[2] AProgress100
// Arg[3] AToTerminate
typedef void(__stdcall*TReadBLFRealtimeCommentCallback)(const pnative_int AObj,const Prealtime_comment_t AComment,const double AProgress100,const pbool AToTerminate);
// Arg[0] AObj
// Arg[1] ASysVar
// Arg[2] AProgress100
// Arg[3] AToTerminate
typedef void(__stdcall*TReadBLFSystemVarCallback)(const pnative_int AObj,const PLIBSystemVar ASysVar,const double AProgress100,const pbool AToTerminate);
// Arg[0] AObj
// Arg[1] AProgress100
typedef void(__stdcall*TReadUnsupportedCallback)(const pnative_int AObj,const double AProgress100);
// Arg[0] pDiagModuleIndex
// Arg[1] AChnIndex
// Arg[2] ASupportFDCAN
// Arg[3] AMaxDLC
// Arg[4] ARequestID
// Arg[5] ARequestIDIsStd
// Arg[6] AResponseID
// Arg[7] AResponseIDIsStd
// Arg[8] AFunctionID
// Arg[9] AFunctionIDIsStd
typedef s32 (__stdcall*Ttsdiag_can_create)(const ps32 pDiagModuleIndex,const u32 AChnIndex,const u8 ASupportFDCAN,const u8 AMaxDLC,const u32 ARequestID,const bool ARequestIDIsStd,const u32 AResponseID,const bool AResponseIDIsStd,const u32 AFunctionID,const bool AFunctionIDIsStd);
// Arg[0] ADiagModuleIndex
// Arg[1] AFDMode
// Arg[2] ASupportBRS
// Arg[3] AMaxDLC
typedef s32 (__stdcall*Ttsdiag_set_fdmode)(const s32 ADiagModuleIndex,const bool AFDMode,const bool ASupportBRS,const s32 AMaxDLC);
// Arg[0] ADiagModuleIndex
typedef s32 (__stdcall*Ttsdiag_can_delete)(const s32 ADiagModuleIndex);
typedef void(__stdcall*Ttsdiag_can_delete_all)();
// Arg[0] ADiagModuleIndex
// Arg[1] AReqDataArray
// Arg[2] AReqDataSize
// Arg[3] AResponseDataArray
// Arg[4] AResponseDataSize
typedef s32 (__stdcall*Ttstp_can_request_and_get_response)(const s32 ADiagModuleIndex,const pu8 AReqDataArray,const s32 AReqDataSize,const pu8 AResponseDataArray,const ps32 AResponseDataSize);
// Arg[0] ADiagModuleIndex
// Arg[1] AReqDataArray
// Arg[2] AReqDataSize
// Arg[3] AResponseDataArray
// Arg[4] AResponseDataSize
typedef s32 (__stdcall*Ttstp_can_request_and_get_response_functional)(const s32 ADiagModuleIndex,const pu8 AReqDataArray,const s32 AReqDataSize,const pu8 AResponseDataArray,const ps32 AResponseDataSize);
// Arg[0] ATpModuleIndex
// Arg[1] AChn
typedef void(__stdcall*N_USData_RevData_Recall_Obj)(const s32 ATpModuleIndex,const s32 AChn);
// Arg[0] ATpModuleIndex
// Arg[1] AChn
// Arg[2] ABusType
// Arg[3] ANAD
// Arg[4] AIdentifier
// Arg[5] ATimeStamp
// Arg[6] APayLoad
// Arg[7] ASize
// Arg[8] AError
typedef void(__stdcall*N_USData_TranslateCompleted_Recall_Obj)(const s32 ATpModuleIndex,const s32 AChn,const u8 ABusType,const s32 ANAD,const s32 AIdentifier,const u64 ATimeStamp,const pu8 APayLoad,const u32 ASize,const ISO_TP_RESAULT AError);
// Arg[0] ATpModuleIndex
// Arg[1] AChn
// Arg[2] ATimeStamp
// Arg[3] APayLoad
// Arg[4] ASize
// Arg[5] AError
typedef void(__stdcall*N_USData_TranslateCompleted_Recall)(const s32 ATpModuleIndex,const s32 AChn,const u64 ATimeStamp,const pu8 APayLoad,const u32 ASize,const ISO_TP_RESAULT AError);
// Arg[0] AMsg
// Arg[1] ALevel
typedef void(__stdcall*TLogDebuggingInfo_t)(const char* AMsg,const s32 ALevel);
// Arg[0] sock
// Arg[1] p
// Arg[2] len
typedef void(__cdecl*tosun_recv_callback)(const s32 sock,const pnative_int p,const u16 len);
// Arg[0] sock
// Arg[1] p
// Arg[2] src
// Arg[3] dest
// Arg[4] ttl
// Arg[5] tos
typedef void(__cdecl*tosun_tcp_presend_callback)(const s32 sock,const pnative_int p,const Pip_addr_t src,const Pip_addr_t dest,const u8 ttl,const u8 tos);
// Arg[0] sock
// Arg[1] p
// Arg[2] len
typedef void(__cdecl*tosun_tcp_ack_callback)(const s32 sock,const pnative_int p,const u16 len);
// Arg[0] AIdxChn
// Arg[1] ATypeName
// Arg[2] ATopicName
// Arg[3] AOriData
// Arg[4] AOriLength
// Arg[5] ANewData
// Arg[6] ANewLength
typedef s32 (__stdcall*Tdds_pre_deserialize_callback)(const u32 AIdxChn,const char* ATypeName,const char* ATopicName,const pu8 AOriData,const u32 AOriLength,const pu8 ANewData,const pu32 ANewLength);
// Arg[0] AIdxChn
// Arg[1] ATypeName
// Arg[2] ATopicName
// Arg[3] AOriData
// Arg[4] AOriLength
// Arg[5] ANewData
// Arg[6] ANewLength
typedef s32 (__stdcall*Tdds_after_serialize_callback)(const u32 AIdxChn,const char* ATypeName,const char* ATopicName,const pu8 AOriData,const u32 AOriLength,const pu8 ANewData,const pu32 ANewLength);
#if defined ( __cplusplus )
extern  "C"
{
#endif
TSAPI(void)finalize_lib_tsmaster();

TSAPI(void)tsfifo_enable_receive_fifo();

TSAPI(void)tsfifo_disable_receive_fifo();

TSAPI(void)tsfifo_enable_receive_error_frames();

TSAPI(void)tsfifo_disable_receive_error_frames();

TSAPI(void)tsdiag_can_delete_all();

TSAPI(void)tsdiag_delete_all();

TSAPI(void)rawsocket_dhcp_stop(const s32 ANetworkIndex);

TSAPI(void)tssocket_ping4(const s32 ANetworkIndex,const Pip4_addr_t ping_addr,const s32 repeatcnt,const u32 interval_ms,const u32 timeout_ms);

TSAPI(void)tssocket_ping6(const s32 ANetworkIndex,const Pip6_addr_t ping_addr,const s32 repeatcnt,const u32 interval_ms,const u32 timeout_ms);

TSAPI(s32)set_libtsmaster_location(const char* AFilePath);

TSAPI(s32)get_libtsmaster_location(const ppchar AFilePath);

TSAPI(s32)initialize_lib_tsmaster(const char* AAppName);

TSAPI(s32)initialize_lib_tsmaster_with_project(const char* AAppName,const char* AProjectFileName);

TSAPI(s32)tsapp_set_logger(const TLIBTSMasterLogger ALogger);

TSAPI(s32)tsapp_log(const char* AStr,const s32 ALevel);

TSAPI(s32)tsapp_set_current_application(const char* AAppName);

TSAPI(s32)tsapp_get_current_application(const ppchar AAppName);

TSAPI(s32)tsapp_del_application(const char* AAppName);

TSAPI(s32)tsapp_add_application(const char* AAppName);

TSAPI(s32)tsapp_get_application_list(const ppchar AAppNameList);

TSAPI(s32)tsapp_set_can_channel_count(const s32 ACount);

TSAPI(s32)tsapp_set_lin_channel_count(const s32 ACount);

TSAPI(s32)tsapp_set_flexray_channel_count(const s32 ACount);

TSAPI(s32)tsapp_get_can_channel_count(s32* ACount);

TSAPI(s32)tsapp_get_lin_channel_count(s32* ACount);

TSAPI(s32)tsapp_get_flexray_channel_count(s32* ACount);

TSAPI(s32)tsapp_set_mapping(const PLIBTSMapping AMapping);

TSAPI(s32)tsapp_set_mapping_verbose(const char* AAppName,const TLIBApplicationChannelType AAppChannelType,const s32 AAppChannel,const char* AHardwareName,const TLIBBusToolDeviceType AHardwareType,const s32 AHardwareSubType,const s32 AHardwareIndex,const s32 AHardwareChannel,const bool AEnableMapping);

TSAPI(s32)tsapp_get_mapping(const PLIBTSMapping AMapping);

TSAPI(s32)tsapp_del_mapping(const PLIBTSMapping AMapping);

TSAPI(s32)tsapp_del_mapping_verbose(const char* AAppName,const TLIBApplicationChannelType AAppChannelType,const s32 AAppChannel);

TSAPI(s32)tsapp_connect();

TSAPI(s32)tsapp_disconnect();

TSAPI(s32)tsapp_set_turbo_mode(const bool AEnable);

TSAPI(s32)tsapp_get_turbo_mode(bool* AEnable);

TSAPI(s32)tsapp_get_error_description(const s32 ACode,const ppchar ADesc);

TSAPI(s32)tsapp_show_channel_mapping_window();

TSAPI(s32)tsapp_show_hardware_configuration_window();

TSAPI(s32)tsapp_show_tsmaster_window(const char* AWindowName,const bool AWaitClose);

TSAPI(s32)tsapp_get_timestamp(const ps64 ATimeUs);

TSAPI(s32)tsapp_execute_python_string(const char* AString,const char* AArguments,const bool ASync,const bool AIsX64,const ppchar AResultLog);

TSAPI(s32)tsapp_execute_python_script(const char* AFilePath,const char* AArguments,const bool ASync,const bool AIsX64,const ppchar AResultLog);

TSAPI(s32)tsapp_get_tsmaster_version(const ps32 AYear,const ps32 AMonth,const ps32 ADay,const ps32 ABuildNumber);

TSAPI(s32)tsapp_get_system_constant_count(const s32 AIdxType,const ps32 ACount);

TSAPI(s32)tsapp_get_system_constant_value_by_index(const s32 AIdxType,const s32 AIdxValue,const ppchar AName,const pdouble AValue,const ppchar ADesc);

TSAPI(s32)tsapp_enumerate_hw_devices(s32* ACount);

TSAPI(s32)tsapp_get_hw_info_by_index(const s32 AIndex,const PLIBHWInfo AHWInfo);

TSAPI(s32)tsapp_get_hw_info_by_index_verbose(const s32 AIndex,const PLIBBusToolDeviceType ADeviceType,const char* AVendorNameBuffer,const s32 AVendorNameBufferSize,const char* ADeviceNameBuffer,const s32 ADeviceNameBufferSize,const char* ASerialStringBuffer,const s32 ASerialStringBufferSize);

TSAPI(s32)tsapp_set_vendor_detect_preferences(const bool AScanTOSUN,const bool  AScanVector,const bool  AScanPeak,const bool  AScanKvaser,const bool  AScanZLG,const bool  ADetectIntrepidcs,const bool  ADetectCANable);

TSAPI(s32)tsapp_get_vendor_detect_preferences(bool* AScanTOSUN,bool*  AScanVector,bool*  AScanPeak,bool*  AScanKvaser,bool*  AScanZLG,bool*  ADetectIntrepidcs,bool*  ADetectCANable);

TSAPI(s32)tsapp_configure_baudrate_lin(const s32 AIdxChn,const float ABaudrateKbps,const s32 AProtocol);

TSAPI(s32)tsapp_configure_baudrate_can(const s32 AIdxChn,const float ABaudrateKbps,const bool AListenOnly,const bool AInstallTermResistor120Ohm);

TSAPI(s32)tsapp_configure_baudrate_canfd(const s32 AIdxChn,const float AArbRateKbps,const float  ADataRateKbps,const TLIBCANFDControllerType AControllerType,const TLIBCANFDControllerMode AControllerMode,const bool AInstallTermResistor120Ohm);

TSAPI(s32)tsapp_configure_ethernet_parameter(const s32 AIdxChn,const s32 AEnabled,const s32 APhyType,const s32 AIsMaster,const s32 AIsAutoNegotiation,const s32 ASpeedType,const s32 ALoopModeType,const s32 AByPassMode,const char* AMacAddress);

TSAPI(s32)tsapp_configure_can_regs(const s32 AIdxChn,const float ABaudrateKbps,const s32 ASEG1,const s32  ASEG2,const s32  APrescaler,const s32  ASJW,const s32 AOnlyListen,const s32 A120OhmConnected);

TSAPI(s32)tsapp_configure_canfd_regs(const s32 AIdxChn,const float AArbBaudrate,const s32 AArbSEG1,const s32  AArbSEG2,const s32  AArbPrescaler,const s32  AArbSJW,const float ADataBaudrate,const s32 ADataSEG1,const s32  ADataSEG2,const s32  ADataPrescaler,const s32  ADataSJW,const TLIBCANFDControllerType AControllerType,const TLIBCANFDControllerMode AControllerMode,const s32 A120OhmConnected);

TSAPI(s32)tsapp_transmit_can_async(const PLIBCAN ACAN);

TSAPI(s32)tsapp_transmit_canfd_async(const PLIBCANFD ACANFD);

TSAPI(s32)tsapp_transmit_lin_async(const PLIBLIN ALIN);

TSAPI(s32)tsapp_transmit_fastlin_async(const PLIBLIN ALIN);

TSAPI(s32)tsapp_transmit_lin_wakeup_async(const s32 AIdxChn,const s32 AWakeupLength,const s32 AWakeupIntervalTime,const s32 AWakeupTimes);

TSAPI(s32)tsapp_transmit_lin_gotosleep_async(const s32 AIdxChn);

TSAPI(s32)tsapp_transmit_flexray_async(const PLIBFlexRay AFlexRay);

TSAPI(s32)tsapp_transmit_can_sync(const PLIBCAN ACAN,const s32 ATimeoutMS);

TSAPI(s32)tsapp_transmit_canfd_sync(const PLIBCANFD ACANfd,const s32 ATimeoutMS);

TSAPI(s32)tsapp_transmit_lin_sync(const PLIBLIN ALIN,const s32 ATimeoutMS);

TSAPI(s32)tsfifo_add_can_canfd_pass_filter(const s32 AIdxChn,const s32 AIdentifier,const bool AIsStd);

TSAPI(s32)tsfifo_add_lin_pass_filter(const s32 AIdxChn,const s32 AIdentifier);

TSAPI(s32)tsfifo_delete_can_canfd_pass_filter(const s32 AIdxChn,const s32 AIdentifier);

TSAPI(s32)tsfifo_delete_lin_pass_filter(const s32 AIdxChn,const s32 AIdentifier);

TSAPI(s32)tsfifo_receive_can_msgs(const PLIBCAN ACANBuffers,const ps32 ACANBufferSize,const s32 AIdxChn,const bool AIncludeTx);

TSAPI(s32)tsfifo_receive_canfd_msgs(const PLIBCANFD ACANFDBuffers,const ps32 ACANFDBufferSize,const s32 AIdxChn,const bool AIncludeTx);

TSAPI(s32)tsfifo_receive_lin_msgs(const PLIBLIN ALINBuffers,const ps32 ALINBufferSize,const s32 AIdxChn,const bool AIncludeTx);

TSAPI(s32)tsfifo_receive_fastlin_msgs(const PLIBLIN AFastLINBuffers,const ps32 AFastLINBufferSize,const s32 AIdxChn,const bool AIncludeTx);

TSAPI(s32)tsfifo_clear_can_receive_buffers(const s32 AIdxChn);

TSAPI(s32)tsfifo_clear_canfd_receive_buffers(const s32 AIdxChn);

TSAPI(s32)tsfifo_clear_lin_receive_buffers(const s32 AIdxChn);

TSAPI(s32)tsfifo_clear_fastlin_receive_buffers(const s32 AIdxChn);

TSAPI(s32)tsfifo_read_can_buffer_frame_count(const s32 AIdxChn,s32* ACount);

TSAPI(s32)tsfifo_read_can_tx_buffer_frame_count(const s32 AIdxChn,s32* ACount);

TSAPI(s32)tsfifo_read_can_rx_buffer_frame_count(const s32 AIdxChn,s32* ACount);

TSAPI(s32)tsfifo_read_canfd_buffer_frame_count(const s32 AIdxChn,s32* ACount);

TSAPI(s32)tsfifo_read_canfd_tx_buffer_frame_count(const s32 AIdxChn,s32* ACount);

TSAPI(s32)tsfifo_read_canfd_rx_buffer_frame_count(const s32 AIdxChn,s32* ACount);

TSAPI(s32)tsfifo_read_lin_buffer_frame_count(const s32 AIdxChn,s32* ACount);

TSAPI(s32)tsfifo_read_lin_tx_buffer_frame_count(const s32 AIdxChn,s32* ACount);

TSAPI(s32)tsfifo_read_lin_rx_buffer_frame_count(const s32 AIdxChn,s32* ACount);

TSAPI(s32)tsfifo_read_fastlin_buffer_frame_count(const s32 AIdxChn,s32* ACount);

TSAPI(s32)tsfifo_read_fastlin_tx_buffer_frame_count(const s32 AIdxChn,s32* ACount);

TSAPI(s32)tsfifo_read_fastlin_rx_buffer_frame_count(const s32 AIdxChn,s32* ACount);

TSAPI(s32)tsfifo_receive_flexray_msgs(const PLIBFlexRay ADataBuffers,const ps32 ADataBufferSize,const s32 AIdxChn,const bool AIncludeTx);

TSAPI(s32)tsfifo_clear_flexray_receive_buffers(const s32 AIdxChn);

TSAPI(s32)tsfifo_read_flexray_buffer_frame_count(const s32 AIdxChn,s32* ACount);

TSAPI(s32)tsfifo_read_flexray_tx_buffer_frame_count(const s32 AIdxChn,s32* ACount);

TSAPI(s32)tsfifo_read_flexray_rx_buffer_frame_count(const s32 AIdxChn,s32* ACount);

TSAPI(s32)tsapp_add_cyclic_msg_can(const PLIBCAN ACAN,const float APeriodMS);

TSAPI(s32)tsapp_update_cyclic_msg_can(const PLIBCAN ACAN);

TSAPI(s32)tsapp_add_cyclic_msg_canfd(const PLIBCANFD ACANFD,const float APeriodMS);

TSAPI(s32)tsapp_delete_cyclic_msg_can(const PLIBCAN ACAN);

TSAPI(s32)tsapp_delete_cyclic_msg_canfd(const PLIBCANFD ACANFD);

TSAPI(s32)tsapp_delete_cyclic_msgs();

TSAPI(s32)tsapp_enable_bus_statistics(const bool AEnable);

TSAPI(s32)tsapp_clear_bus_statistics();

TSAPI(s32)tsapp_get_bus_statistics(const TLIBApplicationChannelType ABusType,const s32 AIdxChn,const TLIBCANBusStatistics AIdxStat,double* AStat);

TSAPI(s32)tsapp_get_fps_can(const s32 AIdxChn,const s32 AIdentifier,s32* AFPS);

TSAPI(s32)tsapp_get_fps_canfd(const s32 AIdxChn,const s32 AIdentifier,s32* AFPS);

TSAPI(s32)tsapp_get_fps_lin(const s32 AIdxChn,const s32 AIdentifier,s32* AFPS);

TSAPI(s32)tsapp_register_event_can(const pnative_int AObj,const TCANQueueEvent_Win32 AEvent);

TSAPI(s32)tsapp_unregister_event_can(const pnative_int AObj,const TCANQueueEvent_Win32 AEvent);

TSAPI(s32)tsapp_register_event_canfd(const pnative_int AObj,const TCANFDQueueEvent_Win32 AEvent);

TSAPI(s32)tsapp_unregister_event_canfd(const pnative_int AObj,const TCANFDQueueEvent_Win32 AEvent);

TSAPI(s32)tsapp_register_event_lin(const pnative_int AObj,const TLINQueueEvent_Win32 AEvent);

TSAPI(s32)tsapp_unregister_event_lin(const pnative_int AObj,const TLINQueueEvent_Win32 AEvent);

TSAPI(s32)tsapp_register_event_flexray(const pnative_int AObj,const TFlexRayQueueEvent_Win32 AEvent);

TSAPI(s32)tsapp_unregister_event_flexray(const pnative_int AObj,const TFlexRayQueueEvent_Win32 AEvent);

TSAPI(s32)tsapp_unregister_events_flexray(const pnative_int AObj);

TSAPI(s32)tsapp_unregister_events_can(const pnative_int AObj);

TSAPI(s32)tsapp_unregister_events_lin(const pnative_int AObj);

TSAPI(s32)tsapp_unregister_events_canfd(const pnative_int AObj);

TSAPI(s32)tsapp_unregister_events_all(const pnative_int AObj);

TSAPI(s32)tsapp_register_pretx_event_can(const pnative_int AObj,const TCANQueueEvent_Win32 AEvent);

TSAPI(s32)tsapp_unregister_pretx_event_can(const pnative_int AObj,const TCANQueueEvent_Win32 AEvent);

TSAPI(s32)tsapp_register_pretx_event_canfd(const pnative_int AObj,const TCANFDQueueEvent_Win32 AEvent);

TSAPI(s32)tsapp_unregister_pretx_event_canfd(const pnative_int AObj,const TCANFDQueueEvent_Win32 AEvent);

TSAPI(s32)tsapp_register_pretx_event_lin(const pnative_int AObj,const TLINQueueEvent_Win32 AEvent);

TSAPI(s32)tsapp_unregister_pretx_event_lin(const pnative_int AObj,const TLINQueueEvent_Win32 AEvent);

TSAPI(s32)tsapp_register_pretx_event_flexray(const pnative_int AObj,const TFlexRayQueueEvent_Win32 AEvent);

TSAPI(s32)tsapp_unregister_pretx_event_flexray(const pnative_int AObj,const TFlexRayQueueEvent_Win32 AEvent);

TSAPI(s32)tsapp_unregister_pretx_events_flexray(const pnative_int AObj);

TSAPI(s32)tsapp_unregister_pretx_events_can(const pnative_int AObj);

TSAPI(s32)tsapp_unregister_pretx_events_lin(const pnative_int AObj);

TSAPI(s32)tsapp_unregister_pretx_events_canfd(const pnative_int AObj);

TSAPI(s32)tsapp_unregister_pretx_events_all(const pnative_int AObj);

TSAPI(s32)tsapp_start_logging(const char* AFileName);

TSAPI(s32)tsapp_stop_logging();

TSAPI(s32)tsapp_excel_load(const char* AFileName,const ppnative_int AObj);

TSAPI(s32)tsapp_excel_get_sheet_count(const pnative_int AObj,s32* ACount);

TSAPI(s32)tsapp_excel_set_sheet_count(const pnative_int AObj,const s32 ACount);

TSAPI(s32)tsapp_excel_get_sheet_name(const pnative_int AObj,const s32 AIdxSheet,const ppchar AName);

TSAPI(s32)tsapp_excel_set_sheet_name(const pnative_int AObj,const s32 AIdxSheet,const char* AName);

TSAPI(s32)tsapp_excel_get_cell_count(const pnative_int AObj,const s32 AIdxSheet,s32* ARowCount,s32* AColCount);

TSAPI(s32)tsapp_excel_get_cell_value(const pnative_int AObj,const s32 AIdxSheet,const s32 AIdxRow,const s32 AIdxCol,const ppchar AValue);

TSAPI(s32)tsapp_excel_set_cell_count(const pnative_int AObj,const s32 AIdxSheet,const s32 ARowCount,const s32 AColCount);

TSAPI(s32)tsapp_excel_set_cell_value(const pnative_int AObj,const s32 AIdxSheet,const s32 AIdxRow,const s32 AIdxCol,const char* AValue);

TSAPI(s32)tsapp_excel_unload(const pnative_int AObj);

TSAPI(s32)tsapp_system_vars_reload_settings();

TSAPI(s32)tsapp_get_system_var_count(const ps32 AinternalCount,const ps32 AUserCount);

TSAPI(s32)tsapp_get_system_var_def_by_index(const bool AIsUser,const s32 AIndex,const PLIBSystemVarDef AVarDef);

TSAPI(s32)tsapp_find_system_var_def_by_name(const bool AIsUser,const char* ACompleteName,const PLIBSystemVarDef AVarDef);

TSAPI(s32)tsapp_get_system_var_double(const char* ACompleteName,const pdouble AValue);

TSAPI(s32)tsapp_get_system_var_int32(const char* ACompleteName,const ps32 AValue);

TSAPI(s32)tsapp_get_system_var_uint32(const char* ACompleteName,const pu32 AValue);

TSAPI(s32)tsapp_get_system_var_int64(const char* ACompleteName,const ps64 AValue);

TSAPI(s32)tsapp_get_system_var_uint64(const char* ACompleteName,const pu64 AValue);

TSAPI(s32)tsapp_get_system_var_uint8_array(const char* ACompleteName,const s32 ACapacity,const ps32 AVarCount,const pu8 AValue);

TSAPI(s32)tsapp_get_system_var_int32_array(const char* ACompleteName,const s32 ACapacity,const ps32 AVarCount,const ps32 AValue);

TSAPI(s32)tsapp_get_system_var_int64_array(const char* ACompleteName,const s32 ACapacity,const ps32 AVarCount,const ps64 AValue);

TSAPI(s32)tsapp_get_system_var_double_array(const char* ACompleteName,const s32 ACapacity,const ps32 AVarCount,const pdouble AValue);

TSAPI(s32)tsapp_get_system_var_string(const char* ACompleteName,const s32 ACapacity,const char* AValue);

TSAPI(s32)tsapp_set_system_var_double(const char* ACompleteName,const double AValue);

TSAPI(s32)tsapp_set_system_var_int32(const char* ACompleteName,const s32 AValue);

TSAPI(s32)tsapp_set_system_var_uint32(const char* ACompleteName,const u32 AValue);

TSAPI(s32)tsapp_set_system_var_int64(const char* ACompleteName,const s64 AValue);

TSAPI(s32)tsapp_set_system_var_uint64(const char* ACompleteName,const u64 AValue);

TSAPI(s32)tsapp_set_system_var_uint8_array(const char* ACompleteName,const s32 ACapacity,const pu8 AValue);

TSAPI(s32)tsapp_set_system_var_int32_array(const char* ACompleteName,const s32 ACapacity,const ps32 AValue);

TSAPI(s32)tsapp_set_system_var_int64_array(const char* ACompleteName,const s32 ACapacity,const ps64 AValue);

TSAPI(s32)tsapp_set_system_var_double_array(const char* ACompleteName,const s32 ACapacity,const pdouble AValue);

TSAPI(s32)tsapp_set_system_var_string(const char* ACompleteName,const char* AValue);

TSAPI(s32)tsapp_log_system_var(const char* ACompleteName);

TSAPI(s32)tsapp_get_system_var_generic(const char* ACompleteName,const s32 ACapacity,const char* AValue);

TSAPI(s32)tsapp_set_system_var_generic(const char* ACompleteName,const char* AValue);

TSAPI(s32)tsapp_get_hardware_id_string(const ppchar AString);

TSAPI(s32)tsapp_get_hardware_id_array(const pu8 AArray8B);

TSAPI(s32)tsapp_create_system_var(const char* ACompleteName,const TLIBSystemVarType AType,const char* ADefaultValue,const char* AComment);

TSAPI(s32)tsapp_delete_system_var(const char* ACompleteName);

TSAPI(s32)tsdb_reload_settings(s32* ALoadedDBCount);

TSAPI(s32)tsdb_save_settings();

TSAPI(s32)tsdb_load_can_db(const char* ADBC,const char* ASupportedChannelsBased0,u32* AId);

TSAPI(s32)tsdb_unload_can_db(const u32 AId);

TSAPI(s32)tsdb_unload_can_dbs();

TSAPI(s32)tsdb_get_can_db_count(s32* ACount);

TSAPI(s32)tsdb_get_can_db_id(const s32 AIndex,u32* AId);

TSAPI(s32)tsdb_get_can_db_info(const u32 ADatabaseId,const s32 AType,const s32 AIndex,const s32 ASubIndex,const ppchar AValue);

TSAPI(s32)tsdb_load_flexray_db(const char* AFRFile,const char* ASupportedChannels,s32* AId);

TSAPI(s32)tsdb_unload_flexray_db(const s32 AId);

TSAPI(s32)tsdb_unload_flexray_dbs();

TSAPI(s32)tsdb_get_flexray_db_count(s32* ACount);

TSAPI(s32)tsdb_get_flexray_db_properties_by_address_verbose(const char* AAddr,s32* ADBIndex,s32* ASignalCount,s32* AFrameCount,s32* AECUCount,s64* ASupportedChannelMask,s64* AFlags,const ppchar AName,const ppchar AComment);

TSAPI(s32)tsdb_get_flexray_db_properties_by_index_verbose(const s32 ADBIndex,s32* ASignalCount,s32* AFrameCount,s32* AECUCount,s64* ASupportedChannelMask,s64* AFlags,const ppchar AName,const ppchar AComment);

TSAPI(s32)tsdb_get_flexray_ecu_properties_by_address_verbose(const char* AAddr,s32* ADBIndex,s32* AECUIndex,s32* ATxFrameCount,s32* ARxFrameCount,const ppchar AName,const ppchar AComment);

TSAPI(s32)tsdb_get_flexray_ecu_properties_by_index_verbose(const s32 ADBIndex,const s32 AECUIndex,s32* ATxFrameCount,s32* ARxFrameCount,const ppchar AName,const ppchar AComment);

TSAPI(s32)tsdb_get_flexray_frame_properties_by_address_verbose(const char* AAddr,s32* ADBIndex,s32* AECUIndex,s32* AFrameIndex,bool* AIsTx,s32* AFRChannelMask,s32* AFRBaseCycle,s32* AFRCycleRepetition,bool* AFRIsStartupFrame,s32* AFRSlotId,s64* AFRCycleMask,s32* ASignalCount,s32* AFRDLC,const ppchar AName,const ppchar AComment);

TSAPI(s32)tsdb_get_flexray_frame_properties_by_index_verbose(const s32 ADBIndex,const s32 AECUIndex,const s32 AFrameIndex,const bool AIsTx,s32* AFRChannelMask,s32* AFRBaseCycle,s32* AFRCycleRepetition,bool* AFRIsStartupFrame,s32* AFRSlotId,s64* AFRCycleMask,s32* ASignalCount,s32* AFRDLC,const ppchar AName,const ppchar AComment);

TSAPI(s32)tsdb_get_flexray_signal_properties_by_address_verbose(const char* AAddr,s32* ADBIndex,s32* AECUIndex,s32* AFrameIndex,s32* ASignalIndex,bool* AIsTx,TSignalType* ASignalType,TFlexRayCompuMethod* ACompuMethod,bool* AIsIntel,s32* AActualStartBit,s32* AActualUpdateBit,s32* ALength,double* AFactor,double* AOffset,double* AInitValue,const ppchar AName,const ppchar AComment);

TSAPI(s32)tsdb_get_flexray_signal_properties_by_index_verbose(const s32 ADBIndex,const s32 AECUIndex,const s32 AFrameIndex,const s32 ASignalIndex,const bool AIsTx,TSignalType* ASignalType,TFlexRayCompuMethod* ACompuMethod,bool* AIsIntel,s32* AActualStartBit,s32* AActualUpdateBit,s32* ALength,double* AFactor,double* AOffset,double* AInitValue,const ppchar AName,const ppchar AComment);

TSAPI(s32)tsdb_get_flexray_db_id(const s32 AIndex,s32* AId);

TSAPI(s32)tsdb_get_can_db_properties_by_index(const PMPDBProperties AValue);

TSAPI(s32)tsdb_get_lin_db_properties_by_index(const PMPDBProperties AValue);

TSAPI(s32)tsdb_get_flexray_db_properties_by_index(const PMPDBProperties AValue);

TSAPI(s32)tsdb_get_can_db_ecu_properties_by_index(const PMPDBECUProperties AValue);

TSAPI(s32)tsdb_get_lin_db_ecu_properties_by_index(const PMPDBECUProperties AValue);

TSAPI(s32)tsdb_get_flexray_db_ecu_properties_by_index(const PMPDBECUProperties AValue);

TSAPI(s32)tsdb_get_can_db_frame_properties_by_index(const PMPDBFrameProperties AValue);

TSAPI(s32)tsdb_get_lin_db_frame_properties_by_index(const PMPDBFrameProperties AValue);

TSAPI(s32)tsdb_get_flexray_db_frame_properties_by_index(const PMPDBFrameProperties AValue);

TSAPI(s32)tsdb_get_can_db_signal_properties_by_index(const PMPDBSignalProperties AValue);

TSAPI(s32)tsdb_get_lin_db_signal_properties_by_index(const PMPDBSignalProperties AValue);

TSAPI(s32)tsdb_get_flexray_db_signal_properties_by_index(const PMPDBSignalProperties AValue);

TSAPI(s32)tsdb_get_can_db_properties_by_address(const char* AAddr,const PMPDBProperties AValue);

TSAPI(s32)tsdb_get_lin_db_properties_by_address(const char* AAddr,const PMPDBProperties AValue);

TSAPI(s32)tsdb_get_flexray_db_properties_by_address(const char* AAddr,const PMPDBProperties AValue);

TSAPI(s32)tsdb_get_can_db_ecu_properties_by_address(const char* AAddr,const PMPDBECUProperties AValue);

TSAPI(s32)tsdb_get_lin_db_ecu_properties_by_address(const char* AAddr,const PMPDBECUProperties AValue);

TSAPI(s32)tsdb_get_flexray_db_ecu_properties_by_address(const char* AAddr,const PMPDBECUProperties AValue);

TSAPI(s32)tsdb_get_can_db_frame_properties_by_address(const char* AAddr,const PMPDBFrameProperties AValue);

TSAPI(s32)tsdb_get_lin_db_frame_properties_by_address(const char* AAddr,const PMPDBFrameProperties AValue);

TSAPI(s32)tsdb_get_flexray_db_frame_properties_by_address(const char* AAddr,const PMPDBFrameProperties AValue);

TSAPI(s32)tsdb_get_can_db_signal_properties_by_address(const char* AAddr,const PMPDBSignalProperties AValue);

TSAPI(s32)tsdb_get_lin_db_signal_properties_by_address(const char* AAddr,const PMPDBSignalProperties AValue);

TSAPI(s32)tsdb_get_flexray_db_signal_properties_by_address(const char* AAddr,const PMPDBSignalProperties AValue);

TSAPI(s32)tsdb_load_lin_db(const char* ALDF,const char* ASupportedChannelsBased0,u32* AId);

TSAPI(s32)tsdb_unload_lin_db(const u32 AId);

TSAPI(s32)tsdb_unload_lin_dbs();

TSAPI(s32)tsdb_get_lin_db_count(s32* ACount);

TSAPI(s32)tsdb_get_lin_db_id(const s32 AIndex,u32* AId);

TSAPI(s32)tsdb_get_can_db_frame_properties_by_db_index(const s32 AIdxDB,const s32 AIndex,const PMPDBFrameProperties AValue);

TSAPI(s32)tsdb_get_lin_db_frame_properties_by_db_index(const s32 AIdxDB,const s32 AIndex,const PMPDBFrameProperties AValue);

TSAPI(s32)tsdb_get_flexray_db_frame_properties_by_db_index(const s32 AIdxDB,const s32 AIndex,const PMPDBFrameProperties AValue);

TSAPI(s32)tsdb_get_can_db_signal_properties_by_frame_index(const s32 AIdxDB,const s32 AIdxFrame,const s32 ASgnIndexInFrame,const PMPDBSignalProperties AValue);

TSAPI(s32)tsdb_get_lin_db_signal_properties_by_frame_index(const s32 AIdxDB,const s32 AIdxFrame,const s32 ASgnIndexInFrame,const PMPDBSignalProperties AValue);

TSAPI(s32)tsdb_get_flexray_db_signal_properties_by_frame_index(const s32 AIdxDB,const s32 AIdxFrame,const s32 ASgnIndexInFrame,const PMPDBSignalProperties AValue);

TSAPI(s32)tsdb_set_signal_value_can(const PLIBCAN ACAN,const char* AMsgName,const char* ASgnName,const double AValue);

TSAPI(s32)tsdb_get_signal_value_can(const PLIBCAN ACAN,const char* AMsgName,const char* ASgnName,double* AValue);

TSAPI(s32)tsdb_set_signal_value_canfd(const PLIBCANFD ACANfd,const char* AMsgName,const char* ASgnName,const double AValue);

TSAPI(s32)tsdb_get_signal_value_canfd(const PLIBCANFD ACANfd,const char* AMsgName,const char* ASgnName,double* AValue);

TSAPI(s32)tslog_reload_settings(s32* ALoadedEngineCount);

TSAPI(s32)tslog_add_online_replay_config(const char* AFileName,s32* AIndex);

TSAPI(s32)tslog_set_online_replay_config(const s32 AIndex,const char* AName,const char* AFileName,const bool AAutoStart,const bool AIsRepetitiveMode,const TLIBOnlineReplayTimingMode AStartTimingMode,const s32 AStartDelayTimeMs,const bool ASendTx,const bool ASendRx,const char* AMappings);

TSAPI(s32)tslog_set_online_replay_config_verbose(const s32 AIndex,const char* AName,const char* AFileName,const bool AAutoStart,const bool AIsRepetitiveMode,const TLIBOnlineReplayTimingMode AStartTimingMode,const s32 AStartDelayTimeMs,const bool ASendTx,const bool ASendRx,const char* AMappings,const bool AForceReplay);

TSAPI(s32)tslog_get_online_replay_count(s32* ACount);

TSAPI(s32)tslog_get_online_replay_config(const s32 AIndex,const ppchar AName,const ppchar AFileName,bool* AAutoStart,bool* AIsRepetitiveMode,TLIBOnlineReplayTimingMode* AStartTimingMode,s32* AStartDelayTimeMs,bool* ASendTx,bool* ASendRx,const ppchar AMappings);

TSAPI(s32)tslog_get_online_replay_config_verbose(const s32 AIndex,const ppchar AName,const ppchar AFileName,bool* AAutoStart,bool* AIsRepetitiveMode,TLIBOnlineReplayTimingMode* AStartTimingMode,s32* AStartDelayTimeMs,bool* ASendTx,bool* ASendRx,const ppchar AMappings,bool* AForceReplay);

TSAPI(s32)tslog_del_online_replay_config(const s32 AIndex);

TSAPI(s32)tslog_del_online_replay_configs();

TSAPI(s32)tslog_start_online_replay(const s32 AIndex);

TSAPI(s32)tslog_start_online_replays();

TSAPI(s32)tslog_pause_online_replay(const s32 AIndex);

TSAPI(s32)tslog_pause_online_replays();

TSAPI(s32)tslog_stop_online_replay(const s32 AIndex);

TSAPI(s32)tslog_stop_online_replays();

TSAPI(s32)tslog_get_online_replay_status(const s32 AIndex,TLIBOnlineReplayStatus* AStatus,float* AProgressPercent100);

TSAPI(s32)tslog_blf_write_start(const char* AFileName,const psize_t AHandle);

TSAPI(s32)tslog_blf_write_set_max_count(const size_t AHandle,const u32 ACount);

TSAPI(s32)tslog_blf_write_can(const size_t AHandle,const PLIBCAN ACAN);

TSAPI(s32)tslog_blf_write_can_fd(const size_t AHandle,const PLIBCANFD ACANFD);

TSAPI(s32)tslog_blf_write_lin(const size_t AHandle,const PLIBLIN ALIN);

TSAPI(s32)tslog_blf_write_realtime_comment(const size_t AHandle,const s64 ATimeUs,const char* AComment);

TSAPI(s32)tslog_blf_write_end(const size_t AHandle);

TSAPI(s32)tslog_blf_read_start(const char* AFileName,const psize_t AHandle,const ps32 AObjCount);

TSAPI(s32)tsLog_blf_read_start_verbose(const char* AFileName,const psize_t AHandle,const ps32 AObjCount,const pu16 AYear,const pu16 AMonth,const pu16 ADayOfWeek,const pu16 ADay,const pu16 AHour,const pu16 AMinute,const pu16 ASecond,const pu16 AMilliseconds);

TSAPI(s32)tslog_blf_read_status(const size_t AHandle,const ps32 AObjReadCount);

TSAPI(s32)tslog_blf_read_object(const size_t AHandle,const ps32 AProgressedCnt,const PSupportedObjType AType,const PLIBCAN ACAN,const PLIBLIN ALIN,const PLIBCANFD ACANFD);

TSAPI(s32)tslog_blf_read_object_w_comment(const size_t AHandle,const ps32 AProgressedCnt,const PSupportedObjType AType,const PLIBCAN ACAN,const PLIBLIN ALIN,const PLIBCANFD ACANFD,const Prealtime_comment_t AComment);

TSAPI(s32)tslog_blf_read_end(const size_t AHandle);

TSAPI(s32)tslog_blf_seek_object_time(const size_t AHandle,const double AProg100,s64* ATime,s32* AProgressedCnt);

TSAPI(s32)tslog_blf_to_asc(const pnative_int AObj,const char* ABLFFileName,const char* AASCFileName,const TReadProgressCallback AProgressCallback);

TSAPI(s32)tslog_asc_to_blf(const pnative_int AObj,const char* AASCFileName,const char* ABLFFileName,const TReadProgressCallback AProgressCallback);

TSAPI(s32)tscom_lin_rbs_reload_settings();

TSAPI(s32)tscom_lin_rbs_start();

TSAPI(s32)tscom_lin_rbs_stop();

TSAPI(s32)tscom_lin_rbs_is_running(bool* AIsRunning);

TSAPI(s32)tscom_lin_rbs_configure(const bool AAutoStart,const bool AAutoSendOnModification,const bool AActivateNodeSimulation,const TLIBRBSInitValueOptions AInitValueOptions);

TSAPI(s32)tscom_lin_rbs_activate_all_networks(const bool AEnable,const bool AIncludingChildren);

TSAPI(s32)tscom_lin_rbs_activate_network_by_name(const s32 AIdxChn,const bool AEnable,const char* ANetworkName,const bool AIncludingChildren);

TSAPI(s32)tscom_lin_rbs_activate_node_by_name(const s32 AIdxChn,const bool AEnable,const char* ANetworkName,const char* ANodeName,const bool AIncludingChildren);

TSAPI(s32)tscom_lin_rbs_activate_message_by_name(const s32 AIdxChn,const bool AEnable,const char* ANetworkName,const char* ANodeName,const char* AMsgName);

TSAPI(s32)tscom_lin_rbs_set_message_delay_time_by_name(const s32 AIdxChn,const s32 AIntervalMs,const char* ANetworkName,const char* ANodeName,const char* AMsgName);

TSAPI(s32)tscom_lin_rbs_get_signal_value_by_element(const s32 AIdxChn,const char* ANetworkName,const char* ANodeName,const char* AMsgName,const char* ASignalName,double* AValue);

TSAPI(s32)tscom_lin_rbs_get_signal_value_by_address(const char* ASymbolAddress,double* AValue);

TSAPI(s32)tscom_lin_rbs_set_signal_value_by_element(const s32 AIdxChn,const char* ANetworkName,const char* ANodeName,const char* AMsgName,const char* ASignalName,const double AValue);

TSAPI(s32)tscom_lin_rbs_set_signal_value_by_address(const char* ASymbolAddress,const double AValue);

TSAPI(s32)tscom_lin_rbs_batch_set_start();

TSAPI(s32)tscom_lin_rbs_batch_set_end();

TSAPI(s32)tscom_lin_rbs_batch_set_signal(const char* AAddr,const double AValue);

TSAPI(s32)tscom_can_rbs_reload_settings();

TSAPI(s32)tscom_can_rbs_start();

TSAPI(s32)tscom_can_rbs_stop();

TSAPI(s32)tscom_can_rbs_is_running(bool* AIsRunning);

TSAPI(s32)tscom_can_rbs_configure(const bool AAutoStart,const bool AAutoSendOnModification,const bool AActivateNodeSimulation,const TLIBRBSInitValueOptions AInitValueOptions);

TSAPI(s32)tscom_can_rbs_activate_all_networks(const bool AEnable,const bool AIncludingChildren);

TSAPI(s32)tscom_can_rbs_activate_network_by_name(const s32 AIdxChn,const bool AEnable,const char* ANetworkName,const bool AIncludingChildren);

TSAPI(s32)tscom_can_rbs_activate_node_by_name(const s32 AIdxChn,const bool AEnable,const char* ANetworkName,const char* ANodeName,const bool AIncludingChildren);

TSAPI(s32)tscom_can_rbs_activate_message_by_name(const s32 AIdxChn,const bool AEnable,const char* ANetworkName,const char* ANodeName,const char* AMsgName);

TSAPI(s32)tscom_can_rbs_set_message_cycle_by_name(const s32 AIdxChn,const s32 AIntervalMs,const char* ANetworkName,const char* ANodeName,const char* AMsgName);

TSAPI(s32)tscom_can_rbs_get_signal_value_by_element(const s32 AIdxChn,const char* ANetworkName,const char* ANodeName,const char* AMsgName,const char* ASignalName,double* AValue);

TSAPI(s32)tscom_can_rbs_get_signal_value_by_address(const char* ASymbolAddress,double* AValue);

TSAPI(s32)tscom_can_rbs_set_signal_value_by_element(const s32 AIdxChn,const char* ANetworkName,const char* ANodeName,const char* AMsgName,const char* ASignalName,const double AValue);

TSAPI(s32)tscom_can_rbs_set_signal_value_by_address(const char* ASymbolAddress,const double AValue);

TSAPI(s32)tscom_can_rbs_batch_set_start();

TSAPI(s32)tscom_can_rbs_batch_set_end();

TSAPI(s32)tscom_can_rbs_batch_set_signal(const char* AAddr,const double AValue);

TSAPI(s32)tscom_flexray_rbs_start();

TSAPI(s32)tscom_flexray_rbs_stop();

TSAPI(s32)tscom_flexray_rbs_is_running(bool* AIsRunning);

TSAPI(s32)tscom_flexray_rbs_configure(const bool AAutoStart,const bool AAutoSendOnModification,const bool AActivateECUSimulation,const TLIBRBSInitValueOptions AInitValueOptions);

TSAPI(s32)tscom_flexray_rbs_activate_all_clusters(const bool AEnable,const bool AIncludingChildren);

TSAPI(s32)tscom_flexray_rbs_activate_cluster_by_name(const s32 AIdxChn,const bool AEnable,const char* AClusterName,const bool AIncludingChildren);

TSAPI(s32)tscom_flexray_rbs_activate_ecu_by_name(const s32 AIdxChn,const bool AEnable,const char* AClusterName,const char* AECUName,const bool AIncludingChildren);

TSAPI(s32)tscom_flexray_rbs_activate_frame_by_name(const s32 AIdxChn,const bool AEnable,const char* AClusterName,const char* AECUName,const char* AFrameName);

TSAPI(s32)tscom_flexray_rbs_get_signal_value_by_element(const s32 AIdxChn,const char* AClusterName,const char* AECUName,const char* AFrameName,const char* ASignalName,double* AValue);

TSAPI(s32)tscom_flexray_rbs_get_signal_value_by_address(const char* ASymbolAddress,double* AValue);

TSAPI(s32)tscom_flexray_rbs_set_signal_value_by_element(const s32 AIdxChn,const char* AClusterName,const char* AECUName,const char* AFrameName,const char* ASignalName,const double AValue);

TSAPI(s32)tscom_flexray_rbs_set_signal_value_by_address(const char* ASymbolAddress,const double AValue);

TSAPI(s32)tscom_flexray_rbs_enable(const bool AEnable);

TSAPI(s32)tscom_flexray_rbs_batch_set_start();

TSAPI(s32)tscom_flexray_rbs_batch_set_end();

TSAPI(s32)tscom_flexray_rbs_batch_set_signal(const char* AAddr,const double AValue);

TSAPI(s32)tscom_flexray_rbs_set_frame_direction(const s32 AIdxChn,const bool AIsTx,const char* AClusterName,const char* AECUName,const char* AFrameName);

TSAPI(s32)tscom_flexray_rbs_set_normal_signal(const char* ASymbolAddress);

TSAPI(s32)tscom_flexray_rbs_set_rc_signal(const char* ASymbolAddress);

TSAPI(s32)tscom_flexray_rbs_set_rc_signal_with_limit(const char* ASymbolAddress,const s32 ALowerLimit,const s32 AUpperLimit);

TSAPI(s32)tscom_flexray_rbs_set_crc_signal(const char* ASymbolAddress,const char* AAlgorithmName,const s32 AIdxByteStart,const s32 AByteCount);

TSAPI(s32)tscom_flexray_set_signal_value_in_raw_frame(const PMPFlexRaySignal AFlexRaySignal,const pu8 AData,const double AValue);

TSAPI(double)tscom_flexray_get_signal_value_in_raw_frame(const PMPFlexRaySignal AFlexRaySignal,const pu8 AData);

TSAPI(s32)tscom_flexray_get_signal_definition(const char* ASignalAddress,const PMPFlexRaySignal ASignalDef);

TSAPI(s32)tsflexray_set_controller_frametrigger(const s32 AIdxChn,const PLIBFlexray_controller_config AControllerConfig,const ps32 AFrameLengthArray,const s32 AFrameNum,const PLIBTrigger_def AFrameTrigger,const s32 AFrameTriggerNum,const s32 ATimeoutMs);

TSAPI(s32)tsflexray_set_controller(const s32 AIdxChn,const PLIBFlexray_controller_config AControllerConfig,const s32 ATimeoutMs);

TSAPI(s32)tsflexray_set_frametrigger(const s32 AIdxChn,const ps32 AFrameLengthArray,const s32 AFrameNum,const PLIBTrigger_def AFrameTrigger,const s32 AFrameTriggerNum,const s32 ATimeoutMs);

TSAPI(s32)tsflexray_cmdreq(const s32 AChnIdx,const s32 AAction,const pu8 AWriteBuffer,const s32 AWriteBufferSize,const pu8 AReadBuffer,const ps32 AReadBufferSize,const s32 ATimeoutMs);

TSAPI(s32)tsflexray_transmit_sync(const s32 AIdxChn,const PLIBFlexRay AData,const s32 ATimeoutMs);

TSAPI(s32)tsflexray_transmit_async(const s32 AIdxChn,const PLIBFlexRay AData);

TSAPI(s32)tsflexray_start_net(const s32 AIdxChn,const s32 ATimeoutMs);

TSAPI(s32)tsflexray_stop_net(const s32 AIdxChn,const s32 ATimeoutMs);

TSAPI(s32)tsflexray_wakeup_pattern(const s32 AIdxChn,const s32 ATimeoutMs);

TSAPI(s32)tsapp_config_ethernet_channel(const s32 AIdxChn,const PLIBEth_CMD_config AConfig,const s32 ATimeoutMs);

TSAPI(s32)tsapp_ethernet_channel_compress_mode(const s32 AIdxChn,const bool AOpen);

TSAPI(s32)tsapp_transmit_ethernet_sync(const PLIBEthernetHeader AEthernetHeader,const s32 ATimeoutMS);

TSAPI(s32)tsapp_transmit_ethernet_async(const PLIBEthernetHeader AEthernetHeader);

TSAPI(s32)tsapp_register_event_ethernet(const pnative_int AObj,const TEthernetQueueEvent_Win32 AEvent);

TSAPI(s32)tsapp_unregister_event_ethernet(const pnative_int AObj,const TEthernetQueueEvent_Win32 AEvent);

TSAPI(s32)tsapp_unregister_events_ethernet(const pnative_int AObj);

TSAPI(s32)tsapp_register_pretx_event_ethernet(const pnative_int AObj,const TEthernetQueueEvent_Win32 AEvent);

TSAPI(s32)tsapp_unregister_pretx_event_ethernet(const pnative_int AObj,const TEthernetQueueEvent_Win32 AEvent);

TSAPI(s32)tsapp_unregister_pretx_events_ethernet(const pnative_int AObj);

TSAPI(s32)tslin_clear_schedule_tables(const s32 AChnIdx);

TSAPI(s32)tslin_switch_runtime_schedule_table(const s32 AChnIdx);

TSAPI(s32)tslin_switch_idle_schedule_table(const s32 AChnIdx);

TSAPI(s32)tslin_switch_normal_schedule_table(const s32 AChnIdx,const s32 ASchIndex);

TSAPI(s32)tslin_stop_lin_channel(const s32 AChnIdx);

TSAPI(s32)tslin_start_lin_channel(const s32 AChnIdx);

TSAPI(s32)tslin_set_node_functiontype(const s32 AChnIdx,const TLINNodeType AFunctionType);

TSAPI(s32)tslin_batch_set_schedule_start(const s32 AChnIdx);

TSAPI(s32)tslin_batch_add_schedule_frame(const s32 AChnIdx,const PLIBLIN ALINData,const s32 ADelayMs);

TSAPI(s32)tslin_batch_set_schedule_end(const s32 AChnIdx);

TSAPI(s32)tstp_lin_master_request(const s32 AChnIdx,const u8 ANAD,const pu8 AData,const s32 ADataNum,const s32 ATimeoutMs);

TSAPI(s32)tstp_lin_master_request_intervalms(const s32 AChnIdx,const u16 AData);

TSAPI(s32)tstp_lin_reset(const s32 AChnIdx);

TSAPI(s32)tstp_lin_slave_response_intervalms(const s32 AChnIdx,const u16 AData);

TSAPI(s32)tstp_lin_tp_para_default(const s32 AChnIdx,const u16 AReqIntervalMs,const u16 AResIntervalMs,const u16 AResRetryTime);

TSAPI(s32)tstp_lin_tp_para_special(const s32 AChnIdx,const u16 AReqIntervalMs,const u16 AResIntervalMs,const u16 AResRetryTime);

TSAPI(s32)tsdiag_lin_read_data_by_identifier(const s32 AChnIdx,const u8 ANAD,const u16 AId,const pu8 AResNAD,const pu8 AResData,const psize_t AResDataNum,const s32 ATimeoutMS);

TSAPI(size_t)tsdiag_lin_write_data_by_identifier(const s32 AChnIdx,const u8 AReqNAD,const u16 AID,const pu8 AReqData,const size_t AReqDataNum,const pu8 AResNAD,const pu8 AResData,const psize_t AResDataNum,const s32 ATimeoutMS);

TSAPI(size_t)tsdiag_lin_session_control(const s32 AChnIdx,const u8 ANAD,const u8 ANewSession,const s32 ATimeoutMS);

TSAPI(size_t)tsdiag_lin_fault_memory_read(const s32 AChnIdx,const u8 ANAD,const s32 ATimeoutMS);

TSAPI(size_t)tsdiag_lin_fault_memory_clear(const s32 AChnIdx,const u8 ANAD,const s32 ATimeoutMS);

TSAPI(s32)tsdiag_can_create(const ps32 pDiagModuleIndex,const s32 AChnIndex,const u8 ASupportFDCAN,const u8 AMaxDLC,const u32 ARequestID,const bool ARequestIDIsStd,const u32 AResponseID,const bool AResponseIDIsStd,const u32 AFunctionID,const bool AFunctionIDIsStd);

TSAPI(s32)tsdiag_can_delete(const s32 ADiagModuleIndex);

TSAPI(s32)tsdiag_doip_create(const ps32 pDiagModuleIndex,const s32 AToolType,const u32 AChnIndex,const char* ATesterIP,const u16 ATesterPort,const char* ADUTIP,const u16 ADUTPort,const u32 ARequestID,const u32 AResponseID,const u32 AFunctionID);

TSAPI(s32)tsdiag_doip_connect(const s32 ADiagModuleIndex);

TSAPI(s32)tsdiag_doip_routing_activation(const s32 ADiagModuleIndex,const u8 AActivateType,const bool ASendOEMSpecificData,const u32 AOEMSpecificData);

TSAPI(s32)tsdiag_doip_disconnect(const s32 ADiagModuleIndex);

TSAPI(s32)tsdiag_lin_create(const ps32 pDiagModuleIndex,const u32 AChnIndex,const u8 ANad);

TSAPI(s32)tstp_lin_set_run_with_normal_schedule_table(const s32 ADiagModuleIndex,const bool ADiagRunWithNormalScheduleTable);

TSAPI(s32)tsdiag_lin_set_nad(const s32 ADiagModuleIndex,const u8 ANAD);

TSAPI(s32)tsdiag_set_channel(const s32 ADiagModuleIndex,const s32 AChnIndex);

TSAPI(s32)tsdiag_set_fdmode(const s32 ADiagModuleIndex,const bool AFDMode,const bool ASupportBRS,const s32 AMaxLength);

TSAPI(s32)tsdiag_set_request_id(const s32 ADiagModuleIndex,const s32 ARequestID,const bool AIsStandard);

TSAPI(s32)tsdiag_set_response_id(const s32 ADiagModuleIndex,const s32 ARequestID,const bool AIsStandard);

TSAPI(s32)tsdiag_set_function_id(const s32 ADiagModuleIndex,const s32 ARequestID,const bool AIsStandard);

TSAPI(s32)tsdiag_set_stmin(const s32 ADiagModuleIndex,const float ASTMin);

TSAPI(s32)tsdiag_set_tx_stmin(const s32 ADiagModuleIndex,const bool ATxSTMinUserDefined,const float ATxSTMin);

TSAPI(s32)tsdiag_set_blocksize(const s32 ADiagModuleIndex,const s32 ABlockSize);

TSAPI(s32)tsdiag_set_maxlength(const s32 ADiagModuleIndex,const s32 AMaxLength);

TSAPI(s32)tsdiag_set_n_wft_max(const s32 ADiagModuleIndex,const u8 AValue);

TSAPI(s32)tsdiag_set_fcdelay_verbose(const s32 ADiagModuleIndex,const bool ATxSTMinUserDefined,const float ATxSTMin);

TSAPI(s32)tsdiag_set_at_least_8bytes(const s32 ADiagModuleIndex,const s32 AIs8Bytes);

TSAPI(s32)tsdiag_set_fcdelay(const s32 ADiagModuleIndex,const float AFCDelay);

TSAPI(s32)tsdiag_set_filled_byte(const s32 ADiagModuleIndex,const u8 AFilledByte);

TSAPI(s32)tsdiag_set_p2_timeout(const s32 ADiagModuleIndex,const s32 ATimeMs);

TSAPI(s32)tsdiag_set_p2_extended(const s32 ADiagModuleIndex,const s32 ATimeMs);

TSAPI(s32)tsdiag_set_s3_servertime(const s32 ADiagModuleIndex,const s32 ATimeMs);

TSAPI(s32)tsdiag_set_s3_clienttime(const s32 ADiagModuleIndex,const s32 ATimeMs);

TSAPI(s32)tsdiag_testerpresent_start(const s32 ADiagModuleIndex);

TSAPI(s32)tsdiag_testerpresent_stop(const s32 ADiagModuleIndex);

TSAPI(s32)tsdiag_testerpreset_checkState(const s32 ADiagModuleIndex,const pbool AStartState);

TSAPI(s32)tsdiag_testerpresent_update_para(const s32 ADiagModuleIndex,const s32 AIsFunctional,const pu8 AReqData,const s32 AReqDataSize,const s32 AIntervalTimeMs);

TSAPI(s32)tstp_send_functional(const s32 ADiagModuleIndex,const pu8 AReqDataArray,const s32 AReqDataSize);

TSAPI(s32)tstp_send_request(const s32 ADiagModuleIndex,const pu8 AReqDataArray,const s32 AReqDataSize);

TSAPI(s32)tstp_request_and_get_response(const s32 ADiagModuleIndex,const pu8 AReqDataArray,const s32 AReqDataSize,const pu8 AResponseDataArray,const ps32 AResponseDataSize);

TSAPI(s32)tstp_request_and_get_response_functional(const s32 ADiagModuleIndex,const pu8 AReqDataArray,const s32 AReqDataSize,const pu8 AResponseDataArray,const ps32 AResponseDataSize);

TSAPI(s32)tsdiag_delete(const s32 ADiagModuleIndex);

TSAPI(s32)tsdiag_session_control(const s32 ADiagModuleIndex,const u8 ASubSession);

TSAPI(s32)tsdiag_routine_control(const s32 ADiagModuleIndex,const u8 ARoutineControlType,const u16 ARoutintID);

TSAPI(s32)tsdiag_communication_control(const s32 ADiagModuleIndex,const u8 AControlType);

TSAPI(s32)tsdiag_security_access_request_seed(const s32 ADiagModuleIndex,const s32 ALevel,const pu8 ARecSeed,const ps32 ARecSeedSize);

TSAPI(s32)tsdiag_security_access_send_key(const s32 ADiagModuleIndex,const s32 ALevel,const pu8 AKeyValue,const s32 AKeySize);

TSAPI(s32)tsdiag_request_download(const s32 ADiagModuleIndex,const u32 AMemAddr,const u32 AMemSize);

TSAPI(s32)tsdiag_request_upload(const s32 ADiagModuleIndex,const u32 AMemAddr,const u32 AMemSize);

TSAPI(s32)tsdiag_transfer_data(const s32 ADiagModuleIndex,const pu8 ASourceDatas,const s32 ADataSize,const s32 AReqCase);

TSAPI(s32)tsdiag_request_transfer_exit(const s32 ADiagModuleIndex);

TSAPI(s32)tsdiag_write_data_by_identifier(const s32 ADiagModuleIndex,const u16 ADataIdentifier,const pu8 AWriteData,const s32 AWriteDataSize);

TSAPI(s32)tsdiag_read_data_by_identifier(const s32 ADiagModuleIndex,const u16 ADataIdentifier,const pu8 AReturnArray,const ps32 AReturnArraySize);

TSAPI(s32)tstp_can_send_functional(const s32 ADiagModuleIndex,const pu8 AReqDataArray,const s32 AReqDataSize);

TSAPI(s32)tstp_can_send_request(const s32 ADiagModuleIndex,const pu8 AReqDataArray,const s32 AReqDataSize);

TSAPI(s32)tstp_can_request_and_get_response(const s32 ADiagModuleIndex,const pu8 AReqDataArray,const s32 AReqDataSize,const pu8 AResponseDataArray,const ps32 AResponseDataSize);

TSAPI(s32)tstp_can_request_and_get_response_functional(const s32 ADiagModuleIndex,const pu8 AReqDataArray,const s32 AReqDataSize,const pu8 AResponseDataArray,const ps32 AResponseDataSize);

TSAPI(s32)tstp_can_register_tx_completed_recall(const s32 ADiagModuleIndex,const N_USData_TranslateCompleted_Recall ATxcompleted);

TSAPI(s32)tstp_can_register_rx_completed_recall(const s32 ADiagModuleIndex,const N_USData_TranslateCompleted_Recall ARxcompleted);

TSAPI(s32)tsdiag_can_session_control(const s32 ADiagModuleIndex,const u8 ASubSession);

TSAPI(s32)tsdiag_can_routine_control(const s32 ADiagModuleIndex,const u8 ARoutineControlType,const u16 ARoutintID);

TSAPI(s32)tsdiag_can_communication_control(const s32 ADiagModuleIndex,const u8 AControlType);

TSAPI(s32)tsdiag_can_security_access_request_seed(const s32 ADiagModuleIndex,const s32 ALevel,const pu8 ARecSeed,const ps32 ARecSeedSize);

TSAPI(s32)tsdiag_can_security_access_send_key(const s32 ADiagModuleIndex,const s32 ALevel,const pu8 AKeyValue,const s32 AKeySize);

TSAPI(s32)tsdiag_can_request_download(const s32 ADiagModuleIndex,const u32 AMemAddr,const u32 AMemSize);

TSAPI(s32)tsdiag_can_request_upload(const s32 ADiagModuleIndex,const u32 AMemAddr,const u32 AMemSize);

TSAPI(s32)tsdiag_can_transfer_data(const s32 ADiagModuleIndex,const pu8 ASourceDatas,const s32 ADataSize,const s32 AReqCase);

TSAPI(s32)tsdiag_can_request_transfer_exit(const s32 ADiagModuleIndex);

TSAPI(s32)tsdiag_can_write_data_by_identifier(const s32 ADiagModuleIndex,const u16 ADataIdentifier,const pu8 AWriteData,const s32 AWriteDataSize);

TSAPI(s32)tsdiag_can_read_data_by_identifier(const s32 ADiagModuleIndex,const u16 ADataIdentifier,const pu8 AReturnArray,const ps32 AReturnArraySize);

TSAPI(s32)tstp_can_register_tx_completed_recall_internal(const s32 ADiagModuleIndex,const N_USData_TranslateCompleted_Recall_Obj ATxcompleted);

TSAPI(s32)tstp_can_register_rx_completed_recall_internal(const s32 ADiagModuleIndex,const N_USData_TranslateCompleted_Recall_Obj ARxcompleted);

TSAPI(s32)tslog_logger_delete_file(const s32 AChnIdx,const s32 AFileIndex,const s32 ATimeoutMS);

TSAPI(s32)tslog_logger_start_export_blf_file(const s32 AChnIdx,const s32 AFileIndex,const char* ABlfFileName,const u64 AStartTimeUs,const s32 AMaxSize,const pdouble AProgress,const u16 AYear,const u16  AMonth,const u16  ADay,const u16  AHour,const u16  AMinute,const u16  ASecond,const u16  AMinisecond,const s32 ATimeoutMS);

TSAPI(s32)tslog_logger_abort_export_blf_file(const s32 AChnIdx,const s32 ATimeoutMS);

TSAPI(s32)tslog_logger_start_online_replay(const s32 AChnIdx,const s32 AFileIndex,const u64 AStartTimeUs,const s32 AMaxSize,const s32 ATimeoutMS);

TSAPI(s32)tslog_logger_start_offline_replay(const s32 AChnIdx,const s32 AFileIndex,const u64 AStartTimeUs,const s32 AMaxSize,const s32 ATimeoutMS);

TSAPI(s32)tslog_logger_stop_replay(const s32 AChnIdx,const s32 ATimeoutMS);

TSAPI(s32)tslog_logger_set_logger_mode(const s32 AChnIdx,const u8 AMode,const s32 ATimeoutMS);

TSAPI(s32)tsapp_logger_enable_gps_module(const s32 AChnIdx,const s32 AEnable,const s32 ATimeoutMS);

TSAPI(s32)tsapp_reset_gps_module(const s32 AChnIdx,const s32 AInitBaudrate,const s32 ATargetBaudrate,const s32 ASampleRate,const s32 ATimeoutMS);

TSAPI(s32)tsapp_unlock_camera_channel(const s32 AChnIdx);

TSAPI(u16)rawsocket_htons(const u16 x);

TSAPI(u32)rawsocket_htonl(const u32 x);

TSAPI(s32)rawsocket_aton(const char* cp,const Pip4_addr_t addr);

TSAPI(char*)rawsocket_ntoa(const Pip4_addr_t addr);

TSAPI(s32)rawsocket_aton6(const char* cp,const Pip6_addr_t addr);

TSAPI(char*)rawsocket_ntoa6(const Pip6_addr_t addr);

TSAPI(char*)rawsocket_inet_ntop(const s32 af,const pnative_int src,const char* dst,const u32 size);

TSAPI(s32)rawsocket_inet_pton(const s32 af,const char* src,const pnative_int dst);

TSAPI(s32)tssocket_initialize(const s32 ANetworkIndex);

TSAPI(s32)tssocket_initialize_verbose(const s32 ANetworkIndex,const TLogDebuggingInfo_t ALog,const bool AActiveDelayACK);

TSAPI(s32)tssocket_finalize(const s32 ANetworkIndex);

TSAPI(s32)tssocket_add_device(const s32 ANetworkIndex,const pu8 macaddr,const pu16 vLan,const Tip4_addr_t ipaddr,const Tip4_addr_t netmask,const Tip4_addr_t gateway,const u16 mtu);

TSAPI(s32)tssocket_remove_device(const s32 ANetworkIndex,const pu8 macaddr,const pu16 vLan,const Pip4_addr_t ipaddr);

TSAPI(s32)tssocket_add_device_ex(const s32 ANetworkIndex,const char* macaddr,const char* vlan,const char* ipaddr,const char* netmask,const char* gateway,const u16 mtu);

TSAPI(s32)tssocket_remove_device_ex(const s32 ANetworkIndex,const char* mac,const char* vlan,const char* ipaddr);

TSAPI(s32)rawsocket_get_errno(const s32 ANetworkIndex);

TSAPI(s32)rawsocket_dhcp_start(const s32 ANetworkIndex);

TSAPI(s32)rawsocket_select(const s32 ANetworkIndex,const s32 maxfdp1,const Pts_fd_set readset,const Pts_fd_set writeset,const Pts_fd_set exceptset,const Pts_timeval timeout);

TSAPI(s32)rawsocket_poll(const s32 ANetworkIndex,const Pts_pollfd fds,const size_t nfds,const s32 timeout);

TSAPI(s32)tssocket_getaddrinfo(const s32 ANetworkIndex,const char* nodename,const char* servname,const Pts_addrinfo hints,const PPts_addrinfo res);

TSAPI(s32)tssocket_freeaddrinfo(const s32 ANetworkIndex,const Pts_addrinfo ai);

TSAPI(s32)tssocket_gethostname(const s32 ANetworkIndex,const char* name,const PPts_hostent AHostent);

TSAPI(s32)tssocket_getalldevices(const s32 ANetworkIndex,const PPts_net_device devs);

TSAPI(s32)tssocket_freedevices(const s32 ANetworkIndex,const Pts_net_device devs);

TSAPI(s32)rawsocket(const s32 ANetworkIndex,const s32 domain,const s32 atype,const s32 protocol,const tosun_recv_callback recv_cb,const tosun_tcp_presend_callback presend_cb,const tosun_tcp_ack_callback send_cb);

TSAPI(s32)rawsocket_accept(const s32 s,const Pts_sockaddr addr,const pu32 addrlen);

TSAPI(s32)rawsocket_bind(const s32 s,const Pts_sockaddr name,const u32 namelen);

TSAPI(s32)rawsocket_shutdown(const s32 s,const s32 how);

TSAPI(s32)rawsocket_getpeername(const s32 s,const Pts_sockaddr name,const pu32 namelen);

TSAPI(s32)rawsocket_getsockname(const s32 s,const Pts_sockaddr name,const pu32 namelen);

TSAPI(s32)rawsocket_getsockopt(const s32 s,const s32 level,const s32 optname,const pnative_int optval,const pu32 optlen);

TSAPI(s32)rawsocket_setsockopt(const s32 s,const s32 level,const s32 optname,const pnative_int optval,const u32 optlen);

TSAPI(s32)rawsocket_close(const s32 s);

TSAPI(s32)rawsocket_close_v2(const s32 s,const s32 AForceExitTimeWait);

TSAPI(s32)rawsocket_connect(const s32 s,const Pts_sockaddr name,const u32 namelen);

TSAPI(s32)rawsocket_listen(const s32 s,const s32 backlog);

TSAPI(size_t)rawsocket_recv(const s32 s,const pnative_int mem,const size_t len,const s32 flags);

TSAPI(size_t)rawsocket_read(const s32 s,const pnative_int mem,const size_t len);

TSAPI(size_t)rawsocket_readv(const s32 s,const Pts_iovec iov,const s32 iovcnt);

TSAPI(size_t)rawsocket_recvfrom(const s32 s,const pnative_int mem,const size_t len,const s32 flags,const Pts_sockaddr from,const pu32 fromlen);

TSAPI(size_t)rawsocket_recvmsg(const s32 s,const Pts_msghdr Amessage,const s32 flags);

TSAPI(size_t)rawsocket_send(const s32 s,const pnative_int dataptr,const size_t size,const s32 flags);

TSAPI(size_t)rawsocket_sendmsg(const s32 s,const Pts_msghdr Amessage,const s32 flags);

TSAPI(size_t)rawsocket_sendto(const s32 s,const pnative_int dataptr,const size_t size,const s32 flags,const Pts_sockaddr ato,const u32 tolen);

TSAPI(size_t)rawsocket_write(const s32 s,const pnative_int dataptr,const size_t size);

TSAPI(size_t)rawsocket_writev(const s32 s,const Pts_iovec iov,const s32 iovcnt);

TSAPI(s32)rawsocket_ioctl(const s32 s,const long cmd,const pnative_int argp);

TSAPI(s32)rawsocket_fcntl(const s32 s,const s32 cmd,const s32 val);

TSAPI(s32)tssocket_tcp(const s32 ANetworkIndex,const char* AIPEndPoint,const ps32 ASocketHandle);

TSAPI(s32)tssocket_tcp_start_listen(const s32 s);

TSAPI(s32)tssocket_tcp_start_receive(const s32 s);

TSAPI(s32)tssocket_tcp_connect(const s32 s,const char* AIPEndPoint);

TSAPI(s32)tssocket_tcp_close(const s32 s);

TSAPI(s32)tssocket_tcp_close_v2(const s32 s,const s32 AForceExitTimeWait);

TSAPI(s32)tssocket_tcp_send(const s32 s,const pu8 AData,const s32 ASize);

TSAPI(s32)tssocket_tcp_send_sync(const s32 s,const pu8 AData,const s32 ASize);

TSAPI(s32)tssocket_tcp_send_async(const s32 s,const pu8 AData,const s32 ASize);

TSAPI(s32)tssocket_tcp_sendto_client(const s32 s,const char* AIPEndPoint,const pu8 AData,const s32 ASize);

TSAPI(s32)tssocket_udp(const s32 ANetworkIndex,const char* AIPEndPoint,const ps32 ASocketHandle);

TSAPI(s32)tssocket_udp_start_receive(const s32 s);

TSAPI(s32)tssocket_udp_close(const s32 s);

TSAPI(s32)tssocket_udp_sendto(const s32 s,const char* AIPEndPoint,const pu8 AData,const s32 ASize);

TSAPI(s32)tssocket_udp_sendto_v2(const s32 s,const u32 AIPAddress,const u16 APort,const pu8 AData,const s32 ASize);

TSAPI(s32)tssocket_register_tcp_listen_event(const s32 s,const TSSocketListenEvent_Win32 AEvent);

TSAPI(s32)tssocket_unregister_tcp_listen_event(const s32 s,const TSSocketListenEvent_Win32 AEvent);

TSAPI(s32)tssocket_unregister_tcp_listen_events(const s32 s);

TSAPI(s32)tssocket_register_tcp_connect_event(const s32 s,const TSSocketNotifyEvent_Win32 AEvent);

TSAPI(s32)tssocket_unregister_tcp_connect_event(const s32 s,const TSSocketNotifyEvent_Win32 AEvent);

TSAPI(s32)tssocket_unregister_tcp_connect_events(const s32 s);

TSAPI(s32)tssocket_register_tcp_receive_event(const s32 s,const TSSocketReceiveEvent_Win32 AEvent);

TSAPI(s32)tssocket_unregister_tcp_receive_event(const s32 s,const TSSocketReceiveEvent_Win32 AEvent);

TSAPI(s32)tssocket_unregister_tcp_receive_events(const s32 s);

TSAPI(s32)tssocket_register_tcp_close_event(const s32 s,const TSSocketNotifyEvent_Win32 AEvent);

TSAPI(s32)tssocket_unregister_tcp_close_event(const s32 s,const TSSocketNotifyEvent_Win32 AEvent);

TSAPI(s32)tssocket_unregister_tcp_close_events(const s32 s);

TSAPI(s32)tssocket_register_tcp_send_event(const s32 s,const TSSocketTransmitEvent_Win32 AEvent);

TSAPI(s32)tssocket_unregister_tcp_send_event(const s32 s,const TSSocketTransmitEvent_Win32 AEvent);

TSAPI(s32)tssocket_unregister_tcp_send_events(const s32 s);

TSAPI(s32)tssocket_register_udp_receivefrom_event(const s32 s,const TSSocketReceiveEvent_Win32 AEvent);

TSAPI(s32)tssocket_unregister_udp_receivefrom_event(const s32 s,const TSSocketReceiveEvent_Win32 AEvent);

TSAPI(s32)tssocket_unregister_udp_receivefrom_events(const s32 s);

TSAPI(s32)tssocket_register_udp_sendto_event(const s32 s,const TSSocketTransmitEvent_Win32 AEvent);

TSAPI(s32)tssocket_unregister_udp_sendto_event(const s32 s,const TSSocketTransmitEvent_Win32 AEvent);

TSAPI(s32)tssocket_unregister_udp_sendto_events(const s32 s);

TSAPI(s32)tssocket_register_udp_receivefrom_eventv2(const s32 s,const TSSocketReceiveEventV2_Win32 AEvent);

TSAPI(s32)tssocket_unregister_udp_receivefrom_eventv2(const s32 s,const TSSocketReceiveEventV2_Win32 AEvent);

TSAPI(s32)tssocket_unregister_udp_receivefrom_eventsv2(const s32 s);

TSAPI(s32)tssocket_register_udp_receivefrom_eventv3(const s32 s,const TSSocketReceiveEventV3_Win32 AEvent);

TSAPI(s32)tssocket_unregister_udp_receivefrom_eventv3(const s32 s,const TSSocketReceiveEventV3_Win32 AEvent);

TSAPI(s32)tssocket_unregister_udp_receivefrom_eventsv3(const s32 s);

TSAPI(s32)tssocket_register_tcp_receive_eventv2(const s32 s,const TSSocketReceiveEventV2_Win32 AEvent);

TSAPI(s32)tssocket_unregister_tcp_receive_eventv2(const s32 s,const TSSocketReceiveEventV2_Win32 AEvent);

TSAPI(s32)tssocket_unregister_tcp_receive_eventsv2(const s32 s);

TSAPI(s32)tsmp_reload_settings();

TSAPI(s32)tsmp_load(const char* AMPFileName,const bool ARunAfterLoad);

TSAPI(s32)tsmp_unload(const char* AMPFileName);

TSAPI(s32)tsmp_unload_all();

TSAPI(s32)tsmp_run(const char* AMPFileName);

TSAPI(s32)tsmp_is_running(const char* AMPFileName,bool* AIsRunning);

TSAPI(s32)tsmp_stop(const char* AMPFileName);

TSAPI(s32)tsmp_run_all();

TSAPI(s32)tsmp_stop_all();

TSAPI(s32)tsmp_call_function(const char* AGroupName,const char* AFuncName,const char* AInParameters,const ppchar AOutParameters);

TSAPI(s32)tsmp_get_function_prototype(const char* AGroupName,const char* AFuncName,const ppchar APrototype);

TSAPI(s32)tsmp_get_mp_function_list(const char* AGroupName,const ppchar AList);

TSAPI(s32)tsmp_get_mp_list(const ppchar AList);

TSAPI(s32)db_get_flexray_cluster_parameters(const s32 AIdxChn,const char* AClusterName,const PLIBFlexRayClusterParameters AValue);

TSAPI(s32)db_get_flexray_controller_parameters(const s32 AIdxChn,const char* AClusterName,const char* AECUName,const PLIBFlexRayControllerParameters AValue);

TSAPI(s32)set_system_var_event_support(const char* ACompleteName,const bool ASupport);

TSAPI(s32)get_system_var_event_support(const char* ACompleteName,const pbool ASupport);

TSAPI(s32)get_date_time(const ps32 AYear,const ps32 AMonth,const ps32 ADay,const ps32 AHour,const ps32 AMinute,const ps32 ASecond,const ps32 AMilliseconds);

TSAPI(s32)tslog_disable_online_replay_filter(const s32 AIndex);

TSAPI(s32)tslog_set_online_replay_filter(const s32 AIndex,const bool AIsPassFilter,const s32 ACount,const ps32 AIdxChannels,const ps32 AIdentifiers);

TSAPI(s32)set_can_signal_raw_value(const PMPCANSignal ACANSignal,const pu8 AData,const u64 AValue);

TSAPI(u64)get_can_signal_raw_value(const PMPCANSignal ACANSignal,const pu8 AData);

TSAPI(s32)set_lin_signal_raw_value(const PMPLINSignal ALINSignal,const pu8 AData,const u64 AValue);

TSAPI(u64)get_lin_signal_raw_value(const PMPLINSignal ALINSignal,const pu8 AData);

TSAPI(s32)set_flexray_signal_raw_value(const PMPFlexRaySignal AFlexRaySignal,const pu8 AData,const u64 AValue);

TSAPI(u64)get_flexray_signal_raw_value(const PMPFlexRaySignal AFlexRaySignal,const pu8 AData);

TSAPI(s32)gpg_delete_all_modules();

TSAPI(s32)gpg_create_module(const char* AProgramName,const char* ADisplayName,const ps64 AModuleId,const ps64 AEntryPointId);

TSAPI(s32)gpg_delete_module(const s64 AModuleId);

TSAPI(s32)gpg_deploy_module(const s64 AModuleId,const char* AGraphicProgramWindowTitle);

TSAPI(s32)gpg_add_action_down(const s64 AModuleId,const s64 AUpperActionId,const char* ADisplayName,const char* AComment,const ps64 AActionId);

TSAPI(s32)gpg_add_action_right(const s64 AModuleId,const s64 ALeftActionId,const char* ADisplayName,const char* AComment,const ps64 AActionId);

TSAPI(s32)gpg_add_goto_down(const s64 AModuleId,const s64 AUpperActionId,const char* ADisplayName,const char* AComment,const char* AJumpLabel,const ps64 AActionId);

TSAPI(s32)gpg_add_goto_right(const s64 AModuleId,const s64 ALeftActionId,const char* ADisplayName,const char* AComment,const char* AJumpLabel,const ps64 AActionId);

TSAPI(s32)gpg_add_from_down(const s64 AModuleId,const s64 AUpperActionId,const char* ADisplayName,const char* AComment,const char* AJumpLabel,const ps64 AActionId);

TSAPI(s32)gpg_add_group_down(const s64 AModuleId,const s64 AUpperActionId,const char* ADisplayName,const char* AComment,const ps64 AGroupId,const ps64 AEntryPointId);

TSAPI(s32)gpg_add_group_right(const s64 AModuleId,const s64 ALeftActionId,const char* ADisplayName,const char* AComment,const ps64 AGroupId,const ps64 AEntryPointId);

TSAPI(s32)gpg_delete_action(const s64 AModuleId,const s64 AActionId);

TSAPI(s32)gpg_set_action_nop(const s64 AModuleId,const s64 AActionId);

TSAPI(s32)gpg_set_action_signal_read_write(const s64 AModuleId,const s64 AActionId);

TSAPI(s32)gpg_set_action_api_call(const s64 AModuleId,const s64 AActionId);

TSAPI(s32)gpg_set_action_expression(const s64 AModuleId,const s64 AActionId);

TSAPI(s32)gpg_configure_action_basic(const s64 AModuleId,const s64 AActionId,const char* ADisplayName,const char* AComment,const s32 ATimeoutMs);

TSAPI(s32)gpg_configure_goto(const s64 AModuleId,const s64 AActionId,const char* ADisplayName,const char* AComment,const char* AJumpLabel);

TSAPI(s32)gpg_configure_from(const s64 AModuleId,const s64 AActionId,const char* ADisplayName,const char* AComment,const char* AJumpLabel);

TSAPI(s32)gpg_configure_nop(const s64 AModuleId,const s64 AActionId,const bool ANextDirectionIsDown,const bool AResultOK,const bool AJumpBackIfEnded);

TSAPI(s32)gpg_configure_group(const s64 AModuleId,const s64 AActionId,const TLIBAutomationSignalType ARepeatCountType,const char* ARepeatCountRepr);

TSAPI(s32)gpg_configure_signal_read_write_list_clear(const s64 AModuleId,const s64 AActionId);

TSAPI(s32)gpg_configure_signal_write_list_append(const s64 AModuleId,const s64 AActionId,const TLIBAutomationSignalType ADestSignalType,const TLIBAutomationSignalType ASrcSignalType,const char* ADestSignalExpr,const char* ASrcSignalExpr,const ps32 AItemIndex);

TSAPI(s32)gpg_configure_signal_read_list_append(const s64 AModuleId,const s64 AActionId,const bool AIsConditionAND,const TLIBAutomationSignalType ADestSignalType,const TLIBAutomationSignalType AMinSignalType,const TLIBAutomationSignalType AMaxSignalType,const char* ADestSignalExpr,const char* AMinSignalExpr,const char* AMaxSignalExpr,const ps32 AItemIndex);

TSAPI(s32)gpg_configure_api_call_arguments(const s64 AModuleId,const s64 AActionId,const TLIBMPFuncSource AAPIType,const char* AAPIName,const PLIBAutomationSignalType AAPIArgTypes,const ppchar AAPIArgNames,const ppchar AAPIArgExprs,const s32 AArraySize);

TSAPI(s32)gpg_configure_api_call_result(const s64 AModuleId,const s64 AActionId,const bool AIgnoreResult,const TLIBAutomationSignalType ASignalType,const char* ASignalExpr);

TSAPI(s32)gpg_configure_expression(const s64 AModuleId,const s64 AActionId,const s32 AxCount,const char* AExpression,const PLIBAutomationSignalType AArgumentTypes,const ppchar AArgumentExprs,const TLIBAutomationSignalType AResultType,const char* AResultExpr);

TSAPI(s32)gpg_add_local_var(const s64 AModuleId,const TLIBSimVarType AType,const char* AName,const char* AInitValue,const char* AComment,const ps32 AItemIndex);

TSAPI(s32)gpg_delete_local_var(const s64 AModuleId,const s32 AItemIndex);

TSAPI(s32)gpg_delete_all_local_vars(const s64 AModuleId);

TSAPI(s32)gpg_delete_group_items(const s64 AModuleId,const s64 AGroupId);

TSAPI(s32)gpg_configure_signal_read_write_list_delete(const s64 AModuleId,const s64 AActionId,const s32 AItemIndex);

TSAPI(s32)flexray_rbs_update_frame_by_header(const PLIBFlexRay AFlexRay);

TSAPI(s32)gpg_configure_module(const s64 AModuleId,const char* AProgramName,const char* ADisplayName,const s32 ARepeatCount,const bool ASelected);

TSAPI(s32)add_path_to_environment(const char* APath);

TSAPI(s32)delete_path_from_environment(const char* APath);

TSAPI(s32)set_system_var_double_w_time(const char* ACompleteName,const double AValue,const s64 ATimeUs);

TSAPI(s32)set_system_var_int32_w_time(const char* ACompleteName,const s32 AValue,const s64 ATimeUs);

TSAPI(s32)set_system_var_uint32_w_time(const char* ACompleteName,const u32 AValue,const s64 ATimeUs);

TSAPI(s32)set_system_var_int64_w_time(const char* ACompleteName,const s64 AValue,const s64 ATimeUs);

TSAPI(s32)set_system_var_uint64_w_time(const char* ACompleteName,const u64 AValue,const s64 ATimeUs);

TSAPI(s32)set_system_var_uint8_array_w_time(const char* ACompleteName,const s32 ACount,const pu8 AValue,const s64 ATimeUs);

TSAPI(s32)set_system_var_int32_array_w_time(const char* ACompleteName,const s32 ACount,const ps32 AValue,const s64 ATimeUs);

TSAPI(s32)set_system_var_double_array_w_time(const char* ACompleteName,const s32 ACount,const pdouble AValue,const s64 ATimeUs);

TSAPI(s32)set_system_var_string_w_time(const char* ACompleteName,const char* AValue,const s64 ATimeUs);

TSAPI(s32)set_system_var_generic_w_time(const char* ACompleteName,const char* AValue,const s64 ATimeUs);

TSAPI(s32)set_system_var_double_async_w_time(const char* ACompleteName,const double AValue,const s64 ATimeUs);

TSAPI(s32)set_system_var_int32_async_w_time(const char* ACompleteName,const s32 AValue,const s64 ATimeUs);

TSAPI(s32)set_system_var_uint32_async_w_time(const char* ACompleteName,const u32 AValue,const s64 ATimeUs);

TSAPI(s32)set_system_var_int64_async_w_time(const char* ACompleteName,const s64 AValue,const s64 ATimeUs);

TSAPI(s32)set_system_var_uint64_async_w_time(const char* ACompleteName,const u64 AValue,const s64 ATimeUs);

TSAPI(s32)set_system_var_uint8_array_async_w_time(const char* ACompleteName,const s32 ACount,const pu8 AValue,const s64 ATimeUs);

TSAPI(s32)set_system_var_int32_array_async_w_time(const char* ACompleteName,const s32 ACount,const ps32 AValue,const s64 ATimeUs);

TSAPI(s32)set_system_var_int64_array_async_w_time(const char* ACompleteName,const s32 ACount,const ps64 AValue,const s64 ATimeUs);

TSAPI(s32)set_system_var_double_array_async_w_time(const char* ACompleteName,const s32 ACount,const pdouble AValue,const s64 ATimeUs);

TSAPI(s32)set_system_var_string_async_w_time(const char* ACompleteName,const char* AValue,const s64 ATimeUs);

TSAPI(s32)set_system_var_generic_async_w_time(const char* ACompleteName,const char* AValue,const s64 ATimeUs);

TSAPI(s32)db_get_signal_startbit_by_pdu_offset(const s32 ASignalStartBitInPDU,const s32 ASignalBitLength,const bool AIsSignalIntel,const bool AIsPDUIntel,const s32 APDUStartBit,const s32 APDUBitLength,const ps32 AActualStartBit);

TSAPI(s32)ui_show_save_file_dialog(const char* ATitle,const char* AFileTypeDesc,const char* AFilter,const char* ASuggestFileName,const ppchar ADestinationFileName);

TSAPI(s32)ui_show_open_file_dialog(const char* ATitle,const char* AFileTypeDesc,const char* AFilter,const char* ASuggestFileName,const ppchar ADestinationFileName);

TSAPI(s32)ui_show_select_directory_dialog(const ppchar ADestinationDirectory);

TSAPI(s32)transmit_ethernet_async(const PLIBEthernetHeader AEthernetHeader);

TSAPI(s32)transmit_ethernet_sync(const PLIBEthernetHeader AEthernetHeader,const s32 ATimeoutMs);

TSAPI(s32)inject_ethernet_frame(const PLIBEthernetHeader AEthernetHeader);

TSAPI(s32)tslog_blf_write_ethernet(const size_t AHandle,const PLIBEthernetHeader AEthernetHeader);

TSAPI(s32)set_ethernet_channel_count(const s32 ACount);

TSAPI(s32)get_ethernet_channel_count(const ps32 ACount);

TSAPI(s32)transmit_ethernet_async_wo_pretx(const PLIBEthernetHeader AEthernetHeader);

TSAPI(s32)db_get_can_db_index_by_id(const s32 AId,const ps32 AIndex);

TSAPI(s32)db_get_lin_db_index_by_id(const s32 AId,const ps32 AIndex);

TSAPI(s32)db_get_flexray_db_index_by_id(const s32 AId,const ps32 AIndex);

TSAPI(s32)eth_build_ipv4_udp_packet(const PLIBEthernetHeader AHeader,const pu8 ASrcIp,const pu8 ADstIp,const u16 ASrcPort,const u16 ADstPort,const pu8 APayload,const u16 APayloadLength,const ps32 AIdentification,const ps32 AFragmentIndex);

TSAPI(s32)register_system_var_change_event(const char* ACompleteName,const TLIBOnSysVarChange AEvent);

TSAPI(s32)unregister_system_var_change_event(const char* ACompleteName,const TLIBOnSysVarChange AEvent);

TSAPI(s32)unregister_system_var_change_events(const TLIBOnSysVarChange AEvent);

TSAPI(s32)block_current_pretx();

TSAPI(s32)call_system_api(const char* AAPIName,const s32 AArgCount,const s32 AArgCapacity,const ppchar AArgs);

TSAPI(s32)call_library_api(const char* AAPIName,const s32 AArgCount,const s32 AArgCapacity,const ppchar AArgs);

TSAPI(s32)eth_is_udp_packet(const PLIBEthernetHeader AHeader,u16* AIdentification,u16* AUDPPacketLength,u16* AUDPDataOffset,bool* AIsPacketEnded);

TSAPI(s32)eth_ip_calc_header_checksum(const PLIBEthernetHeader AHeader,const bool AOverwriteChecksum,const pu16 AChecksum);

TSAPI(s32)eth_udp_calc_checksum(const PLIBEthernetHeader AHeader,const pu8 AUDPPayloadAddr,const u16 AUDPPayloadLength,const bool AOverwriteChecksum,const pu16 AChecksum);

TSAPI(s32)eth_udp_calc_checksum_on_frame(const PLIBEthernetHeader AHeader,const bool AOverwriteChecksum,const pu16 AChecksum);

TSAPI(s32)eth_log_ethernet_frame_data(const PLIBEthernetHeader AHeader);

TSAPI(s32)signal_tester_clear_all();

TSAPI(s32)signal_tester_load_configuration(const char* AFilePath);

TSAPI(s32)signal_tester_save_configuration(const char* AFilePath);

TSAPI(s32)signal_tester_run_item_by_name(const char* AName);

TSAPI(s32)signal_tester_stop_item_by_name(const char* AName);

TSAPI(s32)signal_tester_run_item_by_index(const s32 AIndex);

TSAPI(s32)signal_tester_stop_item_by_index(const s32 AIndex);

TSAPI(s32)signal_tester_get_item_verdict_by_index(const pnative_int AObj,const s32 AIndex,const pbool AIsPass);

TSAPI(s32)signal_tester_get_item_result_by_name(const pnative_int AObj,const char* AName,const pbool AIsPass,const ps64 AEventTimeUs,const ppchar ADescription);

TSAPI(s32)signal_tester_get_item_result_by_index(const pnative_int AObj,const s32 AIndex,const pbool AIsPass,const ps64 AEventTimeUs,const ppchar ADescription);

TSAPI(s32)signal_tester_get_item_verdict_by_name(const pnative_int AObj,const char* AName,const pbool AIsPass);

TSAPI(s32)ini_read_string_wo_quotes(const size_t AHandle,const char* ASection,const char* AKey,const char* AValue,const ps32 AValueCapacity,const char* ADefault);

TSAPI(s32)signal_tester_check_statistics_by_index(const pnative_int AObj,const s32 AIndex,const double AMin,const double AMax,const pbool APass,const pdouble AResult,const ppchar AResultRepr);

TSAPI(s32)signal_tester_check_statistics_by_name(const pnative_int AObj,const char* AItemName,const double AMin,const double AMax,const pbool APass,const pdouble AResult,const ppchar AResultRepr);

TSAPI(s32)signal_tester_enable_item_by_index(const s32 AIndex,const bool AEnable);

TSAPI(s32)signal_tester_enable_item_by_name(const char* AItemName,const bool AEnable);

TSAPI(s32)signal_tester_run_all();

TSAPI(s32)signal_tester_stop_all();

TSAPI(s32)lin_clear_schedule_tables(const s32 AChnIdx);

TSAPI(s32)lin_stop_lin_channel(const s32 AChnIdx);

TSAPI(s32)lin_start_lin_channel(const s32 AChnIdx);

TSAPI(s32)lin_switch_runtime_schedule_table(const s32 AChnIdx);

TSAPI(s32)lin_switch_idle_schedule_table(const s32 AChnIdx);

TSAPI(s32)lin_switch_normal_schedule_table(const s32 AChnIdx,const s32 ASchIndex);

TSAPI(s32)lin_batch_set_schedule_start(const s32 AChnIdx);

TSAPI(s32)lin_batch_add_schedule_frame(const s32 AChnIdx,const PLIBLIN ALINData,const s32 ADelayMs);

TSAPI(s32)lin_batch_set_schedule_end(const s32 AChnIdx);

TSAPI(s32)lin_set_node_functiontype(const s32 AChnIdx,const s32 AFunctionType);

TSAPI(s32)lin_active_frame_in_schedule_table(const u32 AChnIdx,const u8 AID,const s32 AIndex);

TSAPI(s32)lin_deactive_frame_in_schedule_table(const u32 AChnIdx,const u8 AID,const s32 AIndex);

TSAPI(s32)flexray_disable_frame(const s32 AChnIdx,const u8 ASlot,const u8 ABaseCycle,const u8 ACycleRep,const s32 ATimeoutMs);

TSAPI(s32)flexray_enable_frame(const s32 AChnIdx,const u8 ASlot,const u8 ABaseCycle,const u8 ACycleRep,const s32 ATimeoutMs);

TSAPI(s32)open_help_doc(const char* AFileNameWoSuffix,const char* ATitle);

TSAPI(s32)get_language_string(const char* AEnglishStr,const char* AIniSection,const ppchar ATranslatedStr);

TSAPI(s32)convert_blf_to_csv(const char* ABlfFile,const char* ACSVFile,const pbool AToTerminate);

TSAPI(s32)convert_blf_to_csv_with_filter(const char* ABlfFile,const char* ACSVFile,const char* AFilterConf,const pbool AToTerminate);

TSAPI(s32)set_flexray_ub_bit_auto_handle(const bool AIsAutoHandle);

TSAPI(s32)signal_tester_get_item_status_by_index(const s32 AIdx,const pbool AIsRunning,const pbool AIsCheckDone,const PSignalTesterFailReason AFailReason);

TSAPI(s32)signal_tester_get_item_status_by_name(const char* ATesterName,const pbool AIsRunning,const pbool AIsCheckDone,const PSignalTesterFailReason AFailReason);

TSAPI(s32)signal_tester_set_item_time_range_by_index(const s32 AIdx,const double ATimeBegin,const double ATimeEnd);

TSAPI(s32)signal_tester_set_item_time_range_by_name(const char* AName,const double ATimeBegin,const double ATimeEnd);

TSAPI(s32)signal_tester_set_item_value_range_by_index(const s32 AIdx,const double ALow,const double AHigh);

TSAPI(s32)signal_tester_set_item_value_range_by_name(const char* AName,const double ALow,const double AHigh);

TSAPI(s32)start_log_w_filename(const pnative_int AObj,const char* AFileName);

TSAPI(s32)convert_blf_to_mat_w_filter(const char* ABlfFile,const char* AMatFile,const char* AFilterConf,const pbool AToTerminate);

TSAPI(s32)convert_asc_to_mat_w_filter(const char* AASCFile,const char* AMatFile,const char* AFilterConf,const pbool AToTerminate);

TSAPI(s32)convert_asc_to_csv_w_filter(const char* AASCFile,const char* ACSVFile,const char* AFilterConf,const pbool AToTerminate);

TSAPI(s32)set_debug_log_level(const s32 ALevel);

TSAPI(s32)eth_frame_clear_vlans(const PLIBEthernetHeader AHeader);

TSAPI(s32)eth_frame_append_vlan(const PLIBEthernetHeader AHeader,const u16 AVLANId,const u8 APriority,const u8 ACFI);

TSAPI(s32)eth_frame_append_vlans(const PLIBEthernetHeader AHeader,const pu16 AVLANIds,const u8 APriority,const u8 ACFI,const s32 ACount);

TSAPI(s32)eth_frame_remove_vlan(const PLIBEthernetHeader AHeader);

TSAPI(s32)eth_build_ipv4_udp_packet_on_frame(const PLIBEthernetHeader AInputHeader,const pu8 APayload,const u16 APayloadLength,const ps32 AIdentification,const ps32 AFragmentIndex);

TSAPI(s32)eth_udp_fragment_processor_clear();

TSAPI(s32)eth_udp_fragment_processor_parse(const PLIBEthernetHeader AHeader,const PUDPFragmentProcessStatus AStatus,const ppu8 APayload,const pu16 APayloadLength);

TSAPI(s32)eth_frame_insert_vlan(const PLIBEthernetHeader AHeader,const u16 AVLANId,const u8 APriority,const u8 ACFI);

TSAPI(s32)get_language_id(const ps32 AId);

TSAPI(s32)telnet_create(const char* AHost,const u16 APort,const TOnIoIPData ADataEvent,const psize_t AHandle);

TSAPI(s32)telnet_delete(const size_t AHandle);

TSAPI(s32)telnet_send_string(const size_t AHandle,const char* AStr);

TSAPI(s32)telnet_connect(const size_t AHandle);

TSAPI(s32)telnet_disconnect(const size_t AHandle);

TSAPI(s32)telnet_set_connection_callback(const size_t AHandle,const TOnIoIPConnection AConnectedCallback,const TOnIoIPConnection ADisconnectedCallback);

TSAPI(s32)telnet_enable_debug_print(const size_t AHandle,const bool AEnable);

TSAPI(s32)tslog_blf_to_pcap(const pnative_int AObj,const char* ABlfFileName,const char* APcapFileName,const TReadProgressCallback AProgressCallback);

TSAPI(s32)tslog_pcap_to_blf(const pnative_int AObj,const char* APcapFileName,const char* ABlfFileName,const TReadProgressCallback AProgressCallback);

TSAPI(s32)tslog_pcapng_to_blf(const pnative_int AObj,const char* APcapngFileName,const char* ABlfFileName,const TReadProgressCallback AProgressCallback);

TSAPI(s32)tslog_blf_to_pcapng(const pnative_int AObj,const char* ABlfFileName,const char* APcapngFileName,const TReadProgressCallback AProgressCallback);

TSAPI(s32)enter_critical_section();

TSAPI(s32)leave_critical_section();

TSAPI(s32)try_enter_critical_section();

TSAPI(s32)security_update_new_key_sync(const s32 AChnIdx,const char* AOldKey,const u8 AOldKeyLength,const char* ANewKey,const u8 ANewKeyLength,const s32 ATimeoutMS);

TSAPI(s32)security_unlock_write_authority_sync(const s32 AChnIdx,const char* AKey,const u8 AKeyLength,const s32 ATimeoutMS);

TSAPI(s32)security_unlock_write_authority_async(const s32 AChnIdx,const char* AKey,const u8 AKeyLength);

TSAPI(s32)security_write_string_sync(const s32 AChnIdx,const s32 ASlotIndex,const char* AString,const u8 AStringLength,const s32 ATimeoutMs);

TSAPI(s32)security_write_string_async(const s32 AChnIdx,const s32 ASlotIndex,const char* AString,const u8 AStringLength);

TSAPI(s32)security_read_string_sync(const s32 AChnIdx,const s32 ASlotIndex,const char* AString,const pu8 AStringLength,const s32 ATimeoutMS);

TSAPI(s32)security_unlock_encrypt_channel_sync(const s32 AChnIdx,const s32 ASlotIndex,const char* AString,const u8 AStringLength,const s32 ATimeoutMS);

TSAPI(s32)security_unlock_encrypt_channel_async(const s32 AChnIdx,const s32 ASlotIndex,const char* AString,const u8 AStringLength);

TSAPI(s32)security_encrypt_string_sync(const s32 AChnIdx,const s32 ASlotIndex,const char* AString,const pu8 AStringLength,const s32 ATimeoutMS);

TSAPI(s32)security_decrypt_string_sync(const s32 AChnIdx,const s32 ASlotIndex,const char* AString,const pu8 AStringLength,const s32 ATimeoutMS);

TSAPI(s32)tsapp_security_update_new_key_sync(const s32 AChnIdx,const char* AOldKey,const u8 AOldKeyLength,const char* ANewKey,const u8 ANewKeyLength,const s32 ATimeoutMS);

TSAPI(s32)tsapp_security_unlock_write_authority_sync(const s32 AChnIdx,const char* AKey,const u8 AKeyLength,const s32 ATimeoutMS);

TSAPI(s32)tsapp_security_unlock_write_authority_async(const s32 AChnIdx,const char* AKey,const u8 AKeyLength);

TSAPI(s32)tsapp_security_write_string_sync(const s32 AChnIdx,const s32 ASlotIndex,const char* AString,const u8 AStringLength,const s32 ATimeoutMs);

TSAPI(s32)tsapp_security_write_string_async(const s32 AChnIdx,const s32 ASlotIndex,const char* AString,const u8 AStringLength);

TSAPI(s32)tsapp_security_read_string_sync(const s32 AChnIdx,const s32 ASlotIndex,const char* AString,const pu8 AStringLength,const s32 ATimeoutMS);

TSAPI(s32)tsapp_security_unlock_encrypt_channel_sync(const s32 AChnIdx,const s32 ASlotIndex,const char* AString,const u8 AStringLength,const s32 ATimeoutMS);

TSAPI(s32)tsapp_security_unlock_encrypt_channel_async(const s32 AChnIdx,const s32 ASlotIndex,const char* AString,const u8 AStringLength);

TSAPI(s32)tsapp_security_encrypt_string_sync(const s32 AChnIdx,const s32 ASlotIndex,const char* AString,const pu8 AStringLength,const s32 ATimeoutMS);

TSAPI(s32)tsapp_security_decrypt_string_sync(const s32 AChnIdx,const s32 ASlotIndex,const char* AString,const pu8 AStringLength,const s32 ATimeoutMS);

TSAPI(s32)set_channel_timestamp_deviation_factor(const TLIBApplicationChannelType ABusType,const s32 AIdxLogicalChn,const s64 APCTimeUs,const s64 AHwTimeUs);

TSAPI(s32)start_system_message_log(const char* ADirectory);

TSAPI(s32)end_system_message_log(const ppchar ALogFileName);

TSAPI(s32)rpc_create_server(const char* ARpcName,const size_t ABufferSizeBytes,const TOnRpcData ARxEvent,const psize_t AHandle);

TSAPI(s32)rpc_activate_server(const size_t AHandle,const bool AActivate);

TSAPI(s32)rpc_delete_server(const size_t AHandle);

TSAPI(s32)rpc_server_write_sync(const size_t AHandle,const pu8 AAddr,const size_t ASizeBytes);

TSAPI(s32)rpc_create_client(const char* ARpcName,const size_t ABufferSizeBytes,const psize_t AHandle);

TSAPI(s32)rpc_activate_client(const size_t AHandle,const bool AActivate);

TSAPI(s32)rpc_delete_client(const size_t AHandle);

TSAPI(s32)rpc_client_transmit_sync(const size_t AHandle,const pu8 AAddr,const size_t ASizeBytes,const s32 ATimeOutMs);

TSAPI(s32)rpc_client_receive_sync(const size_t AHandle,const psize_t ASizeBytes,const pu8 AAddr,const s32 ATimeOutMs);

TSAPI(s32)mask_fpu_exceptions(const bool AMasked);

TSAPI(s32)rpc_tsmaster_activate_server(const bool AActivate);

TSAPI(s32)rpc_tsmaster_create_client(const char* ATSMasterAppName,const psize_t AHandle);

TSAPI(s32)rpc_tsmaster_activate_client(const size_t AHandle,const bool AActivate);

TSAPI(s32)rpc_tsmaster_delete_client(const size_t AHandle);

TSAPI(s32)rpc_tsmaster_cmd_start_simulation(const size_t AHandle);

TSAPI(s32)rpc_tsmaster_cmd_stop_simulation(const size_t AHandle);

TSAPI(s32)rpc_tsmaster_cmd_write_system_var(const size_t AHandle,const char* ACompleteName,const char* AValue);

TSAPI(s32)rpc_tsmaster_cmd_transfer_memory(const size_t AHandle,const pu8 AAddr,const size_t ASizeBytes);

TSAPI(s32)rpc_tsmaster_cmd_log(const size_t AHandle,const char* AMsg,const s32 ALevel);

TSAPI(s32)rpc_tsmaster_cmd_set_mode_sim(const size_t AHandle);

TSAPI(s32)rpc_tsmaster_cmd_set_mode_realtime(const size_t AHandle);

TSAPI(s32)rpc_tsmaster_cmd_set_mode_free(const size_t AHandle);

TSAPI(s32)rpc_tsmaster_cmd_sim_step(const size_t AHandle,const s64 ATimeUs);

TSAPI(s32)create_process_shared_memory(const ppu8 AAddress,const s32 ASizeBytes);

TSAPI(s32)get_process_shared_memory(const ppu8 AAddress,const ps32 ASizeBytes);

TSAPI(s32)rpc_tsmaster_cmd_sim_step_batch_start(const size_t AHandle);

TSAPI(s32)rpc_tsmaster_cmd_sim_step_batch_end(const size_t AHandle,const s64 ATimeUs);

TSAPI(s32)rpc_tsmaster_cmd_get_project(const size_t AHandle,const ppchar AProjectFullPath);

TSAPI(s32)rpc_tsmaster_cmd_read_system_var(const size_t AHandle,const char* ASysVarName,const pdouble AValue);

TSAPI(s32)rpc_tsmaster_cmd_read_signal(const size_t AHandle,const TLIBApplicationChannelType ABusType,const char* AAddr,const pdouble AValue);

TSAPI(s32)rpc_tsmaster_cmd_write_signal(const size_t AHandle,const TLIBApplicationChannelType ABusType,const char* AAddr,const double AValue);

TSAPI(s32)can_rbs_set_normal_signal(const char* ASymbolAddress);

TSAPI(s32)can_rbs_set_rc_signal(const char* ASymbolAddress);

TSAPI(s32)can_rbs_set_rc_signal_with_limit(const char* ASymbolAddress,const s32 ALowerLimit,const s32 AUpperLimit);

TSAPI(s32)can_rbs_set_crc_signal(const char* ASymbolAddress,const char* AAlgorithmName,const s32 AIdxByteStart,const s32 AByteCount);

TSAPI(s32)clear_user_constants();

TSAPI(s32)append_user_constants_from_c_header(const char* AHeaderFile);

TSAPI(s32)append_user_constant(const char* AConstantName,const double AValue,const char* ADesc);

TSAPI(s32)delete_user_constant(const char* AConstantName);

TSAPI(s32)get_mini_program_count(const ps32 ACount);

TSAPI(s32)get_mini_program_info_by_index(const s32 AIndex,const ps32 AKind,const ppchar AProgramName,const ppchar ADisplayName);

TSAPI(s32)compile_mini_programs(const char* AProgramNames);

TSAPI(s32)set_system_var_init_value(const char* ACompleteName,const char* AValue);

TSAPI(s32)get_system_var_init_value(const char* ACompleteName,const ppchar AValue);

TSAPI(s32)reset_system_var_to_init(const char* ACompleteName);

TSAPI(s32)reset_all_system_var_to_init(const char* AOwner);

TSAPI(s32)get_system_var_generic_upg1(const char* ACompleteName,const ppchar AValue);

TSAPI(s32)rpc_tsmaster_cmd_set_can_signal(const size_t AHandle,const char* ASgnAddress,const double AValue);

TSAPI(s32)rpc_tsmaster_cmd_get_can_signal(const size_t AHandle,const char* ASgnAddress,const pdouble AValue);

TSAPI(s32)rpc_tsmaster_cmd_get_lin_signal(const size_t AHandle,const char* ASgnAddress,const pdouble AValue);

TSAPI(s32)rpc_tsmaster_cmd_set_lin_signal(const size_t AHandle,const char* ASgnAddress,const double AValue);

TSAPI(s32)rpc_tsmaster_cmd_set_flexray_signal(const size_t AHandle,const char* ASgnAddress,const double AValue);

TSAPI(s32)rpc_tsmaster_cmd_get_flexray_signal(const size_t AHandle,const char* ASgnAddress,const pdouble AValue);

TSAPI(s32)rpc_tsmaster_cmd_get_constant(const size_t AHandle,const char* AConstName,const pdouble AValue);

TSAPI(s32)rpc_tsmaster_is_simulation_running(const size_t AHandle,const pbool AIsRunning);

TSAPI(s32)rpc_tsmaster_call_system_api(const size_t AHandle,const char* AAPIName,const s32 AArgCount,const s32 AArgCapacity,const ppchar AArgs);

TSAPI(s32)rpc_tsmaster_call_library_api(const size_t AHandle,const char* AAPIName,const s32 AArgCount,const s32 AArgCapacity,const ppchar AArgs);

TSAPI(s32)get_tsmaster_binary_location(const ppchar ADirectory);

TSAPI(s32)get_active_application_list(const ppchar ATSMasterAppNames);

TSAPI(s32)encode_string(const char* ASrc,const ppchar ADest);

TSAPI(s32)decode_string(const char* ASrc,const ppchar ADest);

TSAPI(s32)rpc_tsmaster_cmd_register_signal_cache(const size_t AHandle,const TLIBApplicationChannelType ABusType,const char* ASgnAddress,const ps64 AId);

TSAPI(s32)rpc_tsmaster_cmd_unregister_signal_cache(const size_t AHandle,const s64 AId);

TSAPI(s32)rpc_tsmaster_cmd_get_signal_cache_value(const size_t AHandle,const s64 AId,const pdouble AValue);

TSAPI(s32)can_rbs_set_crc_signal_w_head_tail(const char* ASymbolAddress,const char* AAlgorithmName,const s32 AIdxByteStart,const s32 AByteCount,const pu8 AHeadAddr,const s32 AHeadSizeBytes,const pu8 ATailAddr,const s32 ATailSizeBytes);

TSAPI(s32)is_realtime_mode(const pbool AValue);

TSAPI(s32)is_simulation_mode(const pbool AValue);

TSAPI(s32)tslog_blf_write_sysvar_double(const size_t AHandle,const char* AName,const s64 ATimeUs,const double AValue);

TSAPI(s32)tslog_blf_write_sysvar_s32(const size_t AHandle,const char* AName,const s64 ATimeUs,const s32 AValue);

TSAPI(s32)tslog_blf_write_sysvar_u32(const size_t AHandle,const char* AName,const s64 ATimeUs,const u32 AValue);

TSAPI(s32)tslog_blf_write_sysvar_s64(const size_t AHandle,const char* AName,const s64 ATimeUs,const s64 AValue);

TSAPI(s32)tslog_blf_write_sysvar_u64(const size_t AHandle,const char* AName,const s64 ATimeUs,const u64 AValue);

TSAPI(s32)tslog_blf_write_sysvar_string(const size_t AHandle,const char* AName,const s64 ATimeUs,const char* AValue);

TSAPI(s32)tslog_blf_write_sysvar_double_array(const size_t AHandle,const char* AName,const s64 ATimeUs,const pdouble AValue,const s32 AValueCount);

TSAPI(s32)tslog_blf_write_sysvar_s32_array(const size_t AHandle,const char* AName,const s64 ATimeUs,const ps32 AValue,const s32 AValueCount);

TSAPI(s32)tslog_blf_write_sysvar_u8_array(const size_t AHandle,const char* AName,const s64 ATimeUs,const pu8 AValue,const s32 AValueCount);

TSAPI(s32)rpc_tsmaster_cmd_start_can_rbs(const size_t AHandle);

TSAPI(s32)rpc_tsmaster_cmd_stop_can_rbs(const size_t AHandle);

TSAPI(s32)rpc_tsmaster_cmd_start_lin_rbs(const size_t AHandle);

TSAPI(s32)rpc_tsmaster_cmd_stop_lin_rbs(const size_t AHandle);

TSAPI(s32)rpc_tsmaster_cmd_start_flexray_rbs(const size_t AHandle);

TSAPI(s32)rpc_tsmaster_cmd_stop_flexray_rbs(const size_t AHandle);

TSAPI(s32)rpc_tsmaster_cmd_is_can_rbs_running(const size_t AHandle,const pbool AIsRunning);

TSAPI(s32)rpc_tsmaster_cmd_is_lin_rbs_running(const size_t AHandle,const pbool AIsRunning);

TSAPI(s32)rpc_tsmaster_cmd_is_flexray_rbs_running(const size_t AHandle,const pbool AIsRunning);

TSAPI(s32)flexray_rbs_reset_update_bits();

TSAPI(s32)can_rbs_reset_update_bits();

TSAPI(s32)can_rbs_fault_inject_handle_on_autosar_crc_event(const TOnAutoSARE2ECanEvt AEvent);

TSAPI(s32)can_rbs_fault_inject_handle_on_autosar_rc_event(const TOnAutoSARE2ECanEvt AEvent);

TSAPI(s32)can_rbs_fault_inject_unhandle_on_autosar_rc_event(const TOnAutoSARE2ECanEvt AEvent);

TSAPI(s32)can_rbs_fault_inject_unhandle_on_autosar_crc_event(const TOnAutoSARE2ECanEvt AEvent);

TSAPI(s32)register_usb_insertion_event(const TOnUSBPlugEvent AEvent);

TSAPI(s32)unregister_usb_insertion_event(const TOnUSBPlugEvent AEvent);

TSAPI(s32)register_usb_removal_event(const TOnUSBPlugEvent AEvent);

TSAPI(s32)unregister_usb_removal_event(const TOnUSBPlugEvent AEvent);

TSAPI(s32)can_rbs_set_update_bits();

TSAPI(s32)flexray_rbs_set_update_bits();

TSAPI(s32)rpc_ip_trigger_data_group(const s32 AGroupId);

TSAPI(s32)can_rbs_get_signal_raw_by_address(const char* ASymbolAddress,const pu64 ARaw);

TSAPI(s32)eth_rbs_start();

TSAPI(s32)eth_rbs_stop();

TSAPI(s32)eth_rbs_is_running(const pbool AIsRunning);

TSAPI(s32)eth_rbs_configure(const bool AAutoStart,const bool AAutoSendOnModification,const bool AActivateNodeSimulation,const s32 AInitValueOptions);

TSAPI(s32)eth_rbs_activate_all_networks(const bool AEnable,const bool AIncludingChildren);

TSAPI(s32)eth_rbs_activate_network_by_name(const s32 AIdxChn,const bool AEnable,const char* ANetworkName,const bool AIncludingChildren);

TSAPI(s32)eth_rbs_activate_node_by_name(const s32 AIdxChn,const bool AEnable,const char* ANetworkName,const char* ANodeName,const bool AIncludingChildren);

TSAPI(s32)eth_rbs_activate_pdu_by_name(const s32 AIdxChn,const bool AEnable,const char* ANetworkName,const char* ANodeName,const char* APDUName);

TSAPI(s32)eth_rbs_set_pdu_phase_and_cycle_by_name(const s32 AIdxChn,const s32 APhaseMs,const s32 ACycleMs,const char* ANetworkName,const char* ANodeName,const char* APDUName);

TSAPI(s32)eth_rbs_get_signal_value_by_element(const s32 AIdxChn,const char* ANetworkName,const char* ANodeName,const char* APDUName,const char* ASignalName,const pdouble AValue);

TSAPI(s32)eth_rbs_set_signal_value_by_element(const s32 AIdxChn,const char* ANetworkName,const char* ANodeName,const char* APDUName,const char* ASignalName,const double AValue);

TSAPI(s32)eth_rbs_get_signal_value_by_address(const char* ASymbolAddress,const pdouble AValue);

TSAPI(s32)eth_rbs_set_signal_value_by_address(const char* ASymbolAddress,const double AValue);

TSAPI(s32)call_model_initialization(const char* ADiagramName,const s32 AInCnt,const s32 AOutCnt,const PLIBMBDDataType AInTypes,const PLIBMBDDataType AOutTypes,const psize_t AHandle);

TSAPI(s32)call_model_step(const size_t AHandle,const s64 ATimeUs,const pnative_int AInValues,const pnative_int AOutValues);

TSAPI(s32)call_model_finalization(const size_t AHandle);

TSAPI(s32)lin_rbs_update_frame_by_id(const s32 AChnIdx,const u8 AId);

TSAPI(s32)lin_rbs_register_force_refresh_frame_by_id(const s32 AChnIdx,const u8 AId);

TSAPI(s32)lin_rbs_unregister_force_refresh_frame_by_id(const s32 AChnIdx,const u8 AId);

TSAPI(s32)rpc_data_channel_create(const char* ARpcName,const s32 AIsMaster,const size_t ABufferSizeBytes,const TOnRpcData ARxEvent,const psize_t AHandle);

TSAPI(s32)rpc_data_channel_delete(const size_t AHandle);

TSAPI(s32)rpc_data_channel_transmit(const size_t AHandle,const pu8 AAddr,const size_t ASizeBytes,const s32 ATimeOutMs);

TSAPI(s32)tssocket_set_host_name(const s32 ANetworkIndex,const char* AIPAddress,const char* AHostName);

TSAPI(s32)tsdo_set_pwm_output_async(const s32 AChn,const double ADuty,const double AFrequency);

TSAPI(s32)tsdo_set_vlevel_output_async(const s32 AChn,const s32 AIOStatus);

TSAPI(s32)can_il_register_autosar_pdu_event(const s32 AChn,const s32 AID,const TOnAutoSARPDUQueueEvent AEvent);

TSAPI(s32)can_il_unregister_autosar_pdu_event(const s32 AChn,const s32 AID,const TOnAutoSARPDUQueueEvent AEvent);

TSAPI(s32)can_il_register_autosar_pdu_pretx_event(const s32 AChn,const s32 AID,const TOnAutoSARPDUPreTxEvent AEvent);

TSAPI(s32)can_il_unregister_autosar_pdu_pretx_event(const s32 AChn,const s32 AID,const TOnAutoSARPDUPreTxEvent AEvent);

TSAPI(s32)can_rbs_fault_inject_disturb_sequencecounter(const s32 AChn,const char* ANetworkName,const char* ANodeName,const char* AMessageName,const char* ASignalGroupName,const s32 atype,const s32 disturbanceMode,const s32 disturbanceCount,const s32 disturbanceValue,const s32 continueMode);

TSAPI(s32)can_rbs_fault_inject_disturb_checksum(const s32 AChn,const char* ANetworkName,const char* ANodeName,const char* AMessageName,const char* ASignalGroupName,const s32 atype,const s32 disturbanceMode,const s32 disturbanceCount,const s32 disturbanceValue);

TSAPI(s32)can_rbs_fault_inject_disturb_updatebit(const s32 AChn,const char* ANetworkName,const char* ANodeName,const char* AMessageName,const char* ASignalGroupName,const s32 disturbanceMode,const s32 disturbanceCount,const s32 disturbanceValue);

TSAPI(s32)tsio_start_configuration();

TSAPI(s32)tsio_end_configuration();

TSAPI(s32)tsdi_config_sync(const s32 AChn,const double ASampleRate,const s32 AInputThrsholdMv,const s32 AReportPWMFreq,const s32 ATimeoutMs);

TSAPI(s32)tsdo_config_sync(const s32 AChn,const s32 AEnableReport,const double ASampleRate,const s32 AOutputLevel,const s32 AOutputMode,const s32 AOutputType,const s32 ATimeoutMs);

TSAPI(s32)cal_add_xcp_ecu(const char* AECUName,const char* AA2LFile,const s32 ATPLayer,const s32 AChnIdx,const s32 AEnabled);

TSAPI(s32)cal_add_ccp_ecu(const char* AECUName,const char* AA2LFile,const s32 AChnIdx,const s32 AEnabled);

TSAPI(s32)cal_remove_ecu(const char* AECUName);

TSAPI(s32)set_di_channel_count(const s32 ACount);

TSAPI(s32)set_do_channel_count(const s32 ACount);

TSAPI(s32)set_ao_channel_count(const s32 ACount);

TSAPI(s32)set_ai_channel_count(const s32 ACount);

TSAPI(s32)get_ai_channel_count(const ps32 ACount);

TSAPI(s32)get_ao_channel_count(const ps32 ACount);

TSAPI(s32)get_do_channel_count(const ps32 ACount);

TSAPI(s32)get_di_channel_count(const ps32 ACount);

TSAPI(s32)cal_get_var_property(const char* AECUName,const char* AVarName,const ppchar ADataType,const pdouble ALowerValue,const pdouble AUpperValue,const pdouble AStepValue);

TSAPI(s32)cal_get_measurement_list(const char* AECUName,const ppchar AMeasurementList);

TSAPI(s32)tac_debugger_create(const TMPTacDebugCallback ACallback,const pnative_int AUserData,const ppnative_int ADebuggerPtr);

TSAPI(s32)tac_debugger_destroy(const pvoid ADebugger);

TSAPI(s32)tac_debugger_terminate(const pvoid debugger);

TSAPI(s32)tac_debugger_register_struct_from_json(const pvoid debugger,const char* type_name,const char* json_definition);

TSAPI(s32)tac_debugger_get_last_error(const pvoid debugger,const char* message,const ps32 message_size,const char* afile,const ps32 file_size,const ps32 line,const ps32 column);

TSAPI(s32)tac_debugger_run_script(const pvoid debugger,const char* script_content,const char* script_name);

TSAPI(s32)tac_debugger_run_file(const pvoid debugger,const char* file_path);

TSAPI(s32)tac_debugger_is_running(const pvoid debugger,const pbool is_running);

TSAPI(s32)tac_debugger_set_breakpoint(const pvoid debugger,const char* afile,const s32 line,const pvoid* breakpoint_ptr);

TSAPI(s32)tac_debugger_remove_breakpoint(const pvoid debugger,const pvoid breakpoint);

TSAPI(s32)tac_debugger_clear_breakpoints(const pvoid debugger);

TSAPI(s32)tac_debugger_get_breakpoints(const pvoid debugger,const pvoid* breakpoints_array,const ps32 count);

TSAPI(s32)tac_debugger_has_breakpoint_at(const pvoid debugger,const char* afile,const s32 line,const pbool exists);

TSAPI(s32)tac_breakpoint_get_info(const pvoid breakpoint,const char* file_buffer,const s32 file_buffer_size,const ps32 line_ptr);

TSAPI(s32)tac_debugger_pause(const pvoid debugger);

TSAPI(s32)tac_debugger_continue(const pvoid debugger);

TSAPI(s32)tac_debugger_step_over(const pvoid debugger);

TSAPI(s32)tac_debugger_step_into(const pvoid debugger);

TSAPI(s32)tac_debugger_step_out(const pvoid debugger);

TSAPI(s32)tac_debugger_get_call_stack_count(const pvoid debugger,const ps32 frame_count);

TSAPI(s32)tac_debugger_get_call_stack_item(const pvoid debugger,const s32 frame_index,const char* item,const ps32 item_buffer_cnt);

TSAPI(s32)tac_debugger_get_local_variables_count(const pvoid debugger,const s32 frame_index,const ps32 variable_cnt);

TSAPI(s32)tac_debugger_get_local_variable(const pvoid debugger,const s32 frame_index,const s32 var_index,const pvoid* variable);

TSAPI(s32)tac_debugger_evaluate_expression(const pvoid debugger,const s32 frame_index,const char* expression,const pvoid* result_value);

TSAPI(s32)tac_value_destroy(const pvoid value);

TSAPI(s32)tac_value_get_type(const pvoid value,const PMPTacValueType type_out);

TSAPI(s32)tac_value_get_name(const pvoid value,const char* name_buffer,const s32 buffer_size);

TSAPI(s32)tac_value_to_string(const pvoid value,const char* str_buffer,const s32 buffer_size);

TSAPI(s32)tac_value_as_integer(const pvoid value,const ps64 AOut);

TSAPI(s32)tac_value_as_float(const pvoid value,const pdouble AOut);

TSAPI(s32)tac_value_as_boolean(const pvoid value,const pbool AOut);

TSAPI(s32)tac_run_script_sync(const char* script_content,const char* script_name);

TSAPI(s32)tac_run_file_sync(const char* file_path);

TSAPI(s32)rpc_set_global_timeout(const s32 ATimeOutMs);

TSAPI(s32)tsdi_get_vlevel_input_sync(const s32 AChnIdx,const ps32 AIOStatus,const s32 ATimeoutMs);

TSAPI(s32)tsdi_get_pwm_input_sync(const s32 AChnIdx,const pdouble ADuty,const pdouble AFreq,const s32 ATimeoutMs);

TSAPI(s32)cal_get_ecu_a2l_list(const ppchar AECUsAndA2Ls);

TSAPI(s32)cal_set_all_datas_by_value(const char* AECUName,const char* AVarName,const double AValue,const u8 AImmediateDownload);

TSAPI(s32)cal_set_all_datas_by_offset(const char* AECUName,const char* AVarName,const double AOffset,const u8 AImmediateDownload);

TSAPI(s32)cal_set_datas_by_offset(const char* AECUName,const char* AVarName,const s32 AStartX,const s32 AStartY,const s32 AXPointsNum,const s32 AYPointsNum,const double AOffset,const u8 AImmediateDownload);

TSAPI(s32)cal_set_datas_by_value(const char* AECUName,const char* AVarName,const s32 AStartX,const s32 AStartY,const s32 AXPointsNum,const s32 AYPointsNum,const double AValue,const u8 AImmediateDownload);

TSAPI(s32)cal_get_axisnum_and_address(const char* AECUName,const char* AVarName,const ps32 AXPointsNum,const ps32 AYPointsNum,const pu32 AAdress,const pu32 AExtAddress);

TSAPI(s32)crypto_encrypt_aes_128_ecb(const pu8 key,const size_t key_length,const pu8 plaintext,const size_t plaintext_length,const pu8 ciphertext,const psize_t ciphertext_length);

TSAPI(s32)crypto_decrypt_aes_128_ecb(const pu8 key,const size_t key_length,const pu8 ciphertext,const size_t ciphertext_length,const pu8 plaintext,const psize_t plaintext_length);

TSAPI(s32)crypto_decrypt_aes_128_cbc(const pu8 key,const size_t key_length,const pu8 ciphertext,const size_t ciphertext_length,const pu8 iv,const size_t iv_length,const pu8 plaintext,const psize_t plaintext_length);

TSAPI(s32)crypto_decrypt_aes_256_cbc(const pu8 key,const size_t key_length,const pu8 ciphertext,const size_t ciphertext_length,const pu8 iv,const size_t iv_length,const pu8 plaintext,const psize_t plaintext_length);

TSAPI(s32)crypto_decrypt_rsa(const u8 key_coding,const pu8 private_key,const size_t key_length,const pu8 ciphertext,const size_t ciphertext_length,const pu8 plaintext,const psize_t plaintext_length,const u8 padding_mode);

TSAPI(s32)crypto_encrypt_rsa(const u8 key_coding,const pu8 public_key,const size_t key_length,const pu8 plaintext,const size_t plaintext_length,const pu8 ciphertext,const psize_t ciphertext_length,const u8 padding_mode);

TSAPI(s32)crypto_encrypt_aes_128_cbc(const pu8 key,const size_t key_length,const pu8 plaintext,const size_t plaintext_length,const pu8 iv,const size_t iv_length,const pu8 ciphertext,const psize_t ciphertext_length);

TSAPI(s32)crypto_encrypt_aes_256_cbc(const pu8 key,const size_t key_length,const pu8 plaintext,const size_t plaintext_length,const pu8 iv,const size_t iv_length,const pu8 ciphertext,const psize_t ciphertext_length);

TSAPI(s32)crypto_digest_sha2_256(const pnative_int data,const size_t data_length,const pu8 hash,const psize_t hash_length);

TSAPI(s32)crypto_digest_sha2_512(const pnative_int data,const size_t data_length,const pu8 hash,const psize_t hash_length);

TSAPI(s32)crypto_digest_sha3_512(const pnative_int data,const size_t data_length,const pu8 hash,const psize_t hash_length);

TSAPI(s32)crypto_digest_sha3_256(const pnative_int data,const size_t data_length,const pu8 hash,const psize_t hash_length);

TSAPI(s32)crypto_digest_md5(const pnative_int data,const size_t data_length,const pu8 hash,const psize_t hash_length);

TSAPI(s32)crypto_generate_cmac(const pu8 key,const size_t key_length,const pu8 data,const size_t data_length,const pu8 cmac,const psize_t cmac_length);

TSAPI(s32)crypto_generate_random_bytes(const pu8 data,const s32 data_length);

TSAPI(s32)crypto_crypt_aes_128_ctr(const pu8 key,const size_t key_length,const pu8 plaintext,const pu8 ciphertext,const size_t text_length,const pu8 nonce,const size_t noncelength);

TSAPI(s32)can_rbs_transmit_pdu(const s32 AChn,const char* ANetworkName,const char* ANodeName,const char* AMessageName,const char* APDUName,const pu8 AData,const s32 ADataLength);

TSAPI(s32)can_rbs_get_signal_value_by_element_verbose(const s32 AIdxChn,const char* ANetworkName,const char* ANodeName,const char* AMessageName,const char* APDUName,const char* ASignalName,const pdouble AValue);

TSAPI(s32)can_rbs_set_signal_value_by_element_verbose(const s32 AIdxChn,const char* ANetworkName,const char* ANodeName,const char* AMessageName,const char* APDUName,const char* ASignalName,const double AValue);

TSAPI(s32)flexray_rbs_set_signal_value_by_element_verbose(const s32 AIdxChn,const char* ANetworkName,const char* ANodeName,const char* AMessageName,const char* APDUName,const char* ASignalName,const double AValue);

TSAPI(s32)flexray_rbs_get_signal_value_by_element_verbose(const s32 AIdxChn,const char* ANetworkName,const char* ANodeName,const char* AMessageName,const char* APDUName,const char* ASignalName,const pdouble AValue);

TSAPI(s32)can_il_register_signal_event(const s32 AIdxChn,const char* ANetworkName,const char* ANodeName,const char* AMessageName,const char* APDUName,const char* ASignalName,const s32 ATriggerOnlyChanged,const TOnSignalEvent AEvent);

TSAPI(s32)can_il_unregister_signal_event(const s32 AIdxChn,const char* ANetworkName,const char* ANodeName,const char* AMessageName,const char* APDUName,const char* ASignalName,const TOnSignalEvent AEvent);

TSAPI(s32)can_rbs_time_monitor_config(const bool AEnableTimeMonitor,const s32 ATimeoutMs,const bool AEnableCyclicPeriodRate,const s32 ACyclicPeriodRateValue);

TSAPI(s32)can_il_register_signal_event_by_id(const s32 AIdxChn,const s32 AFrameID,const u32 APDUID,const char* ASignalName,const s32 ATriggerOnlyChanged,const TOnSignalEvent AEvent);

TSAPI(s32)can_il_unregister_signal_event_by_id(const s32 AIdxChn,const s32 AFrameID,const u32 APDUID,const char* ASignalName,const TOnSignalEvent AEvent);

TSAPI(s32)crypto_signature_rsa(const u8 key_coding,const u8 hash_method,const u8 rsa_padding_mode,const pu8 data,const size_t datalength,const pu8 privatekey,const size_t keylength,const pu8 signature,const psize_t signaturelength);

TSAPI(s32)eth_il_register_autosar_pdu_event(const s32 AChn,const u32 AHeaderID,const TOnAutoSARPDUQueueEvent AEvent);

TSAPI(s32)eth_il_unregister_autosar_pdu_event(const s32 AChn,const u32 AHeaderID,const TOnAutoSARPDUQueueEvent AEvent);

TSAPI(s32)eth_il_register_autosar_pdu_pretx_event(const s32 AChn,const u32 AHeaderID,const TOnAutoSARPDUPreTxEvent AEvent);

TSAPI(s32)eth_il_unregister_autosar_pdu_pretx_event(const s32 AChn,const u32 AHeaderID,const TOnAutoSARPDUPreTxEvent AEvent);

TSAPI(s32)configure_lin_baudrate(const s32 AChn,const float ABaudrateKbps,const s32 AProtocol);

TSAPI(s32)simulate_can_async(const PLIBCAN ACAN,const u8 AIsTx);

TSAPI(s32)simulate_canfd_async(const PLIBCANFD ACANFD,const u8 AIsTx);

TSAPI(s32)simulate_lin_async(const PLIBLIN ALIN,const u8 AIsTx);

TSAPI(s32)simulate_flexray_async(const PLIBFlexRay AFlexRay,const u8 AIsTx);

TSAPI(s32)simulate_ethernet_async(const PLIBEthernetHeader AEthernetHeader,const u8 AIsTx);

TSAPI(s32)can_rbs_set_signal_raw_by_address(const char* ASymbolAddress,const u64 ARaw);

TSAPI(s32)lin_rbs_set_signal_raw_by_address(const char* ASymbolAddress,const u64 ARaw);

TSAPI(s32)lin_rbs_get_signal_raw_by_address(const char* ASymbolAddress,const pu64 ARaw);

TSAPI(s32)db_get_can_network_info_by_index(const s32 AChn,const ppchar ANetworkInfo);

TSAPI(s32)db_get_lin_network_info_by_index(const s32 AChn,const ppchar ANetworkInfo);

TSAPI(s32)db_get_flexray_network_info_by_index(const s32 AChn,const ppchar ANetworkInfo);

TSAPI(s32)db_get_ethernet_network_info_by_index(const s32 AChn,const ppchar ANetworkInfo);

TSAPI(s32)set_system_var_uint8_array_element(const char* ACompleteName,const s32 AIdx,const u8 AValue);

TSAPI(s32)get_system_var_uint8_array_element(const char* ACompleteName,const s32 AIdx,const pu8 AValue);

TSAPI(s32)get_system_var_int32_array_element(const char* ACompleteName,const s32 AIdx,const ps32 AValue);

TSAPI(s32)set_system_var_int32_array_element(const char* ACompleteName,const s32 AIdx,const s32 AValue);

TSAPI(s32)get_system_var_int64_array_element(const char* ACompleteName,const s32 AIdx,const ps64 AValue);

TSAPI(s32)set_system_var_int64_array_element(const char* ACompleteName,const s32 AIdx,const s64 AValue);

TSAPI(s32)get_system_var_double_array_element(const char* ACompleteName,const s32 AIdx,const pdouble AValue);

TSAPI(s32)set_system_var_double_array_element(const char* ACompleteName,const s32 AIdx,const double AValue);

TSAPI(s32)rbs_get_signal_value_by_address(const char* ASymbolAddress,const pdouble AValue);

TSAPI(s32)rbs_set_signal_value_by_address(const char* ASymbolAddress,const double AValue);

TSAPI(s32)get_system_var_type(const char* ACompleteName,const PLIBSystemVarType AType);

TSAPI(s32)metric_get_can_frame_interval_stat(const s32 AIdxChn,const u64 AFrameId,const PTSMetricIntegerSnapshot AIdxStat);

TSAPI(s32)metric_start();

TSAPI(s32)metric_stop();

TSAPI(s32)metric_is_running(const pbool AIsRunning);

TSAPI(s32)metric_register_can_frame_interval(const TLIBApplicationChannelType ABusType,const s32 AIdxChn,const u64 AFrameId);

TSAPI(s32)metric_unregister_can_frame_interval(const TLIBApplicationChannelType ABusType,const s32 AIdxChn,const u64 AFrameId);

TSAPI(s32)metric_get_w_reset_can_frame_interval_stat(const s32 AIdxChn,const u64 AFrameId,const PTSMetricIntegerSnapshot AIdxStat);

TSAPI(s32)metric_reset_can_frame_interval_stat(const s32 AIdxChn,const u64 AFrameId);

TSAPI(s32)metric_reset_frames_interval_stat_of_channel(const TLIBApplicationChannelType ABusType,const s32 AIdxChn);

TSAPI(s32)metric_reset_frames_interval_stat_of_bus(const TLIBApplicationChannelType ABusType);

TSAPI(s32)metric_reset_frames_interval_stat_of_all();

TSAPI(s32)tsai_config_sync(const s32 AChn,const double ASampleRate,const s32 ASampleBits,const s32 ATimeoutMs);

TSAPI(s32)tsao_config_sync(const s32 AChn,const s32 AEnableReport,const double ASampleRate,const s32 AOutputValue,const s32 ATimeoutMs);

TSAPI(s32)tsai_get_value_input_sync(const s32 AChnIdx,const ps32 AIOStatus,const s32 ATimeoutMs);

TSAPI(s32)tsao_set_value_output_async(const s32 AChnIdx,const s32 AIOStatus);

TSAPI(s32)call_system_api_w_serialized_args(const char* AAPIName,const char* ASeparator,const s32 AArgsCapacity,const char* AArgs);

TSAPI(s32)call_library_api_w_serialized_args(const char* AAPIName,const char* ASeparator,const s32 AArgsCapacity,const char* AArgs);

TSAPI(s32)rpc_tsmaster_call_system_api_w_serialized_args(const size_t AHandle,const char* AAPIName,const char* ASeparator,const s32 AArgsCapacity,const char* AArgs);

TSAPI(s32)rpc_tsmaster_call_library_api_w_serialized_args(const size_t AHandle,const char* AAPIName,const char* ASeparator,const s32 AArgsCapacity,const char* AArgs);

TSAPI(s32)can_set_load_balance_control(const s32 AIdxChn,const u8 AIsEnabled,const u32 ADelayUs,const s32 ATimeoutMS);

#if defined ( __cplusplus )
}
#endif
#pragma pack(pop)
#endif
