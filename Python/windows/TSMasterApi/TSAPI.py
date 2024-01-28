from .TSDirver import *
from .TSStruct import * 
from .TSCallback import *
from .TSEnum import *
set_libtsmaster_location = dll.set_libtsmaster_location
#arg[0] AFilePath : None
set_libtsmaster_location.argtypes =[pchar]
set_libtsmaster_location.restype = s32
get_libtsmaster_location = dll.get_libtsmaster_location
#arg[0] AFilePath : None
get_libtsmaster_location.argtypes =[ppchar]
get_libtsmaster_location.restype = s32
initialize_lib_tsmaster = dll.initialize_lib_tsmaster
#arg[0] AAppName : None
initialize_lib_tsmaster.argtypes =[pchar]
initialize_lib_tsmaster.restype = s32
initialize_lib_tsmaster_with_project = dll.initialize_lib_tsmaster_with_project
#arg[0] AAppName : None
#arg[1] AProjectFileName : None
initialize_lib_tsmaster_with_project.argtypes =[pchar,pchar]
initialize_lib_tsmaster_with_project.restype = s32
tsapp_set_logger = dll.tsapp_set_logger
#arg[0] ALogger : None
tsapp_set_logger.argtypes =[TLIBTSMasterLogger]
tsapp_set_logger.restype = s32
tsapp_log = dll.tsapp_log
#arg[0] AStr : output string
#arg[1] ALevel : output level
tsapp_log.argtypes =[pchar,s32]
tsapp_log.restype = s32
tsapp_set_current_application = dll.tsapp_set_current_application
#arg[0] AAppName : APP name
tsapp_set_current_application.argtypes =[pchar]
tsapp_set_current_application.restype = s32
tsapp_get_current_application = dll.tsapp_get_current_application
#arg[0] AAppName : APP name
tsapp_get_current_application.argtypes =[ppchar]
tsapp_get_current_application.restype = s32
tsapp_del_application = dll.tsapp_del_application
#arg[0] AAppName : APP name
tsapp_del_application.argtypes =[pchar]
tsapp_del_application.restype = s32
tsapp_add_application = dll.tsapp_add_application
#arg[0] AAppName : APP name
tsapp_add_application.argtypes =[pchar]
tsapp_add_application.restype = s32
tsapp_get_application_list = dll.tsapp_get_application_list
#arg[0] AAppNameList : None
tsapp_get_application_list.argtypes =[ppchar]
tsapp_get_application_list.restype = s32
tsapp_set_can_channel_count = dll.tsapp_set_can_channel_count
#arg[0] ACount : None
tsapp_set_can_channel_count.argtypes =[s32]
tsapp_set_can_channel_count.restype = s32
tsapp_set_lin_channel_count = dll.tsapp_set_lin_channel_count
#arg[0] ACount : None
tsapp_set_lin_channel_count.argtypes =[s32]
tsapp_set_lin_channel_count.restype = s32
tsapp_set_flexray_channel_count = dll.tsapp_set_flexray_channel_count
#arg[0] ACount : None
tsapp_set_flexray_channel_count.argtypes =[s32]
tsapp_set_flexray_channel_count.restype = s32
tsapp_get_can_channel_count = dll.tsapp_get_can_channel_count
#arg[0] ACount : None
tsapp_get_can_channel_count.argtypes =[ps32]
tsapp_get_can_channel_count.restype = s32
tsapp_get_lin_channel_count = dll.tsapp_get_lin_channel_count
#arg[0] ACount : None
tsapp_get_lin_channel_count.argtypes =[ps32]
tsapp_get_lin_channel_count.restype = s32
tsapp_get_flexray_channel_count = dll.tsapp_get_flexray_channel_count
#arg[0] ACount : None
tsapp_get_flexray_channel_count.argtypes =[ps32]
tsapp_get_flexray_channel_count.restype = s32
tsapp_set_mapping = dll.tsapp_set_mapping
#arg[0] AMapping : None
tsapp_set_mapping.argtypes =[PLIBTSMapping]
tsapp_set_mapping.restype = s32
tsapp_set_mapping_verbose = dll.tsapp_set_mapping_verbose
#arg[0] AAppName : None
#arg[1] AAppChannelType : None
#arg[2] AAppChannel : APP_CHANNEL
#arg[3] AHardwareName : None
#arg[4] AHardwareType : None
#arg[5] AHardwareSubType : None
#arg[6] AHardwareIndex : None
#arg[7] AHardwareChannel : HARDWARE_CHANNEL
#arg[8] AEnableMapping : None
tsapp_set_mapping_verbose.argtypes =[pchar,s32,s32,pchar,s32,s32,s32,s32,c_bool]
tsapp_set_mapping_verbose.restype = s32
tsapp_get_mapping = dll.tsapp_get_mapping
#arg[0] AMapping : None
tsapp_get_mapping.argtypes =[PLIBTSMapping]
tsapp_get_mapping.restype = s32
tsapp_del_mapping = dll.tsapp_del_mapping
#arg[0] AMapping : None
tsapp_del_mapping.argtypes =[PLIBTSMapping]
tsapp_del_mapping.restype = s32
tsapp_del_mapping_verbose = dll.tsapp_del_mapping_verbose
#arg[0] AAppName : None
#arg[1] AAppChannelType : None
#arg[2] AAppChannel : None
tsapp_del_mapping_verbose.argtypes =[pchar,s32,s32]
tsapp_del_mapping_verbose.restype = s32
tsapp_connect = dll.tsapp_connect
tsapp_connect.argtypes =[]
tsapp_connect.restype = s32
tsapp_disconnect = dll.tsapp_disconnect
tsapp_disconnect.argtypes =[]
tsapp_disconnect.restype = s32
tsapp_set_turbo_mode = dll.tsapp_set_turbo_mode
#arg[0] AEnable : None
tsapp_set_turbo_mode.argtypes =[c_bool]
tsapp_set_turbo_mode.restype = s32
tsapp_get_turbo_mode = dll.tsapp_get_turbo_mode
#arg[0] AEnable : None
tsapp_get_turbo_mode.argtypes =[pbool]
tsapp_get_turbo_mode.restype = s32
tsapp_get_error_description = dll.tsapp_get_error_description
#arg[0] ACode : None
#arg[1] ADesc : None
tsapp_get_error_description.argtypes =[s32,ppchar]
tsapp_get_error_description.restype = s32
tsapp_show_channel_mapping_window = dll.tsapp_show_channel_mapping_window
tsapp_show_channel_mapping_window.argtypes =[]
tsapp_show_channel_mapping_window.restype = s32
tsapp_show_hardware_configuration_window = dll.tsapp_show_hardware_configuration_window
tsapp_show_hardware_configuration_window.argtypes =[]
tsapp_show_hardware_configuration_window.restype = s32
tsapp_show_tsmaster_window = dll.tsapp_show_tsmaster_window
#arg[0] AWindowName : None
#arg[1] AWaitClose : None
tsapp_show_tsmaster_window.argtypes =[pchar,c_bool]
tsapp_show_tsmaster_window.restype = s32
tsapp_get_timestamp = dll.tsapp_get_timestamp
#arg[0] ATimeUs : None
tsapp_get_timestamp.argtypes =[ps64]
tsapp_get_timestamp.restype = s32
tsapp_execute_python_string = dll.tsapp_execute_python_string
#arg[0] AString : None
#arg[1] AArguments : None
#arg[2] ASync : None
#arg[3] AIsX64 : None
#arg[4] AResultLog : None
tsapp_execute_python_string.argtypes =[pchar,pchar,c_bool,c_bool,ppchar]
tsapp_execute_python_string.restype = s32
tsapp_execute_python_script = dll.tsapp_execute_python_script
#arg[0] AFilePath : None
#arg[1] AArguments : None
#arg[2] ASync : None
#arg[3] AIsX64 : None
#arg[4] AResultLog : None
tsapp_execute_python_script.argtypes =[pchar,pchar,c_bool,c_bool,ppchar]
tsapp_execute_python_script.restype = s32
tsapp_get_tsmaster_version = dll.tsapp_get_tsmaster_version
#arg[0] AYear : None
#arg[1] AMonth : None
#arg[2] ADay : None
#arg[3] ABuildNumber : None
tsapp_get_tsmaster_version.argtypes =[ps32,ps32,ps32,ps32]
tsapp_get_tsmaster_version.restype = s32
tsapp_get_system_constant_count = dll.tsapp_get_system_constant_count
#arg[0] AIdxType : None
#arg[1] ACount : None
tsapp_get_system_constant_count.argtypes =[s32,ps32]
tsapp_get_system_constant_count.restype = s32
tsapp_get_system_constant_value_by_index = dll.tsapp_get_system_constant_value_by_index
#arg[0] AIdxType : None
#arg[1] AIdxValue : None
#arg[2] AName : None
#arg[3] AValue : None
#arg[4] ADesc : None
tsapp_get_system_constant_value_by_index.argtypes =[s32,s32,ppchar,pdouble,ppchar]
tsapp_get_system_constant_value_by_index.restype = s32
tsapp_enumerate_hw_devices = dll.tsapp_enumerate_hw_devices
#arg[0] ACount : None
tsapp_enumerate_hw_devices.argtypes =[ps32]
tsapp_enumerate_hw_devices.restype = s32
tsapp_get_hw_info_by_index = dll.tsapp_get_hw_info_by_index
#arg[0] AIndex : None
#arg[1] AHWInfo : None
tsapp_get_hw_info_by_index.argtypes =[s32,PLIBHWInfo]
tsapp_get_hw_info_by_index.restype = s32
tsapp_get_hw_info_by_index_verbose = dll.tsapp_get_hw_info_by_index_verbose
#arg[0] AIndex : None
#arg[1] ADeviceType : None
#arg[2] AVendorNameBuffer : array[0..31] of AnsiChar;
#arg[3] AVendorNameBufferSize : None
#arg[4] ADeviceNameBuffer : array[0..31] of AnsiChar;
#arg[5] ADeviceNameBufferSize : None
#arg[6] ASerialStringBuffer : array[0..63] of AnsiChar;
#arg[7] ASerialStringBufferSize : None
tsapp_get_hw_info_by_index_verbose.argtypes =[s32,ps32,pchar,s32,pchar,s32,pchar,s32]
tsapp_get_hw_info_by_index_verbose.restype = s32
tsapp_set_vendor_detect_preferences = dll.tsapp_set_vendor_detect_preferences
#arg[0] AScanTOSUN : None
#arg[1] AScanVector : None
#arg[2] AScanPeak : None
#arg[3] AScanKvaser : None
#arg[4] AScanZLG : None
#arg[5] ADetectIntrepidcs : None
#arg[6] ADetectCANable : None
tsapp_set_vendor_detect_preferences.argtypes =[c_bool,c_bool,c_bool,c_bool,c_bool,c_bool,c_bool]
tsapp_set_vendor_detect_preferences.restype = s32
tsapp_get_vendor_detect_preferences = dll.tsapp_get_vendor_detect_preferences
#arg[0] AScanTOSUN : None
#arg[1] AScanVector : None
#arg[2] AScanPeak : None
#arg[3] AScanKvaser : None
#arg[4] AScanZLG : None
#arg[5] ADetectIntrepidcs : None
#arg[6] ADetectCANable : None
tsapp_get_vendor_detect_preferences.argtypes =[c_bool,c_bool,c_bool,c_bool,c_bool,c_bool,c_bool]
tsapp_get_vendor_detect_preferences.restype = s32
tsapp_configure_baudrate_lin = dll.tsapp_configure_baudrate_lin
#arg[0] AIndex : None
#arg[1] ABaudrateKbps : None
#arg[2] AProtocol : None
tsapp_configure_baudrate_lin.argtypes =[s32,single,s32]
tsapp_configure_baudrate_lin.restype = s32
tsapp_configure_baudrate_can = dll.tsapp_configure_baudrate_can
#arg[0] AIndex : None
#arg[1] ABaudrateKbps : None
#arg[2] AListenOnly : None
#arg[3] AInstallTermResistor120Ohm : None
tsapp_configure_baudrate_can.argtypes =[s32,single,c_bool,c_bool]
tsapp_configure_baudrate_can.restype = s32
tsapp_configure_baudrate_canfd = dll.tsapp_configure_baudrate_canfd
#arg[0] AIndex : None
#arg[1] AArbRateKbps : None
#arg[2] ADataRateKbps : None
#arg[3] AControllerType : None
#arg[4] AControllerMode : None
#arg[5] AInstallTermResistor120Ohm : None
tsapp_configure_baudrate_canfd.argtypes =[s32,single,single,s32,s32,c_bool]
tsapp_configure_baudrate_canfd.restype = s32
tsapp_configure_can_regs = dll.tsapp_configure_can_regs
#arg[0] AIndex : None
#arg[1] ABaudrateKbps : None
#arg[2] ASEG1 : None
#arg[3] ASEG2 : None
#arg[4] APrescaler : None
#arg[5] ASJW : None
#arg[6] AOnlyListen : None
#arg[7] A120OhmConnected : None
tsapp_configure_can_regs.argtypes =[s32,single,s32,s32,s32,s32,s32,s32]
tsapp_configure_can_regs.restype = s32
tsapp_configure_canfd_regs = dll.tsapp_configure_canfd_regs
#arg[0] AIndex : None
#arg[1] AArbBaudrate : None
#arg[2] AArbSEG1 : None
#arg[3] AArbSEG2 : None
#arg[4] AArbPrescaler : None
#arg[5] AArbSJW : None
#arg[6] ADataBaudrate : None
#arg[7] ADataSEG1 : None
#arg[8] ADataSEG2 : None
#arg[9] ADataPrescaler : None
#arg[10] ADataSJW : None
#arg[11] AControllerType : None
#arg[12] AControllerMode : None
#arg[13] A120OhmConnected : None
tsapp_configure_canfd_regs.argtypes =[s32,single,s32,s32,s32,s32,single,s32,s32,s32,s32,s32,s32,s32]
tsapp_configure_canfd_regs.restype = s32
tsapp_transmit_can_async = dll.tsapp_transmit_can_async
#arg[0] ACAN : None
tsapp_transmit_can_async.argtypes =[PLIBCAN]
tsapp_transmit_can_async.restype = s32
tsapp_transmit_canfd_async = dll.tsapp_transmit_canfd_async
#arg[0] ACANFD : None
tsapp_transmit_canfd_async.argtypes =[PLIBCANFD]
tsapp_transmit_canfd_async.restype = s32
tsapp_transmit_lin_async = dll.tsapp_transmit_lin_async
#arg[0] ALIN : None
tsapp_transmit_lin_async.argtypes =[PLIBLIN]
tsapp_transmit_lin_async.restype = s32
tsapp_transmit_fastlin_async = dll.tsapp_transmit_fastlin_async
#arg[0] ALIN : None
tsapp_transmit_fastlin_async.argtypes =[PLIBLIN]
tsapp_transmit_fastlin_async.restype = s32
tsapp_transmit_lin_wakeup_async = dll.tsapp_transmit_lin_wakeup_async
#arg[0] AIdxChn : None
#arg[1] AWakeupLength : None
#arg[2] AWakeupIntervalTime : None
#arg[3] AWakeupTimes : None
tsapp_transmit_lin_wakeup_async.argtypes =[s32,s32,s32,s32]
tsapp_transmit_lin_wakeup_async.restype = s32
tsapp_transmit_lin_gotosleep_async = dll.tsapp_transmit_lin_gotosleep_async
#arg[0] AIdxChn : None
tsapp_transmit_lin_gotosleep_async.argtypes =[s32]
tsapp_transmit_lin_gotosleep_async.restype = s32
tsapp_transmit_can_sync = dll.tsapp_transmit_can_sync
#arg[0] ACAN : None
#arg[1] ATimeoutMS : None
tsapp_transmit_can_sync.argtypes =[PLIBCAN,s32]
tsapp_transmit_can_sync.restype = s32
tsapp_transmit_canfd_sync = dll.tsapp_transmit_canfd_sync
#arg[0] ACANfd : None
#arg[1] ATimeoutMS : None
tsapp_transmit_canfd_sync.argtypes =[PLIBCANFD,s32]
tsapp_transmit_canfd_sync.restype = s32
tsapp_transmit_lin_sync = dll.tsapp_transmit_lin_sync
#arg[0] ALIN : None
#arg[1] ATimeoutMS : None
tsapp_transmit_lin_sync.argtypes =[PLIBLIN,s32]
tsapp_transmit_lin_sync.restype = s32
tsfifo_enable_receive_fifo = dll.tsfifo_enable_receive_fifo
tsfifo_enable_receive_fifo.argtypes =[]
tsfifo_enable_receive_fifo.restype = s32
tsfifo_disable_receive_fifo = dll.tsfifo_disable_receive_fifo
tsfifo_disable_receive_fifo.argtypes =[]
tsfifo_disable_receive_fifo.restype = s32
tsfifo_add_can_canfd_pass_filter = dll.tsfifo_add_can_canfd_pass_filter
#arg[0] AIdxChn : None
#arg[1] AIdentifier : None
#arg[2] AIsStd : None
tsfifo_add_can_canfd_pass_filter.argtypes =[s32,s32,c_bool]
tsfifo_add_can_canfd_pass_filter.restype = s32
tsfifo_add_lin_pass_filter = dll.tsfifo_add_lin_pass_filter
#arg[0] AIdxChn : None
#arg[1] AIdentifier : None
tsfifo_add_lin_pass_filter.argtypes =[s32,s32]
tsfifo_add_lin_pass_filter.restype = s32
tsfifo_delete_can_canfd_pass_filter = dll.tsfifo_delete_can_canfd_pass_filter
#arg[0] AIdxChn : None
#arg[1] AIdentifier : None
tsfifo_delete_can_canfd_pass_filter.argtypes =[s32,s32]
tsfifo_delete_can_canfd_pass_filter.restype = s32
tsfifo_delete_lin_pass_filter = dll.tsfifo_delete_lin_pass_filter
#arg[0] AIdxChn : None
#arg[1] AIdentifier : None
tsfifo_delete_lin_pass_filter.argtypes =[s32,s32]
tsfifo_delete_lin_pass_filter.restype = s32
tsfifo_receive_can_msgs = dll.tsfifo_receive_can_msgs
#arg[0] ACANBuffers : None
#arg[1] ACANBufferSize : None
#arg[2] AIdxChn : None
#arg[3] AIncludeTx : None
tsfifo_receive_can_msgs.argtypes =[PLIBCAN,ps32,s32,c_bool]
tsfifo_receive_can_msgs.restype = s32
tsfifo_receive_canfd_msgs = dll.tsfifo_receive_canfd_msgs
#arg[0] ACANFDBuffers : None
#arg[1] ACANFDBufferSize : None
#arg[2] AIdxChn : None
#arg[3] AIncludeTx : None
tsfifo_receive_canfd_msgs.argtypes =[PLIBCANFD,ps32,s32,c_bool]
tsfifo_receive_canfd_msgs.restype = s32
tsfifo_receive_lin_msgs = dll.tsfifo_receive_lin_msgs
#arg[0] ALINBuffers : None
#arg[1] ALINBufferSize : None
#arg[2] AIdxChn : None
#arg[3] AIncludeTx : None
tsfifo_receive_lin_msgs.argtypes =[PLIBLIN,ps32,s32,c_bool]
tsfifo_receive_lin_msgs.restype = s32
tsfifo_receive_fastlin_msgs = dll.tsfifo_receive_fastlin_msgs
#arg[0] AFastLINBuffers : None
#arg[1] AFastLINBufferSize : None
#arg[2] AIdxChn : None
#arg[3] AIncludeTx : None
tsfifo_receive_fastlin_msgs.argtypes =[PLIBLIN,ps32,s32,c_bool]
tsfifo_receive_fastlin_msgs.restype = s32
tsfifo_clear_can_receive_buffers = dll.tsfifo_clear_can_receive_buffers
#arg[0] AIdxChn : None
tsfifo_clear_can_receive_buffers.argtypes =[s32]
tsfifo_clear_can_receive_buffers.restype = s32
tsfifo_clear_canfd_receive_buffers = dll.tsfifo_clear_canfd_receive_buffers
#arg[0] AIdxChn : None
tsfifo_clear_canfd_receive_buffers.argtypes =[s32]
tsfifo_clear_canfd_receive_buffers.restype = s32
tsfifo_clear_lin_receive_buffers = dll.tsfifo_clear_lin_receive_buffers
#arg[0] AIdxChn : None
tsfifo_clear_lin_receive_buffers.argtypes =[s32]
tsfifo_clear_lin_receive_buffers.restype = s32
tsfifo_clear_fastlin_receive_buffers = dll.tsfifo_clear_fastlin_receive_buffers
#arg[0] AIdxChn : None
tsfifo_clear_fastlin_receive_buffers.argtypes =[s32]
tsfifo_clear_fastlin_receive_buffers.restype = s32
tsfifo_read_can_buffer_frame_count = dll.tsfifo_read_can_buffer_frame_count
#arg[0] AIdxChn : None
#arg[1] ACount : None
tsfifo_read_can_buffer_frame_count.argtypes =[s32,ps32]
tsfifo_read_can_buffer_frame_count.restype = s32
tsfifo_read_can_tx_buffer_frame_count = dll.tsfifo_read_can_tx_buffer_frame_count
#arg[0] AIdxChn : None
#arg[1] ACount : None
tsfifo_read_can_tx_buffer_frame_count.argtypes =[s32,ps32]
tsfifo_read_can_tx_buffer_frame_count.restype = s32
tsfifo_read_can_rx_buffer_frame_count = dll.tsfifo_read_can_rx_buffer_frame_count
#arg[0] AIdxChn : None
#arg[1] ACount : None
tsfifo_read_can_rx_buffer_frame_count.argtypes =[s32,ps32]
tsfifo_read_can_rx_buffer_frame_count.restype = s32
tsfifo_read_canfd_buffer_frame_count = dll.tsfifo_read_canfd_buffer_frame_count
#arg[0] AIdxChn : None
#arg[1] ACount : None
tsfifo_read_canfd_buffer_frame_count.argtypes =[s32,ps32]
tsfifo_read_canfd_buffer_frame_count.restype = s32
tsfifo_read_canfd_tx_buffer_frame_count = dll.tsfifo_read_canfd_tx_buffer_frame_count
#arg[0] AIdxChn : None
#arg[1] ACount : None
tsfifo_read_canfd_tx_buffer_frame_count.argtypes =[s32,ps32]
tsfifo_read_canfd_tx_buffer_frame_count.restype = s32
tsfifo_read_canfd_rx_buffer_frame_count = dll.tsfifo_read_canfd_rx_buffer_frame_count
#arg[0] AIdxChn : None
#arg[1] ACount : None
tsfifo_read_canfd_rx_buffer_frame_count.argtypes =[s32,ps32]
tsfifo_read_canfd_rx_buffer_frame_count.restype = s32
tsfifo_read_lin_buffer_frame_count = dll.tsfifo_read_lin_buffer_frame_count
#arg[0] AIdxChn : None
#arg[1] ACount : None
tsfifo_read_lin_buffer_frame_count.argtypes =[s32,ps32]
tsfifo_read_lin_buffer_frame_count.restype = s32
tsfifo_read_lin_tx_buffer_frame_count = dll.tsfifo_read_lin_tx_buffer_frame_count
#arg[0] AIdxChn : None
#arg[1] ACount : None
tsfifo_read_lin_tx_buffer_frame_count.argtypes =[s32,ps32]
tsfifo_read_lin_tx_buffer_frame_count.restype = s32
tsfifo_read_lin_rx_buffer_frame_count = dll.tsfifo_read_lin_rx_buffer_frame_count
#arg[0] AIdxChn : None
#arg[1] ACount : None
tsfifo_read_lin_rx_buffer_frame_count.argtypes =[s32,ps32]
tsfifo_read_lin_rx_buffer_frame_count.restype = s32
tsfifo_read_fastlin_buffer_frame_count = dll.tsfifo_read_fastlin_buffer_frame_count
#arg[0] AIdxChn : None
#arg[1] ACount : None
tsfifo_read_fastlin_buffer_frame_count.argtypes =[s32,ps32]
tsfifo_read_fastlin_buffer_frame_count.restype = s32
tsfifo_read_fastlin_tx_buffer_frame_count = dll.tsfifo_read_fastlin_tx_buffer_frame_count
#arg[0] AIdxChn : None
#arg[1] ACount : None
tsfifo_read_fastlin_tx_buffer_frame_count.argtypes =[s32,ps32]
tsfifo_read_fastlin_tx_buffer_frame_count.restype = s32
tsfifo_read_fastlin_rx_buffer_frame_count = dll.tsfifo_read_fastlin_rx_buffer_frame_count
#arg[0] AIdxChn : None
#arg[1] ACount : None
tsfifo_read_fastlin_rx_buffer_frame_count.argtypes =[s32,ps32]
tsfifo_read_fastlin_rx_buffer_frame_count.restype = s32
tsfifo_receive_flexray_msgs = dll.tsfifo_receive_flexray_msgs
#arg[0] ADataBuffers : None
#arg[1] ADataBufferSize : None
#arg[2] AIdxChn : None
#arg[3] AIncludeTx : None
tsfifo_receive_flexray_msgs.argtypes =[PLIBFlexRay,ps32,s32,c_bool]
tsfifo_receive_flexray_msgs.restype = s32
tsfifo_clear_flexray_receive_buffers = dll.tsfifo_clear_flexray_receive_buffers
#arg[0] AIdxChn : None
tsfifo_clear_flexray_receive_buffers.argtypes =[s32]
tsfifo_clear_flexray_receive_buffers.restype = s32
tsfifo_read_flexray_buffer_frame_count = dll.tsfifo_read_flexray_buffer_frame_count
#arg[0] AIdxChn : None
#arg[1] ACount : None
tsfifo_read_flexray_buffer_frame_count.argtypes =[s32,ps32]
tsfifo_read_flexray_buffer_frame_count.restype = s32
tsfifo_read_flexray_tx_buffer_frame_count = dll.tsfifo_read_flexray_tx_buffer_frame_count
#arg[0] AIdxChn : None
#arg[1] ACount : None
tsfifo_read_flexray_tx_buffer_frame_count.argtypes =[s32,ps32]
tsfifo_read_flexray_tx_buffer_frame_count.restype = s32
tsfifo_read_flexray_rx_buffer_frame_count = dll.tsfifo_read_flexray_rx_buffer_frame_count
#arg[0] AIdxChn : None
#arg[1] ACount : None
tsfifo_read_flexray_rx_buffer_frame_count.argtypes =[s32,ps32]
tsfifo_read_flexray_rx_buffer_frame_count.restype = s32
tsapp_add_cyclic_msg_can = dll.tsapp_add_cyclic_msg_can
#arg[0] ACAN : None
#arg[1] APeriodMS : None
tsapp_add_cyclic_msg_can.argtypes =[PLIBCAN,single]
tsapp_add_cyclic_msg_can.restype = s32
tsapp_update_cyclic_msg_can = dll.tsapp_update_cyclic_msg_can
#arg[0] ACAN : None
tsapp_update_cyclic_msg_can.argtypes =[PLIBCAN]
tsapp_update_cyclic_msg_can.restype = s32
tsapp_add_cyclic_msg_canfd = dll.tsapp_add_cyclic_msg_canfd
#arg[0] ACANFD : None
#arg[1] APeriodMS : None
tsapp_add_cyclic_msg_canfd.argtypes =[PLIBCANFD,single]
tsapp_add_cyclic_msg_canfd.restype = s32
tsapp_delete_cyclic_msg_can = dll.tsapp_delete_cyclic_msg_can
#arg[0] ACAN : None
tsapp_delete_cyclic_msg_can.argtypes =[PLIBCAN]
tsapp_delete_cyclic_msg_can.restype = s32
tsapp_delete_cyclic_msg_canfd = dll.tsapp_delete_cyclic_msg_canfd
#arg[0] ACANFD : None
tsapp_delete_cyclic_msg_canfd.argtypes =[PLIBCANFD]
tsapp_delete_cyclic_msg_canfd.restype = s32
tsapp_delete_cyclic_msgs = dll.tsapp_delete_cyclic_msgs
tsapp_delete_cyclic_msgs.argtypes =[]
tsapp_delete_cyclic_msgs.restype = s32
tsapp_enable_bus_statistics = dll.tsapp_enable_bus_statistics
#arg[0] AEnable : None
tsapp_enable_bus_statistics.argtypes =[c_bool]
tsapp_enable_bus_statistics.restype = s32
tsapp_clear_bus_statistics = dll.tsapp_clear_bus_statistics
tsapp_clear_bus_statistics.argtypes =[]
tsapp_clear_bus_statistics.restype = s32
tsapp_get_bus_statistics = dll.tsapp_get_bus_statistics
#arg[0] ABusType : None
#arg[1] AIdxChn : None
#arg[2] AIdxStat : None
#arg[3] AStat : None
tsapp_get_bus_statistics.argtypes =[s32,s32,s32,pdouble]
tsapp_get_bus_statistics.restype = s32
tsapp_get_fps_can = dll.tsapp_get_fps_can
#arg[0] AIdxChn : None
#arg[1] AIdentifier : None
#arg[2] AFPS : None
tsapp_get_fps_can.argtypes =[s32,s32,ps32]
tsapp_get_fps_can.restype = s32
tsapp_get_fps_canfd = dll.tsapp_get_fps_canfd
#arg[0] AIdxChn : None
#arg[1] AIdentifier : None
#arg[2] AFPS : None
tsapp_get_fps_canfd.argtypes =[s32,s32,ps32]
tsapp_get_fps_canfd.restype = s32
tsapp_get_fps_lin = dll.tsapp_get_fps_lin
#arg[0] AIdxChn : None
#arg[1] AIdentifier : None
#arg[2] AFPS : None
tsapp_get_fps_lin.argtypes =[s32,s32,ps32]
tsapp_get_fps_lin.restype = s32
tsapp_register_event_gps = dll.tsapp_register_event_gps
#arg[0] AObj : None
#arg[1] AEvent : None
tsapp_register_event_gps.argtypes =[ps32,TGPSQueueEvent_Win32]
tsapp_register_event_gps.restype = s32
tsapp_unregister_event_gps = dll.tsapp_unregister_event_gps
#arg[0] AObj : None
#arg[1] AEvent : None
tsapp_unregister_event_gps.argtypes =[ps32,TGPSQueueEvent_Win32]
tsapp_unregister_event_gps.restype = s32
tsapp_register_event_can = dll.tsapp_register_event_can
#arg[0] AObj : None
#arg[1] AEvent : None
tsapp_register_event_can.argtypes =[ps32,TCANQueueEvent_Win32]
tsapp_register_event_can.restype = s32
tsapp_unregister_event_can = dll.tsapp_unregister_event_can
#arg[0] AObj : None
#arg[1] AEvent : None
tsapp_unregister_event_can.argtypes =[ps32,TCANQueueEvent_Win32]
tsapp_unregister_event_can.restype = s32
tsapp_register_event_canfd = dll.tsapp_register_event_canfd
#arg[0] AObj : None
#arg[1] AEvent : None
tsapp_register_event_canfd.argtypes =[ps32,TCANFDQueueEvent_Win32]
tsapp_register_event_canfd.restype = s32
tsapp_unregister_event_canfd = dll.tsapp_unregister_event_canfd
#arg[0] AObj : None
#arg[1] AEvent : None
tsapp_unregister_event_canfd.argtypes =[ps32,TCANFDQueueEvent_Win32]
tsapp_unregister_event_canfd.restype = s32
tsapp_register_event_lin = dll.tsapp_register_event_lin
#arg[0] AObj : None
#arg[1] AEvent : None
tsapp_register_event_lin.argtypes =[ps32,TLINQueueEvent_Win32]
tsapp_register_event_lin.restype = s32
tsapp_unregister_event_lin = dll.tsapp_unregister_event_lin
#arg[0] AObj : None
#arg[1] AEvent : None
tsapp_unregister_event_lin.argtypes =[ps32,TLINQueueEvent_Win32]
tsapp_unregister_event_lin.restype = s32
tsapp_register_event_flexray = dll.tsapp_register_event_flexray
#arg[0] AObj : None
#arg[1] AEvent : None
tsapp_register_event_flexray.argtypes =[ps32,TFlexRayQueueEvent_Win32]
tsapp_register_event_flexray.restype = s32
tsapp_unregister_event_flexray = dll.tsapp_unregister_event_flexray
#arg[0] AObj : None
#arg[1] AEvent : None
tsapp_unregister_event_flexray.argtypes =[ps32,TFlexRayQueueEvent_Win32]
tsapp_unregister_event_flexray.restype = s32
tsapp_unregister_events_flexray = dll.tsapp_unregister_events_flexray
#arg[0] AObj : None
tsapp_unregister_events_flexray.argtypes =[ps32]
tsapp_unregister_events_flexray.restype = s32
tsapp_unregister_events_can = dll.tsapp_unregister_events_can
#arg[0] AObj : None
tsapp_unregister_events_can.argtypes =[ps32]
tsapp_unregister_events_can.restype = s32
tsapp_unregister_events_lin = dll.tsapp_unregister_events_lin
#arg[0] AObj : None
tsapp_unregister_events_lin.argtypes =[ps32]
tsapp_unregister_events_lin.restype = s32
tsapp_unregister_events_canfd = dll.tsapp_unregister_events_canfd
#arg[0] AObj : None
tsapp_unregister_events_canfd.argtypes =[ps32]
tsapp_unregister_events_canfd.restype = s32
tsapp_unregister_events_all = dll.tsapp_unregister_events_all
#arg[0] AObj : None
tsapp_unregister_events_all.argtypes =[ps32]
tsapp_unregister_events_all.restype = s32
tsapp_register_pretx_event_can = dll.tsapp_register_pretx_event_can
#arg[0] AObj : None
#arg[1] AEvent : None
tsapp_register_pretx_event_can.argtypes =[ps32,TCANQueueEvent_Win32]
tsapp_register_pretx_event_can.restype = s32
tsapp_unregister_pretx_event_can = dll.tsapp_unregister_pretx_event_can
#arg[0] AObj : None
#arg[1] AEvent : None
tsapp_unregister_pretx_event_can.argtypes =[ps32,TCANQueueEvent_Win32]
tsapp_unregister_pretx_event_can.restype = s32
tsapp_register_pretx_event_canfd = dll.tsapp_register_pretx_event_canfd
#arg[0] AObj : None
#arg[1] AEvent : None
tsapp_register_pretx_event_canfd.argtypes =[ps32,TCANFDQueueEvent_Win32]
tsapp_register_pretx_event_canfd.restype = s32
tsapp_unregister_pretx_event_canfd = dll.tsapp_unregister_pretx_event_canfd
#arg[0] AObj : None
#arg[1] AEvent : None
tsapp_unregister_pretx_event_canfd.argtypes =[ps32,TCANFDQueueEvent_Win32]
tsapp_unregister_pretx_event_canfd.restype = s32
tsapp_register_pretx_event_lin = dll.tsapp_register_pretx_event_lin
#arg[0] AObj : None
#arg[1] AEvent : None
tsapp_register_pretx_event_lin.argtypes =[ps32,TLINQueueEvent_Win32]
tsapp_register_pretx_event_lin.restype = s32
tsapp_unregister_pretx_event_lin = dll.tsapp_unregister_pretx_event_lin
#arg[0] AObj : None
#arg[1] AEvent : None
tsapp_unregister_pretx_event_lin.argtypes =[ps32,TLINQueueEvent_Win32]
tsapp_unregister_pretx_event_lin.restype = s32
tsapp_register_pretx_event_flexray = dll.tsapp_register_pretx_event_flexray
#arg[0] AObj : None
#arg[1] AEvent : None
tsapp_register_pretx_event_flexray.argtypes =[ps32,TFlexRayQueueEvent_Win32]
tsapp_register_pretx_event_flexray.restype = s32
tsapp_unregister_pretx_event_flexray = dll.tsapp_unregister_pretx_event_flexray
#arg[0] AObj : None
#arg[1] AEvent : None
tsapp_unregister_pretx_event_flexray.argtypes =[ps32,TFlexRayQueueEvent_Win32]
tsapp_unregister_pretx_event_flexray.restype = s32
tsapp_unregister_pretx_events_flexray = dll.tsapp_unregister_pretx_events_flexray
#arg[0] AObj : None
tsapp_unregister_pretx_events_flexray.argtypes =[ps32]
tsapp_unregister_pretx_events_flexray.restype = s32
tsapp_unregister_pretx_events_can = dll.tsapp_unregister_pretx_events_can
#arg[0] AObj : None
tsapp_unregister_pretx_events_can.argtypes =[ps32]
tsapp_unregister_pretx_events_can.restype = s32
tsapp_unregister_pretx_events_lin = dll.tsapp_unregister_pretx_events_lin
#arg[0] AObj : None
tsapp_unregister_pretx_events_lin.argtypes =[ps32]
tsapp_unregister_pretx_events_lin.restype = s32
tsapp_unregister_pretx_events_canfd = dll.tsapp_unregister_pretx_events_canfd
#arg[0] AObj : None
tsapp_unregister_pretx_events_canfd.argtypes =[ps32]
tsapp_unregister_pretx_events_canfd.restype = s32
tsapp_unregister_pretx_events_all = dll.tsapp_unregister_pretx_events_all
#arg[0] AObj : None
tsapp_unregister_pretx_events_all.argtypes =[ps32]
tsapp_unregister_pretx_events_all.restype = s32
tsapp_start_logging = dll.tsapp_start_logging
#arg[0] AFileName : None
tsapp_start_logging.argtypes =[pchar]
tsapp_start_logging.restype = s32
tsapp_stop_logging = dll.tsapp_stop_logging
tsapp_stop_logging.argtypes =[]
tsapp_stop_logging.restype = s32
tsapp_excel_load = dll.tsapp_excel_load
#arg[0] AFileName : None
#arg[1] AObj : None
tsapp_excel_load.argtypes =[pchar,ps32]
tsapp_excel_load.restype = s32
tsapp_excel_get_sheet_count = dll.tsapp_excel_get_sheet_count
#arg[0] AObj : None
#arg[1] ACount : None
tsapp_excel_get_sheet_count.argtypes =[ps32,s32]
tsapp_excel_get_sheet_count.restype = s32
tsapp_excel_set_sheet_count = dll.tsapp_excel_set_sheet_count
#arg[0] AObj : None
#arg[1] ACount : None
tsapp_excel_set_sheet_count.argtypes =[ps32,s32]
tsapp_excel_set_sheet_count.restype = s32
tsapp_excel_get_sheet_name = dll.tsapp_excel_get_sheet_name
#arg[0] AObj : None
#arg[1] AIdxSheet : None
#arg[2] AName : None
tsapp_excel_get_sheet_name.argtypes =[ps32,s32,ppchar]
tsapp_excel_get_sheet_name.restype = s32
tsapp_excel_set_sheet_name = dll.tsapp_excel_set_sheet_name
#arg[0] AObj : None
#arg[1] AIdxSheet : None
#arg[2] AName : None
tsapp_excel_set_sheet_name.argtypes =[ps32,s32,pchar]
tsapp_excel_set_sheet_name.restype = s32
tsapp_excel_get_cell_count = dll.tsapp_excel_get_cell_count
#arg[0] AObj : None
#arg[1] AIdxSheet : None
#arg[2] ARowCount : None
#arg[3] AColCount : None
tsapp_excel_get_cell_count.argtypes =[ps32,s32,s32,s32]
tsapp_excel_get_cell_count.restype = s32
tsapp_excel_get_cell_value = dll.tsapp_excel_get_cell_value
#arg[0] AObj : None
#arg[1] AIdxSheet : None
#arg[2] AIdxRow : None
#arg[3] AIdxCol : None
tsapp_excel_get_cell_value.argtypes =[ps32,s32,s32,s32]
tsapp_excel_get_cell_value.restype = s32
tsapp_excel_set_cell_count = dll.tsapp_excel_set_cell_count
#arg[0] AObj : None
#arg[1] AIdxSheet : None
#arg[2] ARowCount : None
#arg[3] AColCount : None
tsapp_excel_set_cell_count.argtypes =[ps32,s32,s32,s32]
tsapp_excel_set_cell_count.restype = s32
tsapp_excel_set_cell_value = dll.tsapp_excel_set_cell_value
#arg[0] AObj : None
#arg[1] AIdxSheet : None
#arg[2] AIdxRow : None
#arg[3] AIdxCol : None
tsapp_excel_set_cell_value.argtypes =[ps32,s32,s32,s32]
tsapp_excel_set_cell_value.restype = s32
tsapp_excel_unload = dll.tsapp_excel_unload
#arg[0] AObj : None
tsapp_excel_unload.argtypes =[ps32]
tsapp_excel_unload.restype = s32
tsapp_system_vars_reload_settings = dll.tsapp_system_vars_reload_settings
tsapp_system_vars_reload_settings.argtypes =[]
tsapp_system_vars_reload_settings.restype = s32
tsapp_get_system_var_count = dll.tsapp_get_system_var_count
#arg[0] AinternalCount : None
#arg[1] AUserCount : None
tsapp_get_system_var_count.argtypes =[ps32,ps32]
tsapp_get_system_var_count.restype = s32
tsapp_get_system_var_def_by_index = dll.tsapp_get_system_var_def_by_index
#arg[0] AIsUser : None
#arg[1] AIndex : None
#arg[2] AVarDef : None
tsapp_get_system_var_def_by_index.argtypes =[c_bool,s32,PLIBSystemVarDef]
tsapp_get_system_var_def_by_index.restype = s32
tsapp_find_system_var_def_by_name = dll.tsapp_find_system_var_def_by_name
#arg[0] AIsUser : None
#arg[1] ACompleteName : None
#arg[2] AVarDef : None
tsapp_find_system_var_def_by_name.argtypes =[c_bool,pchar,PLIBSystemVarDef]
tsapp_find_system_var_def_by_name.restype = s32
tsapp_get_system_var_double = dll.tsapp_get_system_var_double
#arg[0] ACompleteName : None
#arg[1] AValue : None
tsapp_get_system_var_double.argtypes =[pchar,pdouble]
tsapp_get_system_var_double.restype = s32
tsapp_get_system_var_int32 = dll.tsapp_get_system_var_int32
#arg[0] ACompleteName : None
#arg[1] AValue : None
tsapp_get_system_var_int32.argtypes =[pchar,ps32]
tsapp_get_system_var_int32.restype = s32
tsapp_get_system_var_uint32 = dll.tsapp_get_system_var_uint32
#arg[0] ACompleteName : None
#arg[1] AValue : None
tsapp_get_system_var_uint32.argtypes =[pchar,pu32]
tsapp_get_system_var_uint32.restype = s32
tsapp_get_system_var_int64 = dll.tsapp_get_system_var_int64
#arg[0] ACompleteName : None
#arg[1] AValue : None
tsapp_get_system_var_int64.argtypes =[pchar,ps64]
tsapp_get_system_var_int64.restype = s32
tsapp_get_system_var_uint64 = dll.tsapp_get_system_var_uint64
#arg[0] ACompleteName : None
#arg[1] AValue : None
tsapp_get_system_var_uint64.argtypes =[pchar,pu64]
tsapp_get_system_var_uint64.restype = s32
tsapp_get_system_var_uint8_array = dll.tsapp_get_system_var_uint8_array
#arg[0] ACompleteName : None
#arg[1] ACapacity : None
#arg[2] AVarCount : None
#arg[3] AValue : None
tsapp_get_system_var_uint8_array.argtypes =[pchar,s32,ps32,pu8]
tsapp_get_system_var_uint8_array.restype = s32
tsapp_get_system_var_int32_array = dll.tsapp_get_system_var_int32_array
#arg[0] ACompleteName : None
#arg[1] ACapacity : None
#arg[2] AVarCount : None
#arg[3] AValue : None
tsapp_get_system_var_int32_array.argtypes =[pchar,s32,ps32,ps32]
tsapp_get_system_var_int32_array.restype = s32
tsapp_get_system_var_int64_array = dll.tsapp_get_system_var_int64_array
#arg[0] ACompleteName : None
#arg[1] ACapacity : None
#arg[2] AVarCount : None
#arg[3] AValue : None
tsapp_get_system_var_int64_array.argtypes =[pchar,s32,ps32,ps64]
tsapp_get_system_var_int64_array.restype = s32
tsapp_get_system_var_double_array = dll.tsapp_get_system_var_double_array
#arg[0] ACompleteName : None
#arg[1] ACapacity : None
#arg[2] AVarCount : None
#arg[3] AValue : None
tsapp_get_system_var_double_array.argtypes =[pchar,s32,ps32,pdouble]
tsapp_get_system_var_double_array.restype = s32
tsapp_get_system_var_string = dll.tsapp_get_system_var_string
#arg[0] ACompleteName : None
#arg[1] ACapacity : None
#arg[2] AValue : None
tsapp_get_system_var_string.argtypes =[pchar,s32,pchar]
tsapp_get_system_var_string.restype = s32
tsapp_set_system_var_double = dll.tsapp_set_system_var_double
#arg[0] ACompleteName : None
#arg[1] AValue : None
tsapp_set_system_var_double.argtypes =[pchar,double]
tsapp_set_system_var_double.restype = s32
tsapp_set_system_var_int32 = dll.tsapp_set_system_var_int32
#arg[0] ACompleteName : None
#arg[1] AValue : None
tsapp_set_system_var_int32.argtypes =[pchar,s32]
tsapp_set_system_var_int32.restype = s32
tsapp_set_system_var_uint32 = dll.tsapp_set_system_var_uint32
#arg[0] ACompleteName : None
#arg[1] AValue : None
tsapp_set_system_var_uint32.argtypes =[pchar,u32]
tsapp_set_system_var_uint32.restype = s32
tsapp_set_system_var_int64 = dll.tsapp_set_system_var_int64
#arg[0] ACompleteName : None
#arg[1] AValue : None
tsapp_set_system_var_int64.argtypes =[pchar,s64]
tsapp_set_system_var_int64.restype = s32
tsapp_set_system_var_uint64 = dll.tsapp_set_system_var_uint64
#arg[0] ACompleteName : None
#arg[1] AValue : None
tsapp_set_system_var_uint64.argtypes =[pchar,u64]
tsapp_set_system_var_uint64.restype = s32
tsapp_set_system_var_uint8_array = dll.tsapp_set_system_var_uint8_array
#arg[0] ACompleteName : None
#arg[1] ACapacity : None
#arg[2] AValue : None
tsapp_set_system_var_uint8_array.argtypes =[pchar,s32,pu8]
tsapp_set_system_var_uint8_array.restype = s32
tsapp_set_system_var_int32_array = dll.tsapp_set_system_var_int32_array
#arg[0] ACompleteName : None
#arg[1] ACapacity : None
#arg[2] AValue : None
tsapp_set_system_var_int32_array.argtypes =[pchar,s32,ps32]
tsapp_set_system_var_int32_array.restype = s32
tsapp_set_system_var_int64_array = dll.tsapp_set_system_var_int64_array
#arg[0] ACompleteName : None
#arg[1] ACapacity : None
#arg[2] AValue : None
tsapp_set_system_var_int64_array.argtypes =[pchar,s32,ps64]
tsapp_set_system_var_int64_array.restype = s32
tsapp_set_system_var_double_array = dll.tsapp_set_system_var_double_array
#arg[0] ACompleteName : None
#arg[1] ACapacity : None
#arg[2] AValue : None
tsapp_set_system_var_double_array.argtypes =[pchar,s32,pdouble]
tsapp_set_system_var_double_array.restype = s32
tsapp_set_system_var_string = dll.tsapp_set_system_var_string
#arg[0] ACompleteName : None
#arg[1] AValue : None
tsapp_set_system_var_string.argtypes =[pchar,pchar]
tsapp_set_system_var_string.restype = s32
tsapp_log_system_var = dll.tsapp_log_system_var
#arg[0] ACompleteName : None
tsapp_log_system_var.argtypes =[pchar]
tsapp_log_system_var.restype = s32
tsapp_get_system_var_generic = dll.tsapp_get_system_var_generic
#arg[0] ACompleteName : None
#arg[1] ACapacity : None
#arg[2] AValue : None
tsapp_get_system_var_generic.argtypes =[pchar,s32,pchar]
tsapp_get_system_var_generic.restype = s32
tsapp_set_system_var_generic = dll.tsapp_set_system_var_generic
#arg[0] ACompleteName : None
#arg[1] AValue : None
tsapp_set_system_var_generic.argtypes =[pchar,pchar]
tsapp_set_system_var_generic.restype = s32
tsapp_get_hardware_id_string = dll.tsapp_get_hardware_id_string
#arg[0] AString : None
tsapp_get_hardware_id_string.argtypes =[ppchar]
tsapp_get_hardware_id_string.restype = s32
tsapp_get_hardware_id_array = dll.tsapp_get_hardware_id_array
#arg[0] AArray8B : None
tsapp_get_hardware_id_array.argtypes =[pu8]
tsapp_get_hardware_id_array.restype = s32
tsapp_create_system_var = dll.tsapp_create_system_var
#arg[0] ACompleteName : None
#arg[1] AType : None
#arg[2] ADefaultValue : None
#arg[3] AComment : None
tsapp_create_system_var.argtypes =[pchar,s32,pchar,pchar]
tsapp_create_system_var.restype = s32
tsapp_delete_system_var = dll.tsapp_delete_system_var
#arg[0] ACompleteName : None
tsapp_delete_system_var.argtypes =[pchar]
tsapp_delete_system_var.restype = s32
tsdb_reload_settings = dll.tsdb_reload_settings
#arg[0] ALoadedDBCount : None
tsdb_reload_settings.argtypes =[ps32]
tsdb_reload_settings.restype = s32
tsdb_save_settings = dll.tsdb_save_settings
tsdb_save_settings.argtypes =[]
tsdb_save_settings.restype = s32
tsdb_load_can_db = dll.tsdb_load_can_db
#arg[0] ADBC : None
#arg[1] ASupportedChannelsBased0 : None
#arg[2] AId : None
tsdb_load_can_db.argtypes =[pchar,pchar,ps32]
tsdb_load_can_db.restype = s32
tsdb_unload_can_db = dll.tsdb_unload_can_db
#arg[0] AId : None
tsdb_unload_can_db.argtypes =[s32]
tsdb_unload_can_db.restype = s32
tsdb_unload_can_dbs = dll.tsdb_unload_can_dbs
tsdb_unload_can_dbs.argtypes =[]
tsdb_unload_can_dbs.restype = s32
tsdb_get_can_db_count = dll.tsdb_get_can_db_count
#arg[0] ACount : None
tsdb_get_can_db_count.argtypes =[ps32]
tsdb_get_can_db_count.restype = s32
tsdb_get_can_db_id = dll.tsdb_get_can_db_id
#arg[0] AIndex : None
#arg[1] AId : None
tsdb_get_can_db_id.argtypes =[s32,ps32]
tsdb_get_can_db_id.restype = s32
tsdb_get_can_db_info = dll.tsdb_get_can_db_info
#arg[0] ADatabaseId : None
#arg[1] AType : None
#arg[2] AIndex : None
#arg[3] ASubIndex : None
#arg[4] AValue : None
tsdb_get_can_db_info.argtypes =[u32,s32,s32,s32,ppchar]
tsdb_get_can_db_info.restype = s32
tsdb_load_flexray_db = dll.tsdb_load_flexray_db
#arg[0] AFRFile : None
#arg[1] ASupportedChannels : None
#arg[2] AId : None
tsdb_load_flexray_db.argtypes =[pchar,pchar,ps32]
tsdb_load_flexray_db.restype = s32
tsdb_unload_flexray_db = dll.tsdb_unload_flexray_db
#arg[0] AId : None
tsdb_unload_flexray_db.argtypes =[s32]
tsdb_unload_flexray_db.restype = s32
tsdb_unload_flexray_dbs = dll.tsdb_unload_flexray_dbs
tsdb_unload_flexray_dbs.argtypes =[]
tsdb_unload_flexray_dbs.restype = s32
tsdb_get_flexray_db_count = dll.tsdb_get_flexray_db_count
#arg[0] ACount : None
tsdb_get_flexray_db_count.argtypes =[ps32]
tsdb_get_flexray_db_count.restype = s32
tsdb_get_flexray_db_properties_by_address_verbose = dll.tsdb_get_flexray_db_properties_by_address_verbose
#arg[0] AAddr : None
#arg[1] ADBIndex : None
#arg[2] ASignalCount : None
#arg[3] AFrameCount : None
#arg[4] AECUCount : None
#arg[5] ASupportedChannelMask : None
#arg[6] AFlags : None
#arg[7] AName : None
#arg[8] AComment : None
tsdb_get_flexray_db_properties_by_address_verbose.argtypes =[pchar,ps32,ps32,ps32,ps32,ps64,ps64,ppchar,ppchar]
tsdb_get_flexray_db_properties_by_address_verbose.restype = s32
tsdb_get_flexray_db_properties_by_index_verbose = dll.tsdb_get_flexray_db_properties_by_index_verbose
#arg[0] ADBIndex : None
#arg[1] ASignalCount : None
#arg[2] AFrameCount : None
#arg[3] AECUCount : None
#arg[4] ASupportedChannelMask : None
#arg[5] AFlags : None
#arg[6] AName : None
#arg[7] AComment : None
tsdb_get_flexray_db_properties_by_index_verbose.argtypes =[s32,ps32,ps32,ps32,ps64,ps64,ppchar,ppchar]
tsdb_get_flexray_db_properties_by_index_verbose.restype = s32
tsdb_get_flexray_ecu_properties_by_address_verbose = dll.tsdb_get_flexray_ecu_properties_by_address_verbose
#arg[0] AAddr : None
#arg[1] ADBIndex : None
#arg[2] AECUIndex : None
#arg[3] ATxFrameCount : None
#arg[4] ARxFrameCount : None
#arg[5] AName : None
#arg[6] AComment : None
tsdb_get_flexray_ecu_properties_by_address_verbose.argtypes =[pchar,ps32,ps32,ps32,ps32,ppchar,ppchar]
tsdb_get_flexray_ecu_properties_by_address_verbose.restype = s32
tsdb_get_flexray_ecu_properties_by_index_verbose = dll.tsdb_get_flexray_ecu_properties_by_index_verbose
#arg[0] ADBIndex : None
#arg[1] AECUIndex : None
#arg[2] ATxFrameCount : None
#arg[3] ARxFrameCount : None
#arg[4] AName : None
#arg[5] AComment : None
tsdb_get_flexray_ecu_properties_by_index_verbose.argtypes =[s32,s32,ps32,ps32,ppchar,ppchar]
tsdb_get_flexray_ecu_properties_by_index_verbose.restype = s32
tsdb_get_flexray_frame_properties_by_address_verbose = dll.tsdb_get_flexray_frame_properties_by_address_verbose
#arg[0] AAddr : None
#arg[1] ADBIndex : None
#arg[2] AECUIndex : None
#arg[3] AFrameIndex : None
#arg[4] AIsTx : None
#arg[5] AFRChannelMask : None
#arg[6] AFRBaseCycle : None
#arg[7] AFRCycleRepetition : None
#arg[8] AFRIsStartupFrame : None
#arg[9] AFRSlotId : None
#arg[10] AFRCycleMask : None
#arg[11] ASignalCount : None
#arg[12] AFRDLC : None
#arg[13] AName : None
#arg[14] AComment : None
tsdb_get_flexray_frame_properties_by_address_verbose.argtypes =[pchar,ps32,ps32,ps32,pbool,ps32,ps32,ps32,pbool,ps32,ps64,ps32,ps32,ppchar,ppchar]
tsdb_get_flexray_frame_properties_by_address_verbose.restype = s32
tsdb_get_flexray_frame_properties_by_index_verbose = dll.tsdb_get_flexray_frame_properties_by_index_verbose
#arg[0] ADBIndex : None
#arg[1] AECUIndex : None
#arg[2] AFrameIndex : None
#arg[3] AIsTx : None
#arg[4] AFRChannelMask : None
#arg[5] AFRBaseCycle : None
#arg[6] AFRCycleRepetition : None
#arg[7] AFRIsStartupFrame : None
#arg[8] AFRSlotId : None
#arg[9] AFRCycleMask : None
#arg[10] ASignalCount : None
#arg[11] AFRDLC : None
#arg[12] AName : None
#arg[13] AComment : None
tsdb_get_flexray_frame_properties_by_index_verbose.argtypes =[s32,s32,s32,c_bool,ps32,ps32,ps32,pbool,ps32,ps64,ps32,ps32,ppchar,ppchar]
tsdb_get_flexray_frame_properties_by_index_verbose.restype = s32
tsdb_get_flexray_signal_properties_by_address_verbose = dll.tsdb_get_flexray_signal_properties_by_address_verbose
#arg[0] AAddr : None
#arg[1] ADBIndex : None
#arg[2] AECUIndex : None
#arg[3] AFrameIndex : None
#arg[4] ASignalIndex : None
#arg[5] AIsTx : None
#arg[6] ASignalType : None
#arg[7] ACompuMethod : None
#arg[8] AIsIntel : None
#arg[9] AActualStartBit : None
#arg[10] AActualUpdateBit : None
#arg[11] ALength : None
#arg[12] AFactor : None
#arg[13] AOffset : None
#arg[14] AInitValue : None
#arg[15] AName : None
#arg[16] AComment : None
tsdb_get_flexray_signal_properties_by_address_verbose.argtypes =[pchar,ps32,ps32,ps32,ps32,pbool,ps32,ps32,pbool,ps32,ps32,ps32,pdouble,pdouble,pdouble,ppchar,ppchar]
tsdb_get_flexray_signal_properties_by_address_verbose.restype = s32
tsdb_get_flexray_signal_properties_by_index_verbose = dll.tsdb_get_flexray_signal_properties_by_index_verbose
#arg[0] ADBIndex : None
#arg[1] AECUIndex : None
#arg[2] AFrameIndex : None
#arg[3] ASignalIndex : None
#arg[4] AIsTx : None
#arg[5] ASignalType : None
#arg[6] ACompuMethod : None
#arg[7] AIsIntel : None
#arg[8] AActualStartBit : None
#arg[9] AActualUpdateBit : None
#arg[10] ALength : None
#arg[11] AFactor : None
#arg[12] AOffset : None
#arg[13] AInitValue : None
#arg[14] AName : None
#arg[15] AComment : None
tsdb_get_flexray_signal_properties_by_index_verbose.argtypes =[s32,s32,s32,s32,c_bool,ps32,ps32,pbool,ps32,ps32,ps32,pdouble,pdouble,pdouble,ppchar,ppchar]
tsdb_get_flexray_signal_properties_by_index_verbose.restype = s32
tsdb_get_flexray_db_id = dll.tsdb_get_flexray_db_id
#arg[0] AIndex : None
#arg[1] AId : None
tsdb_get_flexray_db_id.argtypes =[s32,ps32]
tsdb_get_flexray_db_id.restype = s32
tsdb_get_can_db_properties_by_index = dll.tsdb_get_can_db_properties_by_index
#arg[0] AValue : None
tsdb_get_can_db_properties_by_index.argtypes =[PMPDBProperties]
tsdb_get_can_db_properties_by_index.restype = s32
tsdb_get_lin_db_properties_by_index = dll.tsdb_get_lin_db_properties_by_index
#arg[0] AValue : None
tsdb_get_lin_db_properties_by_index.argtypes =[PMPDBProperties]
tsdb_get_lin_db_properties_by_index.restype = s32
tsdb_get_flexray_db_properties_by_index = dll.tsdb_get_flexray_db_properties_by_index
#arg[0] AValue : None
tsdb_get_flexray_db_properties_by_index.argtypes =[PMPDBProperties]
tsdb_get_flexray_db_properties_by_index.restype = s32
tsdb_get_can_db_ecu_properties_by_index = dll.tsdb_get_can_db_ecu_properties_by_index
#arg[0] AValue : None
tsdb_get_can_db_ecu_properties_by_index.argtypes =[PMPDBECUProperties]
tsdb_get_can_db_ecu_properties_by_index.restype = s32
tsdb_get_lin_db_ecu_properties_by_index = dll.tsdb_get_lin_db_ecu_properties_by_index
#arg[0] AValue : None
tsdb_get_lin_db_ecu_properties_by_index.argtypes =[PMPDBECUProperties]
tsdb_get_lin_db_ecu_properties_by_index.restype = s32
tsdb_get_flexray_db_ecu_properties_by_index = dll.tsdb_get_flexray_db_ecu_properties_by_index
#arg[0] AValue : None
tsdb_get_flexray_db_ecu_properties_by_index.argtypes =[PMPDBECUProperties]
tsdb_get_flexray_db_ecu_properties_by_index.restype = s32
tsdb_get_can_db_frame_properties_by_index = dll.tsdb_get_can_db_frame_properties_by_index
#arg[0] AValue : None
tsdb_get_can_db_frame_properties_by_index.argtypes =[PMPDBFrameProperties]
tsdb_get_can_db_frame_properties_by_index.restype = s32
tsdb_get_lin_db_frame_properties_by_index = dll.tsdb_get_lin_db_frame_properties_by_index
#arg[0] AValue : None
tsdb_get_lin_db_frame_properties_by_index.argtypes =[PMPDBFrameProperties]
tsdb_get_lin_db_frame_properties_by_index.restype = s32
tsdb_get_flexray_db_frame_properties_by_index = dll.tsdb_get_flexray_db_frame_properties_by_index
#arg[0] AValue : None
tsdb_get_flexray_db_frame_properties_by_index.argtypes =[PMPDBFrameProperties]
tsdb_get_flexray_db_frame_properties_by_index.restype = s32
tsdb_get_can_db_signal_properties_by_index = dll.tsdb_get_can_db_signal_properties_by_index
#arg[0] AValue : None
tsdb_get_can_db_signal_properties_by_index.argtypes =[PMPDBSignalProperties]
tsdb_get_can_db_signal_properties_by_index.restype = s32
tsdb_get_lin_db_signal_properties_by_index = dll.tsdb_get_lin_db_signal_properties_by_index
#arg[0] AValue : None
tsdb_get_lin_db_signal_properties_by_index.argtypes =[PMPDBSignalProperties]
tsdb_get_lin_db_signal_properties_by_index.restype = s32
tsdb_get_flexray_db_signal_properties_by_index = dll.tsdb_get_flexray_db_signal_properties_by_index
#arg[0] AValue : None
tsdb_get_flexray_db_signal_properties_by_index.argtypes =[PMPDBSignalProperties]
tsdb_get_flexray_db_signal_properties_by_index.restype = s32
tsdb_get_can_db_properties_by_address = dll.tsdb_get_can_db_properties_by_address
#arg[0] AAddr : None
#arg[1] AValue : None
tsdb_get_can_db_properties_by_address.argtypes =[pchar,PMPDBProperties]
tsdb_get_can_db_properties_by_address.restype = s32
tsdb_get_lin_db_properties_by_address = dll.tsdb_get_lin_db_properties_by_address
#arg[0] AAddr : None
#arg[1] AValue : None
tsdb_get_lin_db_properties_by_address.argtypes =[pchar,PMPDBProperties]
tsdb_get_lin_db_properties_by_address.restype = s32
tsdb_get_flexray_db_properties_by_address = dll.tsdb_get_flexray_db_properties_by_address
#arg[0] AAddr : None
#arg[1] AValue : None
tsdb_get_flexray_db_properties_by_address.argtypes =[pchar,PMPDBProperties]
tsdb_get_flexray_db_properties_by_address.restype = s32
tsdb_get_can_db_ecu_properties_by_address = dll.tsdb_get_can_db_ecu_properties_by_address
#arg[0] AAddr : None
#arg[1] AValue : None
tsdb_get_can_db_ecu_properties_by_address.argtypes =[pchar,PMPDBECUProperties]
tsdb_get_can_db_ecu_properties_by_address.restype = s32
tsdb_get_lin_db_ecu_properties_by_address = dll.tsdb_get_lin_db_ecu_properties_by_address
#arg[0] AAddr : None
#arg[1] AValue : None
tsdb_get_lin_db_ecu_properties_by_address.argtypes =[pchar,PMPDBECUProperties]
tsdb_get_lin_db_ecu_properties_by_address.restype = s32
tsdb_get_flexray_db_ecu_properties_by_address = dll.tsdb_get_flexray_db_ecu_properties_by_address
#arg[0] AAddr : None
#arg[1] AValue : None
tsdb_get_flexray_db_ecu_properties_by_address.argtypes =[pchar,PMPDBECUProperties]
tsdb_get_flexray_db_ecu_properties_by_address.restype = s32
tsdb_get_can_db_frame_properties_by_address = dll.tsdb_get_can_db_frame_properties_by_address
#arg[0] AAddr : None
#arg[1] AValue : None
tsdb_get_can_db_frame_properties_by_address.argtypes =[pchar,PMPDBFrameProperties]
tsdb_get_can_db_frame_properties_by_address.restype = s32
tsdb_get_lin_db_frame_properties_by_address = dll.tsdb_get_lin_db_frame_properties_by_address
#arg[0] AAddr : None
#arg[1] AValue : None
tsdb_get_lin_db_frame_properties_by_address.argtypes =[pchar,PMPDBFrameProperties]
tsdb_get_lin_db_frame_properties_by_address.restype = s32
tsdb_get_flexray_db_frame_properties_by_address = dll.tsdb_get_flexray_db_frame_properties_by_address
#arg[0] AAddr : None
#arg[1] AValue : None
tsdb_get_flexray_db_frame_properties_by_address.argtypes =[pchar,PMPDBFrameProperties]
tsdb_get_flexray_db_frame_properties_by_address.restype = s32
tsdb_get_can_db_signal_properties_by_address = dll.tsdb_get_can_db_signal_properties_by_address
#arg[0] AAddr : None
#arg[1] AValue : None
tsdb_get_can_db_signal_properties_by_address.argtypes =[pchar,PMPDBSignalProperties]
tsdb_get_can_db_signal_properties_by_address.restype = s32
tsdb_get_lin_db_signal_properties_by_address = dll.tsdb_get_lin_db_signal_properties_by_address
#arg[0] AAddr : None
#arg[1] AValue : None
tsdb_get_lin_db_signal_properties_by_address.argtypes =[pchar,PMPDBSignalProperties]
tsdb_get_lin_db_signal_properties_by_address.restype = s32
tsdb_get_flexray_db_signal_properties_by_address = dll.tsdb_get_flexray_db_signal_properties_by_address
#arg[0] AAddr : None
#arg[1] AValue : None
tsdb_get_flexray_db_signal_properties_by_address.argtypes =[pchar,PMPDBSignalProperties]
tsdb_get_flexray_db_signal_properties_by_address.restype = s32
tsdb_load_lin_db = dll.tsdb_load_lin_db
#arg[0] ALDF : None
#arg[1] ASupportedChannelsBased0 : None
#arg[2] AId : None
tsdb_load_lin_db.argtypes =[pchar,pchar,ps32]
tsdb_load_lin_db.restype = s32
tsdb_unload_lin_db = dll.tsdb_unload_lin_db
#arg[0] AId : None
tsdb_unload_lin_db.argtypes =[s32]
tsdb_unload_lin_db.restype = s32
tsdb_unload_lin_dbs = dll.tsdb_unload_lin_dbs
tsdb_unload_lin_dbs.argtypes =[]
tsdb_unload_lin_dbs.restype = s32
tsdb_get_lin_db_count = dll.tsdb_get_lin_db_count
#arg[0] ACount : None
tsdb_get_lin_db_count.argtypes =[ps32]
tsdb_get_lin_db_count.restype = s32
tsdb_get_lin_db_id = dll.tsdb_get_lin_db_id
#arg[0] AIndex : None
#arg[1] AId : None
tsdb_get_lin_db_id.argtypes =[s32,ps32]
tsdb_get_lin_db_id.restype = s32
tsdb_get_can_db_frame_properties_by_db_index = dll.tsdb_get_can_db_frame_properties_by_db_index
#arg[0] AIdxDB : None
#arg[1] AIndex : None
#arg[2] AValue : None
tsdb_get_can_db_frame_properties_by_db_index.argtypes =[s32,u32,PMPDBFrameProperties]
tsdb_get_can_db_frame_properties_by_db_index.restype = s32
tsdb_get_lin_db_frame_properties_by_db_index = dll.tsdb_get_lin_db_frame_properties_by_db_index
#arg[0] AIdxDB : None
#arg[1] AIndex : None
#arg[2] AValue : None
tsdb_get_lin_db_frame_properties_by_db_index.argtypes =[s32,s32,PMPDBFrameProperties]
tsdb_get_lin_db_frame_properties_by_db_index.restype = s32
tsdb_get_flexray_db_frame_properties_by_db_index = dll.tsdb_get_flexray_db_frame_properties_by_db_index
#arg[0] AIdxDB : None
#arg[1] AIndex : None
#arg[2] AValue : None
tsdb_get_flexray_db_frame_properties_by_db_index.argtypes =[s32,s32,PMPDBFrameProperties]
tsdb_get_flexray_db_frame_properties_by_db_index.restype = s32
tsdb_get_can_db_signal_properties_by_frame_index = dll.tsdb_get_can_db_signal_properties_by_frame_index
#arg[0] AIdxDB : None
#arg[1] AIdxFrame : None
#arg[2] ASgnIndexInFrame : None
#arg[3] AValue : None
tsdb_get_can_db_signal_properties_by_frame_index.argtypes =[s32,s32,s32,PMPDBSignalProperties]
tsdb_get_can_db_signal_properties_by_frame_index.restype = s32
tsdb_get_lin_db_signal_properties_by_frame_index = dll.tsdb_get_lin_db_signal_properties_by_frame_index
#arg[0] AIdxDB : None
#arg[1] AIdxFrame : None
#arg[2] ASgnIndexInFrame : None
#arg[3] AValue : None
tsdb_get_lin_db_signal_properties_by_frame_index.argtypes =[s32,s32,s32,PMPDBSignalProperties]
tsdb_get_lin_db_signal_properties_by_frame_index.restype = s32
tsdb_get_flexray_db_signal_properties_by_frame_index = dll.tsdb_get_flexray_db_signal_properties_by_frame_index
#arg[0] AIdxDB : None
#arg[1] AIdxFrame : None
#arg[2] ASgnIndexInFrame : None
#arg[3] AValue : None
tsdb_get_flexray_db_signal_properties_by_frame_index.argtypes =[s32,s32,s32,PMPDBSignalProperties]
tsdb_get_flexray_db_signal_properties_by_frame_index.restype = s32
tsdb_set_signal_value_can = dll.tsdb_set_signal_value_can
#arg[0] ACAN : None
#arg[1] AMsgName : None
#arg[2] ASgnName : None
#arg[3] AValue : None
tsdb_set_signal_value_can.argtypes =[PLIBCAN,pchar,pchar,double]
tsdb_set_signal_value_can.restype = s32
tsdb_get_signal_value_can = dll.tsdb_get_signal_value_can
#arg[0] ACAN : None
#arg[1] AMsgName : None
#arg[2] ASgnName : None
#arg[3] AValue : None
tsdb_get_signal_value_can.argtypes =[PLIBCAN,pchar,pchar,pdouble]
tsdb_get_signal_value_can.restype = s32
tsdb_set_signal_value_canfd = dll.tsdb_set_signal_value_canfd
#arg[0] ACANfd : None
#arg[1] AMsgName : None
#arg[2] ASgnName : None
#arg[3] AValue : None
tsdb_set_signal_value_canfd.argtypes =[PLIBCANFD,pchar,pchar,double]
tsdb_set_signal_value_canfd.restype = s32
tsdb_get_signal_value_canfd = dll.tsdb_get_signal_value_canfd
#arg[0] ACANfd : None
#arg[1] AMsgName : None
#arg[2] ASgnName : None
#arg[3] AValue : None
tsdb_get_signal_value_canfd.argtypes =[PLIBCANFD,pchar,pchar,pdouble]
tsdb_get_signal_value_canfd.restype = s32
tslog_reload_settings = dll.tslog_reload_settings
#arg[0] ALoadedEngineCount : None
tslog_reload_settings.argtypes =[s32]
tslog_reload_settings.restype = s32
tslog_add_online_replay_config = dll.tslog_add_online_replay_config
#arg[0] AFileName : None
#arg[1] AIndex : None
tslog_add_online_replay_config.argtypes =[pchar,ps32]
tslog_add_online_replay_config.restype = s32
tslog_set_online_replay_config = dll.tslog_set_online_replay_config
#arg[0] AIndex : None
#arg[1] AName : None
#arg[2] AFileName : None
#arg[3] AAutoStart : None
#arg[4] AIsRepetitiveMode : None
#arg[5] AStartTimingMode : None
#arg[6] AStartDelayTimeMs : None
#arg[7] ASendTx : None
#arg[8] ASendRx : None
#arg[9] AMappings : None
tslog_set_online_replay_config.argtypes =[s32,pchar,pchar,c_bool,c_bool,s32,s32,c_bool,c_bool,pchar]
tslog_set_online_replay_config.restype = s32
tslog_get_online_replay_count = dll.tslog_get_online_replay_count
#arg[0] ACount : None
tslog_get_online_replay_count.argtypes =[ps32]
tslog_get_online_replay_count.restype = s32
tslog_get_online_replay_config = dll.tslog_get_online_replay_config
#arg[0] AIndex : None
#arg[1] AName : None
#arg[2] AFileName : None
#arg[3] AAutoStart : None
#arg[4] AIsRepetitiveMode : None
#arg[5] AStartTimingMode : None
#arg[6] AStartDelayTimeMs : None
#arg[7] ASendTx : None
#arg[8] ASendRx : None
#arg[9] AMappings : None
tslog_get_online_replay_config.argtypes =[s32,ppchar,ppchar,pbool,pbool,ps32,ps32,pbool,pbool,ppchar]
tslog_get_online_replay_config.restype = s32
tslog_del_online_replay_config = dll.tslog_del_online_replay_config
#arg[0] AIndex : None
tslog_del_online_replay_config.argtypes =[s32]
tslog_del_online_replay_config.restype = s32
tslog_del_online_replay_configs = dll.tslog_del_online_replay_configs
tslog_del_online_replay_configs.argtypes =[]
tslog_del_online_replay_configs.restype = s32
tslog_start_online_replay = dll.tslog_start_online_replay
#arg[0] AIndex : None
tslog_start_online_replay.argtypes =[s32]
tslog_start_online_replay.restype = s32
tslog_start_online_replays = dll.tslog_start_online_replays
tslog_start_online_replays.argtypes =[]
tslog_start_online_replays.restype = s32
tslog_pause_online_replay = dll.tslog_pause_online_replay
#arg[0] AIndex : None
tslog_pause_online_replay.argtypes =[s32]
tslog_pause_online_replay.restype = s32
tslog_pause_online_replays = dll.tslog_pause_online_replays
tslog_pause_online_replays.argtypes =[]
tslog_pause_online_replays.restype = s32
tslog_stop_online_replay = dll.tslog_stop_online_replay
#arg[0] AIndex : None
tslog_stop_online_replay.argtypes =[s32]
tslog_stop_online_replay.restype = s32
tslog_stop_online_replays = dll.tslog_stop_online_replays
tslog_stop_online_replays.argtypes =[]
tslog_stop_online_replays.restype = s32
tslog_get_online_replay_status = dll.tslog_get_online_replay_status
#arg[0] AIndex : None
#arg[1] AStatus : None
#arg[2] AProgressPercent100 : None
tslog_get_online_replay_status.argtypes =[s32,ps8,psingle]
tslog_get_online_replay_status.restype = s32
tslog_blf_write_start = dll.tslog_blf_write_start
#arg[0] AFileName : None
#arg[1] AHandle : None
tslog_blf_write_start.argtypes =[pchar,ps32]
tslog_blf_write_start.restype = s32
tslog_blf_write_set_max_count = dll.tslog_blf_write_set_max_count
#arg[0] AHandle : None
#arg[1] ACount : None
tslog_blf_write_set_max_count.argtypes =[s32,u32]
tslog_blf_write_set_max_count.restype = s32
tslog_blf_write_can = dll.tslog_blf_write_can
#arg[0] AHandle : None
#arg[1] ACAN : None
tslog_blf_write_can.argtypes =[s32,PLIBCAN]
tslog_blf_write_can.restype = s32
tslog_blf_write_can_fd = dll.tslog_blf_write_can_fd
#arg[0] AHandle : None
#arg[1] ACANFD : None
tslog_blf_write_can_fd.argtypes =[s32,PLIBCANFD]
tslog_blf_write_can_fd.restype = s32
tslog_blf_write_lin = dll.tslog_blf_write_lin
#arg[0] AHandle : None
#arg[1] ALIN : None
tslog_blf_write_lin.argtypes =[s32,PLIBLIN]
tslog_blf_write_lin.restype = s32
tslog_blf_write_realtime_comment = dll.tslog_blf_write_realtime_comment
#arg[0] AHandle : None
#arg[1] ATimeUs : None
#arg[2] AComment : None
tslog_blf_write_realtime_comment.argtypes =[s32,s64,pchar]
tslog_blf_write_realtime_comment.restype = s32
tslog_blf_write_end = dll.tslog_blf_write_end
#arg[0] AHandle : None
tslog_blf_write_end.argtypes =[s32]
tslog_blf_write_end.restype = s32
tslog_blf_read_start = dll.tslog_blf_read_start
#arg[0] AFileName : None
#arg[1] AHandle : None
#arg[2] AObjCount : None
tslog_blf_read_start.argtypes =[pchar,ps32,ps32]
tslog_blf_read_start.restype = s32
tsLog_blf_read_start_verbose = dll.tsLog_blf_read_start_verbose
#arg[0] AFileName : None
#arg[1] AHandle : None
#arg[2] AObjCount : None
#arg[3] AYear : None
#arg[4] AMonth : None
#arg[5] ADayOfWeek : None
#arg[6] ADay : None
#arg[7] AHour : None
#arg[8] AMinute : None
#arg[9] ASecond : None
#arg[10] AMilliseconds : None
tsLog_blf_read_start_verbose.argtypes =[pchar,ps32,ps32,pu16,pu16,pu16,pu16,pu16,pu16,pu16,pu16]
tsLog_blf_read_start_verbose.restype = s32
tslog_blf_read_status = dll.tslog_blf_read_status
#arg[0] AHandle : None
#arg[1] AObjReadCount : None
tslog_blf_read_status.argtypes =[s32,ps32]
tslog_blf_read_status.restype = s32
tslog_blf_read_object = dll.tslog_blf_read_object
#arg[0] AHandle : None
#arg[1] AProgressedCnt : None
#arg[2] AType : None
#arg[3] ACAN : None
#arg[4] ALIN : None
#arg[5] ACANFD : None
tslog_blf_read_object.argtypes =[s32,ps32,ps32,PLIBCAN,PLIBLIN,PLIBCANFD]
tslog_blf_read_object.restype = s32
tslog_blf_read_object_w_comment = dll.tslog_blf_read_object_w_comment
#arg[0] AHandle : None
#arg[1] AProgressedCnt : None
#arg[2] AType : None
#arg[3] ACAN : None
#arg[4] ALIN : None
#arg[5] ACANFD : None
#arg[6] AComment : None
tslog_blf_read_object_w_comment.argtypes =[s32,ps32,ps32,PLIBCAN,PLIBLIN,PLIBCANFD,Prealtime_comment_t]
tslog_blf_read_object_w_comment.restype = s32
tslog_blf_read_end = dll.tslog_blf_read_end
#arg[0] AHandle : None
tslog_blf_read_end.argtypes =[s32]
tslog_blf_read_end.restype = s32
tslog_blf_seek_object_time = dll.tslog_blf_seek_object_time
#arg[0] AHandle : None
#arg[1] AProg100 : None
#arg[2] ATime : None
#arg[3] AProgressedCnt : None
tslog_blf_seek_object_time.argtypes =[s32,double,ps64,ps32]
tslog_blf_seek_object_time.restype = s32
tslog_blf_to_asc = dll.tslog_blf_to_asc
#arg[0] AObj : None
#arg[1] ABLFFileName : None
#arg[2] AASCFileName : None
#arg[3] AProgressCallback : None
tslog_blf_to_asc.argtypes =[ps32,pchar,pchar,TReadProgressCallback]
tslog_blf_to_asc.restype = s32
tslog_asc_to_blf = dll.tslog_asc_to_blf
#arg[0] AObj : None
#arg[1] AASCFileName : None
#arg[2] ABLFFileName : None
#arg[3] AProgressCallback : None
tslog_asc_to_blf.argtypes =[ps32,pchar,pchar,TReadProgressCallback]
tslog_asc_to_blf.restype = s32
tscom_lin_rbs_reload_settings = dll.tscom_lin_rbs_reload_settings
tscom_lin_rbs_reload_settings.argtypes =[]
tscom_lin_rbs_reload_settings.restype = s32
tscom_lin_rbs_start = dll.tscom_lin_rbs_start
tscom_lin_rbs_start.argtypes =[]
tscom_lin_rbs_start.restype = s32
tscom_lin_rbs_stop = dll.tscom_lin_rbs_stop
tscom_lin_rbs_stop.argtypes =[]
tscom_lin_rbs_stop.restype = s32
tscom_lin_rbs_is_running = dll.tscom_lin_rbs_is_running
#arg[0] AIsRunning : None
tscom_lin_rbs_is_running.argtypes =[pbool]
tscom_lin_rbs_is_running.restype = s32
tscom_lin_rbs_configure = dll.tscom_lin_rbs_configure
#arg[0] AAutoStart : None
#arg[1] AAutoSendOnModification : None
#arg[2] AActivateNodeSimulation : None
#arg[3] AInitValueOptions : None
tscom_lin_rbs_configure.argtypes =[c_bool,c_bool,c_bool,s32]
tscom_lin_rbs_configure.restype = s32
tscom_lin_rbs_activate_all_networks = dll.tscom_lin_rbs_activate_all_networks
#arg[0] AEnable : None
#arg[1] AIncludingChildren : None
tscom_lin_rbs_activate_all_networks.argtypes =[c_bool,c_bool]
tscom_lin_rbs_activate_all_networks.restype = s32
tscom_lin_rbs_activate_network_by_name = dll.tscom_lin_rbs_activate_network_by_name
#arg[0] AIdxChn : None
#arg[1] AEnable : None
#arg[2] ANetworkName : None
#arg[3] AIncludingChildren : None
tscom_lin_rbs_activate_network_by_name.argtypes =[s32,c_bool,pchar,c_bool]
tscom_lin_rbs_activate_network_by_name.restype = s32
tscom_lin_rbs_activate_node_by_name = dll.tscom_lin_rbs_activate_node_by_name
#arg[0] AIdxChn : None
#arg[1] AEnable : None
#arg[2] ANetworkName : None
#arg[3] ANodeName : None
#arg[4] AIncludingChildren : None
tscom_lin_rbs_activate_node_by_name.argtypes =[s32,c_bool,pchar,pchar,c_bool]
tscom_lin_rbs_activate_node_by_name.restype = s32
tscom_lin_rbs_activate_message_by_name = dll.tscom_lin_rbs_activate_message_by_name
#arg[0] AIdxChn : None
#arg[1] AEnable : None
#arg[2] ANetworkName : None
#arg[3] ANodeName : None
#arg[4] AMsgName : None
tscom_lin_rbs_activate_message_by_name.argtypes =[s32,c_bool,pchar,pchar,pchar]
tscom_lin_rbs_activate_message_by_name.restype = s32
tscom_lin_rbs_set_message_delay_time_by_name = dll.tscom_lin_rbs_set_message_delay_time_by_name
#arg[0] AIdxChn : None
#arg[1] AIntervalMs : None
#arg[2] ANetworkName : None
#arg[3] ANodeName : None
#arg[4] AMsgName : None
tscom_lin_rbs_set_message_delay_time_by_name.argtypes =[s32,s32,pchar,pchar,pchar]
tscom_lin_rbs_set_message_delay_time_by_name.restype = s32
tscom_lin_rbs_get_signal_value_by_element = dll.tscom_lin_rbs_get_signal_value_by_element
#arg[0] AIdxChn : None
#arg[1] ANetworkName : None
#arg[2] ANodeName : None
#arg[3] AMsgName : None
#arg[4] ASignalName : None
#arg[5] AValue : None
tscom_lin_rbs_get_signal_value_by_element.argtypes =[s32,pchar,pchar,pchar,pchar,pdouble]
tscom_lin_rbs_get_signal_value_by_element.restype = s32
tscom_lin_rbs_get_signal_value_by_address = dll.tscom_lin_rbs_get_signal_value_by_address
#arg[0] ASymbolAddress : None
#arg[1] AValue : None
tscom_lin_rbs_get_signal_value_by_address.argtypes =[pchar,pdouble]
tscom_lin_rbs_get_signal_value_by_address.restype = s32
tscom_lin_rbs_set_signal_value_by_element = dll.tscom_lin_rbs_set_signal_value_by_element
#arg[0] AIdxChn : None
#arg[1] ANetworkName : None
#arg[2] ANodeName : None
#arg[3] AMsgName : None
#arg[4] ASignalName : None
#arg[5] AValue : None
tscom_lin_rbs_set_signal_value_by_element.argtypes =[s32,pchar,pchar,pchar,pchar,double]
tscom_lin_rbs_set_signal_value_by_element.restype = s32
tscom_lin_rbs_set_signal_value_by_address = dll.tscom_lin_rbs_set_signal_value_by_address
#arg[0] ASymbolAddress : None
#arg[1] AValue : None
tscom_lin_rbs_set_signal_value_by_address.argtypes =[pchar,double]
tscom_lin_rbs_set_signal_value_by_address.restype = s32
tscom_can_rbs_reload_settings = dll.tscom_can_rbs_reload_settings
tscom_can_rbs_reload_settings.argtypes =[]
tscom_can_rbs_reload_settings.restype = s32
tscom_can_rbs_start = dll.tscom_can_rbs_start
tscom_can_rbs_start.argtypes =[]
tscom_can_rbs_start.restype = s32
tscom_can_rbs_stop = dll.tscom_can_rbs_stop
tscom_can_rbs_stop.argtypes =[]
tscom_can_rbs_stop.restype = s32
tscom_can_rbs_is_running = dll.tscom_can_rbs_is_running
#arg[0] AIsRunning : None
tscom_can_rbs_is_running.argtypes =[pbool]
tscom_can_rbs_is_running.restype = s32
tscom_can_rbs_configure = dll.tscom_can_rbs_configure
#arg[0] AAutoStart : None
#arg[1] AAutoSendOnModification : None
#arg[2] AActivateNodeSimulation : None
#arg[3] AInitValueOptions : None
tscom_can_rbs_configure.argtypes =[c_bool,c_bool,c_bool,s32]
tscom_can_rbs_configure.restype = s32
tscom_can_rbs_activate_all_networks = dll.tscom_can_rbs_activate_all_networks
#arg[0] AEnable : None
#arg[1] AIncludingChildren : None
tscom_can_rbs_activate_all_networks.argtypes =[c_bool,c_bool]
tscom_can_rbs_activate_all_networks.restype = s32
tscom_can_rbs_activate_network_by_name = dll.tscom_can_rbs_activate_network_by_name
#arg[0] AIdxChn : None
#arg[1] AEnable : None
#arg[2] ANetworkName : None
#arg[3] AIncludingChildren : None
tscom_can_rbs_activate_network_by_name.argtypes =[s32,c_bool,pchar,c_bool]
tscom_can_rbs_activate_network_by_name.restype = s32
tscom_can_rbs_activate_node_by_name = dll.tscom_can_rbs_activate_node_by_name
#arg[0] AIdxChn : None
#arg[1] AEnable : None
#arg[2] ANetworkName : None
#arg[3] ANodeName : None
#arg[4] AIncludingChildren : None
tscom_can_rbs_activate_node_by_name.argtypes =[s32,c_bool,pchar,pchar,c_bool]
tscom_can_rbs_activate_node_by_name.restype = s32
tscom_can_rbs_activate_message_by_name = dll.tscom_can_rbs_activate_message_by_name
#arg[0] AIdxChn : None
#arg[1] AEnable : None
#arg[2] ANetworkName : None
#arg[3] ANodeName : None
#arg[4] AMsgName : None
tscom_can_rbs_activate_message_by_name.argtypes =[s32,c_bool,pchar,pchar,pchar]
tscom_can_rbs_activate_message_by_name.restype = s32
tscom_can_rbs_set_message_cycle_by_name = dll.tscom_can_rbs_set_message_cycle_by_name
#arg[0] AIdxChn : None
#arg[1] AIntervalMs : None
#arg[2] ANetworkName : None
#arg[3] ANodeName : None
#arg[4] AMsgName : None
tscom_can_rbs_set_message_cycle_by_name.argtypes =[s32,s32,pchar,pchar,pchar]
tscom_can_rbs_set_message_cycle_by_name.restype = s32
tscom_can_rbs_get_signal_value_by_element = dll.tscom_can_rbs_get_signal_value_by_element
#arg[0] AIdxChn : None
#arg[1] ANetworkName : None
#arg[2] ANodeName : None
#arg[3] AMsgName : None
#arg[4] ASignalName : None
#arg[5] AValue : None
tscom_can_rbs_get_signal_value_by_element.argtypes =[s32,pchar,pchar,pchar,pchar,pdouble]
tscom_can_rbs_get_signal_value_by_element.restype = s32
tscom_can_rbs_get_signal_value_by_address = dll.tscom_can_rbs_get_signal_value_by_address
#arg[0] ASymbolAddress : None
#arg[1] AValue : None
tscom_can_rbs_get_signal_value_by_address.argtypes =[pchar,pdouble]
tscom_can_rbs_get_signal_value_by_address.restype = s32
tscom_can_rbs_set_signal_value_by_element = dll.tscom_can_rbs_set_signal_value_by_element
#arg[0] AIdxChn : None
#arg[1] ANetworkName : None
#arg[2] ANodeName : None
#arg[3] AMsgName : None
#arg[4] ASignalName : None
#arg[5] AValue : None
tscom_can_rbs_set_signal_value_by_element.argtypes =[s32,pchar,pchar,pchar,pchar,double]
tscom_can_rbs_set_signal_value_by_element.restype = s32
tscom_can_rbs_set_signal_value_by_address = dll.tscom_can_rbs_set_signal_value_by_address
#arg[0] ASymbolAddress : None
#arg[1] AValue : None
tscom_can_rbs_set_signal_value_by_address.argtypes =[pchar,double]
tscom_can_rbs_set_signal_value_by_address.restype = s32
tscom_flexray_rbs_start = dll.tscom_flexray_rbs_start
tscom_flexray_rbs_start.argtypes =[]
tscom_flexray_rbs_start.restype = s32
tscom_flexray_rbs_stop = dll.tscom_flexray_rbs_stop
tscom_flexray_rbs_stop.argtypes =[]
tscom_flexray_rbs_stop.restype = s32
tscom_flexray_rbs_is_running = dll.tscom_flexray_rbs_is_running
#arg[0] AIsRunning : None
tscom_flexray_rbs_is_running.argtypes =[pbool]
tscom_flexray_rbs_is_running.restype = s32
tscom_flexray_rbs_configure = dll.tscom_flexray_rbs_configure
#arg[0] AAutoStart : None
#arg[1] AAutoSendOnModification : None
#arg[2] AActivateECUSimulation : None
#arg[3] AInitValueOptions : None
tscom_flexray_rbs_configure.argtypes =[c_bool,c_bool,c_bool,s32]
tscom_flexray_rbs_configure.restype = s32
tscom_flexray_rbs_activate_all_clusters = dll.tscom_flexray_rbs_activate_all_clusters
#arg[0] AEnable : None
#arg[1] AIncludingChildren : None
tscom_flexray_rbs_activate_all_clusters.argtypes =[c_bool,c_bool]
tscom_flexray_rbs_activate_all_clusters.restype = s32
tscom_flexray_rbs_activate_cluster_by_name = dll.tscom_flexray_rbs_activate_cluster_by_name
#arg[0] AIdxChn : None
#arg[1] AEnable : None
#arg[2] AClusterName : None
#arg[3] AIncludingChildren : None
tscom_flexray_rbs_activate_cluster_by_name.argtypes =[s32,c_bool,pchar,c_bool]
tscom_flexray_rbs_activate_cluster_by_name.restype = s32
tscom_flexray_rbs_activate_ecu_by_name = dll.tscom_flexray_rbs_activate_ecu_by_name
#arg[0] AIdxChn : None
#arg[1] AEnable : None
#arg[2] AClusterName : None
#arg[3] AECUName : None
#arg[4] AIncludingChildren : None
tscom_flexray_rbs_activate_ecu_by_name.argtypes =[s32,c_bool,pchar,pchar,c_bool]
tscom_flexray_rbs_activate_ecu_by_name.restype = s32
tscom_flexray_rbs_activate_frame_by_name = dll.tscom_flexray_rbs_activate_frame_by_name
#arg[0] AIdxChn : None
#arg[1] AEnable : None
#arg[2] AClusterName : None
#arg[3] AECUName : None
#arg[4] AFrameName : None
tscom_flexray_rbs_activate_frame_by_name.argtypes =[s32,c_bool,pchar,pchar,pchar]
tscom_flexray_rbs_activate_frame_by_name.restype = s32
tscom_flexray_rbs_get_signal_value_by_element = dll.tscom_flexray_rbs_get_signal_value_by_element
#arg[0] AIdxChn : None
#arg[1] AClusterName : None
#arg[2] AECUName : None
#arg[3] AFrameName : None
#arg[4] ASignalName : None
#arg[5] AValue : None
tscom_flexray_rbs_get_signal_value_by_element.argtypes =[s32,pchar,pchar,pchar,pchar,pdouble]
tscom_flexray_rbs_get_signal_value_by_element.restype = s32
tscom_flexray_rbs_set_signal_value_by_element = dll.tscom_flexray_rbs_set_signal_value_by_element
#arg[0] AIdxChn : None
#arg[1] AClusterName : None
#arg[2] AECUName : None
#arg[3] AFrameName : None
#arg[4] ASignalName : None
#arg[5] AValue : None
tscom_flexray_rbs_set_signal_value_by_element.argtypes =[s32,pchar,pchar,pchar,pchar,double]
tscom_flexray_rbs_set_signal_value_by_element.restype = s32
tscom_flexray_rbs_get_signal_value_by_address = dll.tscom_flexray_rbs_get_signal_value_by_address
#arg[0] ASymbolAddress : None
#arg[1] AValue : None
tscom_flexray_rbs_get_signal_value_by_address.argtypes =[pchar,pdouble]
tscom_flexray_rbs_get_signal_value_by_address.restype = s32
tscom_flexray_rbs_set_signal_value_by_address = dll.tscom_flexray_rbs_set_signal_value_by_address
#arg[0] ASymbolAddress : None
#arg[1] AValue : None
tscom_flexray_rbs_set_signal_value_by_address.argtypes =[pchar,double]
tscom_flexray_rbs_set_signal_value_by_address.restype = s32
tscom_flexray_rbs_enable = dll.tscom_flexray_rbs_enable
#arg[0] AEnable : None
tscom_flexray_rbs_enable.argtypes =[c_bool]
tscom_flexray_rbs_enable.restype = s32
tscom_flexray_rbs_batch_set_start = dll.tscom_flexray_rbs_batch_set_start
tscom_flexray_rbs_batch_set_start.argtypes =[]
tscom_flexray_rbs_batch_set_start.restype = s32
tscom_flexray_rbs_batch_set_end = dll.tscom_flexray_rbs_batch_set_end
tscom_flexray_rbs_batch_set_end.argtypes =[]
tscom_flexray_rbs_batch_set_end.restype = s32
tscom_flexray_rbs_batch_set_signal = dll.tscom_flexray_rbs_batch_set_signal
#arg[0] AAddr : None
#arg[1] AValue : None
tscom_flexray_rbs_batch_set_signal.argtypes =[pchar,double]
tscom_flexray_rbs_batch_set_signal.restype = s32
tscom_flexray_rbs_set_frame_direction = dll.tscom_flexray_rbs_set_frame_direction
#arg[0] AIdxChn : None
#arg[1] AIsTx : None
#arg[2] AClusterName : None
#arg[3] AECUName : None
#arg[4] AFrameName : None
tscom_flexray_rbs_set_frame_direction.argtypes =[s32,c_bool,pchar,pchar,pchar]
tscom_flexray_rbs_set_frame_direction.restype = s32
tscom_flexray_rbs_set_normal_signal = dll.tscom_flexray_rbs_set_normal_signal
#arg[0] ASymbolAddress : None
tscom_flexray_rbs_set_normal_signal.argtypes =[pchar]
tscom_flexray_rbs_set_normal_signal.restype = s32
tscom_flexray_rbs_set_rc_signal = dll.tscom_flexray_rbs_set_rc_signal
#arg[0] ASymbolAddress : None
tscom_flexray_rbs_set_rc_signal.argtypes =[pchar]
tscom_flexray_rbs_set_rc_signal.restype = s32
tscom_flexray_rbs_set_rc_signal_with_limit = dll.tscom_flexray_rbs_set_rc_signal_with_limit
#arg[0] ASymbolAddress : None
#arg[1] ALowerLimit : None
#arg[2] AUpperLimit : None
tscom_flexray_rbs_set_rc_signal_with_limit.argtypes =[pchar,s32,s32]
tscom_flexray_rbs_set_rc_signal_with_limit.restype = s32
tscom_flexray_rbs_set_crc_signal = dll.tscom_flexray_rbs_set_crc_signal
#arg[0] ASymbolAddress : None
#arg[1] AAlgorithmName : None
#arg[2] AIdxByteStart : None
#arg[3] AByteCount : None
tscom_flexray_rbs_set_crc_signal.argtypes =[pchar,pchar,s32,s32]
tscom_flexray_rbs_set_crc_signal.restype = s32
tscom_flexray_set_signal_value_in_raw_frame = dll.tscom_flexray_set_signal_value_in_raw_frame
#arg[0] AFlexRaySignal : None
#arg[1] AData : None
#arg[2] AValue : None
tscom_flexray_set_signal_value_in_raw_frame.argtypes =[PMPFlexRaySignal,pu8,double]
tscom_flexray_set_signal_value_in_raw_frame.restype = s32
tscom_flexray_get_signal_value_in_raw_frame = dll.tscom_flexray_get_signal_value_in_raw_frame
#arg[0] AFlexRaySignal : None
#arg[1] AData : None
tscom_flexray_get_signal_value_in_raw_frame.argtypes =[PMPFlexRaySignal,pu8]
tscom_flexray_get_signal_value_in_raw_frame.restype = s32
tscom_flexray_get_signal_definition = dll.tscom_flexray_get_signal_definition
#arg[0] ASignalAddress : None
#arg[1] ASignalDef : None
tscom_flexray_get_signal_definition.argtypes =[pchar,PMPFlexRaySignal]
tscom_flexray_get_signal_definition.restype = s32
tsflexray_set_controller_frametrigger = dll.tsflexray_set_controller_frametrigger
#arg[0] AIdxChn : None
#arg[1] AControllerConfig : None
#arg[2] AFrameLengthArray : None
#arg[3] AFrameNum : None
#arg[4] AFrameTrigger : None
#arg[5] AFrameTriggerNum : None
#arg[6] ATimeoutMs : None
tsflexray_set_controller_frametrigger.argtypes =[s32,PLIBFlexray_controller_config,ps32,s32,PLIBTrigger_def,s32,s32]
tsflexray_set_controller_frametrigger.restype = s32
tsflexray_set_controller = dll.tsflexray_set_controller
#arg[0] AIdxChn : None
#arg[1] AControllerConfig : None
#arg[2] ATimeoutMs : None
tsflexray_set_controller.argtypes =[s32,PLIBFlexray_controller_config,s32]
tsflexray_set_controller.restype = s32
tsflexray_set_frametrigger = dll.tsflexray_set_frametrigger
#arg[0] AIdxChn : None
#arg[1] AFrameLengthArray : None
#arg[2] AFrameNum : None
#arg[3] AFrameTrigger : None
#arg[4] AFrameTriggerNum : None
#arg[5] ATimeoutMs : None
tsflexray_set_frametrigger.argtypes =[s32,ps32,s32,PLIBTrigger_def,s32,s32]
tsflexray_set_frametrigger.restype = s32
tsflexray_cmdreq = dll.tsflexray_cmdreq
#arg[0] AIdxChn : None
#arg[1] AAction : None
#arg[2] AWriteBuffer : None
#arg[3] AWriteBufferSize : None
#arg[4] AReadBuffer : None
#arg[5] AReadBufferSize : None
#arg[6] ATimeoutMs : None
tsflexray_cmdreq.argtypes =[s32,s32,pu8,s32,pu8,ps32,s32]
tsflexray_cmdreq.restype = s32
tsapp_transmit_flexray_sync = dll.tsapp_transmit_flexray_sync
#arg[0] AData : None
#arg[1] ATimeoutMs : None
tsapp_transmit_flexray_sync.argtypes =[PLIBFlexRay,s32]
tsapp_transmit_flexray_sync.restype = s32
tsapp_transmit_flexray_async = dll.tsapp_transmit_flexray_async
#arg[0] AData : None
tsapp_transmit_flexray_async.argtypes =[PLIBFlexRay]
tsapp_transmit_flexray_async.restype = s32
tsflexray_start_net = dll.tsflexray_start_net
#arg[0] AIdxChn : None
#arg[1] ATimeoutMs : None
tsflexray_start_net.argtypes =[s32,s32]
tsflexray_start_net.restype = s32
tsflexray_stop_net = dll.tsflexray_stop_net
#arg[0] AIdxChn : None
#arg[1] ATimeoutMs : None
tsflexray_stop_net.argtypes =[s32,s32]
tsflexray_stop_net.restype = s32
tsflexray_wakeup_pattern = dll.tsflexray_wakeup_pattern
#arg[0] AIdxChn : None
#arg[1] ATimeoutMs : None
tsflexray_wakeup_pattern.argtypes =[s32,s32]
tsflexray_wakeup_pattern.restype = s32
flexray_enable_frame = dll.flexray_enable_frame
#arg[0] AChnIdx : None
#arg[1] SlotID : None
#arg[2] BaseCycle : None
#arg[3] RepCycle : None
#arg[4] ATimeOut : None
flexray_enable_frame.argtypes =[s32,u8,u8,u8,s32]
flexray_enable_frame.restype = s32
flexray_disable_frame = dll.flexray_disable_frame
#arg[0] AChnIdx : None
#arg[1] SlotID : None
#arg[2] BaseCycle : None
#arg[3] RepCycle : None
#arg[4] ATimeOut : None
flexray_disable_frame.argtypes =[s32,u8,u8,u8,s32]
flexray_disable_frame.restype = s32
tslin_switch_runtime_schedule_table = dll.tslin_switch_runtime_schedule_table
#arg[0] AChnIdx : None
tslin_switch_runtime_schedule_table.argtypes =[s32]
tslin_switch_runtime_schedule_table.restype = s32
tslin_switch_idle_schedule_table = dll.tslin_switch_idle_schedule_table
#arg[0] AChnIdx : None
tslin_switch_idle_schedule_table.argtypes =[s32]
tslin_switch_idle_schedule_table.restype = s32
tslin_switch_normal_schedule_table = dll.tslin_switch_normal_schedule_table
#arg[0] AChnIdx : None
#arg[1] ASchIndex : None
tslin_switch_normal_schedule_table.argtypes =[s32,s32]
tslin_switch_normal_schedule_table.restype = s32
tslin_stop_lin_channel = dll.tslin_stop_lin_channel
#arg[0] AChnIdx : None
tslin_stop_lin_channel.argtypes =[s32]
tslin_stop_lin_channel.restype = s32
tslin_start_lin_channel = dll.tslin_start_lin_channel
#arg[0] AChnIdx : None
tslin_start_lin_channel.argtypes =[s32]
tslin_start_lin_channel.restype = s32
tslin_set_node_functiontype = dll.tslin_set_node_functiontype
#arg[0] AChnIdx : None
#arg[1] AFunctionType : None
tslin_set_node_functiontype.argtypes =[s32,s32]
tslin_set_node_functiontype.restype = s32
tslin_batch_set_schedule_start = dll.tslin_batch_set_schedule_start
#arg[0] AChnIdx : None
tslin_batch_set_schedule_start.argtypes =[s32]
tslin_batch_set_schedule_start.restype = s32
tslin_batch_add_schedule_frame = dll.tslin_batch_add_schedule_frame
#arg[0] AChnIdx : None
#arg[1] ALINData : None
#arg[2] ADelayMs : None
tslin_batch_add_schedule_frame.argtypes =[s32,PLIBLIN,s32]
tslin_batch_add_schedule_frame.restype = s32
tslin_batch_set_schedule_end = dll.tslin_batch_set_schedule_end
#arg[0] AChnIdx : None
tslin_batch_set_schedule_end.argtypes =[s32]
tslin_batch_set_schedule_end.restype = s32
tstp_lin_master_request = dll.tstp_lin_master_request
#arg[0] AChnIdx : None
#arg[1] ANAD : None
#arg[2] AData : None
#arg[3] ADataNum : None
#arg[4] ATimeoutMs : None
tstp_lin_master_request.argtypes =[s32,u8,pu8,s32,s32]
tstp_lin_master_request.restype = s32
tstp_lin_master_request_intervalms = dll.tstp_lin_master_request_intervalms
#arg[0] AChnIdx : None
#arg[1] AData : None
tstp_lin_master_request_intervalms.argtypes =[s32,u16]
tstp_lin_master_request_intervalms.restype = s32
tstp_lin_reset = dll.tstp_lin_reset
#arg[0] AChnIdx : None
tstp_lin_reset.argtypes =[s32]
tstp_lin_reset.restype = s32
tstp_lin_slave_response_intervalms = dll.tstp_lin_slave_response_intervalms
#arg[0] AChnIdx : None
#arg[1] AData : None
tstp_lin_slave_response_intervalms.argtypes =[s32,u16]
tstp_lin_slave_response_intervalms.restype = s32
tstp_lin_tp_para_default = dll.tstp_lin_tp_para_default
#arg[0] AChnIdx : None
#arg[1] AReqIntervalMs : None
#arg[2] AResIntervalMs : None
#arg[3] AResRetryTime : None
tstp_lin_tp_para_default.argtypes =[s32,u16,u16,u16]
tstp_lin_tp_para_default.restype = s32
tstp_lin_tp_para_special = dll.tstp_lin_tp_para_special
#arg[0] AChnIdx : None
#arg[1] AReqIntervalMs : None
#arg[2] AResIntervalMs : None
#arg[3] AResRetryTime : None
tstp_lin_tp_para_special.argtypes =[s32,u16,u16,u16]
tstp_lin_tp_para_special.restype = s32
tsdiag_lin_read_data_by_identifier = dll.tsdiag_lin_read_data_by_identifier
#arg[0] AChnIdx : None
#arg[1] ANAD : None
#arg[2] AId : None
#arg[3] AResNAD : None
#arg[4] AResData : None
#arg[5] AResDataNum : None
#arg[6] ATimeoutMS : None
tsdiag_lin_read_data_by_identifier.argtypes =[s32,u8,u16,pu8,pu8,ps32,s32]
tsdiag_lin_read_data_by_identifier.restype = s32
tsdiag_lin_write_data_by_identifier = dll.tsdiag_lin_write_data_by_identifier
#arg[0] AChnIdx : None
#arg[1] AReqNAD : None
#arg[2] AID : None
#arg[3] AReqData : None
#arg[4] AReqDataNum : None
#arg[5] AResNAD : None
#arg[6] AResData : None
#arg[7] AResDataNum : None
#arg[8] ATimeoutMS : None
tsdiag_lin_write_data_by_identifier.argtypes =[s32,u8,u16,pu8,s32,pu8,pu8,ps32,s32]
tsdiag_lin_write_data_by_identifier.restype = s32
tsdiag_lin_session_control = dll.tsdiag_lin_session_control
#arg[0] AChnIdx : None
#arg[1] ANAD : None
#arg[2] ANewSession : None
#arg[3] ATimeoutMS : None
tsdiag_lin_session_control.argtypes =[s32,u8,u8,s32]
tsdiag_lin_session_control.restype = s32
tsdiag_lin_fault_memory_read = dll.tsdiag_lin_fault_memory_read
#arg[0] AChnIdx : None
#arg[1] ANAD : None
#arg[2] ATimeoutMS : None
tsdiag_lin_fault_memory_read.argtypes =[s32,u8,s32]
tsdiag_lin_fault_memory_read.restype = s32
tsdiag_lin_fault_memory_clear = dll.tsdiag_lin_fault_memory_clear
#arg[0] AChnIdx : None
#arg[1] ANAD : None
#arg[2] ATimeoutMS : None
tsdiag_lin_fault_memory_clear.argtypes =[s32,u8,s32]
tsdiag_lin_fault_memory_clear.restype = s32
tsdiag_can_create = dll.tsdiag_can_create
#arg[0] pDiagModuleIndex : None
#arg[1] AChnIndex : None
#arg[2] ASupportFDCAN : None
#arg[3] AMaxDLC : None
#arg[4] ARequestID : None
#arg[5] ARequestIDIsStd : None
#arg[6] AResponseID : None
#arg[7] AResponseIDIsStd : None
#arg[8] AFunctionID : None
#arg[9] AFunctionIDIsStd : None
tsdiag_can_create.argtypes =[ps32,s32,u8,u8,u32,c_bool,u32,c_bool,u32,c_bool]
tsdiag_can_create.restype = s32
tsdiag_can_delete = dll.tsdiag_can_delete
#arg[0] ADiagModuleIndex : None
tsdiag_can_delete.argtypes =[s32]
tsdiag_can_delete.restype = s32
tsdiag_can_delete_all = dll.tsdiag_can_delete_all
tsdiag_can_delete_all.argtypes =[]
tsdiag_can_delete_all.restype = s32
tsdiag_set_channel = dll.tsdiag_set_channel
#arg[0] ADiagModuleIndex : None
#arg[1] AChnIndex : None
tsdiag_set_channel.argtypes =[s32,s32]
tsdiag_set_channel.restype = s32
tsdiag_set_fdmode = dll.tsdiag_set_fdmode
#arg[0] ADiagModuleIndex : None
#arg[1] AFDMode : None
#arg[2] AMaxLength : None
tsdiag_set_fdmode.argtypes =[s32,c_bool,s32]
tsdiag_set_fdmode.restype = s32
tsdiag_set_request_id = dll.tsdiag_set_request_id
#arg[0] ADiagModuleIndex : None
#arg[1] ARequestID : None
#arg[2] AIsStandard : None
tsdiag_set_request_id.argtypes =[s32,s32,c_bool]
tsdiag_set_request_id.restype = s32
tsdiag_set_response_id = dll.tsdiag_set_response_id
#arg[0] ADiagModuleIndex : None
#arg[1] ARequestID : None
#arg[2] AIsStandard : None
tsdiag_set_response_id.argtypes =[s32,s32,c_bool]
tsdiag_set_response_id.restype = s32
tsdiag_set_function_id = dll.tsdiag_set_function_id
#arg[0] ADiagModuleIndex : None
#arg[1] ARequestID : None
#arg[2] AIsStandard : None
tsdiag_set_function_id.argtypes =[s32,s32,c_bool]
tsdiag_set_function_id.restype = s32
tsdiag_set_stmin = dll.tsdiag_set_stmin
#arg[0] ADiagModuleIndex : None
#arg[1] ASTMin : None
tsdiag_set_stmin.argtypes =[s32,s32]
tsdiag_set_stmin.restype = s32
tsdiag_set_blocksize = dll.tsdiag_set_blocksize
#arg[0] ADiagModuleIndex : None
#arg[1] ABlockSize : None
tsdiag_set_blocksize.argtypes =[s32,s32]
tsdiag_set_blocksize.restype = s32
tsdiag_set_maxlength = dll.tsdiag_set_maxlength
#arg[0] ADiagModuleIndex : None
#arg[1] AMaxLength : None
tsdiag_set_maxlength.argtypes =[s32,s32]
tsdiag_set_maxlength.restype = s32
tsdiag_set_fcdelay = dll.tsdiag_set_fcdelay
#arg[0] ADiagModuleIndex : None
#arg[1] AFCDelay : None
tsdiag_set_fcdelay.argtypes =[s32,s32]
tsdiag_set_fcdelay.restype = s32
tsdiag_set_filled_byte = dll.tsdiag_set_filled_byte
#arg[0] ADiagModuleIndex : None
#arg[1] AFilledByte : None
tsdiag_set_filled_byte.argtypes =[s32,u8]
tsdiag_set_filled_byte.restype = s32
tsdiag_set_p2_timeout = dll.tsdiag_set_p2_timeout
#arg[0] ADiagModuleIndex : None
#arg[1] ATimeMs : None
tsdiag_set_p2_timeout.argtypes =[s32,s32]
tsdiag_set_p2_timeout.restype = s32
tsdiag_set_p2_extended = dll.tsdiag_set_p2_extended
#arg[0] ADiagModuleIndex : None
#arg[1] ATimeMs : None
tsdiag_set_p2_extended.argtypes =[s32,s32]
tsdiag_set_p2_extended.restype = s32
tsdiag_set_s3_servertime = dll.tsdiag_set_s3_servertime
#arg[0] ADiagModuleIndex : None
#arg[1] ATimeMs : None
tsdiag_set_s3_servertime.argtypes =[s32,s32]
tsdiag_set_s3_servertime.restype = s32
tsdiag_set_s3_clienttime = dll.tsdiag_set_s3_clienttime
#arg[0] ADiagModuleIndex : None
#arg[1] ATimeMs : None
tsdiag_set_s3_clienttime.argtypes =[s32,s32]
tsdiag_set_s3_clienttime.restype = s32
tstp_can_send_functional = dll.tstp_can_send_functional
#arg[0] ADiagModuleIndex : None
#arg[1] AReqDataArray : None
#arg[2] AReqDataSize : None
tstp_can_send_functional.argtypes =[s32,pu8,s32]
tstp_can_send_functional.restype = s32
tstp_can_send_request = dll.tstp_can_send_request
#arg[0] ADiagModuleIndex : None
#arg[1] AReqDataArray : None
#arg[2] AReqDataSize : None
tstp_can_send_request.argtypes =[s32,pu8,s32]
tstp_can_send_request.restype = s32
tstp_can_request_and_get_response = dll.tstp_can_request_and_get_response
#arg[0] ADiagModuleIndex : None
#arg[1] AReqDataArray : None
#arg[2] AReqDataSize : None
#arg[3] AResponseDataArray : None
#arg[4] AResponseDataSize : None
tstp_can_request_and_get_response.argtypes =[s32,pu8,s32,pu8,ps32]
tstp_can_request_and_get_response.restype = s32
tstp_can_register_tx_completed_recall = dll.tstp_can_register_tx_completed_recall
#arg[0] ADiagModuleIndex : None
#arg[1] ATxcompleted : None
tstp_can_register_tx_completed_recall.argtypes =[s32,N_USData_TranslateCompleted_Recall]
tstp_can_register_tx_completed_recall.restype = s32
tstp_can_register_rx_completed_recall = dll.tstp_can_register_rx_completed_recall
#arg[0] ADiagModuleIndex : None
#arg[1] ARxcompleted : None
tstp_can_register_rx_completed_recall.argtypes =[s32,N_USData_TranslateCompleted_Recall]
tstp_can_register_rx_completed_recall.restype = s32
tstp_can_register_tx_completed_recall_internal = dll.tstp_can_register_tx_completed_recall_internal
#arg[0] ADiagModuleIndex : None
#arg[1] ATxcompleted : None
tstp_can_register_tx_completed_recall_internal.argtypes =[s32,N_USData_TranslateCompleted_Recall_Obj]
tstp_can_register_tx_completed_recall_internal.restype = s32
tstp_can_register_rx_completed_recall_internal = dll.tstp_can_register_rx_completed_recall_internal
#arg[0] ADiagModuleIndex : None
#arg[1] ARxcompleted : None
tstp_can_register_rx_completed_recall_internal.argtypes =[s32,N_USData_TranslateCompleted_Recall_Obj]
tstp_can_register_rx_completed_recall_internal.restype = s32
tsdiag_can_session_control = dll.tsdiag_can_session_control
#arg[0] ADiagModuleIndex : None
#arg[1] ASubSession : None
tsdiag_can_session_control.argtypes =[s32,u8]
tsdiag_can_session_control.restype = s32
tsdiag_can_routine_control = dll.tsdiag_can_routine_control
#arg[0] ADiagModuleIndex : None
#arg[1] ARoutineControlType : None
#arg[2] ARoutintID : None
tsdiag_can_routine_control.argtypes =[s32,u8,u16]
tsdiag_can_routine_control.restype = s32
tsdiag_can_communication_control = dll.tsdiag_can_communication_control
#arg[0] ADiagModuleIndex : None
#arg[1] AControlType : None
tsdiag_can_communication_control.argtypes =[s32,u8]
tsdiag_can_communication_control.restype = s32
tsdiag_can_security_access_request_seed = dll.tsdiag_can_security_access_request_seed
#arg[0] ADiagModuleIndex : None
#arg[1] ALevel : None
#arg[2] ARecSeed : None
#arg[3] ARecSeedSize : None
tsdiag_can_security_access_request_seed.argtypes =[s32,s32,pu8,ps32]
tsdiag_can_security_access_request_seed.restype = s32
tsdiag_can_security_access_send_key = dll.tsdiag_can_security_access_send_key
#arg[0] ADiagModuleIndex : None
#arg[1] ALevel : None
#arg[2] AKeyValue : None
#arg[3] AKeySize : None
tsdiag_can_security_access_send_key.argtypes =[s32,s32,pu8,s32]
tsdiag_can_security_access_send_key.restype = s32
tsdiag_can_request_download = dll.tsdiag_can_request_download
#arg[0] ADiagModuleIndex : None
#arg[1] AMemAddr : None
#arg[2] AMemSize : None
tsdiag_can_request_download.argtypes =[s32,s32,u32]
tsdiag_can_request_download.restype = s32
tsdiag_can_request_upload = dll.tsdiag_can_request_upload
#arg[0] ADiagModuleIndex : None
#arg[1] AMemAddr : None
#arg[2] AMemSize : None
tsdiag_can_request_upload.argtypes =[s32,s32,u32]
tsdiag_can_request_upload.restype = s32
tsdiag_can_transfer_data = dll.tsdiag_can_transfer_data
#arg[0] ADiagModuleIndex : None
#arg[1] ASourceDatas : None
#arg[2] ADataSize : None
#arg[3] AReqCase : None
tsdiag_can_transfer_data.argtypes =[s32,pu8,s32,s32]
tsdiag_can_transfer_data.restype = s32
tsdiag_can_request_transfer_exit = dll.tsdiag_can_request_transfer_exit
#arg[0] ADiagModuleIndex : None
tsdiag_can_request_transfer_exit.argtypes =[s32]
tsdiag_can_request_transfer_exit.restype = s32
tsdiag_can_write_data_by_identifier = dll.tsdiag_can_write_data_by_identifier
#arg[0] ADiagModuleIndex : None
#arg[1] ADataIdentifier : None
#arg[2] AWriteData : None
#arg[3] AWriteDataSize : None
tsdiag_can_write_data_by_identifier.argtypes =[s32,u16,pu8,s32]
tsdiag_can_write_data_by_identifier.restype = s32
tsdiag_can_read_data_by_identifier = dll.tsdiag_can_read_data_by_identifier
#arg[0] ADiagModuleIndex : None
#arg[1] ADataIdentifier : None
#arg[2] AReturnArray : None
#arg[3] AReturnArraySize : None
tsdiag_can_read_data_by_identifier.argtypes =[s32,u16,pu8,ps32]
tsdiag_can_read_data_by_identifier.restype = s32
tslog_logger_delete_file = dll.tslog_logger_delete_file
#arg[0] AChnIdx : None
#arg[1] AFileIndex : None
#arg[2] ATimeoutMS : None
tslog_logger_delete_file.argtypes =[s32,s32,s32]
tslog_logger_delete_file.restype = s32
tslog_logger_start_export_blf_file = dll.tslog_logger_start_export_blf_file
#arg[0] AChnIdx : None
#arg[1] AFileIndex : None
#arg[2] ABlfFileName : None
#arg[3] AStartTimeUs : None
#arg[4] AMaxSize : None
#arg[5] AProgress : None
#arg[6] AYear : None
#arg[7] AMonth : None
#arg[8] ADay : None
#arg[9] AHour : None
#arg[10] AMinute : None
#arg[11] ASecond : None
#arg[12] AMinisecond : None
#arg[13] ATimeoutMS : None
tslog_logger_start_export_blf_file.argtypes =[s32,s32,pchar,u64,s32,pdouble,u16,u16,u16,u16,u16,u16,u16,s32]
tslog_logger_start_export_blf_file.restype = s32
tslog_logger_abort_export_blf_file = dll.tslog_logger_abort_export_blf_file
#arg[0] AChnIdx : None
#arg[1] ATimeoutMS : None
tslog_logger_abort_export_blf_file.argtypes =[s32,s32]
tslog_logger_abort_export_blf_file.restype = s32
tslog_logger_start_online_replay = dll.tslog_logger_start_online_replay
#arg[0] AChnIdx : None
#arg[1] AFileIndex : None
#arg[2] AStartTimeUs : None
#arg[3] AMaxSize : None
#arg[4] ATimeoutMS : None
tslog_logger_start_online_replay.argtypes =[s32,s32,u64,s32,s32]
tslog_logger_start_online_replay.restype = s32
tslog_logger_start_offline_replay = dll.tslog_logger_start_offline_replay
#arg[0] AChnIdx : None
#arg[1] AFileIndex : None
#arg[2] AStartTimeUs : None
#arg[3] AMaxSize : None
#arg[4] ATimeoutMS : None
tslog_logger_start_offline_replay.argtypes =[s32,s32,u64,s32,s32]
tslog_logger_start_offline_replay.restype = s32
tslog_logger_stop_replay = dll.tslog_logger_stop_replay
#arg[0] AChnIdx : None
#arg[1] ATimeoutMS : None
tslog_logger_stop_replay.argtypes =[s32,s32]
tslog_logger_stop_replay.restype = s32
tslog_logger_set_logger_mode = dll.tslog_logger_set_logger_mode
#arg[0] AChnIdx : None
#arg[1] AMode : None
#arg[2] ATimeoutMS : None
tslog_logger_set_logger_mode.argtypes =[s32,u8,s32]
tslog_logger_set_logger_mode.restype = s32
tsapp_logger_enable_gps_module = dll.tsapp_logger_enable_gps_module
#arg[0] AChnIdx : None
#arg[1] AEnable : None
#arg[2] ATimeoutMS : None
tsapp_logger_enable_gps_module.argtypes =[s32,s32,s32]
tsapp_logger_enable_gps_module.restype = s32
tsapp_reset_gps_module = dll.tsapp_reset_gps_module
#arg[0] AChnIdx : None
#arg[1] AInitBaudrate : None
#arg[2] ATargetBaudrate : None
#arg[3] ATimeoutMS : None
tsapp_reset_gps_module.argtypes =[s32,s32,s32,s32]
tsapp_reset_gps_module.restype = s32
tsapp_unlock_camera_channel = dll.tsapp_unlock_camera_channel
#arg[0] AChnIdx : None
tsapp_unlock_camera_channel.argtypes =[s32]
tsapp_unlock_camera_channel.restype = s32
tsmp_reload_settings = dll.tsmp_reload_settings
tsmp_reload_settings.argtypes =[]
tsmp_reload_settings.restype = s32
tsmp_load = dll.tsmp_load
#arg[0] AMPFileName : None
#arg[1] ARunAfterLoad : None
tsmp_load.argtypes =[pchar,c_bool]
tsmp_load.restype = s32
tsmp_unload = dll.tsmp_unload
#arg[0] AMPFileName : None
tsmp_unload.argtypes =[pchar]
tsmp_unload.restype = s32
tsmp_unload_all = dll.tsmp_unload_all
tsmp_unload_all.argtypes =[]
tsmp_unload_all.restype = s32
tsmp_run = dll.tsmp_run
#arg[0] AMPFileName : None
tsmp_run.argtypes =[pchar]
tsmp_run.restype = s32
tsmp_is_running = dll.tsmp_is_running
#arg[0] AMPFileName : None
#arg[1] AIsRunning : None
tsmp_is_running.argtypes =[pchar,pbool]
tsmp_is_running.restype = s32
tsmp_stop = dll.tsmp_stop
#arg[0] AMPFileName : None
tsmp_stop.argtypes =[pchar]
tsmp_stop.restype = s32
tsmp_run_all = dll.tsmp_run_all
tsmp_run_all.argtypes =[]
tsmp_run_all.restype = s32
tsmp_stop_all = dll.tsmp_stop_all
tsmp_stop_all.argtypes =[]
tsmp_stop_all.restype = s32
tsmp_call_function = dll.tsmp_call_function
#arg[0] AGroupName : None
#arg[1] AFuncName : None
#arg[2] AInParameters : None
#arg[3] AOutParameters : None
tsmp_call_function.argtypes =[pchar,pchar,pchar,ppchar]
tsmp_call_function.restype = s32
tsmp_get_function_address = dll.tsmp_get_function_address
#arg[0] AGroupName : None
#arg[1] AFuncName : None
#arg[2] AAddress : None
tsmp_get_function_address.argtypes =[pchar,pchar,ps32]
tsmp_get_function_address.restype = s32
tsmp_get_function_prototype = dll.tsmp_get_function_prototype
#arg[0] AGroupName : None
#arg[1] AFuncName : None
#arg[2] APrototype : None
tsmp_get_function_prototype.argtypes =[pchar,pchar,ppchar]
tsmp_get_function_prototype.restype = s32
tsmp_get_mp_function_list = dll.tsmp_get_mp_function_list
#arg[0] AGroupName : None
#arg[1] AList : None
tsmp_get_mp_function_list.argtypes =[pchar,ppchar]
tsmp_get_mp_function_list.restype = s32
tsmp_get_mp_list = dll.tsmp_get_mp_list
#arg[0] AList : None
tsmp_get_mp_list.argtypes =[ppchar]
tsmp_get_mp_list.restype = s32
db_get_flexray_cluster_parameters = dll.db_get_flexray_cluster_parameters
#arg[0] AIdxChn : None
#arg[1] AClusterName : None
#arg[2] AValue : None
db_get_flexray_cluster_parameters.argtypes =[s32,pchar,PLIBFlexRayClusterParameters]
db_get_flexray_cluster_parameters.restype = s32
db_get_flexray_controller_parameters = dll.db_get_flexray_controller_parameters
#arg[0] AIdxChn : None
#arg[1] AClusterName : None
#arg[2] AECUName : None
#arg[3] AValue : None
db_get_flexray_controller_parameters.argtypes =[s32,pchar,pchar,PLIBFlexRayControllerParameters]
db_get_flexray_controller_parameters.restype = s32
set_system_var_event_support = dll.set_system_var_event_support
#arg[0] ACompleteName : None
#arg[1] ASupport : None
set_system_var_event_support.argtypes =[pchar,c_bool]
set_system_var_event_support.restype = s32
get_system_var_event_support = dll.get_system_var_event_support
#arg[0] ACompleteName : None
#arg[1] ASupport : None
get_system_var_event_support.argtypes =[pchar,pbool]
get_system_var_event_support.restype = s32
get_date_time = dll.get_date_time
#arg[0] AYear : None
#arg[1] AMonth : None
#arg[2] ADay : None
#arg[3] AHour : None
#arg[4] AMinute : None
#arg[5] ASecond : None
#arg[6] AMilliseconds : None
get_date_time.argtypes =[ps32,ps32,ps32,ps32,ps32,ps32,ps32]
get_date_time.restype = s32
tslog_disable_online_replay_filter = dll.tslog_disable_online_replay_filter
#arg[0] AIndex : None
tslog_disable_online_replay_filter.argtypes =[s32]
tslog_disable_online_replay_filter.restype = s32
tslog_set_online_replay_filter = dll.tslog_set_online_replay_filter
#arg[0] AIndex : None
#arg[1] AIsPassFilter : None
#arg[2] ACount : None
#arg[3] AIdxChannels : None
#arg[4] AIdentifiers : None
tslog_set_online_replay_filter.argtypes =[s32,c_bool,s32,ps32,ps32]
tslog_set_online_replay_filter.restype = s32
set_can_signal_raw_value = dll.set_can_signal_raw_value
#arg[0] ACANSignal : None
#arg[1] AData : None
#arg[2] AValue : None
set_can_signal_raw_value.argtypes =[PMPCANSignal,pu8,s64]
set_can_signal_raw_value.restype = s32
get_can_signal_raw_value = dll.get_can_signal_raw_value
#arg[0] ACANSignal : None
#arg[1] AData : None
get_can_signal_raw_value.argtypes =[PMPCANSignal,pu8]
get_can_signal_raw_value.restype = u64
set_lin_signal_raw_value = dll.set_lin_signal_raw_value
#arg[0] ALINSignal : None
#arg[1] AData : None
#arg[2] AValue : None
set_lin_signal_raw_value.argtypes =[PMPLINSignal,pu8,s64]
set_lin_signal_raw_value.restype = s32
get_lin_signal_raw_value = dll.get_lin_signal_raw_value
#arg[0] ALINSignal : None
#arg[1] AData : None
get_lin_signal_raw_value.argtypes =[PMPLINSignal,pu8]
get_lin_signal_raw_value.restype = u64
set_flexray_signal_raw_value = dll.set_flexray_signal_raw_value
#arg[0] AFlexRaySignal : None
#arg[1] AData : None
#arg[2] AValue : None
set_flexray_signal_raw_value.argtypes =[PMPFlexRaySignal,pu8,double]
set_flexray_signal_raw_value.restype = s32
get_flexray_signal_raw_value = dll.get_flexray_signal_raw_value
#arg[0] AFlexRaySignal : None
#arg[1] AData : None
get_flexray_signal_raw_value.argtypes =[PMPFlexRaySignal,pu8]
get_flexray_signal_raw_value.restype = u64
tscom_set_lin_signal_value = dll.tscom_set_lin_signal_value
#arg[0] AFlexRaySignal : None
#arg[1] AData : None
#arg[2] AValue : None
tscom_set_lin_signal_value.argtypes =[PMPLINSignal,pu8,double]
tscom_set_lin_signal_value.restype = s32
tscom_set_flexray_signal_value = dll.tscom_set_flexray_signal_value
#arg[0] AFlexRaySignal : None
#arg[1] AData : None
#arg[2] AValue : None
tscom_set_flexray_signal_value.argtypes =[PMPFlexRaySignal,pu8,double]
tscom_set_flexray_signal_value.restype = s32
tscom_set_can_signal_value = dll.tscom_set_can_signal_value
#arg[0] AFlexRaySignal : None
#arg[1] AData : None
#arg[2] AValue : None
tscom_set_can_signal_value.argtypes =[PMPCANSignal,pu8,double]
tscom_set_can_signal_value.restype = s32
tscom_get_lin_signal_value = dll.tscom_get_lin_signal_value
#arg[0] AFlexRaySignal : None
#arg[1] AData : None
tscom_get_lin_signal_value.argtypes =[PMPLINSignal,pu8]
tscom_get_lin_signal_value.restype = double
tscom_get_flexray_signal_value = dll.tscom_get_flexray_signal_value
#arg[0] AFlexRaySignal : None
#arg[1] AData : None
tscom_get_flexray_signal_value.argtypes =[PMPFlexRaySignal,pu8]
tscom_get_flexray_signal_value.restype = double
tscom_get_can_signal_value = dll.tscom_get_can_signal_value
#arg[0] AFlexRaySignal : None
#arg[1] AData : None
tscom_get_can_signal_value.argtypes =[PMPCANSignal,pu8]
tscom_get_can_signal_value.restype = double
gpg_delete_all_modules = dll.gpg_delete_all_modules
gpg_delete_all_modules.argtypes =[]
gpg_delete_all_modules.restype = s32
gpg_create_module = dll.gpg_create_module
#arg[0] AProgramName : None
#arg[1] ADisplayName : None
#arg[2] AModuleId : None
#arg[3] AEntryPointId : None
gpg_create_module.argtypes =[pchar,pchar,ps64,ps64]
gpg_create_module.restype = s32
gpg_delete_module = dll.gpg_delete_module
#arg[0] AModuleId : None
gpg_delete_module.argtypes =[s64]
gpg_delete_module.restype = s32
gpg_deploy_module = dll.gpg_deploy_module
#arg[0] AModuleId : None
#arg[1] AGraphicProgramWindowTitle : None
gpg_deploy_module.argtypes =[s64,pchar]
gpg_deploy_module.restype = s32
gpg_add_action_down = dll.gpg_add_action_down
#arg[0] AModuleId : None
#arg[1] AUpperActionId : None
#arg[2] ADisplayName : None
#arg[3] AComment : None
#arg[4] AActionId : None
gpg_add_action_down.argtypes =[s64,s64,pchar,pchar,ps64]
gpg_add_action_down.restype = s32
gpg_add_action_right = dll.gpg_add_action_right
#arg[0] AModuleId : None
#arg[1] ALeftActionId : None
#arg[2] ADisplayName : None
#arg[3] AComment : None
#arg[4] AActionId : None
gpg_add_action_right.argtypes =[s64,s64,pchar,pchar,ps64]
gpg_add_action_right.restype = s32
gpg_add_goto_down = dll.gpg_add_goto_down
#arg[0] AModuleId : None
#arg[1] AUpperActionId : None
#arg[2] ADisplayName : None
#arg[3] AComment : None
#arg[4] AJumpLabel : None
#arg[5] AActionId : None
gpg_add_goto_down.argtypes =[s64,s64,pchar,pchar,pchar,ps64]
gpg_add_goto_down.restype = s32
gpg_add_goto_right = dll.gpg_add_goto_right
#arg[0] AModuleId : None
#arg[1] ALeftActionId : None
#arg[2] ADisplayName : None
#arg[3] AComment : None
#arg[4] AJumpLabel : None
#arg[5] AActionId : None
gpg_add_goto_right.argtypes =[s64,s64,pchar,pchar,pchar,ps64]
gpg_add_goto_right.restype = s32
gpg_add_from_down = dll.gpg_add_from_down
#arg[0] AModuleId : None
#arg[1] AUpperActionId : None
#arg[2] ADisplayName : None
#arg[3] AComment : None
#arg[4] AJumpLabel : None
#arg[5] AActionId : None
gpg_add_from_down.argtypes =[s64,s64,pchar,pchar,pchar,ps64]
gpg_add_from_down.restype = s32
gpg_add_group_down = dll.gpg_add_group_down
#arg[0] AModuleId : None
#arg[1] AUpperActionId : None
#arg[2] ADisplayName : None
#arg[3] AComment : None
#arg[4] AGroupId : None
#arg[5] AEntryPointId : None
gpg_add_group_down.argtypes =[s64,s64,pchar,pchar,ps64,ps64]
gpg_add_group_down.restype = s32
gpg_add_group_right = dll.gpg_add_group_right
#arg[0] AModuleId : None
#arg[1] ALeftActionId : None
#arg[2] ADisplayName : None
#arg[3] AComment : None
#arg[4] AGroupId : None
#arg[5] AEntryPointId : None
gpg_add_group_right.argtypes =[s64,s64,pchar,pchar,ps64,ps64]
gpg_add_group_right.restype = s32
gpg_delete_action = dll.gpg_delete_action
#arg[0] AModuleId : None
#arg[1] AActionId : None
gpg_delete_action.argtypes =[s64,s64]
gpg_delete_action.restype = s32
gpg_set_action_nop = dll.gpg_set_action_nop
#arg[0] AModuleId : None
#arg[1] AActionId : None
gpg_set_action_nop.argtypes =[s64,s64]
gpg_set_action_nop.restype = s32
gpg_set_action_signal_read_write = dll.gpg_set_action_signal_read_write
#arg[0] AModuleId : None
#arg[1] AActionId : None
gpg_set_action_signal_read_write.argtypes =[s64,s64]
gpg_set_action_signal_read_write.restype = s32
gpg_set_action_api_call = dll.gpg_set_action_api_call
#arg[0] AModuleId : None
#arg[1] AActionId : None
gpg_set_action_api_call.argtypes =[s64,s64]
gpg_set_action_api_call.restype = s32
gpg_set_action_expression = dll.gpg_set_action_expression
#arg[0] AModuleId : None
#arg[1] AActionId : None
gpg_set_action_expression.argtypes =[s64,s64]
gpg_set_action_expression.restype = s32
gpg_configure_action_basic = dll.gpg_configure_action_basic
#arg[0] AModuleId : None
#arg[1] AActionId : None
#arg[2] ADisplayName : None
#arg[3] AComment : None
#arg[4] ATimeoutMs : None
gpg_configure_action_basic.argtypes =[s64,s64,pchar,pchar,s32]
gpg_configure_action_basic.restype = s32
gpg_configure_goto = dll.gpg_configure_goto
#arg[0] AModuleId : None
#arg[1] AActionId : None
#arg[2] ADisplayName : None
#arg[3] AComment : None
#arg[4] AJumpLabel : None
gpg_configure_goto.argtypes =[s64,s64,pchar,pchar,pchar]
gpg_configure_goto.restype = s32
gpg_configure_from = dll.gpg_configure_from
#arg[0] AModuleId : None
#arg[1] AActionId : None
#arg[2] ADisplayName : None
#arg[3] AComment : None
#arg[4] AJumpLabel : None
gpg_configure_from.argtypes =[s64,s64,pchar,pchar,pchar]
gpg_configure_from.restype = s32
gpg_configure_nop = dll.gpg_configure_nop
#arg[0] AModuleId : None
#arg[1] AActionId : None
#arg[2] ANextDirectionIsDown : None
#arg[3] AResultOK : None
#arg[4] AJumpBackIfEnded : None
gpg_configure_nop.argtypes =[s64,s64,c_bool,c_bool,c_bool]
gpg_configure_nop.restype = s32
gpg_configure_group = dll.gpg_configure_group
#arg[0] AModuleId : None
#arg[1] AActionId : None
#arg[2] ARepeatCountType : None
#arg[3] ARepeatCountRepr : None
gpg_configure_group.argtypes =[s64,s64,s32,pchar]
gpg_configure_group.restype = s32
gpg_configure_signal_read_write_list_clear = dll.gpg_configure_signal_read_write_list_clear
#arg[0] AModuleId : None
#arg[1] AActionId : None
gpg_configure_signal_read_write_list_clear.argtypes =[s64,s64]
gpg_configure_signal_read_write_list_clear.restype = s32
gpg_configure_signal_write_list_append = dll.gpg_configure_signal_write_list_append
#arg[0] AModuleId : None
#arg[1] AActionId : None
#arg[2] ADestSignalType : None
#arg[3] ASrcSignalType : None
#arg[4] ADestSignalExpr : None
#arg[5] ASrcSignalExpr : None
#arg[6] AItemIndex : None
gpg_configure_signal_write_list_append.argtypes =[s64,s64,s32,s32,pchar,pchar,ps32]
gpg_configure_signal_write_list_append.restype = s32
gpg_configure_signal_read_list_append = dll.gpg_configure_signal_read_list_append
#arg[0] AModuleId : None
#arg[1] AActionId : None
#arg[2] AIsConditionAND : None
#arg[3] ADestSignalType : None
#arg[4] AMinSignalType : None
#arg[5] AMaxSignalType : None
#arg[6] ADestSignalExpr : None
#arg[7] AMinSignalExpr : None
#arg[8] AMaxSignalExpr : None
#arg[9] AItemIndex : None
gpg_configure_signal_read_list_append.argtypes =[s64,s64,c_bool,s32,s32,s32,pchar,pchar,pchar,ps32]
gpg_configure_signal_read_list_append.restype = s32
gpg_configure_api_call_arguments = dll.gpg_configure_api_call_arguments
#arg[0] AModuleId : None
#arg[1] AActionId : None
#arg[2] AAPIType : None
#arg[3] AAPIName : None
#arg[4] AAPIArgTypes : None
#arg[5] AAPIArgNames : None
#arg[6] AAPIArgExprs : None
#arg[7] AArraySize : None
gpg_configure_api_call_arguments.argtypes =[s64,s64,s32,pchar,s32,pchar,pchar,s32]
gpg_configure_api_call_arguments.restype = s32
gpg_configure_api_call_result = dll.gpg_configure_api_call_result
#arg[0] AModuleId : None
#arg[1] AActionId : None
#arg[2] AIgnoreResult : None
#arg[3] ASignalType : None
#arg[4] ASignalExpr : None
gpg_configure_api_call_result.argtypes =[s64,s64,c_bool,s32,pchar]
gpg_configure_api_call_result.restype = s32
gpg_configure_expression = dll.gpg_configure_expression
#arg[0] AModuleId : None
#arg[1] AActionId : None
#arg[2] AxCount : None
#arg[3] AExpression : None
#arg[4] AArgumentTypes : None
#arg[5] AArgumentExprs : None
#arg[6] AResultType : None
#arg[7] AResultExpr : None
gpg_configure_expression.argtypes =[s64,s64,s32,pchar,ps32,ppchar,s32,pchar]
gpg_configure_expression.restype = s32
gpg_add_local_var = dll.gpg_add_local_var
#arg[0] AModuleId : None
#arg[1] AType : None
#arg[2] AName : None
#arg[3] AInitValue : None
#arg[4] AComment : None
#arg[5] AItemIndex : None
gpg_add_local_var.argtypes =[s64,s32,pchar,pchar,pchar,ps32]
gpg_add_local_var.restype = s32
gpg_delete_local_var = dll.gpg_delete_local_var
#arg[0] AModuleId : None
#arg[1] AItemIndex : None
gpg_delete_local_var.argtypes =[s64,ps32]
gpg_delete_local_var.restype = s32
gpg_delete_all_local_vars = dll.gpg_delete_all_local_vars
#arg[0] AModuleId : None
gpg_delete_all_local_vars.argtypes =[s64]
gpg_delete_all_local_vars.restype = s32
gpg_delete_group_items = dll.gpg_delete_group_items
#arg[0] AModuleId : None
#arg[1] AGroupId : None
gpg_delete_group_items.argtypes =[s64,s64]
gpg_delete_group_items.restype = s32
gpg_configure_signal_read_write_list_delete = dll.gpg_configure_signal_read_write_list_delete
#arg[0] AModuleId : None
#arg[1] AActionId : None
#arg[2] AItemIndex : None
gpg_configure_signal_read_write_list_delete.argtypes =[s64,s64,s32]
gpg_configure_signal_read_write_list_delete.restype = s32
flexray_rbs_update_frame_by_header = dll.flexray_rbs_update_frame_by_header
#arg[0] AFlexRay : None
flexray_rbs_update_frame_by_header.argtypes =[PLIBFlexRay]
flexray_rbs_update_frame_by_header.restype = s32
gpg_configure_module = dll.gpg_configure_module
#arg[0] AModuleId : None
#arg[1] AProgramName : None
#arg[2] ADisplayName : None
#arg[3] ARepeatCount : None
#arg[4] ASelected : None
gpg_configure_module.argtypes =[s64,pchar,pchar,s32,c_bool]
gpg_configure_module.restype = s32
add_path_to_environment = dll.add_path_to_environment
#arg[0] APath : None
add_path_to_environment.argtypes =[pchar]
add_path_to_environment.restype = s32
delete_path_from_environment = dll.delete_path_from_environment
#arg[0] APath : None
delete_path_from_environment.argtypes =[pchar]
delete_path_from_environment.restype = s32
set_system_var_double_w_time = dll.set_system_var_double_w_time
#arg[0] ACompleteName : None
#arg[1] AValue : None
#arg[2] ATimeUs : None
set_system_var_double_w_time.argtypes =[pchar,double,s64]
set_system_var_double_w_time.restype = s32
set_system_var_int32_w_time = dll.set_system_var_int32_w_time
#arg[0] ACompleteName : None
#arg[1] AValue : None
#arg[2] ATimeUs : None
set_system_var_int32_w_time.argtypes =[pchar,s32,s64]
set_system_var_int32_w_time.restype = s32
set_system_var_uint32_w_time = dll.set_system_var_uint32_w_time
#arg[0] ACompleteName : None
#arg[1] AValue : None
#arg[2] ATimeUs : None
set_system_var_uint32_w_time.argtypes =[pchar,u32,s64]
set_system_var_uint32_w_time.restype = s32
set_system_var_int64_w_time = dll.set_system_var_int64_w_time
#arg[0] ACompleteName : None
#arg[1] AValue : None
#arg[2] ATimeUs : None
set_system_var_int64_w_time.argtypes =[pchar,s64,s64]
set_system_var_int64_w_time.restype = s32
set_system_var_uint64_w_time = dll.set_system_var_uint64_w_time
#arg[0] ACompleteName : None
#arg[1] AValue : None
#arg[2] ATimeUs : None
set_system_var_uint64_w_time.argtypes =[pchar,u64,s64]
set_system_var_uint64_w_time.restype = s32
set_system_var_uint8_array_w_time = dll.set_system_var_uint8_array_w_time
#arg[0] ACompleteName : None
#arg[1] ACount : None
#arg[2] AValue : None
#arg[3] ATimeUs : None
set_system_var_uint8_array_w_time.argtypes =[pchar,s32,pu8,s64]
set_system_var_uint8_array_w_time.restype = s32
set_system_var_int32_array_w_time = dll.set_system_var_int32_array_w_time
#arg[0] ACompleteName : None
#arg[1] ACount : None
#arg[2] AValue : None
#arg[3] ATimeUs : None
set_system_var_int32_array_w_time.argtypes =[pchar,s32,ps32,s64]
set_system_var_int32_array_w_time.restype = s32
set_system_var_double_array_w_time = dll.set_system_var_double_array_w_time
#arg[0] ACompleteName : None
#arg[1] ACount : None
#arg[2] AValue : None
#arg[3] ATimeUs : None
set_system_var_double_array_w_time.argtypes =[pchar,s32,pdouble,s64]
set_system_var_double_array_w_time.restype = s32
set_system_var_string_w_time = dll.set_system_var_string_w_time
#arg[0] ACompleteName : None
#arg[1] AValue : None
#arg[2] ATimeUs : None
set_system_var_string_w_time.argtypes =[pchar,pchar,s64]
set_system_var_string_w_time.restype = s32
set_system_var_generic_w_time = dll.set_system_var_generic_w_time
#arg[0] ACompleteName : None
#arg[1] AValue : None
#arg[2] ATimeUs : None
set_system_var_generic_w_time.argtypes =[pchar,pchar,s64]
set_system_var_generic_w_time.restype = s32
set_system_var_double_async_w_time = dll.set_system_var_double_async_w_time
#arg[0] ACompleteName : None
#arg[1] AValue : None
#arg[2] ATimeUs : None
set_system_var_double_async_w_time.argtypes =[pchar,double,s64]
set_system_var_double_async_w_time.restype = s32
set_system_var_int32_async_w_time = dll.set_system_var_int32_async_w_time
#arg[0] ACompleteName : None
#arg[1] AValue : None
#arg[2] ATimeUs : None
set_system_var_int32_async_w_time.argtypes =[pchar,s32,s64]
set_system_var_int32_async_w_time.restype = s32
set_system_var_uint32_async_w_time = dll.set_system_var_uint32_async_w_time
#arg[0] ACompleteName : None
#arg[1] AValue : None
#arg[2] ATimeUs : None
set_system_var_uint32_async_w_time.argtypes =[pchar,u32,s64]
set_system_var_uint32_async_w_time.restype = s32
set_system_var_int64_async_w_time = dll.set_system_var_int64_async_w_time
#arg[0] ACompleteName : None
#arg[1] AValue : None
#arg[2] ATimeUs : None
set_system_var_int64_async_w_time.argtypes =[pchar,s64,s64]
set_system_var_int64_async_w_time.restype = s32
set_system_var_uint64_async_w_time = dll.set_system_var_uint64_async_w_time
#arg[0] ACompleteName : None
#arg[1] AValue : None
#arg[2] ATimeUs : None
set_system_var_uint64_async_w_time.argtypes =[pchar,u64,s64]
set_system_var_uint64_async_w_time.restype = s32
set_system_var_uint8_array_async_w_time = dll.set_system_var_uint8_array_async_w_time
#arg[0] ACompleteName : None
#arg[1] ACount : None
#arg[2] AValue : None
#arg[3] ATimeUs : None
set_system_var_uint8_array_async_w_time.argtypes =[pchar,s32,pu8,s64]
set_system_var_uint8_array_async_w_time.restype = s32
set_system_var_int32_array_async_w_time = dll.set_system_var_int32_array_async_w_time
#arg[0] ACompleteName : None
#arg[1] ACount : None
#arg[2] AValue : None
#arg[3] ATimeUs : None
set_system_var_int32_array_async_w_time.argtypes =[pchar,s32,ps32,s64]
set_system_var_int32_array_async_w_time.restype = s32
set_system_var_int64_array_async_w_time = dll.set_system_var_int64_array_async_w_time
#arg[0] ACompleteName : None
#arg[1] ACount : None
#arg[2] AValue : None
#arg[3] ATimeUs : None
set_system_var_int64_array_async_w_time.argtypes =[pchar,s32,ps64,s64]
set_system_var_int64_array_async_w_time.restype = s32
set_system_var_double_array_async_w_time = dll.set_system_var_double_array_async_w_time
#arg[0] ACompleteName : None
#arg[1] ACount : None
#arg[2] AValue : None
#arg[3] ATimeUs : None
set_system_var_double_array_async_w_time.argtypes =[pchar,s32,pdouble,s64]
set_system_var_double_array_async_w_time.restype = s32
set_system_var_string_async_w_time = dll.set_system_var_string_async_w_time
#arg[0] ACompleteName : None
#arg[1] AValue : None
#arg[2] ATimeUs : None
set_system_var_string_async_w_time.argtypes =[pchar,pchar,s64]
set_system_var_string_async_w_time.restype = s32
set_system_var_generic_async_w_time = dll.set_system_var_generic_async_w_time
#arg[0] ACompleteName : None
#arg[1] AValue : None
#arg[2] ATimeUs : None
set_system_var_generic_async_w_time.argtypes =[pchar,pchar,s64]
set_system_var_generic_async_w_time.restype = s32
db_get_signal_startbit_by_pdu_offset = dll.db_get_signal_startbit_by_pdu_offset
#arg[0] ASignalStartBitInPDU : None
#arg[1] ASignalBitLength : None
#arg[2] AIsSignalIntel : None
#arg[3] AIsPDUIntel : None
#arg[4] APDUStartBit : None
#arg[5] APDUBitLength : None
#arg[6] AActualStartBit : None
db_get_signal_startbit_by_pdu_offset.argtypes =[s32,s32,c_bool,c_bool,s32,s32,ps32]
db_get_signal_startbit_by_pdu_offset.restype = s32
ui_show_save_file_dialog = dll.ui_show_save_file_dialog
#arg[0] ATitle : None
#arg[1] AFileTypeDesc : None
#arg[2] AFilter : None
#arg[3] ASuggestFileName : None
#arg[4] ADestinationFileName : None
ui_show_save_file_dialog.argtypes =[pchar,pchar,pchar,pchar,ppchar]
ui_show_save_file_dialog.restype = s32
ui_show_open_file_dialog = dll.ui_show_open_file_dialog
#arg[0] ATitle : None
#arg[1] AFileTypeDesc : None
#arg[2] AFilter : None
#arg[3] ASuggestFileName : None
#arg[4] ADestinationFileName : None
ui_show_open_file_dialog.argtypes =[pchar,pchar,pchar,pchar,ppchar]
ui_show_open_file_dialog.restype = s32
ui_show_select_directory_dialog = dll.ui_show_select_directory_dialog
#arg[0] ADestinationFileName : None
ui_show_select_directory_dialog.argtypes =[ppchar]
ui_show_select_directory_dialog.restype = s32
tsapp_transmit_ethernet_async = dll.tsapp_transmit_ethernet_async
#arg[0] AEthernetHeader : None
tsapp_transmit_ethernet_async.argtypes =[PLIBEthernetHeader]
tsapp_transmit_ethernet_async.restype = s32
tsapp_transmit_ethernet_sync = dll.tsapp_transmit_ethernet_sync
#arg[0] AEthernetHeader : None
#arg[1] ATimeoutMs : None
tsapp_transmit_ethernet_sync.argtypes =[PLIBEthernetHeader,s32]
tsapp_transmit_ethernet_sync.restype = s32
inject_ethernet_frame = dll.inject_ethernet_frame
#arg[0] AEthernetHeader : None
inject_ethernet_frame.argtypes =[PLIBEthernetHeader]
inject_ethernet_frame.restype = s32
tslog_blf_write_ethernet = dll.tslog_blf_write_ethernet
#arg[0] AHandle : None
#arg[1] AEthernetHeader : None
tslog_blf_write_ethernet.argtypes =[s32,PLIBEthernetHeader]
tslog_blf_write_ethernet.restype = s32
set_ethernet_channel_count = dll.set_ethernet_channel_count
#arg[0] ACount : None
set_ethernet_channel_count.argtypes =[s32]
set_ethernet_channel_count.restype = s32
get_ethernet_channel_count = dll.get_ethernet_channel_count
#arg[0] ACount : None
get_ethernet_channel_count.argtypes =[ps32]
get_ethernet_channel_count.restype = s32
transmit_ethernet_async_wo_pretx = dll.transmit_ethernet_async_wo_pretx
#arg[0] AEthernetHeader : None
transmit_ethernet_async_wo_pretx.argtypes =[PLIBEthernetHeader]
transmit_ethernet_async_wo_pretx.restype = s32
db_get_can_db_index_by_id = dll.db_get_can_db_index_by_id
#arg[0] AId : None
#arg[1] AIndex : None
db_get_can_db_index_by_id.argtypes =[s32,ps32]
db_get_can_db_index_by_id.restype = s32
db_get_lin_db_index_by_id = dll.db_get_lin_db_index_by_id
#arg[0] AId : None
#arg[1] AIndex : None
db_get_lin_db_index_by_id.argtypes =[s32,ps32]
db_get_lin_db_index_by_id.restype = s32
db_get_flexray_db_index_by_id = dll.db_get_flexray_db_index_by_id
#arg[0] AId : None
#arg[1] AIndex : None
db_get_flexray_db_index_by_id.argtypes =[s32,ps32]
db_get_flexray_db_index_by_id.restype = s32
eth_build_ipv4_udp_packet = dll.eth_build_ipv4_udp_packet
#arg[0] AHeader : None
#arg[1] ASrcIp : None
#arg[2] ADstIp : None
#arg[3] ASrcPort : None
#arg[4] ADstPort : None
#arg[5] APayload : None
#arg[6] APayloadLength : None
#arg[7] AIdentification : None
#arg[8] AFragmentIndex : None
eth_build_ipv4_udp_packet.argtypes =[PLIBEthernetHeader,pu8,pu8,u16,u16,pu8,u16,ps32,ps32]
eth_build_ipv4_udp_packet.restype = s32
register_system_var_change_event = dll.register_system_var_change_event
#arg[0] ACompleteName : None
#arg[1] AEvent : None
register_system_var_change_event.argtypes =[pchar,TLIBOnSysVarChange]
register_system_var_change_event.restype = s32
unregister_system_var_change_event = dll.unregister_system_var_change_event
#arg[0] ACompleteName : None
#arg[1] AEvent : None
unregister_system_var_change_event.argtypes =[pchar,TLIBOnSysVarChange]
unregister_system_var_change_event.restype = s32
unregister_system_var_change_events = dll.unregister_system_var_change_events
#arg[0] AEvent : None
unregister_system_var_change_events.argtypes =[TLIBOnSysVarChange]
unregister_system_var_change_events.restype = s32
block_current_pretx = dll.block_current_pretx
block_current_pretx.argtypes =[]
block_current_pretx.restype = s32
call_system_api = dll.call_system_api
#arg[0] AAPIName : None
#arg[1] AArgCount : None
#arg[2] AArgCapacity : None
#arg[3] AArgs : None
call_system_api.argtypes =[pchar,s32,s32,ppchar]
call_system_api.restype = s32
call_library_api = dll.call_library_api
#arg[0] AAPIName : None
#arg[1] AArgCount : None
#arg[2] AArgCapacity : None
#arg[3] AArgs : None
call_library_api.argtypes =[pchar,s32,s32,ppchar]
call_library_api.restype = s32
eth_is_udp_packet = dll.eth_is_udp_packet
#arg[0] AHeader : None
#arg[1] AIdentification : None
#arg[2] AUDPPacketLength : None
#arg[3] AUDPDataOffset : None
#arg[4] AIsPacketEnded : None
eth_is_udp_packet.argtypes =[PLIBEthernetHeader,pu16,pu16,pu16,c_bool]
eth_is_udp_packet.restype = s32
eth_ip_calc_header_checksum = dll.eth_ip_calc_header_checksum
#arg[0] AHeader : None
#arg[1] AOverwriteChecksum : None
#arg[2] AChecksum : None
eth_ip_calc_header_checksum.argtypes =[PLIBEthernetHeader,c_bool,pu16]
eth_ip_calc_header_checksum.restype = s32
eth_udp_calc_checksum = dll.eth_udp_calc_checksum
#arg[0] AHeader : None
#arg[1] AUDPPayloadAddr : None
#arg[2] AUDPPayloadLength : None
#arg[3] AOverwriteChecksum : None
#arg[4] AChecksum : None
eth_udp_calc_checksum.argtypes =[PLIBEthernetHeader,pu8,u16,c_bool,pu16]
eth_udp_calc_checksum.restype = s32
eth_udp_calc_checksum_on_frame = dll.eth_udp_calc_checksum_on_frame
#arg[0] AHeader : None
#arg[1] AOverwriteChecksum : None
#arg[2] AChecksum : None
eth_udp_calc_checksum_on_frame.argtypes =[PLIBEthernetHeader,c_bool,pu16]
eth_udp_calc_checksum_on_frame.restype = s32
eth_log_ethernet_frame_data = dll.eth_log_ethernet_frame_data
#arg[0] AHeader : None
eth_log_ethernet_frame_data.argtypes =[PLIBEthernetHeader]
eth_log_ethernet_frame_data.restype = s32
signal_tester_clear_all = dll.signal_tester_clear_all
signal_tester_clear_all.argtypes =[]
signal_tester_clear_all.restype = s32
signal_tester_load_configuration = dll.signal_tester_load_configuration
#arg[0] AFilePath : None
signal_tester_load_configuration.argtypes =[pchar]
signal_tester_load_configuration.restype = s32
signal_tester_save_configuration = dll.signal_tester_save_configuration
#arg[0] AFilePath : None
signal_tester_save_configuration.argtypes =[pchar]
signal_tester_save_configuration.restype = s32
signal_tester_run_item_by_name = dll.signal_tester_run_item_by_name
#arg[0] AName : None
signal_tester_run_item_by_name.argtypes =[pchar]
signal_tester_run_item_by_name.restype = s32
signal_tester_stop_item_by_name = dll.signal_tester_stop_item_by_name
#arg[0] AName : None
signal_tester_stop_item_by_name.argtypes =[pchar]
signal_tester_stop_item_by_name.restype = s32
signal_tester_run_item_by_index = dll.signal_tester_run_item_by_index
#arg[0] AIndex : None
signal_tester_run_item_by_index.argtypes =[s32]
signal_tester_run_item_by_index.restype = s32
signal_tester_stop_item_by_index = dll.signal_tester_stop_item_by_index
#arg[0] AIndex : None
signal_tester_stop_item_by_index.argtypes =[s32]
signal_tester_stop_item_by_index.restype = s32
signal_tester_get_item_verdict_by_index = dll.signal_tester_get_item_verdict_by_index
#arg[0] AObj : None
#arg[1] AIndex : None
#arg[2] AIsPass : None
signal_tester_get_item_verdict_by_index.argtypes =[ps32,s32,pbool]
signal_tester_get_item_verdict_by_index.restype = s32
signal_tester_get_item_result_by_name = dll.signal_tester_get_item_result_by_name
#arg[0] AObj : None
#arg[1] AName : None
#arg[2] AIsPass : None
#arg[3] AEventTimeUs : None
#arg[4] ADescription : None
signal_tester_get_item_result_by_name.argtypes =[ps32,pchar,pbool,ps64,ppchar]
signal_tester_get_item_result_by_name.restype = s32
signal_tester_get_item_result_by_index = dll.signal_tester_get_item_result_by_index
#arg[0] AObj : None
#arg[1] AIndex : None
#arg[2] AIsPass : None
#arg[3] AEventTimeUs : None
#arg[4] ADescription : None
signal_tester_get_item_result_by_index.argtypes =[ps32,s32,pbool,ps64,ppchar]
signal_tester_get_item_result_by_index.restype = s32
signal_tester_get_item_verdict_by_name = dll.signal_tester_get_item_verdict_by_name
#arg[0] AObj : None
#arg[1] AName : None
#arg[2] AIsPass : None
signal_tester_get_item_verdict_by_name.argtypes =[ps32,pchar,pbool]
signal_tester_get_item_verdict_by_name.restype = s32
ini_read_string_wo_quotes = dll.ini_read_string_wo_quotes
#arg[0] AHandle : None
#arg[1] ASection : None
#arg[2] AKey : None
#arg[3] AValue : None
#arg[4] AValueCapacity : None
#arg[5] ADefault : None
ini_read_string_wo_quotes.argtypes =[s32,pchar,pchar,pchar,ps32,pchar]
ini_read_string_wo_quotes.restype = s32
signal_tester_check_statistics_by_index = dll.signal_tester_check_statistics_by_index
#arg[0] AObj : None
#arg[1] AIndex : None
#arg[2] AMin : None
#arg[3] AMax : None
#arg[4] APass : None
#arg[5] AResult : None
#arg[6] AResultRepr : None
signal_tester_check_statistics_by_index.argtypes =[ps32,s32,double,double,pbool,pdouble,ppchar]
signal_tester_check_statistics_by_index.restype = s32
signal_tester_check_statistics_by_name = dll.signal_tester_check_statistics_by_name
#arg[0] AObj : None
#arg[1] AItemName : None
#arg[2] AMin : None
#arg[3] AMax : None
#arg[4] APass : None
#arg[5] AResult : None
#arg[6] AResultRepr : None
signal_tester_check_statistics_by_name.argtypes =[ps32,pchar,double,double,pbool,pdouble,ppchar]
signal_tester_check_statistics_by_name.restype = s32
signal_tester_enable_item_by_index = dll.signal_tester_enable_item_by_index
#arg[0] AIndex : None
#arg[1] AEnable : None
signal_tester_enable_item_by_index.argtypes =[s32,c_bool]
signal_tester_enable_item_by_index.restype = s32
signal_tester_enable_item_by_name = dll.signal_tester_enable_item_by_name
#arg[0] AItemName : None
#arg[1] AEnable : None
signal_tester_enable_item_by_name.argtypes =[pchar,c_bool]
signal_tester_enable_item_by_name.restype = s32
signal_tester_run_all = dll.signal_tester_run_all
signal_tester_run_all.argtypes =[]
signal_tester_run_all.restype = s32
signal_tester_stop_all = dll.signal_tester_stop_all
signal_tester_stop_all.argtypes =[]
signal_tester_stop_all.restype = s32
tslin_clear_schedule_tables = dll.tslin_clear_schedule_tables
#arg[0] AChnIdx : None
tslin_clear_schedule_tables.argtypes =[s32]
tslin_clear_schedule_tables.restype = s32
finalize_lib_tsmaster = dll.finalize_lib_tsmaster
finalize_lib_tsmaster.argtypes =[]
finalize_lib_tsmaster.restype = None
tssocket_htons = dll.tssocket_htons
#arg[0] x : None
tssocket_htons.argtypes =[s32]
tssocket_htons.restype = u16
tssocket_htonl = dll.tssocket_htonl
#arg[0] x : None
tssocket_htonl.argtypes =[s32]
tssocket_htonl.restype = u16
tssocket_aton = dll.tssocket_aton
#arg[0] cp : None
#arg[1] addr : None
tssocket_aton.argtypes =[pchar,Pip4_addr_t]
tssocket_aton.restype = None
tssocket_ntoa = dll.tssocket_ntoa
#arg[0] addr : None
tssocket_ntoa.argtypes =[Pip4_addr_t]
tssocket_ntoa.restype = pchar
tssocket_aton6 = dll.tssocket_aton6
#arg[0] addr : None
tssocket_aton6.argtypes =[Pip6_addr_t]
tssocket_aton6.restype = pchar
tssocket_ntoa6 = dll.tssocket_ntoa6
#arg[0] addr : None
tssocket_ntoa6.argtypes =[Pip6_addr_t]
tssocket_ntoa6.restype = pchar
tssocket_initialize = dll.tssocket_initialize
#arg[0] ANetworkIndex : None
#arg[1] ALog : None
tssocket_initialize.argtypes =[s32,TLogDebuggingInfo]
tssocket_initialize.restype = s32
tssocket_finalize = dll.tssocket_finalize
#arg[0] ANetworkIndex : None
tssocket_finalize.argtypes =[s32]
tssocket_finalize.restype = s32
tssocket_add_device = dll.tssocket_add_device
#arg[0] ANetworkIndex : None
#arg[1] macaddr : None
#arg[2] ipaddr : None
#arg[3] netmask : None
#arg[4] gateway : None
#arg[5] mtu : None
tssocket_add_device.argtypes =[s32,pu8,Tip4_addr_t,Tip4_addr_t,Tip4_addr_t,u16]
tssocket_add_device.restype = s32
tssocket_remove_device = dll.tssocket_remove_device
#arg[0] ANetworkIndex : None
#arg[1] macaddr : None
#arg[2] ipaddr : None
tssocket_remove_device.argtypes =[s32,pu8,Pip4_addr_t]
tssocket_remove_device.restype = s32
tssocket_dhcp_start = dll.tssocket_dhcp_start
#arg[0] ANetworkIndex : None
tssocket_dhcp_start.argtypes =[s32]
tssocket_dhcp_start.restype = s32
tssocket_dhcp_stop = dll.tssocket_dhcp_stop
#arg[0] ANetworkIndex : None
tssocket_dhcp_stop.argtypes =[s32]
tssocket_dhcp_stop.restype = s32
tssocket_accept = dll.tssocket_accept
#arg[0] ANetworkIndex : None
#arg[1] s : None
#arg[2] addr : None
#arg[3] addrlen : None
tssocket_accept.argtypes =[s32,s32,Pts_sockaddr,pu32]
tssocket_accept.restype = s32
tssocket_bind = dll.tssocket_bind
#arg[0] ANetworkIndex : None
#arg[1] s : None
#arg[2] name : None
#arg[3] namelen : None
tssocket_bind.argtypes =[s32,s32,Pts_sockaddr,u32]
tssocket_bind.restype = s32
tssocket_shutdown = dll.tssocket_shutdown
#arg[0] ANetworkIndex : None
#arg[1] s : None
#arg[2] how : None
tssocket_shutdown.argtypes =[s32,s32,s32]
tssocket_shutdown.restype = s32
tssocket_getpeername = dll.tssocket_getpeername
#arg[0] ANetworkIndex : None
#arg[1] s : None
#arg[2] name : None
#arg[3] namelen : None
tssocket_getpeername.argtypes =[s32,s32,Pts_sockaddr,u32]
tssocket_getpeername.restype = s32
tssocket_getsockname = dll.tssocket_getsockname
#arg[0] ANetworkIndex : None
#arg[1] s : None
#arg[2] name : None
#arg[3] namelen : None
tssocket_getsockname.argtypes =[s32,s32,Pts_sockaddr,u32]
tssocket_getsockname.restype = s32
tssocket_getsockopt = dll.tssocket_getsockopt
#arg[0] ANetworkIndex : None
#arg[1] s : None
#arg[2] level : None
#arg[3] optname : None
#arg[4] optval : None
#arg[5] optlen : None
tssocket_getsockopt.argtypes =[s32,s32,s32,s32,ps32,pu32]
tssocket_getsockopt.restype = s32
tssocket_setsockopt = dll.tssocket_setsockopt
#arg[0] ANetworkIndex : None
#arg[1] s : None
#arg[2] level : None
#arg[3] optname : None
#arg[4] optval : None
#arg[5] optlen : None
tssocket_setsockopt.argtypes =[s32,s32,s32,s32,ps32,u32]
tssocket_setsockopt.restype = s32
tssocket_close = dll.tssocket_close
#arg[0] ANetworkIndex : None
#arg[1] s : None
tssocket_close.argtypes =[s32,s32]
tssocket_close.restype = s32
tssocket_connect = dll.tssocket_connect
#arg[0] ANetworkIndex : None
#arg[1] s : None
#arg[2] name : None
#arg[3] namelen : None
tssocket_connect.argtypes =[s32,s32,Pts_sockaddr,u32]
tssocket_connect.restype = s32
tssocket_listen = dll.tssocket_listen
#arg[0] ANetworkIndex : None
#arg[1] s : None
#arg[2] backlog : None
tssocket_listen.argtypes =[s32,s32,s32]
tssocket_listen.restype = s32
tssocket_recv = dll.tssocket_recv
#arg[0] ANetworkIndex : None
#arg[1] s : None
#arg[2] mem : None
#arg[3] len : None
#arg[4] flags : None
tssocket_recv.argtypes =[s32,s32,pu8,size_t,s32]
tssocket_recv.restype = s32
tssocket_read = dll.tssocket_read
#arg[0] ANetworkIndex : None
#arg[1] s : None
#arg[2] mem : None
#arg[3] len : None
tssocket_read.argtypes =[s32,s32,pu8,size_t]
tssocket_read.restype = s32
tssocket_readv = dll.tssocket_readv
#arg[0] ANetworkIndex : None
#arg[1] s : None
#arg[2] iov : None
#arg[3] iovcnt : None
tssocket_readv.argtypes =[s32,s32,Pts_iovec,s32]
tssocket_readv.restype = s32
tssocket_recvfrom = dll.tssocket_recvfrom
#arg[0] ANetworkIndex : None
#arg[1] s : None
#arg[2] mem : None
#arg[3] len : None
#arg[4] flags : None
#arg[5] from : None
#arg[6] fromlen : None
tssocket_recvfrom.argtypes =[s32,s32,pu8,size_t,s32,Pts_sockaddr,pu32]
tssocket_recvfrom.restype = s32
tssocket_recvmsg = dll.tssocket_recvmsg
#arg[0] ANetworkIndex : None
#arg[1] s : None
#arg[2] Amessage : None
#arg[3] flags : None
tssocket_recvmsg.argtypes =[s32,s32,Pts_msghdr,s32]
tssocket_recvmsg.restype = s32
tssocket_send = dll.tssocket_send
#arg[0] ANetworkIndex : None
#arg[1] s : None
#arg[2] dataptr : None
#arg[3] size : None
#arg[4] flags : None
tssocket_send.argtypes =[s32,s32,pu8,size_t,s32]
tssocket_send.restype = s32
tssocket_sendto = dll.tssocket_sendto
#arg[0] ANetworkIndex : None
#arg[1] s : None
#arg[2] dataptr : None
#arg[3] size : None
#arg[4] flags : None
#arg[5] ato : None
#arg[6] tolen : None
tssocket_sendto.argtypes =[s32,s32,pu8,size_t,s32,Pts_sockaddr,u32]
tssocket_sendto.restype = s32
tssocket = dll.tssocket
#arg[0] ANetworkIndex : None
#arg[1] domain : None
#arg[2] atype : None
#arg[3] protocol : None
#arg[4] recv_cb : None
#arg[5] presend_cb : None
#arg[6] send_cb : None
tssocket.argtypes =[s32,s32,s32,s32,tosun_recv_callback,tosun_tcp_presend_callback,tosun_tcp_ack_callback]
tssocket.restype = s32
tssocket_write = dll.tssocket_write
#arg[0] ANetworkIndex : None
#arg[1] s : None
#arg[2] dataptr : None
#arg[3] size : None
tssocket_write.argtypes =[s32,s32,pu8,size_t]
tssocket_write.restype = s32
tssocket_writev = dll.tssocket_writev
#arg[0] ANetworkIndex : None
#arg[1] s : None
#arg[2] iov : None
#arg[3] iovcnt : None
tssocket_writev.argtypes =[s32,s32,Pts_iovec,s32]
tssocket_writev.restype = s32
tssocket_select = dll.tssocket_select
#arg[0] ANetworkIndex : None
#arg[1] maxfdp1 : None
#arg[2] readset : None
#arg[3] writeset : None
#arg[4] exceptset : None
#arg[5] timeout : None
tssocket_select.argtypes =[s32,s32,Pts_fd_set,Pts_fd_set,Pts_fd_set,Pts_timeval]
tssocket_select.restype = s32
tssocket_poll = dll.tssocket_poll
#arg[0] ANetworkIndex : None
#arg[1] fds : None
#arg[2] nfds : None
#arg[3] timeout : None
tssocket_poll.argtypes =[s32,Pts_pollfd,u32,s32]
tssocket_poll.restype = s32
tssocket_ioctl = dll.tssocket_ioctl
#arg[0] ANetworkIndex : None
#arg[1] s : None
#arg[2] cmd : None
#arg[3] argp : None
tssocket_ioctl.argtypes =[s32,s32,s32,ps32]
tssocket_ioctl.restype = s32
tssocket_fcntl = dll.tssocket_fcntl
#arg[0] ANetworkIndex : None
#arg[1] s : None
#arg[2] cmd : None
#arg[3] val : None
tssocket_fcntl.argtypes =[s32,s32,s32,s32]
tssocket_fcntl.restype = s32
tssocket_inet_ntop = dll.tssocket_inet_ntop
#arg[0] ANetworkIndex : None
#arg[1] af : None
#arg[2] src : None
#arg[3] dst : None
#arg[4] size : None
tssocket_inet_ntop.argtypes =[s32,s32,ps32,pchar,u32]
tssocket_inet_ntop.restype = s32
tssocket_inet_pton = dll.tssocket_inet_pton
#arg[0] ANetworkIndex : None
#arg[1] af : None
#arg[2] src : None
#arg[3] dst : None
tssocket_inet_pton.argtypes =[s32,s32,ps32,pchar]
tssocket_inet_pton.restype = s32
tssocket_ping4 = dll.tssocket_ping4
#arg[0] ANetworkIndex : None
#arg[1] ping_addr : None
#arg[2] repeat : None
#arg[3] interval_ms : None
#arg[4] timeout_ms : None
tssocket_ping4.argtypes =[s32,Pip4_addr_t,s32,u32,u32]
tssocket_ping4.restype = None
tssocket_ping6 = dll.tssocket_ping6
#arg[0] ANetworkIndex : None
#arg[1] ping_addr : None
#arg[2] repeat : None
#arg[3] interval_ms : None
#arg[4] timeout_ms : None
tssocket_ping6.argtypes =[s32,Pip6_addr_t,s32,u32,u32]
tssocket_ping6.restype = None
