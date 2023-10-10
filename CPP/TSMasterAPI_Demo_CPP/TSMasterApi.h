#ifndef   _TSMASTER_API_H_
#define  _TSMASTER_API_H_


#include <stdint.h>
#include <cstring>
#include <string>
#include <memory>
#include <vector>

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

#pragma pack (1)
typedef struct _TCAN  {
	u8 FIdxChn;           // channel index starting from 0
	u8 FProperties;
	u8 FDLC;              // dlc from 0 to 8
	u8 FReserved;         // reserved to keep alignment
	s32 FIdentifier;      // CAN identifier
	u64 FTimeUS;          // timestamp in us  //Modified by Eric 0321
	u8  FData[8];           // 8 data bytes to send

	bool is_tx_get();
	void is_tx_set(bool);
	bool is_data_get();
	void is_data_set(bool);
	bool is_std_get();
	void is_std_set(bool);
	bool is_err_get();
	void is_err_set(bool);

	void load_data_array(u8* a, int len = 8) {
		if (len > 8) len = 8;
		memcpy(FData, a, len);
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
		is_tx_set(false);
		is_std_set(true);
		is_data_set(true);
		*(u64*)(&FData[0]) = 0;
		FTimeUS = 0;
	}
	// initialize with extended identifier -----------------------
	void init_w_ext_id(s32 AId, s32 ADLC) {
		FIdxChn = 0;
		FIdentifier = AId;
		FDLC = ADLC;
		FProperties = 0;
		is_tx_set(false);
		is_std_set(false);
		is_data_set(true);
		*(u64*)(&FData[0]) = 0;
		FTimeUS = 0;
	}
	_TCAN()
	{
		FIdxChn = 0;
		FIdentifier = 0;
		FDLC = 0;
		FReserved = 0;
		FProperties = 0;
		*(u64*)(&FData[0]) = 0;
		FTimeUS = 0;
	}
} TLIBCAN, * PLIBCAN;


typedef struct _TCANFD  {
	u8 FIdxChn;
	u8 FProperties;
	u8 FDLC;
	u8 FFDProperties;
	s32 FIdentifier;
	s64 FTimeUS;
	u8  FData[64];

	bool is_tx_get();
	void is_tx_set(bool);
	bool is_data_get();
	void is_data_set(bool);
	bool is_std_get();
	void is_std_set(bool);
	bool is_err_get();
	void is_err_set(bool);

	bool is_edl_get();
	void is_edl_set(bool);
	bool is_brs_get();
	void is_brs_set(bool);
	bool is_esi_get();
	void is_esi_set(bool);


	void load_data_array(u8* a, int len = 64) {
		if (len > 64) len = 64;
		memcpy(FData, a, len);
	}
	// initialize with standard identifier -----------------------
	void init_w_std_id(s32 AId, s32 ADLC) {
		FIdxChn = 0;
		FIdentifier = AId;
		FDLC = ADLC;
		FProperties = 0;
		FFDProperties = 0;
		is_edl_set(true);
		is_tx_set(false);
		is_std_set(true);
		is_data_set(true);
        memset(FData, 0, sizeof(FData));
		FTimeUS = 0;
	}

	// initialize with extended identifier -----------------------
	void init_w_ext_id(s32 AId, s32 ADLC) {
		FIdxChn = 0;
		FIdentifier = AId;
		FDLC = ADLC;
		FProperties = 0;
		FFDProperties = 0;
		is_edl_set(true);
		is_tx_set(false);
		is_std_set(false);
		is_data_set(true);
		memset(FData, 0, sizeof(FData));
		FTimeUS = 0;
	}

	// get fd data length ----------------------------------------
	s32 get_data_length() {
		static const u8 DLC_DATA_BYTE_CNT[16] = {
			0, 1, 2, 3, 4, 5, 6, 7,
			8, 12, 16, 20, 24, 32, 48, 64
		};
		s32 l = std::min(FDLC, (u8)15);
		l = std::max(l, 0);
		return DLC_DATA_BYTE_CNT[l];
	}
	// to CAN struct ---------------------------------------------
	TLIBCAN to_tcan(void) {
		return *(TLIBCAN*)(&FIdxChn);
	}

} TLIBCANFD, * PLIBCANFD;


typedef struct _TLIBEthernetHeader {
	u8 FIdxChn;                             // app channel index starting from 0 = Network index
	u8 FIdxSwitch;                          // Network's switch index
	u8 FIdxPort;                            // Network's switch's port index, 0~127: measurement port, 128~255: virtual port
	u8 FDir;                                // 0 = Rx, 1 = Tx, 2 = TxRq
	u8 FReserved0;                          // 1 padding byte
	u8 FReserved1;                          // 1 padding byte
	u16 FEthernetPayloadLength;             // Length of Ethernet payload data in bytes. Max. 1582 Byte(without Ethernet header), 1612 Byte(Inclusive ethernet header)
	u32 FProperties;                       // Bit 0
	u64 FTimeUs;                           // timestamp in us
	u8* FEthernetDataPointer;              // data pointer
	//{$IFDEF WIN32}
	u32 FPaddings;                 // to be compatible with x64
	//{$ENDIF}
}TLIBEthernetHeader, *PLIBEthernetHeader;

typedef struct _TLIBFlexRay {
	u8 FIdxChn;                // channel index starting from 0
	u8 FChannelMask;           // 0: reserved, 1: A, 2: B, 3: AB
	u8 FDir;                   // 0: Rx, 1: Tx, 2: Tx Request
	u8 FPayloadLength;         // payload length in bytes
	u8 FActualPayloadLength;   // actual data bytes
	u8 FCycleNumber;           // cycle number: 0~63
	u8 FCCType;                // 0 = Architecture independent, 1 = Invalid CC type, 2 = Cyclone I, 3 = BUSDOCTOR, 4 = Cyclone II, 5 = Vector VN interface, 6 = VN - Sync - Pulse(only in Status Event, for debugging purposes only)
	u8 FReserved0;             // 1 reserved byte
	u16 FHeaderCRCA;          // header crc A
	u16 FHeaderCRCB;          // header crc B
	u16 FFrameStateInfo;      // bit 0~15, error flags
	u16 FSlotId;              // static seg: 0~1023
	u32 FFrameFlags;          // bit 0~22
								  // 0 1 = Null frame.
								  // 1 1 = Data segment contains valid data
								  // 2 1 = Sync bit
								  // 3 1 = Startup flag
								  // 4 1 = Payload preamble bit
								  // 5 1 = Reserved bit
								  // 6 1 = Error flag(error frame or invalid frame)
								  // 7..14 Reserved
								  // 15 1 = Async.monitoring has generated this event
								  // 16 1 = Event is a PDU
								  // 17 Valid for PDUs only.The bit is set if the PDU is valid(either if the PDU has no  // update bit, or the update bit for the PDU was set in the received frame).
								  // 18 Reserved
								  // 19 1 = Raw frame(only valid if PDUs are used in the configuration).A raw frame may  // contain PDUs in its payload
								  // 20 1 = Dynamic segment	0 = Static segment
								  // 21 This flag is only valid for frames and not for PDUs.	1 = The PDUs in the payload of  // this frame are logged in separate logging entries. 0 = The PDUs in the payload of this  // frame must be extracted out of this frame.The logging file does not contain separate  // PDU - entries.
								  // 22 Valid for PDUs only.The bit is set if the PDU has an update bit
	u32 FFrameCRC;            // frame crc
	u64 FReserved1;           // 8 reserved bytes
	u64 FReserved2;           // 8 reserved bytes
	u64 FTimeUs;              // timestamp in us
	u8 FData[254]; // 254 data bytes
}TLIBFlexRay, *PLIBFlexRay;

typedef struct
{
	s64  FTimeUs;
	int   FEventType;     // 0
	u32 FCapacity;
	char* FComment;
}TRealtime_comment_t, * PRealtime_comment_t;

typedef enum
{
	MasterNode = 0,
	SlaveNode,
	MonitorNode
}TLINNodeType;
typedef struct _TLIN{
	u8 FIdxChn;           // channel index starting from 0
	u8 FErrStatus;          //  0: normal
	u8 FProperties;       // 
	u8 FDLC;              // dlc from 0 to 8
	u8 FIdentifier;       // LIN identifier:0--64
	u8 FChecksum;         // LIN checksum
	u8 FStatus;           // place holder 1
	u64 FTimeUS;          // timestamp in us  //Modified by Eric 0321
	u8  FData[8];           // 8 data bytes to send

	bool is_tx_get();
	void is_tx_set(bool);
	bool is_send_break_get();
	void is_send_break_set(bool);
	bool is_reccived_break_get();
	void is_reccived_break_set(bool);
	bool is_send_sync_get();
	void is_send_sync_set(bool);
	bool is_reccived_sync_get();
	void is_reccived_sync_set(bool);
	// load data bytes -------------------------------------------
	void load_data_array(u8* a, int len = 8) {
		if (len > 8) len = 8;
		memcpy(FData, a, len);
	}
	// initialize with identifier --------------------------------
	void init_w_id(const s32 AId, const s32 ADLC) {
		FIdxChn = 0;
		FErrStatus = 0;
		is_tx_set(false);
		FDLC = ADLC;
		FIdentifier = AId;
		*(__int64*)(&FData[0]) = 0;
		FChecksum = 0;
		FStatus = 0;
		FTimeUS = 0;
	}

}TLIBLIN, * PLIBLIN;

// Generic definitions ===========================================
typedef void(__stdcall* TProcedure)(const void* AObj);
typedef void(__stdcall* TProcedureSetInt)(const void* AObj, const s32 AValue);
typedef s32(__stdcall* TIntFunction)(const void* AObj);
typedef void(__stdcall* TProcedureSetDouble)(const void* AObj, const double AValue);
typedef double(__stdcall* TDoubleFunction)(const void* AObj);
typedef void(__stdcall* TProcedureSetString)(const void* AObj, const char* AValue);
typedef char* (__stdcall* TStringFunction)(const void* AObj);
typedef void(__stdcall* TProcedureSetCAN)(const void* AObj, const PLIBCAN AValue);
typedef TLIBCAN(__stdcall* TTCANFunction)(const void* AObj);
typedef void(__stdcall* TProcedureSetCANFD)(const void* AObj, const PLIBCANFD AValue);
typedef TLIBCANFD(__stdcall* TTCANFDFunction)(const void* AObj);
typedef void(__stdcall* TProcedureSetLIN)(const void* AObj, const PLIBLIN AValue);
typedef TLIBLIN(__stdcall* TTLINFunction)(const void* AObj);

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
	TS_TC1005_DEVICE = 8,
	CANABLE_USB_DEVICE = 9,
	TS_WIRELESS_OBD = 10,
	TS_USB_DEVICE_EX = 11
} TLIBBusToolDeviceType, * PLIBBusToolDeviceType;


typedef enum { lfdtCAN = 0, lfdtISOCAN = 1, lfdtNonISOCAN = 2 }TLIBCANFDControllerType;
typedef enum { lfdmNormal = 0, lfdmACKOff = 1, lfdmRestricted = 2, lfdmInternalLoopback = 3, lfdmExternalLoopback = 4 } TLIBCANFDControllerMode;
typedef enum {
	TS_UNKNOWN_DEVICE = 0,
	TSCAN_PRO = 1,    // TSCAN_PRO_4_CHs_SJA1000
	TSCAN_Lite1 = 2,  // TSCAN_LITE_2_CHs_INTL_2515
	TC1001 = 3,  // TSCAN_MINI_1_CHs_INTL
	TL1001 = 4,  // TSLIN_MINI_1_CHs           = 4,
	TC1011 = 5,  // TSCAN_FD_MINI_1_CHs_INTL   = 5,  // TSCAN FD Mini
	TM5011 = 6,  // TSCAN_LIN_IO_2_CHs_F105    = 6,
	TC1002 = 7,  // TSCAN_LITE_2_CHs_F105      = 7,
	TC1014 = 8,  // TSCAN_LIN_DIO_AIO          = 8,  // TSCANLIN
	TSCANFD2517 = 9,   // TSCAN_FD_MINI_1_CHs_2517   = 9
	TC1026 = 10,   //FD_1_LIN_6
	TC1016 = 11,   //FD_4_LIN_2
	TC1012 = 12,   //FD_1_LIN_1
	TC1013 = 13,   //FD_2
	TLog1002 = 14,   //FD_2_LIN_2
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
	TF10XX = 25,    //Such TF1011
	TL1004_FD_4_LIN_2 = 26,    //Tlog1004OnH750
	TE1051 = 27
}TLIB_TS_Device_Sub_Type;

typedef enum { APP_CAN = 0, APP_LIN = 1 } TLIBApplicationChannelType;
typedef enum {
	cbsBusLoad = 0, cbsPeakLoad, cbsFpsStdData, cbsAllStdData,
	cbsFpsExtData, cbsAllExtData, cbsFpsStdRemote, cbsAllStdRemote,
	cbsFpsExtRemote, cbsAllExtRemote, cbsFpsErrorFrame, cbsAllErrorFrame
} TLIBCANBusStatistics;

#define VENDOR_NAME_LENGTH            (32)
#define DEVICE_SERIAL_STRING_LENGTH   (64)
// Hardware Info definition
typedef struct _TLIBHWInfo {
	TLIBBusToolDeviceType FDeviceType;
	s32 FDeviceIndex;
	char FVendorName[VENDOR_NAME_LENGTH];
	char FDeviceName[APP_DEVICE_NAME_LENGTH];
	char FSerialString[DEVICE_SERIAL_STRING_LENGTH];
}TLIBHWInfo, * PLIBHWInfo;

typedef struct _TLIBTSMapping{
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
typedef struct _TLIBSystemVarDef {
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
// database utilities
typedef struct _TCANSignal{
	u8     FCANSgnType; // 0 - Unsigned, 1 - Signed, 2 - Single 32, 3 - Double 64
	bool   FIsIntel;
	s32    FStartBit;
	s32    FLength;
	double FFactor;
	double FOffset;
} TCANSignal, * PCANSignal;
#define CANMsgDecl(typ, name, chn, prop, dlc, id) const typ name = {{chn, prop, dlc, 0, id, 0, {0}}};
#define CANSgnDecl(name, typ, isIntel, startBit, len, factor, offset) const TCANSignal name = {typ, isIntel, startBit, len, factor, offset};
typedef enum { rivUseDB = 0, rivUseLast, rivUse0 } TLIBRBSInitValueOptions;
typedef double(__stdcall* TGetCANSignalValue)(const PCANSignal ACANSignal, const pu8 AData);
typedef void(__stdcall* TSetCANSignalValue)(const PCANSignal ACANSignal, const pu8 AData, const double AValue);
typedef void(__stdcall* TCANEvent)(const ps32 AObj, const PLIBCAN ACAN);
typedef void(__stdcall* TCANFDEvent)(const ps32 AObj, const PLIBCANFD ACANFD);
typedef void(__stdcall* TLINEvent)(const ps32 AObj, const PLIBLIN ALIN);
typedef void(__stdcall* TFlexrayEvent)(const ps32 AObj, const PLIBFlexRay AFRData);
typedef void(__stdcall* TEthernetEvent)(const ps32 AObj, const PLIBEthernetHeader AEthenertData);
typedef void(__stdcall* TLogger)(const char* AStr, const s32 ALevel);

#pragma pack ()
#define IDX_ERR_DLL_NOT_READY           (77)

class TSMasterApi_priv;
class TSMasterApi
{
private:
	std::shared_ptr<TSMasterApi_priv> priv_data_p;
	TSMasterApi() {}
public:
	TSMasterApi(const TSMasterApi&) = delete;
	TSMasterApi& operator=(const TSMasterApi&) = delete;
	static TSMasterApi& get_instance() {
		static TSMasterApi instance;
		return instance;
	}


	//设置APP名称和DLL路径，通常应该第一时间调用，DLL路径如果非默认安装，请手动指定
	bool set_app_and_dll(const std::string & app_name
		, const std::string & dll_path = "TSMaster.dll");

	s32 tsapp_add_application(const char* AAppName);
	s32 tsapp_add_cyclic_msg_can(const PLIBCAN ACAN, const float APeriodMS);
	s32 tsapp_add_cyclic_msg_canfd(const PLIBCANFD ACANFD, const float APeriodMS);
	s32 tsapp_clear_bus_statistics(void);
	s32 tsapp_configure_baudrate_can(const s32 AIdxChn, const float ABaudrateKbps, const bool AListenOnly, const bool AInstallTermResistor120Ohm);
	s32 tsapp_configure_baudrate_canfd(const s32 AIdxChn, const float ABaudrateArbKbps, const float ABaudrateDataKbps, const TCANFDControllerType AControllerType, const TCANFDControllerMode AControllerMode, const bool AInstallTermResistor120Ohm);
    //AProtocol: {0:}LIN_PROTOCL_13, { 1: }LIN_PROTOCL_20, { ; 2: }LIN_PROTOCL_21, { ; 3: }LIN_PROTOCL_J2602
	s32 tsapp_configure_baudrate_lin(const s32 AIdxChn, const float ABaudrateKbps, const s32 AProtocol);
	s32 tsapp_connect(void);
	s32 tsapp_del_application(const char* AAppName);
	s32 tsapp_del_mapping(const PLIBTSMapping AMapping);
	s32 tsapp_del_mapping_verbose(const char* AAppName,
		const TLIBApplicationChannelType AAppChannelType,
		const s32 AAppChannel);
	s32 tsapp_delete_cyclic_msg_can(const PLIBCAN ACAN);
	s32 tsapp_delete_cyclic_msg_canfd(const PLIBCANFD ACANFD);
	s32 tsapp_delete_cyclic_msgs(void);
	s32 tsapp_disconnect(void);
	s32 tsapp_enable_bus_statistics(const bool AEnable);
	s32 tsapp_enumerate_hw_devices(const ps32 ACount);
	s32 tsapp_execute_python_string(const char* AString, const bool AIsSync, const bool AIsX64, char** AResultLog);
	s32 tsapp_execute_python_script(const char* AFilePath, const bool AIsSync, const bool AIsX64, char** AResultLog);
	s32 tsapp_get_application_list(char** AAppNameList);
	s32 tsapp_get_bus_statistics(const TLIBApplicationChannelType ABusType, const s32 AIdxChn, const TLIBCANBusStatistics AIdxStat, pdouble AStat);
	s32 tsapp_get_can_channel_count(const ps32 ACount);
	s32 tsapp_get_current_application(const char** AAppName);
	s32 tsapp_get_error_description(const s32 ACode, char** ADesc);
	s32 tsapp_get_fps_can(const s32 AIdxChn, const s32 AIdentifier, ps32 AFPS);
	s32 tsapp_get_fps_canfd(const s32 AIdxChn, const s32 AIdentifier, ps32 AFPS);
	s32 tsapp_get_fps_lin(const s32 AIdxChn, const s32 AIdentifier, ps32 AFPS);
	s32 tsapp_get_hw_info_by_index(const s32 AIndex, const PLIBHWInfo AHWInfo);
	s32 tsapp_get_hw_info_by_index_verbose(const s32 AIndex,
		PLIBBusToolDeviceType ADeviceType,
		char* AVendorNameBuffer, //array[0..31] of AnsiChar;
		s32 AVendorNameBufferSize,
		char* ADeviceNameBuffer, //array[0..31] of AnsiChar;
		s32 ADeviceNameBufferSize,
		char* ASerialStringBuffer, //array[0..63] of AnsiChar
		s32 ASerialStringBufferSize
	);
	s32 tsapp_get_lin_channel_count(const ps32 ACount);
	s32 tsapp_get_mapping(const PLIBTSMapping AMapping);
	s32 tsapp_get_mapping_verbose(const char* AAppName,
		const TLIBApplicationChannelType AAppChannelType,
		const s32 AAppChannel,
		const PLIBTSMapping AMapping);
	s32 tsapp_get_timestamp(s64* ATimestamp);
	s32 tsapp_get_turbo_mode(const bool* AEnable);
	void tsapp_log(const char* AStr, const TLogLevel ALevel);
	void tsfifo_enable_receive_error_frames(void);
	void tsfifo_enable_receive_fifo(void);
	void tsfifo_disable_receive_error_frames(void);
	void tsfifo_disable_receive_fifo(void);
	s32 tsfifo_read_can_buffer_frame_count(const s32 AIdxChn, ps32 ACount);
	s32 tsfifo_read_can_rx_buffer_frame_count(const s32 AIdxChn, ps32 ACount);
	s32 tsfifo_read_can_tx_buffer_frame_count(const s32 AIdxChn, ps32 ACount);
	s32 tsfifo_read_canfd_buffer_frame_count(const s32 AIdxChn, ps32 ACount);
	s32 tsfifo_read_canfd_rx_buffer_frame_count(const s32 AIdxChn, ps32 ACount);
	s32 tsfifo_read_canfd_tx_buffer_frame_count(const s32 AIdxChn, ps32 ACount);
	s32 tsfifo_read_fastlin_buffer_frame_count(const s32 AIdxChn, ps32 ACount);
	s32 tsfifo_read_fastlin_rx_buffer_frame_count(const s32 AIdxChn, ps32 ACount);
	s32 tsfifo_read_fastlin_tx_buffer_frame_count(const s32 AIdxChn, ps32 ACount);
	s32 tsfifo_read_lin_buffer_frame_count(const s32 AIdxChn, ps32 ACount);
	s32 tsfifo_read_lin_rx_buffer_frame_count(const s32 AIdxChn, ps32 ACount);
	s32 tsfifo_read_lin_tx_buffer_frame_count(const s32 AIdxChn, ps32 ACount);
	s32 tsfifo_receive_can_msgs(PLIBCAN ACANBuffers, ps32 ACANBufferSize, const s32 AIdxChn, const bool AIncludeTx);
	s32 tsfifo_receive_canfd_msgs(PLIBCANFD ACANFDBuffers, ps32 ACANFDBufferSize, const s32 AIdxChn, const bool AIncludeTx);
	s32 tsfifo_receive_fastlin_msgs(PLIBLIN ALINBuffers, ps32 ALINBufferSize, const s32 AIdxChn, const bool AIncludeTx);
	s32 tsfifo_receive_lin_msgs(PLIBLIN ALINBuffers, ps32 ALINBufferSize, const s32 AIdxChn, const bool AIncludeTx);
	s32 tsfifo_clear_can_receive_buffers(const s32 AIdxChn);
	s32 tsfifo_clear_canfd_receive_buffers(const s32 AIdxChn);
	s32 tsfifo_clear_fastlin_receive_buffers(const s32 AIdxChn);
	s32 tsfifo_clear_lin_receive_buffers(const s32 AIdxChn);
	s32 tsapp_register_event_can(const ps32 AObj, const TCANEvent AEvent);
	s32 tsapp_register_event_canfd(const ps32 AObj, const TCANFDEvent AEvent);
	s32 tsapp_register_event_lin(const ps32 AObj, const TLINEvent AEvent);
	s32 tsapp_register_event_flexray(const ps32 AObj, const TFlexrayEvent AEvent);
	s32 tsapp_register_event_ethernet(const ps32 AObj, const TEthernetEvent AEvent);
	s32 tsapp_register_pretx_event_can(const ps32 AObj, const TCANEvent AEvent);
	s32 tsapp_register_pretx_event_canfd(const ps32 AObj, const TCANFDEvent AEvent);
	s32 tsapp_register_pretx_event_lin(const ps32 AObj, const TLINEvent AEvent);
	s32 tsapp_register_pretx_event_flexray(const ps32 AObj, const TFlexrayEvent AEvent);
	s32 tsapp_register_pretx_event_ethernet(const ps32 AObj, const TEthernetEvent AEvent);
	s32 tsapp_set_can_channel_count(const s32 ACount);
	s32 tsapp_set_current_application(const char* AAppName);
	s32 tsapp_set_lin_channel_count(const s32 ACount);
	s32 tsapp_set_logger(const TLogger ALogger);
	s32 tsapp_set_mapping(const PLIBTSMapping AMapping);
	s32 tsapp_set_mapping_verbose(const char* AAppName,
		const TLIBApplicationChannelType AAppChannelType,
		const s32 AAppChannel,
		const char* AHardwareName,
		const TLIBBusToolDeviceType AHardwareType,
		const s32 AHardwareSubType,
		const s32 AHardwareIndex,
		const s32 AHardwareChannel,
		const bool AEnableMapping);
	s32 tsapp_set_turbo_mode(const bool AEnable);
	s32 tsapp_set_vendor_detect_preferences(const bool AScanTOSUN,
		const bool AScanVector,
		const bool AScanPeak,
		const bool AScanKvaser,
		const bool AScanZLG,
		const bool AScanIntrepidcs);
	s32 tsapp_show_tsmaster_window(const char* AWindowName, const bool AWaitClose);
	s32 tsapp_start_logging(const char* AFullFileName);
	s32 tsapp_stop_logging(void);
	s32 tsapp_transmit_can_async(const PLIBCAN ACAN);
	s32 tsapp_transmit_canfd_async(const PLIBCANFD ACANFD);
	s32 tsapp_transmit_lin_async(const PLIBLIN ALIN);
	s32 tsapp_transmit_flexray_async(const PLIBFlexRay AFlexray);
	s32 tsapp_transmit_ethernet_async(const PLIBEthernetHeader AEthernetHeader);
	s32 tsapp_transmit_header_and_receive_msg(s32 AChn, u8 AIdentifier, u8 ADLC, PLIBLIN ALINData, s32 ATimeoutMs);
	s32 tsapp_transmit_can_sync(const PLIBCAN ACAN, const s32 ATimeoutMS);
	s32 tsapp_transmit_canfd_sync(const PLIBCANFD ACANFD, const s32 ATimeoutMS);
	s32 tsapp_transmit_lin_sync(const PLIBLIN ALIN, const s32 ATimeoutMS);
	s32 tsapp_unregister_event_can(const ps32 AObj, const TCANEvent AEvent);
	s32 tsapp_unregister_event_canfd(const ps32 AObj, const TCANFDEvent AEvent);
	s32 tsapp_unregister_event_lin(const ps32 AObj, const TLINEvent AEvent);
	s32 tsapp_unregister_event_flexray(const ps32 AObj, const TFlexrayEvent AEvent);
	s32 tsapp_unregister_event_ethernet(const ps32 AObj, const TEthernetEvent AEvent);
	s32 tsapp_unregister_events_can(const ps32 AObj);
	s32 tsapp_unregister_events_lin(const ps32 AObj);
	s32 tsapp_unregister_events_canfd(const ps32 AObj);
	s32 tsapp_unregister_events_flexray(const ps32 AObj);
	s32 tsapp_unregister_events_ethernet(const ps32 AObj);
	s32 tsapp_unregister_events_all(const ps32 AObj);
	s32 tsapp_unregister_pretx_event_can(const ps32 AObj, const TCANEvent AEvent);
	s32 tsapp_unregister_pretx_event_canfd(const ps32 AObj, const TCANFDEvent AEvent);
	s32 tsapp_unregister_pretx_event_lin(const ps32 AObj, const TLINEvent AEvent);
	s32 tsapp_unregister_pretx_event_flexray(const ps32 AObj, const TFlexrayEvent AEvent);
	s32 tsapp_unregister_pretx_event_ethernet(const ps32 AObj, const TEthernetEvent AEvent);
	s32 tsapp_unregister_pretx_events_can(const ps32 AObj);
	s32 tsapp_unregister_pretx_events_lin(const ps32 AObj);
	s32 tsapp_unregister_pretx_events_canfd(const ps32 AObj);
	s32 tsapp_unregister_pretx_events_flexray(const ps32 AObj);
	s32 tsapp_unregister_pretx_events_ethernet(const ps32 AObj);
	s32 tsapp_unregister_pretx_events_all(const ps32 AObj);

	s32 tscom_can_rbs_start(void);
	s32 tscom_can_rbs_stop(void);
	s32 tscom_can_rbs_is_running(bool* AIsRunning);
	s32 tscom_can_rbs_configure(const bool AAutoStart, const bool AAutoSendOnModification, const bool AActivateNodeSimulation, const TLIBRBSInitValueOptions AInitValueOptions);
	s32 tscom_can_rbs_activate_all_networks(const bool AEnable, const bool AIncludingChildren);
	s32 tscom_can_rbs_activate_network_by_name(const bool AEnable, const char* ANetworkName, const bool AIncludingChildren);
	s32 tscom_can_rbs_activate_node_by_name(const bool AEnable, const char* ANetworkName, const char* ANodeName, const bool AIncludingChildren);
	s32 tscom_can_rbs_activate_message_by_name(const bool AEnable, const char* ANetworkName, const char* ANodeName, const char* AMsgName);
	s32 tscom_can_rbs_get_signal_value_by_element(const s32 AIdxChn, const char* ANetworkName, const char* ANodeName, const char* AMsgName, const char* ASignalName, double* AValue);
	s32 tscom_can_rbs_get_signal_value_by_address(const char* ASymbolAddress, double* AValue);
	s32 tscom_can_rbs_set_signal_value_by_element(const s32 AIdxChn, const char* ANetworkName, const char* ANodeName, const char* AMsgName, const char* ASignalName, const double AValue);
	s32 tscom_can_rbs_set_signal_value_by_address(const char* ASymbolAddress, const double AValue);
	s32 tsdb_get_signal_value_can(const PLIBCAN ACAN, const char* AMsgName, const char* ASgnName, double* AValue);
	s32 tsdb_get_signal_value_canfd(const PLIBCANFD ACANFD, const char* AMsgName, const char* ASgnName, double* AValue);
	s32 tsdb_set_signal_value_can(const PLIBCAN ACAN, const char* AMsgName, const char* ASgnName, const double AValue);
	s32 tsdb_set_signal_value_canfd(const PLIBCANFD ACANFD, const char* AMsgName, const char* ASgnName, const double AValue);
	s32 tsdb_load_can_db(const char* ADBC, const char* ASupportedChannelsBased0, u32* AId);
	s32 tsdb_unload_can_db(const u32 AId);
	s32 tsdb_unload_can_dbs(void);
	s32 tsdb_get_can_db_count(s32* ACount);
	s32 tsdb_get_can_db_id(const s32 AIndex, u32* AId);
	s32 tsdb_get_can_db_info(const u32 ADatabaseId, const s32 AType, const s32 AIndex, const s32 ASubIndex, char** AValue);
	s32 tslog_add_online_replay_config(const char* AFileName, s32* AIndex);
	s32 tslog_set_online_replay_config(const s32 AIndex, const char* AName, const char* AFileName, const bool AAutoStart, const bool AIsRepetitiveMode, const TLIBOnlineReplayTimingMode AStartTimingMode, const s32 AStartDelayTimeMs, const bool ASendTx, const bool ASendRx, const char* AMappings);
	s32 tslog_get_online_replay_count(s32* ACount);
	s32 tslog_get_online_replay_config(const s32 AIndex, char** AName, char** AFileName, bool* AAutoStart, bool* AIsRepetitiveMode, TLIBOnlineReplayTimingMode* AStartTimingMode, s32* AStartDelayTimeMs, bool* ASendTx, bool* ASendRx, char** AMappings);
	s32 tslog_del_online_replay_config(const s32 AIndex);
	s32 tslog_del_online_replay_configs(void);
	s32 tslog_start_online_replay(const s32 AIndex);
	s32 tslog_start_online_replays(void);
	s32 tslog_pause_online_replay(const s32 AIndex);
	s32 tslog_pause_online_replays(void);
	s32 tslog_stop_online_replay(const s32 AIndex);
	s32 tslog_stop_online_replays(void);
	s32 tslog_get_online_replay_status(const s32 AIndex, TLIBOnlineReplayStatus* AStatus, float* AProgressPercent100);

	// blf
	s32 tslog_blf_write_start(const char* AFileName, int* AHandle); //stdcall
	s32 tslog_blf_write_can(int AHandle, PLIBCAN ACAN);
	s32 tslog_blf_write_can_fd(int AHandle , PLIBCANFD ACANFD );
	s32 tslog_blf_write_lin(int AHandle, PLIBLIN ALIN );
	s32 tslog_blf_write_realtime_comment(int AHandle , s64 ATimeUs , char* AComment);
	s32 tslog_blf_write_end(int AHandle);
	s32 tslog_blf_read_start(const char* AFileName, int* AHandle, int* AObjCount);
	s32 tsLog_blf_read_start_verbose(const char* AFileName, int* AHandle, int* AObjCount,
										u16* AYear, u16* AMonth, u16* ADayOfWeek,
		                                u16* ADay, u16* AHour, u16* AMinute,
		                                u16* ASecond, u16* AMilliseconds);
	s32 tslog_blf_read_status(int AHandle, int * AObjReadCount);
	s32 tslog_blf_read_object(int AHandle, int* AProgressedCnt, int* AType/* PSupportedObjType*/, PLIBCAN ACAN, 
		                                  PLIBLIN ALIN, PLIBCANFD ACANFD);
	s32 tslog_blf_read_object_w_comment(int AHandle, int* AProgressedCnt, int* AType/* PSupportedObjType*/,
		                                 PLIBCAN ACAN, PLIBLIN ALIN, PLIBCANFD ACANFD, PRealtime_comment_t AComment);
	s32 tslog_blf_read_end(int AHandle);
	s32 tslog_blf_seek_object_time(int AHandle, const double AProg100, s64* ATime, int* AProgressedCnt);
	//s32 tslog_blf_to_asc(char* ABLFFileName, char* AASCFileName, TProgressCallback AProgressCallback);
	//s32 tslog_asc_to_blf(char* AASCFileName, char* ABLFFileName , TProgressCallback AProgressCallback);

	s32 tslin_enable_runtime_schedule_table(const s32 AChnIdx);
	s32 tslin_set_schedule_table(const s32 AChnIdx, const s32 ASchIndex);
	s32 tslin_stop_lin_channel(const s32 AChnIdx);
	s32 tslin_start_lin_channel(const s32 AChnIdx);
	s32 tslin_set_node_funtiontype(const s32 AChnIdx, const TLINNodeType AFunctionType);

};
#endif
