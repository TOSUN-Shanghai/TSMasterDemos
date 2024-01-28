#ifndef _TSMaster_H
#define _TSMaster_H

#include <math.h>
#include <stdio.h>
#include <cstring>

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
typedef float  single;
typedef float* psingle;
typedef double* pdouble;
typedef char* pchar;
typedef char** ppchar;
typedef void* TObject;
typedef void* pvoid;
typedef bool* pbool; 

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
    u8 FReserved;//
    s32 FIdentifier;//CAN identifier   = CAN
    s64 FTimeUs;//timestamp in us = CAN
    u8 FData[8];
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
}TLIBCAN, * PLIBCAN;

typedef struct _TLIBCANFD
{
    u8 FIdxChn;//channel index starting from 0
    u8 FProperties;//default 0, masked status:  = CAN [7] 0-normal frame, 1-error frame [6] 0-not logged, 1-already logged [5-3] tbd [2] 0-std frame, 1-extended frame [1] 0-data frame, 1-remote frame [0] dir: 0-RX, 1-TX
    u8 FDLC;//dlc from 0 to 15   = CAN
    u8 FFDProperties;//[7-3] tbd <> CAN  [2] ESI, The E RROR S TATE I NDICATOR (ESI) flag is transmitted dominant by error active nodes, recessive by error passive nodes. ESI does not exist in CAN format frames [1] BRS, If the bit is transmitted recessive, the bit rate is switched from the standard bit rate of the A RBITRATION P HASE to the preconfigured alternate bit rate of the D ATA P HASE . If it is transmitted dominant, the bit rate is not switched. BRS does not exist in CAN format frames. [0] EDL: 0-normal CAN frame, 1-FD frame, added 2020-02-12, The E XTENDED D ATA L ENGTH (EDL) bit is recessive. It only exists in CAN FD format frames
    s32 FIdentifier;//CAN identifier   = CAN
    s64 FTimeUs;//timestamp in us = CAN
    u8 FData[ 64] ;
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
}TLIBCANFD,*PLIBCANFD;


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
    u8 FData[ 8] ;
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
}TLIBLIN,*PLIBLIN;

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
    u8 FData[ 254] ;
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
}TLIBFlexRay,*PLIBFlexRay;

typedef struct _TLIBEthernetHeader
{
    u8 FIdxChn;//app channel index starting from 0 = Network index
    u8 FIdxSwitch;//Network's switch index
    u8 FIdxPort;// Network's switch's port index, 0~127: measurement port, 128~255: virtual port
    u8 FConfig;//  0-1: 0 = Rx, 1 = Tx, 2 = TxRq // 2: crc status, for tx, 0: crc is include in data, 1: crc is not include in data //                for rx, 0: crc is ok, 1: crc is not ok // 3: tx done type, 0: only report timestamp, 1: report full info(header+frame)
    u16 FEthernetPayloadLength;// Length of Ethernet payload data in bytes. Max. 1582 Byte(without Ethernet header), 1612 Byte(Inclusive ethernet header)
    u16 freserved;//Reserved
    u64 FTimeUs;//timestamp in us
    pu8 FEthernetDataAddr;//data ps32
    #ifdef _WIN32
    u32 FPadding;                // to be compatible with x64
    #endif
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
        freserved = 0;
        FTimeUs = 0;
        reset_data_pointer();
#ifdef _WIN32
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
        std:memcpy(ethernet_payload_addr(), ABuffer, l);
    }
    void set_ip_packet_payload_length(const u16 ALength){
        u16 o;
        if (!is_ip_frame()) return;
        has_vlans(&o);
        *(pu16)(FEthernetDataAddr + 16 + o) = SWAP_BYTES(ALength) + 20;
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
        *(FEthernetDataAddr + 0x26 + o) = SWAP_BYTES(ALength);
    }
    u16 get_udp_payload_length(){
        u16 o;
        if (!is_udp_frame()) return 0;
        has_vlans(&o);
        o = *(FEthernetDataAddr + 0x26 + o);
        return SWAP_BYTES(o);
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
            *AOffset = (SWAP_BYTES(*AOffset) and 0x1FFF) << 3;
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
}TLIBEthernetHeader,*PLIBEthernetHeader;typedef enum {
    APP_CAN = 0,
    APP_LIN = 1,
    APP_FlexRay = 2,
    APP_Ethernet = 3,
}TLIBApplicationChannelType;
typedef enum {
    stCANSignal = 0,
    stLINSignal = 1,
    stSystemVar = 2,
    stFlexRay = 3,
    stEthernet = 4,
}TSignalType;
typedef enum {
    trmRelativeMode = 0,
    trmTriggeredMode = 1,
    trmAbsoluteMode = 2,
}TTimeRangeTestMode;
typedef enum {
    tstCANSignal = 0,
    tstLINSignal = 1,
    tstSystemVar = 2,
    tstFlexRay = 3,
    tstExpression = 4,
} TTriggerSignalType;
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
}TSignalCheckKind;
typedef enum {
    sskMin = 0,
    sskMax = 1,
    sskAverage = 2,
    sskStdDeviation = 3,
}TSignalStatisticsKind;
typedef enum {
    fcmIdentical = 0,
    fcmLinear = 1,
    fcmScaleLinear = 2,
    fcmTextTable = 3,
    fcmTABNoIntp = 4,
    fcmFormula = 5,
}TFlexRayCompuMethod;
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
}TLIBCANBusStatistics;
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
}TLIBSystemVarType;
typedef enum {
    smdBiDirection = 0,
    smdSgnToSysVar = 1,
    smdSysVarToSgn = 2,
}TSymbolMappingDirection;
typedef enum {
    rppInit = 0,
    rppReplaying = 1,
    rppEnded = 2,
}TReplayPhase;
typedef enum {
    ortImmediately = 0,
    ortAsLog = 1,
    ortDelayed = 2,
}TLIBOnlineReplayTimingMode;
typedef enum {
    orsNotStarted = 0,
    orsRunning = 1,
    orsPaused = 2,
    orsCompleted = 3,
    orsTerminated = 4,
}TLIBOnlineReplayStatus;
typedef enum {
    rivUseDB = 0,
    rivUseLast = 1,
    rivUse0 = 2,
}TLIBRBSInitValueOptions;
typedef enum {
    sotCAN = 0,
    sotLIN = 1,
    sotCANFD = 2,
    sotRealtimeComment = 3,
    sotSystemVar = 4,
    sotFlexRay = 5,
}TSupportedObjType;
typedef enum {
    amrsNotRun = 0,
    amrsPrepareRun = 1,
    amrsRunning = 2,
    amrsPaused = 3,
    amrsStepping = 4,
    amrsFinished = 5,
}TLIBAutomationModuleRunningState;
typedef enum {
    lastCANSignal = 0,
    lastLINSignal = 1,
    lastSysVar = 2,
    lastLocalVar = 3,
    lastConst = 4,
    lastFlexRaySignal = 5,
    lastImmediateValue = 6,
    lastUnknown = 7,
}TLIBAutomationSignalType ;
typedef enum {
    lmfsSystemFunc = 0,
    lmfsMPLIB = 1,
    lmfsInternal = 2,
} TLIBMPFuncSource ;
typedef enum {
    lvtInteger = 0,
    lvtDouble = 1,
    lvtString = 2,
    lvtCANMsg = 3,
    lvtCANFDMsg = 4,
    lvtLINMsg = 5,
    lvtUnknown = 6,
}TLIBSimVarType;
typedef enum {
    sssStopped = 0,
    sssRunning = 1,
    sssPaused = 2,
}TSTIMSignalStatus;
typedef enum {
    lfdtCAN = 0,
    lfdtISOCAN = 1,
    lfdtNonISOCAN = 2,
}TLIBCANFDControllerType;
typedef enum {
    lfdmNormal = 0,
    lfdmACKOff = 1,
    lfdmRestricted = 2,
    lfdmInternalLoopback = 3,
    lfdmExternalLoopback = 4,
}TLIBCANFDControllerMode;
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
}TLIB_TS_Device_Sub_Type;
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
}TLIB_XL_Device_Sub_Type;
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
    BUS_DEV_TYPE_COUNT = 12,
}TLIBBusToolDeviceType;
typedef enum {
    T_MasterNode = 0,
    T_SlaveNode = 1,
    T_MonitorNode = 2,
}TLINNodeType;
typedef enum {
    LIN_PROTOCL_13 = 0,
    LIN_PROTOCL_20 = 1,
    LIN_PROTOCL_21 = 2,
    LIN_PROTOCL_J2602 = 3,
}TLINProtocol;

typedef struct _TLIBFlexRayClusterParameters
{
    char FShortName[ 32] ;
    char FLongName[ 32] ;
    char FDescription[ 32] ;
    char FSpeed[ 32] ;
    char  FChannels[ 32] ;
    char FBitCountingPolicy[ 32] ;
    char FProtocol[ 32] ;
    char FProtocolVersion[ 32] ;
    char FMedium[ 32] ;
    s32 FIsHighLowBitOrder;//
    s32 FMaxFrameLengthByte;//
    s32 FNumberOfCycles;//cycle parameters
    s32 FCycle_us;//
    double FBit_us;//
    double FSampleClockPeriod_us;//
    double  FMacrotick_us;//
    s32 FMacroPerCycle;//
    s32 FNumberOfStaticSlots;//
    s32 FStaticSlot_MT;//
    s32 FActionPointOffset_MT;//
    s32 FTSSTransmitter_gdBit;//
    s32 FPayloadLengthStatic_WORD;//
    s32 FNumberOfMiniSlots;//
    s32 FMiniSlot_MT;//
    s32 FMiniSlotActionPointOffset_MT;//
    s32 FDynamicSlotIdlePhase_MiniSlots;//
    s32  FSymbolWindow_MT;//
    s32 FNIT_MT;//
    s32 FSyncNodeMax;//
    s32 FNetworkManagementVectorLength;//Wakeup and startup parameters
    s32 FListenNoise;//
    s32 FColdStartAttempts;//
    s32 FCASRxLowMax_gdBit;//
    s32 FWakeupSymbolRxIdle_gdBit;//
    s32 FWakeupSymbolRxLow_gdBit;//
    s32  FWakeupSymbolRxWindow_gdBit;//
    s32 FWakeupSymbolTxIdle_gdBit;//
    s32 FWakeupSymbolTxLow_gdBit;//
    double FMaxInitializationError_us;//clock correction parameters
    s32 FClusterDriftDamping_uT;//
    s32 FOffsetCorrectionStart_MT;//
    s32 FMaxWithoutClockCorrectionFatal;//
    s32 FMaxWithoutClockCorrectionPassive;//
}TLIBFlexRayClusterParameters,*PLIBFlexRayClusterParameters;

typedef struct _TLIBFlexRayControllerParameters
{
    char FShortName[ 32] ;
    char FConnectedChannels[ 32] ;
    s32 FMicroPerCycle_uT;//
    s32 FMicroPerMacroNom_uT;//
    double FMicroTick_us;//
    s32 FSamplesPerMicrotick;//wakeup & startup parameters
    s32  FWakeupChannelA;//
    s32  FWakeupChannelB;//
    s32  FMaxDrift_uT;//
    s32  FWakeupPattern;//
    s32  FListenTimeout_uT;//
    s32  FAcceptedStartupRange_uT;//
    s32  FMacroInitialOffsetA_MT;//
    s32  FMacroInitialOffsetB_MT;//
    s32  FMacroInitialOffsetA_uT;//
    s32  FMacroInitialOffsetB_uT;//clock correction parameters
    char  FKeySlotUsage[ 32] ;
    s32  FKeySlotID;//
    s32  FsingleSlotEnabled;//
    s32  FClusterDriftDamping_uT;//
    s32  FDocodingCorrection_uT;//
    s32  FDelayCompensationA_uT;//
    s32  FDelayCompensationB_uT;//
    s32  FOffsetCorrectionOut_uT;//
    s32  FExternRateCorrection_uT;//
    s32  FRateCorrectionOut_uT;//
    s32  FExternOffsetCorrection_uT;//
    s32  FAllowHaltDueToClock;//
    s32  FAllowPassivToActive;//latesttx
    s32  FLatestTx;//
    s32  FMaxDynamicPayloadLength;//
}TLIBFlexRayControllerParameters,*PLIBFlexRayControllerParameters;

typedef struct _TLIBEthernetMAX
{
    TLIBEthernetHeader FHeader;//
    u8 FBytes[ 1612] ;
}TLIBEthernetMAX,*PLIBEthernetMAX;

typedef struct _TLIBFlexray_controller_config
{
    u8 NETWORK_MANAGEMENT_VECTOR_LENGTH;//
    u8 PAYLOAD_LENGTH_STATIC;//
    u16 FReserved;//
    u16 LATEST_TX;//__ prtc1Control
    u16 T_S_S_TRANSMITTER;//
    u8 CAS_RX_LOW_MAX;//
    u8 SPEED;//0 for 10m, 1 for 5m, 2 for 2.5m, convert from Database
    u16 WAKE_UP_SYMBOL_RX_WINDOW;//
    u8 WAKE_UP_PATTERN;//__ prtc2Control
    u8 WAKE_UP_SYMBOL_RX_IDLE;//
    u8 WAKE_UP_SYMBOL_RX_LOW;//
    u8 WAKE_UP_SYMBOL_TX_IDLE;//
    u8 WAKE_UP_SYMBOL_TX_LOW;//__ succ1Config
    u8 channelAConnectedNode;//Enable ChannelA: 0: Disable 1: Enable
    u8 channelBConnectedNode;//Enable ChannelB: 0: Disable 1: Enable
    u8 channelASymbolTransmitted;//Enable Symble Transmit function of Channel A: 0: Disable 1: Enable
    u8 channelBSymbolTransmitted;//Enable Symble Transmit function of Channel B: 0: Disable 1: Enable
    u8 ALLOW_HALT_DUE_TO_CLOCK;//
    u8 single_SLOT_ENABLED;//FALSE_0, TRUE_1
    u8 wake_up_idx;//Wake up channe: 0:ChannelA， 1:ChannelB
    u8 ALLOW_PASSIVE_TO_ACTIVE;//
    u8 COLD_START_ATTEMPTS;//
    u8 synchFrameTransmitted;//Need to transmit sync frame
    u8 startupFrameTransmitted;//Need to transmit startup frame // __ succ2Config
    u32 LISTEN_TIMEOUT;//
    u8 LISTEN_NOISE;//2_16 __ succ3Config
    u8 MAX_WITHOUT_CLOCK_CORRECTION_PASSIVE;//
    u8 MAX_WITHOUT_CLOCK_CORRECTION_FATAL;//
    u8 REVERS0;//Memory Align // __ gtuConfig //__ gtu01Config
    u32 MICRO_PER_CYCLE;//__ gtu02Config
    u16 Macro_Per_Cycle;//
    u8 SYNC_NODE_MAX;//
    u8 REVERS1;//Memory Align //__ gtu03Config
    u8 MICRO_INITIAL_OFFSET_A;//
    u8 MICRO_INITIAL_OFFSET_B;//
    u8 MACRO_INITIAL_OFFSET_A;//
    u8 MACRO_INITIAL_OFFSET_B;//__ gtu04Config
    u16 N_I_T;//
    u16 OFFSET_CORRECTION_START;//__ gtu05Config
    u8 DELAY_COMPENSATION_A;//
    u8 DELAY_COMPENSATION_B;//
    u8 CLUSTER_DRIFT_DAMPING;//
    u8 DECODING_CORRECTION;//__ gtu06Config
    u16 ACCEPTED_STARTUP_RANGE;//
    u16 MAX_DRIFT;//__ gtu07Config
    u16 STATIC_SLOT;//
    u16 NUMBER_OF_STATIC_SLOTS;//__ gtu08Config
    u8 MINISLOT;//
    u8 REVERS2;//Memory Align
    u16 NUMBER_OF_MINISLOTS;//__ gtu09Config
    u8 DYNAMIC_SLOT_IDLE_PHASE;//
    u8 ACTION_POINT_OFFSET;//
    u8 MINISLOT_ACTION_POINT_OFFSET;//
    u8 REVERS3;//Memory Align __ gtu10Config
    u16 OFFSET_CORRECTION_OUT;//
    u16 RATE_CORRECTION_OUT;//__ gtu11Config
    u8 EXTERN_OFFSET_CORRECTION;//
    u8 EXTERN_RATE_CORRECTION;//
    u8 REVERS4;//Memory Align
    u8 config_byte;//Memory Align //bit0: 1：启用cha上终端电阻  0：不启用 //bit1: 1：启用chb上终端电阻  0：不启用 //bit2: 1：启用接收FIFO    0：不启用 //bit4: 1：cha桥接使能             0：不使能 //bit5: 1：chb桥接使能             0：不使能
}TLIBFlexray_controller_config,*PLIBFlexray_controller_config;

typedef struct _TLIBTrigger_def
{
    u8 frame_idx;//
    u8 slot_id;//
    u8 cycle_code;//BASE-CYCLE + CYCLE-REPETITION
    u8 config_byte;////bit 0:是否使能通道A//bit 1:是否使能通道B//bit 2:是否网络管理报文//bit 3:传输模式，0表示连续传输，1表示单次触发//bit 4:是否为冷启动报文，只有缓冲区0可以置1//bit 5:是否为同步报文，只有缓冲区0/1可以置1//bit 6://bit 7:帧类型：0-静态，1-动态
}TLIBTrigger_def,*PLIBTrigger_def;

typedef struct _TLIBGPSData
{
    u64 FTimeUS;//timestamp in us
    u32 UTCTime;//
    u32 UTCDate;//
    single Latitude;//
    single Longitude;//
    single Speed;//
    single Direct;//
    single Altitude;//
    u8 N_S;//
    u8 E_W;//
    u8 Satellite;//
    u8 FIdxChn;//
}TLIBGPSData,*PLIBGPSData;

typedef struct _TLIBEth_CMD_config
{
    u8 eth_config0;////bit 0-1 phy_type:2; //0: 100base-Tx/1000Base-T, 1: 100/1000Base-T1, 2,3: rev//bit2 auto_neg : 1;//bit3-4: speed : 2; //0-10mbps, 1-100mbps, 2-1000mbps//bit5: is_master : 1;//bit6-7 loop : 2;//0: no loop, 1: mac_loop, 2: phy-loop, 3: phy_remote loop
    u8 eth_config1;////bit0 wakeup : 1;//0-disable, 1-enable//bit1-4 test_mode : 4;//  0x00 normal operation  other test mode//bit5-6 tx_mode : 2;//  0x00 enable 0x01 disable//bit7  enable : 1;
    u8 eth_config2;////bit0-4 phy_addr : 5;//bit5 accept wrong crc frame:1
    u8 eth_config3;////bit0: disable_promiscuous_mode//bit1: enable_recieve_all//bit2-3: enable_srouce_fileter: 0 disable 1: enable 2 inverse//bit4: inverse_dest_fileter//bit5-6: ControlFrames: 0: block all  1: forward all  2: forward by filter//bit7: enable rx broadcast frame
    u8 filter_config0;////bit0-1: multicast frame filter: 0: no filter  1: perfect 2: hash 3: hash and perfect//bit2-3: unicast frame filter: 0: perfect 1: hash 2: hash and perfect
    u8 filter_config1;//
    u64 filter_hash_table;////bit0-47: mac addr For example, if 0x112233445566 is received//          (0x11 in lane 0 of the first column) on the MII as the destination address, then the//          MacAddress0 Register [47:0] is compared with 0x665544332211//          perfect0 is always enable
    u64 filter_perfect0;////bit63: AE: Address Enable, When this bit is set, the address filter module uses the second MAC address for perfect//          filtering. When this bit is reset, the address filter module ignores the address for filtering.//bit62: SA: Source Address://          When this bit is set, the MAC Address1[47:0] is used to compare with the SA fields of the//          received packet. When this bit is reset, the MAC Address x[47:0] is used to compare with the//          DA fields of the received packet.//bit56-61: MBC[5:0]: Mask Byte Control//          These bits are mask control bits for comparing each of the MAC Address bytes. When set//          high, the MAC does not compare the corresponding byte of received DA or SA with the//          contents of MAC Address1 registers. Each bit controls the masking of the bytes as follows://          Bit 29: Register 194[15:8]//          Bit 28: Register 194[7:0]//          Bit 27: Register 195[31:24]//          ..//          Bit 24: Register 195[7:0]//          You can filter a group of addresses (known as group address filtering) by masking one or//          more bytes of the address.//bit0-47:  same as filter_perfect0
    u64 filter_perfect1;//
    u64 rev[ 6] ;
}TLIBEth_CMD_config,*PLIBEth_CMD_config;

typedef struct _Trealtime_comment_t
{
    s64 FTimeUs;//
    s32 FEventType;//
    s32 FCapacity;//
    pchar FComment;//
    u32 FPadding;//to be compatible with x64
}Trealtime_comment_t,*Prealtime_comment_t;

typedef struct _TLIBSystemVar
{
    s64 FTimeUs;//
    s32 FType;//
    u32 FNameCapacity;//
    u32 FDataCapacity;//
    pchar FName;//
    pu8 FData;//
    s64 FPadding;//to be compatible with x64
}TLIBSystemVar,*PLIBSystemVar;

typedef struct _TMPCANSignal
{
    u8 FCANSgnType;//0 - Unsigned, 1 - Signed, 2 - single 32, 3 - Double 64
    bool FIsIntel;//
    s32 FStartBit;//
    s32 FLength;//
    double FFactor;//
    double FOffset;//
}TMPCANSignal,*PMPCANSignal;

typedef struct _TMPLINSignal
{
    u8 FLINSgnType;//0 - Unsigned, 1 - Signed, 2 - single 32, 3 - Double 64
    bool FIsIntel;//
    s32 FStartBit;//
    s32 FLength;//
    double FFactor;//
    double FOffset;//
}TMPLINSignal,*PMPLINSignal;

typedef struct _TMPFlexRaySignal
{
    u8 FFRSgnType;//0 - Unsigned, 1 - Signed, 2 - single 32, 3 - Double 64
    u8 FCompuMethod;//0 - Identical, 1 - Linear, 2 - Scale Linear, 3 - TextTable, 4 - TABNoIntp, 5 - Formula
    u8 FReserved;//
    bool FIsIntel;//
    s32 FStartBit;//
    s32 FUpdateBit;//
    s32 FLength;//
    double FFactor;//
    double FOffset;//
    s32 FActualStartBit;//added 2023-07-18
    s32 FActualUpdateBit;//added 2023-07-18
}TMPFlexRaySignal,*PMPFlexRaySignal;

typedef struct _TMPDBProperties
{
    s32 FDBIndex;//
    s32 FSignalCount;//
    s32 FFrameCount;//
    s32 FECUCount;//
    u64 FSupportedChannelMask;//
    char FName[ 512] ;
    char FComment[ 512] ;
    u64 FFlags;//Bit 0: whether generate mp header
}TMPDBProperties,*PMPDBProperties;

typedef struct _TMPDBECUProperties
{
    s32 FDBIndex;//
    s32 FECUIndex;//
    s32 FTxFrameCount;//
    s32 FRxFrameCount;//
    char FName[ 512] ;
    char FComment[ 512] ;
}TMPDBECUProperties,*PMPDBECUProperties;

typedef struct _TMPDBFrameProperties
{
    s32 FDBIndex;//
    s32 FECUIndex;//
    s32 FFrameIndex;//
    u8 FIsTx;//
    u8 FReserved1;//
    u16 FCycleTimeMs;//
    s32 FFrameType;//
    u8 FCANIsDataFrame;//
    u8 FCANIsStdFrame;//
    u8 FCANIsEdl;//
    u8 FCANIsBrs;//
    s32 FCANIdentifier;//
    s32 FCANDLC;//
    s32 FCANDataBytes;//
    s32 FLINIdentifier;//
    s32 FLINDLC;//
    u8 FFRChannelMask;//
    u8 FFRBaseCycle;//
    u8 FFRCycleRepetition;//
    u8 FFRIsStartupFrame;//
    u16 FFRSlotId;//
    u16 FFRDLC;//
    u64 FFRCycleMask;//
    s32 FSignalCount;//
    char FName[ 512] ;
    char FComment[ 512] ;
}TMPDBFrameProperties,*PMPDBFrameProperties;

typedef struct _TMPDBSignalProperties
{
    s32 FDBIndex;//
    s32 FECUIndex;//
    s32 FFrameIndex;//
    s32 FSignalIndex;//
    u8 FIsTx;//
    u8 FReserved1;//
    u8 FReserved2;//
    u8 FReserved3;//
    s32 FSignalType;//
    TMPCANSignal FCANSignal;//
    TMPLINSignal FLINSignal;//
    TMPFlexRaySignal FFlexRaySignal;//
    s32 FParentFrameId;//
    double FInitValue;//
    char FName[ 512] ;
    char FComment[ 512] ;
}TMPDBSignalProperties,*PMPDBSignalProperties;

typedef struct _TLIBHWInfo
{
    s32 FDeviceType;//
    s32 FDeviceIndex;//
    char FVendorName[ 32] ;
    char FDeviceName[ 32] ;
    char FSerialString[ 64] ;
}TLIBHWInfo,*PLIBHWInfo;

typedef struct _TLIBTSMapping
{
    char FAppName[ 32] ;
    s32 FAppChannelIndex;//
    s32 FAppChannelType;//
    s32 FHWDeviceType;//
    s32 FHWIndex;//
    s32 FHWChannelIndex;//
    s32 FHWDeviceSubType;//
    char FHWDeviceName[ 32] ;
    bool FMappingDisabled;//
}TLIBTSMapping,*PLIBTSMapping;

typedef struct _TLIBSystemVarDef
{
    char FName[ 32] ;
    char FCategory[ 32] ;
    char FComment[ 32] ;
    s32 FDataType;//
    bool FIsReadOnly;//
    double FValueMin;//
    double FValueMax;//
    char FUnit[ 32] ;
}TLIBSystemVarDef,*PLIBSystemVarDef;

typedef struct _Tip4_addr_t
{
    u32 addr;//
}Tip4_addr_t,*Pip4_addr_t;

typedef struct _Tip6_addr_t
{
    u32 addr[ 4] ;
    u8 zone;//
}Tip6_addr_t,*Pip6_addr_t;

typedef struct _Tts_sockaddr
{
    u8 sa_len;//
    u8 sa_family;//
    char sa_data[ 14] ;
}Tts_sockaddr,*Pts_sockaddr;

typedef struct _Tts_iovec
{
    TObject iov_base;//
    size_t iov_len;//
}Tts_iovec,*Pts_iovec;

typedef struct _Tts_msghdr
{
    TObject msg_name;//
    u32 msg_namelen;//
    Pts_iovec msg_iov;//
    s32 msg_iovlen;//
    TObject msg_control;//
    u32 msg_controllen;//
    s32 msg_flags;//
}Tts_msghdr,*Pts_msghdr;

typedef struct _Tts_fd_set
{
    u8 fd_bits[ 2] ;
}Tts_fd_set,*Pts_fd_set;

typedef struct _Tts_timeval
{
    u32 tv_sec;//
    u32 tv_usec;//
}Tts_timeval,*Pts_timeval;

typedef struct _Tts_pollfd
{
    s32 fd;//
    s16 events;//
    s16 revents;//
}Tts_pollfd,*Pts_pollfd;

typedef struct _Tts_sockaddr_in
{
    u8 sin_len;//
    u8 sin_family;//
    u16 sin_port;//
    Tip4_addr_t sin_addr;//
    u8 sin_zero[ 8] ;
}Tts_sockaddr_in,*Pts_sockaddr_in;

typedef struct _Tip_addr_t
{
    Tip6_addr_t ip4Or6;//
    u32 FType;//
}Tip_addr_t,*Pip_addr_t;

typedef double(__stdcall*TCANQueueEvent_API)(const PLIBCAN AData);
typedef double(__stdcall*TGPSQueueEvent_Win32)(const ps32 AObj,const PLIBGPSData AData);
typedef double(__stdcall*TCANQueueEvent_Win32)(const ps32 AObj,const PLIBCAN AData);
typedef double(__stdcall*TCANFDQueueEvent_Win32)(const ps32 AObj,const PLIBCANFD AData);
typedef double(__stdcall*TFlexRayQueueEvent_Win32)(const ps32 AObj,const PLIBFlexRay AData);
typedef double(__stdcall*TEthernetQueueEvent_Win32)(const ps32 AObj,const PLIBEthernetHeader AData);
typedef double(__stdcall*TLINQueueEvent_Win32)(const ps32 AObj,const PLIBLIN AData);
typedef double(__stdcall*TLIBTSMasterLogger)(const pchar AStr,const s32 ALevel);
typedef double(__stdcall*TFirmwareUpdateCallback)(const TObject AOpaque,const u32 AStatus,const single APercentage100);
typedef double(__stdcall*TOnIoIPData)(const ps32 Aps32,const s32 ASize);
typedef double(__stdcall*TOnIoIPData_API)(const ps32 Aps32,const s32 ASize);
typedef double(__stdcall*TOnIoIPConnection)(const pchar AIPAddress,const s32 APort);
typedef double(__stdcall*TOnIoIPConnection_API)(const pchar AIPAddress,const s32 APort);
typedef double(__stdcall*TLIBWriteAPIDocumentFunc)(const ps32 AObj,const pchar AName,const pchar AGroup,const pchar ADesc,const pchar AExample,const s32 AParaCount);
typedef double(__stdcall*TLIBWriteAPIParaFunc)(const ps32 AObj,const s32 AIdx,const pchar AAPIName,const pchar AParaName,const bool AIsConst,const pchar AParaType,const pchar ADesc);
typedef double(__stdcall*TLIBWriteAPIDocument)(const ps32 AObj,const TLIBWriteAPIDocumentFunc AWriteDoc,const TLIBWriteAPIParaFunc AWritePara);
typedef double(__stdcall*TLIBOnSysVarChange)(const pchar ACompleteName);
typedef double(__stdcall*TReadProgressCallback)(const ps32 AObj,const double AProgress100);
typedef double(__stdcall*N_USData_TranslateCompleted_Recall)(const s32 ATpModuleIndex,const s32 AChn,const u64 ATimeStamp,const pu8 APayLoad,const u32 ASize,const s32 AError);
typedef double(__stdcall*N_USData_TranslateCompleted_Recall_Obj)(const s32 ATpModuleIndex,const s32 AChn,const u8 ABusType,const s32 ANAD,const s32 AIdentifier,const u64 ATimeStamp,const pu8 APayLoad,const u32 ASize,const s32 AError);
typedef double(__stdcall*TLogDebuggingInfo)(const pchar AMsg,const s32 ALevel);
typedef double(__stdcall*tosun_recv_callback)(const s32 sock,const ps32 p,const u16 len);
typedef double(__stdcall*tosun_tcp_presend_callback)(const s32 sock,const ps32 p,const Pip_addr_t src,const Pip_addr_t dest,const u8 ttl,const u8 tos);
typedef double(__stdcall*tosun_tcp_ack_callback)(const s32 sock,const ps32 p,const u16 len);
#if defined ( __cplusplus )
extern  "C" 
{
#endif
//arg[0] AFilePath : None
TSAPI(s32) set_libtsmaster_location(const char*  AFilePath);
//arg[0] AFilePath : None
TSAPI(s32) get_libtsmaster_location(const ppchar AFilePath);
//arg[0] AAppName : None
TSAPI(s32) initialize_lib_tsmaster(const char*  AAppName);
//arg[0] AAppName : None
//arg[1] AProjectFileName : None
TSAPI(s32) initialize_lib_tsmaster_with_project(const char*  AAppName,const char*  AProjectFileName);
//arg[0] ALogger : None
TSAPI(s32) tsapp_set_logger(const TLIBTSMasterLogger ALogger);
//arg[0] AStr : output string
//arg[1] ALevel : output level
TSAPI(s32) tsapp_log(const char*  AStr,const s32 ALevel);
//arg[0] AAppName : APP name
TSAPI(s32) tsapp_set_current_application(const char*  AAppName);
//arg[0] AAppName : APP name
TSAPI(s32) tsapp_get_current_application(const ppchar AAppName);
//arg[0] AAppName : APP name
TSAPI(s32) tsapp_del_application(const char*  AAppName);
//arg[0] AAppName : APP name
TSAPI(s32) tsapp_add_application(const char*  AAppName);
//arg[0] AAppNameList : None
TSAPI(s32) tsapp_get_application_list(const ppchar AAppNameList);
//arg[0] ACount : None
TSAPI(s32) tsapp_set_can_channel_count(const s32 ACount);
//arg[0] ACount : None
TSAPI(s32) tsapp_set_lin_channel_count(const s32 ACount);
//arg[0] ACount : None
TSAPI(s32) tsapp_set_flexray_channel_count(const s32 ACount);
//arg[0] ACount : None
TSAPI(s32) tsapp_get_can_channel_count(const ps32 ACount);
//arg[0] ACount : None
TSAPI(s32) tsapp_get_lin_channel_count(const ps32 ACount);
//arg[0] ACount : None
TSAPI(s32) tsapp_get_flexray_channel_count(const ps32 ACount);
//arg[0] AMapping : None
TSAPI(s32) tsapp_set_mapping(const PLIBTSMapping AMapping);
//arg[0] AAppName : None
//arg[1] AAppChannelType : None
//arg[2] AAppChannel : APP_CHANNEL
//arg[3] AHardwareName : None
//arg[4] AHardwareType : None
//arg[5] AHardwareSubType : None
//arg[6] AHardwareIndex : None
//arg[7] AHardwareChannel : HARDWARE_CHANNEL
//arg[8] AEnableMapping : None
TSAPI(s32) tsapp_set_mapping_verbose(const char*  AAppName,const s32 AAppChannelType,const s32 AAppChannel,const char*  AHardwareName,const s32 AHardwareType,const s32 AHardwareSubType,const s32 AHardwareIndex,const s32 AHardwareChannel,const bool AEnableMapping);
//arg[0] AMapping : None
TSAPI(s32) tsapp_get_mapping(const PLIBTSMapping AMapping);
//arg[0] AMapping : None
TSAPI(s32) tsapp_del_mapping(const PLIBTSMapping AMapping);
//arg[0] AAppName : None
//arg[1] AAppChannelType : None
//arg[2] AAppChannel : None
TSAPI(s32) tsapp_del_mapping_verbose(const char*  AAppName,const s32 AAppChannelType,const s32 AAppChannel);
TSAPI(s32) tsapp_connect();
TSAPI(s32) tsapp_disconnect();
//arg[0] AEnable : None
TSAPI(s32) tsapp_set_turbo_mode(const bool AEnable);
//arg[0] AEnable : None
TSAPI(s32) tsapp_get_turbo_mode(const pbool AEnable);
//arg[0] ACode : None
//arg[1] ADesc : None
TSAPI(s32) tsapp_get_error_description(const s32 ACode,const ppchar ADesc);
TSAPI(s32) tsapp_show_channel_mapping_window();
TSAPI(s32) tsapp_show_hardware_configuration_window();
//arg[0] AWindowName : None
//arg[1] AWaitClose : None
TSAPI(s32) tsapp_show_tsmaster_window(const char*  AWindowName,const bool AWaitClose);
//arg[0] ATimeUs : None
TSAPI(s32) tsapp_get_timestamp(const ps64 ATimeUs);
//arg[0] AString : None
//arg[1] AArguments : None
//arg[2] ASync : None
//arg[3] AIsX64 : None
//arg[4] AResultLog : None
TSAPI(s32) tsapp_execute_python_string(const char*  AString,const char*  AArguments,const bool ASync,const bool AIsX64,const ppchar AResultLog);
//arg[0] AFilePath : None
//arg[1] AArguments : None
//arg[2] ASync : None
//arg[3] AIsX64 : None
//arg[4] AResultLog : None
TSAPI(s32) tsapp_execute_python_script(const char*  AFilePath,const char*  AArguments,const bool ASync,const bool AIsX64,const ppchar AResultLog);
//arg[0] AYear : None
//arg[1] AMonth : None
//arg[2] ADay : None
//arg[3] ABuildNumber : None
TSAPI(s32) tsapp_get_tsmaster_version(const ps32 AYear,const ps32 AMonth,const ps32 ADay,const ps32 ABuildNumber);
//arg[0] AIdxType : None
//arg[1] ACount : None
TSAPI(s32) tsapp_get_system_constant_count(const s32 AIdxType,const ps32 ACount);
//arg[0] AIdxType : None
//arg[1] AIdxValue : None
//arg[2] AName : None
//arg[3] AValue : None
//arg[4] ADesc : None
TSAPI(s32) tsapp_get_system_constant_value_by_index(const s32 AIdxType,const s32 AIdxValue,const ppchar AName,const pdouble AValue,const ppchar ADesc);
//arg[0] ACount : None
TSAPI(s32) tsapp_enumerate_hw_devices(const ps32 ACount);
//arg[0] AIndex : None
//arg[1] AHWInfo : None
TSAPI(s32) tsapp_get_hw_info_by_index(const s32 AIndex,const PLIBHWInfo AHWInfo);
//arg[0] AIndex : None
//arg[1] ADeviceType : None
//arg[2] AVendorNameBuffer : array[0..31] of AnsiChar;
//arg[3] AVendorNameBufferSize : None
//arg[4] ADeviceNameBuffer : array[0..31] of AnsiChar;
//arg[5] ADeviceNameBufferSize : None
//arg[6] ASerialStringBuffer : array[0..63] of AnsiChar;
//arg[7] ASerialStringBufferSize : None
TSAPI(s32) tsapp_get_hw_info_by_index_verbose(const s32 AIndex,const ps32 ADeviceType,const char*  AVendorNameBuffer,const s32 AVendorNameBufferSize,const char*  ADeviceNameBuffer,const s32 ADeviceNameBufferSize,const char*  ASerialStringBuffer,const s32 ASerialStringBufferSize);
//arg[0] AScanTOSUN : None
//arg[1] AScanVector : None
//arg[2] AScanPeak : None
//arg[3] AScanKvaser : None
//arg[4] AScanZLG : None
//arg[5] ADetectIntrepidcs : None
//arg[6] ADetectCANable : None
TSAPI(s32) tsapp_set_vendor_detect_preferences(const bool AScanTOSUN,const bool AScanVector,const bool AScanPeak,const bool AScanKvaser,const bool AScanZLG,const bool ADetectIntrepidcs,const bool ADetectCANable);
//arg[0] AScanTOSUN : None
//arg[1] AScanVector : None
//arg[2] AScanPeak : None
//arg[3] AScanKvaser : None
//arg[4] AScanZLG : None
//arg[5] ADetectIntrepidcs : None
//arg[6] ADetectCANable : None
TSAPI(s32) tsapp_get_vendor_detect_preferences(const bool AScanTOSUN,const bool AScanVector,const bool AScanPeak,const bool AScanKvaser,const bool AScanZLG,const bool ADetectIntrepidcs,const bool ADetectCANable);
//arg[0] AIndex : None
//arg[1] ABaudrateKbps : None
//arg[2] AProtocol : None
TSAPI(s32) tsapp_configure_baudrate_lin(const s32 AIndex,const single ABaudrateKbps,const s32 AProtocol);
//arg[0] AIndex : None
//arg[1] ABaudrateKbps : None
//arg[2] AListenOnly : None
//arg[3] AInstallTermResistor120Ohm : None
TSAPI(s32) tsapp_configure_baudrate_can(const s32 AIndex,const single ABaudrateKbps,const bool AListenOnly,const bool AInstallTermResistor120Ohm);
//arg[0] AIndex : None
//arg[1] AArbRateKbps : None
//arg[2] ADataRateKbps : None
//arg[3] AControllerType : None
//arg[4] AControllerMode : None
//arg[5] AInstallTermResistor120Ohm : None
TSAPI(s32) tsapp_configure_baudrate_canfd(const s32 AIndex,const single AArbRateKbps,const single ADataRateKbps,const s32 AControllerType,const s32 AControllerMode,const bool AInstallTermResistor120Ohm);
//arg[0] AIndex : None
//arg[1] ABaudrateKbps : None
//arg[2] ASEG1 : None
//arg[3] ASEG2 : None
//arg[4] APrescaler : None
//arg[5] ASJW : None
//arg[6] AOnlyListen : None
//arg[7] A120OhmConnected : None
TSAPI(s32) tsapp_configure_can_regs(const s32 AIndex,const single ABaudrateKbps,const s32 ASEG1,const s32 ASEG2,const s32 APrescaler,const s32 ASJW,const s32 AOnlyListen,const s32 A120OhmConnected);
//arg[0] AIndex : None
//arg[1] AArbBaudrate : None
//arg[2] AArbSEG1 : None
//arg[3] AArbSEG2 : None
//arg[4] AArbPrescaler : None
//arg[5] AArbSJW : None
//arg[6] ADataBaudrate : None
//arg[7] ADataSEG1 : None
//arg[8] ADataSEG2 : None
//arg[9] ADataPrescaler : None
//arg[10] ADataSJW : None
//arg[11] AControllerType : None
//arg[12] AControllerMode : None
//arg[13] A120OhmConnected : None
TSAPI(s32) tsapp_configure_canfd_regs(const s32 AIndex,const single AArbBaudrate,const s32 AArbSEG1,const s32 AArbSEG2,const s32 AArbPrescaler,const s32 AArbSJW,const single ADataBaudrate,const s32 ADataSEG1,const s32 ADataSEG2,const s32 ADataPrescaler,const s32 ADataSJW,const s32 AControllerType,const s32 AControllerMode,const s32 A120OhmConnected);
//arg[0] ACAN : None
TSAPI(s32) tsapp_transmit_can_async(const PLIBCAN ACAN);
//arg[0] ACANFD : None
TSAPI(s32) tsapp_transmit_canfd_async(const PLIBCANFD ACANFD);
//arg[0] ALIN : None
TSAPI(s32) tsapp_transmit_lin_async(const PLIBLIN ALIN);
//arg[0] ALIN : None
TSAPI(s32) tsapp_transmit_fastlin_async(const PLIBLIN ALIN);
//arg[0] AIdxChn : None
//arg[1] AWakeupLength : None
//arg[2] AWakeupIntervalTime : None
//arg[3] AWakeupTimes : None
TSAPI(s32) tsapp_transmit_lin_wakeup_async(const s32 AIdxChn,const s32 AWakeupLength,const s32 AWakeupIntervalTime,const s32 AWakeupTimes);
//arg[0] AIdxChn : None
TSAPI(s32) tsapp_transmit_lin_gotosleep_async(const s32 AIdxChn);
//arg[0] ACAN : None
//arg[1] ATimeoutMS : None
TSAPI(s32) tsapp_transmit_can_sync(const PLIBCAN ACAN,const s32 ATimeoutMS);
//arg[0] ACANfd : None
//arg[1] ATimeoutMS : None
TSAPI(s32) tsapp_transmit_canfd_sync(const PLIBCANFD ACANfd,const s32 ATimeoutMS);
//arg[0] ALIN : None
//arg[1] ATimeoutMS : None
TSAPI(s32) tsapp_transmit_lin_sync(const PLIBLIN ALIN,const s32 ATimeoutMS);
TSAPI(s32) tsfifo_enable_receive_fifo();
TSAPI(s32) tsfifo_disable_receive_fifo();
//arg[0] AIdxChn : None
//arg[1] AIdentifier : None
//arg[2] AIsStd : None
TSAPI(s32) tsfifo_add_can_canfd_pass_filter(const s32 AIdxChn,const s32 AIdentifier,const bool AIsStd);
//arg[0] AIdxChn : None
//arg[1] AIdentifier : None
TSAPI(s32) tsfifo_add_lin_pass_filter(const s32 AIdxChn,const s32 AIdentifier);
//arg[0] AIdxChn : None
//arg[1] AIdentifier : None
TSAPI(s32) tsfifo_delete_can_canfd_pass_filter(const s32 AIdxChn,const s32 AIdentifier);
//arg[0] AIdxChn : None
//arg[1] AIdentifier : None
TSAPI(s32) tsfifo_delete_lin_pass_filter(const s32 AIdxChn,const s32 AIdentifier);
//arg[0] ACANBuffers : None
//arg[1] ACANBufferSize : None
//arg[2] AIdxChn : None
//arg[3] AIncludeTx : None
TSAPI(s32) tsfifo_receive_can_msgs(const PLIBCAN ACANBuffers,const ps32 ACANBufferSize,const s32 AIdxChn,const bool AIncludeTx);
//arg[0] ACANFDBuffers : None
//arg[1] ACANFDBufferSize : None
//arg[2] AIdxChn : None
//arg[3] AIncludeTx : None
TSAPI(s32) tsfifo_receive_canfd_msgs(const PLIBCANFD ACANFDBuffers,const ps32 ACANFDBufferSize,const s32 AIdxChn,const bool AIncludeTx);
//arg[0] ALINBuffers : None
//arg[1] ALINBufferSize : None
//arg[2] AIdxChn : None
//arg[3] AIncludeTx : None
TSAPI(s32) tsfifo_receive_lin_msgs(const PLIBLIN ALINBuffers,const ps32 ALINBufferSize,const s32 AIdxChn,const bool AIncludeTx);
//arg[0] AFastLINBuffers : None
//arg[1] AFastLINBufferSize : None
//arg[2] AIdxChn : None
//arg[3] AIncludeTx : None
TSAPI(s32) tsfifo_receive_fastlin_msgs(const PLIBLIN AFastLINBuffers,const ps32 AFastLINBufferSize,const s32 AIdxChn,const bool AIncludeTx);
//arg[0] AIdxChn : None
TSAPI(s32) tsfifo_clear_can_receive_buffers(const s32 AIdxChn);
//arg[0] AIdxChn : None
TSAPI(s32) tsfifo_clear_canfd_receive_buffers(const s32 AIdxChn);
//arg[0] AIdxChn : None
TSAPI(s32) tsfifo_clear_lin_receive_buffers(const s32 AIdxChn);
//arg[0] AIdxChn : None
TSAPI(s32) tsfifo_clear_fastlin_receive_buffers(const s32 AIdxChn);
//arg[0] AIdxChn : None
//arg[1] ACount : None
TSAPI(s32) tsfifo_read_can_buffer_frame_count(const s32 AIdxChn,const ps32 ACount);
//arg[0] AIdxChn : None
//arg[1] ACount : None
TSAPI(s32) tsfifo_read_can_tx_buffer_frame_count(const s32 AIdxChn,const ps32 ACount);
//arg[0] AIdxChn : None
//arg[1] ACount : None
TSAPI(s32) tsfifo_read_can_rx_buffer_frame_count(const s32 AIdxChn,const ps32 ACount);
//arg[0] AIdxChn : None
//arg[1] ACount : None
TSAPI(s32) tsfifo_read_canfd_buffer_frame_count(const s32 AIdxChn,const ps32 ACount);
//arg[0] AIdxChn : None
//arg[1] ACount : None
TSAPI(s32) tsfifo_read_canfd_tx_buffer_frame_count(const s32 AIdxChn,const ps32 ACount);
//arg[0] AIdxChn : None
//arg[1] ACount : None
TSAPI(s32) tsfifo_read_canfd_rx_buffer_frame_count(const s32 AIdxChn,const ps32 ACount);
//arg[0] AIdxChn : None
//arg[1] ACount : None
TSAPI(s32) tsfifo_read_lin_buffer_frame_count(const s32 AIdxChn,const ps32 ACount);
//arg[0] AIdxChn : None
//arg[1] ACount : None
TSAPI(s32) tsfifo_read_lin_tx_buffer_frame_count(const s32 AIdxChn,const ps32 ACount);
//arg[0] AIdxChn : None
//arg[1] ACount : None
TSAPI(s32) tsfifo_read_lin_rx_buffer_frame_count(const s32 AIdxChn,const ps32 ACount);
//arg[0] AIdxChn : None
//arg[1] ACount : None
TSAPI(s32) tsfifo_read_fastlin_buffer_frame_count(const s32 AIdxChn,const ps32 ACount);
//arg[0] AIdxChn : None
//arg[1] ACount : None
TSAPI(s32) tsfifo_read_fastlin_tx_buffer_frame_count(const s32 AIdxChn,const ps32 ACount);
//arg[0] AIdxChn : None
//arg[1] ACount : None
TSAPI(s32) tsfifo_read_fastlin_rx_buffer_frame_count(const s32 AIdxChn,const ps32 ACount);
//arg[0] ADataBuffers : None
//arg[1] ADataBufferSize : None
//arg[2] AIdxChn : None
//arg[3] AIncludeTx : None
TSAPI(s32) tsfifo_receive_flexray_msgs(const PLIBFlexRay ADataBuffers,const ps32 ADataBufferSize,const s32 AIdxChn,const bool AIncludeTx);
//arg[0] AIdxChn : None
TSAPI(s32) tsfifo_clear_flexray_receive_buffers(const s32 AIdxChn);
//arg[0] AIdxChn : None
//arg[1] ACount : None
TSAPI(s32) tsfifo_read_flexray_buffer_frame_count(const s32 AIdxChn,const ps32 ACount);
//arg[0] AIdxChn : None
//arg[1] ACount : None
TSAPI(s32) tsfifo_read_flexray_tx_buffer_frame_count(const s32 AIdxChn,const ps32 ACount);
//arg[0] AIdxChn : None
//arg[1] ACount : None
TSAPI(s32) tsfifo_read_flexray_rx_buffer_frame_count(const s32 AIdxChn,const ps32 ACount);
//arg[0] ACAN : None
//arg[1] APeriodMS : None
TSAPI(s32) tsapp_add_cyclic_msg_can(const PLIBCAN ACAN,const single APeriodMS);
//arg[0] ACAN : None
TSAPI(s32) tsapp_update_cyclic_msg_can(const PLIBCAN ACAN);
//arg[0] ACANFD : None
//arg[1] APeriodMS : None
TSAPI(s32) tsapp_add_cyclic_msg_canfd(const PLIBCANFD ACANFD,const single APeriodMS);
//arg[0] ACAN : None
TSAPI(s32) tsapp_delete_cyclic_msg_can(const PLIBCAN ACAN);
//arg[0] ACANFD : None
TSAPI(s32) tsapp_delete_cyclic_msg_canfd(const PLIBCANFD ACANFD);
TSAPI(s32) tsapp_delete_cyclic_msgs();
//arg[0] AEnable : None
TSAPI(s32) tsapp_enable_bus_statistics(const bool AEnable);
TSAPI(s32) tsapp_clear_bus_statistics();
//arg[0] ABusType : None
//arg[1] AIdxChn : None
//arg[2] AIdxStat : None
//arg[3] AStat : None
TSAPI(s32) tsapp_get_bus_statistics(const s32 ABusType,const s32 AIdxChn,const s32 AIdxStat,const pdouble AStat);
//arg[0] AIdxChn : None
//arg[1] AIdentifier : None
//arg[2] AFPS : None
TSAPI(s32) tsapp_get_fps_can(const s32 AIdxChn,const s32 AIdentifier,const ps32 AFPS);
//arg[0] AIdxChn : None
//arg[1] AIdentifier : None
//arg[2] AFPS : None
TSAPI(s32) tsapp_get_fps_canfd(const s32 AIdxChn,const s32 AIdentifier,const ps32 AFPS);
//arg[0] AIdxChn : None
//arg[1] AIdentifier : None
//arg[2] AFPS : None
TSAPI(s32) tsapp_get_fps_lin(const s32 AIdxChn,const s32 AIdentifier,const ps32 AFPS);
//arg[0] AObj : None
//arg[1] AEvent : None
TSAPI(s32) tsapp_register_event_gps(const ps32 AObj,const TGPSQueueEvent_Win32 AEvent);
//arg[0] AObj : None
//arg[1] AEvent : None
TSAPI(s32) tsapp_unregister_event_gps(const ps32 AObj,const TGPSQueueEvent_Win32 AEvent);
//arg[0] AObj : None
//arg[1] AEvent : None
TSAPI(s32) tsapp_register_event_can(const ps32 AObj,const TCANQueueEvent_Win32 AEvent);
//arg[0] AObj : None
//arg[1] AEvent : None
TSAPI(s32) tsapp_unregister_event_can(const ps32 AObj,const TCANQueueEvent_Win32 AEvent);
//arg[0] AObj : None
//arg[1] AEvent : None
TSAPI(s32) tsapp_register_event_canfd(const ps32 AObj,const TCANFDQueueEvent_Win32 AEvent);
//arg[0] AObj : None
//arg[1] AEvent : None
TSAPI(s32) tsapp_unregister_event_canfd(const ps32 AObj,const TCANFDQueueEvent_Win32 AEvent);
//arg[0] AObj : None
//arg[1] AEvent : None
TSAPI(s32) tsapp_register_event_lin(const ps32 AObj,const TLINQueueEvent_Win32 AEvent);
//arg[0] AObj : None
//arg[1] AEvent : None
TSAPI(s32) tsapp_unregister_event_lin(const ps32 AObj,const TLINQueueEvent_Win32 AEvent);
//arg[0] AObj : None
//arg[1] AEvent : None
TSAPI(s32) tsapp_register_event_flexray(const ps32 AObj,const TFlexRayQueueEvent_Win32 AEvent);
//arg[0] AObj : None
//arg[1] AEvent : None
TSAPI(s32) tsapp_unregister_event_flexray(const ps32 AObj,const TFlexRayQueueEvent_Win32 AEvent);
//arg[0] AObj : None
TSAPI(s32) tsapp_unregister_events_flexray(const ps32 AObj);
//arg[0] AObj : None
TSAPI(s32) tsapp_unregister_events_can(const ps32 AObj);
//arg[0] AObj : None
TSAPI(s32) tsapp_unregister_events_lin(const ps32 AObj);
//arg[0] AObj : None
TSAPI(s32) tsapp_unregister_events_canfd(const ps32 AObj);
//arg[0] AObj : None
TSAPI(s32) tsapp_unregister_events_all(const ps32 AObj);
//arg[0] AObj : None
//arg[1] AEvent : None
TSAPI(s32) tsapp_register_pretx_event_can(const ps32 AObj,const TCANQueueEvent_Win32 AEvent);
//arg[0] AObj : None
//arg[1] AEvent : None
TSAPI(s32) tsapp_unregister_pretx_event_can(const ps32 AObj,const TCANQueueEvent_Win32 AEvent);
//arg[0] AObj : None
//arg[1] AEvent : None
TSAPI(s32) tsapp_register_pretx_event_canfd(const ps32 AObj,const TCANFDQueueEvent_Win32 AEvent);
//arg[0] AObj : None
//arg[1] AEvent : None
TSAPI(s32) tsapp_unregister_pretx_event_canfd(const ps32 AObj,const TCANFDQueueEvent_Win32 AEvent);
//arg[0] AObj : None
//arg[1] AEvent : None
TSAPI(s32) tsapp_register_pretx_event_lin(const ps32 AObj,const TLINQueueEvent_Win32 AEvent);
//arg[0] AObj : None
//arg[1] AEvent : None
TSAPI(s32) tsapp_unregister_pretx_event_lin(const ps32 AObj,const TLINQueueEvent_Win32 AEvent);
//arg[0] AObj : None
//arg[1] AEvent : None
TSAPI(s32) tsapp_register_pretx_event_flexray(const ps32 AObj,const TFlexRayQueueEvent_Win32 AEvent);
//arg[0] AObj : None
//arg[1] AEvent : None
TSAPI(s32) tsapp_unregister_pretx_event_flexray(const ps32 AObj,const TFlexRayQueueEvent_Win32 AEvent);
//arg[0] AObj : None
TSAPI(s32) tsapp_unregister_pretx_events_flexray(const ps32 AObj);
//arg[0] AObj : None
TSAPI(s32) tsapp_unregister_pretx_events_can(const ps32 AObj);
//arg[0] AObj : None
TSAPI(s32) tsapp_unregister_pretx_events_lin(const ps32 AObj);
//arg[0] AObj : None
TSAPI(s32) tsapp_unregister_pretx_events_canfd(const ps32 AObj);
//arg[0] AObj : None
TSAPI(s32) tsapp_unregister_pretx_events_all(const ps32 AObj);
//arg[0] AFileName : None
TSAPI(s32) tsapp_start_logging(const char*  AFileName);
TSAPI(s32) tsapp_stop_logging();
//arg[0] AFileName : None
//arg[1] AObj : None
TSAPI(s32) tsapp_excel_load(const char*  AFileName,const ps32 AObj);
//arg[0] AObj : None
//arg[1] ACount : None
TSAPI(s32) tsapp_excel_get_sheet_count(const ps32 AObj,const s32 ACount);
//arg[0] AObj : None
//arg[1] ACount : None
TSAPI(s32) tsapp_excel_set_sheet_count(const ps32 AObj,const s32 ACount);
//arg[0] AObj : None
//arg[1] AIdxSheet : None
//arg[2] AName : None
TSAPI(s32) tsapp_excel_get_sheet_name(const ps32 AObj,const s32 AIdxSheet,const ppchar AName);
//arg[0] AObj : None
//arg[1] AIdxSheet : None
//arg[2] AName : None
TSAPI(s32) tsapp_excel_set_sheet_name(const ps32 AObj,const s32 AIdxSheet,const char*  AName);
//arg[0] AObj : None
//arg[1] AIdxSheet : None
//arg[2] ARowCount : None
//arg[3] AColCount : None
TSAPI(s32) tsapp_excel_get_cell_count(const ps32 AObj,const s32 AIdxSheet,const s32 ARowCount,const s32 AColCount);
//arg[0] AObj : None
//arg[1] AIdxSheet : None
//arg[2] AIdxRow : None
//arg[3] AIdxCol : None
TSAPI(s32) tsapp_excel_get_cell_value(const ps32 AObj,const s32 AIdxSheet,const s32 AIdxRow,const s32 AIdxCol);
//arg[0] AObj : None
//arg[1] AIdxSheet : None
//arg[2] ARowCount : None
//arg[3] AColCount : None
TSAPI(s32) tsapp_excel_set_cell_count(const ps32 AObj,const s32 AIdxSheet,const s32 ARowCount,const s32 AColCount);
//arg[0] AObj : None
//arg[1] AIdxSheet : None
//arg[2] AIdxRow : None
//arg[3] AIdxCol : None
TSAPI(s32) tsapp_excel_set_cell_value(const ps32 AObj,const s32 AIdxSheet,const s32 AIdxRow,const s32 AIdxCol);
//arg[0] AObj : None
TSAPI(s32) tsapp_excel_unload(const ps32 AObj);
TSAPI(s32) tsapp_system_vars_reload_settings();
//arg[0] AinternalCount : None
//arg[1] AUserCount : None
TSAPI(s32) tsapp_get_system_var_count(const ps32 AinternalCount,const ps32 AUserCount);
//arg[0] AIsUser : None
//arg[1] AIndex : None
//arg[2] AVarDef : None
TSAPI(s32) tsapp_get_system_var_def_by_index(const bool AIsUser,const s32 AIndex,const PLIBSystemVarDef AVarDef);
//arg[0] AIsUser : None
//arg[1] ACompleteName : None
//arg[2] AVarDef : None
TSAPI(s32) tsapp_find_system_var_def_by_name(const bool AIsUser,const char*  ACompleteName,const PLIBSystemVarDef AVarDef);
//arg[0] ACompleteName : None
//arg[1] AValue : None
TSAPI(s32) tsapp_get_system_var_double(const char*  ACompleteName,const pdouble AValue);
//arg[0] ACompleteName : None
//arg[1] AValue : None
TSAPI(s32) tsapp_get_system_var_int32(const char*  ACompleteName,const ps32 AValue);
//arg[0] ACompleteName : None
//arg[1] AValue : None
TSAPI(s32) tsapp_get_system_var_uint32(const char*  ACompleteName,const pu32 AValue);
//arg[0] ACompleteName : None
//arg[1] AValue : None
TSAPI(s32) tsapp_get_system_var_int64(const char*  ACompleteName,const ps64 AValue);
//arg[0] ACompleteName : None
//arg[1] AValue : None
TSAPI(s32) tsapp_get_system_var_uint64(const char*  ACompleteName,const pu64 AValue);
//arg[0] ACompleteName : None
//arg[1] ACapacity : None
//arg[2] AVarCount : None
//arg[3] AValue : None
TSAPI(s32) tsapp_get_system_var_uint8_array(const char*  ACompleteName,const s32 ACapacity,const ps32 AVarCount,const pu8 AValue);
//arg[0] ACompleteName : None
//arg[1] ACapacity : None
//arg[2] AVarCount : None
//arg[3] AValue : None
TSAPI(s32) tsapp_get_system_var_int32_array(const char*  ACompleteName,const s32 ACapacity,const ps32 AVarCount,const ps32 AValue);
//arg[0] ACompleteName : None
//arg[1] ACapacity : None
//arg[2] AVarCount : None
//arg[3] AValue : None
TSAPI(s32) tsapp_get_system_var_int64_array(const char*  ACompleteName,const s32 ACapacity,const ps32 AVarCount,const ps64 AValue);
//arg[0] ACompleteName : None
//arg[1] ACapacity : None
//arg[2] AVarCount : None
//arg[3] AValue : None
TSAPI(s32) tsapp_get_system_var_double_array(const char*  ACompleteName,const s32 ACapacity,const ps32 AVarCount,const pdouble AValue);
//arg[0] ACompleteName : None
//arg[1] ACapacity : None
//arg[2] AValue : None
TSAPI(s32) tsapp_get_system_var_string(const char*  ACompleteName,const s32 ACapacity,const char*  AValue);
//arg[0] ACompleteName : None
//arg[1] AValue : None
TSAPI(s32) tsapp_set_system_var_double(const char*  ACompleteName,const double AValue);
//arg[0] ACompleteName : None
//arg[1] AValue : None
TSAPI(s32) tsapp_set_system_var_int32(const char*  ACompleteName,const s32 AValue);
//arg[0] ACompleteName : None
//arg[1] AValue : None
TSAPI(s32) tsapp_set_system_var_uint32(const char*  ACompleteName,const u32 AValue);
//arg[0] ACompleteName : None
//arg[1] AValue : None
TSAPI(s32) tsapp_set_system_var_int64(const char*  ACompleteName,const s64 AValue);
//arg[0] ACompleteName : None
//arg[1] AValue : None
TSAPI(s32) tsapp_set_system_var_uint64(const char*  ACompleteName,const u64 AValue);
//arg[0] ACompleteName : None
//arg[1] ACapacity : None
//arg[2] AValue : None
TSAPI(s32) tsapp_set_system_var_uint8_array(const char*  ACompleteName,const s32 ACapacity,const pu8 AValue);
//arg[0] ACompleteName : None
//arg[1] ACapacity : None
//arg[2] AValue : None
TSAPI(s32) tsapp_set_system_var_int32_array(const char*  ACompleteName,const s32 ACapacity,const ps32 AValue);
//arg[0] ACompleteName : None
//arg[1] ACapacity : None
//arg[2] AValue : None
TSAPI(s32) tsapp_set_system_var_int64_array(const char*  ACompleteName,const s32 ACapacity,const ps64 AValue);
//arg[0] ACompleteName : None
//arg[1] ACapacity : None
//arg[2] AValue : None
TSAPI(s32) tsapp_set_system_var_double_array(const char*  ACompleteName,const s32 ACapacity,const pdouble AValue);
//arg[0] ACompleteName : None
//arg[1] AValue : None
TSAPI(s32) tsapp_set_system_var_string(const char*  ACompleteName,const char*  AValue);
//arg[0] ACompleteName : None
TSAPI(s32) tsapp_log_system_var(const char*  ACompleteName);
//arg[0] ACompleteName : None
//arg[1] ACapacity : None
//arg[2] AValue : None
TSAPI(s32) tsapp_get_system_var_generic(const char*  ACompleteName,const s32 ACapacity,const char*  AValue);
//arg[0] ACompleteName : None
//arg[1] AValue : None
TSAPI(s32) tsapp_set_system_var_generic(const char*  ACompleteName,const char*  AValue);
//arg[0] AString : None
TSAPI(s32) tsapp_get_hardware_id_string(const ppchar AString);
//arg[0] AArray8B : None
TSAPI(s32) tsapp_get_hardware_id_array(const pu8 AArray8B);
//arg[0] ACompleteName : None
//arg[1] AType : None
//arg[2] ADefaultValue : None
//arg[3] AComment : None
TSAPI(s32) tsapp_create_system_var(const char*  ACompleteName,const s32 AType,const char*  ADefaultValue,const char*  AComment);
//arg[0] ACompleteName : None
TSAPI(s32) tsapp_delete_system_var(const char*  ACompleteName);
//arg[0] ALoadedDBCount : None
TSAPI(s32) tsdb_reload_settings(const ps32 ALoadedDBCount);
TSAPI(s32) tsdb_save_settings();
//arg[0] ADBC : None
//arg[1] ASupportedChannelsBased0 : None
//arg[2] AId : None
TSAPI(s32) tsdb_load_can_db(const char*  ADBC,const char*  ASupportedChannelsBased0,const ps32 AId);
//arg[0] AId : None
TSAPI(s32) tsdb_unload_can_db(const s32 AId);
TSAPI(s32) tsdb_unload_can_dbs();
//arg[0] ACount : None
TSAPI(s32) tsdb_get_can_db_count(const ps32 ACount);
//arg[0] AIndex : None
//arg[1] AId : None
TSAPI(s32) tsdb_get_can_db_id(const s32 AIndex,const ps32 AId);
//arg[0] ADatabaseId : None
//arg[1] AType : None
//arg[2] AIndex : None
//arg[3] ASubIndex : None
//arg[4] AValue : None
TSAPI(s32) tsdb_get_can_db_info(const u32 ADatabaseId,const s32 AType,const s32 AIndex,const s32 ASubIndex,const ppchar AValue);
//arg[0] AFRFile : None
//arg[1] ASupportedChannels : None
//arg[2] AId : None
TSAPI(s32) tsdb_load_flexray_db(const char*  AFRFile,const char*  ASupportedChannels,const ps32 AId);
//arg[0] AId : None
TSAPI(s32) tsdb_unload_flexray_db(const s32 AId);
TSAPI(s32) tsdb_unload_flexray_dbs();
//arg[0] ACount : None
TSAPI(s32) tsdb_get_flexray_db_count(const ps32 ACount);
//arg[0] AAddr : None
//arg[1] ADBIndex : None
//arg[2] ASignalCount : None
//arg[3] AFrameCount : None
//arg[4] AECUCount : None
//arg[5] ASupportedChannelMask : None
//arg[6] AFlags : None
//arg[7] AName : None
//arg[8] AComment : None
TSAPI(s32) tsdb_get_flexray_db_properties_by_address_verbose(const char*  AAddr,const ps32 ADBIndex,const ps32 ASignalCount,const ps32 AFrameCount,const ps32 AECUCount,const ps64 ASupportedChannelMask,const ps64 AFlags,const ppchar AName,const ppchar AComment);
//arg[0] ADBIndex : None
//arg[1] ASignalCount : None
//arg[2] AFrameCount : None
//arg[3] AECUCount : None
//arg[4] ASupportedChannelMask : None
//arg[5] AFlags : None
//arg[6] AName : None
//arg[7] AComment : None
TSAPI(s32) tsdb_get_flexray_db_properties_by_index_verbose(const s32 ADBIndex,const ps32 ASignalCount,const ps32 AFrameCount,const ps32 AECUCount,const ps64 ASupportedChannelMask,const ps64 AFlags,const ppchar AName,const ppchar AComment);
//arg[0] AAddr : None
//arg[1] ADBIndex : None
//arg[2] AECUIndex : None
//arg[3] ATxFrameCount : None
//arg[4] ARxFrameCount : None
//arg[5] AName : None
//arg[6] AComment : None
TSAPI(s32) tsdb_get_flexray_ecu_properties_by_address_verbose(const char*  AAddr,const ps32 ADBIndex,const ps32 AECUIndex,const ps32 ATxFrameCount,const ps32 ARxFrameCount,const ppchar AName,const ppchar AComment);
//arg[0] ADBIndex : None
//arg[1] AECUIndex : None
//arg[2] ATxFrameCount : None
//arg[3] ARxFrameCount : None
//arg[4] AName : None
//arg[5] AComment : None
TSAPI(s32) tsdb_get_flexray_ecu_properties_by_index_verbose(const s32 ADBIndex,const s32 AECUIndex,const ps32 ATxFrameCount,const ps32 ARxFrameCount,const ppchar AName,const ppchar AComment);
//arg[0] AAddr : None
//arg[1] ADBIndex : None
//arg[2] AECUIndex : None
//arg[3] AFrameIndex : None
//arg[4] AIsTx : None
//arg[5] AFRChannelMask : None
//arg[6] AFRBaseCycle : None
//arg[7] AFRCycleRepetition : None
//arg[8] AFRIsStartupFrame : None
//arg[9] AFRSlotId : None
//arg[10] AFRCycleMask : None
//arg[11] ASignalCount : None
//arg[12] AFRDLC : None
//arg[13] AName : None
//arg[14] AComment : None
TSAPI(s32) tsdb_get_flexray_frame_properties_by_address_verbose(const char*  AAddr,const ps32 ADBIndex,const ps32 AECUIndex,const ps32 AFrameIndex,const pbool AIsTx,const ps32 AFRChannelMask,const ps32 AFRBaseCycle,const ps32 AFRCycleRepetition,const pbool AFRIsStartupFrame,const ps32 AFRSlotId,const ps64 AFRCycleMask,const ps32 ASignalCount,const ps32 AFRDLC,const ppchar AName,const ppchar AComment);
//arg[0] ADBIndex : None
//arg[1] AECUIndex : None
//arg[2] AFrameIndex : None
//arg[3] AIsTx : None
//arg[4] AFRChannelMask : None
//arg[5] AFRBaseCycle : None
//arg[6] AFRCycleRepetition : None
//arg[7] AFRIsStartupFrame : None
//arg[8] AFRSlotId : None
//arg[9] AFRCycleMask : None
//arg[10] ASignalCount : None
//arg[11] AFRDLC : None
//arg[12] AName : None
//arg[13] AComment : None
TSAPI(s32) tsdb_get_flexray_frame_properties_by_index_verbose(const s32 ADBIndex,const s32 AECUIndex,const s32 AFrameIndex,const bool AIsTx,const ps32 AFRChannelMask,const ps32 AFRBaseCycle,const ps32 AFRCycleRepetition,const pbool AFRIsStartupFrame,const ps32 AFRSlotId,const ps64 AFRCycleMask,const ps32 ASignalCount,const ps32 AFRDLC,const ppchar AName,const ppchar AComment);
//arg[0] AAddr : None
//arg[1] ADBIndex : None
//arg[2] AECUIndex : None
//arg[3] AFrameIndex : None
//arg[4] ASignalIndex : None
//arg[5] AIsTx : None
//arg[6] ASignalType : None
//arg[7] ACompuMethod : None
//arg[8] AIsIntel : None
//arg[9] AActualStartBit : None
//arg[10] AActualUpdateBit : None
//arg[11] ALength : None
//arg[12] AFactor : None
//arg[13] AOffset : None
//arg[14] AInitValue : None
//arg[15] AName : None
//arg[16] AComment : None
TSAPI(s32) tsdb_get_flexray_signal_properties_by_address_verbose(const char*  AAddr,const ps32 ADBIndex,const ps32 AECUIndex,const ps32 AFrameIndex,const ps32 ASignalIndex,const pbool AIsTx,const ps32 ASignalType,const ps32 ACompuMethod,const pbool AIsIntel,const ps32 AActualStartBit,const ps32 AActualUpdateBit,const ps32 ALength,const pdouble AFactor,const pdouble AOffset,const pdouble AInitValue,const ppchar AName,const ppchar AComment);
//arg[0] ADBIndex : None
//arg[1] AECUIndex : None
//arg[2] AFrameIndex : None
//arg[3] ASignalIndex : None
//arg[4] AIsTx : None
//arg[5] ASignalType : None
//arg[6] ACompuMethod : None
//arg[7] AIsIntel : None
//arg[8] AActualStartBit : None
//arg[9] AActualUpdateBit : None
//arg[10] ALength : None
//arg[11] AFactor : None
//arg[12] AOffset : None
//arg[13] AInitValue : None
//arg[14] AName : None
//arg[15] AComment : None
TSAPI(s32) tsdb_get_flexray_signal_properties_by_index_verbose(const s32 ADBIndex,const s32 AECUIndex,const s32 AFrameIndex,const s32 ASignalIndex,const bool AIsTx,const ps32 ASignalType,const ps32 ACompuMethod,const pbool AIsIntel,const ps32 AActualStartBit,const ps32 AActualUpdateBit,const ps32 ALength,const pdouble AFactor,const pdouble AOffset,const pdouble AInitValue,const ppchar AName,const ppchar AComment);
//arg[0] AIndex : None
//arg[1] AId : None
TSAPI(s32) tsdb_get_flexray_db_id(const s32 AIndex,const ps32 AId);
//arg[0] AValue : None
TSAPI(s32) tsdb_get_can_db_properties_by_index(const PMPDBProperties AValue);
//arg[0] AValue : None
TSAPI(s32) tsdb_get_lin_db_properties_by_index(const PMPDBProperties AValue);
//arg[0] AValue : None
TSAPI(s32) tsdb_get_flexray_db_properties_by_index(const PMPDBProperties AValue);
//arg[0] AValue : None
TSAPI(s32) tsdb_get_can_db_ecu_properties_by_index(const PMPDBECUProperties AValue);
//arg[0] AValue : None
TSAPI(s32) tsdb_get_lin_db_ecu_properties_by_index(const PMPDBECUProperties AValue);
//arg[0] AValue : None
TSAPI(s32) tsdb_get_flexray_db_ecu_properties_by_index(const PMPDBECUProperties AValue);
//arg[0] AValue : None
TSAPI(s32) tsdb_get_can_db_frame_properties_by_index(const PMPDBFrameProperties AValue);
//arg[0] AValue : None
TSAPI(s32) tsdb_get_lin_db_frame_properties_by_index(const PMPDBFrameProperties AValue);
//arg[0] AValue : None
TSAPI(s32) tsdb_get_flexray_db_frame_properties_by_index(const PMPDBFrameProperties AValue);
//arg[0] AValue : None
TSAPI(s32) tsdb_get_can_db_signal_properties_by_index(const PMPDBSignalProperties AValue);
//arg[0] AValue : None
TSAPI(s32) tsdb_get_lin_db_signal_properties_by_index(const PMPDBSignalProperties AValue);
//arg[0] AValue : None
TSAPI(s32) tsdb_get_flexray_db_signal_properties_by_index(const PMPDBSignalProperties AValue);
//arg[0] AAddr : None
//arg[1] AValue : None
TSAPI(s32) tsdb_get_can_db_properties_by_address(const char*  AAddr,const PMPDBProperties AValue);
//arg[0] AAddr : None
//arg[1] AValue : None
TSAPI(s32) tsdb_get_lin_db_properties_by_address(const char*  AAddr,const PMPDBProperties AValue);
//arg[0] AAddr : None
//arg[1] AValue : None
TSAPI(s32) tsdb_get_flexray_db_properties_by_address(const char*  AAddr,const PMPDBProperties AValue);
//arg[0] AAddr : None
//arg[1] AValue : None
TSAPI(s32) tsdb_get_can_db_ecu_properties_by_address(const char*  AAddr,const PMPDBECUProperties AValue);
//arg[0] AAddr : None
//arg[1] AValue : None
TSAPI(s32) tsdb_get_lin_db_ecu_properties_by_address(const char*  AAddr,const PMPDBECUProperties AValue);
//arg[0] AAddr : None
//arg[1] AValue : None
TSAPI(s32) tsdb_get_flexray_db_ecu_properties_by_address(const char*  AAddr,const PMPDBECUProperties AValue);
//arg[0] AAddr : None
//arg[1] AValue : None
TSAPI(s32) tsdb_get_can_db_frame_properties_by_address(const char*  AAddr,const PMPDBFrameProperties AValue);
//arg[0] AAddr : None
//arg[1] AValue : None
TSAPI(s32) tsdb_get_lin_db_frame_properties_by_address(const char*  AAddr,const PMPDBFrameProperties AValue);
//arg[0] AAddr : None
//arg[1] AValue : None
TSAPI(s32) tsdb_get_flexray_db_frame_properties_by_address(const char*  AAddr,const PMPDBFrameProperties AValue);
//arg[0] AAddr : None
//arg[1] AValue : None
TSAPI(s32) tsdb_get_can_db_signal_properties_by_address(const char*  AAddr,const PMPDBSignalProperties AValue);
//arg[0] AAddr : None
//arg[1] AValue : None
TSAPI(s32) tsdb_get_lin_db_signal_properties_by_address(const char*  AAddr,const PMPDBSignalProperties AValue);
//arg[0] AAddr : None
//arg[1] AValue : None
TSAPI(s32) tsdb_get_flexray_db_signal_properties_by_address(const char*  AAddr,const PMPDBSignalProperties AValue);
//arg[0] ALDF : None
//arg[1] ASupportedChannelsBased0 : None
//arg[2] AId : None
TSAPI(s32) tsdb_load_lin_db(const char*  ALDF,const char*  ASupportedChannelsBased0,const ps32 AId);
//arg[0] AId : None
TSAPI(s32) tsdb_unload_lin_db(const s32 AId);
TSAPI(s32) tsdb_unload_lin_dbs();
//arg[0] ACount : None
TSAPI(s32) tsdb_get_lin_db_count(const ps32 ACount);
//arg[0] AIndex : None
//arg[1] AId : None
TSAPI(s32) tsdb_get_lin_db_id(const s32 AIndex,const ps32 AId);
//arg[0] AIdxDB : None
//arg[1] AIndex : None
//arg[2] AValue : None
TSAPI(s32) tsdb_get_can_db_frame_properties_by_db_index(const s32 AIdxDB,const u32 AIndex,const PMPDBFrameProperties AValue);
//arg[0] AIdxDB : None
//arg[1] AIndex : None
//arg[2] AValue : None
TSAPI(s32) tsdb_get_lin_db_frame_properties_by_db_index(const s32 AIdxDB,const s32 AIndex,const PMPDBFrameProperties AValue);
//arg[0] AIdxDB : None
//arg[1] AIndex : None
//arg[2] AValue : None
TSAPI(s32) tsdb_get_flexray_db_frame_properties_by_db_index(const s32 AIdxDB,const s32 AIndex,const PMPDBFrameProperties AValue);
//arg[0] AIdxDB : None
//arg[1] AIdxFrame : None
//arg[2] ASgnIndexInFrame : None
//arg[3] AValue : None
TSAPI(s32) tsdb_get_can_db_signal_properties_by_frame_index(const s32 AIdxDB,const s32 AIdxFrame,const s32 ASgnIndexInFrame,const PMPDBSignalProperties AValue);
//arg[0] AIdxDB : None
//arg[1] AIdxFrame : None
//arg[2] ASgnIndexInFrame : None
//arg[3] AValue : None
TSAPI(s32) tsdb_get_lin_db_signal_properties_by_frame_index(const s32 AIdxDB,const s32 AIdxFrame,const s32 ASgnIndexInFrame,const PMPDBSignalProperties AValue);
//arg[0] AIdxDB : None
//arg[1] AIdxFrame : None
//arg[2] ASgnIndexInFrame : None
//arg[3] AValue : None
TSAPI(s32) tsdb_get_flexray_db_signal_properties_by_frame_index(const s32 AIdxDB,const s32 AIdxFrame,const s32 ASgnIndexInFrame,const PMPDBSignalProperties AValue);
//arg[0] ACAN : None
//arg[1] AMsgName : None
//arg[2] ASgnName : None
//arg[3] AValue : None
TSAPI(s32) tsdb_set_signal_value_can(const PLIBCAN ACAN,const char*  AMsgName,const char*  ASgnName,const double AValue);
//arg[0] ACAN : None
//arg[1] AMsgName : None
//arg[2] ASgnName : None
//arg[3] AValue : None
TSAPI(s32) tsdb_get_signal_value_can(const PLIBCAN ACAN,const char*  AMsgName,const char*  ASgnName,const pdouble AValue);
//arg[0] ACANfd : None
//arg[1] AMsgName : None
//arg[2] ASgnName : None
//arg[3] AValue : None
TSAPI(s32) tsdb_set_signal_value_canfd(const PLIBCANFD ACANfd,const char*  AMsgName,const char*  ASgnName,const double AValue);
//arg[0] ACANfd : None
//arg[1] AMsgName : None
//arg[2] ASgnName : None
//arg[3] AValue : None
TSAPI(s32) tsdb_get_signal_value_canfd(const PLIBCANFD ACANfd,const char*  AMsgName,const char*  ASgnName,const pdouble AValue);
//arg[0] ALoadedEngineCount : None
TSAPI(s32) tslog_reload_settings(const s32 ALoadedEngineCount);
//arg[0] AFileName : None
//arg[1] AIndex : None
TSAPI(s32) tslog_add_online_replay_config(const char*  AFileName,const ps32 AIndex);
//arg[0] AIndex : None
//arg[1] AName : None
//arg[2] AFileName : None
//arg[3] AAutoStart : None
//arg[4] AIsRepetitiveMode : None
//arg[5] AStartTimingMode : None
//arg[6] AStartDelayTimeMs : None
//arg[7] ASendTx : None
//arg[8] ASendRx : None
//arg[9] AMappings : None
TSAPI(s32) tslog_set_online_replay_config(const s32 AIndex,const char*  AName,const char*  AFileName,const bool AAutoStart,const bool AIsRepetitiveMode,const s32 AStartTimingMode,const s32 AStartDelayTimeMs,const bool ASendTx,const bool ASendRx,const char*  AMappings);
//arg[0] ACount : None
TSAPI(s32) tslog_get_online_replay_count(const ps32 ACount);
//arg[0] AIndex : None
//arg[1] AName : None
//arg[2] AFileName : None
//arg[3] AAutoStart : None
//arg[4] AIsRepetitiveMode : None
//arg[5] AStartTimingMode : None
//arg[6] AStartDelayTimeMs : None
//arg[7] ASendTx : None
//arg[8] ASendRx : None
//arg[9] AMappings : None
TSAPI(s32) tslog_get_online_replay_config(const s32 AIndex,const ppchar AName,const ppchar AFileName,const pbool AAutoStart,const pbool AIsRepetitiveMode,const ps32 AStartTimingMode,const ps32 AStartDelayTimeMs,const pbool ASendTx,const pbool ASendRx,const ppchar AMappings);
//arg[0] AIndex : None
TSAPI(s32) tslog_del_online_replay_config(const s32 AIndex);
TSAPI(s32) tslog_del_online_replay_configs();
//arg[0] AIndex : None
TSAPI(s32) tslog_start_online_replay(const s32 AIndex);
TSAPI(s32) tslog_start_online_replays();
//arg[0] AIndex : None
TSAPI(s32) tslog_pause_online_replay(const s32 AIndex);
TSAPI(s32) tslog_pause_online_replays();
//arg[0] AIndex : None
TSAPI(s32) tslog_stop_online_replay(const s32 AIndex);
TSAPI(s32) tslog_stop_online_replays();
//arg[0] AIndex : None
//arg[1] AStatus : None
//arg[2] AProgressPercent100 : None
TSAPI(s32) tslog_get_online_replay_status(const s32 AIndex,const ps8 AStatus,const psingle AProgressPercent100);
//arg[0] AFileName : None
//arg[1] AHandle : None
TSAPI(s32) tslog_blf_write_start(const char*  AFileName,const ps32 AHandle);
//arg[0] AHandle : None
//arg[1] ACount : None
TSAPI(s32) tslog_blf_write_set_max_count(const s32 AHandle,const u32 ACount);
//arg[0] AHandle : None
//arg[1] ACAN : None
TSAPI(s32) tslog_blf_write_can(const s32 AHandle,const PLIBCAN ACAN);
//arg[0] AHandle : None
//arg[1] ACANFD : None
TSAPI(s32) tslog_blf_write_can_fd(const s32 AHandle,const PLIBCANFD ACANFD);
//arg[0] AHandle : None
//arg[1] ALIN : None
TSAPI(s32) tslog_blf_write_lin(const s32 AHandle,const PLIBLIN ALIN);
//arg[0] AHandle : None
//arg[1] ATimeUs : None
//arg[2] AComment : None
TSAPI(s32) tslog_blf_write_realtime_comment(const s32 AHandle,const s64 ATimeUs,const char*  AComment);
//arg[0] AHandle : None
TSAPI(s32) tslog_blf_write_end(const s32 AHandle);
//arg[0] AFileName : None
//arg[1] AHandle : None
//arg[2] AObjCount : None
TSAPI(s32) tslog_blf_read_start(const char*  AFileName,const ps32 AHandle,const ps32 AObjCount);
//arg[0] AFileName : None
//arg[1] AHandle : None
//arg[2] AObjCount : None
//arg[3] AYear : None
//arg[4] AMonth : None
//arg[5] ADayOfWeek : None
//arg[6] ADay : None
//arg[7] AHour : None
//arg[8] AMinute : None
//arg[9] ASecond : None
//arg[10] AMilliseconds : None
TSAPI(s32) tsLog_blf_read_start_verbose(const char*  AFileName,const ps32 AHandle,const ps32 AObjCount,const pu16 AYear,const pu16 AMonth,const pu16 ADayOfWeek,const pu16 ADay,const pu16 AHour,const pu16 AMinute,const pu16 ASecond,const pu16 AMilliseconds);
//arg[0] AHandle : None
//arg[1] AObjReadCount : None
TSAPI(s32) tslog_blf_read_status(const s32 AHandle,const ps32 AObjReadCount);
//arg[0] AHandle : None
//arg[1] AProgressedCnt : None
//arg[2] AType : None
//arg[3] ACAN : None
//arg[4] ALIN : None
//arg[5] ACANFD : None
TSAPI(s32) tslog_blf_read_object(const s32 AHandle,const ps32 AProgressedCnt,const ps32 AType,const PLIBCAN ACAN,const PLIBLIN ALIN,const PLIBCANFD ACANFD);
//arg[0] AHandle : None
//arg[1] AProgressedCnt : None
//arg[2] AType : None
//arg[3] ACAN : None
//arg[4] ALIN : None
//arg[5] ACANFD : None
//arg[6] AComment : None
TSAPI(s32) tslog_blf_read_object_w_comment(const s32 AHandle,const ps32 AProgressedCnt,const ps32 AType,const PLIBCAN ACAN,const PLIBLIN ALIN,const PLIBCANFD ACANFD,const Prealtime_comment_t AComment);
//arg[0] AHandle : None
TSAPI(s32) tslog_blf_read_end(const s32 AHandle);
//arg[0] AHandle : None
//arg[1] AProg100 : None
//arg[2] ATime : None
//arg[3] AProgressedCnt : None
TSAPI(s32) tslog_blf_seek_object_time(const s32 AHandle,const double AProg100,const ps64 ATime,const ps32 AProgressedCnt);
//arg[0] AObj : None
//arg[1] ABLFFileName : None
//arg[2] AASCFileName : None
//arg[3] AProgressCallback : None
TSAPI(s32) tslog_blf_to_asc(const ps32 AObj,const char*  ABLFFileName,const char*  AASCFileName,const TReadProgressCallback AProgressCallback);
//arg[0] AObj : None
//arg[1] AASCFileName : None
//arg[2] ABLFFileName : None
//arg[3] AProgressCallback : None
TSAPI(s32) tslog_asc_to_blf(const ps32 AObj,const char*  AASCFileName,const char*  ABLFFileName,const TReadProgressCallback AProgressCallback);
TSAPI(s32) tscom_lin_rbs_reload_settings();
TSAPI(s32) tscom_lin_rbs_start();
TSAPI(s32) tscom_lin_rbs_stop();
//arg[0] AIsRunning : None
TSAPI(s32) tscom_lin_rbs_is_running(const pbool AIsRunning);
//arg[0] AAutoStart : None
//arg[1] AAutoSendOnModification : None
//arg[2] AActivateNodeSimulation : None
//arg[3] AInitValueOptions : None
TSAPI(s32) tscom_lin_rbs_configure(const bool AAutoStart,const bool AAutoSendOnModification,const bool AActivateNodeSimulation,const s32 AInitValueOptions);
//arg[0] AEnable : None
//arg[1] AIncludingChildren : None
TSAPI(s32) tscom_lin_rbs_activate_all_networks(const bool AEnable,const bool AIncludingChildren);
//arg[0] AIdxChn : None
//arg[1] AEnable : None
//arg[2] ANetworkName : None
//arg[3] AIncludingChildren : None
TSAPI(s32) tscom_lin_rbs_activate_network_by_name(const s32 AIdxChn,const bool AEnable,const char*  ANetworkName,const bool AIncludingChildren);
//arg[0] AIdxChn : None
//arg[1] AEnable : None
//arg[2] ANetworkName : None
//arg[3] ANodeName : None
//arg[4] AIncludingChildren : None
TSAPI(s32) tscom_lin_rbs_activate_node_by_name(const s32 AIdxChn,const bool AEnable,const char*  ANetworkName,const char*  ANodeName,const bool AIncludingChildren);
//arg[0] AIdxChn : None
//arg[1] AEnable : None
//arg[2] ANetworkName : None
//arg[3] ANodeName : None
//arg[4] AMsgName : None
TSAPI(s32) tscom_lin_rbs_activate_message_by_name(const s32 AIdxChn,const bool AEnable,const char*  ANetworkName,const char*  ANodeName,const char*  AMsgName);
//arg[0] AIdxChn : None
//arg[1] AIntervalMs : None
//arg[2] ANetworkName : None
//arg[3] ANodeName : None
//arg[4] AMsgName : None
TSAPI(s32) tscom_lin_rbs_set_message_delay_time_by_name(const s32 AIdxChn,const s32 AIntervalMs,const char*  ANetworkName,const char*  ANodeName,const char*  AMsgName);
//arg[0] AIdxChn : None
//arg[1] ANetworkName : None
//arg[2] ANodeName : None
//arg[3] AMsgName : None
//arg[4] ASignalName : None
//arg[5] AValue : None
TSAPI(s32) tscom_lin_rbs_get_signal_value_by_element(const s32 AIdxChn,const char*  ANetworkName,const char*  ANodeName,const char*  AMsgName,const char*  ASignalName,const pdouble AValue);
//arg[0] ASymbolAddress : None
//arg[1] AValue : None
TSAPI(s32) tscom_lin_rbs_get_signal_value_by_address(const char*  ASymbolAddress,const pdouble AValue);
//arg[0] AIdxChn : None
//arg[1] ANetworkName : None
//arg[2] ANodeName : None
//arg[3] AMsgName : None
//arg[4] ASignalName : None
//arg[5] AValue : None
TSAPI(s32) tscom_lin_rbs_set_signal_value_by_element(const s32 AIdxChn,const char*  ANetworkName,const char*  ANodeName,const char*  AMsgName,const char*  ASignalName,const double AValue);
//arg[0] ASymbolAddress : None
//arg[1] AValue : None
TSAPI(s32) tscom_lin_rbs_set_signal_value_by_address(const char*  ASymbolAddress,const double AValue);
TSAPI(s32) tscom_can_rbs_reload_settings();
TSAPI(s32) tscom_can_rbs_start();
TSAPI(s32) tscom_can_rbs_stop();
//arg[0] AIsRunning : None
TSAPI(s32) tscom_can_rbs_is_running(const pbool AIsRunning);
//arg[0] AAutoStart : None
//arg[1] AAutoSendOnModification : None
//arg[2] AActivateNodeSimulation : None
//arg[3] AInitValueOptions : None
TSAPI(s32) tscom_can_rbs_configure(const bool AAutoStart,const bool AAutoSendOnModification,const bool AActivateNodeSimulation,const s32 AInitValueOptions);
//arg[0] AEnable : None
//arg[1] AIncludingChildren : None
TSAPI(s32) tscom_can_rbs_activate_all_networks(const bool AEnable,const bool AIncludingChildren);
//arg[0] AIdxChn : None
//arg[1] AEnable : None
//arg[2] ANetworkName : None
//arg[3] AIncludingChildren : None
TSAPI(s32) tscom_can_rbs_activate_network_by_name(const s32 AIdxChn,const bool AEnable,const char*  ANetworkName,const bool AIncludingChildren);
//arg[0] AIdxChn : None
//arg[1] AEnable : None
//arg[2] ANetworkName : None
//arg[3] ANodeName : None
//arg[4] AIncludingChildren : None
TSAPI(s32) tscom_can_rbs_activate_node_by_name(const s32 AIdxChn,const bool AEnable,const char*  ANetworkName,const char*  ANodeName,const bool AIncludingChildren);
//arg[0] AIdxChn : None
//arg[1] AEnable : None
//arg[2] ANetworkName : None
//arg[3] ANodeName : None
//arg[4] AMsgName : None
TSAPI(s32) tscom_can_rbs_activate_message_by_name(const s32 AIdxChn,const bool AEnable,const char*  ANetworkName,const char*  ANodeName,const char*  AMsgName);
//arg[0] AIdxChn : None
//arg[1] AIntervalMs : None
//arg[2] ANetworkName : None
//arg[3] ANodeName : None
//arg[4] AMsgName : None
TSAPI(s32) tscom_can_rbs_set_message_cycle_by_name(const s32 AIdxChn,const s32 AIntervalMs,const char*  ANetworkName,const char*  ANodeName,const char*  AMsgName);
//arg[0] AIdxChn : None
//arg[1] ANetworkName : None
//arg[2] ANodeName : None
//arg[3] AMsgName : None
//arg[4] ASignalName : None
//arg[5] AValue : None
TSAPI(s32) tscom_can_rbs_get_signal_value_by_element(const s32 AIdxChn,const char*  ANetworkName,const char*  ANodeName,const char*  AMsgName,const char*  ASignalName,const pdouble AValue);
//arg[0] ASymbolAddress : None
//arg[1] AValue : None
TSAPI(s32) tscom_can_rbs_get_signal_value_by_address(const char*  ASymbolAddress,const pdouble AValue);
//arg[0] AIdxChn : None
//arg[1] ANetworkName : None
//arg[2] ANodeName : None
//arg[3] AMsgName : None
//arg[4] ASignalName : None
//arg[5] AValue : None
TSAPI(s32) tscom_can_rbs_set_signal_value_by_element(const s32 AIdxChn,const char*  ANetworkName,const char*  ANodeName,const char*  AMsgName,const char*  ASignalName,const double AValue);
//arg[0] ASymbolAddress : None
//arg[1] AValue : None
TSAPI(s32) tscom_can_rbs_set_signal_value_by_address(const char*  ASymbolAddress,const double AValue);
TSAPI(s32) tscom_flexray_rbs_start();
TSAPI(s32) tscom_flexray_rbs_stop();
//arg[0] AIsRunning : None
TSAPI(s32) tscom_flexray_rbs_is_running(const pbool AIsRunning);
//arg[0] AAutoStart : None
//arg[1] AAutoSendOnModification : None
//arg[2] AActivateECUSimulation : None
//arg[3] AInitValueOptions : None
TSAPI(s32) tscom_flexray_rbs_configure(const bool AAutoStart,const bool AAutoSendOnModification,const bool AActivateECUSimulation,const s32 AInitValueOptions);
//arg[0] AEnable : None
//arg[1] AIncludingChildren : None
TSAPI(s32) tscom_flexray_rbs_activate_all_clusters(const bool AEnable,const bool AIncludingChildren);
//arg[0] AIdxChn : None
//arg[1] AEnable : None
//arg[2] AClusterName : None
//arg[3] AIncludingChildren : None
TSAPI(s32) tscom_flexray_rbs_activate_cluster_by_name(const s32 AIdxChn,const bool AEnable,const char*  AClusterName,const bool AIncludingChildren);
//arg[0] AIdxChn : None
//arg[1] AEnable : None
//arg[2] AClusterName : None
//arg[3] AECUName : None
//arg[4] AIncludingChildren : None
TSAPI(s32) tscom_flexray_rbs_activate_ecu_by_name(const s32 AIdxChn,const bool AEnable,const char*  AClusterName,const char*  AECUName,const bool AIncludingChildren);
//arg[0] AIdxChn : None
//arg[1] AEnable : None
//arg[2] AClusterName : None
//arg[3] AECUName : None
//arg[4] AFrameName : None
TSAPI(s32) tscom_flexray_rbs_activate_frame_by_name(const s32 AIdxChn,const bool AEnable,const char*  AClusterName,const char*  AECUName,const char*  AFrameName);
//arg[0] AIdxChn : None
//arg[1] AClusterName : None
//arg[2] AECUName : None
//arg[3] AFrameName : None
//arg[4] ASignalName : None
//arg[5] AValue : None
TSAPI(s32) tscom_flexray_rbs_get_signal_value_by_element(const s32 AIdxChn,const char*  AClusterName,const char*  AECUName,const char*  AFrameName,const char*  ASignalName,const pdouble AValue);
//arg[0] AIdxChn : None
//arg[1] AClusterName : None
//arg[2] AECUName : None
//arg[3] AFrameName : None
//arg[4] ASignalName : None
//arg[5] AValue : None
TSAPI(s32) tscom_flexray_rbs_set_signal_value_by_element(const s32 AIdxChn,const char*  AClusterName,const char*  AECUName,const char*  AFrameName,const char*  ASignalName,const double AValue);
//arg[0] ASymbolAddress : None
//arg[1] AValue : None
TSAPI(s32) tscom_flexray_rbs_get_signal_value_by_address(const char*  ASymbolAddress,const pdouble AValue);
//arg[0] ASymbolAddress : None
//arg[1] AValue : None
TSAPI(s32) tscom_flexray_rbs_set_signal_value_by_address(const char*  ASymbolAddress,const double AValue);
//arg[0] AEnable : None
TSAPI(s32) tscom_flexray_rbs_enable(const bool AEnable);
TSAPI(s32) tscom_flexray_rbs_batch_set_start();
TSAPI(s32) tscom_flexray_rbs_batch_set_end();
//arg[0] AAddr : None
//arg[1] AValue : None
TSAPI(s32) tscom_flexray_rbs_batch_set_signal(const char*  AAddr,const double AValue);
//arg[0] AIdxChn : None
//arg[1] AIsTx : None
//arg[2] AClusterName : None
//arg[3] AECUName : None
//arg[4] AFrameName : None
TSAPI(s32) tscom_flexray_rbs_set_frame_direction(const s32 AIdxChn,const bool AIsTx,const char*  AClusterName,const char*  AECUName,const char*  AFrameName);
//arg[0] ASymbolAddress : None
TSAPI(s32) tscom_flexray_rbs_set_normal_signal(const char*  ASymbolAddress);
//arg[0] ASymbolAddress : None
TSAPI(s32) tscom_flexray_rbs_set_rc_signal(const char*  ASymbolAddress);
//arg[0] ASymbolAddress : None
//arg[1] ALowerLimit : None
//arg[2] AUpperLimit : None
TSAPI(s32) tscom_flexray_rbs_set_rc_signal_with_limit(const char*  ASymbolAddress,const s32 ALowerLimit,const s32 AUpperLimit);
//arg[0] ASymbolAddress : None
//arg[1] AAlgorithmName : None
//arg[2] AIdxByteStart : None
//arg[3] AByteCount : None
TSAPI(s32) tscom_flexray_rbs_set_crc_signal(const char*  ASymbolAddress,const char*  AAlgorithmName,const s32 AIdxByteStart,const s32 AByteCount);
//arg[0] AFlexRaySignal : None
//arg[1] AData : None
//arg[2] AValue : None
TSAPI(s32) tscom_flexray_set_signal_value_in_raw_frame(const PMPFlexRaySignal AFlexRaySignal,const pu8 AData,const double AValue);
//arg[0] AFlexRaySignal : None
//arg[1] AData : None
TSAPI(s32) tscom_flexray_get_signal_value_in_raw_frame(const PMPFlexRaySignal AFlexRaySignal,const pu8 AData);
//arg[0] ASignalAddress : None
//arg[1] ASignalDef : None
TSAPI(s32) tscom_flexray_get_signal_definition(const char*  ASignalAddress,const PMPFlexRaySignal ASignalDef);
//arg[0] AIdxChn : None
//arg[1] AControllerConfig : None
//arg[2] AFrameLengthArray : None
//arg[3] AFrameNum : None
//arg[4] AFrameTrigger : None
//arg[5] AFrameTriggerNum : None
//arg[6] ATimeoutMs : None
TSAPI(s32) tsflexray_set_controller_frametrigger(const s32 AIdxChn,const PLIBFlexray_controller_config AControllerConfig,const ps32 AFrameLengthArray,const s32 AFrameNum,const PLIBTrigger_def AFrameTrigger,const s32 AFrameTriggerNum,const s32 ATimeoutMs);
//arg[0] AIdxChn : None
//arg[1] AControllerConfig : None
//arg[2] ATimeoutMs : None
TSAPI(s32) tsflexray_set_controller(const s32 AIdxChn,const PLIBFlexray_controller_config AControllerConfig,const s32 ATimeoutMs);
//arg[0] AIdxChn : None
//arg[1] AFrameLengthArray : None
//arg[2] AFrameNum : None
//arg[3] AFrameTrigger : None
//arg[4] AFrameTriggerNum : None
//arg[5] ATimeoutMs : None
TSAPI(s32) tsflexray_set_frametrigger(const s32 AIdxChn,const ps32 AFrameLengthArray,const s32 AFrameNum,const PLIBTrigger_def AFrameTrigger,const s32 AFrameTriggerNum,const s32 ATimeoutMs);
//arg[0] AIdxChn : None
//arg[1] AAction : None
//arg[2] AWriteBuffer : None
//arg[3] AWriteBufferSize : None
//arg[4] AReadBuffer : None
//arg[5] AReadBufferSize : None
//arg[6] ATimeoutMs : None
TSAPI(s32) tsflexray_cmdreq(const s32 AIdxChn,const s32 AAction,const pu8 AWriteBuffer,const s32 AWriteBufferSize,const pu8 AReadBuffer,const ps32 AReadBufferSize,const s32 ATimeoutMs);
//arg[0] AData : None
//arg[1] ATimeoutMs : None
TSAPI(s32) tsapp_transmit_flexray_sync(const PLIBFlexRay AData,const s32 ATimeoutMs);
//arg[0] AData : None
TSAPI(s32) tsapp_transmit_flexray_async(const PLIBFlexRay AData);
//arg[0] AIdxChn : None
//arg[1] ATimeoutMs : None
TSAPI(s32) tsflexray_start_net(const s32 AIdxChn,const s32 ATimeoutMs);
//arg[0] AIdxChn : None
//arg[1] ATimeoutMs : None
TSAPI(s32) tsflexray_stop_net(const s32 AIdxChn,const s32 ATimeoutMs);
//arg[0] AIdxChn : None
//arg[1] ATimeoutMs : None
TSAPI(s32) tsflexray_wakeup_pattern(const s32 AIdxChn,const s32 ATimeoutMs);
//arg[0] AChnIdx : None
//arg[1] SlotID : None
//arg[2] BaseCycle : None
//arg[3] RepCycle : None
//arg[4] ATimeOut : None
TSAPI(s32) flexray_enable_frame(const s32 AChnIdx,const u8 SlotID,const u8 BaseCycle,const u8 RepCycle,const s32 ATimeOut);
//arg[0] AChnIdx : None
//arg[1] SlotID : None
//arg[2] BaseCycle : None
//arg[3] RepCycle : None
//arg[4] ATimeOut : None
TSAPI(s32) flexray_disable_frame(const s32 AChnIdx,const u8 SlotID,const u8 BaseCycle,const u8 RepCycle,const s32 ATimeOut);
//arg[0] AChnIdx : None
TSAPI(s32) tslin_switch_runtime_schedule_table(const s32 AChnIdx);
//arg[0] AChnIdx : None
TSAPI(s32) tslin_switch_idle_schedule_table(const s32 AChnIdx);
//arg[0] AChnIdx : None
//arg[1] ASchIndex : None
TSAPI(s32) tslin_switch_normal_schedule_table(const s32 AChnIdx,const s32 ASchIndex);
//arg[0] AChnIdx : None
TSAPI(s32) tslin_stop_lin_channel(const s32 AChnIdx);
//arg[0] AChnIdx : None
TSAPI(s32) tslin_start_lin_channel(const s32 AChnIdx);
//arg[0] AChnIdx : None
//arg[1] AFunctionType : None
TSAPI(s32) tslin_set_node_functiontype(const s32 AChnIdx,const s32 AFunctionType);
//arg[0] AChnIdx : None
TSAPI(s32) tslin_batch_set_schedule_start(const s32 AChnIdx);
//arg[0] AChnIdx : None
//arg[1] ALINData : None
//arg[2] ADelayMs : None
TSAPI(s32) tslin_batch_add_schedule_frame(const s32 AChnIdx,const PLIBLIN ALINData,const s32 ADelayMs);
//arg[0] AChnIdx : None
TSAPI(s32) tslin_batch_set_schedule_end(const s32 AChnIdx);
//arg[0] AChnIdx : None
//arg[1] ANAD : None
//arg[2] AData : None
//arg[3] ADataNum : None
//arg[4] ATimeoutMs : None
TSAPI(s32) tstp_lin_master_request(const s32 AChnIdx,const u8 ANAD,const pu8 AData,const s32 ADataNum,const s32 ATimeoutMs);
//arg[0] AChnIdx : None
//arg[1] AData : None
TSAPI(s32) tstp_lin_master_request_intervalms(const s32 AChnIdx,const u16 AData);
//arg[0] AChnIdx : None
TSAPI(s32) tstp_lin_reset(const s32 AChnIdx);
//arg[0] AChnIdx : None
//arg[1] AData : None
TSAPI(s32) tstp_lin_slave_response_intervalms(const s32 AChnIdx,const u16 AData);
//arg[0] AChnIdx : None
//arg[1] AReqIntervalMs : None
//arg[2] AResIntervalMs : None
//arg[3] AResRetryTime : None
TSAPI(s32) tstp_lin_tp_para_default(const s32 AChnIdx,const u16 AReqIntervalMs,const u16 AResIntervalMs,const u16 AResRetryTime);
//arg[0] AChnIdx : None
//arg[1] AReqIntervalMs : None
//arg[2] AResIntervalMs : None
//arg[3] AResRetryTime : None
TSAPI(s32) tstp_lin_tp_para_special(const s32 AChnIdx,const u16 AReqIntervalMs,const u16 AResIntervalMs,const u16 AResRetryTime);
//arg[0] AChnIdx : None
//arg[1] ANAD : None
//arg[2] AId : None
//arg[3] AResNAD : None
//arg[4] AResData : None
//arg[5] AResDataNum : None
//arg[6] ATimeoutMS : None
TSAPI(s32) tsdiag_lin_read_data_by_identifier(const s32 AChnIdx,const u8 ANAD,const u16 AId,const pu8 AResNAD,const pu8 AResData,const ps32 AResDataNum,const s32 ATimeoutMS);
//arg[0] AChnIdx : None
//arg[1] AReqNAD : None
//arg[2] AID : None
//arg[3] AReqData : None
//arg[4] AReqDataNum : None
//arg[5] AResNAD : None
//arg[6] AResData : None
//arg[7] AResDataNum : None
//arg[8] ATimeoutMS : None
TSAPI(s32) tsdiag_lin_write_data_by_identifier(const s32 AChnIdx,const u8 AReqNAD,const u16 AID,const pu8 AReqData,const s32 AReqDataNum,const pu8 AResNAD,const pu8 AResData,const ps32 AResDataNum,const s32 ATimeoutMS);
//arg[0] AChnIdx : None
//arg[1] ANAD : None
//arg[2] ANewSession : None
//arg[3] ATimeoutMS : None
TSAPI(s32) tsdiag_lin_session_control(const s32 AChnIdx,const u8 ANAD,const u8 ANewSession,const s32 ATimeoutMS);
//arg[0] AChnIdx : None
//arg[1] ANAD : None
//arg[2] ATimeoutMS : None
TSAPI(s32) tsdiag_lin_fault_memory_read(const s32 AChnIdx,const u8 ANAD,const s32 ATimeoutMS);
//arg[0] AChnIdx : None
//arg[1] ANAD : None
//arg[2] ATimeoutMS : None
TSAPI(s32) tsdiag_lin_fault_memory_clear(const s32 AChnIdx,const u8 ANAD,const s32 ATimeoutMS);
//arg[0] pDiagModuleIndex : None
//arg[1] AChnIndex : None
//arg[2] ASupportFDCAN : None
//arg[3] AMaxDLC : None
//arg[4] ARequestID : None
//arg[5] ARequestIDIsStd : None
//arg[6] AResponseID : None
//arg[7] AResponseIDIsStd : None
//arg[8] AFunctionID : None
//arg[9] AFunctionIDIsStd : None
TSAPI(s32) tsdiag_can_create(const ps32 pDiagModuleIndex,const s32 AChnIndex,const u8 ASupportFDCAN,const u8 AMaxDLC,const u32 ARequestID,const bool ARequestIDIsStd,const u32 AResponseID,const bool AResponseIDIsStd,const u32 AFunctionID,const bool AFunctionIDIsStd);
//arg[0] ADiagModuleIndex : None
TSAPI(s32) tsdiag_can_delete(const s32 ADiagModuleIndex);
TSAPI(s32) tsdiag_can_delete_all();
//arg[0] ADiagModuleIndex : None
//arg[1] AChnIndex : None
TSAPI(s32) tsdiag_set_channel(const s32 ADiagModuleIndex,const s32 AChnIndex);
//arg[0] ADiagModuleIndex : None
//arg[1] AFDMode : None
//arg[2] AMaxLength : None
TSAPI(s32) tsdiag_set_fdmode(const s32 ADiagModuleIndex,const bool AFDMode,const s32 AMaxLength);
//arg[0] ADiagModuleIndex : None
//arg[1] ARequestID : None
//arg[2] AIsStandard : None
TSAPI(s32) tsdiag_set_request_id(const s32 ADiagModuleIndex,const s32 ARequestID,const bool AIsStandard);
//arg[0] ADiagModuleIndex : None
//arg[1] ARequestID : None
//arg[2] AIsStandard : None
TSAPI(s32) tsdiag_set_response_id(const s32 ADiagModuleIndex,const s32 ARequestID,const bool AIsStandard);
//arg[0] ADiagModuleIndex : None
//arg[1] ARequestID : None
//arg[2] AIsStandard : None
TSAPI(s32) tsdiag_set_function_id(const s32 ADiagModuleIndex,const s32 ARequestID,const bool AIsStandard);
//arg[0] ADiagModuleIndex : None
//arg[1] ASTMin : None
TSAPI(s32) tsdiag_set_stmin(const s32 ADiagModuleIndex,const s32 ASTMin);
//arg[0] ADiagModuleIndex : None
//arg[1] ABlockSize : None
TSAPI(s32) tsdiag_set_blocksize(const s32 ADiagModuleIndex,const s32 ABlockSize);
//arg[0] ADiagModuleIndex : None
//arg[1] AMaxLength : None
TSAPI(s32) tsdiag_set_maxlength(const s32 ADiagModuleIndex,const s32 AMaxLength);
//arg[0] ADiagModuleIndex : None
//arg[1] AFCDelay : None
TSAPI(s32) tsdiag_set_fcdelay(const s32 ADiagModuleIndex,const s32 AFCDelay);
//arg[0] ADiagModuleIndex : None
//arg[1] AFilledByte : None
TSAPI(s32) tsdiag_set_filled_byte(const s32 ADiagModuleIndex,const u8 AFilledByte);
//arg[0] ADiagModuleIndex : None
//arg[1] ATimeMs : None
TSAPI(s32) tsdiag_set_p2_timeout(const s32 ADiagModuleIndex,const s32 ATimeMs);
//arg[0] ADiagModuleIndex : None
//arg[1] ATimeMs : None
TSAPI(s32) tsdiag_set_p2_extended(const s32 ADiagModuleIndex,const s32 ATimeMs);
//arg[0] ADiagModuleIndex : None
//arg[1] ATimeMs : None
TSAPI(s32) tsdiag_set_s3_servertime(const s32 ADiagModuleIndex,const s32 ATimeMs);
//arg[0] ADiagModuleIndex : None
//arg[1] ATimeMs : None
TSAPI(s32) tsdiag_set_s3_clienttime(const s32 ADiagModuleIndex,const s32 ATimeMs);
//arg[0] ADiagModuleIndex : None
//arg[1] AReqDataArray : None
//arg[2] AReqDataSize : None
TSAPI(s32) tstp_can_send_functional(const s32 ADiagModuleIndex,const pu8 AReqDataArray,const s32 AReqDataSize);
//arg[0] ADiagModuleIndex : None
//arg[1] AReqDataArray : None
//arg[2] AReqDataSize : None
TSAPI(s32) tstp_can_send_request(const s32 ADiagModuleIndex,const pu8 AReqDataArray,const s32 AReqDataSize);
//arg[0] ADiagModuleIndex : None
//arg[1] AReqDataArray : None
//arg[2] AReqDataSize : None
//arg[3] AResponseDataArray : None
//arg[4] AResponseDataSize : None
TSAPI(s32) tstp_can_request_and_get_response(const s32 ADiagModuleIndex,const pu8 AReqDataArray,const s32 AReqDataSize,const pu8 AResponseDataArray,const ps32 AResponseDataSize);
//arg[0] ADiagModuleIndex : None
//arg[1] ATxcompleted : None
TSAPI(s32) tstp_can_register_tx_completed_recall(const s32 ADiagModuleIndex,const N_USData_TranslateCompleted_Recall ATxcompleted);
//arg[0] ADiagModuleIndex : None
//arg[1] ARxcompleted : None
TSAPI(s32) tstp_can_register_rx_completed_recall(const s32 ADiagModuleIndex,const N_USData_TranslateCompleted_Recall ARxcompleted);
//arg[0] ADiagModuleIndex : None
//arg[1] ATxcompleted : None
TSAPI(s32) tstp_can_register_tx_completed_recall_internal(const s32 ADiagModuleIndex,const N_USData_TranslateCompleted_Recall_Obj ATxcompleted);
//arg[0] ADiagModuleIndex : None
//arg[1] ARxcompleted : None
TSAPI(s32) tstp_can_register_rx_completed_recall_internal(const s32 ADiagModuleIndex,const N_USData_TranslateCompleted_Recall_Obj ARxcompleted);
//arg[0] ADiagModuleIndex : None
//arg[1] ASubSession : None
TSAPI(s32) tsdiag_can_session_control(const s32 ADiagModuleIndex,const u8 ASubSession);
//arg[0] ADiagModuleIndex : None
//arg[1] ARoutineControlType : None
//arg[2] ARoutintID : None
TSAPI(s32) tsdiag_can_routine_control(const s32 ADiagModuleIndex,const u8 ARoutineControlType,const u16 ARoutintID);
//arg[0] ADiagModuleIndex : None
//arg[1] AControlType : None
TSAPI(s32) tsdiag_can_communication_control(const s32 ADiagModuleIndex,const u8 AControlType);
//arg[0] ADiagModuleIndex : None
//arg[1] ALevel : None
//arg[2] ARecSeed : None
//arg[3] ARecSeedSize : None
TSAPI(s32) tsdiag_can_security_access_request_seed(const s32 ADiagModuleIndex,const s32 ALevel,const pu8 ARecSeed,const ps32 ARecSeedSize);
//arg[0] ADiagModuleIndex : None
//arg[1] ALevel : None
//arg[2] AKeyValue : None
//arg[3] AKeySize : None
TSAPI(s32) tsdiag_can_security_access_send_key(const s32 ADiagModuleIndex,const s32 ALevel,const pu8 AKeyValue,const s32 AKeySize);
//arg[0] ADiagModuleIndex : None
//arg[1] AMemAddr : None
//arg[2] AMemSize : None
TSAPI(s32) tsdiag_can_request_download(const s32 ADiagModuleIndex,const s32 AMemAddr,const u32 AMemSize);
//arg[0] ADiagModuleIndex : None
//arg[1] AMemAddr : None
//arg[2] AMemSize : None
TSAPI(s32) tsdiag_can_request_upload(const s32 ADiagModuleIndex,const s32 AMemAddr,const u32 AMemSize);
//arg[0] ADiagModuleIndex : None
//arg[1] ASourceDatas : None
//arg[2] ADataSize : None
//arg[3] AReqCase : None
TSAPI(s32) tsdiag_can_transfer_data(const s32 ADiagModuleIndex,const pu8 ASourceDatas,const s32 ADataSize,const s32 AReqCase);
//arg[0] ADiagModuleIndex : None
TSAPI(s32) tsdiag_can_request_transfer_exit(const s32 ADiagModuleIndex);
//arg[0] ADiagModuleIndex : None
//arg[1] ADataIdentifier : None
//arg[2] AWriteData : None
//arg[3] AWriteDataSize : None
TSAPI(s32) tsdiag_can_write_data_by_identifier(const s32 ADiagModuleIndex,const u16 ADataIdentifier,const pu8 AWriteData,const s32 AWriteDataSize);
//arg[0] ADiagModuleIndex : None
//arg[1] ADataIdentifier : None
//arg[2] AReturnArray : None
//arg[3] AReturnArraySize : None
TSAPI(s32) tsdiag_can_read_data_by_identifier(const s32 ADiagModuleIndex,const u16 ADataIdentifier,const pu8 AReturnArray,const ps32 AReturnArraySize);
//arg[0] AChnIdx : None
//arg[1] AFileIndex : None
//arg[2] ATimeoutMS : None
TSAPI(s32) tslog_logger_delete_file(const s32 AChnIdx,const s32 AFileIndex,const s32 ATimeoutMS);
//arg[0] AChnIdx : None
//arg[1] AFileIndex : None
//arg[2] ABlfFileName : None
//arg[3] AStartTimeUs : None
//arg[4] AMaxSize : None
//arg[5] AProgress : None
//arg[6] AYear : None
//arg[7] AMonth : None
//arg[8] ADay : None
//arg[9] AHour : None
//arg[10] AMinute : None
//arg[11] ASecond : None
//arg[12] AMinisecond : None
//arg[13] ATimeoutMS : None
TSAPI(s32) tslog_logger_start_export_blf_file(const s32 AChnIdx,const s32 AFileIndex,const char*  ABlfFileName,const u64 AStartTimeUs,const s32 AMaxSize,const pdouble AProgress,const u16 AYear,const u16 AMonth,const u16 ADay,const u16 AHour,const u16 AMinute,const u16 ASecond,const u16 AMinisecond,const s32 ATimeoutMS);
//arg[0] AChnIdx : None
//arg[1] ATimeoutMS : None
TSAPI(s32) tslog_logger_abort_export_blf_file(const s32 AChnIdx,const s32 ATimeoutMS);
//arg[0] AChnIdx : None
//arg[1] AFileIndex : None
//arg[2] AStartTimeUs : None
//arg[3] AMaxSize : None
//arg[4] ATimeoutMS : None
TSAPI(s32) tslog_logger_start_online_replay(const s32 AChnIdx,const s32 AFileIndex,const u64 AStartTimeUs,const s32 AMaxSize,const s32 ATimeoutMS);
//arg[0] AChnIdx : None
//arg[1] AFileIndex : None
//arg[2] AStartTimeUs : None
//arg[3] AMaxSize : None
//arg[4] ATimeoutMS : None
TSAPI(s32) tslog_logger_start_offline_replay(const s32 AChnIdx,const s32 AFileIndex,const u64 AStartTimeUs,const s32 AMaxSize,const s32 ATimeoutMS);
//arg[0] AChnIdx : None
//arg[1] ATimeoutMS : None
TSAPI(s32) tslog_logger_stop_replay(const s32 AChnIdx,const s32 ATimeoutMS);
//arg[0] AChnIdx : None
//arg[1] AMode : None
//arg[2] ATimeoutMS : None
TSAPI(s32) tslog_logger_set_logger_mode(const s32 AChnIdx,const u8 AMode,const s32 ATimeoutMS);
//arg[0] AChnIdx : None
//arg[1] AEnable : None
//arg[2] ATimeoutMS : None
TSAPI(s32) tsapp_logger_enable_gps_module(const s32 AChnIdx,const s32 AEnable,const s32 ATimeoutMS);
//arg[0] AChnIdx : None
//arg[1] AInitBaudrate : None
//arg[2] ATargetBaudrate : None
//arg[3] ATimeoutMS : None
TSAPI(s32) tsapp_reset_gps_module(const s32 AChnIdx,const s32 AInitBaudrate,const s32 ATargetBaudrate,const s32 ATimeoutMS);
//arg[0] AChnIdx : None
TSAPI(s32) tsapp_unlock_camera_channel(const s32 AChnIdx);
TSAPI(s32) tsmp_reload_settings();
//arg[0] AMPFileName : None
//arg[1] ARunAfterLoad : None
TSAPI(s32) tsmp_load(const char*  AMPFileName,const bool ARunAfterLoad);
//arg[0] AMPFileName : None
TSAPI(s32) tsmp_unload(const char*  AMPFileName);
TSAPI(s32) tsmp_unload_all();
//arg[0] AMPFileName : None
TSAPI(s32) tsmp_run(const char*  AMPFileName);
//arg[0] AMPFileName : None
//arg[1] AIsRunning : None
TSAPI(s32) tsmp_is_running(const char*  AMPFileName,const pbool AIsRunning);
//arg[0] AMPFileName : None
TSAPI(s32) tsmp_stop(const char*  AMPFileName);
TSAPI(s32) tsmp_run_all();
TSAPI(s32) tsmp_stop_all();
//arg[0] AGroupName : None
//arg[1] AFuncName : None
//arg[2] AInParameters : None
//arg[3] AOutParameters : None
TSAPI(s32) tsmp_call_function(const char*  AGroupName,const char*  AFuncName,const char*  AInParameters,const ppchar AOutParameters);
//arg[0] AGroupName : None
//arg[1] AFuncName : None
//arg[2] AAddress : None
TSAPI(s32) tsmp_get_function_address(const char*  AGroupName,const char*  AFuncName,const ps32 AAddress);
//arg[0] AGroupName : None
//arg[1] AFuncName : None
//arg[2] APrototype : None
TSAPI(s32) tsmp_get_function_prototype(const char*  AGroupName,const char*  AFuncName,const ppchar APrototype);
//arg[0] AGroupName : None
//arg[1] AList : None
TSAPI(s32) tsmp_get_mp_function_list(const char*  AGroupName,const ppchar AList);
//arg[0] AList : None
TSAPI(s32) tsmp_get_mp_list(const ppchar AList);
//arg[0] AIdxChn : None
//arg[1] AClusterName : None
//arg[2] AValue : None
TSAPI(s32) db_get_flexray_cluster_parameters(const s32 AIdxChn,const char*  AClusterName,const PLIBFlexRayClusterParameters AValue);
//arg[0] AIdxChn : None
//arg[1] AClusterName : None
//arg[2] AECUName : None
//arg[3] AValue : None
TSAPI(s32) db_get_flexray_controller_parameters(const s32 AIdxChn,const char*  AClusterName,const char*  AECUName,const PLIBFlexRayControllerParameters AValue);
//arg[0] ACompleteName : None
//arg[1] ASupport : None
TSAPI(s32) set_system_var_event_support(const char*  ACompleteName,const bool ASupport);
//arg[0] ACompleteName : None
//arg[1] ASupport : None
TSAPI(s32) get_system_var_event_support(const char*  ACompleteName,const pbool ASupport);
//arg[0] AYear : None
//arg[1] AMonth : None
//arg[2] ADay : None
//arg[3] AHour : None
//arg[4] AMinute : None
//arg[5] ASecond : None
//arg[6] AMilliseconds : None
TSAPI(s32) get_date_time(const ps32 AYear,const ps32 AMonth,const ps32 ADay,const ps32 AHour,const ps32 AMinute,const ps32 ASecond,const ps32 AMilliseconds);
//arg[0] AIndex : None
TSAPI(s32) tslog_disable_online_replay_filter(const s32 AIndex);
//arg[0] AIndex : None
//arg[1] AIsPassFilter : None
//arg[2] ACount : None
//arg[3] AIdxChannels : None
//arg[4] AIdentifiers : None
TSAPI(s32) tslog_set_online_replay_filter(const s32 AIndex,const bool AIsPassFilter,const s32 ACount,const ps32 AIdxChannels,const ps32 AIdentifiers);
//arg[0] ACANSignal : None
//arg[1] AData : None
//arg[2] AValue : None
TSAPI(s32) set_can_signal_raw_value(const PMPCANSignal ACANSignal,const pu8 AData,const s64 AValue);
//arg[0] ACANSignal : None
//arg[1] AData : None
TSAPI(u64) get_can_signal_raw_value(const PMPCANSignal ACANSignal,const pu8 AData);
//arg[0] ALINSignal : None
//arg[1] AData : None
//arg[2] AValue : None
TSAPI(s32) set_lin_signal_raw_value(const PMPLINSignal ALINSignal,const pu8 AData,const s64 AValue);
//arg[0] ALINSignal : None
//arg[1] AData : None
TSAPI(u64) get_lin_signal_raw_value(const PMPLINSignal ALINSignal,const pu8 AData);
//arg[0] AFlexRaySignal : None
//arg[1] AData : None
//arg[2] AValue : None
TSAPI(s32) set_flexray_signal_raw_value(const PMPFlexRaySignal AFlexRaySignal,const pu8 AData,const double AValue);
//arg[0] AFlexRaySignal : None
//arg[1] AData : None
TSAPI(u64) get_flexray_signal_raw_value(const PMPFlexRaySignal AFlexRaySignal,const pu8 AData);
//arg[0] AFlexRaySignal : None
//arg[1] AData : None
//arg[2] AValue : None
TSAPI(s32) tscom_set_lin_signal_value(const PMPLINSignal AFlexRaySignal,const pu8 AData,const double AValue);
//arg[0] AFlexRaySignal : None
//arg[1] AData : None
//arg[2] AValue : None
TSAPI(s32) tscom_set_flexray_signal_value(const PMPFlexRaySignal AFlexRaySignal,const pu8 AData,const double AValue);
//arg[0] AFlexRaySignal : None
//arg[1] AData : None
//arg[2] AValue : None
TSAPI(s32) tscom_set_can_signal_value(const PMPCANSignal AFlexRaySignal,const pu8 AData,const double AValue);
//arg[0] AFlexRaySignal : None
//arg[1] AData : None
TSAPI(double) tscom_get_lin_signal_value(const PMPLINSignal AFlexRaySignal,const pu8 AData);
//arg[0] AFlexRaySignal : None
//arg[1] AData : None
TSAPI(double) tscom_get_flexray_signal_value(const PMPFlexRaySignal AFlexRaySignal,const pu8 AData);
//arg[0] AFlexRaySignal : None
//arg[1] AData : None
TSAPI(double) tscom_get_can_signal_value(const PMPCANSignal AFlexRaySignal,const pu8 AData);
TSAPI(s32) gpg_delete_all_modules();
//arg[0] AProgramName : None
//arg[1] ADisplayName : None
//arg[2] AModuleId : None
//arg[3] AEntryPointId : None
TSAPI(s32) gpg_create_module(const char*  AProgramName,const char*  ADisplayName,const ps64 AModuleId,const ps64 AEntryPointId);
//arg[0] AModuleId : None
TSAPI(s32) gpg_delete_module(const s64 AModuleId);
//arg[0] AModuleId : None
//arg[1] AGraphicProgramWindowTitle : None
TSAPI(s32) gpg_deploy_module(const s64 AModuleId,const char*  AGraphicProgramWindowTitle);
//arg[0] AModuleId : None
//arg[1] AUpperActionId : None
//arg[2] ADisplayName : None
//arg[3] AComment : None
//arg[4] AActionId : None
TSAPI(s32) gpg_add_action_down(const s64 AModuleId,const s64 AUpperActionId,const char*  ADisplayName,const char*  AComment,const ps64 AActionId);
//arg[0] AModuleId : None
//arg[1] ALeftActionId : None
//arg[2] ADisplayName : None
//arg[3] AComment : None
//arg[4] AActionId : None
TSAPI(s32) gpg_add_action_right(const s64 AModuleId,const s64 ALeftActionId,const char*  ADisplayName,const char*  AComment,const ps64 AActionId);
//arg[0] AModuleId : None
//arg[1] AUpperActionId : None
//arg[2] ADisplayName : None
//arg[3] AComment : None
//arg[4] AJumpLabel : None
//arg[5] AActionId : None
TSAPI(s32) gpg_add_goto_down(const s64 AModuleId,const s64 AUpperActionId,const char*  ADisplayName,const char*  AComment,const char*  AJumpLabel,const ps64 AActionId);
//arg[0] AModuleId : None
//arg[1] ALeftActionId : None
//arg[2] ADisplayName : None
//arg[3] AComment : None
//arg[4] AJumpLabel : None
//arg[5] AActionId : None
TSAPI(s32) gpg_add_goto_right(const s64 AModuleId,const s64 ALeftActionId,const char*  ADisplayName,const char*  AComment,const char*  AJumpLabel,const ps64 AActionId);
//arg[0] AModuleId : None
//arg[1] AUpperActionId : None
//arg[2] ADisplayName : None
//arg[3] AComment : None
//arg[4] AJumpLabel : None
//arg[5] AActionId : None
TSAPI(s32) gpg_add_from_down(const s64 AModuleId,const s64 AUpperActionId,const char*  ADisplayName,const char*  AComment,const char*  AJumpLabel,const ps64 AActionId);
//arg[0] AModuleId : None
//arg[1] AUpperActionId : None
//arg[2] ADisplayName : None
//arg[3] AComment : None
//arg[4] AGroupId : None
//arg[5] AEntryPointId : None
TSAPI(s32) gpg_add_group_down(const s64 AModuleId,const s64 AUpperActionId,const char*  ADisplayName,const char*  AComment,const ps64 AGroupId,const ps64 AEntryPointId);
//arg[0] AModuleId : None
//arg[1] ALeftActionId : None
//arg[2] ADisplayName : None
//arg[3] AComment : None
//arg[4] AGroupId : None
//arg[5] AEntryPointId : None
TSAPI(s32) gpg_add_group_right(const s64 AModuleId,const s64 ALeftActionId,const char*  ADisplayName,const char*  AComment,const ps64 AGroupId,const ps64 AEntryPointId);
//arg[0] AModuleId : None
//arg[1] AActionId : None
TSAPI(s32) gpg_delete_action(const s64 AModuleId,const s64 AActionId);
//arg[0] AModuleId : None
//arg[1] AActionId : None
TSAPI(s32) gpg_set_action_nop(const s64 AModuleId,const s64 AActionId);
//arg[0] AModuleId : None
//arg[1] AActionId : None
TSAPI(s32) gpg_set_action_signal_read_write(const s64 AModuleId,const s64 AActionId);
//arg[0] AModuleId : None
//arg[1] AActionId : None
TSAPI(s32) gpg_set_action_api_call(const s64 AModuleId,const s64 AActionId);
//arg[0] AModuleId : None
//arg[1] AActionId : None
TSAPI(s32) gpg_set_action_expression(const s64 AModuleId,const s64 AActionId);
//arg[0] AModuleId : None
//arg[1] AActionId : None
//arg[2] ADisplayName : None
//arg[3] AComment : None
//arg[4] ATimeoutMs : None
TSAPI(s32) gpg_configure_action_basic(const s64 AModuleId,const s64 AActionId,const char*  ADisplayName,const char*  AComment,const s32 ATimeoutMs);
//arg[0] AModuleId : None
//arg[1] AActionId : None
//arg[2] ADisplayName : None
//arg[3] AComment : None
//arg[4] AJumpLabel : None
TSAPI(s32) gpg_configure_goto(const s64 AModuleId,const s64 AActionId,const char*  ADisplayName,const char*  AComment,const char*  AJumpLabel);
//arg[0] AModuleId : None
//arg[1] AActionId : None
//arg[2] ADisplayName : None
//arg[3] AComment : None
//arg[4] AJumpLabel : None
TSAPI(s32) gpg_configure_from(const s64 AModuleId,const s64 AActionId,const char*  ADisplayName,const char*  AComment,const char*  AJumpLabel);
//arg[0] AModuleId : None
//arg[1] AActionId : None
//arg[2] ANextDirectionIsDown : None
//arg[3] AResultOK : None
//arg[4] AJumpBackIfEnded : None
TSAPI(s32) gpg_configure_nop(const s64 AModuleId,const s64 AActionId,const bool ANextDirectionIsDown,const bool AResultOK,const bool AJumpBackIfEnded);
//arg[0] AModuleId : None
//arg[1] AActionId : None
//arg[2] ARepeatCountType : None
//arg[3] ARepeatCountRepr : None
TSAPI(s32) gpg_configure_group(const s64 AModuleId,const s64 AActionId,const s32 ARepeatCountType,const char*  ARepeatCountRepr);
//arg[0] AModuleId : None
//arg[1] AActionId : None
TSAPI(s32) gpg_configure_signal_read_write_list_clear(const s64 AModuleId,const s64 AActionId);
//arg[0] AModuleId : None
//arg[1] AActionId : None
//arg[2] ADestSignalType : None
//arg[3] ASrcSignalType : None
//arg[4] ADestSignalExpr : None
//arg[5] ASrcSignalExpr : None
//arg[6] AItemIndex : None
TSAPI(s32) gpg_configure_signal_write_list_append(const s64 AModuleId,const s64 AActionId,const s32 ADestSignalType,const s32 ASrcSignalType,const char*  ADestSignalExpr,const char*  ASrcSignalExpr,const ps32 AItemIndex);
//arg[0] AModuleId : None
//arg[1] AActionId : None
//arg[2] AIsConditionAND : None
//arg[3] ADestSignalType : None
//arg[4] AMinSignalType : None
//arg[5] AMaxSignalType : None
//arg[6] ADestSignalExpr : None
//arg[7] AMinSignalExpr : None
//arg[8] AMaxSignalExpr : None
//arg[9] AItemIndex : None
TSAPI(s32) gpg_configure_signal_read_list_append(const s64 AModuleId,const s64 AActionId,const bool AIsConditionAND,const s32 ADestSignalType,const s32 AMinSignalType,const s32 AMaxSignalType,const char*  ADestSignalExpr,const char*  AMinSignalExpr,const char*  AMaxSignalExpr,const ps32 AItemIndex);
//arg[0] AModuleId : None
//arg[1] AActionId : None
//arg[2] AAPIType : None
//arg[3] AAPIName : None
//arg[4] AAPIArgTypes : None
//arg[5] AAPIArgNames : None
//arg[6] AAPIArgExprs : None
//arg[7] AArraySize : None
TSAPI(s32) gpg_configure_api_call_arguments(const s64 AModuleId,const s64 AActionId,const s32 AAPIType,const char*  AAPIName,const s32 AAPIArgTypes,const char*  AAPIArgNames,const char*  AAPIArgExprs,const s32 AArraySize);
//arg[0] AModuleId : None
//arg[1] AActionId : None
//arg[2] AIgnoreResult : None
//arg[3] ASignalType : None
//arg[4] ASignalExpr : None
TSAPI(s32) gpg_configure_api_call_result(const s64 AModuleId,const s64 AActionId,const bool AIgnoreResult,const s32 ASignalType,const char*  ASignalExpr);
//arg[0] AModuleId : None
//arg[1] AActionId : None
//arg[2] AxCount : None
//arg[3] AExpression : None
//arg[4] AArgumentTypes : None
//arg[5] AArgumentExprs : None
//arg[6] AResultType : None
//arg[7] AResultExpr : None
TSAPI(s32) gpg_configure_expression(const s64 AModuleId,const s64 AActionId,const s32 AxCount,const char*  AExpression,const ps32 AArgumentTypes,const ppchar AArgumentExprs,const s32 AResultType,const char*  AResultExpr);
//arg[0] AModuleId : None
//arg[1] AType : None
//arg[2] AName : None
//arg[3] AInitValue : None
//arg[4] AComment : None
//arg[5] AItemIndex : None
TSAPI(s32) gpg_add_local_var(const s64 AModuleId,const s32 AType,const char*  AName,const char*  AInitValue,const char*  AComment,const ps32 AItemIndex);
//arg[0] AModuleId : None
//arg[1] AItemIndex : None
TSAPI(s32) gpg_delete_local_var(const s64 AModuleId,const ps32 AItemIndex);
//arg[0] AModuleId : None
TSAPI(s32) gpg_delete_all_local_vars(const s64 AModuleId);
//arg[0] AModuleId : None
//arg[1] AGroupId : None
TSAPI(s32) gpg_delete_group_items(const s64 AModuleId,const s64 AGroupId);
//arg[0] AModuleId : None
//arg[1] AActionId : None
//arg[2] AItemIndex : None
TSAPI(s32) gpg_configure_signal_read_write_list_delete(const s64 AModuleId,const s64 AActionId,const s32 AItemIndex);
//arg[0] AFlexRay : None
TSAPI(s32) flexray_rbs_update_frame_by_header(const PLIBFlexRay AFlexRay);
//arg[0] AModuleId : None
//arg[1] AProgramName : None
//arg[2] ADisplayName : None
//arg[3] ARepeatCount : None
//arg[4] ASelected : None
TSAPI(s32) gpg_configure_module(const s64 AModuleId,const char*  AProgramName,const char*  ADisplayName,const s32 ARepeatCount,const bool ASelected);
//arg[0] APath : None
TSAPI(s32) add_path_to_environment(const char*  APath);
//arg[0] APath : None
TSAPI(s32) delete_path_from_environment(const char*  APath);
//arg[0] ACompleteName : None
//arg[1] AValue : None
//arg[2] ATimeUs : None
TSAPI(s32) set_system_var_double_w_time(const char*  ACompleteName,const double AValue,const s64 ATimeUs);
//arg[0] ACompleteName : None
//arg[1] AValue : None
//arg[2] ATimeUs : None
TSAPI(s32) set_system_var_int32_w_time(const char*  ACompleteName,const s32 AValue,const s64 ATimeUs);
//arg[0] ACompleteName : None
//arg[1] AValue : None
//arg[2] ATimeUs : None
TSAPI(s32) set_system_var_uint32_w_time(const char*  ACompleteName,const u32 AValue,const s64 ATimeUs);
//arg[0] ACompleteName : None
//arg[1] AValue : None
//arg[2] ATimeUs : None
TSAPI(s32) set_system_var_int64_w_time(const char*  ACompleteName,const s64 AValue,const s64 ATimeUs);
//arg[0] ACompleteName : None
//arg[1] AValue : None
//arg[2] ATimeUs : None
TSAPI(s32) set_system_var_uint64_w_time(const char*  ACompleteName,const u64 AValue,const s64 ATimeUs);
//arg[0] ACompleteName : None
//arg[1] ACount : None
//arg[2] AValue : None
//arg[3] ATimeUs : None
TSAPI(s32) set_system_var_uint8_array_w_time(const char*  ACompleteName,const s32 ACount,const pu8 AValue,const s64 ATimeUs);
//arg[0] ACompleteName : None
//arg[1] ACount : None
//arg[2] AValue : None
//arg[3] ATimeUs : None
TSAPI(s32) set_system_var_int32_array_w_time(const char*  ACompleteName,const s32 ACount,const ps32 AValue,const s64 ATimeUs);
//arg[0] ACompleteName : None
//arg[1] ACount : None
//arg[2] AValue : None
//arg[3] ATimeUs : None
TSAPI(s32) set_system_var_double_array_w_time(const char*  ACompleteName,const s32 ACount,const pdouble AValue,const s64 ATimeUs);
//arg[0] ACompleteName : None
//arg[1] AValue : None
//arg[2] ATimeUs : None
TSAPI(s32) set_system_var_string_w_time(const char*  ACompleteName,const char*  AValue,const s64 ATimeUs);
//arg[0] ACompleteName : None
//arg[1] AValue : None
//arg[2] ATimeUs : None
TSAPI(s32) set_system_var_generic_w_time(const char*  ACompleteName,const char*  AValue,const s64 ATimeUs);
//arg[0] ACompleteName : None
//arg[1] AValue : None
//arg[2] ATimeUs : None
TSAPI(s32) set_system_var_double_async_w_time(const char*  ACompleteName,const double AValue,const s64 ATimeUs);
//arg[0] ACompleteName : None
//arg[1] AValue : None
//arg[2] ATimeUs : None
TSAPI(s32) set_system_var_int32_async_w_time(const char*  ACompleteName,const s32 AValue,const s64 ATimeUs);
//arg[0] ACompleteName : None
//arg[1] AValue : None
//arg[2] ATimeUs : None
TSAPI(s32) set_system_var_uint32_async_w_time(const char*  ACompleteName,const u32 AValue,const s64 ATimeUs);
//arg[0] ACompleteName : None
//arg[1] AValue : None
//arg[2] ATimeUs : None
TSAPI(s32) set_system_var_int64_async_w_time(const char*  ACompleteName,const s64 AValue,const s64 ATimeUs);
//arg[0] ACompleteName : None
//arg[1] AValue : None
//arg[2] ATimeUs : None
TSAPI(s32) set_system_var_uint64_async_w_time(const char*  ACompleteName,const u64 AValue,const s64 ATimeUs);
//arg[0] ACompleteName : None
//arg[1] ACount : None
//arg[2] AValue : None
//arg[3] ATimeUs : None
TSAPI(s32) set_system_var_uint8_array_async_w_time(const char*  ACompleteName,const s32 ACount,const pu8 AValue,const s64 ATimeUs);
//arg[0] ACompleteName : None
//arg[1] ACount : None
//arg[2] AValue : None
//arg[3] ATimeUs : None
TSAPI(s32) set_system_var_int32_array_async_w_time(const char*  ACompleteName,const s32 ACount,const ps32 AValue,const s64 ATimeUs);
//arg[0] ACompleteName : None
//arg[1] ACount : None
//arg[2] AValue : None
//arg[3] ATimeUs : None
TSAPI(s32) set_system_var_int64_array_async_w_time(const char*  ACompleteName,const s32 ACount,const ps64 AValue,const s64 ATimeUs);
//arg[0] ACompleteName : None
//arg[1] ACount : None
//arg[2] AValue : None
//arg[3] ATimeUs : None
TSAPI(s32) set_system_var_double_array_async_w_time(const char*  ACompleteName,const s32 ACount,const pdouble AValue,const s64 ATimeUs);
//arg[0] ACompleteName : None
//arg[1] AValue : None
//arg[2] ATimeUs : None
TSAPI(s32) set_system_var_string_async_w_time(const char*  ACompleteName,const char*  AValue,const s64 ATimeUs);
//arg[0] ACompleteName : None
//arg[1] AValue : None
//arg[2] ATimeUs : None
TSAPI(s32) set_system_var_generic_async_w_time(const char*  ACompleteName,const char*  AValue,const s64 ATimeUs);
//arg[0] ASignalStartBitInPDU : None
//arg[1] ASignalBitLength : None
//arg[2] AIsSignalIntel : None
//arg[3] AIsPDUIntel : None
//arg[4] APDUStartBit : None
//arg[5] APDUBitLength : None
//arg[6] AActualStartBit : None
TSAPI(s32) db_get_signal_startbit_by_pdu_offset(const s32 ASignalStartBitInPDU,const s32 ASignalBitLength,const bool AIsSignalIntel,const bool AIsPDUIntel,const s32 APDUStartBit,const s32 APDUBitLength,const ps32 AActualStartBit);
//arg[0] ATitle : None
//arg[1] AFileTypeDesc : None
//arg[2] AFilter : None
//arg[3] ASuggestFileName : None
//arg[4] ADestinationFileName : None
TSAPI(s32) ui_show_save_file_dialog(const char*  ATitle,const char*  AFileTypeDesc,const char*  AFilter,const char*  ASuggestFileName,const ppchar ADestinationFileName);
//arg[0] ATitle : None
//arg[1] AFileTypeDesc : None
//arg[2] AFilter : None
//arg[3] ASuggestFileName : None
//arg[4] ADestinationFileName : None
TSAPI(s32) ui_show_open_file_dialog(const char*  ATitle,const char*  AFileTypeDesc,const char*  AFilter,const char*  ASuggestFileName,const ppchar ADestinationFileName);
//arg[0] ADestinationFileName : None
TSAPI(s32) ui_show_select_directory_dialog(const ppchar ADestinationFileName);
//arg[0] AEthernetHeader : None
TSAPI(s32) tsapp_transmit_ethernet_async(const PLIBEthernetHeader AEthernetHeader);
//arg[0] AEthernetHeader : None
//arg[1] ATimeoutMs : None
TSAPI(s32) tsapp_transmit_ethernet_sync(const PLIBEthernetHeader AEthernetHeader,const s32 ATimeoutMs);
//arg[0] AEthernetHeader : None
TSAPI(s32) inject_ethernet_frame(const PLIBEthernetHeader AEthernetHeader);
//arg[0] AHandle : None
//arg[1] AEthernetHeader : None
TSAPI(s32) tslog_blf_write_ethernet(const s32 AHandle,const PLIBEthernetHeader AEthernetHeader);
//arg[0] ACount : None
TSAPI(s32) set_ethernet_channel_count(const s32 ACount);
//arg[0] ACount : None
TSAPI(s32) get_ethernet_channel_count(const ps32 ACount);
//arg[0] AEthernetHeader : None
TSAPI(s32) transmit_ethernet_async_wo_pretx(const PLIBEthernetHeader AEthernetHeader);
//arg[0] AId : None
//arg[1] AIndex : None
TSAPI(s32) db_get_can_db_index_by_id(const s32 AId,const ps32 AIndex);
//arg[0] AId : None
//arg[1] AIndex : None
TSAPI(s32) db_get_lin_db_index_by_id(const s32 AId,const ps32 AIndex);
//arg[0] AId : None
//arg[1] AIndex : None
TSAPI(s32) db_get_flexray_db_index_by_id(const s32 AId,const ps32 AIndex);
//arg[0] AHeader : None
//arg[1] ASrcIp : None
//arg[2] ADstIp : None
//arg[3] ASrcPort : None
//arg[4] ADstPort : None
//arg[5] APayload : None
//arg[6] APayloadLength : None
//arg[7] AIdentification : None
//arg[8] AFragmentIndex : None
TSAPI(s32) eth_build_ipv4_udp_packet(const PLIBEthernetHeader AHeader,const pu8 ASrcIp,const pu8 ADstIp,const u16 ASrcPort,const u16 ADstPort,const pu8 APayload,const u16 APayloadLength,const ps32 AIdentification,const ps32 AFragmentIndex);
//arg[0] ACompleteName : None
//arg[1] AEvent : None
TSAPI(s32) register_system_var_change_event(const char*  ACompleteName,const TLIBOnSysVarChange AEvent);
//arg[0] ACompleteName : None
//arg[1] AEvent : None
TSAPI(s32) unregister_system_var_change_event(const char*  ACompleteName,const TLIBOnSysVarChange AEvent);
//arg[0] AEvent : None
TSAPI(s32) unregister_system_var_change_events(const TLIBOnSysVarChange AEvent);
TSAPI(s32) block_current_pretx();
//arg[0] AAPIName : None
//arg[1] AArgCount : None
//arg[2] AArgCapacity : None
//arg[3] AArgs : None
TSAPI(s32) call_system_api(const char*  AAPIName,const s32 AArgCount,const s32 AArgCapacity,const ppchar AArgs);
//arg[0] AAPIName : None
//arg[1] AArgCount : None
//arg[2] AArgCapacity : None
//arg[3] AArgs : None
TSAPI(s32) call_library_api(const char*  AAPIName,const s32 AArgCount,const s32 AArgCapacity,const ppchar AArgs);
//arg[0] AHeader : None
//arg[1] AIdentification : None
//arg[2] AUDPPacketLength : None
//arg[3] AUDPDataOffset : None
//arg[4] AIsPacketEnded : None
TSAPI(s32) eth_is_udp_packet(const PLIBEthernetHeader AHeader,const pu16 AIdentification,const pu16 AUDPPacketLength,const pu16 AUDPDataOffset,const bool AIsPacketEnded);
//arg[0] AHeader : None
//arg[1] AOverwriteChecksum : None
//arg[2] AChecksum : None
TSAPI(s32) eth_ip_calc_header_checksum(const PLIBEthernetHeader AHeader,const bool AOverwriteChecksum,const pu16 AChecksum);
//arg[0] AHeader : None
//arg[1] AUDPPayloadAddr : None
//arg[2] AUDPPayloadLength : None
//arg[3] AOverwriteChecksum : None
//arg[4] AChecksum : None
TSAPI(s32) eth_udp_calc_checksum(const PLIBEthernetHeader AHeader,const pu8 AUDPPayloadAddr,const u16 AUDPPayloadLength,const bool AOverwriteChecksum,const pu16 AChecksum);
//arg[0] AHeader : None
//arg[1] AOverwriteChecksum : None
//arg[2] AChecksum : None
TSAPI(s32) eth_udp_calc_checksum_on_frame(const PLIBEthernetHeader AHeader,const bool AOverwriteChecksum,const pu16 AChecksum);
//arg[0] AHeader : None
TSAPI(s32) eth_log_ethernet_frame_data(const PLIBEthernetHeader AHeader);
TSAPI(s32) signal_tester_clear_all();
//arg[0] AFilePath : None
TSAPI(s32) signal_tester_load_configuration(const char*  AFilePath);
//arg[0] AFilePath : None
TSAPI(s32) signal_tester_save_configuration(const char*  AFilePath);
//arg[0] AName : None
TSAPI(s32) signal_tester_run_item_by_name(const char*  AName);
//arg[0] AName : None
TSAPI(s32) signal_tester_stop_item_by_name(const char*  AName);
//arg[0] AIndex : None
TSAPI(s32) signal_tester_run_item_by_index(const s32 AIndex);
//arg[0] AIndex : None
TSAPI(s32) signal_tester_stop_item_by_index(const s32 AIndex);
//arg[0] AObj : None
//arg[1] AIndex : None
//arg[2] AIsPass : None
TSAPI(s32) signal_tester_get_item_verdict_by_index(const ps32 AObj,const s32 AIndex,const pbool AIsPass);
//arg[0] AObj : None
//arg[1] AName : None
//arg[2] AIsPass : None
//arg[3] AEventTimeUs : None
//arg[4] ADescription : None
TSAPI(s32) signal_tester_get_item_result_by_name(const ps32 AObj,const char*  AName,const pbool AIsPass,const ps64 AEventTimeUs,const ppchar ADescription);
//arg[0] AObj : None
//arg[1] AIndex : None
//arg[2] AIsPass : None
//arg[3] AEventTimeUs : None
//arg[4] ADescription : None
TSAPI(s32) signal_tester_get_item_result_by_index(const ps32 AObj,const s32 AIndex,const pbool AIsPass,const ps64 AEventTimeUs,const ppchar ADescription);
//arg[0] AObj : None
//arg[1] AName : None
//arg[2] AIsPass : None
TSAPI(s32) signal_tester_get_item_verdict_by_name(const ps32 AObj,const char*  AName,const pbool AIsPass);
//arg[0] AHandle : None
//arg[1] ASection : None
//arg[2] AKey : None
//arg[3] AValue : None
//arg[4] AValueCapacity : None
//arg[5] ADefault : None
TSAPI(s32) ini_read_string_wo_quotes(const s32 AHandle,const char*  ASection,const char*  AKey,const char*  AValue,const ps32 AValueCapacity,const char*  ADefault);
//arg[0] AObj : None
//arg[1] AIndex : None
//arg[2] AMin : None
//arg[3] AMax : None
//arg[4] APass : None
//arg[5] AResult : None
//arg[6] AResultRepr : None
TSAPI(s32) signal_tester_check_statistics_by_index(const ps32 AObj,const s32 AIndex,const double AMin,const double AMax,const pbool APass,const pdouble AResult,const ppchar AResultRepr);
//arg[0] AObj : None
//arg[1] AItemName : None
//arg[2] AMin : None
//arg[3] AMax : None
//arg[4] APass : None
//arg[5] AResult : None
//arg[6] AResultRepr : None
TSAPI(s32) signal_tester_check_statistics_by_name(const ps32 AObj,const char*  AItemName,const double AMin,const double AMax,const pbool APass,const pdouble AResult,const ppchar AResultRepr);
//arg[0] AIndex : None
//arg[1] AEnable : None
TSAPI(s32) signal_tester_enable_item_by_index(const s32 AIndex,const bool AEnable);
//arg[0] AItemName : None
//arg[1] AEnable : None
TSAPI(s32) signal_tester_enable_item_by_name(const char*  AItemName,const bool AEnable);
TSAPI(s32) signal_tester_run_all();
TSAPI(s32) signal_tester_stop_all();
//arg[0] AChnIdx : None
TSAPI(s32) tslin_clear_schedule_tables(const s32 AChnIdx);
TSAPI(void) finalize_lib_tsmaster();
//arg[0] x : None
TSAPI(u16) tssocket_htons(const s32 x);
//arg[0] x : None
TSAPI(u16) tssocket_htonl(const s32 x);
//arg[0] cp : None
//arg[1] addr : None
TSAPI(void) tssocket_aton(const char*  cp,const Pip4_addr_t addr);
//arg[0] addr : None
TSAPI(pchar) tssocket_ntoa(const Pip4_addr_t addr);
//arg[0] addr : None
TSAPI(pchar) tssocket_aton6(const Pip6_addr_t addr);
//arg[0] addr : None
TSAPI(pchar) tssocket_ntoa6(const Pip6_addr_t addr);
//arg[0] ANetworkIndex : None
//arg[1] ALog : None
TSAPI(s32) tssocket_initialize(const s32 ANetworkIndex,const TLogDebuggingInfo ALog);
//arg[0] ANetworkIndex : None
TSAPI(s32) tssocket_finalize(const s32 ANetworkIndex);
//arg[0] ANetworkIndex : None
//arg[1] macaddr : None
//arg[2] ipaddr : None
//arg[3] netmask : None
//arg[4] gateway : None
//arg[5] mtu : None
TSAPI(s32) tssocket_add_device(const s32 ANetworkIndex,const pu8 macaddr,const Tip4_addr_t ipaddr,const Tip4_addr_t netmask,const Tip4_addr_t gateway,const u16 mtu);
//arg[0] ANetworkIndex : None
//arg[1] macaddr : None
//arg[2] ipaddr : None
TSAPI(s32) tssocket_remove_device(const s32 ANetworkIndex,const pu8 macaddr,const Tip4_addr_t ipaddr);
//arg[0] ANetworkIndex : None
TSAPI(s32) tssocket_dhcp_start(const s32 ANetworkIndex);
//arg[0] ANetworkIndex : None
TSAPI(s32) tssocket_dhcp_stop(const s32 ANetworkIndex);
//arg[0] ANetworkIndex : None
//arg[1] s : None
//arg[2] addr : None
//arg[3] addrlen : None
TSAPI(s32) tssocket_accept(const s32 ANetworkIndex,const s32 s,const Pts_sockaddr addr,const pu32 addrlen);
//arg[0] ANetworkIndex : None
//arg[1] s : None
//arg[2] name : None
//arg[3] namelen : None
TSAPI(s32) tssocket_bind(const s32 ANetworkIndex,const s32 s,const Pts_sockaddr name,const u32 namelen);
//arg[0] ANetworkIndex : None
//arg[1] s : None
//arg[2] how : None
TSAPI(s32) tssocket_shutdown(const s32 ANetworkIndex,const s32 s,const s32 how);
//arg[0] ANetworkIndex : None
//arg[1] s : None
//arg[2] name : None
//arg[3] namelen : None
TSAPI(s32) tssocket_getpeername(const s32 ANetworkIndex,const s32 s,const Pts_sockaddr name,const u32 namelen);
//arg[0] ANetworkIndex : None
//arg[1] s : None
//arg[2] name : None
//arg[3] namelen : None
TSAPI(s32) tssocket_getsockname(const s32 ANetworkIndex,const s32 s,const Pts_sockaddr name,const u32 namelen);
//arg[0] ANetworkIndex : None
//arg[1] s : None
//arg[2] level : None
//arg[3] optname : None
//arg[4] optval : None
//arg[5] optlen : None
TSAPI(s32) tssocket_getsockopt(const s32 ANetworkIndex,const s32 s,const s32 level,const s32 optname,const ps32 optval,const pu32 optlen);
//arg[0] ANetworkIndex : None
//arg[1] s : None
//arg[2] level : None
//arg[3] optname : None
//arg[4] optval : None
//arg[5] optlen : None
TSAPI(s32) tssocket_setsockopt(const s32 ANetworkIndex,const s32 s,const s32 level,const s32 optname,const ps32 optval,const u32 optlen);
//arg[0] ANetworkIndex : None
//arg[1] s : None
TSAPI(s32) tssocket_close(const s32 ANetworkIndex,const s32 s);
//arg[0] ANetworkIndex : None
//arg[1] s : None
//arg[2] name : None
//arg[3] namelen : None
TSAPI(s32) tssocket_connect(const s32 ANetworkIndex,const s32 s,const Pts_sockaddr name,const u32 namelen);
//arg[0] ANetworkIndex : None
//arg[1] s : None
//arg[2] backlog : None
TSAPI(s32) tssocket_listen(const s32 ANetworkIndex,const s32 s,const s32 backlog);
//arg[0] ANetworkIndex : None
//arg[1] s : None
//arg[2] mem : None
//arg[3] len : None
//arg[4] flags : None
TSAPI(s32) tssocket_recv(const s32 ANetworkIndex,const s32 s,const pu8 mem,const size_t len,const s32 flags);
//arg[0] ANetworkIndex : None
//arg[1] s : None
//arg[2] mem : None
//arg[3] len : None
TSAPI(s32) tssocket_read(const s32 ANetworkIndex,const s32 s,const pu8 mem,const size_t len);
//arg[0] ANetworkIndex : None
//arg[1] s : None
//arg[2] iov : None
//arg[3] iovcnt : None
TSAPI(s32) tssocket_readv(const s32 ANetworkIndex,const s32 s,const Pts_iovec iov,const s32 iovcnt);
//arg[0] ANetworkIndex : None
//arg[1] s : None
//arg[2] mem : None
//arg[3] len : None
//arg[4] flags : None
//arg[5] from : None
//arg[6] fromlen : None
TSAPI(s32) tssocket_recvfrom(const s32 ANetworkIndex,const s32 s,const pu8 mem,const size_t len,const s32 flags,const Pts_sockaddr from,const pu32 fromlen);
//arg[0] ANetworkIndex : None
//arg[1] s : None
//arg[2] Amessage : None
//arg[3] flags : None
TSAPI(s32) tssocket_recvmsg(const s32 ANetworkIndex,const s32 s,const Pts_msghdr Amessage,const s32 flags);
//arg[0] ANetworkIndex : None
//arg[1] s : None
//arg[2] dataptr : None
//arg[3] size : None
//arg[4] flags : None
TSAPI(s32) tssocket_send(const s32 ANetworkIndex,const s32 s,const pu8 dataptr,const size_t size,const s32 flags);
//arg[0] ANetworkIndex : None
//arg[1] s : None
//arg[2] dataptr : None
//arg[3] size : None
//arg[4] flags : None
//arg[5] ato : None
//arg[6] tolen : None
TSAPI(s32) tssocket_sendto(const s32 ANetworkIndex,const s32 s,const pu8 dataptr,const size_t size,const s32 flags,const Pts_sockaddr ato,const u32 tolen);
//arg[0] ANetworkIndex : None
//arg[1] domain : None
//arg[2] atype : None
//arg[3] protocol : None
//arg[4] recv_cb : None
//arg[5] presend_cb : None
//arg[6] send_cb : None
TSAPI(s32) tssocket(const s32 ANetworkIndex,const s32 domain,const s32 atype,const s32 protocol,const tosun_recv_callback recv_cb,const tosun_tcp_presend_callback presend_cb,const tosun_tcp_ack_callback send_cb);
//arg[0] ANetworkIndex : None
//arg[1] s : None
//arg[2] dataptr : None
//arg[3] size : None
TSAPI(s32) tssocket_write(const s32 ANetworkIndex,const s32 s,const pu8 dataptr,const size_t size);
//arg[0] ANetworkIndex : None
//arg[1] s : None
//arg[2] iov : None
//arg[3] iovcnt : None
TSAPI(s32) tssocket_writev(const s32 ANetworkIndex,const s32 s,const Pts_iovec iov,const s32 iovcnt);
//arg[0] ANetworkIndex : None
//arg[1] maxfdp1 : None
//arg[2] readset : None
//arg[3] writeset : None
//arg[4] exceptset : None
//arg[5] timeout : None
TSAPI(s32) tssocket_select(const s32 ANetworkIndex,const s32 maxfdp1,const Pts_fd_set readset,const Pts_fd_set writeset,const Pts_fd_set exceptset,const Pts_timeval timeout);
//arg[0] ANetworkIndex : None
//arg[1] fds : None
//arg[2] nfds : None
//arg[3] timeout : None
TSAPI(s32) tssocket_poll(const s32 ANetworkIndex,const Pts_pollfd fds,const u32 nfds,const s32 timeout);
//arg[0] ANetworkIndex : None
//arg[1] s : None
//arg[2] cmd : None
//arg[3] argp : None
TSAPI(s32) tssocket_ioctl(const s32 ANetworkIndex,const s32 s,const s32 cmd,const ps32 argp);
//arg[0] ANetworkIndex : None
//arg[1] s : None
//arg[2] cmd : None
//arg[3] val : None
TSAPI(s32) tssocket_fcntl(const s32 ANetworkIndex,const s32 s,const s32 cmd,const s32 val);
//arg[0] ANetworkIndex : None
//arg[1] af : None
//arg[2] src : None
//arg[3] dst : None
//arg[4] size : None
TSAPI(s32) tssocket_inet_ntop(const s32 ANetworkIndex,const s32 af,const ps32 src,const char*  dst,const u32 size);
//arg[0] ANetworkIndex : None
//arg[1] af : None
//arg[2] src : None
//arg[3] dst : None
TSAPI(s32) tssocket_inet_pton(const s32 ANetworkIndex,const s32 af,const ps32 src,const char*  dst);
//arg[0] ANetworkIndex : None
//arg[1] ping_addr : None
//arg[2] repeat : None
//arg[3] interval_ms : None
//arg[4] timeout_ms : None
TSAPI(void) tssocket_ping4(const s32 ANetworkIndex,const Pip4_addr_t ping_addr,const s32 repeat,const u32 interval_ms,const u32 timeout_ms);
//arg[0] ANetworkIndex : None
//arg[1] ping_addr : None
//arg[2] repeat : None
//arg[3] interval_ms : None
//arg[4] timeout_ms : None
TSAPI(void) tssocket_ping6(const s32 ANetworkIndex,const Pip6_addr_t ping_addr,const s32 repeat,const u32 interval_ms,const u32 timeout_ms);
#if defined ( __cplusplus )
}
#endif
#pragma pack(pop)
#endif