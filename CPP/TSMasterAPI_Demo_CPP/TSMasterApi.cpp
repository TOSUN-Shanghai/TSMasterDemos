#include "TSMasterApi.h"

#include <windows.h>  


static bool read_bool(u8 value, u8 mask) {
	if ((value & mask) != 0)
		return true;
	return false;
};
static void set_bool(u8& value, u8 mask, bool inp) {
	if (inp)
	{
		value |= mask;
	}
	else {
		value &= (~mask);
	}
};

// CAN definitions
#define MASK_CANProp_DIR_TX 0x01
#define MASK_CANProp_REMOTE 0x02
#define MASK_CANProp_EXTEND 0x04
#define MASK_CANProp_ERROR  0x80
#define MASK_CANProp_LOGGED 0x60

bool _TCAN::is_tx_get()
{
	return read_bool(FProperties, MASK_CANProp_DIR_TX);
}
void _TCAN::is_tx_set(bool inp)
{
	set_bool(FProperties, MASK_CANProp_DIR_TX, inp);
}
bool _TCAN::is_data_get()
{
	return !read_bool(FProperties, MASK_CANProp_REMOTE);
}
void _TCAN::is_data_set(bool inp)
{
	set_bool(FProperties, MASK_CANProp_DIR_TX, !inp);
}
bool _TCAN::is_std_get()
{
	return !read_bool(FProperties, MASK_CANProp_EXTEND);
}
void _TCAN::is_std_set(bool inp)
{
	set_bool(FProperties, MASK_CANProp_EXTEND, !inp);
}
bool _TCAN::is_err_get()
{
	return read_bool(FProperties, MASK_CANProp_ERROR);
}
void _TCAN::is_err_set(bool inp)
{
	set_bool(FProperties, MASK_CANProp_ERROR, inp);
}


bool _TCANFD::is_tx_get()
{
	return read_bool(FProperties, MASK_CANProp_DIR_TX);
}
void _TCANFD::is_tx_set(bool inp)
{
	set_bool(FProperties, MASK_CANProp_DIR_TX, inp);
}
bool _TCANFD::is_data_get()
{
	return !read_bool(FProperties, MASK_CANProp_REMOTE);
}
void _TCANFD::is_data_set(bool inp)
{
	set_bool(FProperties, MASK_CANProp_DIR_TX, !inp);
}
bool _TCANFD::is_std_get()
{
	return !read_bool(FProperties, MASK_CANProp_EXTEND);
}
void _TCANFD::is_std_set(bool inp)
{
	set_bool(FProperties, MASK_CANProp_EXTEND, !inp);
}
bool _TCANFD::is_err_get()
{
	return read_bool(FProperties, MASK_CANProp_ERROR);
}
void _TCANFD::is_err_set(bool inp)
{
	set_bool(FProperties, MASK_CANProp_ERROR, inp);
}

// CAN FD message properties
#define MASK_CANFDProp_IS_FD 0x01
#define MASK_CANFDProp_IS_EDL MASK_CANFDProp_IS_FD
#define MASK_CANFDProp_IS_BRS 0x02
#define MASK_CANFDProp_IS_ESI 0x04
bool _TCANFD::is_edl_get()
{
	return read_bool(FFDProperties, MASK_CANFDProp_IS_EDL);
}
void _TCANFD::is_edl_set(bool inp)
{
	set_bool(FFDProperties, MASK_CANFDProp_IS_EDL, inp);
}
bool _TCANFD::is_brs_get()
{
	return read_bool(FFDProperties, MASK_CANFDProp_IS_BRS);
}
void _TCANFD::is_brs_set(bool inp)
{
	set_bool(FFDProperties, MASK_CANFDProp_IS_BRS, inp);
}
bool _TCANFD::is_esi_get()
{
	return read_bool(FFDProperties, MASK_CANFDProp_IS_ESI);
}
void _TCANFD::is_esi_set(bool inp)
{
	set_bool(FFDProperties, MASK_CANFDProp_IS_ESI, inp);
}


// LIN message properties
#define MASK_LINProp_DIR_TX         0x01
#define MASK_LINProp_SEND_BREAK     0x02
#define MASK_LINProp_RECEIVED_BREAK 0x04
#define MASK_LINProp_SEND_SYNC      0x80
#define MASK_LINProp_RECEIVED_SYNC  0x10

bool _TLIN::is_tx_get()
{
	return read_bool(FProperties, MASK_LINProp_DIR_TX);
}
void _TLIN::is_tx_set(bool inp)
{
	set_bool(FProperties, MASK_LINProp_DIR_TX, inp);
}
bool _TLIN::is_send_break_get()
{
	return read_bool(FProperties, MASK_LINProp_SEND_BREAK);
}
void _TLIN::is_send_break_set(bool inp)
{
	set_bool(FProperties, MASK_LINProp_SEND_BREAK, inp);
}
bool _TLIN::is_reccived_break_get()
{
	return read_bool(FProperties, MASK_LINProp_RECEIVED_BREAK);
}
void _TLIN::is_reccived_break_set(bool inp)
{
	set_bool(FProperties, MASK_LINProp_RECEIVED_BREAK, inp);
}
bool _TLIN::is_send_sync_get()
{
	return read_bool(FProperties, MASK_LINProp_SEND_SYNC);
}
void _TLIN::is_send_sync_set(bool inp)
{
	set_bool(FProperties, MASK_LINProp_SEND_SYNC, inp);
}
bool _TLIN::is_reccived_sync_get()
{
	return read_bool(FProperties, MASK_LINProp_RECEIVED_SYNC);
}
void _TLIN::is_reccived_sync_set(bool inp)
{
	set_bool(FProperties, MASK_LINProp_RECEIVED_SYNC, inp);
}


static std::wstring Str2Wstr(std::string str)
{
	if (str.length() == 0)
		return L"";

	std::wstring wstr;
	wstr.assign(str.begin(), str.end());
	return wstr;
}


class TSMasterApi_priv
{
private:
	std::string last_error;
	HMODULE hDll = NULL;
	template <typename T> bool load_ptr(T& ptr, const std::string& name) {
		ptr = (T)GetProcAddress(hDll, name.c_str());
		if (ptr == nullptr)
		{
			last_error = "TSMasterApi: fail to load function " + name;
		}
		return ptr != nullptr;
	}
public:
	std::string app_name;
	std::string dll_path;
	void(__stdcall* initialize_lib_tsmaster)(const char* pAppName) = nullptr;   //initialize_lib_tsmaster
	void(__stdcall* finalize_lib_tsmaster)(void) = nullptr;   //initialize_lib_tsmaster
	s32(__stdcall* tsapp_add_application)(const char* AAppName) = nullptr;
	s32(__stdcall* tsapp_add_cyclic_msg_can)(const PLIBCAN ACAN, const float
		APeriodMS) = nullptr;
	s32(__stdcall* tsapp_add_cyclic_msg_canfd)(const PLIBCANFD ACANFD, const float
		APeriodMS) = nullptr;
	s32(__stdcall* tsapp_clear_bus_statistics)(void) = nullptr;
	s32(__stdcall* tsapp_configure_baudrate_can)(const s32 AIdxChn, const float
		ABaudrateKbps, const bool AListenOnly, const bool AInstallTermResistor120Ohm)
		= nullptr;
	s32(__stdcall* tsapp_configure_baudrate_canfd)(const s32 AIdxChn, const float
		ABaudrateArbKbps, const float ABaudrateDataKbps, const TCANFDControllerType
		AControllerType, const TCANFDControllerMode AControllerMode, const bool
		AInstallTermResistor120Ohm) = nullptr;
	s32(__stdcall* tsapp_configure_baudrate_lin)(const s32 AIdxChn, const float ABaudrateKbps, const s32 AProtocol);
	s32(__stdcall* tsapp_connect)(void) = nullptr;
	s32(__stdcall* tsapp_del_application)(const char* AAppName) = nullptr;
	s32(__stdcall* tsapp_del_mapping)(const PLIBTSMapping AMapping) = nullptr;
	s32(__stdcall* tsapp_del_mapping_verbose)(const char* AAppName,
		const TLIBApplicationChannelType AAppChannelType,
		const s32 AAppChannel) = nullptr;
	s32(__stdcall* tsapp_delete_cyclic_msg_can)(const PLIBCAN ACAN) = nullptr;
	s32(__stdcall* tsapp_delete_cyclic_msg_canfd)(const PLIBCANFD ACANFD) = nullptr;
	s32(__stdcall* tsapp_delete_cyclic_msgs)(void) = nullptr;
	s32(__stdcall* tsapp_disconnect)(void) = nullptr;
	s32(__stdcall* tsapp_enable_bus_statistics)(const bool AEnable) = nullptr;
	s32(__stdcall* tsapp_enumerate_hw_devices)(const ps32 ACount) = nullptr;
	s32(__stdcall* tsapp_execute_python_string)(const char* AString, const bool
		AIsSync, const bool AIsX64, char** AResultLog) = nullptr;
	s32(__stdcall* tsapp_execute_python_script)(const char* AFilePath, const bool
		AIsSync, const bool AIsX64, char** AResultLog) = nullptr;
	s32(__stdcall* tsapp_get_application_list)(char** AAppNameList) = nullptr;
	s32(__stdcall* tsapp_get_bus_statistics)(const TLIBApplicationChannelType
		ABusType, const s32 AIdxChn, const TLIBCANBusStatistics AIdxStat, pdouble
		AStat) = nullptr;
	s32(__stdcall* tsapp_get_can_channel_count)(const ps32 ACount) = nullptr;
	s32(__stdcall* tsapp_get_current_application)(const char** AAppName) = nullptr;
	s32(__stdcall* tsapp_get_error_description)(const s32 ACode, char** ADesc) =
		nullptr;
	s32(__stdcall* tsapp_get_fps_can)(const s32 AIdxChn, const s32 AIdentifier,
		ps32 AFPS) = nullptr;
	s32(__stdcall* tsapp_get_fps_canfd)(const s32 AIdxChn, const s32 AIdentifier,
		ps32 AFPS) = nullptr;
	s32(__stdcall* tsapp_get_fps_lin)(const s32 AIdxChn, const s32 AIdentifier,
		ps32 AFPS) = nullptr;
	s32(__stdcall* tsapp_get_hw_info_by_index)(const s32 AIndex, const PLIBHWInfo
		AHWInfo) = nullptr;
	s32(__stdcall* tsapp_get_hw_info_by_index_verbose)(const s32 AIndex,
		PLIBBusToolDeviceType ADeviceType,
		char* AVendorNameBuffer, //array[0..31] of AnsiChar = nullptr;
		s32 AVendorNameBufferSize,
		char* ADeviceNameBuffer, //array[0..31] of AnsiChar = nullptr;
		s32 ADeviceNameBufferSize,
		char* ASerialStringBuffer, //array[0..63] of AnsiChar
		s32 ASerialStringBufferSize
		) = nullptr;
	s32(__stdcall* tsapp_get_lin_channel_count)(const ps32 ACount) = nullptr;
	s32(__stdcall* tsapp_get_mapping)(const PLIBTSMapping AMapping) = nullptr;
	s32(__stdcall* tsapp_get_mapping_verbose)(const char* AAppName,
		const TLIBApplicationChannelType AAppChannelType,
		const s32 AAppChannel,
		const PLIBTSMapping AMapping) = nullptr;
	s32(__stdcall* tsapp_get_timestamp)(s64* ATimestamp) = nullptr;
	s32(__stdcall* tsapp_get_turbo_mode)(const bool* AEnable) = nullptr;
	// tsapp_get_vendor_detect_preferences
	void(__stdcall* tsapp_log)(const char* AStr, const TLogLevel ALevel) = nullptr;
	void(__stdcall* tsfifo_enable_receive_error_frames)(void) = nullptr;
	void(__stdcall* tsfifo_enable_receive_fifo)(void) = nullptr;
	void(__stdcall* tsfifo_disable_receive_error_frames)(void) = nullptr;
	void(__stdcall* tsfifo_disable_receive_fifo)(void) = nullptr;
	s32(__stdcall* tsfifo_read_can_buffer_frame_count)(const s32 AIdxChn, ps32
		ACount) = nullptr;
	s32(__stdcall* tsfifo_read_can_rx_buffer_frame_count)(const s32 AIdxChn, ps32
		ACount) = nullptr;
	s32(__stdcall* tsfifo_read_can_tx_buffer_frame_count)(const s32 AIdxChn, ps32
		ACount) = nullptr;
	s32(__stdcall* tsfifo_read_canfd_buffer_frame_count)(const s32 AIdxChn, ps32
		ACount) = nullptr;
	s32(__stdcall* tsfifo_read_canfd_rx_buffer_frame_count)(const s32 AIdxChn, ps32
		ACount) = nullptr;
	s32(__stdcall* tsfifo_read_canfd_tx_buffer_frame_count)(const s32 AIdxChn, ps32
		ACount) = nullptr;
	s32(__stdcall* tsfifo_read_fastlin_buffer_frame_count)(const s32 AIdxChn, ps32
		ACount) = nullptr;
	s32(__stdcall* tsfifo_read_fastlin_rx_buffer_frame_count)(const s32 AIdxChn,
		ps32 ACount) = nullptr;
	s32(__stdcall* tsfifo_read_fastlin_tx_buffer_frame_count)(const s32 AIdxChn,
		ps32 ACount) = nullptr;
	s32(__stdcall* tsfifo_read_lin_buffer_frame_count)(const s32 AIdxChn, ps32
		ACount) = nullptr;
	s32(__stdcall* tsfifo_read_lin_rx_buffer_frame_count)(const s32 AIdxChn, ps32
		ACount) = nullptr;
	s32(__stdcall* tsfifo_read_lin_tx_buffer_frame_count)(const s32 AIdxChn, ps32
		ACount) = nullptr;
	s32(__stdcall* tsfifo_receive_can_msgs)(PLIBCAN ACANBuffers, ps32
		ACANBufferSize, const s32 AIdxChn, const bool AIncludeTx) = nullptr;
	s32(__stdcall* tsfifo_receive_canfd_msgs)(PLIBCANFD ACANFDBuffers, ps32
		ACANFDBufferSize, const s32 AIdxChn, const bool AIncludeTx) = nullptr;
	s32(__stdcall* tsfifo_receive_fastlin_msgs)(PLIBLIN ALINBuffers, ps32
		ALINBufferSize, const s32 AIdxChn, const bool AIncludeTx) = nullptr;
	s32(__stdcall* tsfifo_receive_lin_msgs)(PLIBLIN ALINBuffers, ps32
		ALINBufferSize, const s32 AIdxChn, const bool AIncludeTx) = nullptr;
	s32(__stdcall* tsfifo_clear_can_receive_buffers)(const s32 AIdxChn) = nullptr;
	s32(__stdcall* tsfifo_clear_canfd_receive_buffers)(const s32 AIdxChn) = nullptr;
	s32(__stdcall* tsfifo_clear_fastlin_receive_buffers)(const s32 AIdxChn) =
		nullptr;
	s32(__stdcall* tsfifo_clear_lin_receive_buffers)(const s32 AIdxChn) = nullptr;
	s32(__stdcall* tsapp_register_event_can)(const ps32 AObj, const TCANEvent
		AEvent) = nullptr;
	s32(__stdcall* tsapp_register_event_canfd)(const ps32 AObj, const TCANFDEvent
		AEvent) = nullptr;
	s32(__stdcall* tsapp_register_event_lin)(const ps32 AObj, const TLINEvent
		AEvent) = nullptr;
	s32(__stdcall* tsapp_register_pretx_event_can)(const ps32 AObj, const TCANEvent
		AEvent) = nullptr;
	s32(__stdcall* tsapp_register_pretx_event_canfd)(const ps32 AObj, const
		TCANFDEvent AEvent) = nullptr;
	s32(__stdcall* tsapp_register_pretx_event_lin)(const ps32 AObj, const TLINEvent
		AEvent) = nullptr;
	s32(__stdcall* tsapp_unregister_event_flexray)(const ps32 AObj, const TFlexrayEvent AEvent) = nullptr;
	s32(__stdcall* tsapp_unregister_event_ethernet)(const ps32 AObj, const TEthernetEvent AEvent) = nullptr;
	s32(__stdcall* tsapp_unregister_events_flexray)(const ps32 AObj) = nullptr;
	s32(__stdcall* tsapp_unregister_events_ethernet)(const ps32 AObj) = nullptr;
	s32(__stdcall* tsapp_unregister_pretx_event_flexray)(const ps32 AObj, const TFlexrayEvent AEvent) = nullptr;
	s32(__stdcall* tsapp_unregister_pretx_event_ethernet)(const ps32 AObj, const TEthernetEvent AEvent) = nullptr;
	s32(__stdcall* tsapp_unregister_pretx_events_flexray)(const ps32 AObj) = nullptr;
	s32(__stdcall* tsapp_unregister_pretx_events_ethernet)(const ps32 AObj) = nullptr;
	s32(__stdcall* tsapp_set_can_channel_count)(const s32 ACount) = nullptr;
	s32(__stdcall* tsapp_set_current_application)(const char* AAppName) = nullptr;
	s32(__stdcall* tsapp_set_lin_channel_count)(const s32 ACount) = nullptr;
	s32(__stdcall* tsapp_set_logger)(const TLogger ALogger) = nullptr;
	s32(__stdcall* tsapp_set_mapping)(const PLIBTSMapping AMapping) = nullptr;
	s32(__stdcall* tsapp_set_mapping_verbose)(const char* AAppName,
		const TLIBApplicationChannelType AAppChannelType,
		const s32 AAppChannel,
		const char* AHardwareName,
		const TLIBBusToolDeviceType AHardwareType,
		const s32 AHardwareSubType,
		const s32 AHardwareIndex,
		const s32 AHardwareChannel,
		const bool AEnableMapping) = nullptr;
	s32(__stdcall* tsapp_set_turbo_mode)(const bool AEnable) = nullptr;
	s32(__stdcall* tsapp_set_vendor_detect_preferences)(const bool AScanTOSUN,
		const bool AScanVector,
		const bool AScanPeak,
		const bool AScanKvaser,
		const bool AScanZLG,
		const bool AScanIntrepidcs) = nullptr;
	// tsapp_show_channel_mapping_window
	// tsapp_show_hardware_configuration_window
	s32(__stdcall* tsapp_show_tsmaster_window)(const char* AWindowName, const bool
		AWaitClose) = nullptr;
	s32(__stdcall* tsapp_start_logging)(const char* AFullFileName) = nullptr;
	s32(__stdcall* tsapp_stop_logging)(void) = nullptr;
	s32(__stdcall* tsapp_transmit_can_async)(const PLIBCAN ACAN) = nullptr;
	s32(__stdcall* tsapp_transmit_canfd_async)(const PLIBCANFD ACANFD) = nullptr;
	s32(__stdcall* tsapp_transmit_lin_async)(const PLIBLIN ALIN) = nullptr;
	s32(__stdcall* tsapp_transmit_flexray_async)(const PLIBFlexRay ALIN) = nullptr;
	s32(__stdcall* tsapp_transmit_ethernet_async)(const PLIBEthernetHeader ALIN) = nullptr;
	s32(__stdcall* tsapp_transmit_header_and_receive_msg)(s32 AChn, u8 AIdentifier, u8 ADLC, PLIBLIN ALINData, s32 ATimeoutMs) = nullptr;
	s32(__stdcall* tsapp_transmit_can_sync)(const PLIBCAN ACAN, const s32
		ATimeoutMS) = nullptr;
	s32(__stdcall* tsapp_transmit_canfd_sync)(const PLIBCANFD ACANFD, const s32
		ATimeoutMS) = nullptr;
	s32(__stdcall* tsapp_transmit_lin_sync)(const PLIBLIN ALIN, const s32
		ATimeoutMS) = nullptr;
	// tsapp_transmit_fastlin_async
	s32(__stdcall* tsapp_unregister_event_can)(const ps32 AObj, const TCANEvent
		AEvent) = nullptr;
	s32(__stdcall* tsapp_unregister_event_canfd)(const ps32 AObj, const TCANFDEvent
		AEvent) = nullptr;
	s32(__stdcall* tsapp_unregister_event_lin)(const ps32 AObj, const TLINEvent
		AEvent) = nullptr;
	s32(__stdcall* tsapp_unregister_events_can)(const ps32 AObj) = nullptr;
	s32(__stdcall* tsapp_unregister_events_lin)(const ps32 AObj) = nullptr;
	s32(__stdcall* tsapp_unregister_events_canfd)(const ps32 AObj) = nullptr;
	s32(__stdcall* tsapp_unregister_events_all)(const ps32 AObj) = nullptr;
	s32(__stdcall* tsapp_unregister_pretx_event_can)(const ps32 AObj, const
		TCANEvent AEvent) = nullptr;
	s32(__stdcall* tsapp_unregister_pretx_event_canfd)(const ps32 AObj, const
		TCANFDEvent AEvent) = nullptr;
	s32(__stdcall* tsapp_unregister_pretx_event_lin)(const ps32 AObj, const
		TLINEvent AEvent) = nullptr;
	s32(__stdcall* tsapp_unregister_pretx_events_can)(const ps32 AObj) = nullptr;
	s32(__stdcall* tsapp_unregister_pretx_events_lin)(const ps32 AObj) = nullptr;
	s32(__stdcall* tsapp_unregister_pretx_events_canfd)(const ps32 AObj) = nullptr;
	s32(__stdcall* tsapp_unregister_pretx_events_all)(const ps32 AObj) = nullptr;
	// tsapp_update_cyclic_msg_can
	s32(__stdcall* tscom_can_rbs_start)(void) = nullptr;
	s32(__stdcall* tscom_can_rbs_stop)(void) = nullptr;
	s32(__stdcall* tscom_can_rbs_is_running)(bool* AIsRunning) = nullptr;
	s32(__stdcall* tscom_can_rbs_configure)(const bool AAutoStart, const bool
		AAutoSendOnModification, const bool AActivateNodeSimulation, const
		TLIBRBSInitValueOptions AInitValueOptions) = nullptr;
	s32(__stdcall* tscom_can_rbs_activate_all_networks)(const bool AEnable, const
		bool AIncludingChildren) = nullptr;
	s32(__stdcall* tscom_can_rbs_activate_network_by_name)(const bool AEnable,
		const char* ANetworkName, const bool AIncludingChildren) = nullptr;
	s32(__stdcall* tscom_can_rbs_activate_node_by_name)(const bool AEnable, const
		char* ANetworkName, const char* ANodeName, const bool AIncludingChildren) =
		nullptr;
	s32(__stdcall* tscom_can_rbs_activate_message_by_name)(const bool AEnable,
		const char* ANetworkName, const char* ANodeName, const char* AMsgName) =
		nullptr;
	s32(__stdcall* tscom_can_rbs_get_signal_value_by_element)(const s32 AIdxChn,
		const char* ANetworkName, const char* ANodeName, const char* AMsgName, const
		char* ASignalName, double* AValue) = nullptr;
	s32(__stdcall* tscom_can_rbs_get_signal_value_by_address)(const char*
		ASymbolAddress, double* AValue) = nullptr;
	s32(__stdcall* tscom_can_rbs_set_signal_value_by_element)(const s32 AIdxChn,
		const char* ANetworkName, const char* ANodeName, const char* AMsgName, const
		char* ASignalName, const double AValue) = nullptr;
	s32(__stdcall* tscom_can_rbs_set_signal_value_by_address)(const char*
		ASymbolAddress, const double AValue) = nullptr;
	s32(__stdcall* tsdb_get_signal_value_can)(const PLIBCAN ACAN, const char*
		AMsgName, const char* ASgnName, double* AValue) = nullptr;
	s32(__stdcall* tsdb_get_signal_value_canfd)(const PLIBCANFD ACANFD, const char*
		AMsgName, const char* ASgnName, double* AValue) = nullptr;
	s32(__stdcall* tsdb_set_signal_value_can)(const PLIBCAN ACAN, const char*
		AMsgName, const char* ASgnName, const double AValue) = nullptr;
	s32(__stdcall* tsdb_set_signal_value_canfd)(const PLIBCANFD ACANFD, const char*
		AMsgName, const char* ASgnName, const double AValue) = nullptr;
	s32(__stdcall* tsdb_load_can_db)(const char* ADBC, const char*
		ASupportedChannelsBased0, u32* AId) = nullptr;
	s32(__stdcall* tsdb_unload_can_db)(const u32 AId) = nullptr;
	s32(__stdcall* tsdb_unload_can_dbs)(void) = nullptr;
	s32(__stdcall* tsdb_get_can_db_count)(s32* ACount) = nullptr;
	s32(__stdcall* tsdb_get_can_db_id)(const s32 AIndex, u32* AId) = nullptr;
	s32(__stdcall* tsdb_get_can_db_info)(const u32 ADatabaseId, const s32 AType,
		const s32 AIndex, const s32 ASubIndex, char** AValue) = nullptr;
	s32(__stdcall* tslog_add_online_replay_config)(const char* AFileName, s32*
		AIndex) = nullptr;
	s32(__stdcall* tslog_set_online_replay_config)(const s32 AIndex, const char*
		AName, const char* AFileName, const bool AAutoStart, const bool
		AIsRepetitiveMode, const TLIBOnlineReplayTimingMode AStartTimingMode, const
		s32 AStartDelayTimeMs, const bool ASendTx, const bool ASendRx, const char*
		AMappings) = nullptr;
	s32(__stdcall* tslog_get_online_replay_count)(s32* ACount) = nullptr;
	s32(__stdcall* tslog_get_online_replay_config)(const s32 AIndex, char** AName,
		char** AFileName, bool* AAutoStart, bool* AIsRepetitiveMode,
		TLIBOnlineReplayTimingMode* AStartTimingMode, s32* AStartDelayTimeMs, bool*
		ASendTx, bool* ASendRx, char** AMappings) = nullptr;
	s32(__stdcall* tslog_del_online_replay_config)(const s32 AIndex) = nullptr;
	s32(__stdcall* tslog_del_online_replay_configs)(void) = nullptr;
	s32(__stdcall* tslog_start_online_replay)(const s32 AIndex) = nullptr;
	s32(__stdcall* tslog_start_online_replays)(void) = nullptr;
	s32(__stdcall* tslog_pause_online_replay)(const s32 AIndex) = nullptr;
	s32(__stdcall* tslog_pause_online_replays)(void) = nullptr;
	s32(__stdcall* tslog_stop_online_replay)(const s32 AIndex) = nullptr;
	s32(__stdcall* tslog_stop_online_replays)(void) = nullptr;
	s32(__stdcall* tslog_get_online_replay_status)(const s32 AIndex,
		TLIBOnlineReplayStatus* AStatus, float* AProgressPercent101) = nullptr;

	s32(__stdcall* tslog_blf_write_start)(const char* AFileName, int* AHandle) = nullptr; //stdcall
	s32(__stdcall* tslog_blf_write_can)(int AHandle, PLIBCAN ACAN) = nullptr;
	s32(__stdcall* tslog_blf_write_can_fd)(int AHandle, PLIBCANFD ACANFD) = nullptr;
	s32(__stdcall* tslog_blf_write_lin)(int AHandle, PLIBLIN ALIN) = nullptr;
	s32(__stdcall* tslog_blf_write_realtime_comment)(int AHandle, s64 ATimeUs, char* AComment) = nullptr;
	s32(__stdcall* tslog_blf_write_end)(int AHandle) = nullptr;
	s32(__stdcall* tslog_blf_read_start)(const char* AFileName, int* AHandle, int* AObjCount) = nullptr;
	s32(__stdcall* tsLog_blf_read_start_verbose)(const char* AFileName, int* AHandle, int* AObjCount,
		u16* AYear, u16* AMonth, u16* ADayOfWeek,
		u16* ADay, u16* AHour, u16* AMinute,
		u16* ASecond, u16* AMilliseconds) = nullptr;
	s32(__stdcall* tslog_blf_read_status)(int AHandle, int* AObjReadCount) = nullptr;
	s32(__stdcall* tslog_blf_read_object)(int AHandle, int* AProgressedCnt, int* AType/* PSupportedObjType*/, PLIBCAN ACAN,
		PLIBLIN ALIN, PLIBCANFD ACANFD) = nullptr;
	s32(__stdcall* tslog_blf_read_object_w_comment)(int AHandle, int* AProgressedCnt, int* AType/* PSupportedObjType*/,
		PLIBCAN ACAN, PLIBLIN ALIN, PLIBCANFD ACANFD, PRealtime_comment_t AComment) = nullptr;
	s32(__stdcall* tslog_blf_read_end)(int AHandle) = nullptr;
	s32(__stdcall* tslog_blf_seek_object_time)(int AHandle, const double AProg100, s64* ATime, int* AProgressedCnt) = nullptr;

	s32(__stdcall* tslin_enable_runtime_schedule_table)(const s32 AChnIdx) = nullptr;
	s32(__stdcall* tslin_set_schedule_table)(const s32 AChnIdx, const s32 ASchIndex) = nullptr;
	s32(__stdcall* tslin_stop_lin_channel)(const s32 AChnIdx) = nullptr;
	s32(__stdcall* tslin_start_lin_channel)(const s32 AChnIdx) = nullptr;
	s32(__stdcall* tslin_set_node_funtiontype)(const s32 AChnIdx, const TLINNodeType AFunctionType) = nullptr;

	bool is_ready() {
		return hDll != NULL;
	}
	const std::string get_last_error()
	{
		return last_error;
	}
	TSMasterApi_priv(const std::string& app_name, const std::string& dll_path)
	{
		this->app_name = app_name;
		this->dll_path = dll_path;

		// Loads the DLL
		auto str_tmp = Str2Wstr(dll_path);
		hDll = LoadLibrary(str_tmp.c_str());
		if (hDll == NULL)
		{
			last_error = "TSMasterApi: fail to load dll at " + dll_path;
		}
		else {
			if (load_ptr(initialize_lib_tsmaster, "initialize_lib_tsmaster")
				&& load_ptr(finalize_lib_tsmaster, "finalize_lib_tsmaster")
				&& load_ptr(tsapp_add_application, "tsapp_add_application")
				&& load_ptr(tsapp_add_cyclic_msg_can, "tsapp_add_cyclic_msg_can")
				&& load_ptr(tsapp_add_cyclic_msg_canfd, "tsapp_add_cyclic_msg_canfd")
				&& load_ptr(tsapp_clear_bus_statistics, "tsapp_clear_bus_statistics")
				&& load_ptr(tsapp_configure_baudrate_can, "tsapp_configure_baudrate_can")
				&& load_ptr(tsapp_configure_baudrate_canfd, "tsapp_configure_baudrate_canfd")
				&& load_ptr(tsapp_configure_baudrate_lin, "tsapp_configure_baudrate_lin")
				&& load_ptr(tsapp_connect, "tsapp_connect")
				&& load_ptr(tsapp_del_application, "tsapp_del_application")
				&& load_ptr(tsapp_del_mapping, "tsapp_del_mapping")
				&& load_ptr(tsapp_del_mapping_verbose, "tsapp_del_mapping_verbose")
				&& load_ptr(tsapp_delete_cyclic_msg_can, "tsapp_delete_cyclic_msg_can")
				&& load_ptr(tsapp_delete_cyclic_msg_canfd, "tsapp_delete_cyclic_msg_canfd")
				&& load_ptr(tsapp_delete_cyclic_msgs, "tsapp_delete_cyclic_msgs")
				&& load_ptr(tsapp_disconnect, "tsapp_disconnect")
				&& load_ptr(tsapp_enable_bus_statistics, "tsapp_enable_bus_statistics")
				&& load_ptr(tsapp_enumerate_hw_devices, "tsapp_enumerate_hw_devices")
				&& load_ptr(tsapp_execute_python_string, "tsapp_execute_python_string")
				&& load_ptr(tsapp_execute_python_script, "tsapp_execute_python_script")
				&& load_ptr(tsapp_get_application_list, "tsapp_get_application_list")
				&& load_ptr(tsapp_get_bus_statistics, "tsapp_get_bus_statistics")
				&& load_ptr(tsapp_get_can_channel_count, "tsapp_get_can_channel_count")
				&& load_ptr(tsapp_get_current_application, "tsapp_get_current_application")
				&& load_ptr(tsapp_get_error_description, "tsapp_get_error_description")
				&& load_ptr(tsapp_get_fps_can, "tsapp_get_fps_can")
				&& load_ptr(tsapp_get_fps_canfd, "tsapp_get_fps_canfd")
				&& load_ptr(tsapp_get_fps_lin, "tsapp_get_fps_lin")
				&& load_ptr(tsapp_get_hw_info_by_index, "tsapp_get_hw_info_by_index")
				&& load_ptr(tsapp_get_hw_info_by_index_verbose,
					"tsapp_get_hw_info_by_index_verbose")
				&& load_ptr(tsapp_get_lin_channel_count, "tsapp_get_lin_channel_count")
				&& load_ptr(tsapp_get_mapping, "tsapp_get_mapping")
				&& load_ptr(tsapp_get_mapping_verbose, "tsapp_get_mapping_verbose")
				&& load_ptr(tsapp_get_timestamp, "tsapp_get_timestamp")
				&& load_ptr(tsapp_get_turbo_mode, "tsapp_get_turbo_mode")
				&& load_ptr(tsapp_log, "tsapp_log")
				&& load_ptr(tsfifo_enable_receive_error_frames, "tsfifo_enable_receive_error_frames")
				&& load_ptr(tsfifo_enable_receive_fifo, "tsfifo_enable_receive_fifo")
				&& load_ptr(tsfifo_disable_receive_error_frames, "tsfifo_disable_receive_error_frames")
				&& load_ptr(tsfifo_disable_receive_fifo, "tsfifo_disable_receive_fifo")
				&& load_ptr(tsfifo_read_can_buffer_frame_count,
					"tsfifo_read_can_buffer_frame_count")
				&& load_ptr(tsfifo_read_can_rx_buffer_frame_count,
					"tsfifo_read_can_rx_buffer_frame_count")
				&& load_ptr(tsfifo_read_can_tx_buffer_frame_count,
					"tsfifo_read_can_tx_buffer_frame_count")
				&& load_ptr(tsfifo_read_canfd_buffer_frame_count,
					"tsfifo_read_canfd_buffer_frame_count")
				&& load_ptr(tsfifo_read_canfd_rx_buffer_frame_count,
					"tsfifo_read_canfd_rx_buffer_frame_count")
				&& load_ptr(tsfifo_read_canfd_tx_buffer_frame_count,
					"tsfifo_read_canfd_tx_buffer_frame_count")
				&& load_ptr(tsfifo_read_fastlin_buffer_frame_count,
					"tsfifo_read_fastlin_buffer_frame_count")
				&& load_ptr(tsfifo_read_fastlin_rx_buffer_frame_count,
					"tsfifo_read_fastlin_rx_buffer_frame_count")
				&& load_ptr(tsfifo_read_fastlin_tx_buffer_frame_count,
					"tsfifo_read_fastlin_tx_buffer_frame_count")
				&& load_ptr(tsfifo_read_lin_buffer_frame_count,
					"tsfifo_read_lin_buffer_frame_count")
				&& load_ptr(tsfifo_read_lin_rx_buffer_frame_count,
					"tsfifo_read_lin_rx_buffer_frame_count")
				&& load_ptr(tsfifo_read_lin_tx_buffer_frame_count,
					"tsfifo_read_lin_tx_buffer_frame_count")
				&& load_ptr(tsfifo_receive_can_msgs, "tsfifo_receive_can_msgs")
				&& load_ptr(tsfifo_receive_canfd_msgs, "tsfifo_receive_canfd_msgs")
				&& load_ptr(tsfifo_receive_fastlin_msgs, "tsfifo_receive_fastlin_msgs")
				&& load_ptr(tsfifo_receive_lin_msgs, "tsfifo_receive_lin_msgs")
				&& load_ptr(tsfifo_clear_can_receive_buffers,
					"tsfifo_clear_can_receive_buffers")
				&& load_ptr(tsfifo_clear_canfd_receive_buffers,
					"tsfifo_clear_canfd_receive_buffers")
				&& load_ptr(tsfifo_clear_fastlin_receive_buffers,
					"tsfifo_clear_fastlin_receive_buffers")
				&& load_ptr(tsfifo_clear_lin_receive_buffers,
					"tsfifo_clear_lin_receive_buffers")
				&& load_ptr(tsapp_register_event_can, "tsapp_register_event_can")
				&& load_ptr(tsapp_register_event_canfd, "tsapp_register_event_canfd")
				&& load_ptr(tsapp_register_event_lin, "tsapp_register_event_lin")
				&& load_ptr(tsapp_register_pretx_event_can, "tsapp_register_pretx_event_can")
				&& load_ptr(tsapp_register_pretx_event_canfd,
					"tsapp_register_pretx_event_canfd")
				&& load_ptr(tsapp_register_pretx_event_lin, "tsapp_register_pretx_event_lin")
				&& load_ptr(tsapp_unregister_event_flexray, "tsapp_unregister_event_flexray")
				&& load_ptr(tsapp_unregister_event_ethernet, "tsapp_unregister_event_ethernet")
				&& load_ptr(tsapp_unregister_events_flexray, "tsapp_unregister_events_flexray")
				&& load_ptr(tsapp_unregister_events_ethernet, "tsapp_unregister_events_ethernet")
				&& load_ptr(tsapp_unregister_pretx_event_flexray, "tsapp_unregister_pretx_event_flexray")
				&& load_ptr(tsapp_unregister_pretx_event_ethernet, "tsapp_unregister_pretx_event_ethernet")
				&& load_ptr(tsapp_unregister_pretx_events_flexray, "tsapp_unregister_pretx_events_flexray")
				&& load_ptr(tsapp_unregister_pretx_events_ethernet, "tsapp_unregister_pretx_events_ethernet")
				&& load_ptr(tsapp_set_can_channel_count, "tsapp_set_can_channel_count")
				&& load_ptr(tsapp_set_current_application, "tsapp_set_current_application")
				&& load_ptr(tsapp_set_lin_channel_count, "tsapp_set_lin_channel_count")
				&& load_ptr(tsapp_set_logger, "tsapp_set_logger")
				&& load_ptr(tsapp_set_mapping, "tsapp_set_mapping")
				&& load_ptr(tsapp_set_mapping_verbose, "tsapp_set_mapping_verbose")
				&& load_ptr(tsapp_set_turbo_mode, "tsapp_set_turbo_mode")
				&& load_ptr(tsapp_set_vendor_detect_preferences,
					"tsapp_set_vendor_detect_preferences")
				&& load_ptr(tsapp_show_tsmaster_window, "tsapp_show_tsmaster_window")
				&& load_ptr(tsapp_start_logging, "tsapp_start_logging")
				&& load_ptr(tsapp_stop_logging, "tsapp_stop_logging")
				&& load_ptr(tsapp_transmit_can_async, "tsapp_transmit_can_async")
				&& load_ptr(tsapp_transmit_canfd_async, "tsapp_transmit_canfd_async")
				&& load_ptr(tsapp_transmit_lin_async, "tsapp_transmit_lin_async")
				&& load_ptr(tsapp_transmit_flexray_async, "tsapp_transmit_flexray_async")
				&& load_ptr(tsapp_transmit_ethernet_async, " tsapp_transmit_ethernet_async")
				&& load_ptr(tsapp_transmit_header_and_receive_msg, "tsapp_transmit_header_and_receive_msg")
				&& load_ptr(tsapp_transmit_can_sync, "tsapp_transmit_can_sync")
				&& load_ptr(tsapp_transmit_canfd_sync, "tsapp_transmit_canfd_sync")
				&& load_ptr(tsapp_transmit_lin_sync, "tsapp_transmit_lin_sync")
				&& load_ptr(tsapp_unregister_event_can, "tsapp_unregister_event_can")
				&& load_ptr(tsapp_unregister_event_canfd, "tsapp_unregister_event_canfd")
				&& load_ptr(tsapp_unregister_event_lin, "tsapp_unregister_event_lin")
				&& load_ptr(tsapp_unregister_events_can, "tsapp_unregister_events_can")
				&& load_ptr(tsapp_unregister_events_lin, "tsapp_unregister_events_lin")
				&& load_ptr(tsapp_unregister_events_canfd, "tsapp_unregister_events_canfd")
				&& load_ptr(tsapp_unregister_events_all, "tsapp_unregister_events_all")
				&& load_ptr(tsapp_unregister_pretx_event_can,
					"tsapp_unregister_pretx_event_can")
				&& load_ptr(tsapp_unregister_pretx_event_canfd,
					"tsapp_unregister_pretx_event_canfd")
				&& load_ptr(tsapp_unregister_pretx_event_lin,
					"tsapp_unregister_pretx_event_lin")
				&& load_ptr(tsapp_unregister_pretx_events_can,
					"tsapp_unregister_pretx_events_can")
				&& load_ptr(tsapp_unregister_pretx_events_lin,
					"tsapp_unregister_pretx_events_lin")
				&& load_ptr(tsapp_unregister_pretx_events_canfd,
					"tsapp_unregister_pretx_events_canfd")
				&& load_ptr(tsapp_unregister_pretx_events_all,
					"tsapp_unregister_pretx_events_all")
				&& load_ptr(tscom_can_rbs_start, "tscom_can_rbs_start")
				&& load_ptr(tscom_can_rbs_stop, "tscom_can_rbs_stop")
				&& load_ptr(tscom_can_rbs_is_running, "tscom_can_rbs_is_running")
				&& load_ptr(tscom_can_rbs_configure, "tscom_can_rbs_configure")
				&& load_ptr(tscom_can_rbs_activate_all_networks,
					"tscom_can_rbs_activate_all_networks")
				&& load_ptr(tscom_can_rbs_activate_network_by_name,
					"tscom_can_rbs_activate_network_by_name")
				&& load_ptr(tscom_can_rbs_activate_node_by_name,
					"tscom_can_rbs_activate_node_by_name")
				&& load_ptr(tscom_can_rbs_activate_message_by_name,
					"tscom_can_rbs_activate_message_by_name")
				&& load_ptr(tscom_can_rbs_get_signal_value_by_element,
					"tscom_can_rbs_get_signal_value_by_element")
				&& load_ptr(tscom_can_rbs_get_signal_value_by_address,
					"tscom_can_rbs_get_signal_value_by_address")
				&& load_ptr(tscom_can_rbs_set_signal_value_by_element,
					"tscom_can_rbs_set_signal_value_by_element")
				&& load_ptr(tscom_can_rbs_set_signal_value_by_address,
					"tscom_can_rbs_set_signal_value_by_address")
				&& load_ptr(tsdb_get_signal_value_can, "tsdb_get_signal_value_can")
				&& load_ptr(tsdb_get_signal_value_canfd, "tsdb_get_signal_value_canfd")
				&& load_ptr(tsdb_set_signal_value_can, "tsdb_set_signal_value_can")
				&& load_ptr(tsdb_set_signal_value_canfd, "tsdb_set_signal_value_canfd")
				&& load_ptr(tsdb_load_can_db, "tsdb_load_can_db")
				&& load_ptr(tsdb_unload_can_db, "tsdb_unload_can_db")
				&& load_ptr(tsdb_unload_can_dbs, "tsdb_unload_can_dbs")
				&& load_ptr(tsdb_get_can_db_count, "tsdb_get_can_db_count")
				&& load_ptr(tsdb_get_can_db_id, "tsdb_get_can_db_id")
				&& load_ptr(tsdb_get_can_db_info, "tsdb_get_can_db_info")
				&& load_ptr(tslog_add_online_replay_config, "tslog_add_online_replay_config")
				&& load_ptr(tslog_set_online_replay_config, "tslog_set_online_replay_config")
				&& load_ptr(tslog_get_online_replay_count, "tslog_get_online_replay_count")
				&& load_ptr(tslog_get_online_replay_config, "tslog_get_online_replay_config")
				&& load_ptr(tslog_del_online_replay_config, "tslog_del_online_replay_config")
				&& load_ptr(tslog_del_online_replay_configs, "tslog_del_online_replay_configs")
				&& load_ptr(tslog_start_online_replay, "tslog_start_online_replay")
				&& load_ptr(tslog_start_online_replays, "tslog_start_online_replays")
				&& load_ptr(tslog_pause_online_replay, "tslog_pause_online_replay")
				&& load_ptr(tslog_pause_online_replays, "tslog_pause_online_replays")
				&& load_ptr(tslog_stop_online_replay, "tslog_stop_online_replay")
				&& load_ptr(tslog_stop_online_replays, "tslog_stop_online_replays")
				&& load_ptr(tslog_get_online_replay_status, "tslog_get_online_replay_status")
				&& load_ptr(tslin_enable_runtime_schedule_table, "tslin_enable_runtime_schedule_table")
					&& load_ptr(tslin_set_schedule_table, "tslin_set_schedule_table")
					&& load_ptr(tslin_stop_lin_channel, "tslin_stop_lin_channel")
					&& load_ptr(tslin_start_lin_channel, "tslin_start_lin_channel")
					&& load_ptr(tslin_set_node_funtiontype, "tslin_set_node_funtiontype")
					&& load_ptr(tslog_blf_write_start, "tslog_blf_write_start")
				    && load_ptr(tslog_blf_write_can, "tslog_blf_write_can")
					&& load_ptr(tslog_blf_write_can_fd, "tslog_blf_write_can_fd")
					&& load_ptr(tslog_blf_write_lin, "tslog_blf_write_lin")
					&& load_ptr(tslog_blf_write_realtime_comment, "tslog_blf_write_realtime_comment")
					&& load_ptr(tslog_blf_write_end, "tslog_blf_write_end")
					&& load_ptr(tslog_blf_read_start, "tslog_blf_read_start")
					&& load_ptr(tsLog_blf_read_start_verbose, "tsLog_blf_read_start_verbose")
					&& load_ptr(tslog_blf_read_status, "tslog_blf_read_status")
					&& load_ptr(tslog_blf_read_object, "tslog_blf_read_object")
					&& load_ptr(tslog_blf_read_object_w_comment, "tslog_blf_read_object_w_comment")
					&& load_ptr(tslog_blf_read_end, "tslog_blf_read_end")
					&& load_ptr(tslog_blf_seek_object_time, "tslog_blf_seek_object_time")
				)
			{
				initialize_lib_tsmaster(app_name.c_str());
			}
			else {
				//some function load fail, release dll handle
				FreeLibrary(hDll);
				hDll = NULL;
			}
		}
	}
	~TSMasterApi_priv()
	{
		if (hDll != NULL)
		{
			finalize_lib_tsmaster();
			FreeLibrary(hDll);
			hDll = NULL;
		}
	}
};

bool TSMasterApi::set_app_and_dll(const std::string& app_name, const std::string& dll_path)
{
	//if priv_data_p is already ok
	if (priv_data_p != nullptr
		&& priv_data_p->is_ready()
		)
	{
		//if all par are same
		if (priv_data_p->app_name == app_name && priv_data_p->dll_path == dll_path)
		{
			//nothing to do
		}
		else {
			//free last priv data
			priv_data_p = nullptr;
		}
	}
	if (priv_data_p == nullptr)
	{
		priv_data_p = std::shared_ptr<TSMasterApi_priv>(new TSMasterApi_priv(app_name, dll_path));
	}
	return priv_data_p->is_ready();
}

s32 TSMasterApi::tsapp_add_application(const char* AAppName)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_add_application(AAppName);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_add_cyclic_msg_can(const PLIBCAN ACAN, const float APeriodMS)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_add_cyclic_msg_can(ACAN, APeriodMS);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_add_cyclic_msg_canfd(const PLIBCANFD ACANFD, const float APeriodMS)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_add_cyclic_msg_canfd(ACANFD, APeriodMS);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_clear_bus_statistics(void)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_clear_bus_statistics();
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_configure_baudrate_can(const s32 AIdxChn, const float ABaudrateKbps, const bool AListenOnly, const bool AInstallTermResistor120Ohm)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_configure_baudrate_can(AIdxChn, ABaudrateKbps, AListenOnly, AInstallTermResistor120Ohm);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_configure_baudrate_canfd(const s32 AIdxChn, const float ABaudrateArbKbps, const float ABaudrateDataKbps, const TCANFDControllerType AControllerType, const TCANFDControllerMode AControllerMode, const bool AInstallTermResistor120Ohm)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_configure_baudrate_canfd(AIdxChn, ABaudrateArbKbps, ABaudrateDataKbps, AControllerType, AControllerMode, AInstallTermResistor120Ohm);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_configure_baudrate_lin(const s32 AIdxChn, const float ABaudrateKbps, const s32 AProtocol)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_configure_baudrate_lin(AIdxChn, ABaudrateKbps, AProtocol);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_connect(void)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_connect();
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_del_application(const char* AAppName)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_del_application(AAppName);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_del_mapping(const PLIBTSMapping AMapping)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_del_mapping(AMapping);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_del_mapping_verbose(const char* AAppName,
	const TLIBApplicationChannelType AAppChannelType,
	const s32 AAppChannel)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_del_mapping_verbose(AAppName, AAppChannelType, AAppChannel);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_delete_cyclic_msg_can(const PLIBCAN ACAN)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_delete_cyclic_msg_can(ACAN);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_delete_cyclic_msg_canfd(const PLIBCANFD ACANFD)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_delete_cyclic_msg_canfd(ACANFD);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_delete_cyclic_msgs(void)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_delete_cyclic_msgs();
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_disconnect(void)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_disconnect();
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_enable_bus_statistics(const bool AEnable)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_enable_bus_statistics(AEnable);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_enumerate_hw_devices(const ps32 ACount)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_enumerate_hw_devices(ACount);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_execute_python_string(const char* AString, const bool AIsSync, const bool AIsX64, char** AResultLog)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_execute_python_string(AString, AIsSync, AIsX64, AResultLog);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_execute_python_script(const char* AFilePath, const bool AIsSync, const bool AIsX64, char** AResultLog)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_execute_python_script(AFilePath, AIsSync, AIsX64, AResultLog);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_get_application_list(char** AAppNameList)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_get_application_list(AAppNameList);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_get_bus_statistics(const TLIBApplicationChannelType ABusType, const s32 AIdxChn, const TLIBCANBusStatistics AIdxStat, pdouble AStat)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_get_bus_statistics(ABusType, AIdxChn, AIdxStat, AStat);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_get_can_channel_count(const ps32 ACount)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_get_can_channel_count(ACount);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_get_current_application(const char** AAppName)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_get_current_application(AAppName);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_get_error_description(const s32 ACode, char** ADesc)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_get_error_description(ACode, ADesc);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_get_fps_can(const s32 AIdxChn, const s32 AIdentifier, ps32 AFPS)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_get_fps_can(AIdxChn, AIdentifier, AFPS);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_get_fps_canfd(const s32 AIdxChn, const s32 AIdentifier, ps32 AFPS)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_get_fps_canfd(AIdxChn, AIdentifier, AFPS);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_get_fps_lin(const s32 AIdxChn, const s32 AIdentifier, ps32 AFPS)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_get_fps_lin(AIdxChn, AIdentifier, AFPS);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_get_hw_info_by_index(const s32 AIndex, const PLIBHWInfo AHWInfo)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_get_hw_info_by_index(AIndex, AHWInfo);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_get_hw_info_by_index_verbose(const s32 AIndex,
	PLIBBusToolDeviceType ADeviceType,
	char* AVendorNameBuffer, //array[0..31] of AnsiChar
	s32 AVendorNameBufferSize,
	char* ADeviceNameBuffer, //array[0..31] of AnsiChar
	s32 ADeviceNameBufferSize,
	char* ASerialStringBuffer, //array[0..63] of AnsiChar
	s32 ASerialStringBufferSize
)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_get_hw_info_by_index_verbose(AIndex, ADeviceType
			, AVendorNameBuffer, AVendorNameBufferSize, ADeviceNameBuffer, ADeviceNameBufferSize
			, ASerialStringBuffer, ASerialStringBufferSize);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_get_lin_channel_count(const ps32 ACount)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_get_lin_channel_count(ACount);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_get_mapping(const PLIBTSMapping AMapping)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_get_mapping(AMapping);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_get_mapping_verbose(const char* AAppName,
	const TLIBApplicationChannelType AAppChannelType,
	const s32 AAppChannel,
	const PLIBTSMapping AMapping)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_get_mapping_verbose(AAppName, AAppChannelType, AAppChannel, AMapping);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_get_timestamp(s64* ATimestamp)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_get_timestamp(ATimestamp);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_get_turbo_mode(const bool* AEnable)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_get_turbo_mode(AEnable);
	}
	return IDX_ERR_DLL_NOT_READY;
}
// TSMasterApi::tsapp_get_vendor_detect_preferences
void TSMasterApi::tsapp_log(const char* AStr, const TLogLevel ALevel)
{
	if (priv_data_p != nullptr)
	{
		priv_data_p->tsapp_log(AStr, ALevel);
	}
}
void TSMasterApi::tsfifo_enable_receive_error_frames(void)
{
	if (priv_data_p != nullptr)
	{
		priv_data_p->tsfifo_enable_receive_error_frames();
	}
}
void TSMasterApi::tsfifo_enable_receive_fifo(void)
{
	if (priv_data_p != nullptr)
	{
		priv_data_p->tsfifo_enable_receive_fifo();
	}
}
void TSMasterApi::tsfifo_disable_receive_error_frames(void)
{
	if (priv_data_p != nullptr)
	{
		priv_data_p->tsfifo_disable_receive_error_frames();
	}
}
void TSMasterApi::tsfifo_disable_receive_fifo(void)
{
	if (priv_data_p != nullptr)
	{
		priv_data_p->tsfifo_disable_receive_fifo();
	}
}
s32 TSMasterApi::tsfifo_read_can_buffer_frame_count(const s32 AIdxChn, ps32 ACount)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsfifo_read_can_buffer_frame_count(AIdxChn, ACount);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsfifo_read_can_rx_buffer_frame_count(const s32 AIdxChn, ps32 ACount)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsfifo_read_can_rx_buffer_frame_count(AIdxChn, ACount);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsfifo_read_can_tx_buffer_frame_count(const s32 AIdxChn, ps32 ACount)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsfifo_read_can_tx_buffer_frame_count(AIdxChn, ACount);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsfifo_read_canfd_buffer_frame_count(const s32 AIdxChn, ps32 ACount)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsfifo_read_canfd_buffer_frame_count(AIdxChn, ACount);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsfifo_read_canfd_rx_buffer_frame_count(const s32 AIdxChn, ps32 ACount)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsfifo_read_canfd_rx_buffer_frame_count(AIdxChn, ACount);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsfifo_read_canfd_tx_buffer_frame_count(const s32 AIdxChn, ps32 ACount)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsfifo_read_canfd_tx_buffer_frame_count(AIdxChn, ACount);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsfifo_read_fastlin_buffer_frame_count(const s32 AIdxChn, ps32 ACount)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsfifo_read_fastlin_buffer_frame_count(AIdxChn, ACount);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsfifo_read_fastlin_rx_buffer_frame_count(const s32 AIdxChn, ps32 ACount)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsfifo_read_fastlin_rx_buffer_frame_count(AIdxChn, ACount);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsfifo_read_fastlin_tx_buffer_frame_count(const s32 AIdxChn, ps32 ACount)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsfifo_read_fastlin_tx_buffer_frame_count(AIdxChn, ACount);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsfifo_read_lin_buffer_frame_count(const s32 AIdxChn, ps32 ACount)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsfifo_read_lin_buffer_frame_count(AIdxChn, ACount);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsfifo_read_lin_rx_buffer_frame_count(const s32 AIdxChn, ps32 ACount)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsfifo_read_lin_rx_buffer_frame_count(AIdxChn, ACount);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsfifo_read_lin_tx_buffer_frame_count(const s32 AIdxChn, ps32 ACount)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsfifo_read_lin_tx_buffer_frame_count(AIdxChn, ACount);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsfifo_receive_can_msgs(PLIBCAN ACANBuffers, ps32 ACANBufferSize, const s32 AIdxChn, const bool AIncludeTx)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsfifo_receive_can_msgs(ACANBuffers, ACANBufferSize, AIdxChn, AIncludeTx);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsfifo_receive_canfd_msgs(PLIBCANFD ACANFDBuffers, ps32 ACANFDBufferSize, const s32 AIdxChn, const bool AIncludeTx)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsfifo_receive_canfd_msgs(ACANFDBuffers, ACANFDBufferSize, AIdxChn, AIncludeTx);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsfifo_receive_fastlin_msgs(PLIBLIN ALINBuffers, ps32 ALINBufferSize, const s32 AIdxChn, const bool AIncludeTx)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsfifo_receive_fastlin_msgs(ALINBuffers, ALINBufferSize, AIdxChn, AIncludeTx);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsfifo_receive_lin_msgs(PLIBLIN ALINBuffers, ps32 ALINBufferSize, const s32 AIdxChn, const bool AIncludeTx)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsfifo_receive_lin_msgs(ALINBuffers, ALINBufferSize, AIdxChn, AIncludeTx);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsfifo_clear_can_receive_buffers(const s32 AIdxChn)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsfifo_clear_can_receive_buffers(AIdxChn);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsfifo_clear_canfd_receive_buffers(const s32 AIdxChn)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsfifo_clear_canfd_receive_buffers(AIdxChn);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsfifo_clear_fastlin_receive_buffers(const s32 AIdxChn)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsfifo_clear_fastlin_receive_buffers(AIdxChn);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsfifo_clear_lin_receive_buffers(const s32 AIdxChn)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsfifo_clear_lin_receive_buffers(AIdxChn);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_register_event_can(const ps32 AObj, const TCANEvent AEvent)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_register_event_can(AObj, AEvent);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_register_event_canfd(const ps32 AObj, const TCANFDEvent AEvent)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_register_event_canfd(AObj, AEvent);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_register_event_lin(const ps32 AObj, const TLINEvent AEvent)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_register_event_lin(AObj, AEvent);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_unregister_event_flexray(const ps32 AObj, const TFlexrayEvent AEvent)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_unregister_event_flexray(AObj, AEvent);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_unregister_event_ethernet(const ps32 AObj, const TEthernetEvent AEvent)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_unregister_event_ethernet(AObj, AEvent);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_unregister_events_flexray(const ps32 AObj)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_unregister_events_flexray(AObj);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_unregister_events_ethernet(const ps32 AObj)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_unregister_events_ethernet(AObj);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_unregister_pretx_event_flexray(const ps32 AObj, const TFlexrayEvent AEvent)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_unregister_pretx_event_flexray(AObj, AEvent);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_unregister_pretx_event_ethernet(const ps32 AObj, const TEthernetEvent AEvent)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_unregister_pretx_event_ethernet(AObj, AEvent);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_unregister_pretx_events_flexray(const ps32 AObj)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_unregister_pretx_events_flexray(AObj);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_unregister_pretx_events_ethernet(const ps32 AObj)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_unregister_pretx_events_ethernet(AObj);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_register_pretx_event_can(const ps32 AObj, const TCANEvent AEvent)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_register_pretx_event_can(AObj, AEvent);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_register_pretx_event_canfd(const ps32 AObj, const TCANFDEvent AEvent)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_register_pretx_event_canfd(AObj, AEvent);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_register_pretx_event_lin(const ps32 AObj, const TLINEvent AEvent)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_register_pretx_event_lin(AObj, AEvent);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_set_can_channel_count(const s32 ACount)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_set_can_channel_count(ACount);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_set_current_application(const char* AAppName)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_set_current_application(AAppName);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_set_lin_channel_count(const s32 ACount)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_set_lin_channel_count(ACount);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_set_logger(const TLogger ALogger)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_set_logger(ALogger);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_set_mapping(const PLIBTSMapping AMapping)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_set_mapping(AMapping);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_set_mapping_verbose(const char* AAppName,
	const TLIBApplicationChannelType AAppChannelType,
	const s32 AAppChannel,
	const char* AHardwareName,
	const TLIBBusToolDeviceType AHardwareType,
	const s32 AHardwareSubType,
	const s32 AHardwareIndex,
	const s32 AHardwareChannel,
	const bool AEnableMapping)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_set_mapping_verbose(AAppName, AAppChannelType, AAppChannel, AHardwareName, AHardwareType, AHardwareSubType, AHardwareIndex, AHardwareChannel, AEnableMapping);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_set_turbo_mode(const bool AEnable)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_set_turbo_mode(AEnable);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_set_vendor_detect_preferences(const bool AScanTOSUN,
	const bool AScanVector,
	const bool AScanPeak,
	const bool AScanKvaser,
	const bool AScanZLG,
	const bool AScanIntrepidcs)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_set_vendor_detect_preferences(AScanTOSUN, AScanVector, AScanPeak, AScanKvaser, AScanZLG, AScanIntrepidcs);
	}
	return IDX_ERR_DLL_NOT_READY;
}
// TSMasterApi::tsapp_show_channel_mapping_window
// TSMasterApi::tsapp_show_hardware_configuration_window
s32 TSMasterApi::tsapp_show_tsmaster_window(const char* AWindowName, const bool AWaitClose)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_show_tsmaster_window(AWindowName, AWaitClose);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_start_logging(const char* AFullFileName)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_start_logging(AFullFileName);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_stop_logging(void)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_stop_logging();
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_transmit_can_async(const PLIBCAN ACAN)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_transmit_can_async(ACAN);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_transmit_canfd_async(const PLIBCANFD ACANFD)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_transmit_canfd_async(ACANFD);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_transmit_lin_async(const PLIBLIN ALIN)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_transmit_lin_async(ALIN);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_transmit_flexray_async(const PLIBFlexRay AFlexray)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_transmit_flexray_async(AFlexray);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_transmit_ethernet_async(const PLIBEthernetHeader AEthernetHeader)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_transmit_ethernet_async(AEthernetHeader);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_transmit_header_and_receive_msg(s32 AChn, u8 AIdentifier, u8 ADLC, PLIBLIN ALINData, s32 ATimeoutMs)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_transmit_header_and_receive_msg(AChn, AIdentifier, ADLC, ALINData, ATimeoutMs);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_transmit_can_sync(const PLIBCAN ACAN, const s32 ATimeoutMS)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_transmit_can_sync(ACAN, ATimeoutMS);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_transmit_canfd_sync(const PLIBCANFD ACANFD, const s32 ATimeoutMS)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_transmit_canfd_sync(ACANFD, ATimeoutMS);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_transmit_lin_sync(const PLIBLIN ALIN, const s32 ATimeoutMS)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_transmit_lin_sync(ALIN, ATimeoutMS);
	}
	return IDX_ERR_DLL_NOT_READY;
}
// TSMasterApi::tsapp_transmit_fastlin_async
s32 TSMasterApi::tsapp_unregister_event_can(const ps32 AObj, const TCANEvent AEvent)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_unregister_event_can(AObj, AEvent);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_unregister_event_canfd(const ps32 AObj, const TCANFDEvent AEvent)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_unregister_event_canfd(AObj, AEvent);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_unregister_event_lin(const ps32 AObj, const TLINEvent AEvent)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_unregister_event_lin(AObj, AEvent);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_unregister_events_can(const ps32 AObj)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_unregister_events_can(AObj);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_unregister_events_lin(const ps32 AObj)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_unregister_events_lin(AObj);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_unregister_events_canfd(const ps32 AObj)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_unregister_events_canfd(AObj);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_unregister_events_all(const ps32 AObj)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_unregister_events_all(AObj);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_unregister_pretx_event_can(const ps32 AObj, const TCANEvent AEvent)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_unregister_pretx_event_can(AObj, AEvent);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_unregister_pretx_event_canfd(const ps32 AObj, const TCANFDEvent AEvent)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_unregister_pretx_event_canfd(AObj, AEvent);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_unregister_pretx_event_lin(const ps32 AObj, const TLINEvent AEvent)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_unregister_pretx_event_lin(AObj, AEvent);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_unregister_pretx_events_can(const ps32 AObj)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_unregister_pretx_events_can(AObj);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_unregister_pretx_events_lin(const ps32 AObj)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_unregister_pretx_events_lin(AObj);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_unregister_pretx_events_canfd(const ps32 AObj)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_unregister_pretx_events_canfd(AObj);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsapp_unregister_pretx_events_all(const ps32 AObj)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsapp_unregister_pretx_events_all(AObj);
	}
	return IDX_ERR_DLL_NOT_READY;
}
// TSMasterApi::tsapp_update_cyclic_msg_can
s32 TSMasterApi::tscom_can_rbs_start(void)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tscom_can_rbs_start();
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tscom_can_rbs_stop(void)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tscom_can_rbs_stop();
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tscom_can_rbs_is_running(bool* AIsRunning)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tscom_can_rbs_is_running(AIsRunning);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tscom_can_rbs_configure(const bool AAutoStart, const bool AAutoSendOnModification, const bool AActivateNodeSimulation, const TLIBRBSInitValueOptions AInitValueOptions)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tscom_can_rbs_configure(AAutoStart, AAutoSendOnModification, AActivateNodeSimulation, AInitValueOptions);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tscom_can_rbs_activate_all_networks(const bool AEnable, const bool AIncludingChildren)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tscom_can_rbs_activate_all_networks(AEnable, AIncludingChildren);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tscom_can_rbs_activate_network_by_name(const bool AEnable, const char* ANetworkName, const bool AIncludingChildren)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tscom_can_rbs_activate_network_by_name(AEnable, ANetworkName, AIncludingChildren);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tscom_can_rbs_activate_node_by_name(const bool AEnable, const char* ANetworkName, const char* ANodeName, const bool AIncludingChildren)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tscom_can_rbs_activate_node_by_name(AEnable, ANetworkName, ANodeName, AIncludingChildren);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tscom_can_rbs_activate_message_by_name(const bool AEnable, const char* ANetworkName, const char* ANodeName, const char* AMsgName)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tscom_can_rbs_activate_message_by_name(AEnable, ANetworkName, ANodeName, AMsgName);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tscom_can_rbs_get_signal_value_by_element(const s32 AIdxChn, const char* ANetworkName, const char* ANodeName, const char* AMsgName, const char* ASignalName, double* AValue)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tscom_can_rbs_get_signal_value_by_element(AIdxChn, ANetworkName, ANodeName, AMsgName, ASignalName, AValue);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tscom_can_rbs_get_signal_value_by_address(const char* ASymbolAddress, double* AValue)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tscom_can_rbs_get_signal_value_by_address(ASymbolAddress, AValue);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tscom_can_rbs_set_signal_value_by_element(const s32 AIdxChn, const char* ANetworkName, const char* ANodeName, const char* AMsgName, const char* ASignalName, const double AValue)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tscom_can_rbs_set_signal_value_by_element(AIdxChn, ANetworkName, ANodeName, AMsgName, ASignalName, AValue);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tscom_can_rbs_set_signal_value_by_address(const char* ASymbolAddress, const double AValue)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tscom_can_rbs_set_signal_value_by_address(ASymbolAddress, AValue);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsdb_get_signal_value_can(const PLIBCAN ACAN, const char* AMsgName, const char* ASgnName, double* AValue)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsdb_get_signal_value_can(ACAN, AMsgName, ASgnName, AValue);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsdb_get_signal_value_canfd(const PLIBCANFD ACANFD, const char* AMsgName, const char* ASgnName, double* AValue)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsdb_get_signal_value_canfd(ACANFD, AMsgName, ASgnName, AValue);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsdb_set_signal_value_can(const PLIBCAN ACAN, const char* AMsgName, const char* ASgnName, const double AValue)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsdb_set_signal_value_can(ACAN, AMsgName, ASgnName, AValue);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsdb_set_signal_value_canfd(const PLIBCANFD ACANFD, const char* AMsgName, const char* ASgnName, const double AValue)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsdb_set_signal_value_canfd(ACANFD, AMsgName, ASgnName, AValue);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsdb_load_can_db(const char* ADBC, const char* ASupportedChannelsBased0, u32* AId)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsdb_load_can_db(ADBC, ASupportedChannelsBased0, AId);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsdb_unload_can_db(const u32 AId)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsdb_unload_can_db(AId);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsdb_unload_can_dbs(void)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsdb_unload_can_dbs();
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsdb_get_can_db_count(s32* ACount)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsdb_get_can_db_count(ACount);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsdb_get_can_db_id(const s32 AIndex, u32* AId)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsdb_get_can_db_id(AIndex, AId);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsdb_get_can_db_info(const u32 ADatabaseId, const s32 AType, const s32 AIndex, const s32 ASubIndex, char** AValue)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsdb_get_can_db_info(ADatabaseId, AType, AIndex, ASubIndex, AValue);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tslog_add_online_replay_config(const char* AFileName, s32* AIndex)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tslog_add_online_replay_config(AFileName, AIndex);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tslog_set_online_replay_config(const s32 AIndex, const char* AName, const char* AFileName, const bool AAutoStart, const bool AIsRepetitiveMode, const TLIBOnlineReplayTimingMode AStartTimingMode, const s32 AStartDelayTimeMs, const bool ASendTx, const bool ASendRx, const char* AMappings)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tslog_set_online_replay_config(AIndex, AName, AFileName, AAutoStart, AIsRepetitiveMode, AStartTimingMode, AStartDelayTimeMs, ASendTx, ASendRx,  AMappings);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tslog_get_online_replay_count(s32* ACount)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tslog_get_online_replay_count(ACount);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tslog_get_online_replay_config(const s32 AIndex, char** AName, char** AFileName, bool* AAutoStart, bool* AIsRepetitiveMode, TLIBOnlineReplayTimingMode* AStartTimingMode, s32* AStartDelayTimeMs, bool* ASendTx, bool* ASendRx, char** AMappings)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tslog_get_online_replay_config(AIndex, AName, AFileName, AAutoStart, AIsRepetitiveMode, AStartTimingMode, AStartDelayTimeMs, ASendTx, ASendRx, AMappings);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tslog_del_online_replay_config(const s32 AIndex)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tslog_del_online_replay_config(AIndex);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tslog_del_online_replay_configs(void)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tslog_del_online_replay_configs();
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tslog_start_online_replay(const s32 AIndex)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tslog_start_online_replay(AIndex);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tslog_start_online_replays(void)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tslog_start_online_replays();
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tslog_pause_online_replay(const s32 AIndex)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tslog_pause_online_replay(AIndex);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tslog_pause_online_replays(void)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tslog_pause_online_replays();
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tslog_stop_online_replay(const s32 AIndex)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tslog_stop_online_replay(AIndex);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tslog_stop_online_replays(void)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tslog_stop_online_replays();
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tslog_get_online_replay_status(const s32 AIndex, TLIBOnlineReplayStatus* AStatus, float* AProgressPercent100)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tslog_get_online_replay_status(AIndex, AStatus, AProgressPercent100);
	}
	return IDX_ERR_DLL_NOT_READY;
}
//
s32 TSMasterApi::tslog_blf_write_start(const char* AFileName, int* AHandle) //stdcall
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tslog_blf_write_start(AFileName, AHandle);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tslog_blf_write_can(int AHandle, PLIBCAN ACAN)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tslog_blf_write_can(AHandle, ACAN);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tslog_blf_write_can_fd(int AHandle, PLIBCANFD ACANFD)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tslog_blf_write_can_fd(AHandle, ACANFD);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tslog_blf_write_lin(int AHandle, PLIBLIN ALIN)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tslog_blf_write_lin(AHandle, ALIN);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tslog_blf_write_realtime_comment(int AHandle, s64 ATimeUs, char* AComment)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tslog_blf_write_realtime_comment(AHandle, ATimeUs,  AComment);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tslog_blf_write_end(int AHandle)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tslog_blf_write_end(AHandle);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tslog_blf_read_start(const char* AFileName, int* AHandle, int* AObjCount)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tslog_blf_read_start(AFileName,  AHandle,  AObjCount);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tsLog_blf_read_start_verbose(const char* AFileName, int* AHandle, int* AObjCount,
	u16* AYear, u16* AMonth, u16* ADayOfWeek,
	u16* ADay, u16* AHour, u16* AMinute,
	u16* ASecond, u16* AMilliseconds)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tsLog_blf_read_start_verbose(AFileName,  AHandle,  AObjCount,
			 AYear,  AMonth,  ADayOfWeek,
			 ADay,  AHour,  AMinute,
			 ASecond,  AMilliseconds);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tslog_blf_read_status(int AHandle, int* AObjReadCount)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tslog_blf_read_status(AHandle, AObjReadCount);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tslog_blf_read_object(int AHandle, int* AProgressedCnt, int* AType/* PSupportedObjType*/, PLIBCAN ACAN,
	PLIBLIN ALIN, PLIBCANFD ACANFD)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tslog_blf_read_object(AHandle, AProgressedCnt, AType/* PSupportedObjType*/, ACAN,
			ALIN, ACANFD);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tslog_blf_read_object_w_comment(int AHandle, int* AProgressedCnt, int* AType/* PSupportedObjType*/,
	PLIBCAN ACAN, PLIBLIN ALIN, PLIBCANFD ACANFD, PRealtime_comment_t AComment)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tslog_blf_read_object_w_comment(AHandle, AProgressedCnt, AType/* PSupportedObjType*/,
			ACAN, ALIN, ACANFD, AComment);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tslog_blf_read_end(int AHandle)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tslog_blf_read_end(AHandle);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tslog_blf_seek_object_time(int AHandle, const double AProg100, s64* ATime, int* AProgressedCnt)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tslog_blf_seek_object_time(AHandle,  AProg100, ATime, AProgressedCnt);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tslin_enable_runtime_schedule_table(const s32 AChnIdx)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tslin_enable_runtime_schedule_table(AChnIdx);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tslin_set_schedule_table(const s32 AChnIdx, const s32 ASchIndex)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tslin_set_schedule_table(AChnIdx, ASchIndex);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tslin_stop_lin_channel(const s32 AChnIdx)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tslin_stop_lin_channel(AChnIdx);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tslin_start_lin_channel(const s32 AChnIdx)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tslin_start_lin_channel(AChnIdx);
	}
	return IDX_ERR_DLL_NOT_READY;
}
s32 TSMasterApi::tslin_set_node_funtiontype(const s32 AChnIdx, const TLINNodeType AFunctionType)
{
	if (priv_data_p != nullptr)
	{
		return priv_data_p->tslin_set_node_funtiontype(AChnIdx, AFunctionType);
	}
	return IDX_ERR_DLL_NOT_READY;
}