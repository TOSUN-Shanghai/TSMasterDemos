from .TSDirver import *
from .TSStruct import * 
from .TSCallback import *
from .TSEnum import *
finalize_lib_tsmaster = dll.finalize_lib_tsmaster
finalize_lib_tsmaster.restype = None
finalize_lib_tsmaster.argtypes = []

tsfifo_enable_receive_fifo = dll.tsfifo_enable_receive_fifo
tsfifo_enable_receive_fifo.restype = None
tsfifo_enable_receive_fifo.argtypes = []

tsfifo_disable_receive_fifo = dll.tsfifo_disable_receive_fifo
tsfifo_disable_receive_fifo.restype = None
tsfifo_disable_receive_fifo.argtypes = []

tsfifo_enable_receive_error_frames = dll.tsfifo_enable_receive_error_frames
tsfifo_enable_receive_error_frames.restype = None
tsfifo_enable_receive_error_frames.argtypes = []

tsfifo_disable_receive_error_frames = dll.tsfifo_disable_receive_error_frames
tsfifo_disable_receive_error_frames.restype = None
tsfifo_disable_receive_error_frames.argtypes = []

tsdiag_can_delete_all = dll.tsdiag_can_delete_all
tsdiag_can_delete_all.restype = None
tsdiag_can_delete_all.argtypes = []

#arg[0] ANetworkIndex
rawsocket_dhcp_stop = dll.rawsocket_dhcp_stop
rawsocket_dhcp_stop.restype = None
rawsocket_dhcp_stop.argtypes = [s32]

#arg[0] ANetworkIndex
#arg[1] ping_addr
#arg[2] repeatcnt
#arg[3] interval_ms
#arg[4] timeout_ms
tssocket_ping4 = dll.tssocket_ping4
tssocket_ping4.restype = None
tssocket_ping4.argtypes = [s32,Pip4_addr_t,s32,u32,u32]

#arg[0] ANetworkIndex
#arg[1] ping_addr
#arg[2] repeatcnt
#arg[3] interval_ms
#arg[4] timeout_ms
tssocket_ping6 = dll.tssocket_ping6
tssocket_ping6.restype = None
tssocket_ping6.argtypes = [s32,Pip6_addr_t,s32,u32,u32]

#arg[0] AFilePath
set_libtsmaster_location = dll.set_libtsmaster_location
set_libtsmaster_location.restype = s32
set_libtsmaster_location.argtypes = [pchar]

#arg[0] AFilePath
get_libtsmaster_location = dll.get_libtsmaster_location
get_libtsmaster_location.restype = s32
get_libtsmaster_location.argtypes = [ppchar]

#arg[0] AAppName
initialize_lib_tsmaster = dll.initialize_lib_tsmaster
initialize_lib_tsmaster.restype = s32
initialize_lib_tsmaster.argtypes = [pchar]

#arg[0] AAppName
#arg[1] AProjectFileName
initialize_lib_tsmaster_with_project = dll.initialize_lib_tsmaster_with_project
initialize_lib_tsmaster_with_project.restype = s32
initialize_lib_tsmaster_with_project.argtypes = [pchar,pchar]

#arg[0] ALogger
tsapp_set_logger = dll.tsapp_set_logger
tsapp_set_logger.restype = s32
tsapp_set_logger.argtypes = [TLIBTSMasterLogger]

#arg[0] AStr
#arg[1] ALevel
tsapp_log = dll.tsapp_log
tsapp_log.restype = s32
tsapp_log.argtypes = [pchar,s32]

#arg[0] AAppName
tsapp_set_current_application = dll.tsapp_set_current_application
tsapp_set_current_application.restype = s32
tsapp_set_current_application.argtypes = [pchar]

#arg[0] AAppName
tsapp_get_current_application = dll.tsapp_get_current_application
tsapp_get_current_application.restype = s32
tsapp_get_current_application.argtypes = [ppchar]

#arg[0] AAppName
tsapp_del_application = dll.tsapp_del_application
tsapp_del_application.restype = s32
tsapp_del_application.argtypes = [pchar]

#arg[0] AAppName
tsapp_add_application = dll.tsapp_add_application
tsapp_add_application.restype = s32
tsapp_add_application.argtypes = [pchar]

#arg[0] AAppNameList
tsapp_get_application_list = dll.tsapp_get_application_list
tsapp_get_application_list.restype = s32
tsapp_get_application_list.argtypes = [ppchar]

#arg[0] ACount
tsapp_set_can_channel_count = dll.tsapp_set_can_channel_count
tsapp_set_can_channel_count.restype = s32
tsapp_set_can_channel_count.argtypes = [s32]

#arg[0] ACount
tsapp_set_lin_channel_count = dll.tsapp_set_lin_channel_count
tsapp_set_lin_channel_count.restype = s32
tsapp_set_lin_channel_count.argtypes = [s32]

#arg[0] ACount
tsapp_set_flexray_channel_count = dll.tsapp_set_flexray_channel_count
tsapp_set_flexray_channel_count.restype = s32
tsapp_set_flexray_channel_count.argtypes = [s32]

#arg[0] ACount
tsapp_get_can_channel_count = dll.tsapp_get_can_channel_count
tsapp_get_can_channel_count.restype = s32
tsapp_get_can_channel_count.argtypes = [POINTER(s32)]

#arg[0] ACount
tsapp_get_lin_channel_count = dll.tsapp_get_lin_channel_count
tsapp_get_lin_channel_count.restype = s32
tsapp_get_lin_channel_count.argtypes = [POINTER(s32)]

#arg[0] ACount
tsapp_get_flexray_channel_count = dll.tsapp_get_flexray_channel_count
tsapp_get_flexray_channel_count.restype = s32
tsapp_get_flexray_channel_count.argtypes = [POINTER(s32)]

#arg[0] AMapping
tsapp_set_mapping = dll.tsapp_set_mapping
tsapp_set_mapping.restype = s32
tsapp_set_mapping.argtypes = [PLIBTSMapping]

#arg[0] AAppName
#arg[1] AAppChannelType
#arg[2] AAppChannel
#arg[3] AHardwareName
#arg[4] AHardwareType
#arg[5] AHardwareSubType
#arg[6] AHardwareIndex
#arg[7] AHardwareChannel
#arg[8] AEnableMapping
tsapp_set_mapping_verbose = dll.tsapp_set_mapping_verbose
tsapp_set_mapping_verbose.restype = s32
tsapp_set_mapping_verbose.argtypes = [pchar,TLIBApplicationChannelType,s32,pchar,TLIBBusToolDeviceType,s32,s32,s32,cbool]

#arg[0] AMapping
tsapp_get_mapping = dll.tsapp_get_mapping
tsapp_get_mapping.restype = s32
tsapp_get_mapping.argtypes = [PLIBTSMapping]

#arg[0] AMapping
tsapp_del_mapping = dll.tsapp_del_mapping
tsapp_del_mapping.restype = s32
tsapp_del_mapping.argtypes = [PLIBTSMapping]

#arg[0] AAppName
#arg[1] AAppChannelType
#arg[2] AAppChannel
tsapp_del_mapping_verbose = dll.tsapp_del_mapping_verbose
tsapp_del_mapping_verbose.restype = s32
tsapp_del_mapping_verbose.argtypes = [pchar,TLIBApplicationChannelType,s32]

tsapp_connect = dll.tsapp_connect
tsapp_connect.restype = s32
tsapp_connect.argtypes = []

tsapp_disconnect = dll.tsapp_disconnect
tsapp_disconnect.restype = s32
tsapp_disconnect.argtypes = []

#arg[0] AEnable
tsapp_set_turbo_mode = dll.tsapp_set_turbo_mode
tsapp_set_turbo_mode.restype = s32
tsapp_set_turbo_mode.argtypes = [cbool]

#arg[0] AEnable
tsapp_get_turbo_mode = dll.tsapp_get_turbo_mode
tsapp_get_turbo_mode.restype = s32
tsapp_get_turbo_mode.argtypes = [POINTER(cbool)]

#arg[0] ACode
#arg[1] ADesc
tsapp_get_error_description = dll.tsapp_get_error_description
tsapp_get_error_description.restype = s32
tsapp_get_error_description.argtypes = [s32,ppchar]

tsapp_show_channel_mapping_window = dll.tsapp_show_channel_mapping_window
tsapp_show_channel_mapping_window.restype = s32
tsapp_show_channel_mapping_window.argtypes = []

tsapp_show_hardware_configuration_window = dll.tsapp_show_hardware_configuration_window
tsapp_show_hardware_configuration_window.restype = s32
tsapp_show_hardware_configuration_window.argtypes = []

#arg[0] AWindowName
#arg[1] AWaitClose
tsapp_show_tsmaster_window = dll.tsapp_show_tsmaster_window
tsapp_show_tsmaster_window.restype = s32
tsapp_show_tsmaster_window.argtypes = [pchar,cbool]

#arg[0] ATimeUs
tsapp_get_timestamp = dll.tsapp_get_timestamp
tsapp_get_timestamp.restype = s32
tsapp_get_timestamp.argtypes = [ps64]

#arg[0] AString
#arg[1] AArguments
#arg[2] ASync
#arg[3] AIsX64
#arg[4] AResultLog
tsapp_execute_python_string = dll.tsapp_execute_python_string
tsapp_execute_python_string.restype = s32
tsapp_execute_python_string.argtypes = [pchar,pchar,cbool,cbool,ppchar]

#arg[0] AFilePath
#arg[1] AArguments
#arg[2] ASync
#arg[3] AIsX64
#arg[4] AResultLog
tsapp_execute_python_script = dll.tsapp_execute_python_script
tsapp_execute_python_script.restype = s32
tsapp_execute_python_script.argtypes = [pchar,pchar,cbool,cbool,ppchar]

#arg[0] AYear
#arg[1] AMonth
#arg[2] ADay
#arg[3] ABuildNumber
tsapp_get_tsmaster_version = dll.tsapp_get_tsmaster_version
tsapp_get_tsmaster_version.restype = s32
tsapp_get_tsmaster_version.argtypes = [ps32,ps32,ps32,ps32]

#arg[0] AIdxType
#arg[1] ACount
tsapp_get_system_constant_count = dll.tsapp_get_system_constant_count
tsapp_get_system_constant_count.restype = s32
tsapp_get_system_constant_count.argtypes = [s32,ps32]

#arg[0] AIdxType
#arg[1] AIdxValue
#arg[2] AName
#arg[3] AValue
#arg[4] ADesc
tsapp_get_system_constant_value_by_index = dll.tsapp_get_system_constant_value_by_index
tsapp_get_system_constant_value_by_index.restype = s32
tsapp_get_system_constant_value_by_index.argtypes = [s32,s32,ppchar,pdouble,ppchar]

#arg[0] ACount
tsapp_enumerate_hw_devices = dll.tsapp_enumerate_hw_devices
tsapp_enumerate_hw_devices.restype = s32
tsapp_enumerate_hw_devices.argtypes = [POINTER(s32)]

#arg[0] AIndex
#arg[1] AHWInfo
tsapp_get_hw_info_by_index = dll.tsapp_get_hw_info_by_index
tsapp_get_hw_info_by_index.restype = s32
tsapp_get_hw_info_by_index.argtypes = [s32,PLIBHWInfo]

#arg[0] AIndex
#arg[1] ADeviceType
#arg[2] AVendorNameBuffer
#arg[3] AVendorNameBufferSize
#arg[4] ADeviceNameBuffer
#arg[5] ADeviceNameBufferSize
#arg[6] ASerialStringBuffer
#arg[7] ASerialStringBufferSize
tsapp_get_hw_info_by_index_verbose = dll.tsapp_get_hw_info_by_index_verbose
tsapp_get_hw_info_by_index_verbose.restype = s32
tsapp_get_hw_info_by_index_verbose.argtypes = [s32,PLIBBusToolDeviceType,pchar,s32,pchar,s32,pchar,s32]

#arg[0] AScanTOSUN
#arg[1] AScanVector
#arg[2] AScanPeak
#arg[3] AScanKvaser
#arg[4] AScanZLG
#arg[5] ADetectIntrepidcs
#arg[6] ADetectCANable
tsapp_set_vendor_detect_preferences = dll.tsapp_set_vendor_detect_preferences
tsapp_set_vendor_detect_preferences.restype = s32
tsapp_set_vendor_detect_preferences.argtypes = [cbool,cbool,cbool,cbool,cbool,cbool,cbool]

#arg[0] AScanTOSUN
#arg[1] AScanVector
#arg[2] AScanPeak
#arg[3] AScanKvaser
#arg[4] AScanZLG
#arg[5] ADetectIntrepidcs
#arg[6] ADetectCANable
tsapp_get_vendor_detect_preferences = dll.tsapp_get_vendor_detect_preferences
tsapp_get_vendor_detect_preferences.restype = s32
tsapp_get_vendor_detect_preferences.argtypes = [POINTER(cbool),POINTER(cbool),POINTER(cbool),POINTER(cbool),POINTER(cbool),POINTER(cbool),POINTER(cbool)]

#arg[0] AIdxChn
#arg[1] ABaudrateKbps
#arg[2] AProtocol
tsapp_configure_baudrate_lin = dll.tsapp_configure_baudrate_lin
tsapp_configure_baudrate_lin.restype = s32
tsapp_configure_baudrate_lin.argtypes = [s32,single,s32]

#arg[0] AIdxChn
#arg[1] ABaudrateKbps
#arg[2] AListenOnly
#arg[3] AInstallTermResistor120Ohm
tsapp_configure_baudrate_can = dll.tsapp_configure_baudrate_can
tsapp_configure_baudrate_can.restype = s32
tsapp_configure_baudrate_can.argtypes = [s32,single,cbool,cbool]

#arg[0] AIdxChn
#arg[1] AArbRateKbps
#arg[2] ADataRateKbps
#arg[3] AControllerType
#arg[4] AControllerMode
#arg[5] AInstallTermResistor120Ohm
tsapp_configure_baudrate_canfd = dll.tsapp_configure_baudrate_canfd
tsapp_configure_baudrate_canfd.restype = s32
tsapp_configure_baudrate_canfd.argtypes = [s32,single,single,TLIBCANFDControllerType,TLIBCANFDControllerMode,cbool]

#arg[0] AIdxChn
#arg[1] ABaudrateKbps
#arg[2] ASEG1
#arg[3] ASEG2
#arg[4] APrescaler
#arg[5] ASJW
#arg[6] AOnlyListen
#arg[7] A120OhmConnected
tsapp_configure_can_regs = dll.tsapp_configure_can_regs
tsapp_configure_can_regs.restype = s32
tsapp_configure_can_regs.argtypes = [s32,single,s32,s32,s32,s32,s32,s32]

#arg[0] AIdxChn
#arg[1] AArbBaudrate
#arg[2] AArbSEG1
#arg[3] AArbSEG2
#arg[4] AArbPrescaler
#arg[5] AArbSJW
#arg[6] ADataBaudrate
#arg[7] ADataSEG1
#arg[8] ADataSEG2
#arg[9] ADataPrescaler
#arg[10] ADataSJW
#arg[11] AControllerType
#arg[12] AControllerMode
#arg[13] A120OhmConnected
tsapp_configure_canfd_regs = dll.tsapp_configure_canfd_regs
tsapp_configure_canfd_regs.restype = s32
tsapp_configure_canfd_regs.argtypes = [s32,single,s32,s32,s32,s32,single,s32,s32,s32,s32,TLIBCANFDControllerType,TLIBCANFDControllerMode,s32]

#arg[0] ACAN
tsapp_transmit_can_async = dll.tsapp_transmit_can_async
tsapp_transmit_can_async.restype = s32
tsapp_transmit_can_async.argtypes = [PLIBCAN]

#arg[0] ACANFD
tsapp_transmit_canfd_async = dll.tsapp_transmit_canfd_async
tsapp_transmit_canfd_async.restype = s32
tsapp_transmit_canfd_async.argtypes = [PLIBCANFD]

#arg[0] ALIN
tsapp_transmit_lin_async = dll.tsapp_transmit_lin_async
tsapp_transmit_lin_async.restype = s32
tsapp_transmit_lin_async.argtypes = [PLIBLIN]

#arg[0] ALIN
tsapp_transmit_fastlin_async = dll.tsapp_transmit_fastlin_async
tsapp_transmit_fastlin_async.restype = s32
tsapp_transmit_fastlin_async.argtypes = [PLIBLIN]

#arg[0] AIdxChn
#arg[1] AWakeupLength
#arg[2] AWakeupIntervalTime
#arg[3] AWakeupTimes
tsapp_transmit_lin_wakeup_async = dll.tsapp_transmit_lin_wakeup_async
tsapp_transmit_lin_wakeup_async.restype = s32
tsapp_transmit_lin_wakeup_async.argtypes = [s32,s32,s32,s32]

#arg[0] AIdxChn
tsapp_transmit_lin_gotosleep_async = dll.tsapp_transmit_lin_gotosleep_async
tsapp_transmit_lin_gotosleep_async.restype = s32
tsapp_transmit_lin_gotosleep_async.argtypes = [s32]

#arg[0] ACAN
#arg[1] ATimeoutMS
tsapp_transmit_can_sync = dll.tsapp_transmit_can_sync
tsapp_transmit_can_sync.restype = s32
tsapp_transmit_can_sync.argtypes = [PLIBCAN,s32]

#arg[0] ACANfd
#arg[1] ATimeoutMS
tsapp_transmit_canfd_sync = dll.tsapp_transmit_canfd_sync
tsapp_transmit_canfd_sync.restype = s32
tsapp_transmit_canfd_sync.argtypes = [PLIBCANFD,s32]

#arg[0] ALIN
#arg[1] ATimeoutMS
tsapp_transmit_lin_sync = dll.tsapp_transmit_lin_sync
tsapp_transmit_lin_sync.restype = s32
tsapp_transmit_lin_sync.argtypes = [PLIBLIN,s32]

#arg[0] AIdxChn
#arg[1] AIdentifier
#arg[2] AIsStd
tsfifo_add_can_canfd_pass_filter = dll.tsfifo_add_can_canfd_pass_filter
tsfifo_add_can_canfd_pass_filter.restype = s32
tsfifo_add_can_canfd_pass_filter.argtypes = [s32,s32,cbool]

#arg[0] AIdxChn
#arg[1] AIdentifier
tsfifo_add_lin_pass_filter = dll.tsfifo_add_lin_pass_filter
tsfifo_add_lin_pass_filter.restype = s32
tsfifo_add_lin_pass_filter.argtypes = [s32,s32]

#arg[0] AIdxChn
#arg[1] AIdentifier
tsfifo_delete_can_canfd_pass_filter = dll.tsfifo_delete_can_canfd_pass_filter
tsfifo_delete_can_canfd_pass_filter.restype = s32
tsfifo_delete_can_canfd_pass_filter.argtypes = [s32,s32]

#arg[0] AIdxChn
#arg[1] AIdentifier
tsfifo_delete_lin_pass_filter = dll.tsfifo_delete_lin_pass_filter
tsfifo_delete_lin_pass_filter.restype = s32
tsfifo_delete_lin_pass_filter.argtypes = [s32,s32]

#arg[0] ACANBuffers
#arg[1] ACANBufferSize
#arg[2] AIdxChn
#arg[3] AIncludeTx
tsfifo_receive_can_msgs = dll.tsfifo_receive_can_msgs
tsfifo_receive_can_msgs.restype = s32
tsfifo_receive_can_msgs.argtypes = [PLIBCAN,ps32,s32,cbool]

#arg[0] ACANFDBuffers
#arg[1] ACANFDBufferSize
#arg[2] AIdxChn
#arg[3] AIncludeTx
tsfifo_receive_canfd_msgs = dll.tsfifo_receive_canfd_msgs
tsfifo_receive_canfd_msgs.restype = s32
tsfifo_receive_canfd_msgs.argtypes = [PLIBCANFD,ps32,s32,cbool]

#arg[0] ALINBuffers
#arg[1] ALINBufferSize
#arg[2] AIdxChn
#arg[3] AIncludeTx
tsfifo_receive_lin_msgs = dll.tsfifo_receive_lin_msgs
tsfifo_receive_lin_msgs.restype = s32
tsfifo_receive_lin_msgs.argtypes = [PLIBLIN,ps32,s32,cbool]

#arg[0] AFastLINBuffers
#arg[1] AFastLINBufferSize
#arg[2] AIdxChn
#arg[3] AIncludeTx
tsfifo_receive_fastlin_msgs = dll.tsfifo_receive_fastlin_msgs
tsfifo_receive_fastlin_msgs.restype = s32
tsfifo_receive_fastlin_msgs.argtypes = [PLIBLIN,ps32,s32,cbool]

#arg[0] AIdxChn
tsfifo_clear_can_receive_buffers = dll.tsfifo_clear_can_receive_buffers
tsfifo_clear_can_receive_buffers.restype = s32
tsfifo_clear_can_receive_buffers.argtypes = [s32]

#arg[0] AIdxChn
tsfifo_clear_canfd_receive_buffers = dll.tsfifo_clear_canfd_receive_buffers
tsfifo_clear_canfd_receive_buffers.restype = s32
tsfifo_clear_canfd_receive_buffers.argtypes = [s32]

#arg[0] AIdxChn
tsfifo_clear_lin_receive_buffers = dll.tsfifo_clear_lin_receive_buffers
tsfifo_clear_lin_receive_buffers.restype = s32
tsfifo_clear_lin_receive_buffers.argtypes = [s32]

#arg[0] AIdxChn
tsfifo_clear_fastlin_receive_buffers = dll.tsfifo_clear_fastlin_receive_buffers
tsfifo_clear_fastlin_receive_buffers.restype = s32
tsfifo_clear_fastlin_receive_buffers.argtypes = [s32]

#arg[0] AIdxChn
#arg[1] ACount
tsfifo_read_can_buffer_frame_count = dll.tsfifo_read_can_buffer_frame_count
tsfifo_read_can_buffer_frame_count.restype = s32
tsfifo_read_can_buffer_frame_count.argtypes = [s32,POINTER(s32)]

#arg[0] AIdxChn
#arg[1] ACount
tsfifo_read_can_tx_buffer_frame_count = dll.tsfifo_read_can_tx_buffer_frame_count
tsfifo_read_can_tx_buffer_frame_count.restype = s32
tsfifo_read_can_tx_buffer_frame_count.argtypes = [s32,POINTER(s32)]

#arg[0] AIdxChn
#arg[1] ACount
tsfifo_read_can_rx_buffer_frame_count = dll.tsfifo_read_can_rx_buffer_frame_count
tsfifo_read_can_rx_buffer_frame_count.restype = s32
tsfifo_read_can_rx_buffer_frame_count.argtypes = [s32,POINTER(s32)]

#arg[0] AIdxChn
#arg[1] ACount
tsfifo_read_canfd_buffer_frame_count = dll.tsfifo_read_canfd_buffer_frame_count
tsfifo_read_canfd_buffer_frame_count.restype = s32
tsfifo_read_canfd_buffer_frame_count.argtypes = [s32,POINTER(s32)]

#arg[0] AIdxChn
#arg[1] ACount
tsfifo_read_canfd_tx_buffer_frame_count = dll.tsfifo_read_canfd_tx_buffer_frame_count
tsfifo_read_canfd_tx_buffer_frame_count.restype = s32
tsfifo_read_canfd_tx_buffer_frame_count.argtypes = [s32,POINTER(s32)]

#arg[0] AIdxChn
#arg[1] ACount
tsfifo_read_canfd_rx_buffer_frame_count = dll.tsfifo_read_canfd_rx_buffer_frame_count
tsfifo_read_canfd_rx_buffer_frame_count.restype = s32
tsfifo_read_canfd_rx_buffer_frame_count.argtypes = [s32,POINTER(s32)]

#arg[0] AIdxChn
#arg[1] ACount
tsfifo_read_lin_buffer_frame_count = dll.tsfifo_read_lin_buffer_frame_count
tsfifo_read_lin_buffer_frame_count.restype = s32
tsfifo_read_lin_buffer_frame_count.argtypes = [s32,POINTER(s32)]

#arg[0] AIdxChn
#arg[1] ACount
tsfifo_read_lin_tx_buffer_frame_count = dll.tsfifo_read_lin_tx_buffer_frame_count
tsfifo_read_lin_tx_buffer_frame_count.restype = s32
tsfifo_read_lin_tx_buffer_frame_count.argtypes = [s32,POINTER(s32)]

#arg[0] AIdxChn
#arg[1] ACount
tsfifo_read_lin_rx_buffer_frame_count = dll.tsfifo_read_lin_rx_buffer_frame_count
tsfifo_read_lin_rx_buffer_frame_count.restype = s32
tsfifo_read_lin_rx_buffer_frame_count.argtypes = [s32,POINTER(s32)]

#arg[0] AIdxChn
#arg[1] ACount
tsfifo_read_fastlin_buffer_frame_count = dll.tsfifo_read_fastlin_buffer_frame_count
tsfifo_read_fastlin_buffer_frame_count.restype = s32
tsfifo_read_fastlin_buffer_frame_count.argtypes = [s32,POINTER(s32)]

#arg[0] AIdxChn
#arg[1] ACount
tsfifo_read_fastlin_tx_buffer_frame_count = dll.tsfifo_read_fastlin_tx_buffer_frame_count
tsfifo_read_fastlin_tx_buffer_frame_count.restype = s32
tsfifo_read_fastlin_tx_buffer_frame_count.argtypes = [s32,POINTER(s32)]

#arg[0] AIdxChn
#arg[1] ACount
tsfifo_read_fastlin_rx_buffer_frame_count = dll.tsfifo_read_fastlin_rx_buffer_frame_count
tsfifo_read_fastlin_rx_buffer_frame_count.restype = s32
tsfifo_read_fastlin_rx_buffer_frame_count.argtypes = [s32,POINTER(s32)]

#arg[0] ADataBuffers
#arg[1] ADataBufferSize
#arg[2] AIdxChn
#arg[3] AIncludeTx
tsfifo_receive_flexray_msgs = dll.tsfifo_receive_flexray_msgs
tsfifo_receive_flexray_msgs.restype = s32
tsfifo_receive_flexray_msgs.argtypes = [PLIBFlexRay,ps32,s32,cbool]

#arg[0] AIdxChn
tsfifo_clear_flexray_receive_buffers = dll.tsfifo_clear_flexray_receive_buffers
tsfifo_clear_flexray_receive_buffers.restype = s32
tsfifo_clear_flexray_receive_buffers.argtypes = [s32]

#arg[0] AIdxChn
#arg[1] ACount
tsfifo_read_flexray_buffer_frame_count = dll.tsfifo_read_flexray_buffer_frame_count
tsfifo_read_flexray_buffer_frame_count.restype = s32
tsfifo_read_flexray_buffer_frame_count.argtypes = [s32,POINTER(s32)]

#arg[0] AIdxChn
#arg[1] ACount
tsfifo_read_flexray_tx_buffer_frame_count = dll.tsfifo_read_flexray_tx_buffer_frame_count
tsfifo_read_flexray_tx_buffer_frame_count.restype = s32
tsfifo_read_flexray_tx_buffer_frame_count.argtypes = [s32,POINTER(s32)]

#arg[0] AIdxChn
#arg[1] ACount
tsfifo_read_flexray_rx_buffer_frame_count = dll.tsfifo_read_flexray_rx_buffer_frame_count
tsfifo_read_flexray_rx_buffer_frame_count.restype = s32
tsfifo_read_flexray_rx_buffer_frame_count.argtypes = [s32,POINTER(s32)]

#arg[0] ACAN
#arg[1] APeriodMS
tsapp_add_cyclic_msg_can = dll.tsapp_add_cyclic_msg_can
tsapp_add_cyclic_msg_can.restype = s32
tsapp_add_cyclic_msg_can.argtypes = [PLIBCAN,single]

#arg[0] ACAN
tsapp_update_cyclic_msg_can = dll.tsapp_update_cyclic_msg_can
tsapp_update_cyclic_msg_can.restype = s32
tsapp_update_cyclic_msg_can.argtypes = [PLIBCAN]

#arg[0] ACANFD
#arg[1] APeriodMS
tsapp_add_cyclic_msg_canfd = dll.tsapp_add_cyclic_msg_canfd
tsapp_add_cyclic_msg_canfd.restype = s32
tsapp_add_cyclic_msg_canfd.argtypes = [PLIBCANFD,single]

#arg[0] ACAN
tsapp_delete_cyclic_msg_can = dll.tsapp_delete_cyclic_msg_can
tsapp_delete_cyclic_msg_can.restype = s32
tsapp_delete_cyclic_msg_can.argtypes = [PLIBCAN]

#arg[0] ACANFD
tsapp_delete_cyclic_msg_canfd = dll.tsapp_delete_cyclic_msg_canfd
tsapp_delete_cyclic_msg_canfd.restype = s32
tsapp_delete_cyclic_msg_canfd.argtypes = [PLIBCANFD]

tsapp_delete_cyclic_msgs = dll.tsapp_delete_cyclic_msgs
tsapp_delete_cyclic_msgs.restype = s32
tsapp_delete_cyclic_msgs.argtypes = []

#arg[0] AEnable
tsapp_enable_bus_statistics = dll.tsapp_enable_bus_statistics
tsapp_enable_bus_statistics.restype = s32
tsapp_enable_bus_statistics.argtypes = [cbool]

tsapp_clear_bus_statistics = dll.tsapp_clear_bus_statistics
tsapp_clear_bus_statistics.restype = s32
tsapp_clear_bus_statistics.argtypes = []

#arg[0] ABusType
#arg[1] AIdxChn
#arg[2] AIdxStat
#arg[3] AStat
tsapp_get_bus_statistics = dll.tsapp_get_bus_statistics
tsapp_get_bus_statistics.restype = s32
tsapp_get_bus_statistics.argtypes = [TLIBApplicationChannelType,s32,TLIBCANBusStatistics,POINTER(double)]

#arg[0] AIdxChn
#arg[1] AIdentifier
#arg[2] AFPS
tsapp_get_fps_can = dll.tsapp_get_fps_can
tsapp_get_fps_can.restype = s32
tsapp_get_fps_can.argtypes = [s32,s32,POINTER(s32)]

#arg[0] AIdxChn
#arg[1] AIdentifier
#arg[2] AFPS
tsapp_get_fps_canfd = dll.tsapp_get_fps_canfd
tsapp_get_fps_canfd.restype = s32
tsapp_get_fps_canfd.argtypes = [s32,s32,POINTER(s32)]

#arg[0] AIdxChn
#arg[1] AIdentifier
#arg[2] AFPS
tsapp_get_fps_lin = dll.tsapp_get_fps_lin
tsapp_get_fps_lin.restype = s32
tsapp_get_fps_lin.argtypes = [s32,s32,POINTER(s32)]

#arg[0] AObj
#arg[1] AEvent
tsapp_register_event_can = dll.tsapp_register_event_can
tsapp_register_event_can.restype = s32
tsapp_register_event_can.argtypes = [ps32,TCANQueueEvent_Win32]

#arg[0] AObj
#arg[1] AEvent
tsapp_unregister_event_can = dll.tsapp_unregister_event_can
tsapp_unregister_event_can.restype = s32
tsapp_unregister_event_can.argtypes = [ps32,TCANQueueEvent_Win32]

#arg[0] AObj
#arg[1] AEvent
tsapp_register_event_canfd = dll.tsapp_register_event_canfd
tsapp_register_event_canfd.restype = s32
tsapp_register_event_canfd.argtypes = [ps32,TCANFDQueueEvent_Win32]

#arg[0] AObj
#arg[1] AEvent
tsapp_unregister_event_canfd = dll.tsapp_unregister_event_canfd
tsapp_unregister_event_canfd.restype = s32
tsapp_unregister_event_canfd.argtypes = [ps32,TCANFDQueueEvent_Win32]

#arg[0] AObj
#arg[1] AEvent
tsapp_register_event_lin = dll.tsapp_register_event_lin
tsapp_register_event_lin.restype = s32
tsapp_register_event_lin.argtypes = [ps32,TLINQueueEvent_Win32]

#arg[0] AObj
#arg[1] AEvent
tsapp_unregister_event_lin = dll.tsapp_unregister_event_lin
tsapp_unregister_event_lin.restype = s32
tsapp_unregister_event_lin.argtypes = [ps32,TLINQueueEvent_Win32]

#arg[0] AObj
#arg[1] AEvent
tsapp_register_event_flexray = dll.tsapp_register_event_flexray
tsapp_register_event_flexray.restype = s32
tsapp_register_event_flexray.argtypes = [ps32,TFlexRayQueueEvent_Win32]

#arg[0] AObj
#arg[1] AEvent
tsapp_unregister_event_flexray = dll.tsapp_unregister_event_flexray
tsapp_unregister_event_flexray.restype = s32
tsapp_unregister_event_flexray.argtypes = [ps32,TFlexRayQueueEvent_Win32]

#arg[0] AObj
tsapp_unregister_events_flexray = dll.tsapp_unregister_events_flexray
tsapp_unregister_events_flexray.restype = s32
tsapp_unregister_events_flexray.argtypes = [ps32]

#arg[0] AObj
tsapp_unregister_events_can = dll.tsapp_unregister_events_can
tsapp_unregister_events_can.restype = s32
tsapp_unregister_events_can.argtypes = [ps32]

#arg[0] AObj
tsapp_unregister_events_lin = dll.tsapp_unregister_events_lin
tsapp_unregister_events_lin.restype = s32
tsapp_unregister_events_lin.argtypes = [ps32]

#arg[0] AObj
tsapp_unregister_events_canfd = dll.tsapp_unregister_events_canfd
tsapp_unregister_events_canfd.restype = s32
tsapp_unregister_events_canfd.argtypes = [ps32]

#arg[0] AObj
tsapp_unregister_events_all = dll.tsapp_unregister_events_all
tsapp_unregister_events_all.restype = s32
tsapp_unregister_events_all.argtypes = [ps32]

#arg[0] AObj
#arg[1] AEvent
tsapp_register_pretx_event_can = dll.tsapp_register_pretx_event_can
tsapp_register_pretx_event_can.restype = s32
tsapp_register_pretx_event_can.argtypes = [ps32,TCANQueueEvent_Win32]

#arg[0] AObj
#arg[1] AEvent
tsapp_unregister_pretx_event_can = dll.tsapp_unregister_pretx_event_can
tsapp_unregister_pretx_event_can.restype = s32
tsapp_unregister_pretx_event_can.argtypes = [ps32,TCANQueueEvent_Win32]

#arg[0] AObj
#arg[1] AEvent
tsapp_register_pretx_event_canfd = dll.tsapp_register_pretx_event_canfd
tsapp_register_pretx_event_canfd.restype = s32
tsapp_register_pretx_event_canfd.argtypes = [ps32,TCANFDQueueEvent_Win32]

#arg[0] AObj
#arg[1] AEvent
tsapp_unregister_pretx_event_canfd = dll.tsapp_unregister_pretx_event_canfd
tsapp_unregister_pretx_event_canfd.restype = s32
tsapp_unregister_pretx_event_canfd.argtypes = [ps32,TCANFDQueueEvent_Win32]

#arg[0] AObj
#arg[1] AEvent
tsapp_register_pretx_event_lin = dll.tsapp_register_pretx_event_lin
tsapp_register_pretx_event_lin.restype = s32
tsapp_register_pretx_event_lin.argtypes = [ps32,TLINQueueEvent_Win32]

#arg[0] AObj
#arg[1] AEvent
tsapp_unregister_pretx_event_lin = dll.tsapp_unregister_pretx_event_lin
tsapp_unregister_pretx_event_lin.restype = s32
tsapp_unregister_pretx_event_lin.argtypes = [ps32,TLINQueueEvent_Win32]

#arg[0] AObj
#arg[1] AEvent
tsapp_register_pretx_event_flexray = dll.tsapp_register_pretx_event_flexray
tsapp_register_pretx_event_flexray.restype = s32
tsapp_register_pretx_event_flexray.argtypes = [ps32,TFlexRayQueueEvent_Win32]

#arg[0] AObj
#arg[1] AEvent
tsapp_unregister_pretx_event_flexray = dll.tsapp_unregister_pretx_event_flexray
tsapp_unregister_pretx_event_flexray.restype = s32
tsapp_unregister_pretx_event_flexray.argtypes = [ps32,TFlexRayQueueEvent_Win32]

#arg[0] AObj
tsapp_unregister_pretx_events_flexray = dll.tsapp_unregister_pretx_events_flexray
tsapp_unregister_pretx_events_flexray.restype = s32
tsapp_unregister_pretx_events_flexray.argtypes = [ps32]

#arg[0] AObj
tsapp_unregister_pretx_events_can = dll.tsapp_unregister_pretx_events_can
tsapp_unregister_pretx_events_can.restype = s32
tsapp_unregister_pretx_events_can.argtypes = [ps32]

#arg[0] AObj
tsapp_unregister_pretx_events_lin = dll.tsapp_unregister_pretx_events_lin
tsapp_unregister_pretx_events_lin.restype = s32
tsapp_unregister_pretx_events_lin.argtypes = [ps32]

#arg[0] AObj
tsapp_unregister_pretx_events_canfd = dll.tsapp_unregister_pretx_events_canfd
tsapp_unregister_pretx_events_canfd.restype = s32
tsapp_unregister_pretx_events_canfd.argtypes = [ps32]

#arg[0] AObj
tsapp_unregister_pretx_events_all = dll.tsapp_unregister_pretx_events_all
tsapp_unregister_pretx_events_all.restype = s32
tsapp_unregister_pretx_events_all.argtypes = [ps32]

#arg[0] AFileName
tsapp_start_logging = dll.tsapp_start_logging
tsapp_start_logging.restype = s32
tsapp_start_logging.argtypes = [pchar]

tsapp_stop_logging = dll.tsapp_stop_logging
tsapp_stop_logging.restype = s32
tsapp_stop_logging.argtypes = []

#arg[0] AFileName
#arg[1] AObj
tsapp_excel_load = dll.tsapp_excel_load
tsapp_excel_load.restype = s32
tsapp_excel_load.argtypes = [pchar,pps32]

#arg[0] AObj
#arg[1] ACount
tsapp_excel_get_sheet_count = dll.tsapp_excel_get_sheet_count
tsapp_excel_get_sheet_count.restype = s32
tsapp_excel_get_sheet_count.argtypes = [ps32,POINTER(s32)]

#arg[0] AObj
#arg[1] ACount
tsapp_excel_set_sheet_count = dll.tsapp_excel_set_sheet_count
tsapp_excel_set_sheet_count.restype = s32
tsapp_excel_set_sheet_count.argtypes = [ps32,s32]

#arg[0] AObj
#arg[1] AIdxSheet
#arg[2] AName
tsapp_excel_get_sheet_name = dll.tsapp_excel_get_sheet_name
tsapp_excel_get_sheet_name.restype = s32
tsapp_excel_get_sheet_name.argtypes = [ps32,s32,ppchar]

#arg[0] AObj
#arg[1] AIdxSheet
#arg[2] AName
tsapp_excel_set_sheet_name = dll.tsapp_excel_set_sheet_name
tsapp_excel_set_sheet_name.restype = s32
tsapp_excel_set_sheet_name.argtypes = [ps32,s32,pchar]

#arg[0] AObj
#arg[1] AIdxSheet
#arg[2] ARowCount
#arg[3] AColCount
tsapp_excel_get_cell_count = dll.tsapp_excel_get_cell_count
tsapp_excel_get_cell_count.restype = s32
tsapp_excel_get_cell_count.argtypes = [ps32,s32,POINTER(s32),POINTER(s32)]

#arg[0] AObj
#arg[1] AIdxSheet
#arg[2] AIdxRow
#arg[3] AIdxCol
#arg[4] AValue
tsapp_excel_get_cell_value = dll.tsapp_excel_get_cell_value
tsapp_excel_get_cell_value.restype = s32
tsapp_excel_get_cell_value.argtypes = [ps32,s32,s32,s32,ppchar]

#arg[0] AObj
#arg[1] AIdxSheet
#arg[2] ARowCount
#arg[3] AColCount
tsapp_excel_set_cell_count = dll.tsapp_excel_set_cell_count
tsapp_excel_set_cell_count.restype = s32
tsapp_excel_set_cell_count.argtypes = [ps32,s32,s32,s32]

#arg[0] AObj
#arg[1] AIdxSheet
#arg[2] AIdxRow
#arg[3] AIdxCol
#arg[4] AValue
tsapp_excel_set_cell_value = dll.tsapp_excel_set_cell_value
tsapp_excel_set_cell_value.restype = s32
tsapp_excel_set_cell_value.argtypes = [ps32,s32,s32,s32,pchar]

#arg[0] AObj
tsapp_excel_unload = dll.tsapp_excel_unload
tsapp_excel_unload.restype = s32
tsapp_excel_unload.argtypes = [ps32]

tsapp_system_vars_reload_settings = dll.tsapp_system_vars_reload_settings
tsapp_system_vars_reload_settings.restype = s32
tsapp_system_vars_reload_settings.argtypes = []

#arg[0] AinternalCount
#arg[1] AUserCount
tsapp_get_system_var_count = dll.tsapp_get_system_var_count
tsapp_get_system_var_count.restype = s32
tsapp_get_system_var_count.argtypes = [ps32,ps32]

#arg[0] AIsUser
#arg[1] AIndex
#arg[2] AVarDef
tsapp_get_system_var_def_by_index = dll.tsapp_get_system_var_def_by_index
tsapp_get_system_var_def_by_index.restype = s32
tsapp_get_system_var_def_by_index.argtypes = [cbool,s32,PLIBSystemVarDef]

#arg[0] AIsUser
#arg[1] ACompleteName
#arg[2] AVarDef
tsapp_find_system_var_def_by_name = dll.tsapp_find_system_var_def_by_name
tsapp_find_system_var_def_by_name.restype = s32
tsapp_find_system_var_def_by_name.argtypes = [cbool,pchar,PLIBSystemVarDef]

#arg[0] ACompleteName
#arg[1] AValue
tsapp_get_system_var_double = dll.tsapp_get_system_var_double
tsapp_get_system_var_double.restype = s32
tsapp_get_system_var_double.argtypes = [pchar,pdouble]

#arg[0] ACompleteName
#arg[1] AValue
tsapp_get_system_var_int32 = dll.tsapp_get_system_var_int32
tsapp_get_system_var_int32.restype = s32
tsapp_get_system_var_int32.argtypes = [pchar,ps32]

#arg[0] ACompleteName
#arg[1] AValue
tsapp_get_system_var_uint32 = dll.tsapp_get_system_var_uint32
tsapp_get_system_var_uint32.restype = s32
tsapp_get_system_var_uint32.argtypes = [pchar,pu32]

#arg[0] ACompleteName
#arg[1] AValue
tsapp_get_system_var_int64 = dll.tsapp_get_system_var_int64
tsapp_get_system_var_int64.restype = s32
tsapp_get_system_var_int64.argtypes = [pchar,ps64]

#arg[0] ACompleteName
#arg[1] AValue
tsapp_get_system_var_uint64 = dll.tsapp_get_system_var_uint64
tsapp_get_system_var_uint64.restype = s32
tsapp_get_system_var_uint64.argtypes = [pchar,pu64]

#arg[0] ACompleteName
#arg[1] ACapacity
#arg[2] AVarCount
#arg[3] AValue
tsapp_get_system_var_uint8_array = dll.tsapp_get_system_var_uint8_array
tsapp_get_system_var_uint8_array.restype = s32
tsapp_get_system_var_uint8_array.argtypes = [pchar,s32,ps32,pu8]

#arg[0] ACompleteName
#arg[1] ACapacity
#arg[2] AVarCount
#arg[3] AValue
tsapp_get_system_var_int32_array = dll.tsapp_get_system_var_int32_array
tsapp_get_system_var_int32_array.restype = s32
tsapp_get_system_var_int32_array.argtypes = [pchar,s32,ps32,ps32]

#arg[0] ACompleteName
#arg[1] ACapacity
#arg[2] AVarCount
#arg[3] AValue
tsapp_get_system_var_int64_array = dll.tsapp_get_system_var_int64_array
tsapp_get_system_var_int64_array.restype = s32
tsapp_get_system_var_int64_array.argtypes = [pchar,s32,ps32,ps64]

#arg[0] ACompleteName
#arg[1] ACapacity
#arg[2] AVarCount
#arg[3] AValue
tsapp_get_system_var_double_array = dll.tsapp_get_system_var_double_array
tsapp_get_system_var_double_array.restype = s32
tsapp_get_system_var_double_array.argtypes = [pchar,s32,ps32,pdouble]

#arg[0] ACompleteName
#arg[1] ACapacity
#arg[2] AValue
tsapp_get_system_var_string = dll.tsapp_get_system_var_string
tsapp_get_system_var_string.restype = s32
tsapp_get_system_var_string.argtypes = [pchar,s32,pchar]

#arg[0] ACompleteName
#arg[1] AValue
tsapp_set_system_var_double = dll.tsapp_set_system_var_double
tsapp_set_system_var_double.restype = s32
tsapp_set_system_var_double.argtypes = [pchar,double]

#arg[0] ACompleteName
#arg[1] AValue
tsapp_set_system_var_int32 = dll.tsapp_set_system_var_int32
tsapp_set_system_var_int32.restype = s32
tsapp_set_system_var_int32.argtypes = [pchar,s32]

#arg[0] ACompleteName
#arg[1] AValue
tsapp_set_system_var_uint32 = dll.tsapp_set_system_var_uint32
tsapp_set_system_var_uint32.restype = s32
tsapp_set_system_var_uint32.argtypes = [pchar,u32]

#arg[0] ACompleteName
#arg[1] AValue
tsapp_set_system_var_int64 = dll.tsapp_set_system_var_int64
tsapp_set_system_var_int64.restype = s32
tsapp_set_system_var_int64.argtypes = [pchar,s64]

#arg[0] ACompleteName
#arg[1] AValue
tsapp_set_system_var_uint64 = dll.tsapp_set_system_var_uint64
tsapp_set_system_var_uint64.restype = s32
tsapp_set_system_var_uint64.argtypes = [pchar,u64]

#arg[0] ACompleteName
#arg[1] ACapacity
#arg[2] AValue
tsapp_set_system_var_uint8_array = dll.tsapp_set_system_var_uint8_array
tsapp_set_system_var_uint8_array.restype = s32
tsapp_set_system_var_uint8_array.argtypes = [pchar,s32,pu8]

#arg[0] ACompleteName
#arg[1] ACapacity
#arg[2] AValue
tsapp_set_system_var_int32_array = dll.tsapp_set_system_var_int32_array
tsapp_set_system_var_int32_array.restype = s32
tsapp_set_system_var_int32_array.argtypes = [pchar,s32,ps32]

#arg[0] ACompleteName
#arg[1] ACapacity
#arg[2] AValue
tsapp_set_system_var_int64_array = dll.tsapp_set_system_var_int64_array
tsapp_set_system_var_int64_array.restype = s32
tsapp_set_system_var_int64_array.argtypes = [pchar,s32,ps64]

#arg[0] ACompleteName
#arg[1] ACapacity
#arg[2] AValue
tsapp_set_system_var_double_array = dll.tsapp_set_system_var_double_array
tsapp_set_system_var_double_array.restype = s32
tsapp_set_system_var_double_array.argtypes = [pchar,s32,pdouble]

#arg[0] ACompleteName
#arg[1] AValue
tsapp_set_system_var_string = dll.tsapp_set_system_var_string
tsapp_set_system_var_string.restype = s32
tsapp_set_system_var_string.argtypes = [pchar,pchar]

#arg[0] ACompleteName
tsapp_log_system_var = dll.tsapp_log_system_var
tsapp_log_system_var.restype = s32
tsapp_log_system_var.argtypes = [pchar]

#arg[0] ACompleteName
#arg[1] ACapacity
#arg[2] AValue
tsapp_get_system_var_generic = dll.tsapp_get_system_var_generic
tsapp_get_system_var_generic.restype = s32
tsapp_get_system_var_generic.argtypes = [pchar,s32,pchar]

#arg[0] ACompleteName
#arg[1] AValue
tsapp_set_system_var_generic = dll.tsapp_set_system_var_generic
tsapp_set_system_var_generic.restype = s32
tsapp_set_system_var_generic.argtypes = [pchar,pchar]

#arg[0] AString
tsapp_get_hardware_id_string = dll.tsapp_get_hardware_id_string
tsapp_get_hardware_id_string.restype = s32
tsapp_get_hardware_id_string.argtypes = [ppchar]

#arg[0] AArray8B
tsapp_get_hardware_id_array = dll.tsapp_get_hardware_id_array
tsapp_get_hardware_id_array.restype = s32
tsapp_get_hardware_id_array.argtypes = [pu8]

#arg[0] ACompleteName
#arg[1] AType
#arg[2] ADefaultValue
#arg[3] AComment
tsapp_create_system_var = dll.tsapp_create_system_var
tsapp_create_system_var.restype = s32
tsapp_create_system_var.argtypes = [pchar,TLIBSystemVarType,pchar,pchar]

#arg[0] ACompleteName
tsapp_delete_system_var = dll.tsapp_delete_system_var
tsapp_delete_system_var.restype = s32
tsapp_delete_system_var.argtypes = [pchar]

#arg[0] ALoadedDBCount
tsdb_reload_settings = dll.tsdb_reload_settings
tsdb_reload_settings.restype = s32
tsdb_reload_settings.argtypes = [POINTER(s32)]

tsdb_save_settings = dll.tsdb_save_settings
tsdb_save_settings.restype = s32
tsdb_save_settings.argtypes = []

#arg[0] ADBC
#arg[1] ASupportedChannelsBased0
#arg[2] AId
tsdb_load_can_db = dll.tsdb_load_can_db
tsdb_load_can_db.restype = s32
tsdb_load_can_db.argtypes = [pchar,pchar,POINTER(u32)]

#arg[0] AId
tsdb_unload_can_db = dll.tsdb_unload_can_db
tsdb_unload_can_db.restype = s32
tsdb_unload_can_db.argtypes = [u32]

tsdb_unload_can_dbs = dll.tsdb_unload_can_dbs
tsdb_unload_can_dbs.restype = s32
tsdb_unload_can_dbs.argtypes = []

#arg[0] ACount
tsdb_get_can_db_count = dll.tsdb_get_can_db_count
tsdb_get_can_db_count.restype = s32
tsdb_get_can_db_count.argtypes = [POINTER(s32)]

#arg[0] AIndex
#arg[1] AId
tsdb_get_can_db_id = dll.tsdb_get_can_db_id
tsdb_get_can_db_id.restype = s32
tsdb_get_can_db_id.argtypes = [s32,POINTER(u32)]

#arg[0] ADatabaseId
#arg[1] AType
#arg[2] AIndex
#arg[3] ASubIndex
#arg[4] AValue
tsdb_get_can_db_info = dll.tsdb_get_can_db_info
tsdb_get_can_db_info.restype = s32
tsdb_get_can_db_info.argtypes = [u32,s32,s32,s32,ppchar]

#arg[0] AFRFile
#arg[1] ASupportedChannels
#arg[2] AId
tsdb_load_flexray_db = dll.tsdb_load_flexray_db
tsdb_load_flexray_db.restype = s32
tsdb_load_flexray_db.argtypes = [pchar,pchar,POINTER(s32)]

#arg[0] AId
tsdb_unload_flexray_db = dll.tsdb_unload_flexray_db
tsdb_unload_flexray_db.restype = s32
tsdb_unload_flexray_db.argtypes = [s32]

tsdb_unload_flexray_dbs = dll.tsdb_unload_flexray_dbs
tsdb_unload_flexray_dbs.restype = s32
tsdb_unload_flexray_dbs.argtypes = []

#arg[0] ACount
tsdb_get_flexray_db_count = dll.tsdb_get_flexray_db_count
tsdb_get_flexray_db_count.restype = s32
tsdb_get_flexray_db_count.argtypes = [POINTER(s32)]

#arg[0] AAddr
#arg[1] ADBIndex
#arg[2] ASignalCount
#arg[3] AFrameCount
#arg[4] AECUCount
#arg[5] ASupportedChannelMask
#arg[6] AFlags
#arg[7] AName
#arg[8] AComment
tsdb_get_flexray_db_properties_by_address_verbose = dll.tsdb_get_flexray_db_properties_by_address_verbose
tsdb_get_flexray_db_properties_by_address_verbose.restype = s32
tsdb_get_flexray_db_properties_by_address_verbose.argtypes = [pchar,POINTER(s32),POINTER(s32),POINTER(s32),POINTER(s32),POINTER(s64),POINTER(s64),ppchar,ppchar]

#arg[0] ADBIndex
#arg[1] ASignalCount
#arg[2] AFrameCount
#arg[3] AECUCount
#arg[4] ASupportedChannelMask
#arg[5] AFlags
#arg[6] AName
#arg[7] AComment
tsdb_get_flexray_db_properties_by_index_verbose = dll.tsdb_get_flexray_db_properties_by_index_verbose
tsdb_get_flexray_db_properties_by_index_verbose.restype = s32
tsdb_get_flexray_db_properties_by_index_verbose.argtypes = [s32,POINTER(s32),POINTER(s32),POINTER(s32),POINTER(s64),POINTER(s64),ppchar,ppchar]

#arg[0] AAddr
#arg[1] ADBIndex
#arg[2] AECUIndex
#arg[3] ATxFrameCount
#arg[4] ARxFrameCount
#arg[5] AName
#arg[6] AComment
tsdb_get_flexray_ecu_properties_by_address_verbose = dll.tsdb_get_flexray_ecu_properties_by_address_verbose
tsdb_get_flexray_ecu_properties_by_address_verbose.restype = s32
tsdb_get_flexray_ecu_properties_by_address_verbose.argtypes = [pchar,POINTER(s32),POINTER(s32),POINTER(s32),POINTER(s32),ppchar,ppchar]

#arg[0] ADBIndex
#arg[1] AECUIndex
#arg[2] ATxFrameCount
#arg[3] ARxFrameCount
#arg[4] AName
#arg[5] AComment
tsdb_get_flexray_ecu_properties_by_index_verbose = dll.tsdb_get_flexray_ecu_properties_by_index_verbose
tsdb_get_flexray_ecu_properties_by_index_verbose.restype = s32
tsdb_get_flexray_ecu_properties_by_index_verbose.argtypes = [s32,s32,POINTER(s32),POINTER(s32),ppchar,ppchar]

#arg[0] AAddr
#arg[1] ADBIndex
#arg[2] AECUIndex
#arg[3] AFrameIndex
#arg[4] AIsTx
#arg[5] AFRChannelMask
#arg[6] AFRBaseCycle
#arg[7] AFRCycleRepetition
#arg[8] AFRIsStartupFrame
#arg[9] AFRSlotId
#arg[10] AFRCycleMask
#arg[11] ASignalCount
#arg[12] AFRDLC
#arg[13] AName
#arg[14] AComment
tsdb_get_flexray_frame_properties_by_address_verbose = dll.tsdb_get_flexray_frame_properties_by_address_verbose
tsdb_get_flexray_frame_properties_by_address_verbose.restype = s32
tsdb_get_flexray_frame_properties_by_address_verbose.argtypes = [pchar,POINTER(s32),POINTER(s32),POINTER(s32),POINTER(cbool),POINTER(s32),POINTER(s32),POINTER(s32),POINTER(cbool),POINTER(s32),POINTER(s64),POINTER(s32),POINTER(s32),ppchar,ppchar]

#arg[0] ADBIndex
#arg[1] AECUIndex
#arg[2] AFrameIndex
#arg[3] AIsTx
#arg[4] AFRChannelMask
#arg[5] AFRBaseCycle
#arg[6] AFRCycleRepetition
#arg[7] AFRIsStartupFrame
#arg[8] AFRSlotId
#arg[9] AFRCycleMask
#arg[10] ASignalCount
#arg[11] AFRDLC
#arg[12] AName
#arg[13] AComment
tsdb_get_flexray_frame_properties_by_index_verbose = dll.tsdb_get_flexray_frame_properties_by_index_verbose
tsdb_get_flexray_frame_properties_by_index_verbose.restype = s32
tsdb_get_flexray_frame_properties_by_index_verbose.argtypes = [s32,s32,s32,cbool,POINTER(s32),POINTER(s32),POINTER(s32),POINTER(cbool),POINTER(s32),POINTER(s64),POINTER(s32),POINTER(s32),ppchar,ppchar]

#arg[0] AAddr
#arg[1] ADBIndex
#arg[2] AECUIndex
#arg[3] AFrameIndex
#arg[4] ASignalIndex
#arg[5] AIsTx
#arg[6] ASignalType
#arg[7] ACompuMethod
#arg[8] AIsIntel
#arg[9] AActualStartBit
#arg[10] AActualUpdateBit
#arg[11] ALength
#arg[12] AFactor
#arg[13] AOffset
#arg[14] AInitValue
#arg[15] AName
#arg[16] AComment
tsdb_get_flexray_signal_properties_by_address_verbose = dll.tsdb_get_flexray_signal_properties_by_address_verbose
tsdb_get_flexray_signal_properties_by_address_verbose.restype = s32
tsdb_get_flexray_signal_properties_by_address_verbose.argtypes = [pchar,POINTER(s32),POINTER(s32),POINTER(s32),POINTER(s32),POINTER(cbool),POINTER(TSignalType),POINTER(TFlexRayCompuMethod),POINTER(cbool),POINTER(s32),POINTER(s32),POINTER(s32),POINTER(double),POINTER(double),POINTER(double),ppchar,ppchar]

#arg[0] ADBIndex
#arg[1] AECUIndex
#arg[2] AFrameIndex
#arg[3] ASignalIndex
#arg[4] AIsTx
#arg[5] ASignalType
#arg[6] ACompuMethod
#arg[7] AIsIntel
#arg[8] AActualStartBit
#arg[9] AActualUpdateBit
#arg[10] ALength
#arg[11] AFactor
#arg[12] AOffset
#arg[13] AInitValue
#arg[14] AName
#arg[15] AComment
tsdb_get_flexray_signal_properties_by_index_verbose = dll.tsdb_get_flexray_signal_properties_by_index_verbose
tsdb_get_flexray_signal_properties_by_index_verbose.restype = s32
tsdb_get_flexray_signal_properties_by_index_verbose.argtypes = [s32,s32,s32,s32,cbool,POINTER(TSignalType),POINTER(TFlexRayCompuMethod),POINTER(cbool),POINTER(s32),POINTER(s32),POINTER(s32),POINTER(double),POINTER(double),POINTER(double),ppchar,ppchar]

#arg[0] AIndex
#arg[1] AId
tsdb_get_flexray_db_id = dll.tsdb_get_flexray_db_id
tsdb_get_flexray_db_id.restype = s32
tsdb_get_flexray_db_id.argtypes = [s32,POINTER(s32)]

#arg[0] AValue
tsdb_get_can_db_properties_by_index = dll.tsdb_get_can_db_properties_by_index
tsdb_get_can_db_properties_by_index.restype = s32
tsdb_get_can_db_properties_by_index.argtypes = [PMPDBProperties]

#arg[0] AValue
tsdb_get_lin_db_properties_by_index = dll.tsdb_get_lin_db_properties_by_index
tsdb_get_lin_db_properties_by_index.restype = s32
tsdb_get_lin_db_properties_by_index.argtypes = [PMPDBProperties]

#arg[0] AValue
tsdb_get_flexray_db_properties_by_index = dll.tsdb_get_flexray_db_properties_by_index
tsdb_get_flexray_db_properties_by_index.restype = s32
tsdb_get_flexray_db_properties_by_index.argtypes = [PMPDBProperties]

#arg[0] AValue
tsdb_get_can_db_ecu_properties_by_index = dll.tsdb_get_can_db_ecu_properties_by_index
tsdb_get_can_db_ecu_properties_by_index.restype = s32
tsdb_get_can_db_ecu_properties_by_index.argtypes = [PMPDBECUProperties]

#arg[0] AValue
tsdb_get_lin_db_ecu_properties_by_index = dll.tsdb_get_lin_db_ecu_properties_by_index
tsdb_get_lin_db_ecu_properties_by_index.restype = s32
tsdb_get_lin_db_ecu_properties_by_index.argtypes = [PMPDBECUProperties]

#arg[0] AValue
tsdb_get_flexray_db_ecu_properties_by_index = dll.tsdb_get_flexray_db_ecu_properties_by_index
tsdb_get_flexray_db_ecu_properties_by_index.restype = s32
tsdb_get_flexray_db_ecu_properties_by_index.argtypes = [PMPDBECUProperties]

#arg[0] AValue
tsdb_get_can_db_frame_properties_by_index = dll.tsdb_get_can_db_frame_properties_by_index
tsdb_get_can_db_frame_properties_by_index.restype = s32
tsdb_get_can_db_frame_properties_by_index.argtypes = [PMPDBFrameProperties]

#arg[0] AValue
tsdb_get_lin_db_frame_properties_by_index = dll.tsdb_get_lin_db_frame_properties_by_index
tsdb_get_lin_db_frame_properties_by_index.restype = s32
tsdb_get_lin_db_frame_properties_by_index.argtypes = [PMPDBFrameProperties]

#arg[0] AValue
tsdb_get_flexray_db_frame_properties_by_index = dll.tsdb_get_flexray_db_frame_properties_by_index
tsdb_get_flexray_db_frame_properties_by_index.restype = s32
tsdb_get_flexray_db_frame_properties_by_index.argtypes = [PMPDBFrameProperties]

#arg[0] AValue
tsdb_get_can_db_signal_properties_by_index = dll.tsdb_get_can_db_signal_properties_by_index
tsdb_get_can_db_signal_properties_by_index.restype = s32
tsdb_get_can_db_signal_properties_by_index.argtypes = [PMPDBSignalProperties]

#arg[0] AValue
tsdb_get_lin_db_signal_properties_by_index = dll.tsdb_get_lin_db_signal_properties_by_index
tsdb_get_lin_db_signal_properties_by_index.restype = s32
tsdb_get_lin_db_signal_properties_by_index.argtypes = [PMPDBSignalProperties]

#arg[0] AValue
tsdb_get_flexray_db_signal_properties_by_index = dll.tsdb_get_flexray_db_signal_properties_by_index
tsdb_get_flexray_db_signal_properties_by_index.restype = s32
tsdb_get_flexray_db_signal_properties_by_index.argtypes = [PMPDBSignalProperties]

#arg[0] AAddr
#arg[1] AValue
tsdb_get_can_db_properties_by_address = dll.tsdb_get_can_db_properties_by_address
tsdb_get_can_db_properties_by_address.restype = s32
tsdb_get_can_db_properties_by_address.argtypes = [pchar,PMPDBProperties]

#arg[0] AAddr
#arg[1] AValue
tsdb_get_lin_db_properties_by_address = dll.tsdb_get_lin_db_properties_by_address
tsdb_get_lin_db_properties_by_address.restype = s32
tsdb_get_lin_db_properties_by_address.argtypes = [pchar,PMPDBProperties]

#arg[0] AAddr
#arg[1] AValue
tsdb_get_flexray_db_properties_by_address = dll.tsdb_get_flexray_db_properties_by_address
tsdb_get_flexray_db_properties_by_address.restype = s32
tsdb_get_flexray_db_properties_by_address.argtypes = [pchar,PMPDBProperties]

#arg[0] AAddr
#arg[1] AValue
tsdb_get_can_db_ecu_properties_by_address = dll.tsdb_get_can_db_ecu_properties_by_address
tsdb_get_can_db_ecu_properties_by_address.restype = s32
tsdb_get_can_db_ecu_properties_by_address.argtypes = [pchar,PMPDBECUProperties]

#arg[0] AAddr
#arg[1] AValue
tsdb_get_lin_db_ecu_properties_by_address = dll.tsdb_get_lin_db_ecu_properties_by_address
tsdb_get_lin_db_ecu_properties_by_address.restype = s32
tsdb_get_lin_db_ecu_properties_by_address.argtypes = [pchar,PMPDBECUProperties]

#arg[0] AAddr
#arg[1] AValue
tsdb_get_flexray_db_ecu_properties_by_address = dll.tsdb_get_flexray_db_ecu_properties_by_address
tsdb_get_flexray_db_ecu_properties_by_address.restype = s32
tsdb_get_flexray_db_ecu_properties_by_address.argtypes = [pchar,PMPDBECUProperties]

#arg[0] AAddr
#arg[1] AValue
tsdb_get_can_db_frame_properties_by_address = dll.tsdb_get_can_db_frame_properties_by_address
tsdb_get_can_db_frame_properties_by_address.restype = s32
tsdb_get_can_db_frame_properties_by_address.argtypes = [pchar,PMPDBFrameProperties]

#arg[0] AAddr
#arg[1] AValue
tsdb_get_lin_db_frame_properties_by_address = dll.tsdb_get_lin_db_frame_properties_by_address
tsdb_get_lin_db_frame_properties_by_address.restype = s32
tsdb_get_lin_db_frame_properties_by_address.argtypes = [pchar,PMPDBFrameProperties]

#arg[0] AAddr
#arg[1] AValue
tsdb_get_flexray_db_frame_properties_by_address = dll.tsdb_get_flexray_db_frame_properties_by_address
tsdb_get_flexray_db_frame_properties_by_address.restype = s32
tsdb_get_flexray_db_frame_properties_by_address.argtypes = [pchar,PMPDBFrameProperties]

#arg[0] AAddr
#arg[1] AValue
tsdb_get_can_db_signal_properties_by_address = dll.tsdb_get_can_db_signal_properties_by_address
tsdb_get_can_db_signal_properties_by_address.restype = s32
tsdb_get_can_db_signal_properties_by_address.argtypes = [pchar,PMPDBSignalProperties]

#arg[0] AAddr
#arg[1] AValue
tsdb_get_lin_db_signal_properties_by_address = dll.tsdb_get_lin_db_signal_properties_by_address
tsdb_get_lin_db_signal_properties_by_address.restype = s32
tsdb_get_lin_db_signal_properties_by_address.argtypes = [pchar,PMPDBSignalProperties]

#arg[0] AAddr
#arg[1] AValue
tsdb_get_flexray_db_signal_properties_by_address = dll.tsdb_get_flexray_db_signal_properties_by_address
tsdb_get_flexray_db_signal_properties_by_address.restype = s32
tsdb_get_flexray_db_signal_properties_by_address.argtypes = [pchar,PMPDBSignalProperties]

#arg[0] ALDF
#arg[1] ASupportedChannelsBased0
#arg[2] AId
tsdb_load_lin_db = dll.tsdb_load_lin_db
tsdb_load_lin_db.restype = s32
tsdb_load_lin_db.argtypes = [pchar,pchar,POINTER(u32)]

#arg[0] AId
tsdb_unload_lin_db = dll.tsdb_unload_lin_db
tsdb_unload_lin_db.restype = s32
tsdb_unload_lin_db.argtypes = [u32]

tsdb_unload_lin_dbs = dll.tsdb_unload_lin_dbs
tsdb_unload_lin_dbs.restype = s32
tsdb_unload_lin_dbs.argtypes = []

#arg[0] ACount
tsdb_get_lin_db_count = dll.tsdb_get_lin_db_count
tsdb_get_lin_db_count.restype = s32
tsdb_get_lin_db_count.argtypes = [POINTER(s32)]

#arg[0] AIndex
#arg[1] AId
tsdb_get_lin_db_id = dll.tsdb_get_lin_db_id
tsdb_get_lin_db_id.restype = s32
tsdb_get_lin_db_id.argtypes = [s32,POINTER(u32)]

#arg[0] AIdxDB
#arg[1] AIndex
#arg[2] AValue
tsdb_get_can_db_frame_properties_by_db_index = dll.tsdb_get_can_db_frame_properties_by_db_index
tsdb_get_can_db_frame_properties_by_db_index.restype = s32
tsdb_get_can_db_frame_properties_by_db_index.argtypes = [s32,s32,PMPDBFrameProperties]

#arg[0] AIdxDB
#arg[1] AIndex
#arg[2] AValue
tsdb_get_lin_db_frame_properties_by_db_index = dll.tsdb_get_lin_db_frame_properties_by_db_index
tsdb_get_lin_db_frame_properties_by_db_index.restype = s32
tsdb_get_lin_db_frame_properties_by_db_index.argtypes = [s32,s32,PMPDBFrameProperties]

#arg[0] AIdxDB
#arg[1] AIndex
#arg[2] AValue
tsdb_get_flexray_db_frame_properties_by_db_index = dll.tsdb_get_flexray_db_frame_properties_by_db_index
tsdb_get_flexray_db_frame_properties_by_db_index.restype = s32
tsdb_get_flexray_db_frame_properties_by_db_index.argtypes = [s32,s32,PMPDBFrameProperties]

#arg[0] AIdxDB
#arg[1] AIdxFrame
#arg[2] ASgnIndexInFrame
#arg[3] AValue
tsdb_get_can_db_signal_properties_by_frame_index = dll.tsdb_get_can_db_signal_properties_by_frame_index
tsdb_get_can_db_signal_properties_by_frame_index.restype = s32
tsdb_get_can_db_signal_properties_by_frame_index.argtypes = [s32,s32,s32,PMPDBSignalProperties]

#arg[0] AIdxDB
#arg[1] AIdxFrame
#arg[2] ASgnIndexInFrame
#arg[3] AValue
tsdb_get_lin_db_signal_properties_by_frame_index = dll.tsdb_get_lin_db_signal_properties_by_frame_index
tsdb_get_lin_db_signal_properties_by_frame_index.restype = s32
tsdb_get_lin_db_signal_properties_by_frame_index.argtypes = [s32,s32,s32,PMPDBSignalProperties]

#arg[0] AIdxDB
#arg[1] AIdxFrame
#arg[2] ASgnIndexInFrame
#arg[3] AValue
tsdb_get_flexray_db_signal_properties_by_frame_index = dll.tsdb_get_flexray_db_signal_properties_by_frame_index
tsdb_get_flexray_db_signal_properties_by_frame_index.restype = s32
tsdb_get_flexray_db_signal_properties_by_frame_index.argtypes = [s32,s32,s32,PMPDBSignalProperties]

#arg[0] ACAN
#arg[1] AMsgName
#arg[2] ASgnName
#arg[3] AValue
tsdb_set_signal_value_can = dll.tsdb_set_signal_value_can
tsdb_set_signal_value_can.restype = s32
tsdb_set_signal_value_can.argtypes = [PLIBCAN,pchar,pchar,double]

#arg[0] ACAN
#arg[1] AMsgName
#arg[2] ASgnName
#arg[3] AValue
tsdb_get_signal_value_can = dll.tsdb_get_signal_value_can
tsdb_get_signal_value_can.restype = s32
tsdb_get_signal_value_can.argtypes = [PLIBCAN,pchar,pchar,POINTER(double)]

#arg[0] ACANfd
#arg[1] AMsgName
#arg[2] ASgnName
#arg[3] AValue
tsdb_set_signal_value_canfd = dll.tsdb_set_signal_value_canfd
tsdb_set_signal_value_canfd.restype = s32
tsdb_set_signal_value_canfd.argtypes = [PLIBCANFD,pchar,pchar,double]

#arg[0] ACANfd
#arg[1] AMsgName
#arg[2] ASgnName
#arg[3] AValue
tsdb_get_signal_value_canfd = dll.tsdb_get_signal_value_canfd
tsdb_get_signal_value_canfd.restype = s32
tsdb_get_signal_value_canfd.argtypes = [PLIBCANFD,pchar,pchar,POINTER(double)]

#arg[0] ALoadedEngineCount
tslog_reload_settings = dll.tslog_reload_settings
tslog_reload_settings.restype = s32
tslog_reload_settings.argtypes = [POINTER(s32)]

#arg[0] AFileName
#arg[1] AIndex
tslog_add_online_replay_config = dll.tslog_add_online_replay_config
tslog_add_online_replay_config.restype = s32
tslog_add_online_replay_config.argtypes = [pchar,POINTER(s32)]

#arg[0] AIndex
#arg[1] AName
#arg[2] AFileName
#arg[3] AAutoStart
#arg[4] AIsRepetitiveMode
#arg[5] AStartTimingMode
#arg[6] AStartDelayTimeMs
#arg[7] ASendTx
#arg[8] ASendRx
#arg[9] AMappings
tslog_set_online_replay_config = dll.tslog_set_online_replay_config
tslog_set_online_replay_config.restype = s32
tslog_set_online_replay_config.argtypes = [s32,pchar,pchar,cbool,cbool,TLIBOnlineReplayTimingMode,s32,cbool,cbool,pchar]

#arg[0] ACount
tslog_get_online_replay_count = dll.tslog_get_online_replay_count
tslog_get_online_replay_count.restype = s32
tslog_get_online_replay_count.argtypes = [POINTER(s32)]

#arg[0] AIndex
#arg[1] AName
#arg[2] AFileName
#arg[3] AAutoStart
#arg[4] AIsRepetitiveMode
#arg[5] AStartTimingMode
#arg[6] AStartDelayTimeMs
#arg[7] ASendTx
#arg[8] ASendRx
#arg[9] AMappings
tslog_get_online_replay_config = dll.tslog_get_online_replay_config
tslog_get_online_replay_config.restype = s32
tslog_get_online_replay_config.argtypes = [s32,ppchar,ppchar,POINTER(cbool),POINTER(cbool),POINTER(TLIBOnlineReplayTimingMode),POINTER(s32),POINTER(cbool),POINTER(cbool),ppchar]

#arg[0] AIndex
tslog_del_online_replay_config = dll.tslog_del_online_replay_config
tslog_del_online_replay_config.restype = s32
tslog_del_online_replay_config.argtypes = [s32]

tslog_del_online_replay_configs = dll.tslog_del_online_replay_configs
tslog_del_online_replay_configs.restype = s32
tslog_del_online_replay_configs.argtypes = []

#arg[0] AIndex
tslog_start_online_replay = dll.tslog_start_online_replay
tslog_start_online_replay.restype = s32
tslog_start_online_replay.argtypes = [s32]

tslog_start_online_replays = dll.tslog_start_online_replays
tslog_start_online_replays.restype = s32
tslog_start_online_replays.argtypes = []

#arg[0] AIndex
tslog_pause_online_replay = dll.tslog_pause_online_replay
tslog_pause_online_replay.restype = s32
tslog_pause_online_replay.argtypes = [s32]

tslog_pause_online_replays = dll.tslog_pause_online_replays
tslog_pause_online_replays.restype = s32
tslog_pause_online_replays.argtypes = []

#arg[0] AIndex
tslog_stop_online_replay = dll.tslog_stop_online_replay
tslog_stop_online_replay.restype = s32
tslog_stop_online_replay.argtypes = [s32]

tslog_stop_online_replays = dll.tslog_stop_online_replays
tslog_stop_online_replays.restype = s32
tslog_stop_online_replays.argtypes = []

#arg[0] AIndex
#arg[1] AStatus
#arg[2] AProgressPercent100
tslog_get_online_replay_status = dll.tslog_get_online_replay_status
tslog_get_online_replay_status.restype = s32
tslog_get_online_replay_status.argtypes = [s32,POINTER(TLIBOnlineReplayStatus),POINTER(single)]

#arg[0] AFileName
#arg[1] AHandle
tslog_blf_write_start = dll.tslog_blf_write_start
tslog_blf_write_start.restype = s32
tslog_blf_write_start.argtypes = [pchar,psize_t]

#arg[0] AHandle
#arg[1] ACount
tslog_blf_write_set_max_count = dll.tslog_blf_write_set_max_count
tslog_blf_write_set_max_count.restype = s32
tslog_blf_write_set_max_count.argtypes = [size_t,u32]

#arg[0] AHandle
#arg[1] ACAN
tslog_blf_write_can = dll.tslog_blf_write_can
tslog_blf_write_can.restype = s32
tslog_blf_write_can.argtypes = [size_t,PLIBCAN]

#arg[0] AHandle
#arg[1] ACANFD
tslog_blf_write_can_fd = dll.tslog_blf_write_can_fd
tslog_blf_write_can_fd.restype = s32
tslog_blf_write_can_fd.argtypes = [size_t,PLIBCANFD]

#arg[0] AHandle
#arg[1] ALIN
tslog_blf_write_lin = dll.tslog_blf_write_lin
tslog_blf_write_lin.restype = s32
tslog_blf_write_lin.argtypes = [size_t,PLIBLIN]

#arg[0] AHandle
#arg[1] ATimeUs
#arg[2] AComment
tslog_blf_write_realtime_comment = dll.tslog_blf_write_realtime_comment
tslog_blf_write_realtime_comment.restype = s32
tslog_blf_write_realtime_comment.argtypes = [size_t,s64,pchar]

#arg[0] AHandle
tslog_blf_write_end = dll.tslog_blf_write_end
tslog_blf_write_end.restype = s32
tslog_blf_write_end.argtypes = [size_t]

#arg[0] AFileName
#arg[1] AHandle
#arg[2] AObjCount
tslog_blf_read_start = dll.tslog_blf_read_start
tslog_blf_read_start.restype = s32
tslog_blf_read_start.argtypes = [pchar,psize_t,ps32]

#arg[0] AFileName
#arg[1] AHandle
#arg[2] AObjCount
#arg[3] AYear
#arg[4] AMonth
#arg[5] ADayOfWeek
#arg[6] ADay
#arg[7] AHour
#arg[8] AMinute
#arg[9] ASecond
#arg[10] AMilliseconds
tsLog_blf_read_start_verbose = dll.tsLog_blf_read_start_verbose
tsLog_blf_read_start_verbose.restype = s32
tsLog_blf_read_start_verbose.argtypes = [pchar,psize_t,ps32,pu16,pu16,pu16,pu16,pu16,pu16,pu16,pu16]

#arg[0] AHandle
#arg[1] AObjReadCount
tslog_blf_read_status = dll.tslog_blf_read_status
tslog_blf_read_status.restype = s32
tslog_blf_read_status.argtypes = [size_t,ps32]

#arg[0] AHandle
#arg[1] AProgressedCnt
#arg[2] AType
#arg[3] ACAN
#arg[4] ALIN
#arg[5] ACANFD
tslog_blf_read_object = dll.tslog_blf_read_object
tslog_blf_read_object.restype = s32
tslog_blf_read_object.argtypes = [size_t,ps32,PSupportedObjType,PLIBCAN,PLIBLIN,PLIBCANFD]

#arg[0] AHandle
#arg[1] AProgressedCnt
#arg[2] AType
#arg[3] ACAN
#arg[4] ALIN
#arg[5] ACANFD
#arg[6] AComment
tslog_blf_read_object_w_comment = dll.tslog_blf_read_object_w_comment
tslog_blf_read_object_w_comment.restype = s32
tslog_blf_read_object_w_comment.argtypes = [size_t,ps32,PSupportedObjType,PLIBCAN,PLIBLIN,PLIBCANFD,Prealtime_comment_t]

#arg[0] AHandle
tslog_blf_read_end = dll.tslog_blf_read_end
tslog_blf_read_end.restype = s32
tslog_blf_read_end.argtypes = [size_t]

#arg[0] AHandle
#arg[1] AProg100
#arg[2] ATime
#arg[3] AProgressedCnt
tslog_blf_seek_object_time = dll.tslog_blf_seek_object_time
tslog_blf_seek_object_time.restype = s32
tslog_blf_seek_object_time.argtypes = [size_t,double,POINTER(s64),POINTER(s32)]

#arg[0] AObj
#arg[1] ABLFFileName
#arg[2] AASCFileName
#arg[3] AProgressCallback
tslog_blf_to_asc = dll.tslog_blf_to_asc
tslog_blf_to_asc.restype = s32
tslog_blf_to_asc.argtypes = [ps32,pchar,pchar,TReadProgressCallback]

#arg[0] AObj
#arg[1] AASCFileName
#arg[2] ABLFFileName
#arg[3] AProgressCallback
tslog_asc_to_blf = dll.tslog_asc_to_blf
tslog_asc_to_blf.restype = s32
tslog_asc_to_blf.argtypes = [ps32,pchar,pchar,TReadProgressCallback]

tscom_lin_rbs_reload_settings = dll.tscom_lin_rbs_reload_settings
tscom_lin_rbs_reload_settings.restype = s32
tscom_lin_rbs_reload_settings.argtypes = []

tscom_lin_rbs_start = dll.tscom_lin_rbs_start
tscom_lin_rbs_start.restype = s32
tscom_lin_rbs_start.argtypes = []

tscom_lin_rbs_stop = dll.tscom_lin_rbs_stop
tscom_lin_rbs_stop.restype = s32
tscom_lin_rbs_stop.argtypes = []

#arg[0] AIsRunning
tscom_lin_rbs_is_running = dll.tscom_lin_rbs_is_running
tscom_lin_rbs_is_running.restype = s32
tscom_lin_rbs_is_running.argtypes = [POINTER(cbool)]

#arg[0] AAutoStart
#arg[1] AAutoSendOnModification
#arg[2] AActivateNodeSimulation
#arg[3] AInitValueOptions
tscom_lin_rbs_configure = dll.tscom_lin_rbs_configure
tscom_lin_rbs_configure.restype = s32
tscom_lin_rbs_configure.argtypes = [cbool,cbool,cbool,TLIBRBSInitValueOptions]

#arg[0] AEnable
#arg[1] AIncludingChildren
tscom_lin_rbs_activate_all_networks = dll.tscom_lin_rbs_activate_all_networks
tscom_lin_rbs_activate_all_networks.restype = s32
tscom_lin_rbs_activate_all_networks.argtypes = [cbool,cbool]

#arg[0] AIdxChn
#arg[1] AEnable
#arg[2] ANetworkName
#arg[3] AIncludingChildren
tscom_lin_rbs_activate_network_by_name = dll.tscom_lin_rbs_activate_network_by_name
tscom_lin_rbs_activate_network_by_name.restype = s32
tscom_lin_rbs_activate_network_by_name.argtypes = [s32,cbool,pchar,cbool]

#arg[0] AIdxChn
#arg[1] AEnable
#arg[2] ANetworkName
#arg[3] ANodeName
#arg[4] AIncludingChildren
tscom_lin_rbs_activate_node_by_name = dll.tscom_lin_rbs_activate_node_by_name
tscom_lin_rbs_activate_node_by_name.restype = s32
tscom_lin_rbs_activate_node_by_name.argtypes = [s32,cbool,pchar,pchar,cbool]

#arg[0] AIdxChn
#arg[1] AEnable
#arg[2] ANetworkName
#arg[3] ANodeName
#arg[4] AMsgName
tscom_lin_rbs_activate_message_by_name = dll.tscom_lin_rbs_activate_message_by_name
tscom_lin_rbs_activate_message_by_name.restype = s32
tscom_lin_rbs_activate_message_by_name.argtypes = [s32,cbool,pchar,pchar,pchar]

#arg[0] AIdxChn
#arg[1] AIntervalMs
#arg[2] ANetworkName
#arg[3] ANodeName
#arg[4] AMsgName
tscom_lin_rbs_set_message_delay_time_by_name = dll.tscom_lin_rbs_set_message_delay_time_by_name
tscom_lin_rbs_set_message_delay_time_by_name.restype = s32
tscom_lin_rbs_set_message_delay_time_by_name.argtypes = [s32,s32,pchar,pchar,pchar]

#arg[0] AIdxChn
#arg[1] ANetworkName
#arg[2] ANodeName
#arg[3] AMsgName
#arg[4] ASignalName
#arg[5] AValue
tscom_lin_rbs_get_signal_value_by_element = dll.tscom_lin_rbs_get_signal_value_by_element
tscom_lin_rbs_get_signal_value_by_element.restype = s32
tscom_lin_rbs_get_signal_value_by_element.argtypes = [s32,pchar,pchar,pchar,pchar,POINTER(double)]

#arg[0] ASymbolAddress
#arg[1] AValue
tscom_lin_rbs_get_signal_value_by_address = dll.tscom_lin_rbs_get_signal_value_by_address
tscom_lin_rbs_get_signal_value_by_address.restype = s32
tscom_lin_rbs_get_signal_value_by_address.argtypes = [pchar,POINTER(double)]

#arg[0] AIdxChn
#arg[1] ANetworkName
#arg[2] ANodeName
#arg[3] AMsgName
#arg[4] ASignalName
#arg[5] AValue
tscom_lin_rbs_set_signal_value_by_element = dll.tscom_lin_rbs_set_signal_value_by_element
tscom_lin_rbs_set_signal_value_by_element.restype = s32
tscom_lin_rbs_set_signal_value_by_element.argtypes = [s32,pchar,pchar,pchar,pchar,double]

#arg[0] ASymbolAddress
#arg[1] AValue
tscom_lin_rbs_set_signal_value_by_address = dll.tscom_lin_rbs_set_signal_value_by_address
tscom_lin_rbs_set_signal_value_by_address.restype = s32
tscom_lin_rbs_set_signal_value_by_address.argtypes = [pchar,double]

tscom_can_rbs_reload_settings = dll.tscom_can_rbs_reload_settings
tscom_can_rbs_reload_settings.restype = s32
tscom_can_rbs_reload_settings.argtypes = []

tscom_can_rbs_start = dll.tscom_can_rbs_start
tscom_can_rbs_start.restype = s32
tscom_can_rbs_start.argtypes = []

tscom_can_rbs_stop = dll.tscom_can_rbs_stop
tscom_can_rbs_stop.restype = s32
tscom_can_rbs_stop.argtypes = []

#arg[0] AIsRunning
tscom_can_rbs_is_running = dll.tscom_can_rbs_is_running
tscom_can_rbs_is_running.restype = s32
tscom_can_rbs_is_running.argtypes = [POINTER(cbool)]

#arg[0] AAutoStart
#arg[1] AAutoSendOnModification
#arg[2] AActivateNodeSimulation
#arg[3] AInitValueOptions
tscom_can_rbs_configure = dll.tscom_can_rbs_configure
tscom_can_rbs_configure.restype = s32
tscom_can_rbs_configure.argtypes = [cbool,cbool,cbool,TLIBRBSInitValueOptions]

#arg[0] AEnable
#arg[1] AIncludingChildren
tscom_can_rbs_activate_all_networks = dll.tscom_can_rbs_activate_all_networks
tscom_can_rbs_activate_all_networks.restype = s32
tscom_can_rbs_activate_all_networks.argtypes = [cbool,cbool]

#arg[0] AIdxChn
#arg[1] AEnable
#arg[2] ANetworkName
#arg[3] AIncludingChildren
tscom_can_rbs_activate_network_by_name = dll.tscom_can_rbs_activate_network_by_name
tscom_can_rbs_activate_network_by_name.restype = s32
tscom_can_rbs_activate_network_by_name.argtypes = [s32,cbool,pchar,cbool]

#arg[0] AIdxChn
#arg[1] AEnable
#arg[2] ANetworkName
#arg[3] ANodeName
#arg[4] AIncludingChildren
tscom_can_rbs_activate_node_by_name = dll.tscom_can_rbs_activate_node_by_name
tscom_can_rbs_activate_node_by_name.restype = s32
tscom_can_rbs_activate_node_by_name.argtypes = [s32,cbool,pchar,pchar,cbool]

#arg[0] AIdxChn
#arg[1] AEnable
#arg[2] ANetworkName
#arg[3] ANodeName
#arg[4] AMsgName
tscom_can_rbs_activate_message_by_name = dll.tscom_can_rbs_activate_message_by_name
tscom_can_rbs_activate_message_by_name.restype = s32
tscom_can_rbs_activate_message_by_name.argtypes = [s32,cbool,pchar,pchar,pchar]

#arg[0] AIdxChn
#arg[1] AIntervalMs
#arg[2] ANetworkName
#arg[3] ANodeName
#arg[4] AMsgName
tscom_can_rbs_set_message_cycle_by_name = dll.tscom_can_rbs_set_message_cycle_by_name
tscom_can_rbs_set_message_cycle_by_name.restype = s32
tscom_can_rbs_set_message_cycle_by_name.argtypes = [s32,s32,pchar,pchar,pchar]

#arg[0] AIdxChn
#arg[1] ANetworkName
#arg[2] ANodeName
#arg[3] AMsgName
#arg[4] ASignalName
#arg[5] AValue
tscom_can_rbs_get_signal_value_by_element = dll.tscom_can_rbs_get_signal_value_by_element
tscom_can_rbs_get_signal_value_by_element.restype = s32
tscom_can_rbs_get_signal_value_by_element.argtypes = [s32,pchar,pchar,pchar,pchar,POINTER(double)]

#arg[0] ASymbolAddress
#arg[1] AValue
tscom_can_rbs_get_signal_value_by_address = dll.tscom_can_rbs_get_signal_value_by_address
tscom_can_rbs_get_signal_value_by_address.restype = s32
tscom_can_rbs_get_signal_value_by_address.argtypes = [pchar,POINTER(double)]

#arg[0] AIdxChn
#arg[1] ANetworkName
#arg[2] ANodeName
#arg[3] AMsgName
#arg[4] ASignalName
#arg[5] AValue
tscom_can_rbs_set_signal_value_by_element = dll.tscom_can_rbs_set_signal_value_by_element
tscom_can_rbs_set_signal_value_by_element.restype = s32
tscom_can_rbs_set_signal_value_by_element.argtypes = [s32,pchar,pchar,pchar,pchar,double]

#arg[0] ASymbolAddress
#arg[1] AValue
tscom_can_rbs_set_signal_value_by_address = dll.tscom_can_rbs_set_signal_value_by_address
tscom_can_rbs_set_signal_value_by_address.restype = s32
tscom_can_rbs_set_signal_value_by_address.argtypes = [pchar,double]

tscom_flexray_rbs_start = dll.tscom_flexray_rbs_start
tscom_flexray_rbs_start.restype = s32
tscom_flexray_rbs_start.argtypes = []

tscom_flexray_rbs_stop = dll.tscom_flexray_rbs_stop
tscom_flexray_rbs_stop.restype = s32
tscom_flexray_rbs_stop.argtypes = []

#arg[0] AIsRunning
tscom_flexray_rbs_is_running = dll.tscom_flexray_rbs_is_running
tscom_flexray_rbs_is_running.restype = s32
tscom_flexray_rbs_is_running.argtypes = [POINTER(cbool)]

#arg[0] AAutoStart
#arg[1] AAutoSendOnModification
#arg[2] AActivateECUSimulation
#arg[3] AInitValueOptions
tscom_flexray_rbs_configure = dll.tscom_flexray_rbs_configure
tscom_flexray_rbs_configure.restype = s32
tscom_flexray_rbs_configure.argtypes = [cbool,cbool,cbool,TLIBRBSInitValueOptions]

#arg[0] AEnable
#arg[1] AIncludingChildren
tscom_flexray_rbs_activate_all_clusters = dll.tscom_flexray_rbs_activate_all_clusters
tscom_flexray_rbs_activate_all_clusters.restype = s32
tscom_flexray_rbs_activate_all_clusters.argtypes = [cbool,cbool]

#arg[0] AIdxChn
#arg[1] AEnable
#arg[2] AClusterName
#arg[3] AIncludingChildren
tscom_flexray_rbs_activate_cluster_by_name = dll.tscom_flexray_rbs_activate_cluster_by_name
tscom_flexray_rbs_activate_cluster_by_name.restype = s32
tscom_flexray_rbs_activate_cluster_by_name.argtypes = [s32,cbool,pchar,cbool]

#arg[0] AIdxChn
#arg[1] AEnable
#arg[2] AClusterName
#arg[3] AECUName
#arg[4] AIncludingChildren
tscom_flexray_rbs_activate_ecu_by_name = dll.tscom_flexray_rbs_activate_ecu_by_name
tscom_flexray_rbs_activate_ecu_by_name.restype = s32
tscom_flexray_rbs_activate_ecu_by_name.argtypes = [s32,cbool,pchar,pchar,cbool]

#arg[0] AIdxChn
#arg[1] AEnable
#arg[2] AClusterName
#arg[3] AECUName
#arg[4] AFrameName
tscom_flexray_rbs_activate_frame_by_name = dll.tscom_flexray_rbs_activate_frame_by_name
tscom_flexray_rbs_activate_frame_by_name.restype = s32
tscom_flexray_rbs_activate_frame_by_name.argtypes = [s32,cbool,pchar,pchar,pchar]

#arg[0] AIdxChn
#arg[1] AClusterName
#arg[2] AECUName
#arg[3] AFrameName
#arg[4] ASignalName
#arg[5] AValue
tscom_flexray_rbs_get_signal_value_by_element = dll.tscom_flexray_rbs_get_signal_value_by_element
tscom_flexray_rbs_get_signal_value_by_element.restype = s32
tscom_flexray_rbs_get_signal_value_by_element.argtypes = [s32,pchar,pchar,pchar,pchar,POINTER(double)]

#arg[0] ASymbolAddress
#arg[1] AValue
tscom_flexray_rbs_get_signal_value_by_address = dll.tscom_flexray_rbs_get_signal_value_by_address
tscom_flexray_rbs_get_signal_value_by_address.restype = s32
tscom_flexray_rbs_get_signal_value_by_address.argtypes = [pchar,POINTER(double)]

#arg[0] AIdxChn
#arg[1] AClusterName
#arg[2] AECUName
#arg[3] AFrameName
#arg[4] ASignalName
#arg[5] AValue
tscom_flexray_rbs_set_signal_value_by_element = dll.tscom_flexray_rbs_set_signal_value_by_element
tscom_flexray_rbs_set_signal_value_by_element.restype = s32
tscom_flexray_rbs_set_signal_value_by_element.argtypes = [s32,pchar,pchar,pchar,pchar,double]

#arg[0] ASymbolAddress
#arg[1] AValue
tscom_flexray_rbs_set_signal_value_by_address = dll.tscom_flexray_rbs_set_signal_value_by_address
tscom_flexray_rbs_set_signal_value_by_address.restype = s32
tscom_flexray_rbs_set_signal_value_by_address.argtypes = [pchar,double]

#arg[0] AEnable
tscom_flexray_rbs_enable = dll.tscom_flexray_rbs_enable
tscom_flexray_rbs_enable.restype = s32
tscom_flexray_rbs_enable.argtypes = [cbool]

tscom_flexray_rbs_batch_set_start = dll.tscom_flexray_rbs_batch_set_start
tscom_flexray_rbs_batch_set_start.restype = s32
tscom_flexray_rbs_batch_set_start.argtypes = []

tscom_flexray_rbs_batch_set_end = dll.tscom_flexray_rbs_batch_set_end
tscom_flexray_rbs_batch_set_end.restype = s32
tscom_flexray_rbs_batch_set_end.argtypes = []

#arg[0] AAddr
#arg[1] AValue
tscom_flexray_rbs_batch_set_signal = dll.tscom_flexray_rbs_batch_set_signal
tscom_flexray_rbs_batch_set_signal.restype = s32
tscom_flexray_rbs_batch_set_signal.argtypes = [pchar,double]

#arg[0] AIdxChn
#arg[1] AIsTx
#arg[2] AClusterName
#arg[3] AECUName
#arg[4] AFrameName
tscom_flexray_rbs_set_frame_direction = dll.tscom_flexray_rbs_set_frame_direction
tscom_flexray_rbs_set_frame_direction.restype = s32
tscom_flexray_rbs_set_frame_direction.argtypes = [s32,cbool,pchar,pchar,pchar]

#arg[0] ASymbolAddress
tscom_flexray_rbs_set_normal_signal = dll.tscom_flexray_rbs_set_normal_signal
tscom_flexray_rbs_set_normal_signal.restype = s32
tscom_flexray_rbs_set_normal_signal.argtypes = [pchar]

#arg[0] ASymbolAddress
tscom_flexray_rbs_set_rc_signal = dll.tscom_flexray_rbs_set_rc_signal
tscom_flexray_rbs_set_rc_signal.restype = s32
tscom_flexray_rbs_set_rc_signal.argtypes = [pchar]

#arg[0] ASymbolAddress
#arg[1] ALowerLimit
#arg[2] AUpperLimit
tscom_flexray_rbs_set_rc_signal_with_limit = dll.tscom_flexray_rbs_set_rc_signal_with_limit
tscom_flexray_rbs_set_rc_signal_with_limit.restype = s32
tscom_flexray_rbs_set_rc_signal_with_limit.argtypes = [pchar,s32,s32]

#arg[0] ASymbolAddress
#arg[1] AAlgorithmName
#arg[2] AIdxByteStart
#arg[3] AByteCount
tscom_flexray_rbs_set_crc_signal = dll.tscom_flexray_rbs_set_crc_signal
tscom_flexray_rbs_set_crc_signal.restype = s32
tscom_flexray_rbs_set_crc_signal.argtypes = [pchar,pchar,s32,s32]

#arg[0] AFlexRaySignal
#arg[1] AData
#arg[2] AValue
tscom_flexray_set_signal_value_in_raw_frame = dll.tscom_flexray_set_signal_value_in_raw_frame
tscom_flexray_set_signal_value_in_raw_frame.restype = s32
tscom_flexray_set_signal_value_in_raw_frame.argtypes = [PMPFlexRaySignal,pu8,double]

#arg[0] AFlexRaySignal
#arg[1] AData
tscom_flexray_get_signal_value_in_raw_frame = dll.tscom_flexray_get_signal_value_in_raw_frame
tscom_flexray_get_signal_value_in_raw_frame.restype = double
tscom_flexray_get_signal_value_in_raw_frame.argtypes = [PMPFlexRaySignal,pu8]

#arg[0] ASignalAddress
#arg[1] ASignalDef
tscom_flexray_get_signal_definition = dll.tscom_flexray_get_signal_definition
tscom_flexray_get_signal_definition.restype = s32
tscom_flexray_get_signal_definition.argtypes = [pchar,PMPFlexRaySignal]

#arg[0] AIdxChn
#arg[1] AControllerConfig
#arg[2] AFrameLengthArray
#arg[3] AFrameNum
#arg[4] AFrameTrigger
#arg[5] AFrameTriggerNum
#arg[6] ATimeoutMs
tsflexray_set_controller_frametrigger = dll.tsflexray_set_controller_frametrigger
tsflexray_set_controller_frametrigger.restype = s32
tsflexray_set_controller_frametrigger.argtypes = [s32,PLIBFlexray_controller_config,ps32,s32,PLIBTrigger_def,s32,s32]

#arg[0] AIdxChn
#arg[1] AControllerConfig
#arg[2] ATimeoutMs
tsflexray_set_controller = dll.tsflexray_set_controller
tsflexray_set_controller.restype = s32
tsflexray_set_controller.argtypes = [s32,PLIBFlexray_controller_config,s32]

#arg[0] AIdxChn
#arg[1] AFrameLengthArray
#arg[2] AFrameNum
#arg[3] AFrameTrigger
#arg[4] AFrameTriggerNum
#arg[5] ATimeoutMs
tsflexray_set_frametrigger = dll.tsflexray_set_frametrigger
tsflexray_set_frametrigger.restype = s32
tsflexray_set_frametrigger.argtypes = [s32,ps32,s32,PLIBTrigger_def,s32,s32]

#arg[0] AChnIdx
#arg[1] AAction
#arg[2] AWriteBuffer
#arg[3] AWriteBufferSize
#arg[4] AReadBuffer
#arg[5] AReadBufferSize
#arg[6] ATimeoutMs
tsflexray_cmdreq = dll.tsflexray_cmdreq
tsflexray_cmdreq.restype = s32
tsflexray_cmdreq.argtypes = [s32,s32,pu8,s32,pu8,ps32,s32]

#arg[0] AIdxChn
#arg[1] AData
#arg[2] ATimeoutMs
tsflexray_transmit_sync = dll.tsflexray_transmit_sync
tsflexray_transmit_sync.restype = s32
tsflexray_transmit_sync.argtypes = [s32,PLIBFlexRay,s32]

#arg[0] AIdxChn
#arg[1] AData
tsflexray_transmit_async = dll.tsflexray_transmit_async
tsflexray_transmit_async.restype = s32
tsflexray_transmit_async.argtypes = [s32,PLIBFlexRay]

#arg[0] AIdxChn
#arg[1] ATimeoutMs
tsflexray_start_net = dll.tsflexray_start_net
tsflexray_start_net.restype = s32
tsflexray_start_net.argtypes = [s32,s32]

#arg[0] AIdxChn
#arg[1] ATimeoutMs
tsflexray_stop_net = dll.tsflexray_stop_net
tsflexray_stop_net.restype = s32
tsflexray_stop_net.argtypes = [s32,s32]

#arg[0] AIdxChn
#arg[1] ATimeoutMs
tsflexray_wakeup_pattern = dll.tsflexray_wakeup_pattern
tsflexray_wakeup_pattern.restype = s32
tsflexray_wakeup_pattern.argtypes = [s32,s32]

#arg[0] AIdxChn
#arg[1] AConfig
#arg[2] ATimeoutMs
tsapp_config_ethernet_channel = dll.tsapp_config_ethernet_channel
tsapp_config_ethernet_channel.restype = s32
tsapp_config_ethernet_channel.argtypes = [s32,PLIBEth_CMD_config,s32]

#arg[0] AIdxChn
#arg[1] AOpen
tsapp_ethernet_channel_compress_mode = dll.tsapp_ethernet_channel_compress_mode
tsapp_ethernet_channel_compress_mode.restype = s32
tsapp_ethernet_channel_compress_mode.argtypes = [s32,cbool]

#arg[0] AEthernetHeader
#arg[1] ATimeoutMS
tsapp_transmit_ethernet_sync = dll.tsapp_transmit_ethernet_sync
tsapp_transmit_ethernet_sync.restype = s32
tsapp_transmit_ethernet_sync.argtypes = [PLIBEthernetHeader,s32]

#arg[0] AEthernetHeader
tsapp_transmit_ethernet_async = dll.tsapp_transmit_ethernet_async
tsapp_transmit_ethernet_async.restype = s32
tsapp_transmit_ethernet_async.argtypes = [PLIBEthernetHeader]

#arg[0] AObj
#arg[1] AEvent
tsapp_register_event_ethernet = dll.tsapp_register_event_ethernet
tsapp_register_event_ethernet.restype = s32
tsapp_register_event_ethernet.argtypes = [ps32,TEthernetQueueEvent_Win32]

#arg[0] AObj
#arg[1] AEvent
tsapp_unregister_event_ethernet = dll.tsapp_unregister_event_ethernet
tsapp_unregister_event_ethernet.restype = s32
tsapp_unregister_event_ethernet.argtypes = [ps32,TEthernetQueueEvent_Win32]

#arg[0] AObj
tsapp_unregister_events_ethernet = dll.tsapp_unregister_events_ethernet
tsapp_unregister_events_ethernet.restype = s32
tsapp_unregister_events_ethernet.argtypes = [ps32]

#arg[0] AObj
#arg[1] AEvent
tsapp_register_pretx_event_ethernet = dll.tsapp_register_pretx_event_ethernet
tsapp_register_pretx_event_ethernet.restype = s32
tsapp_register_pretx_event_ethernet.argtypes = [ps32,TEthernetQueueEvent_Win32]

#arg[0] AObj
#arg[1] AEvent
tsapp_unregister_pretx_event_ethernet = dll.tsapp_unregister_pretx_event_ethernet
tsapp_unregister_pretx_event_ethernet.restype = s32
tsapp_unregister_pretx_event_ethernet.argtypes = [ps32,TEthernetQueueEvent_Win32]

#arg[0] AObj
tsapp_unregister_pretx_events_ethernet = dll.tsapp_unregister_pretx_events_ethernet
tsapp_unregister_pretx_events_ethernet.restype = s32
tsapp_unregister_pretx_events_ethernet.argtypes = [ps32]

#arg[0] AChnIdx
tslin_clear_schedule_tables = dll.tslin_clear_schedule_tables
tslin_clear_schedule_tables.restype = s32
tslin_clear_schedule_tables.argtypes = [s32]

#arg[0] AChnIdx
tslin_switch_runtime_schedule_table = dll.tslin_switch_runtime_schedule_table
tslin_switch_runtime_schedule_table.restype = s32
tslin_switch_runtime_schedule_table.argtypes = [s32]

#arg[0] AChnIdx
tslin_switch_idle_schedule_table = dll.tslin_switch_idle_schedule_table
tslin_switch_idle_schedule_table.restype = s32
tslin_switch_idle_schedule_table.argtypes = [s32]

#arg[0] AChnIdx
#arg[1] ASchIndex
tslin_switch_normal_schedule_table = dll.tslin_switch_normal_schedule_table
tslin_switch_normal_schedule_table.restype = s32
tslin_switch_normal_schedule_table.argtypes = [s32,s32]

#arg[0] AChnIdx
tslin_stop_lin_channel = dll.tslin_stop_lin_channel
tslin_stop_lin_channel.restype = s32
tslin_stop_lin_channel.argtypes = [s32]

#arg[0] AChnIdx
tslin_start_lin_channel = dll.tslin_start_lin_channel
tslin_start_lin_channel.restype = s32
tslin_start_lin_channel.argtypes = [s32]

#arg[0] AChnIdx
#arg[1] AFunctionType
tslin_set_node_functiontype = dll.tslin_set_node_functiontype
tslin_set_node_functiontype.restype = s32
tslin_set_node_functiontype.argtypes = [s32,TLINNodeType]

#arg[0] AChnIdx
tslin_batch_set_schedule_start = dll.tslin_batch_set_schedule_start
tslin_batch_set_schedule_start.restype = s32
tslin_batch_set_schedule_start.argtypes = [s32]

#arg[0] AChnIdx
#arg[1] ALINData
#arg[2] ADelayMs
tslin_batch_add_schedule_frame = dll.tslin_batch_add_schedule_frame
tslin_batch_add_schedule_frame.restype = s32
tslin_batch_add_schedule_frame.argtypes = [s32,PLIBLIN,s32]

#arg[0] AChnIdx
tslin_batch_set_schedule_end = dll.tslin_batch_set_schedule_end
tslin_batch_set_schedule_end.restype = s32
tslin_batch_set_schedule_end.argtypes = [s32]

#arg[0] AChnIdx
#arg[1] ANAD
#arg[2] AData
#arg[3] ADataNum
#arg[4] ATimeoutMs
tstp_lin_master_request = dll.tstp_lin_master_request
tstp_lin_master_request.restype = s32
tstp_lin_master_request.argtypes = [s32,u8,pu8,s32,s32]

#arg[0] AChnIdx
#arg[1] AData
tstp_lin_master_request_intervalms = dll.tstp_lin_master_request_intervalms
tstp_lin_master_request_intervalms.restype = s32
tstp_lin_master_request_intervalms.argtypes = [s32,u16]

#arg[0] AChnIdx
tstp_lin_reset = dll.tstp_lin_reset
tstp_lin_reset.restype = s32
tstp_lin_reset.argtypes = [s32]

#arg[0] AChnIdx
#arg[1] AData
tstp_lin_slave_response_intervalms = dll.tstp_lin_slave_response_intervalms
tstp_lin_slave_response_intervalms.restype = s32
tstp_lin_slave_response_intervalms.argtypes = [s32,u16]

#arg[0] AChnIdx
#arg[1] AReqIntervalMs
#arg[2] AResIntervalMs
#arg[3] AResRetryTime
tstp_lin_tp_para_default = dll.tstp_lin_tp_para_default
tstp_lin_tp_para_default.restype = s32
tstp_lin_tp_para_default.argtypes = [s32,u16,u16,u16]

#arg[0] AChnIdx
#arg[1] AReqIntervalMs
#arg[2] AResIntervalMs
#arg[3] AResRetryTime
tstp_lin_tp_para_special = dll.tstp_lin_tp_para_special
tstp_lin_tp_para_special.restype = s32
tstp_lin_tp_para_special.argtypes = [s32,u16,u16,u16]

#arg[0] AChnIdx
#arg[1] ANAD
#arg[2] AId
#arg[3] AResNAD
#arg[4] AResData
#arg[5] AResDataNum
#arg[6] ATimeoutMS
tsdiag_lin_read_data_by_identifier = dll.tsdiag_lin_read_data_by_identifier
tsdiag_lin_read_data_by_identifier.restype = s32
tsdiag_lin_read_data_by_identifier.argtypes = [s32,u8,u16,pu8,pu8,psize_t,s32]

#arg[0] AChnIdx
#arg[1] AReqNAD
#arg[2] AID
#arg[3] AReqData
#arg[4] AReqDataNum
#arg[5] AResNAD
#arg[6] AResData
#arg[7] AResDataNum
#arg[8] ATimeoutMS
tsdiag_lin_write_data_by_identifier = dll.tsdiag_lin_write_data_by_identifier
tsdiag_lin_write_data_by_identifier.restype = size_t
tsdiag_lin_write_data_by_identifier.argtypes = [s32,u8,u16,pu8,size_t,pu8,pu8,psize_t,s32]

#arg[0] AChnIdx
#arg[1] ANAD
#arg[2] ANewSession
#arg[3] ATimeoutMS
tsdiag_lin_session_control = dll.tsdiag_lin_session_control
tsdiag_lin_session_control.restype = size_t
tsdiag_lin_session_control.argtypes = [s32,u8,u8,s32]

#arg[0] AChnIdx
#arg[1] ANAD
#arg[2] ATimeoutMS
tsdiag_lin_fault_memory_read = dll.tsdiag_lin_fault_memory_read
tsdiag_lin_fault_memory_read.restype = size_t
tsdiag_lin_fault_memory_read.argtypes = [s32,u8,s32]

#arg[0] AChnIdx
#arg[1] ANAD
#arg[2] ATimeoutMS
tsdiag_lin_fault_memory_clear = dll.tsdiag_lin_fault_memory_clear
tsdiag_lin_fault_memory_clear.restype = size_t
tsdiag_lin_fault_memory_clear.argtypes = [s32,u8,s32]

#arg[0] pDiagModuleIndex
#arg[1] AChnIndex
#arg[2] ASupportFDCAN
#arg[3] AMaxDLC
#arg[4] ARequestID
#arg[5] ARequestIDIsStd
#arg[6] AResponseID
#arg[7] AResponseIDIsStd
#arg[8] AFunctionID
#arg[9] AFunctionIDIsStd
tsdiag_can_create = dll.tsdiag_can_create
tsdiag_can_create.restype = s32
tsdiag_can_create.argtypes = [ps32,s32,u8,u8,u32,cbool,u32,cbool,u32,cbool]

#arg[0] ADiagModuleIndex
tsdiag_can_delete = dll.tsdiag_can_delete
tsdiag_can_delete.restype = s32
tsdiag_can_delete.argtypes = [s32]

#arg[0] ADiagModuleIndex
#arg[1] AChnIndex
tsdiag_set_channel = dll.tsdiag_set_channel
tsdiag_set_channel.restype = s32
tsdiag_set_channel.argtypes = [s32,s32]

#arg[0] ADiagModuleIndex
#arg[1] AFDMode
#arg[2] ASupportBRS
#arg[3] AMaxLength
tsdiag_set_fdmode = dll.tsdiag_set_fdmode
tsdiag_set_fdmode.restype = s32
tsdiag_set_fdmode.argtypes = [s32,cbool,cbool,s32]

#arg[0] ADiagModuleIndex
#arg[1] ARequestID
#arg[2] AIsStandard
tsdiag_set_request_id = dll.tsdiag_set_request_id
tsdiag_set_request_id.restype = s32
tsdiag_set_request_id.argtypes = [s32,s32,cbool]

#arg[0] ADiagModuleIndex
#arg[1] ARequestID
#arg[2] AIsStandard
tsdiag_set_response_id = dll.tsdiag_set_response_id
tsdiag_set_response_id.restype = s32
tsdiag_set_response_id.argtypes = [s32,s32,cbool]

#arg[0] ADiagModuleIndex
#arg[1] ARequestID
#arg[2] AIsStandard
tsdiag_set_function_id = dll.tsdiag_set_function_id
tsdiag_set_function_id.restype = s32
tsdiag_set_function_id.argtypes = [s32,s32,cbool]

#arg[0] ADiagModuleIndex
#arg[1] ASTMin
tsdiag_set_stmin = dll.tsdiag_set_stmin
tsdiag_set_stmin.restype = s32
tsdiag_set_stmin.argtypes = [s32,s32]

#arg[0] ADiagModuleIndex
#arg[1] ABlockSize
tsdiag_set_blocksize = dll.tsdiag_set_blocksize
tsdiag_set_blocksize.restype = s32
tsdiag_set_blocksize.argtypes = [s32,s32]

#arg[0] ADiagModuleIndex
#arg[1] AMaxLength
tsdiag_set_maxlength = dll.tsdiag_set_maxlength
tsdiag_set_maxlength.restype = s32
tsdiag_set_maxlength.argtypes = [s32,s32]

#arg[0] ADiagModuleIndex
#arg[1] AFCDelay
tsdiag_set_fcdelay = dll.tsdiag_set_fcdelay
tsdiag_set_fcdelay.restype = s32
tsdiag_set_fcdelay.argtypes = [s32,s32]

#arg[0] ADiagModuleIndex
#arg[1] AFilledByte
tsdiag_set_filled_byte = dll.tsdiag_set_filled_byte
tsdiag_set_filled_byte.restype = s32
tsdiag_set_filled_byte.argtypes = [s32,u8]

#arg[0] ADiagModuleIndex
#arg[1] ATimeMs
tsdiag_set_p2_timeout = dll.tsdiag_set_p2_timeout
tsdiag_set_p2_timeout.restype = s32
tsdiag_set_p2_timeout.argtypes = [s32,s32]

#arg[0] ADiagModuleIndex
#arg[1] ATimeMs
tsdiag_set_p2_extended = dll.tsdiag_set_p2_extended
tsdiag_set_p2_extended.restype = s32
tsdiag_set_p2_extended.argtypes = [s32,s32]

#arg[0] ADiagModuleIndex
#arg[1] ATimeMs
tsdiag_set_s3_servertime = dll.tsdiag_set_s3_servertime
tsdiag_set_s3_servertime.restype = s32
tsdiag_set_s3_servertime.argtypes = [s32,s32]

#arg[0] ADiagModuleIndex
#arg[1] ATimeMs
tsdiag_set_s3_clienttime = dll.tsdiag_set_s3_clienttime
tsdiag_set_s3_clienttime.restype = s32
tsdiag_set_s3_clienttime.argtypes = [s32,s32]

#arg[0] ADiagModuleIndex
#arg[1] AReqDataArray
#arg[2] AReqDataSize
tstp_can_send_functional = dll.tstp_can_send_functional
tstp_can_send_functional.restype = s32
tstp_can_send_functional.argtypes = [s32,pu8,s32]

#arg[0] ADiagModuleIndex
#arg[1] AReqDataArray
#arg[2] AReqDataSize
tstp_can_send_request = dll.tstp_can_send_request
tstp_can_send_request.restype = s32
tstp_can_send_request.argtypes = [s32,pu8,s32]

#arg[0] ADiagModuleIndex
#arg[1] AReqDataArray
#arg[2] AReqDataSize
#arg[3] AResponseDataArray
#arg[4] AResponseDataSize
tstp_can_request_and_get_response = dll.tstp_can_request_and_get_response
tstp_can_request_and_get_response.restype = s32
tstp_can_request_and_get_response.argtypes = [s32,pu8,s32,pu8,ps32]

#arg[0] ADiagModuleIndex
#arg[1] AReqDataArray
#arg[2] AReqDataSize
#arg[3] AResponseDataArray
#arg[4] AResponseDataSize
tstp_can_request_and_get_response_functional = dll.tstp_can_request_and_get_response_functional
tstp_can_request_and_get_response_functional.restype = s32
tstp_can_request_and_get_response_functional.argtypes = [s32,pu8,s32,pu8,ps32]

#arg[0] ADiagModuleIndex
#arg[1] ATxcompleted
tstp_can_register_tx_completed_recall = dll.tstp_can_register_tx_completed_recall
tstp_can_register_tx_completed_recall.restype = s32
tstp_can_register_tx_completed_recall.argtypes = [s32,N_USData_TranslateCompleted_Recall]

#arg[0] ADiagModuleIndex
#arg[1] ARxcompleted
tstp_can_register_rx_completed_recall = dll.tstp_can_register_rx_completed_recall
tstp_can_register_rx_completed_recall.restype = s32
tstp_can_register_rx_completed_recall.argtypes = [s32,N_USData_TranslateCompleted_Recall]

#arg[0] ADiagModuleIndex
#arg[1] ATxcompleted
tstp_can_register_tx_completed_recall_internal = dll.tstp_can_register_tx_completed_recall_internal
tstp_can_register_tx_completed_recall_internal.restype = s32
tstp_can_register_tx_completed_recall_internal.argtypes = [s32,N_USData_TranslateCompleted_Recall_Obj]

#arg[0] ADiagModuleIndex
#arg[1] ARxcompleted
tstp_can_register_rx_completed_recall_internal = dll.tstp_can_register_rx_completed_recall_internal
tstp_can_register_rx_completed_recall_internal.restype = s32
tstp_can_register_rx_completed_recall_internal.argtypes = [s32,N_USData_TranslateCompleted_Recall_Obj]

#arg[0] ADiagModuleIndex
#arg[1] ASubSession
tsdiag_can_session_control = dll.tsdiag_can_session_control
tsdiag_can_session_control.restype = s32
tsdiag_can_session_control.argtypes = [s32,u8]

#arg[0] ADiagModuleIndex
#arg[1] ARoutineControlType
#arg[2] ARoutintID
tsdiag_can_routine_control = dll.tsdiag_can_routine_control
tsdiag_can_routine_control.restype = s32
tsdiag_can_routine_control.argtypes = [s32,u8,u16]

#arg[0] ADiagModuleIndex
#arg[1] AControlType
tsdiag_can_communication_control = dll.tsdiag_can_communication_control
tsdiag_can_communication_control.restype = s32
tsdiag_can_communication_control.argtypes = [s32,u8]

#arg[0] ADiagModuleIndex
#arg[1] ALevel
#arg[2] ARecSeed
#arg[3] ARecSeedSize
tsdiag_can_security_access_request_seed = dll.tsdiag_can_security_access_request_seed
tsdiag_can_security_access_request_seed.restype = s32
tsdiag_can_security_access_request_seed.argtypes = [s32,s32,pu8,ps32]

#arg[0] ADiagModuleIndex
#arg[1] ALevel
#arg[2] AKeyValue
#arg[3] AKeySize
tsdiag_can_security_access_send_key = dll.tsdiag_can_security_access_send_key
tsdiag_can_security_access_send_key.restype = s32
tsdiag_can_security_access_send_key.argtypes = [s32,s32,pu8,s32]

#arg[0] ADiagModuleIndex
#arg[1] AMemAddr
#arg[2] AMemSize
tsdiag_can_request_download = dll.tsdiag_can_request_download
tsdiag_can_request_download.restype = s32
tsdiag_can_request_download.argtypes = [s32,u32,u32]

#arg[0] ADiagModuleIndex
#arg[1] AMemAddr
#arg[2] AMemSize
tsdiag_can_request_upload = dll.tsdiag_can_request_upload
tsdiag_can_request_upload.restype = s32
tsdiag_can_request_upload.argtypes = [s32,u32,u32]

#arg[0] ADiagModuleIndex
#arg[1] ASourceDatas
#arg[2] ADataSize
#arg[3] AReqCase
tsdiag_can_transfer_data = dll.tsdiag_can_transfer_data
tsdiag_can_transfer_data.restype = s32
tsdiag_can_transfer_data.argtypes = [s32,pu8,s32,s32]

#arg[0] ADiagModuleIndex
tsdiag_can_request_transfer_exit = dll.tsdiag_can_request_transfer_exit
tsdiag_can_request_transfer_exit.restype = s32
tsdiag_can_request_transfer_exit.argtypes = [s32]

#arg[0] ADiagModuleIndex
#arg[1] ADataIdentifier
#arg[2] AWriteData
#arg[3] AWriteDataSize
tsdiag_can_write_data_by_identifier = dll.tsdiag_can_write_data_by_identifier
tsdiag_can_write_data_by_identifier.restype = s32
tsdiag_can_write_data_by_identifier.argtypes = [s32,u16,pu8,s32]

#arg[0] ADiagModuleIndex
#arg[1] ADataIdentifier
#arg[2] AReturnArray
#arg[3] AReturnArraySize
tsdiag_can_read_data_by_identifier = dll.tsdiag_can_read_data_by_identifier
tsdiag_can_read_data_by_identifier.restype = s32
tsdiag_can_read_data_by_identifier.argtypes = [s32,u16,pu8,ps32]

#arg[0] AChnIdx
#arg[1] AFileIndex
#arg[2] ATimeoutMS
tslog_logger_delete_file = dll.tslog_logger_delete_file
tslog_logger_delete_file.restype = s32
tslog_logger_delete_file.argtypes = [s32,s32,s32]

#arg[0] AChnIdx
#arg[1] AFileIndex
#arg[2] ABlfFileName
#arg[3] AStartTimeUs
#arg[4] AMaxSize
#arg[5] AProgress
#arg[6] AYear
#arg[7] AMonth
#arg[8] ADay
#arg[9] AHour
#arg[10] AMinute
#arg[11] ASecond
#arg[12] AMinisecond
#arg[13] ATimeoutMS
tslog_logger_start_export_blf_file = dll.tslog_logger_start_export_blf_file
tslog_logger_start_export_blf_file.restype = s32
tslog_logger_start_export_blf_file.argtypes = [s32,s32,pchar,u64,s32,pdouble,u16,u16,u16,u16,u16,u16,u16,s32]

#arg[0] AChnIdx
#arg[1] ATimeoutMS
tslog_logger_abort_export_blf_file = dll.tslog_logger_abort_export_blf_file
tslog_logger_abort_export_blf_file.restype = s32
tslog_logger_abort_export_blf_file.argtypes = [s32,s32]

#arg[0] AChnIdx
#arg[1] AFileIndex
#arg[2] AStartTimeUs
#arg[3] AMaxSize
#arg[4] ATimeoutMS
tslog_logger_start_online_replay = dll.tslog_logger_start_online_replay
tslog_logger_start_online_replay.restype = s32
tslog_logger_start_online_replay.argtypes = [s32,s32,u64,s32,s32]

#arg[0] AChnIdx
#arg[1] AFileIndex
#arg[2] AStartTimeUs
#arg[3] AMaxSize
#arg[4] ATimeoutMS
tslog_logger_start_offline_replay = dll.tslog_logger_start_offline_replay
tslog_logger_start_offline_replay.restype = s32
tslog_logger_start_offline_replay.argtypes = [s32,s32,u64,s32,s32]

#arg[0] AChnIdx
#arg[1] ATimeoutMS
tslog_logger_stop_replay = dll.tslog_logger_stop_replay
tslog_logger_stop_replay.restype = s32
tslog_logger_stop_replay.argtypes = [s32,s32]

#arg[0] AChnIdx
#arg[1] AMode
#arg[2] ATimeoutMS
tslog_logger_set_logger_mode = dll.tslog_logger_set_logger_mode
tslog_logger_set_logger_mode.restype = s32
tslog_logger_set_logger_mode.argtypes = [s32,u8,s32]

#arg[0] AChnIdx
#arg[1] AEnable
#arg[2] ATimeoutMS
tsapp_logger_enable_gps_module = dll.tsapp_logger_enable_gps_module
tsapp_logger_enable_gps_module.restype = s32
tsapp_logger_enable_gps_module.argtypes = [s32,s32,s32]

#arg[0] AChnIdx
#arg[1] AInitBaudrate
#arg[2] ATargetBaudrate
#arg[3] ASampleRate
#arg[4] ATimeoutMS
tsapp_reset_gps_module = dll.tsapp_reset_gps_module
tsapp_reset_gps_module.restype = s32
tsapp_reset_gps_module.argtypes = [s32,s32,s32,s32,s32]

#arg[0] AChnIdx
tsapp_unlock_camera_channel = dll.tsapp_unlock_camera_channel
tsapp_unlock_camera_channel.restype = s32
tsapp_unlock_camera_channel.argtypes = [s32]

#arg[0] x
rawsocket_htons = dll.rawsocket_htons
rawsocket_htons.restype = u16
rawsocket_htons.argtypes = [u16]

#arg[0] x
rawsocket_htonl = dll.rawsocket_htonl
rawsocket_htonl.restype = u32
rawsocket_htonl.argtypes = [u32]

#arg[0] cp
#arg[1] addr
rawsocket_aton = dll.rawsocket_aton
rawsocket_aton.restype = s32
rawsocket_aton.argtypes = [pchar,Pip4_addr_t]

#arg[0] addr
rawsocket_ntoa = dll.rawsocket_ntoa
rawsocket_ntoa.restype = pchar
rawsocket_ntoa.argtypes = [Pip4_addr_t]

#arg[0] cp
#arg[1] addr
rawsocket_aton6 = dll.rawsocket_aton6
rawsocket_aton6.restype = s32
rawsocket_aton6.argtypes = [pchar,Pip6_addr_t]

#arg[0] addr
rawsocket_ntoa6 = dll.rawsocket_ntoa6
rawsocket_ntoa6.restype = pchar
rawsocket_ntoa6.argtypes = [Pip6_addr_t]

#arg[0] af
#arg[1] src
#arg[2] dst
#arg[3] size
rawsocket_inet_ntop = dll.rawsocket_inet_ntop
rawsocket_inet_ntop.restype = pchar
rawsocket_inet_ntop.argtypes = [s32,ps32,pchar,u32]

#arg[0] af
#arg[1] src
#arg[2] dst
rawsocket_inet_pton = dll.rawsocket_inet_pton
rawsocket_inet_pton.restype = s32
rawsocket_inet_pton.argtypes = [s32,pchar,ps32]

#arg[0] ANetworkIndex
tssocket_initialize = dll.tssocket_initialize
tssocket_initialize.restype = s32
tssocket_initialize.argtypes = [s32]

#arg[0] ANetworkIndex
#arg[1] ALog
tssocket_initialize_verbose = dll.tssocket_initialize_verbose
tssocket_initialize_verbose.restype = s32
tssocket_initialize_verbose.argtypes = [s32,TLogDebuggingInfo_t]

#arg[0] ANetworkIndex
tssocket_finalize = dll.tssocket_finalize
tssocket_finalize.restype = s32
tssocket_finalize.argtypes = [s32]

#arg[0] ANetworkIndex
#arg[1] macaddr
#arg[2] vLan
#arg[3] ipaddr
#arg[4] netmask
#arg[5] gateway
#arg[6] mtu
tssocket_add_device = dll.tssocket_add_device
tssocket_add_device.restype = s32
tssocket_add_device.argtypes = [s32,pu8,pu16,Tip4_addr_t,Tip4_addr_t,Tip4_addr_t,u16]

#arg[0] ANetworkIndex
#arg[1] macaddr
#arg[2] vLan
#arg[3] ipaddr
tssocket_remove_device = dll.tssocket_remove_device
tssocket_remove_device.restype = s32
tssocket_remove_device.argtypes = [s32,pu8,pu16,Pip4_addr_t]

#arg[0] ANetworkIndex
#arg[1] macaddr
#arg[2] vlan
#arg[3] ipaddr
#arg[4] netmask
#arg[5] gateway
#arg[6] mtu
tssocket_add_device_ex = dll.tssocket_add_device_ex
tssocket_add_device_ex.restype = s32
tssocket_add_device_ex.argtypes = [s32,pchar,pchar,pchar,pchar,pchar,u16]

#arg[0] ANetworkIndex
#arg[1] mac
#arg[2] vlan
#arg[3] ipaddr
tssocket_remove_device_ex = dll.tssocket_remove_device_ex
tssocket_remove_device_ex.restype = s32
tssocket_remove_device_ex.argtypes = [s32,pchar,pchar,pchar]

#arg[0] ANetworkIndex
rawsocket_get_errno = dll.rawsocket_get_errno
rawsocket_get_errno.restype = s32
rawsocket_get_errno.argtypes = [s32]

#arg[0] ANetworkIndex
rawsocket_dhcp_start = dll.rawsocket_dhcp_start
rawsocket_dhcp_start.restype = s32
rawsocket_dhcp_start.argtypes = [s32]

#arg[0] ANetworkIndex
#arg[1] maxfdp1
#arg[2] readset
#arg[3] writeset
#arg[4] exceptset
#arg[5] timeout
rawsocket_select = dll.rawsocket_select
rawsocket_select.restype = s32
rawsocket_select.argtypes = [s32,s32,Pts_fd_set,Pts_fd_set,Pts_fd_set,Pts_timeval]

#arg[0] ANetworkIndex
#arg[1] fds
#arg[2] nfds
#arg[3] timeout
rawsocket_poll = dll.rawsocket_poll
rawsocket_poll.restype = s32
rawsocket_poll.argtypes = [s32,Pts_pollfd,size_t,s32]

#arg[0] ANetworkIndex
#arg[1] domain
#arg[2] atype
#arg[3] protocol
#arg[4] recv_cb
#arg[5] presend_cb
#arg[6] send_cb
rawsocket = dll.rawsocket
rawsocket.restype = s32
rawsocket.argtypes = [s32,s32,s32,s32,tosun_recv_callback,tosun_tcp_presend_callback,tosun_tcp_ack_callback]

#arg[0] s
#arg[1] addr
#arg[2] addrlen
rawsocket_accept = dll.rawsocket_accept
rawsocket_accept.restype = s32
rawsocket_accept.argtypes = [s32,Pts_sockaddr,pu32]

#arg[0] s
#arg[1] name
#arg[2] namelen
rawsocket_bind = dll.rawsocket_bind
rawsocket_bind.restype = s32
rawsocket_bind.argtypes = [s32,Pts_sockaddr,u32]

#arg[0] s
#arg[1] how
rawsocket_shutdown = dll.rawsocket_shutdown
rawsocket_shutdown.restype = s32
rawsocket_shutdown.argtypes = [s32,s32]

#arg[0] s
#arg[1] name
#arg[2] namelen
rawsocket_getpeername = dll.rawsocket_getpeername
rawsocket_getpeername.restype = s32
rawsocket_getpeername.argtypes = [s32,Pts_sockaddr,pu32]

#arg[0] s
#arg[1] name
#arg[2] namelen
rawsocket_getsockname = dll.rawsocket_getsockname
rawsocket_getsockname.restype = s32
rawsocket_getsockname.argtypes = [s32,Pts_sockaddr,pu32]

#arg[0] s
#arg[1] level
#arg[2] optname
#arg[3] optval
#arg[4] optlen
rawsocket_getsockopt = dll.rawsocket_getsockopt
rawsocket_getsockopt.restype = s32
rawsocket_getsockopt.argtypes = [s32,s32,s32,ps32,pu32]

#arg[0] s
#arg[1] level
#arg[2] optname
#arg[3] optval
#arg[4] optlen
rawsocket_setsockopt = dll.rawsocket_setsockopt
rawsocket_setsockopt.restype = s32
rawsocket_setsockopt.argtypes = [s32,s32,s32,ps32,u32]

#arg[0] s
rawsocket_close = dll.rawsocket_close
rawsocket_close.restype = s32
rawsocket_close.argtypes = [s32]

#arg[0] s
#arg[1] AForceExitTimeWait
rawsocket_close_v2 = dll.rawsocket_close_v2
rawsocket_close_v2.restype = s32
rawsocket_close_v2.argtypes = [s32,s32]

#arg[0] s
#arg[1] name
#arg[2] namelen
rawsocket_connect = dll.rawsocket_connect
rawsocket_connect.restype = s32
rawsocket_connect.argtypes = [s32,Pts_sockaddr,u32]

#arg[0] s
#arg[1] backlog
rawsocket_listen = dll.rawsocket_listen
rawsocket_listen.restype = s32
rawsocket_listen.argtypes = [s32,s32]

#arg[0] s
#arg[1] mem
#arg[2] len
#arg[3] flags
rawsocket_recv = dll.rawsocket_recv
rawsocket_recv.restype = size_t
rawsocket_recv.argtypes = [s32,ps32,size_t,s32]

#arg[0] s
#arg[1] mem
#arg[2] len
rawsocket_read = dll.rawsocket_read
rawsocket_read.restype = size_t
rawsocket_read.argtypes = [s32,ps32,size_t]

#arg[0] s
#arg[1] iov
#arg[2] iovcnt
rawsocket_readv = dll.rawsocket_readv
rawsocket_readv.restype = size_t
rawsocket_readv.argtypes = [s32,Pts_iovec,s32]

#arg[0] s
#arg[1] mem
#arg[2] len
#arg[3] flags
#arg[4] from
#arg[5] fromlen
rawsocket_recvfrom = dll.rawsocket_recvfrom
rawsocket_recvfrom.restype = size_t
rawsocket_recvfrom.argtypes = [s32,ps32,size_t,s32,Pts_sockaddr,pu32]

#arg[0] s
#arg[1] Amessage
#arg[2] flags
rawsocket_recvmsg = dll.rawsocket_recvmsg
rawsocket_recvmsg.restype = size_t
rawsocket_recvmsg.argtypes = [s32,Pts_msghdr,s32]

#arg[0] s
#arg[1] dataptr
#arg[2] size
#arg[3] flags
rawsocket_send = dll.rawsocket_send
rawsocket_send.restype = size_t
rawsocket_send.argtypes = [s32,ps32,size_t,s32]

#arg[0] s
#arg[1] Amessage
#arg[2] flags
rawsocket_sendmsg = dll.rawsocket_sendmsg
rawsocket_sendmsg.restype = size_t
rawsocket_sendmsg.argtypes = [s32,Pts_msghdr,s32]

#arg[0] s
#arg[1] dataptr
#arg[2] size
#arg[3] flags
#arg[4] ato
#arg[5] tolen
rawsocket_sendto = dll.rawsocket_sendto
rawsocket_sendto.restype = size_t
rawsocket_sendto.argtypes = [s32,ps32,size_t,s32,Pts_sockaddr,u32]

#arg[0] s
#arg[1] dataptr
#arg[2] size
rawsocket_write = dll.rawsocket_write
rawsocket_write.restype = size_t
rawsocket_write.argtypes = [s32,ps32,size_t]

#arg[0] s
#arg[1] iov
#arg[2] iovcnt
rawsocket_writev = dll.rawsocket_writev
rawsocket_writev.restype = size_t
rawsocket_writev.argtypes = [s32,Pts_iovec,s32]

#arg[0] s
#arg[1] cmd
#arg[2] argp
rawsocket_ioctl = dll.rawsocket_ioctl
rawsocket_ioctl.restype = s32
rawsocket_ioctl.argtypes = [s32,s32,ps32]

#arg[0] s
#arg[1] cmd
#arg[2] val
rawsocket_fcntl = dll.rawsocket_fcntl
rawsocket_fcntl.restype = s32
rawsocket_fcntl.argtypes = [s32,s32,s32]

#arg[0] ANetworkIndex
#arg[1] AIPEndPoint
#arg[2] ASocketHandle
tssocket_tcp = dll.tssocket_tcp
tssocket_tcp.restype = s32
tssocket_tcp.argtypes = [s32,pchar,ps32]

#arg[0] s
tssocket_tcp_start_listen = dll.tssocket_tcp_start_listen
tssocket_tcp_start_listen.restype = s32
tssocket_tcp_start_listen.argtypes = [s32]

#arg[0] s
tssocket_tcp_start_receive = dll.tssocket_tcp_start_receive
tssocket_tcp_start_receive.restype = s32
tssocket_tcp_start_receive.argtypes = [s32]

#arg[0] s
#arg[1] AIPEndPoint
tssocket_tcp_connect = dll.tssocket_tcp_connect
tssocket_tcp_connect.restype = s32
tssocket_tcp_connect.argtypes = [s32,pchar]

#arg[0] s
tssocket_tcp_close = dll.tssocket_tcp_close
tssocket_tcp_close.restype = s32
tssocket_tcp_close.argtypes = [s32]

#arg[0] s
#arg[1] AForceExitTimeWait
tssocket_tcp_close_v2 = dll.tssocket_tcp_close_v2
tssocket_tcp_close_v2.restype = s32
tssocket_tcp_close_v2.argtypes = [s32,s32]

#arg[0] s
#arg[1] AData
#arg[2] ASize
tssocket_tcp_send = dll.tssocket_tcp_send
tssocket_tcp_send.restype = s32
tssocket_tcp_send.argtypes = [s32,pu8,s32]

#arg[0] s
#arg[1] AIPEndPoint
#arg[2] AData
#arg[3] ASize
tssocket_tcp_sendto_client = dll.tssocket_tcp_sendto_client
tssocket_tcp_sendto_client.restype = s32
tssocket_tcp_sendto_client.argtypes = [s32,pchar,pu8,s32]

#arg[0] ANetworkIndex
#arg[1] AIPEndPoint
#arg[2] ASocketHandle
tssocket_udp = dll.tssocket_udp
tssocket_udp.restype = s32
tssocket_udp.argtypes = [s32,pchar,ps32]

#arg[0] s
tssocket_udp_start_receive = dll.tssocket_udp_start_receive
tssocket_udp_start_receive.restype = s32
tssocket_udp_start_receive.argtypes = [s32]

#arg[0] s
tssocket_udp_close = dll.tssocket_udp_close
tssocket_udp_close.restype = s32
tssocket_udp_close.argtypes = [s32]

#arg[0] s
#arg[1] AIPEndPoint
#arg[2] AData
#arg[3] ASize
tssocket_udp_sendto = dll.tssocket_udp_sendto
tssocket_udp_sendto.restype = s32
tssocket_udp_sendto.argtypes = [s32,pchar,pu8,s32]

#arg[0] s
#arg[1] AIPAddress
#arg[2] APort
#arg[3] AData
#arg[4] ASize
tssocket_udp_sendto_v2 = dll.tssocket_udp_sendto_v2
tssocket_udp_sendto_v2.restype = s32
tssocket_udp_sendto_v2.argtypes = [s32,u32,u16,pu8,s32]

#arg[0] s
#arg[1] AEvent
tssocket_register_tcp_listen_event = dll.tssocket_register_tcp_listen_event
tssocket_register_tcp_listen_event.restype = s32
tssocket_register_tcp_listen_event.argtypes = [s32,TSSocketListenEvent_Win32]

#arg[0] s
#arg[1] AEvent
tssocket_unregister_tcp_listen_event = dll.tssocket_unregister_tcp_listen_event
tssocket_unregister_tcp_listen_event.restype = s32
tssocket_unregister_tcp_listen_event.argtypes = [s32,TSSocketListenEvent_Win32]

#arg[0] s
tssocket_unregister_tcp_listen_events = dll.tssocket_unregister_tcp_listen_events
tssocket_unregister_tcp_listen_events.restype = s32
tssocket_unregister_tcp_listen_events.argtypes = [s32]

#arg[0] s
#arg[1] AEvent
tssocket_register_tcp_connect_event = dll.tssocket_register_tcp_connect_event
tssocket_register_tcp_connect_event.restype = s32
tssocket_register_tcp_connect_event.argtypes = [s32,TSSocketNotifyEvent_Win32]

#arg[0] s
#arg[1] AEvent
tssocket_unregister_tcp_connect_event = dll.tssocket_unregister_tcp_connect_event
tssocket_unregister_tcp_connect_event.restype = s32
tssocket_unregister_tcp_connect_event.argtypes = [s32,TSSocketNotifyEvent_Win32]

#arg[0] s
tssocket_unregister_tcp_connect_events = dll.tssocket_unregister_tcp_connect_events
tssocket_unregister_tcp_connect_events.restype = s32
tssocket_unregister_tcp_connect_events.argtypes = [s32]

#arg[0] s
#arg[1] AEvent
tssocket_register_tcp_receive_event = dll.tssocket_register_tcp_receive_event
tssocket_register_tcp_receive_event.restype = s32
tssocket_register_tcp_receive_event.argtypes = [s32,TSSocketReceiveEvent_Win32]

#arg[0] s
#arg[1] AEvent
tssocket_unregister_tcp_receive_event = dll.tssocket_unregister_tcp_receive_event
tssocket_unregister_tcp_receive_event.restype = s32
tssocket_unregister_tcp_receive_event.argtypes = [s32,TSSocketReceiveEvent_Win32]

#arg[0] s
tssocket_unregister_tcp_receive_events = dll.tssocket_unregister_tcp_receive_events
tssocket_unregister_tcp_receive_events.restype = s32
tssocket_unregister_tcp_receive_events.argtypes = [s32]

#arg[0] s
#arg[1] AEvent
tssocket_register_tcp_close_event = dll.tssocket_register_tcp_close_event
tssocket_register_tcp_close_event.restype = s32
tssocket_register_tcp_close_event.argtypes = [s32,TSSocketNotifyEvent_Win32]

#arg[0] s
#arg[1] AEvent
tssocket_unregister_tcp_close_event = dll.tssocket_unregister_tcp_close_event
tssocket_unregister_tcp_close_event.restype = s32
tssocket_unregister_tcp_close_event.argtypes = [s32,TSSocketNotifyEvent_Win32]

#arg[0] s
tssocket_unregister_tcp_close_events = dll.tssocket_unregister_tcp_close_events
tssocket_unregister_tcp_close_events.restype = s32
tssocket_unregister_tcp_close_events.argtypes = [s32]

#arg[0] s
#arg[1] AEvent
tssocket_register_tcp_send_event = dll.tssocket_register_tcp_send_event
tssocket_register_tcp_send_event.restype = s32
tssocket_register_tcp_send_event.argtypes = [s32,TSSocketTransmitEvent_Win32]

#arg[0] s
#arg[1] AEvent
tssocket_unregister_tcp_send_event = dll.tssocket_unregister_tcp_send_event
tssocket_unregister_tcp_send_event.restype = s32
tssocket_unregister_tcp_send_event.argtypes = [s32,TSSocketTransmitEvent_Win32]

#arg[0] s
tssocket_unregister_tcp_send_events = dll.tssocket_unregister_tcp_send_events
tssocket_unregister_tcp_send_events.restype = s32
tssocket_unregister_tcp_send_events.argtypes = [s32]

#arg[0] s
#arg[1] AEvent
tssocket_register_udp_receivefrom_event = dll.tssocket_register_udp_receivefrom_event
tssocket_register_udp_receivefrom_event.restype = s32
tssocket_register_udp_receivefrom_event.argtypes = [s32,TSSocketReceiveEvent_Win32]

#arg[0] s
#arg[1] AEvent
tssocket_unregister_udp_receivefrom_event = dll.tssocket_unregister_udp_receivefrom_event
tssocket_unregister_udp_receivefrom_event.restype = s32
tssocket_unregister_udp_receivefrom_event.argtypes = [s32,TSSocketReceiveEvent_Win32]

#arg[0] s
tssocket_unregister_udp_receivefrom_events = dll.tssocket_unregister_udp_receivefrom_events
tssocket_unregister_udp_receivefrom_events.restype = s32
tssocket_unregister_udp_receivefrom_events.argtypes = [s32]

#arg[0] s
#arg[1] AEvent
tssocket_register_udp_sendto_event = dll.tssocket_register_udp_sendto_event
tssocket_register_udp_sendto_event.restype = s32
tssocket_register_udp_sendto_event.argtypes = [s32,TSSocketTransmitEvent_Win32]

#arg[0] s
#arg[1] AEvent
tssocket_unregister_udp_sendto_event = dll.tssocket_unregister_udp_sendto_event
tssocket_unregister_udp_sendto_event.restype = s32
tssocket_unregister_udp_sendto_event.argtypes = [s32,TSSocketTransmitEvent_Win32]

#arg[0] s
tssocket_unregister_udp_sendto_events = dll.tssocket_unregister_udp_sendto_events
tssocket_unregister_udp_sendto_events.restype = s32
tssocket_unregister_udp_sendto_events.argtypes = [s32]

#arg[0] s
#arg[1] AEvent
tssocket_register_udp_receivefrom_eventv2 = dll.tssocket_register_udp_receivefrom_eventv2
tssocket_register_udp_receivefrom_eventv2.restype = s32
tssocket_register_udp_receivefrom_eventv2.argtypes = [s32,TSSocketReceiveEventV2_Win32]

#arg[0] s
#arg[1] AEvent
tssocket_unregister_udp_receivefrom_eventv2 = dll.tssocket_unregister_udp_receivefrom_eventv2
tssocket_unregister_udp_receivefrom_eventv2.restype = s32
tssocket_unregister_udp_receivefrom_eventv2.argtypes = [s32,TSSocketReceiveEventV2_Win32]

#arg[0] s
tssocket_unregister_udp_receivefrom_eventsv2 = dll.tssocket_unregister_udp_receivefrom_eventsv2
tssocket_unregister_udp_receivefrom_eventsv2.restype = s32
tssocket_unregister_udp_receivefrom_eventsv2.argtypes = [s32]

#arg[0] s
#arg[1] AEvent
tssocket_register_udp_receivefrom_eventv3 = dll.tssocket_register_udp_receivefrom_eventv3
tssocket_register_udp_receivefrom_eventv3.restype = s32
tssocket_register_udp_receivefrom_eventv3.argtypes = [s32,TSSocketReceiveEventV3_Win32]

#arg[0] s
#arg[1] AEvent
tssocket_unregister_udp_receivefrom_eventv3 = dll.tssocket_unregister_udp_receivefrom_eventv3
tssocket_unregister_udp_receivefrom_eventv3.restype = s32
tssocket_unregister_udp_receivefrom_eventv3.argtypes = [s32,TSSocketReceiveEventV3_Win32]

#arg[0] s
tssocket_unregister_udp_receivefrom_eventsv3 = dll.tssocket_unregister_udp_receivefrom_eventsv3
tssocket_unregister_udp_receivefrom_eventsv3.restype = s32
tssocket_unregister_udp_receivefrom_eventsv3.argtypes = [s32]

#arg[0] s
#arg[1] AEvent
tssocket_register_tcp_receive_eventv2 = dll.tssocket_register_tcp_receive_eventv2
tssocket_register_tcp_receive_eventv2.restype = s32
tssocket_register_tcp_receive_eventv2.argtypes = [s32,TSSocketReceiveEventV2_Win32]

#arg[0] s
#arg[1] AEvent
tssocket_unregister_tcp_receive_eventv2 = dll.tssocket_unregister_tcp_receive_eventv2
tssocket_unregister_tcp_receive_eventv2.restype = s32
tssocket_unregister_tcp_receive_eventv2.argtypes = [s32,TSSocketReceiveEventV2_Win32]

#arg[0] s
tssocket_unregister_tcp_receive_eventsv2 = dll.tssocket_unregister_tcp_receive_eventsv2
tssocket_unregister_tcp_receive_eventsv2.restype = s32
tssocket_unregister_tcp_receive_eventsv2.argtypes = [s32]

tsmp_reload_settings = dll.tsmp_reload_settings
tsmp_reload_settings.restype = s32
tsmp_reload_settings.argtypes = []

#arg[0] AMPFileName
#arg[1] ARunAfterLoad
tsmp_load = dll.tsmp_load
tsmp_load.restype = s32
tsmp_load.argtypes = [pchar,cbool]

#arg[0] AMPFileName
tsmp_unload = dll.tsmp_unload
tsmp_unload.restype = s32
tsmp_unload.argtypes = [pchar]

tsmp_unload_all = dll.tsmp_unload_all
tsmp_unload_all.restype = s32
tsmp_unload_all.argtypes = []

#arg[0] AMPFileName
tsmp_run = dll.tsmp_run
tsmp_run.restype = s32
tsmp_run.argtypes = [pchar]

#arg[0] AMPFileName
#arg[1] AIsRunning
tsmp_is_running = dll.tsmp_is_running
tsmp_is_running.restype = s32
tsmp_is_running.argtypes = [pchar,POINTER(cbool)]

#arg[0] AMPFileName
tsmp_stop = dll.tsmp_stop
tsmp_stop.restype = s32
tsmp_stop.argtypes = [pchar]

tsmp_run_all = dll.tsmp_run_all
tsmp_run_all.restype = s32
tsmp_run_all.argtypes = []

tsmp_stop_all = dll.tsmp_stop_all
tsmp_stop_all.restype = s32
tsmp_stop_all.argtypes = []

#arg[0] AGroupName
#arg[1] AFuncName
#arg[2] AInParameters
#arg[3] AOutParameters
tsmp_call_function = dll.tsmp_call_function
tsmp_call_function.restype = s32
tsmp_call_function.argtypes = [pchar,pchar,pchar,ppchar]

#arg[0] AGroupName
#arg[1] AFuncName
#arg[2] APrototype
tsmp_get_function_prototype = dll.tsmp_get_function_prototype
tsmp_get_function_prototype.restype = s32
tsmp_get_function_prototype.argtypes = [pchar,pchar,ppchar]

#arg[0] AGroupName
#arg[1] AList
tsmp_get_mp_function_list = dll.tsmp_get_mp_function_list
tsmp_get_mp_function_list.restype = s32
tsmp_get_mp_function_list.argtypes = [pchar,ppchar]

#arg[0] AList
tsmp_get_mp_list = dll.tsmp_get_mp_list
tsmp_get_mp_list.restype = s32
tsmp_get_mp_list.argtypes = [ppchar]

#arg[0] AIdxChn
#arg[1] AClusterName
#arg[2] AValue
db_get_flexray_cluster_parameters = dll.db_get_flexray_cluster_parameters
db_get_flexray_cluster_parameters.restype = s32
db_get_flexray_cluster_parameters.argtypes = [s32,pchar,PLIBFlexRayClusterParameters]

#arg[0] AIdxChn
#arg[1] AClusterName
#arg[2] AECUName
#arg[3] AValue
db_get_flexray_controller_parameters = dll.db_get_flexray_controller_parameters
db_get_flexray_controller_parameters.restype = s32
db_get_flexray_controller_parameters.argtypes = [s32,pchar,pchar,PLIBFlexRayControllerParameters]

#arg[0] ACompleteName
#arg[1] ASupport
set_system_var_event_support = dll.set_system_var_event_support
set_system_var_event_support.restype = s32
set_system_var_event_support.argtypes = [pchar,cbool]

#arg[0] ACompleteName
#arg[1] ASupport
get_system_var_event_support = dll.get_system_var_event_support
get_system_var_event_support.restype = s32
get_system_var_event_support.argtypes = [pchar,pbool]

#arg[0] AYear
#arg[1] AMonth
#arg[2] ADay
#arg[3] AHour
#arg[4] AMinute
#arg[5] ASecond
#arg[6] AMilliseconds
get_date_time = dll.get_date_time
get_date_time.restype = s32
get_date_time.argtypes = [ps32,ps32,ps32,ps32,ps32,ps32,ps32]

#arg[0] AIndex
tslog_disable_online_replay_filter = dll.tslog_disable_online_replay_filter
tslog_disable_online_replay_filter.restype = s32
tslog_disable_online_replay_filter.argtypes = [s32]

#arg[0] AIndex
#arg[1] AIsPassFilter
#arg[2] ACount
#arg[3] AIdxChannels
#arg[4] AIdentifiers
tslog_set_online_replay_filter = dll.tslog_set_online_replay_filter
tslog_set_online_replay_filter.restype = s32
tslog_set_online_replay_filter.argtypes = [s32,cbool,s32,ps32,ps32]

#arg[0] ACANSignal
#arg[1] AData
#arg[2] AValue
set_can_signal_raw_value = dll.set_can_signal_raw_value
set_can_signal_raw_value.restype = s32
set_can_signal_raw_value.argtypes = [PMPCANSignal,pu8,s64]

#arg[0] ACANSignal
#arg[1] AData
get_can_signal_raw_value = dll.get_can_signal_raw_value
get_can_signal_raw_value.restype = u64
get_can_signal_raw_value.argtypes = [PMPCANSignal,pu8]

#arg[0] ALINSignal
#arg[1] AData
#arg[2] AValue
set_lin_signal_raw_value = dll.set_lin_signal_raw_value
set_lin_signal_raw_value.restype = s32
set_lin_signal_raw_value.argtypes = [PMPLINSignal,pu8,double]

#arg[0] ALINSignal
#arg[1] AData
get_lin_signal_raw_value = dll.get_lin_signal_raw_value
get_lin_signal_raw_value.restype = u64
get_lin_signal_raw_value.argtypes = [PMPLINSignal,pu8]

#arg[0] AFlexRaySignal
#arg[1] AData
#arg[2] AValue
set_flexray_signal_raw_value = dll.set_flexray_signal_raw_value
set_flexray_signal_raw_value.restype = s32
set_flexray_signal_raw_value.argtypes = [PMPFlexRaySignal,pu8,double]

#arg[0] AFlexRaySignal
#arg[1] AData
get_flexray_signal_raw_value = dll.get_flexray_signal_raw_value
get_flexray_signal_raw_value.restype = u64
get_flexray_signal_raw_value.argtypes = [PMPFlexRaySignal,pu8]

gpg_delete_all_modules = dll.gpg_delete_all_modules
gpg_delete_all_modules.restype = s32
gpg_delete_all_modules.argtypes = []

#arg[0] AProgramName
#arg[1] ADisplayName
#arg[2] AModuleId
#arg[3] AEntryPointId
gpg_create_module = dll.gpg_create_module
gpg_create_module.restype = s32
gpg_create_module.argtypes = [pchar,pchar,ps64,ps64]

#arg[0] AModuleId
gpg_delete_module = dll.gpg_delete_module
gpg_delete_module.restype = s32
gpg_delete_module.argtypes = [s64]

#arg[0] AModuleId
#arg[1] AGraphicProgramWindowTitle
gpg_deploy_module = dll.gpg_deploy_module
gpg_deploy_module.restype = s32
gpg_deploy_module.argtypes = [s64,pchar]

#arg[0] AModuleId
#arg[1] AUpperActionId
#arg[2] ADisplayName
#arg[3] AComment
#arg[4] AActionId
gpg_add_action_down = dll.gpg_add_action_down
gpg_add_action_down.restype = s32
gpg_add_action_down.argtypes = [s64,s64,pchar,pchar,ps64]

#arg[0] AModuleId
#arg[1] ALeftActionId
#arg[2] ADisplayName
#arg[3] AComment
#arg[4] AActionId
gpg_add_action_right = dll.gpg_add_action_right
gpg_add_action_right.restype = s32
gpg_add_action_right.argtypes = [s64,s64,pchar,pchar,ps64]

#arg[0] AModuleId
#arg[1] AUpperActionId
#arg[2] ADisplayName
#arg[3] AComment
#arg[4] AJumpLabel
#arg[5] AActionId
gpg_add_goto_down = dll.gpg_add_goto_down
gpg_add_goto_down.restype = s32
gpg_add_goto_down.argtypes = [s64,s64,pchar,pchar,pchar,ps64]

#arg[0] AModuleId
#arg[1] ALeftActionId
#arg[2] ADisplayName
#arg[3] AComment
#arg[4] AJumpLabel
#arg[5] AActionId
gpg_add_goto_right = dll.gpg_add_goto_right
gpg_add_goto_right.restype = s32
gpg_add_goto_right.argtypes = [s64,s64,pchar,pchar,pchar,ps64]

#arg[0] AModuleId
#arg[1] AUpperActionId
#arg[2] ADisplayName
#arg[3] AComment
#arg[4] AJumpLabel
#arg[5] AActionId
gpg_add_from_down = dll.gpg_add_from_down
gpg_add_from_down.restype = s32
gpg_add_from_down.argtypes = [s64,s64,pchar,pchar,pchar,ps64]

#arg[0] AModuleId
#arg[1] AUpperActionId
#arg[2] ADisplayName
#arg[3] AComment
#arg[4] AGroupId
#arg[5] AEntryPointId
gpg_add_group_down = dll.gpg_add_group_down
gpg_add_group_down.restype = s32
gpg_add_group_down.argtypes = [s64,s64,pchar,pchar,ps64,ps64]

#arg[0] AModuleId
#arg[1] ALeftActionId
#arg[2] ADisplayName
#arg[3] AComment
#arg[4] AGroupId
#arg[5] AEntryPointId
gpg_add_group_right = dll.gpg_add_group_right
gpg_add_group_right.restype = s32
gpg_add_group_right.argtypes = [s64,s64,pchar,pchar,ps64,ps64]

#arg[0] AModuleId
#arg[1] AActionId
gpg_delete_action = dll.gpg_delete_action
gpg_delete_action.restype = s32
gpg_delete_action.argtypes = [s64,s64]

#arg[0] AModuleId
#arg[1] AActionId
gpg_set_action_nop = dll.gpg_set_action_nop
gpg_set_action_nop.restype = s32
gpg_set_action_nop.argtypes = [s64,s64]

#arg[0] AModuleId
#arg[1] AActionId
gpg_set_action_signal_read_write = dll.gpg_set_action_signal_read_write
gpg_set_action_signal_read_write.restype = s32
gpg_set_action_signal_read_write.argtypes = [s64,s64]

#arg[0] AModuleId
#arg[1] AActionId
gpg_set_action_api_call = dll.gpg_set_action_api_call
gpg_set_action_api_call.restype = s32
gpg_set_action_api_call.argtypes = [s64,s64]

#arg[0] AModuleId
#arg[1] AActionId
gpg_set_action_expression = dll.gpg_set_action_expression
gpg_set_action_expression.restype = s32
gpg_set_action_expression.argtypes = [s64,s64]

#arg[0] AModuleId
#arg[1] AActionId
#arg[2] ADisplayName
#arg[3] AComment
#arg[4] ATimeoutMs
gpg_configure_action_basic = dll.gpg_configure_action_basic
gpg_configure_action_basic.restype = s32
gpg_configure_action_basic.argtypes = [s64,s64,pchar,pchar,s32]

#arg[0] AModuleId
#arg[1] AActionId
#arg[2] ADisplayName
#arg[3] AComment
#arg[4] AJumpLabel
gpg_configure_goto = dll.gpg_configure_goto
gpg_configure_goto.restype = s32
gpg_configure_goto.argtypes = [s64,s64,pchar,pchar,pchar]

#arg[0] AModuleId
#arg[1] AActionId
#arg[2] ADisplayName
#arg[3] AComment
#arg[4] AJumpLabel
gpg_configure_from = dll.gpg_configure_from
gpg_configure_from.restype = s32
gpg_configure_from.argtypes = [s64,s64,pchar,pchar,pchar]

#arg[0] AModuleId
#arg[1] AActionId
#arg[2] ANextDirectionIsDown
#arg[3] AResultOK
#arg[4] AJumpBackIfEnded
gpg_configure_nop = dll.gpg_configure_nop
gpg_configure_nop.restype = s32
gpg_configure_nop.argtypes = [s64,s64,cbool,cbool,cbool]

#arg[0] AModuleId
#arg[1] AActionId
#arg[2] ARepeatCountType
#arg[3] ARepeatCountRepr
gpg_configure_group = dll.gpg_configure_group
gpg_configure_group.restype = s32
gpg_configure_group.argtypes = [s64,s64,TLIBAutomationSignalType,pchar]

#arg[0] AModuleId
#arg[1] AActionId
gpg_configure_signal_read_write_list_clear = dll.gpg_configure_signal_read_write_list_clear
gpg_configure_signal_read_write_list_clear.restype = s32
gpg_configure_signal_read_write_list_clear.argtypes = [s64,s64]

#arg[0] AModuleId
#arg[1] AActionId
#arg[2] ADestSignalType
#arg[3] ASrcSignalType
#arg[4] ADestSignalExpr
#arg[5] ASrcSignalExpr
#arg[6] AItemIndex
gpg_configure_signal_write_list_append = dll.gpg_configure_signal_write_list_append
gpg_configure_signal_write_list_append.restype = s32
gpg_configure_signal_write_list_append.argtypes = [s64,s64,TLIBAutomationSignalType,TLIBAutomationSignalType,pchar,pchar,ps32]

#arg[0] AModuleId
#arg[1] AActionId
#arg[2] AIsConditionAND
#arg[3] ADestSignalType
#arg[4] AMinSignalType
#arg[5] AMaxSignalType
#arg[6] ADestSignalExpr
#arg[7] AMinSignalExpr
#arg[8] AMaxSignalExpr
#arg[9] AItemIndex
gpg_configure_signal_read_list_append = dll.gpg_configure_signal_read_list_append
gpg_configure_signal_read_list_append.restype = s32
gpg_configure_signal_read_list_append.argtypes = [s64,s64,cbool,TLIBAutomationSignalType,TLIBAutomationSignalType,TLIBAutomationSignalType,pchar,pchar,pchar,ps32]

#arg[0] AModuleId
#arg[1] AActionId
#arg[2] AAPIType
#arg[3] AAPIName
#arg[4] AAPIArgTypes
#arg[5] AAPIArgNames
#arg[6] AAPIArgExprs
#arg[7] AArraySize
gpg_configure_api_call_arguments = dll.gpg_configure_api_call_arguments
gpg_configure_api_call_arguments.restype = s32
gpg_configure_api_call_arguments.argtypes = [s64,s64,TLIBMPFuncSource,pchar,PLIBAutomationSignalType,ppchar,ppchar,s32]

#arg[0] AModuleId
#arg[1] AActionId
#arg[2] AIgnoreResult
#arg[3] ASignalType
#arg[4] ASignalExpr
gpg_configure_api_call_result = dll.gpg_configure_api_call_result
gpg_configure_api_call_result.restype = s32
gpg_configure_api_call_result.argtypes = [s64,s64,cbool,TLIBAutomationSignalType,pchar]

#arg[0] AModuleId
#arg[1] AActionId
#arg[2] AxCount
#arg[3] AExpression
#arg[4] AArgumentTypes
#arg[5] AArgumentExprs
#arg[6] AResultType
#arg[7] AResultExpr
gpg_configure_expression = dll.gpg_configure_expression
gpg_configure_expression.restype = s32
gpg_configure_expression.argtypes = [s64,s64,s32,pchar,PLIBAutomationSignalType,ppchar,TLIBAutomationSignalType,pchar]

#arg[0] AModuleId
#arg[1] AType
#arg[2] AName
#arg[3] AInitValue
#arg[4] AComment
#arg[5] AItemIndex
gpg_add_local_var = dll.gpg_add_local_var
gpg_add_local_var.restype = s32
gpg_add_local_var.argtypes = [s64,TLIBSimVarType,pchar,pchar,pchar,ps32]

#arg[0] AModuleId
#arg[1] AItemIndex
gpg_delete_local_var = dll.gpg_delete_local_var
gpg_delete_local_var.restype = s32
gpg_delete_local_var.argtypes = [s64,s32]

#arg[0] AModuleId
gpg_delete_all_local_vars = dll.gpg_delete_all_local_vars
gpg_delete_all_local_vars.restype = s32
gpg_delete_all_local_vars.argtypes = [s64]

#arg[0] AModuleId
#arg[1] AGroupId
gpg_delete_group_items = dll.gpg_delete_group_items
gpg_delete_group_items.restype = s32
gpg_delete_group_items.argtypes = [s64,s64]

#arg[0] AModuleId
#arg[1] AActionId
#arg[2] AItemIndex
gpg_configure_signal_read_write_list_delete = dll.gpg_configure_signal_read_write_list_delete
gpg_configure_signal_read_write_list_delete.restype = s32
gpg_configure_signal_read_write_list_delete.argtypes = [s64,s64,s32]

#arg[0] AFlexRay
flexray_rbs_update_frame_by_header = dll.flexray_rbs_update_frame_by_header
flexray_rbs_update_frame_by_header.restype = s32
flexray_rbs_update_frame_by_header.argtypes = [PLIBFlexRay]

#arg[0] AModuleId
#arg[1] AProgramName
#arg[2] ADisplayName
#arg[3] ARepeatCount
#arg[4] ASelected
gpg_configure_module = dll.gpg_configure_module
gpg_configure_module.restype = s32
gpg_configure_module.argtypes = [s64,pchar,pchar,s32,cbool]

#arg[0] APath
add_path_to_environment = dll.add_path_to_environment
add_path_to_environment.restype = s32
add_path_to_environment.argtypes = [pchar]

#arg[0] APath
delete_path_from_environment = dll.delete_path_from_environment
delete_path_from_environment.restype = s32
delete_path_from_environment.argtypes = [pchar]

#arg[0] ACompleteName
#arg[1] AValue
#arg[2] ATimeUs
set_system_var_double_w_time = dll.set_system_var_double_w_time
set_system_var_double_w_time.restype = s32
set_system_var_double_w_time.argtypes = [pchar,double,s64]

#arg[0] ACompleteName
#arg[1] AValue
#arg[2] ATimeUs
set_system_var_int32_w_time = dll.set_system_var_int32_w_time
set_system_var_int32_w_time.restype = s32
set_system_var_int32_w_time.argtypes = [pchar,s32,s64]

#arg[0] ACompleteName
#arg[1] AValue
#arg[2] ATimeUs
set_system_var_uint32_w_time = dll.set_system_var_uint32_w_time
set_system_var_uint32_w_time.restype = s32
set_system_var_uint32_w_time.argtypes = [pchar,u32,s64]

#arg[0] ACompleteName
#arg[1] AValue
#arg[2] ATimeUs
set_system_var_int64_w_time = dll.set_system_var_int64_w_time
set_system_var_int64_w_time.restype = s32
set_system_var_int64_w_time.argtypes = [pchar,s64,s64]

#arg[0] ACompleteName
#arg[1] AValue
#arg[2] ATimeUs
set_system_var_uint64_w_time = dll.set_system_var_uint64_w_time
set_system_var_uint64_w_time.restype = s32
set_system_var_uint64_w_time.argtypes = [pchar,u64,s64]

#arg[0] ACompleteName
#arg[1] ACount
#arg[2] AValue
#arg[3] ATimeUs
set_system_var_uint8_array_w_time = dll.set_system_var_uint8_array_w_time
set_system_var_uint8_array_w_time.restype = s32
set_system_var_uint8_array_w_time.argtypes = [pchar,s32,pu8,s64]

#arg[0] ACompleteName
#arg[1] ACount
#arg[2] AValue
#arg[3] ATimeUs
set_system_var_int32_array_w_time = dll.set_system_var_int32_array_w_time
set_system_var_int32_array_w_time.restype = s32
set_system_var_int32_array_w_time.argtypes = [pchar,s32,ps32,s64]

#arg[0] ACompleteName
#arg[1] ACount
#arg[2] AValue
#arg[3] ATimeUs
set_system_var_double_array_w_time = dll.set_system_var_double_array_w_time
set_system_var_double_array_w_time.restype = s32
set_system_var_double_array_w_time.argtypes = [pchar,s32,pdouble,s64]

#arg[0] ACompleteName
#arg[1] AValue
#arg[2] ATimeUs
set_system_var_string_w_time = dll.set_system_var_string_w_time
set_system_var_string_w_time.restype = s32
set_system_var_string_w_time.argtypes = [pchar,pchar,s64]

#arg[0] ACompleteName
#arg[1] AValue
#arg[2] ATimeUs
set_system_var_generic_w_time = dll.set_system_var_generic_w_time
set_system_var_generic_w_time.restype = s32
set_system_var_generic_w_time.argtypes = [pchar,pchar,s64]

#arg[0] ACompleteName
#arg[1] AValue
#arg[2] ATimeUs
set_system_var_double_async_w_time = dll.set_system_var_double_async_w_time
set_system_var_double_async_w_time.restype = s32
set_system_var_double_async_w_time.argtypes = [pchar,double,s64]

#arg[0] ACompleteName
#arg[1] AValue
#arg[2] ATimeUs
set_system_var_int32_async_w_time = dll.set_system_var_int32_async_w_time
set_system_var_int32_async_w_time.restype = s32
set_system_var_int32_async_w_time.argtypes = [pchar,s32,s64]

#arg[0] ACompleteName
#arg[1] AValue
#arg[2] ATimeUs
set_system_var_uint32_async_w_time = dll.set_system_var_uint32_async_w_time
set_system_var_uint32_async_w_time.restype = s32
set_system_var_uint32_async_w_time.argtypes = [pchar,u32,s64]

#arg[0] ACompleteName
#arg[1] AValue
#arg[2] ATimeUs
set_system_var_int64_async_w_time = dll.set_system_var_int64_async_w_time
set_system_var_int64_async_w_time.restype = s32
set_system_var_int64_async_w_time.argtypes = [pchar,s64,s64]

#arg[0] ACompleteName
#arg[1] AValue
#arg[2] ATimeUs
set_system_var_uint64_async_w_time = dll.set_system_var_uint64_async_w_time
set_system_var_uint64_async_w_time.restype = s32
set_system_var_uint64_async_w_time.argtypes = [pchar,u64,s64]

#arg[0] ACompleteName
#arg[1] ACount
#arg[2] AValue
#arg[3] ATimeUs
set_system_var_uint8_array_async_w_time = dll.set_system_var_uint8_array_async_w_time
set_system_var_uint8_array_async_w_time.restype = s32
set_system_var_uint8_array_async_w_time.argtypes = [pchar,s32,pu8,s64]

#arg[0] ACompleteName
#arg[1] ACount
#arg[2] AValue
#arg[3] ATimeUs
set_system_var_int32_array_async_w_time = dll.set_system_var_int32_array_async_w_time
set_system_var_int32_array_async_w_time.restype = s32
set_system_var_int32_array_async_w_time.argtypes = [pchar,s32,ps32,s64]

#arg[0] ACompleteName
#arg[1] ACount
#arg[2] AValue
#arg[3] ATimeUs
set_system_var_int64_array_async_w_time = dll.set_system_var_int64_array_async_w_time
set_system_var_int64_array_async_w_time.restype = s32
set_system_var_int64_array_async_w_time.argtypes = [pchar,s32,ps64,s64]

#arg[0] ACompleteName
#arg[1] ACount
#arg[2] AValue
#arg[3] ATimeUs
set_system_var_double_array_async_w_time = dll.set_system_var_double_array_async_w_time
set_system_var_double_array_async_w_time.restype = s32
set_system_var_double_array_async_w_time.argtypes = [pchar,s32,pdouble,s64]

#arg[0] ACompleteName
#arg[1] AValue
#arg[2] ATimeUs
set_system_var_string_async_w_time = dll.set_system_var_string_async_w_time
set_system_var_string_async_w_time.restype = s32
set_system_var_string_async_w_time.argtypes = [pchar,pchar,s64]

#arg[0] ACompleteName
#arg[1] AValue
#arg[2] ATimeUs
set_system_var_generic_async_w_time = dll.set_system_var_generic_async_w_time
set_system_var_generic_async_w_time.restype = s32
set_system_var_generic_async_w_time.argtypes = [pchar,pchar,s64]

#arg[0] ASignalStartBitInPDU
#arg[1] ASignalBitLength
#arg[2] AIsSignalIntel
#arg[3] AIsPDUIntel
#arg[4] APDUStartBit
#arg[5] APDUBitLength
#arg[6] AActualStartBit
db_get_signal_startbit_by_pdu_offset = dll.db_get_signal_startbit_by_pdu_offset
db_get_signal_startbit_by_pdu_offset.restype = s32
db_get_signal_startbit_by_pdu_offset.argtypes = [s32,s32,cbool,cbool,s32,s32,ps32]

#arg[0] ATitle
#arg[1] AFileTypeDesc
#arg[2] AFilter
#arg[3] ASuggestFileName
#arg[4] ADestinationFileName
ui_show_save_file_dialog = dll.ui_show_save_file_dialog
ui_show_save_file_dialog.restype = s32
ui_show_save_file_dialog.argtypes = [pchar,pchar,pchar,pchar,ppchar]

#arg[0] ATitle
#arg[1] AFileTypeDesc
#arg[2] AFilter
#arg[3] ASuggestFileName
#arg[4] ADestinationFileName
ui_show_open_file_dialog = dll.ui_show_open_file_dialog
ui_show_open_file_dialog.restype = s32
ui_show_open_file_dialog.argtypes = [pchar,pchar,pchar,pchar,ppchar]

#arg[0] ADestinationDirectory
ui_show_select_directory_dialog = dll.ui_show_select_directory_dialog
ui_show_select_directory_dialog.restype = s32
ui_show_select_directory_dialog.argtypes = [ppchar]

#arg[0] AEthernetHeader
transmit_ethernet_async = dll.transmit_ethernet_async
transmit_ethernet_async.restype = s32
transmit_ethernet_async.argtypes = [PLIBEthernetHeader]

#arg[0] AEthernetHeader
#arg[1] ATimeoutMs
transmit_ethernet_sync = dll.transmit_ethernet_sync
transmit_ethernet_sync.restype = s32
transmit_ethernet_sync.argtypes = [PLIBEthernetHeader,s32]

#arg[0] AEthernetHeader
inject_ethernet_frame = dll.inject_ethernet_frame
inject_ethernet_frame.restype = s32
inject_ethernet_frame.argtypes = [PLIBEthernetHeader]

#arg[0] AHandle
#arg[1] AEthernetHeader
tslog_blf_write_ethernet = dll.tslog_blf_write_ethernet
tslog_blf_write_ethernet.restype = s32
tslog_blf_write_ethernet.argtypes = [size_t,PLIBEthernetHeader]

#arg[0] ACount
set_ethernet_channel_count = dll.set_ethernet_channel_count
set_ethernet_channel_count.restype = s32
set_ethernet_channel_count.argtypes = [s32]

#arg[0] ACount
get_ethernet_channel_count = dll.get_ethernet_channel_count
get_ethernet_channel_count.restype = s32
get_ethernet_channel_count.argtypes = [ps32]

#arg[0] AEthernetHeader
transmit_ethernet_async_wo_pretx = dll.transmit_ethernet_async_wo_pretx
transmit_ethernet_async_wo_pretx.restype = s32
transmit_ethernet_async_wo_pretx.argtypes = [PLIBEthernetHeader]

#arg[0] AId
#arg[1] AIndex
db_get_can_db_index_by_id = dll.db_get_can_db_index_by_id
db_get_can_db_index_by_id.restype = s32
db_get_can_db_index_by_id.argtypes = [s32,ps32]

#arg[0] AId
#arg[1] AIndex
db_get_lin_db_index_by_id = dll.db_get_lin_db_index_by_id
db_get_lin_db_index_by_id.restype = s32
db_get_lin_db_index_by_id.argtypes = [s32,ps32]

#arg[0] AId
#arg[1] AIndex
db_get_flexray_db_index_by_id = dll.db_get_flexray_db_index_by_id
db_get_flexray_db_index_by_id.restype = s32
db_get_flexray_db_index_by_id.argtypes = [s32,ps32]

#arg[0] AHeader
#arg[1] ASrcIp
#arg[2] ADstIp
#arg[3] ASrcPort
#arg[4] ADstPort
#arg[5] APayload
#arg[6] APayloadLength
#arg[7] AIdentification
#arg[8] AFragmentIndex
eth_build_ipv4_udp_packet = dll.eth_build_ipv4_udp_packet
eth_build_ipv4_udp_packet.restype = s32
eth_build_ipv4_udp_packet.argtypes = [PLIBEthernetHeader,pu8,pu8,u16,u16,pu8,u16,ps32,ps32]

#arg[0] ACompleteName
#arg[1] AEvent
register_system_var_change_event = dll.register_system_var_change_event
register_system_var_change_event.restype = s32
register_system_var_change_event.argtypes = [pchar,TLIBOnSysVarChange]

#arg[0] ACompleteName
#arg[1] AEvent
unregister_system_var_change_event = dll.unregister_system_var_change_event
unregister_system_var_change_event.restype = s32
unregister_system_var_change_event.argtypes = [pchar,TLIBOnSysVarChange]

#arg[0] AEvent
unregister_system_var_change_events = dll.unregister_system_var_change_events
unregister_system_var_change_events.restype = s32
unregister_system_var_change_events.argtypes = [TLIBOnSysVarChange]

block_current_pretx = dll.block_current_pretx
block_current_pretx.restype = s32
block_current_pretx.argtypes = []

#arg[0] AAPIName
#arg[1] AArgCount
#arg[2] AArgCapacity
#arg[3] AArgs
call_system_api = dll.call_system_api
call_system_api.restype = s32
call_system_api.argtypes = [pchar,s32,s32,ppchar]

#arg[0] AAPIName
#arg[1] AArgCount
#arg[2] AArgCapacity
#arg[3] AArgs
call_library_api = dll.call_library_api
call_library_api.restype = s32
call_library_api.argtypes = [pchar,s32,s32,ppchar]

#arg[0] AHeader
#arg[1] AIdentification
#arg[2] AUDPPacketLength
#arg[3] AUDPDataOffset
#arg[4] AIsPacketEnded
eth_is_udp_packet = dll.eth_is_udp_packet
eth_is_udp_packet.restype = s32
eth_is_udp_packet.argtypes = [PLIBEthernetHeader,POINTER(u16),POINTER(u16),POINTER(u16),POINTER(cbool)]

#arg[0] AHeader
#arg[1] AOverwriteChecksum
#arg[2] AChecksum
eth_ip_calc_header_checksum = dll.eth_ip_calc_header_checksum
eth_ip_calc_header_checksum.restype = s32
eth_ip_calc_header_checksum.argtypes = [PLIBEthernetHeader,cbool,pu16]

#arg[0] AHeader
#arg[1] AUDPPayloadAddr
#arg[2] AUDPPayloadLength
#arg[3] AOverwriteChecksum
#arg[4] AChecksum
eth_udp_calc_checksum = dll.eth_udp_calc_checksum
eth_udp_calc_checksum.restype = s32
eth_udp_calc_checksum.argtypes = [PLIBEthernetHeader,pu8,u16,cbool,pu16]

#arg[0] AHeader
#arg[1] AOverwriteChecksum
#arg[2] AChecksum
eth_udp_calc_checksum_on_frame = dll.eth_udp_calc_checksum_on_frame
eth_udp_calc_checksum_on_frame.restype = s32
eth_udp_calc_checksum_on_frame.argtypes = [PLIBEthernetHeader,cbool,pu16]

#arg[0] AHeader
eth_log_ethernet_frame_data = dll.eth_log_ethernet_frame_data
eth_log_ethernet_frame_data.restype = s32
eth_log_ethernet_frame_data.argtypes = [PLIBEthernetHeader]

signal_tester_clear_all = dll.signal_tester_clear_all
signal_tester_clear_all.restype = s32
signal_tester_clear_all.argtypes = []

#arg[0] AFilePath
signal_tester_load_configuration = dll.signal_tester_load_configuration
signal_tester_load_configuration.restype = s32
signal_tester_load_configuration.argtypes = [pchar]

#arg[0] AFilePath
signal_tester_save_configuration = dll.signal_tester_save_configuration
signal_tester_save_configuration.restype = s32
signal_tester_save_configuration.argtypes = [pchar]

#arg[0] AName
signal_tester_run_item_by_name = dll.signal_tester_run_item_by_name
signal_tester_run_item_by_name.restype = s32
signal_tester_run_item_by_name.argtypes = [pchar]

#arg[0] AName
signal_tester_stop_item_by_name = dll.signal_tester_stop_item_by_name
signal_tester_stop_item_by_name.restype = s32
signal_tester_stop_item_by_name.argtypes = [pchar]

#arg[0] AIndex
signal_tester_run_item_by_index = dll.signal_tester_run_item_by_index
signal_tester_run_item_by_index.restype = s32
signal_tester_run_item_by_index.argtypes = [s32]

#arg[0] AIndex
signal_tester_stop_item_by_index = dll.signal_tester_stop_item_by_index
signal_tester_stop_item_by_index.restype = s32
signal_tester_stop_item_by_index.argtypes = [s32]

#arg[0] AObj
#arg[1] AIndex
#arg[2] AIsPass
signal_tester_get_item_verdict_by_index = dll.signal_tester_get_item_verdict_by_index
signal_tester_get_item_verdict_by_index.restype = s32
signal_tester_get_item_verdict_by_index.argtypes = [ps32,s32,pbool]

#arg[0] AObj
#arg[1] AName
#arg[2] AIsPass
#arg[3] AEventTimeUs
#arg[4] ADescription
signal_tester_get_item_result_by_name = dll.signal_tester_get_item_result_by_name
signal_tester_get_item_result_by_name.restype = s32
signal_tester_get_item_result_by_name.argtypes = [ps32,pchar,pbool,ps64,ppchar]

#arg[0] AObj
#arg[1] AIndex
#arg[2] AIsPass
#arg[3] AEventTimeUs
#arg[4] ADescription
signal_tester_get_item_result_by_index = dll.signal_tester_get_item_result_by_index
signal_tester_get_item_result_by_index.restype = s32
signal_tester_get_item_result_by_index.argtypes = [ps32,s32,pbool,ps64,ppchar]

#arg[0] AObj
#arg[1] AName
#arg[2] AIsPass
signal_tester_get_item_verdict_by_name = dll.signal_tester_get_item_verdict_by_name
signal_tester_get_item_verdict_by_name.restype = s32
signal_tester_get_item_verdict_by_name.argtypes = [ps32,pchar,pbool]

#arg[0] AHandle
#arg[1] ASection
#arg[2] AKey
#arg[3] AValue
#arg[4] AValueCapacity
#arg[5] ADefault
ini_read_string_wo_quotes = dll.ini_read_string_wo_quotes
ini_read_string_wo_quotes.restype = s32
ini_read_string_wo_quotes.argtypes = [size_t,pchar,pchar,pchar,ps32,pchar]

#arg[0] AObj
#arg[1] AIndex
#arg[2] AMin
#arg[3] AMax
#arg[4] APass
#arg[5] AResult
#arg[6] AResultRepr
signal_tester_check_statistics_by_index = dll.signal_tester_check_statistics_by_index
signal_tester_check_statistics_by_index.restype = s32
signal_tester_check_statistics_by_index.argtypes = [ps32,s32,double,double,pbool,pdouble,ppchar]

#arg[0] AObj
#arg[1] AItemName
#arg[2] AMin
#arg[3] AMax
#arg[4] APass
#arg[5] AResult
#arg[6] AResultRepr
signal_tester_check_statistics_by_name = dll.signal_tester_check_statistics_by_name
signal_tester_check_statistics_by_name.restype = s32
signal_tester_check_statistics_by_name.argtypes = [ps32,pchar,double,double,pbool,pdouble,ppchar]

#arg[0] AIndex
#arg[1] AEnable
signal_tester_enable_item_by_index = dll.signal_tester_enable_item_by_index
signal_tester_enable_item_by_index.restype = s32
signal_tester_enable_item_by_index.argtypes = [s32,cbool]

#arg[0] AItemName
#arg[1] AEnable
signal_tester_enable_item_by_name = dll.signal_tester_enable_item_by_name
signal_tester_enable_item_by_name.restype = s32
signal_tester_enable_item_by_name.argtypes = [pchar,cbool]

signal_tester_run_all = dll.signal_tester_run_all
signal_tester_run_all.restype = s32
signal_tester_run_all.argtypes = []

signal_tester_stop_all = dll.signal_tester_stop_all
signal_tester_stop_all.restype = s32
signal_tester_stop_all.argtypes = []

#arg[0] AChnIdx
lin_clear_schedule_tables = dll.lin_clear_schedule_tables
lin_clear_schedule_tables.restype = s32
lin_clear_schedule_tables.argtypes = [s32]

#arg[0] AChnIdx
lin_stop_lin_channel = dll.lin_stop_lin_channel
lin_stop_lin_channel.restype = s32
lin_stop_lin_channel.argtypes = [s32]

#arg[0] AChnIdx
lin_start_lin_channel = dll.lin_start_lin_channel
lin_start_lin_channel.restype = s32
lin_start_lin_channel.argtypes = [s32]

#arg[0] AChnIdx
lin_switch_runtime_schedule_table = dll.lin_switch_runtime_schedule_table
lin_switch_runtime_schedule_table.restype = s32
lin_switch_runtime_schedule_table.argtypes = [s32]

#arg[0] AChnIdx
lin_switch_idle_schedule_table = dll.lin_switch_idle_schedule_table
lin_switch_idle_schedule_table.restype = s32
lin_switch_idle_schedule_table.argtypes = [s32]

#arg[0] AChnIdx
#arg[1] ASchIndex
lin_switch_normal_schedule_table = dll.lin_switch_normal_schedule_table
lin_switch_normal_schedule_table.restype = s32
lin_switch_normal_schedule_table.argtypes = [s32,s32]

#arg[0] AChnIdx
lin_batch_set_schedule_start = dll.lin_batch_set_schedule_start
lin_batch_set_schedule_start.restype = s32
lin_batch_set_schedule_start.argtypes = [s32]

#arg[0] AChnIdx
#arg[1] ALINData
#arg[2] ADelayMs
lin_batch_add_schedule_frame = dll.lin_batch_add_schedule_frame
lin_batch_add_schedule_frame.restype = s32
lin_batch_add_schedule_frame.argtypes = [s32,PLIBLIN,s32]

#arg[0] AChnIdx
lin_batch_set_schedule_end = dll.lin_batch_set_schedule_end
lin_batch_set_schedule_end.restype = s32
lin_batch_set_schedule_end.argtypes = [s32]

#arg[0] AChnIdx
#arg[1] AFunctionType
lin_set_node_functiontype = dll.lin_set_node_functiontype
lin_set_node_functiontype.restype = s32
lin_set_node_functiontype.argtypes = [s32,s32]

#arg[0] AChnIdx
#arg[1] AID
#arg[2] AIndex
lin_active_frame_in_schedule_table = dll.lin_active_frame_in_schedule_table
lin_active_frame_in_schedule_table.restype = s32
lin_active_frame_in_schedule_table.argtypes = [u32,u8,s32]

#arg[0] AChnIdx
#arg[1] AID
#arg[2] AIndex
lin_deactive_frame_in_schedule_table = dll.lin_deactive_frame_in_schedule_table
lin_deactive_frame_in_schedule_table.restype = s32
lin_deactive_frame_in_schedule_table.argtypes = [u32,u8,s32]

#arg[0] AChnIdx
#arg[1] ASlot
#arg[2] ABaseCycle
#arg[3] ACycleRep
#arg[4] ATimeoutMs
flexray_disable_frame = dll.flexray_disable_frame
flexray_disable_frame.restype = s32
flexray_disable_frame.argtypes = [s32,u8,u8,u8,s32]

#arg[0] AChnIdx
#arg[1] ASlot
#arg[2] ABaseCycle
#arg[3] ACycleRep
#arg[4] ATimeoutMs
flexray_enable_frame = dll.flexray_enable_frame
flexray_enable_frame.restype = s32
flexray_enable_frame.argtypes = [s32,u8,u8,u8,s32]

#arg[0] AFileNameWoSuffix
#arg[1] ATitle
open_help_doc = dll.open_help_doc
open_help_doc.restype = s32
open_help_doc.argtypes = [pchar,pchar]

#arg[0] AEnglishStr
#arg[1] AIniSection
#arg[2] ATranslatedStr
get_language_string = dll.get_language_string
get_language_string.restype = s32
get_language_string.argtypes = [pchar,pchar,ppchar]

#arg[0] ABlfFile
#arg[1] ACSVFile
#arg[2] AToTerminate
convert_blf_to_csv = dll.convert_blf_to_csv
convert_blf_to_csv.restype = s32
convert_blf_to_csv.argtypes = [pchar,pchar,pbool]

#arg[0] ABlfFile
#arg[1] ACSVFile
#arg[2] AFilterConf
#arg[3] AToTerminate
convert_blf_to_csv_with_filter = dll.convert_blf_to_csv_with_filter
convert_blf_to_csv_with_filter.restype = s32
convert_blf_to_csv_with_filter.argtypes = [pchar,pchar,pchar,pbool]

#arg[0] AIsAutoHandle
set_flexray_ub_bit_auto_handle = dll.set_flexray_ub_bit_auto_handle
set_flexray_ub_bit_auto_handle.restype = s32
set_flexray_ub_bit_auto_handle.argtypes = [cbool]

#arg[0] AIdx
#arg[1] AIsRunning
#arg[2] AIsCheckDone
#arg[3] AFailReason
signal_tester_get_item_status_by_index = dll.signal_tester_get_item_status_by_index
signal_tester_get_item_status_by_index.restype = s32
signal_tester_get_item_status_by_index.argtypes = [s32,pbool,pbool,PSignalTesterFailReason]

#arg[0] ATesterName
#arg[1] AIsRunning
#arg[2] AIsCheckDone
#arg[3] AFailReason
signal_tester_get_item_status_by_name = dll.signal_tester_get_item_status_by_name
signal_tester_get_item_status_by_name.restype = s32
signal_tester_get_item_status_by_name.argtypes = [pchar,pbool,pbool,PSignalTesterFailReason]

#arg[0] AIdx
#arg[1] ATimeBegin
#arg[2] ATimeEnd
signal_tester_set_item_time_range_by_index = dll.signal_tester_set_item_time_range_by_index
signal_tester_set_item_time_range_by_index.restype = s32
signal_tester_set_item_time_range_by_index.argtypes = [s32,double,double]

#arg[0] AName
#arg[1] ATimeBegin
#arg[2] ATimeEnd
signal_tester_set_item_time_range_by_name = dll.signal_tester_set_item_time_range_by_name
signal_tester_set_item_time_range_by_name.restype = s32
signal_tester_set_item_time_range_by_name.argtypes = [pchar,double,double]

#arg[0] AIdx
#arg[1] ALow
#arg[2] AHigh
signal_tester_set_item_value_range_by_index = dll.signal_tester_set_item_value_range_by_index
signal_tester_set_item_value_range_by_index.restype = s32
signal_tester_set_item_value_range_by_index.argtypes = [s32,double,double]

#arg[0] AName
#arg[1] ALow
#arg[2] AHigh
signal_tester_set_item_value_range_by_name = dll.signal_tester_set_item_value_range_by_name
signal_tester_set_item_value_range_by_name.restype = s32
signal_tester_set_item_value_range_by_name.argtypes = [pchar,double,double]

#arg[0] AObj
#arg[1] AFileName
start_log_w_filename = dll.start_log_w_filename
start_log_w_filename.restype = s32
start_log_w_filename.argtypes = [ps32,pchar]

#arg[0] ABlfFile
#arg[1] AMatFile
#arg[2] AFilterConf
#arg[3] AToTerminate
convert_blf_to_mat_w_filter = dll.convert_blf_to_mat_w_filter
convert_blf_to_mat_w_filter.restype = s32
convert_blf_to_mat_w_filter.argtypes = [pchar,pchar,pchar,pbool]

#arg[0] AASCFile
#arg[1] AMatFile
#arg[2] AFilterConf
#arg[3] AToTerminate
convert_asc_to_mat_w_filter = dll.convert_asc_to_mat_w_filter
convert_asc_to_mat_w_filter.restype = s32
convert_asc_to_mat_w_filter.argtypes = [pchar,pchar,pchar,pbool]

#arg[0] AASCFile
#arg[1] ACSVFile
#arg[2] AFilterConf
#arg[3] AToTerminate
convert_asc_to_csv_w_filter = dll.convert_asc_to_csv_w_filter
convert_asc_to_csv_w_filter.restype = s32
convert_asc_to_csv_w_filter.argtypes = [pchar,pchar,pchar,pbool]

#arg[0] ALevel
set_debug_log_level = dll.set_debug_log_level
set_debug_log_level.restype = s32
set_debug_log_level.argtypes = [s32]

#arg[0] AHeader
eth_frame_clear_vlans = dll.eth_frame_clear_vlans
eth_frame_clear_vlans.restype = s32
eth_frame_clear_vlans.argtypes = [PLIBEthernetHeader]

#arg[0] AHeader
#arg[1] AVLANId
#arg[2] APriority
#arg[3] ACFI
eth_frame_append_vlan = dll.eth_frame_append_vlan
eth_frame_append_vlan.restype = s32
eth_frame_append_vlan.argtypes = [PLIBEthernetHeader,u16,u8,u8]

#arg[0] AHeader
#arg[1] AVLANIds
#arg[2] APriority
#arg[3] ACFI
#arg[4] ACount
eth_frame_append_vlans = dll.eth_frame_append_vlans
eth_frame_append_vlans.restype = s32
eth_frame_append_vlans.argtypes = [PLIBEthernetHeader,pu16,u8,u8,s32]

#arg[0] AHeader
eth_frame_remove_vlan = dll.eth_frame_remove_vlan
eth_frame_remove_vlan.restype = s32
eth_frame_remove_vlan.argtypes = [PLIBEthernetHeader]

#arg[0] AInputHeader
#arg[1] APayload
#arg[2] APayloadLength
#arg[3] AIdentification
#arg[4] AFragmentIndex
eth_build_ipv4_udp_packet_on_frame = dll.eth_build_ipv4_udp_packet_on_frame
eth_build_ipv4_udp_packet_on_frame.restype = s32
eth_build_ipv4_udp_packet_on_frame.argtypes = [PLIBEthernetHeader,pu8,u16,ps32,ps32]

eth_udp_fragment_processor_clear = dll.eth_udp_fragment_processor_clear
eth_udp_fragment_processor_clear.restype = s32
eth_udp_fragment_processor_clear.argtypes = []

#arg[0] AHeader
#arg[1] AStatus
#arg[2] APayload
#arg[3] APayloadLength
eth_udp_fragment_processor_parse = dll.eth_udp_fragment_processor_parse
eth_udp_fragment_processor_parse.restype = s32
eth_udp_fragment_processor_parse.argtypes = [PLIBEthernetHeader,PUDPFragmentProcessStatus,ppu8,pu16]

#arg[0] AHeader
#arg[1] AVLANId
#arg[2] APriority
#arg[3] ACFI
eth_frame_insert_vlan = dll.eth_frame_insert_vlan
eth_frame_insert_vlan.restype = s32
eth_frame_insert_vlan.argtypes = [PLIBEthernetHeader,u16,u8,u8]

#arg[0] AId
get_language_id = dll.get_language_id
get_language_id.restype = s32
get_language_id.argtypes = [ps32]

#arg[0] AHost
#arg[1] APort
#arg[2] ADataEvent
#arg[3] AHandle
telnet_create = dll.telnet_create
telnet_create.restype = s32
telnet_create.argtypes = [pchar,u16,TOnIoIPData,psize_t]

#arg[0] AHandle
telnet_delete = dll.telnet_delete
telnet_delete.restype = s32
telnet_delete.argtypes = [size_t]

#arg[0] AHandle
#arg[1] AStr
telnet_send_string = dll.telnet_send_string
telnet_send_string.restype = s32
telnet_send_string.argtypes = [size_t,pchar]

#arg[0] AHandle
telnet_connect = dll.telnet_connect
telnet_connect.restype = s32
telnet_connect.argtypes = [size_t]

#arg[0] AHandle
telnet_disconnect = dll.telnet_disconnect
telnet_disconnect.restype = s32
telnet_disconnect.argtypes = [size_t]

#arg[0] AHandle
#arg[1] AConnectedCallback
#arg[2] ADisconnectedCallback
telnet_set_connection_callback = dll.telnet_set_connection_callback
telnet_set_connection_callback.restype = s32
telnet_set_connection_callback.argtypes = [size_t,TOnIoIPConnection,TOnIoIPConnection]

#arg[0] AHandle
#arg[1] AEnable
telnet_enable_debug_print = dll.telnet_enable_debug_print
telnet_enable_debug_print.restype = s32
telnet_enable_debug_print.argtypes = [size_t,cbool]

#arg[0] AObj
#arg[1] ABlfFileName
#arg[2] APcapFileName
#arg[3] AProgressCallback
tslog_blf_to_pcap = dll.tslog_blf_to_pcap
tslog_blf_to_pcap.restype = s32
tslog_blf_to_pcap.argtypes = [ps32,pchar,pchar,TReadProgressCallback]

#arg[0] AObj
#arg[1] APcapFileName
#arg[2] ABlfFileName
#arg[3] AProgressCallback
tslog_pcap_to_blf = dll.tslog_pcap_to_blf
tslog_pcap_to_blf.restype = s32
tslog_pcap_to_blf.argtypes = [ps32,pchar,pchar,TReadProgressCallback]

#arg[0] AObj
#arg[1] APcapngFileName
#arg[2] ABlfFileName
#arg[3] AProgressCallback
tslog_pcapng_to_blf = dll.tslog_pcapng_to_blf
tslog_pcapng_to_blf.restype = s32
tslog_pcapng_to_blf.argtypes = [ps32,pchar,pchar,TReadProgressCallback]

#arg[0] AObj
#arg[1] ABlfFileName
#arg[2] APcapngFileName
#arg[3] AProgressCallback
tslog_blf_to_pcapng = dll.tslog_blf_to_pcapng
tslog_blf_to_pcapng.restype = s32
tslog_blf_to_pcapng.argtypes = [ps32,pchar,pchar,TReadProgressCallback]

enter_critical_section = dll.enter_critical_section
enter_critical_section.restype = s32
enter_critical_section.argtypes = []

leave_critical_section = dll.leave_critical_section
leave_critical_section.restype = s32
leave_critical_section.argtypes = []

try_enter_critical_section = dll.try_enter_critical_section
try_enter_critical_section.restype = s32
try_enter_critical_section.argtypes = []

#arg[0] AChnIdx
#arg[1] AOldKey
#arg[2] AOldKeyLength
#arg[3] ANewKey
#arg[4] ANewKeyLength
#arg[5] ATimeoutMS
security_update_new_key_sync = dll.security_update_new_key_sync
security_update_new_key_sync.restype = s32
security_update_new_key_sync.argtypes = [s32,pchar,u8,pchar,u8,s32]

#arg[0] AChnIdx
#arg[1] AKey
#arg[2] AKeyLength
#arg[3] ATimeoutMS
security_unlock_write_authority_sync = dll.security_unlock_write_authority_sync
security_unlock_write_authority_sync.restype = s32
security_unlock_write_authority_sync.argtypes = [s32,pchar,u8,s32]

#arg[0] AChnIdx
#arg[1] AKey
#arg[2] AKeyLength
security_unlock_write_authority_async = dll.security_unlock_write_authority_async
security_unlock_write_authority_async.restype = s32
security_unlock_write_authority_async.argtypes = [s32,pchar,u8]

#arg[0] AChnIdx
#arg[1] ASlotIndex
#arg[2] AString
#arg[3] AStringLength
#arg[4] ATimeoutMs
security_write_string_sync = dll.security_write_string_sync
security_write_string_sync.restype = s32
security_write_string_sync.argtypes = [s32,s32,pchar,u8,s32]

#arg[0] AChnIdx
#arg[1] ASlotIndex
#arg[2] AString
#arg[3] AStringLength
security_write_string_async = dll.security_write_string_async
security_write_string_async.restype = s32
security_write_string_async.argtypes = [s32,s32,pchar,u8]

#arg[0] AChnIdx
#arg[1] ASlotIndex
#arg[2] AString
#arg[3] AStringLength
#arg[4] ATimeoutMS
security_read_string_sync = dll.security_read_string_sync
security_read_string_sync.restype = s32
security_read_string_sync.argtypes = [s32,s32,pchar,pu8,s32]

#arg[0] AChnIdx
#arg[1] ASlotIndex
#arg[2] AString
#arg[3] AStringLength
#arg[4] ATimeoutMS
security_unlock_encrypt_channel_sync = dll.security_unlock_encrypt_channel_sync
security_unlock_encrypt_channel_sync.restype = s32
security_unlock_encrypt_channel_sync.argtypes = [s32,s32,pchar,u8,s32]

#arg[0] AChnIdx
#arg[1] ASlotIndex
#arg[2] AString
#arg[3] AStringLength
security_unlock_encrypt_channel_async = dll.security_unlock_encrypt_channel_async
security_unlock_encrypt_channel_async.restype = s32
security_unlock_encrypt_channel_async.argtypes = [s32,s32,pchar,u8]

#arg[0] AChnIdx
#arg[1] ASlotIndex
#arg[2] AString
#arg[3] AStringLength
#arg[4] ATimeoutMS
security_encrypt_string_sync = dll.security_encrypt_string_sync
security_encrypt_string_sync.restype = s32
security_encrypt_string_sync.argtypes = [s32,s32,pchar,pu8,s32]

#arg[0] AChnIdx
#arg[1] ASlotIndex
#arg[2] AString
#arg[3] AStringLength
#arg[4] ATimeoutMS
security_decrypt_string_sync = dll.security_decrypt_string_sync
security_decrypt_string_sync.restype = s32
security_decrypt_string_sync.argtypes = [s32,s32,pchar,pu8,s32]

#arg[0] AChnIdx
#arg[1] AOldKey
#arg[2] AOldKeyLength
#arg[3] ANewKey
#arg[4] ANewKeyLength
#arg[5] ATimeoutMS
tsapp_security_update_new_key_sync = dll.tsapp_security_update_new_key_sync
tsapp_security_update_new_key_sync.restype = s32
tsapp_security_update_new_key_sync.argtypes = [s32,pchar,u8,pchar,u8,s32]

#arg[0] AChnIdx
#arg[1] AKey
#arg[2] AKeyLength
#arg[3] ATimeoutMS
tsapp_security_unlock_write_authority_sync = dll.tsapp_security_unlock_write_authority_sync
tsapp_security_unlock_write_authority_sync.restype = s32
tsapp_security_unlock_write_authority_sync.argtypes = [s32,pchar,u8,s32]

#arg[0] AChnIdx
#arg[1] AKey
#arg[2] AKeyLength
tsapp_security_unlock_write_authority_async = dll.tsapp_security_unlock_write_authority_async
tsapp_security_unlock_write_authority_async.restype = s32
tsapp_security_unlock_write_authority_async.argtypes = [s32,pchar,u8]

#arg[0] AChnIdx
#arg[1] ASlotIndex
#arg[2] AString
#arg[3] AStringLength
#arg[4] ATimeoutMs
tsapp_security_write_string_sync = dll.tsapp_security_write_string_sync
tsapp_security_write_string_sync.restype = s32
tsapp_security_write_string_sync.argtypes = [s32,s32,pchar,u8,s32]

#arg[0] AChnIdx
#arg[1] ASlotIndex
#arg[2] AString
#arg[3] AStringLength
tsapp_security_write_string_async = dll.tsapp_security_write_string_async
tsapp_security_write_string_async.restype = s32
tsapp_security_write_string_async.argtypes = [s32,s32,pchar,u8]

#arg[0] AChnIdx
#arg[1] ASlotIndex
#arg[2] AString
#arg[3] AStringLength
#arg[4] ATimeoutMS
tsapp_security_read_string_sync = dll.tsapp_security_read_string_sync
tsapp_security_read_string_sync.restype = s32
tsapp_security_read_string_sync.argtypes = [s32,s32,pchar,pu8,s32]

#arg[0] AChnIdx
#arg[1] ASlotIndex
#arg[2] AString
#arg[3] AStringLength
#arg[4] ATimeoutMS
tsapp_security_unlock_encrypt_channel_sync = dll.tsapp_security_unlock_encrypt_channel_sync
tsapp_security_unlock_encrypt_channel_sync.restype = s32
tsapp_security_unlock_encrypt_channel_sync.argtypes = [s32,s32,pchar,u8,s32]

#arg[0] AChnIdx
#arg[1] ASlotIndex
#arg[2] AString
#arg[3] AStringLength
tsapp_security_unlock_encrypt_channel_async = dll.tsapp_security_unlock_encrypt_channel_async
tsapp_security_unlock_encrypt_channel_async.restype = s32
tsapp_security_unlock_encrypt_channel_async.argtypes = [s32,s32,pchar,u8]

#arg[0] AChnIdx
#arg[1] ASlotIndex
#arg[2] AString
#arg[3] AStringLength
#arg[4] ATimeoutMS
tsapp_security_encrypt_string_sync = dll.tsapp_security_encrypt_string_sync
tsapp_security_encrypt_string_sync.restype = s32
tsapp_security_encrypt_string_sync.argtypes = [s32,s32,pchar,pu8,s32]

#arg[0] AChnIdx
#arg[1] ASlotIndex
#arg[2] AString
#arg[3] AStringLength
#arg[4] ATimeoutMS
tsapp_security_decrypt_string_sync = dll.tsapp_security_decrypt_string_sync
tsapp_security_decrypt_string_sync.restype = s32
tsapp_security_decrypt_string_sync.argtypes = [s32,s32,pchar,pu8,s32]

#arg[0] ABusType
#arg[1] AIdxLogicalChn
#arg[2] APCTimeUs
#arg[3] AHwTimeUs
set_channel_timestamp_deviation_factor = dll.set_channel_timestamp_deviation_factor
set_channel_timestamp_deviation_factor.restype = s32
set_channel_timestamp_deviation_factor.argtypes = [TLIBApplicationChannelType,s32,s64,s64]

#arg[0] ADirectory
start_system_message_log = dll.start_system_message_log
start_system_message_log.restype = s32
start_system_message_log.argtypes = [pchar]

#arg[0] ALogFileName
end_system_message_log = dll.end_system_message_log
end_system_message_log.restype = s32
end_system_message_log.argtypes = [ppchar]

#arg[0] ARpcName
#arg[1] ABufferSizeBytes
#arg[2] ARxEvent
#arg[3] AHandle
rpc_create_server = dll.rpc_create_server
rpc_create_server.restype = s32
rpc_create_server.argtypes = [pchar,size_t,TOnRpcData,psize_t]

#arg[0] AHandle
#arg[1] AActivate
rpc_activate_server = dll.rpc_activate_server
rpc_activate_server.restype = s32
rpc_activate_server.argtypes = [size_t,cbool]

#arg[0] AHandle
rpc_delete_server = dll.rpc_delete_server
rpc_delete_server.restype = s32
rpc_delete_server.argtypes = [size_t]

#arg[0] AHandle
#arg[1] AAddr
#arg[2] ASizeBytes
rpc_server_write_sync = dll.rpc_server_write_sync
rpc_server_write_sync.restype = s32
rpc_server_write_sync.argtypes = [size_t,pu8,size_t]

#arg[0] ARpcName
#arg[1] ABufferSizeBytes
#arg[2] AHandle
rpc_create_client = dll.rpc_create_client
rpc_create_client.restype = s32
rpc_create_client.argtypes = [pchar,size_t,psize_t]

#arg[0] AHandle
#arg[1] AActivate
rpc_activate_client = dll.rpc_activate_client
rpc_activate_client.restype = s32
rpc_activate_client.argtypes = [size_t,cbool]

#arg[0] AHandle
rpc_delete_client = dll.rpc_delete_client
rpc_delete_client.restype = s32
rpc_delete_client.argtypes = [size_t]

#arg[0] AHandle
#arg[1] AAddr
#arg[2] ASizeBytes
#arg[3] ATimeOutMs
rpc_client_transmit_sync = dll.rpc_client_transmit_sync
rpc_client_transmit_sync.restype = s32
rpc_client_transmit_sync.argtypes = [size_t,pu8,size_t,s32]

#arg[0] AHandle
#arg[1] ASizeBytes
#arg[2] AAddr
#arg[3] ATimeOutMs
rpc_client_receive_sync = dll.rpc_client_receive_sync
rpc_client_receive_sync.restype = s32
rpc_client_receive_sync.argtypes = [size_t,psize_t,pu8,s32]

#arg[0] AMasked
mask_fpu_exceptions = dll.mask_fpu_exceptions
mask_fpu_exceptions.restype = s32
mask_fpu_exceptions.argtypes = [cbool]

#arg[0] AActivate
rpc_tsmaster_activate_server = dll.rpc_tsmaster_activate_server
rpc_tsmaster_activate_server.restype = s32
rpc_tsmaster_activate_server.argtypes = [cbool]

#arg[0] ATSMasterAppName
#arg[1] AHandle
rpc_tsmaster_create_client = dll.rpc_tsmaster_create_client
rpc_tsmaster_create_client.restype = s32
rpc_tsmaster_create_client.argtypes = [pchar,psize_t]

#arg[0] AHandle
#arg[1] AActivate
rpc_tsmaster_activate_client = dll.rpc_tsmaster_activate_client
rpc_tsmaster_activate_client.restype = s32
rpc_tsmaster_activate_client.argtypes = [size_t,cbool]

#arg[0] AHandle
rpc_tsmaster_delete_client = dll.rpc_tsmaster_delete_client
rpc_tsmaster_delete_client.restype = s32
rpc_tsmaster_delete_client.argtypes = [size_t]

#arg[0] AHandle
rpc_tsmaster_cmd_start_simulation = dll.rpc_tsmaster_cmd_start_simulation
rpc_tsmaster_cmd_start_simulation.restype = s32
rpc_tsmaster_cmd_start_simulation.argtypes = [size_t]

#arg[0] AHandle
rpc_tsmaster_cmd_stop_simulation = dll.rpc_tsmaster_cmd_stop_simulation
rpc_tsmaster_cmd_stop_simulation.restype = s32
rpc_tsmaster_cmd_stop_simulation.argtypes = [size_t]

#arg[0] AHandle
#arg[1] ACompleteName
#arg[2] AValue
rpc_tsmaster_cmd_write_system_var = dll.rpc_tsmaster_cmd_write_system_var
rpc_tsmaster_cmd_write_system_var.restype = s32
rpc_tsmaster_cmd_write_system_var.argtypes = [size_t,pchar,pchar]

#arg[0] AHandle
#arg[1] AAddr
#arg[2] ASizeBytes
rpc_tsmaster_cmd_transfer_memory = dll.rpc_tsmaster_cmd_transfer_memory
rpc_tsmaster_cmd_transfer_memory.restype = s32
rpc_tsmaster_cmd_transfer_memory.argtypes = [size_t,pu8,size_t]

#arg[0] AHandle
#arg[1] AMsg
#arg[2] ALevel
rpc_tsmaster_cmd_log = dll.rpc_tsmaster_cmd_log
rpc_tsmaster_cmd_log.restype = s32
rpc_tsmaster_cmd_log.argtypes = [size_t,pchar,s32]

#arg[0] AHandle
rpc_tsmaster_cmd_set_mode_sim = dll.rpc_tsmaster_cmd_set_mode_sim
rpc_tsmaster_cmd_set_mode_sim.restype = s32
rpc_tsmaster_cmd_set_mode_sim.argtypes = [size_t]

#arg[0] AHandle
rpc_tsmaster_cmd_set_mode_realtime = dll.rpc_tsmaster_cmd_set_mode_realtime
rpc_tsmaster_cmd_set_mode_realtime.restype = s32
rpc_tsmaster_cmd_set_mode_realtime.argtypes = [size_t]

#arg[0] AHandle
rpc_tsmaster_cmd_set_mode_free = dll.rpc_tsmaster_cmd_set_mode_free
rpc_tsmaster_cmd_set_mode_free.restype = s32
rpc_tsmaster_cmd_set_mode_free.argtypes = [size_t]

#arg[0] AHandle
#arg[1] ATimeUs
rpc_tsmaster_cmd_sim_step = dll.rpc_tsmaster_cmd_sim_step
rpc_tsmaster_cmd_sim_step.restype = s32
rpc_tsmaster_cmd_sim_step.argtypes = [size_t,s64]

#arg[0] AAddress
#arg[1] ASizeBytes
create_process_shared_memory = dll.create_process_shared_memory
create_process_shared_memory.restype = s32
create_process_shared_memory.argtypes = [ppu8,s32]

#arg[0] AAddress
#arg[1] ASizeBytes
get_process_shared_memory = dll.get_process_shared_memory
get_process_shared_memory.restype = s32
get_process_shared_memory.argtypes = [ppu8,ps32]

#arg[0] AHandle
rpc_tsmaster_cmd_sim_step_batch_start = dll.rpc_tsmaster_cmd_sim_step_batch_start
rpc_tsmaster_cmd_sim_step_batch_start.restype = s32
rpc_tsmaster_cmd_sim_step_batch_start.argtypes = [size_t]

#arg[0] AHandle
#arg[1] ATimeUs
rpc_tsmaster_cmd_sim_step_batch_end = dll.rpc_tsmaster_cmd_sim_step_batch_end
rpc_tsmaster_cmd_sim_step_batch_end.restype = s32
rpc_tsmaster_cmd_sim_step_batch_end.argtypes = [size_t,s64]

#arg[0] AHandle
#arg[1] AProjectFullPath
rpc_tsmaster_cmd_get_project = dll.rpc_tsmaster_cmd_get_project
rpc_tsmaster_cmd_get_project.restype = s32
rpc_tsmaster_cmd_get_project.argtypes = [size_t,ppchar]

#arg[0] AHandle
#arg[1] ASysVarName
#arg[2] AValue
rpc_tsmaster_cmd_read_system_var = dll.rpc_tsmaster_cmd_read_system_var
rpc_tsmaster_cmd_read_system_var.restype = s32
rpc_tsmaster_cmd_read_system_var.argtypes = [size_t,pchar,pdouble]

#arg[0] AHandle
#arg[1] ABusType
#arg[2] AAddr
#arg[3] AValue
rpc_tsmaster_cmd_read_signal = dll.rpc_tsmaster_cmd_read_signal
rpc_tsmaster_cmd_read_signal.restype = s32
rpc_tsmaster_cmd_read_signal.argtypes = [size_t,TLIBApplicationChannelType,pchar,pdouble]

#arg[0] AHandle
#arg[1] ABusType
#arg[2] AAddr
#arg[3] AValue
rpc_tsmaster_cmd_write_signal = dll.rpc_tsmaster_cmd_write_signal
rpc_tsmaster_cmd_write_signal.restype = s32
rpc_tsmaster_cmd_write_signal.argtypes = [size_t,TLIBApplicationChannelType,pchar,double]

#arg[0] ASymbolAddress
can_rbs_set_normal_signal = dll.can_rbs_set_normal_signal
can_rbs_set_normal_signal.restype = s32
can_rbs_set_normal_signal.argtypes = [pchar]

#arg[0] ASymbolAddress
can_rbs_set_rc_signal = dll.can_rbs_set_rc_signal
can_rbs_set_rc_signal.restype = s32
can_rbs_set_rc_signal.argtypes = [pchar]

#arg[0] ASymbolAddress
#arg[1] ALowerLimit
#arg[2] AUpperLimit
can_rbs_set_rc_signal_with_limit = dll.can_rbs_set_rc_signal_with_limit
can_rbs_set_rc_signal_with_limit.restype = s32
can_rbs_set_rc_signal_with_limit.argtypes = [pchar,s32,s32]

#arg[0] ASymbolAddress
#arg[1] AAlgorithmName
#arg[2] AIdxByteStart
#arg[3] AByteCount
can_rbs_set_crc_signal = dll.can_rbs_set_crc_signal
can_rbs_set_crc_signal.restype = s32
can_rbs_set_crc_signal.argtypes = [pchar,pchar,s32,s32]

clear_user_constants = dll.clear_user_constants
clear_user_constants.restype = s32
clear_user_constants.argtypes = []

#arg[0] AHeaderFile
append_user_constants_from_c_header = dll.append_user_constants_from_c_header
append_user_constants_from_c_header.restype = s32
append_user_constants_from_c_header.argtypes = [pchar]

#arg[0] AConstantName
#arg[1] AValue
#arg[2] ADesc
append_user_constant = dll.append_user_constant
append_user_constant.restype = s32
append_user_constant.argtypes = [pchar,double,pchar]

#arg[0] AConstantName
delete_user_constant = dll.delete_user_constant
delete_user_constant.restype = s32
delete_user_constant.argtypes = [pchar]

#arg[0] ACount
get_mini_program_count = dll.get_mini_program_count
get_mini_program_count.restype = s32
get_mini_program_count.argtypes = [ps32]

#arg[0] AIndex
#arg[1] AKind
#arg[2] AProgramName
#arg[3] ADisplayName
get_mini_program_info_by_index = dll.get_mini_program_info_by_index
get_mini_program_info_by_index.restype = s32
get_mini_program_info_by_index.argtypes = [s32,ps32,ppchar,ppchar]

#arg[0] AProgramNames
compile_mini_programs = dll.compile_mini_programs
compile_mini_programs.restype = s32
compile_mini_programs.argtypes = [pchar]

#arg[0] ACompleteName
#arg[1] AValue
set_system_var_init_value = dll.set_system_var_init_value
set_system_var_init_value.restype = s32
set_system_var_init_value.argtypes = [pchar,pchar]

#arg[0] ACompleteName
#arg[1] AValue
get_system_var_init_value = dll.get_system_var_init_value
get_system_var_init_value.restype = s32
get_system_var_init_value.argtypes = [pchar,ppchar]

#arg[0] ACompleteName
reset_system_var_to_init = dll.reset_system_var_to_init
reset_system_var_to_init.restype = s32
reset_system_var_to_init.argtypes = [pchar]

#arg[0] AOwner
reset_all_system_var_to_init = dll.reset_all_system_var_to_init
reset_all_system_var_to_init.restype = s32
reset_all_system_var_to_init.argtypes = [pchar]

#arg[0] ACompleteName
#arg[1] AValue
get_system_var_generic_upg1 = dll.get_system_var_generic_upg1
get_system_var_generic_upg1.restype = s32
get_system_var_generic_upg1.argtypes = [pchar,ppchar]

#arg[0] AHandle
#arg[1] ASgnAddress
#arg[2] AValue
rpc_tsmaster_cmd_set_can_signal = dll.rpc_tsmaster_cmd_set_can_signal
rpc_tsmaster_cmd_set_can_signal.restype = s32
rpc_tsmaster_cmd_set_can_signal.argtypes = [size_t,pchar,double]

#arg[0] AHandle
#arg[1] ASgnAddress
#arg[2] AValue
rpc_tsmaster_cmd_get_can_signal = dll.rpc_tsmaster_cmd_get_can_signal
rpc_tsmaster_cmd_get_can_signal.restype = s32
rpc_tsmaster_cmd_get_can_signal.argtypes = [size_t,pchar,pdouble]

#arg[0] AHandle
#arg[1] ASgnAddress
#arg[2] AValue
rpc_tsmaster_cmd_get_lin_signal = dll.rpc_tsmaster_cmd_get_lin_signal
rpc_tsmaster_cmd_get_lin_signal.restype = s32
rpc_tsmaster_cmd_get_lin_signal.argtypes = [size_t,pchar,pdouble]

#arg[0] AHandle
#arg[1] ASgnAddress
#arg[2] AValue
rpc_tsmaster_cmd_set_lin_signal = dll.rpc_tsmaster_cmd_set_lin_signal
rpc_tsmaster_cmd_set_lin_signal.restype = s32
rpc_tsmaster_cmd_set_lin_signal.argtypes = [size_t,pchar,double]

#arg[0] AHandle
#arg[1] ASgnAddress
#arg[2] AValue
rpc_tsmaster_cmd_set_flexray_signal = dll.rpc_tsmaster_cmd_set_flexray_signal
rpc_tsmaster_cmd_set_flexray_signal.restype = s32
rpc_tsmaster_cmd_set_flexray_signal.argtypes = [size_t,pchar,double]

#arg[0] AHandle
#arg[1] ASgnAddress
#arg[2] AValue
rpc_tsmaster_cmd_get_flexray_signal = dll.rpc_tsmaster_cmd_get_flexray_signal
rpc_tsmaster_cmd_get_flexray_signal.restype = s32
rpc_tsmaster_cmd_get_flexray_signal.argtypes = [size_t,pchar,pdouble]

#arg[0] AHandle
#arg[1] AConstName
#arg[2] AValue
rpc_tsmaster_cmd_get_constant = dll.rpc_tsmaster_cmd_get_constant
rpc_tsmaster_cmd_get_constant.restype = s32
rpc_tsmaster_cmd_get_constant.argtypes = [size_t,pchar,pdouble]

#arg[0] AHandle
#arg[1] AIsRunning
rpc_tsmaster_is_simulation_running = dll.rpc_tsmaster_is_simulation_running
rpc_tsmaster_is_simulation_running.restype = s32
rpc_tsmaster_is_simulation_running.argtypes = [size_t,pbool]

#arg[0] AHandle
#arg[1] AAPIName
#arg[2] AArgCount
#arg[3] AArgCapacity
#arg[4] AArgs
rpc_tsmaster_call_system_api = dll.rpc_tsmaster_call_system_api
rpc_tsmaster_call_system_api.restype = s32
rpc_tsmaster_call_system_api.argtypes = [size_t,pchar,s32,s32,ppchar]

#arg[0] AHandle
#arg[1] AAPIName
#arg[2] AArgCount
#arg[3] AArgCapacity
#arg[4] AArgs
rpc_tsmaster_call_library_api = dll.rpc_tsmaster_call_library_api
rpc_tsmaster_call_library_api.restype = s32
rpc_tsmaster_call_library_api.argtypes = [size_t,pchar,s32,s32,ppchar]

#arg[0] ADirectory
get_tsmaster_binary_location = dll.get_tsmaster_binary_location
get_tsmaster_binary_location.restype = s32
get_tsmaster_binary_location.argtypes = [ppchar]

#arg[0] ATSMasterAppNames
get_active_application_list = dll.get_active_application_list
get_active_application_list.restype = s32
get_active_application_list.argtypes = [ppchar]

