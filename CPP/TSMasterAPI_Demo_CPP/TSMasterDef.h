#ifndef __LIBTSCAN_H
#define __LIBTSCAN_H

#include <iostream>
#include <windows.h>  

#define DLLIMPORT __declspec(dllimport)
#pragma pack(1)
#include <stdint.h>
typedef uint8_t u8;
typedef int8_t s8;
typedef uint16_t u16;
typedef int16_t s16;
typedef uint32_t u32;
typedef int32_t s32;
typedef uint64_t u64;
typedef int64_t s64;
typedef wchar_t wchar;
typedef struct _u8x8 { u8 d[8]; } u8x8;

typedef enum :s32
{
	CHN1,
	CHN2,
	CHN3,
	CHN4,
	CHN5,
	CHN6,
	CHN7,
	CHN8,
	CHN9,
	CHN10,
	CHN11,
	CHN12,
	CHN13,
	CHN14,
	CHN15,
	CHN16,
	CHN17,
	CHN18,
	CHN19,
	CHN20,
	CHN21,
	CHN22,
	CHN23,
	CHN24,
	CHN25,
	CHN26,
	CHN27,
	CHN28,
	CHN29,
	CHN30,
	CHN31,
	CHN32
}APP_CHANNEL;

#define ONLY_RX_DATA  (0)
#define TX_RX_DATA    (1)


//Mapping Definition
 // Mapping definition
typedef enum:s32 {
	APP_CAN = 0,
	APP_LIN = 1
}TLIBApplicationChannelType;

typedef enum :s32{
	BUS_UNKNOWN_TYPE = 0,
	TS_TCP_DEVICE = 1,
	XL_USB_DEVICE = 2,
	TS_USB_DEVICE = 3,
	PEAK_USB_DEVICE = 4,
	KVASER_USB_DEVICE = 5,
	ZLG_USB_DEVICE = 6,
	ICS_USB_DEVICE = 7,
	TS_TC1005_DEVICE = 8
}TLIBBusToolDeviceType;

typedef struct _TLIBTSMapping {
	u8  FAppName[32];
	APP_CHANNEL FAppChannelIndex;   //s32
	TLIBApplicationChannelType FAppChannelType;
	TLIBBusToolDeviceType FHWDeviceType;
	s32 FHWIndex;
	s32 FHWChannelIndex;
	s32 FHWDeviceSubType;
    u8 FHWDeviceName[32];
	boolean FMappingDisabled;
}TLIBTSMapping, *PLIBTSMapping;

typedef union {
	u8 value;
	struct {
		u8 istx : 1;
		u8 remoteframe : 1;
		u8 extframe : 1;
		u8 tbd : 4;
		u8 iserrorframe : 1;
	}bits;
}TCANProperty;

typedef struct _TCAN {
	u8 FIdxChn;           // channel index starting from 0
	TCANProperty FProperties;       // default 0, masked status:
						  // [7] 0-normal frame, 1-error frame
						  // [6-3] tbd
						  // [2] 0-std frame, 1-extended frame
						  // [1] 0-data frame, 1-remote frame
						  // [0] dir: 0-RX, 1-TX
	u8 FDLC;              // dlc from 0 to 8
	u8 FReserved;         // reserved to keep alignment
	s32 FIdentifier;      // CAN identifier
	u64 FTimeUS;          // timestamp in us  //Modified by Eric 0321
	u8x8 FData;           // 8 data bytes to send
} TLIBCAN,*PLIBCAN;

typedef struct _TCANFD {
    u8 FIdxChn;
    u8 FProperties;
    u8 FDLC;
    u8 FFDProperties;
    s32 FIdentifier;
    s64 FTimeUs;
    u8  FData[64];
} TCANFD, * PCANFD;


typedef union
{
	u8 value;
	struct {
		u8 istx : 1;
		u8 breaksended : 1;
		u8 breakreceived : 1;
		u8 syncreceived : 1;
		u8 hwtype : 2;
		u8 isLogged : 1;
		u8 iserrorframe : 1;
	}bits;
}TLINProperty;
typedef struct _TLIN {
	u8 FIdxChn;           // channel index starting from 0
	u8 FErrCode;          //  0: normal
	TLINProperty FProperties;       // default 0, masked status:
						   // [7] tbd
						   // [6] 0-not logged, 1-already logged
						   // [5-4] FHWType //DEV_MASTER,DEV_SLAVE,DEV_LISTENER
						   // [3] 0-not ReceivedSync, 1- ReceivedSync
						   // [2] 0-not received FReceiveBreak, 1-Received Break
						   // [1] 0-not send FReceiveBreak, 1-send Break
						   // [0] dir: 0-RX, 1-TX
	u8 FDLC;              // dlc from 0 to 8
	u8 FIdentifier;       // LIN identifier:0--64
	u8 FChecksum;         // LIN checksum
	u8 FStatus;           // place holder 1
	u64 FTimeUS;          // timestamp in us  //Modified by Eric 0321
	u8x8 FData;           // 8 data bytes to send
}TLIBLIN;
typedef enum
{
	MasterNode,
	SlaveNode,
	MonitorNode
}TLIN_FUNCTION_TYPE;
//function pointer type

//App
typedef void (__stdcall* Tinitialize_lib_tsmaster)(const char* pAppName);   //initialize_lib_tsmaster
typedef void(__stdcall* Tfinalize_lib_tsmaster)(void);   //initialize_lib_tsmaster
//Communication
/*typedef s32(__stdcall* TTransmitCANAsync)(const PCAN ACAN);
typedef s32(__stdcall* TTransmitCANFDAsync)(const PCANFD ACANFD);
typedef s32(__stdcall* TTransmitLINAsync)(const PLIN ALIN);
typedef s32(__stdcall* TTransmitCANSync)(const PCAN ACAN, const s32 ATimeoutMS);
typedef s32(__stdcall* TTransmitCANFDSync)(const PCANFD ACANFD, const s32 ATimeoutMS);
typedef s32(__stdcall* TTransmitLINSync)(const PLIN ALIN, const s32 ATimeoutMS);
typedef double(__stdcall* TGetCANSignalValue)(const PCANSignal ACANSignal, const pu8 AData);
typedef void(__stdcall* TSetCANSignalValue)(const PCANSignal ACANSignal, const pu8 AData, const double AValue);
typedef void(__stdcall* TCANEvent)(const ps32 AObj, const PCAN ACAN);
typedef void(__stdcall* TCANFDEvent)(const ps32 AObj, const PCANFD ACANFD);
typedef void(__stdcall* TLINEvent)(const ps32 AObj, const PLIN ALIN);
typedef s32(__stdcall* TRegisterCANEvent)(const ps32 AObj, const TCANEvent AEvent);
typedef s32(__stdcall* TUnregisterCANEvent)(const ps32 AObj, const TCANEvent AEvent);
typedef s32(__stdcall* TRegisterCANFDEvent)(const ps32 AObj, const TCANFDEvent AEvent);
typedef s32(__stdcall* TUnregisterCANFDEvent)(const ps32 AObj, const TCANFDEvent AEvent);
typedef s32(__stdcall* TRegisterLINEvent)(const ps32 AObj, const TLINEvent AEvent);
typedef s32(__stdcall* TUnregisterLINEvent)(const ps32 AObj, const TLINEvent AEvent);
typedef s32(__stdcall* TUnregisterCANEvents)(const ps32 AObj);
typedef s32(__stdcall* TUnregisterLINEvents)(const ps32 AObj);
typedef s32(__stdcall* TUnregisterCANFDEvents)(const ps32 AObj);
typedef s32(__stdcall* TUnregisterALLEvents)(const ps32 AObj);
typedef s32(__stdcall* TEnableBusStatistics)(const bool AEnable);
typedef s32(__stdcall* TClearBusStatistics)(void);
typedef s32(__stdcall* TGetBusStatistics)(const TLIBApplicationChannelType ABusType, const s32 AIdxChn, const TLIBCANBusStatistics AIdxStat, pdouble AStat);
typedef s32(__stdcall* TGetFPSCAN)(const s32 AIdxChn, const s32 AIdentifier, ps32 AFPS);
typedef s32(__stdcall* TGetFPSCANFD)(const s32 AIdxChn, const s32 AIdentifier, ps32 AFPS);
typedef s32(__stdcall* TGetFPSLIN)(const s32 AIdxChn, const s32 AIdentifier, ps32 AFPS);
typedef s32(__stdcall* TWaitCANMessage)(const void* AObj, const PCAN ATxCAN, const PCAN ARxCAN, const s32 ATimeoutMS);
typedef s32(__stdcall* TWaitCANFDMessage)(const void* AObj, const PCANFD ATxCANFD, const PCANFD ARxCANFD, const s32 ATimeoutMS);
typedef s32(__stdcall* TAddCyclicMsgCAN)(const PCAN ACAN, const float APeriodMS);
typedef s32(__stdcall* TAddCyclicMsgCANFD)(const PCANFD ACANFD, const float APeriodMS);
typedef s32(__stdcall* TDeleteCyclicMsgCAN)(const PCAN ACAN);
typedef s32(__stdcall* TDeleteCyclicMsgCANFD)(const PCANFD ACANFD);
typedef s32(__stdcall* TDeleteCyclicMsgs)(void);
// online replay functions
typedef s32(__stdcall* Ttslog_add_online_replay_config)(const char* AFileName, s32* AIndex);
typedef s32(__stdcall* Ttslog_set_online_replay_config)(const s32 AIndex, const char* AName, const char* AFileName, const bool AAutoStart, const bool AIsRepetitiveMode, const TLIBOnlineReplayTimingMode AStartTimingMode, const s32 AStartDelayTimeMs, const bool ASendTx, const bool ASendRx, const char* AMappings);
typedef s32(__stdcall* Ttslog_get_online_replay_count)(s32* ACount);
typedef s32(__stdcall* Ttslog_get_online_replay_config)(const s32 AIndex, char** AName, char** AFileName, bool* AAutoStart, bool* AIsRepetitiveMode, TLIBOnlineReplayTimingMode* AStartTimingMode, s32* AStartDelayTimeMs, bool* ASendTx, bool* ASendRx, char** AMappings);
typedef s32(__stdcall* Ttslog_del_online_replay_config)(const s32 AIndex);
typedef s32(__stdcall* Ttslog_del_online_replay_configs)(void);
typedef s32(__stdcall* Ttslog_start_online_replay)(const s32 AIndex);
typedef s32(__stdcall* Ttslog_start_online_replays)(void);
typedef s32(__stdcall* Ttslog_pause_online_replay)(const s32 AIndex);
typedef s32(__stdcall* Ttslog_pause_online_replays)(void);
typedef s32(__stdcall* Ttslog_stop_online_replay)(const s32 AIndex);
typedef s32(__stdcall* Ttslog_stop_online_replays)(void);
typedef s32(__stdcall* Ttslog_get_online_replay_status)(const s32 AIndex, TLIBOnlineReplayStatus* AStatus, float* AProgressPercent100);
// CAN rbs functions
typedef s32(__stdcall* TCANRBSStart)(void);
typedef s32(__stdcall* TCANRBSStop)(void);
typedef s32(__stdcall* TCANRBSIsRunning)(bool* AIsRunning);
typedef s32(__stdcall* TCANRBSConfigure)(const bool AAutoStart, const bool AAutoSendOnModification, const bool AActivateNodeSimulation, const TLIBRBSInitValueOptions AInitValueOptions);
typedef s32(__stdcall* TCANRBSActivateAllNetworks)(const bool AEnable, const bool AIncludingChildren);
typedef s32(__stdcall* TCANRBSActivateNetworkByName)(const bool AEnable, const char* ANetworkName, const bool AIncludingChildren);
typedef s32(__stdcall* TCANRBSActivateNodeByName)(const bool AEnable, const char* ANetworkName, const char* ANodeName, const bool AIncludingChildren);
typedef s32(__stdcall* TCANRBSActivateMessageByName)(const bool AEnable, const char* ANetworkName, const char* ANodeName, const char* AMsgName);*/
typedef s32(__stdcall* TCANRBSGetSignalValueByElement)(const s32 AIdxChn, const char* ANetworkName, const char* ANodeName, const char* AMsgName, const char* ASignalName, double* AValue);
typedef s32(__stdcall* TCANRBSGetSignalValueByAddress)(const char* ASymbolAddress, double* AValue);
typedef s32(__stdcall* TCANRBSSetSignalValueByElement)(const s32 AIdxChn, const char* ANetworkName, const char* ANodeName, const char* AMsgName, const char* ASignalName, const double AValue);
typedef s32(__stdcall* TCANRBSSetSignalValueByAddress)(const char* ASymbolAddress, const double AValue);



#endif