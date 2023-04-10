#ifndef _TSCANLIN_API_H_
#define _TSCANLIN_API_H_

#include "TSMasterDef.h"

class TSMasterApi
{
  private:
	  //variable
	  HMODULE hDll;
	  byte dllIsLoaded;
      Tinitialize_lib_tsmaster pInitLibTSMaster;
      Tfinalize_lib_tsmaster pFinalizeTSMaster;
	//Com 
      // CAN functions
      /*
      TTransmitCANAsync      transmit_can_async;
      TTransmitCANSync       transmit_can_sync;
      // CAN FD functions  
      TTransmitCANFDAsync    transmit_canfd_async;
      TTransmitCANFDSync     transmit_canfd_sync;
      // LIN functions     
      TTransmitLINAsync      transmit_lin_async;
      TTransmitLINSync       transmit_lin_sync;
      // Database functions
      TGetCANSignalValue     get_can_signal_value;
      TSetCANSignalValue     set_can_signal_value;
      // Bus statistics
      TEnableBusStatistics   enable_bus_statistics;
      TClearBusStatistics    clear_bus_statistics;
      TGetBusStatistics      get_bus_statistics;
      TGetFPSCAN             get_fps_can;
      TGetFPSCANFD           get_fps_canfd;
      TGetFPSLIN             get_fps_lin;
      // Bus functions
      TWaitCANMessage        internal_wait_can_message;
      TWaitCANFDMessage      internal_wait_canfd_message;
      TAddCyclicMsgCAN       add_cyclic_message_can;
      TAddCyclicMsgCANFD     add_cyclic_message_canfd;
      TDeleteCyclicMsgCAN    del_cyclic_message_can;
      TDeleteCyclicMsgCANFD  del_cyclic_message_canfd;
      TDeleteCyclicMsgs      del_cyclic_messages;
      // Bus callbacks
      TRegisterCANEvent      internal_register_event_can;
      TUnregisterCANEvent    internal_unregister_event_can;
      TRegisterCANFDEvent    internal_register_event_canfd;
      TUnregisterCANFDEvent  internal_unregister_event_canfd;
      TRegisterLINEvent      internal_register_event_lin;
      TUnregisterLINEvent    internal_unregister_event_lin;
      TUnregisterCANEvents   internal_unregister_events_can;
      TUnregisterLINEvents   internal_unregister_events_lin;
      TUnregisterCANFDEvents internal_unregister_events_canfd;
      TUnregisterALLEvents   internal_unregister_events_all;
      // online replay
      Ttslog_add_online_replay_config  tslog_add_online_replay_config;
      Ttslog_set_online_replay_config  tslog_set_online_replay_config;
      Ttslog_get_online_replay_count   tslog_get_online_replay_count;
      Ttslog_get_online_replay_config  tslog_get_online_replay_config;
      Ttslog_del_online_replay_config  tslog_del_online_replay_config;
      Ttslog_del_online_replay_configs tslog_del_online_replay_configs;
      Ttslog_start_online_replay       tslog_start_online_replay;
      Ttslog_start_online_replays      tslog_start_online_replays;
      Ttslog_pause_online_replay       tslog_pause_online_replay;
      Ttslog_pause_online_replays      tslog_pause_online_replays;
      Ttslog_stop_online_replay        tslog_stop_online_replay;
      Ttslog_stop_online_replays       tslog_stop_online_replays;
      Ttslog_get_online_replay_status  tslog_get_online_replay_status;
      // CAN rbs
      TCANRBSStart                     can_rbs_start;
      TCANRBSStop                      can_rbs_stop;
      TCANRBSIsRunning                 can_rbs_is_running;
      TCANRBSConfigure                 can_rbs_configure;
      TCANRBSActivateAllNetworks       can_rbs_activate_all_networks;
      TCANRBSActivateNetworkByName     can_rbs_activate_network_by_name;
      TCANRBSActivateNodeByName        can_rbs_activate_node_by_name;
      TCANRBSActivateMessageByName     can_rbs_activate_message_by_name;*/
      TCANRBSGetSignalValueByElement   tscom_can_rbs_get_signal_value_by_element;
      TCANRBSGetSignalValueByAddress   tscom_can_rbs_get_signal_value_by_address;
      TCANRBSSetSignalValueByElement   tscom_can_rbs_set_signal_value_by_element;
      TCANRBSSetSignalValueByAddress   tscom_can_rbs_set_signal_value_by_address;
	  byte LoadAPI();
	  void InitializePointers();
public:
	  TSMasterApi(const char* AAppName);
	  ~TSMasterApi();

      s32 CANRBSGetSignalValueByElement(const s32 AIdxChn, const char* ANetworkName, const char* ANodeName, const char* AMsgName, const char* ASignalName, double* AValue);
      s32 CANRBSGetSignalValueByAddress(const char* ASymbolAddress, double* AValue);
      s32 /*__stdcall*/ CANRBSSetSignalValueByElement(const s32 AIdxChn, const char* ANetworkName, const char* ANodeName, const char* AMsgName, const char* ASignalName, const double AValue);
      s32 /*__stdcall*/ CANRBSSetSignalValueByAddress(const char* ASymbolAddress, const double AValue);
};

#endif