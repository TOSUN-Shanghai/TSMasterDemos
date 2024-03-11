'''
Author: seven 865762826@qq.com
Date: 2023-03-06 16:36:32
LastEditors: seven 865762826@qq.com
LastEditTime: 2023-11-23 16:08:41
github:https://github.com/sy950915/TSMasterAPI.git
''' 
from ctypes import *
from . import TSAPI as dll
from .TSEnum import *



# 释放
def finalize_lib_tsmaster():
    dll.finalize_lib_tsmaster()


#  TSMasterAPI必须先调用该初始化函数，才可进行后续操作
def initialize_lib_tsmaster(AppName: bytes):
    return dll.initialize_lib_tsmaster(AppName)

#加载TSMaster工程进行初始化
#AppName: 应用程序名称,必须为utf-8或者b''
#projectfile:工程路径,必须为utf-8或者b''
def initialize_lib_tsmaster_with_project(AppName:bytes,projectfile:bytes):
    '''
    示例:initialize_lib_tsmaster_with_project(b'TSMaster',b'D:/TSMaster/TSMaster_Test)
    '''
    return dll.initialize_lib_tsmaster_with_project(AppName,projectfile)

#获取当前应用程序名称
def tsapp_get_current_application():
    AppName = POINTER(POINTER(c_char))()
    ret = dll.tsapp_get_current_application(byref(AppName))
    if ret ==0:
        return string_at(AppName)
    return tsapp_get_error_description(ret)

#设置当前应用程序名称
#AppName: 应用程序名称,必须为utf-8或者b''
def tsapp_set_current_application(AppName:bytes):
    '''
    示例:tsapp_set_current_application(b'TSMaster')
    '''
    return dll.tsapp_set_current_application(AppName)

# 设置can通道数
def tsapp_set_can_channel_count(count: c_int32):
    '''
    示例:tsapp_set_can_channel_count(c_int32(2))
    '''
    r = dll.tsapp_set_can_channel_count(count)
    return r


# 获取can通道数
def tsapp_get_can_channel_count(count: c_int32):
    '''
    示例:
    count = c_int32(0)
    tsapp_get_can_channel_count(count)
    print(count)
    '''
    r = dll.tsapp_get_can_channel_count(count)
    return r


# 设置lin通道数
def tsapp_set_lin_channel_count(count: c_int32):
    '''
    示例:tsapp_set_lin_channel_count(c_int32(2))
    '''
    r = dll.tsapp_set_lin_channel_count(count)
    return r


# 获取lin通道数
def tsapp_get_lin_channel_count(count: c_int32):
    '''
    示例:
    count = c_int32(0)
    tsapp_get_lin_channel_count(count)
    print(count)
    '''
    r = dll.tsapp_get_lin_channel_count(count)
    return r


# 按需创建通道映射
def tsapp_set_mapping(mapping: dll.TLIBTSMapping):
    """
    Amapping = dll.TLIBTSMapping()
    Amapping.FAppName = APPName
    Amapping.FAppChannelType = TLIBApplicationChannelType.APP_CAN
    Amapping.FHWDeviceName  = b"TC1016"
    Amapping.FAppChannelIndex = 0
    Amapping.FHWDeviceType = TLIBBusToolDeviceType.TS_USB_DEVICE //TOSUN HW
    Amapping.FHWDeviceSubType = TLIB_TS_Device_Sub_Type.TC1016
    Amapping.FHWIndex = 0
    Amapping.FHWChannelIndex = 0
    Amapping.FMappingDisabled = False
    tsapp_set_mapping(Amapping)
    """
    r = dll.tsapp_set_mapping(byref(mapping))
    return r


def tsapp_set_mapping_verbose(AppName: bytes, ALIBApplicationChannelType: TLIBApplicationChannelType, CHNIdx: c_int32,HW_name: str,BusToolDeviceType: c_int32, HW_Type: c_int32,HW_IDX:c_int32 ,AHardwareChannel: c_int32,AEnableMapping: c_bool):
    """
    tsapp_set_mapping_verbose(AppName, TLIBApplicationChannelType.APP_CAN, 0,
                                      "TC1016".encode("UTF8"), TLIBBusToolDeviceType.TS_USB_DEVICE,
                                      TLIB_TS_Device_Sub_Type.TC1016, 0, True):
    """
    r = dll.tsapp_set_mapping_verbose(AppName, ALIBApplicationChannelType, CHNIdx, HW_name, BusToolDeviceType, HW_Type, HW_IDX, AHardwareChannel, AEnableMapping)
    return r


# 删除硬件通道映射
def tsapp_del_mapping_verbose(AppName: bytes, ALIBApplicationChannelType: TLIBApplicationChannelType, APP_Channel: c_int32):
    """
    tsapp_del_mapping_verbose(AppName, TLIBApplicationChannelType.APP_CAN, 0):
    """
    r = dll.tsapp_del_mapping_verbose(AppName, ALIBApplicationChannelType, APP_Channel)
    return r


# 设置can通道参数 bps
def tsapp_configure_baudrate_can(APP_Channel: c_int32, ABaudrateKbps: c_float, AListenOnly: c_bool,
                                 AInstallTermResistor120Ohm: c_bool):
    """
    ABaudrateKbps = c_float(500)
    tsapp_configure_baudrate_can(0,ABaudrateKbps,False,True):
    """
    if isinstance(ABaudrateKbps,int) or isinstance(ABaudrateKbps,float):
        ABaudrateKbps = c_float(ABaudrateKbps)
    r = dll.tsapp_configure_baudrate_can(APP_Channel, ABaudrateKbps, AListenOnly, AInstallTermResistor120Ohm)
    return r


# 设置canfd通道波特率
def tsapp_configure_baudrate_canfd(AIdxChn: c_int32, ABaudrateArbKbps: c_float, ABaudrateDataKbps: c_float,AControllerType: c_int16, AControllerMode: c_int16,AInstallTermResistor120Ohm: c_bool):
    """
    tsapp_configure_baudrate_canfd(0, 500.0, 2000.0,dll.TLIBCANFDControllerType.lfdtISOCAN,dll.TLIBCANFDControllerMode.lfdmNormal, True)

    ABaudrateArbKbps = c_float(500)
    ABaudrateDataKbps = c_float(2000)
    tsapp_configure_baudrate_canfd(0, ABaudrateArbKbps, ABaudrateDataKbps,dll.TLIBCANFDControllerType.lfdtISOCAN,dll.TLIBCANFDControllerMode.lfdmNormal, True)
    """
    if isinstance(ABaudrateArbKbps,int) or isinstance(ABaudrateArbKbps,float):
        ABaudrateArbKbps = c_float(ABaudrateArbKbps)
    if isinstance(ABaudrateDataKbps,int) or isinstance(ABaudrateDataKbps,float):
        ABaudrateDataKbps = c_float(ABaudrateDataKbps)
    r = dll.tsapp_configure_baudrate_canfd(AIdxChn, ABaudrateArbKbps, ABaudrateDataKbps,AControllerType, AControllerMode, AInstallTermResistor120Ohm)
    return r


# can brs 采样率设置  AOnlyListen=0表示只听模式  A120大于0表示激活终端电阻，=0表示不激活
def tsapp_configure_can_regs(AIdxChn: c_int32, ABaudrateKbps: float, ASEG1: int, ASEG2: int, APrescaler: int,ASJ2: int, AOnlyListen: int, A120: int):
    """
    tsapp_configure_can_regs(0, 500.0,63,16,1,80,0,1)
    """
    if isinstance(ABaudrateKbps,int) or isinstance(ABaudrateKbps,float):
        ABaudrateKbps = c_float(ABaudrateKbps)
    if isinstance(ASEG1,int) or isinstance(ASEG1,float):
        ASEG1 = c_int32(ASEG1)
    if isinstance(ASEG2,int) or isinstance(ASEG2,float):
        ASEG2 = c_int32(ASEG2)
    if isinstance(APrescaler,int) or isinstance(APrescaler,float):
        APrescaler = c_int32(APrescaler)
    if isinstance(ASJ2,int) or isinstance(ASJ2,float):
        ASJ2 = c_int32(ASJ2)
    r = dll.tsapp_configure_can_regs(AIdxChn, c_float(ABaudrateKbps), c_int32(ASEG1), c_int32(ASEG2),
                                     c_int32(APrescaler), c_int32(ASJ2), AOnlyListen, A120)
    return r


# canfd brs 采样率设置
def tsapp_configure_canfd_regs(AIdxChn: c_int32, AArbBaudrateKbps: float, AArbSEG1: int, AArbSEG2: int,
                               AArbPrescaler: int,
                               AArbSJ2: int, ADataBaudrateKbps: float, ADataSEG1: int, ADataSEG2: int,
                               ADataPrescaler: int,
                               ADataSJ2: int, AControllerType: dll.TLIBCANFDControllerType,
                               AControllerMode: dll.TLIBCANFDControllerMode,
                               AInstallTermResistor120Ohm: int):
    """
    tsapp_configure_canfd_regs(0, 500.0,63,16,1,80,2000.0,15,4,1,20)
    """
    if isinstance(AArbBaudrateKbps,int) or isinstance(AArbBaudrateKbps,float):
        AArbBaudrateKbps = c_float(AArbBaudrateKbps)
    if isinstance(AArbSEG1,int) or isinstance(AArbSEG1,float):
        AArbSEG1 = c_int32(AArbSEG1)
    if isinstance(AArbSEG2,int) or isinstance(AArbSEG2,float):
        AArbSEG2 = c_int32(AArbSEG2)
    if isinstance(AArbPrescaler,int) or isinstance(AArbPrescaler,float):
        AArbPrescaler = c_int32(AArbPrescaler)
    if isinstance(AArbSJ2,int) or isinstance(AArbSJ2,float):
        AArbSJ2 = c_int32(AArbSJ2)
    if isinstance(ADataBaudrateKbps,int) or isinstance(ADataBaudrateKbps,float):
        ADataBaudrateKbps = c_float(ADataBaudrateKbps)
    if isinstance(ADataSEG1,int) or isinstance(ADataSEG1,float):
        ADataSEG1 = c_int32(ADataSEG1)
    if isinstance(ADataSEG2,int) or isinstance(ADataSEG2,float):
        ADataSEG2 = c_int32(ADataSEG2)
    if isinstance(ADataPrescaler,int) or isinstance(ADataPrescaler,float):
        ADataPrescaler = c_int32(ADataPrescaler)
    if isinstance(ADataSJ2,int) or isinstance(ADataSJ2,float):
        ADataSJ2 = c_int32(ADataSJ2)

    r = dll.tsapp_configure_canfd_regs(AIdxChn, c_float(AArbBaudrateKbps), c_int32(AArbSEG1), c_int32(AArbSEG2),
                                    c_int32(AArbPrescaler), c_int32(AArbSJ2),
                                    c_float(ADataBaudrateKbps), c_int32(ADataSEG1),
                                    c_int32(ADataSEG2), c_int32(ADataPrescaler), c_int32(ADataSJ2), AControllerType,
                                    AControllerMode,
                                    AInstallTermResistor120Ohm)
    return r


# 设置lin通道波特率
def tsapp_configure_baudrate_lin(AIdxChn: c_int32, ABaudrateKbps: int, TLINProtocol: TLINProtocol):
    """
    tsapp_configure_baudrate_lin(0,19.2,TLINProtocol.LINProtocol_13)
    """
    if isinstance(ABaudrateKbps,int) or isinstance(ABaudrateKbps,float):
        ABaudrateKbps = c_float(ABaudrateKbps)
    r = dll.tsapp_configure_baudrate_lin(AIdxChn, ABaudrateKbps, TLINProtocol)
    return r


# 设置LIN模式
def tslin_set_node_funtiontype(AIdxChn: c_int32, TLINNodeType: TLINNodeType):
    """
    tslin_set_node_funtiontype(0,TLINNodeType.T_MASTER_NODE) #主节点
    tslin_set_node_funtiontype(0,TLINNodeType.T_SLAVE_NODE)  #从节点
    """
    r = dll.tslin_set_node_functiontype(AIdxChn, TLINNodeType)
    return r


# 程序启动
def tsapp_connect():
    r = dll.tsapp_connect()
    return r


# 程序关闭
def tsapp_disconnect():
    r = dll.tsapp_disconnect()
    return r

# 增加应用程序
def tsapp_add_application(AppName: bytes):
    """
    tsapp_add_application(b'TSMaster1')
    """
    r = tsapp_add_application(AppName)
    return r


def tsapp_del_application(AppName: bytes):
    """
    tsapp_del_application(b'TSMaster1')
    """
    r = tsapp_del_application(AppName)
    return r


# 以APeriodMS为周期循环发送can报文
def tsapp_add_cyclic_msg_can(Msg: dll.TLIBCAN, APeriodMS: c_float):
    """
    ACAN = dll.TLIBCAN(FIdxChn=0, FDLC=8, FIdentifier=0x1, FProperties=1, FData=[1,2,3,4,5])
    tsapp_add_cyclic_msg_can(ACAN,100) #周期100ms发送
    """
    if isinstance(APeriodMS,int) or isinstance(APeriodMS,float):
        APeriodMS = c_float(APeriodMS)
    r = dll.tsapp_add_cyclic_msg_can(byref(Msg), APeriodMS)
    return r


# 删除循环发送can报文
def tsapp_del_cyclic_msg_can(Msg: dll.TLIBCAN):
    """
    ACAN = dll.TLIBCAN(FIdxChn=0, FDLC=8, FIdentifier=0x1, FProperties=1)
    tsapp_del_cyclic_msg_can(ACAN)
    """
    r = dll.tsapp_delete_cyclic_msg_can(byref(Msg))
    return r


# 以APeriodMS为周期循环发送canfd报文
def tsapp_add_cyclic_msg_canfd(Msg: dll.TLIBCANFD, APeriodMS: c_float):
    """
    ACANFD = dll.TLIBCANFD(FIdxChn=0, FDLC=8, FIdentifier=0x1, FProperties=1, FData=[1,2,3,4,5])
    tsapp_add_cyclic_msg_canfd(ACANFD,100) #周期100ms发送
    """
    if isinstance(APeriodMS,int) or isinstance(APeriodMS,float):
        APeriodMS = c_float(APeriodMS)
    r = dll.tsapp_add_cyclic_msg_canfd(byref(Msg), APeriodMS)
    return r


# 删除循环发送canfd报文
def tsapp_del_cyclic_msg_canfd(Msg: dll.TLIBCANFD):
    """
    ACANFD = dll.TLIBCANFD(FIdxChn=0, FDLC=8, FIdentifier=0x1, FProperties=1)
    tsapp_del_cyclic_msg_canfd(ACANFD)
    """
    r = dll.tsapp_delete_cyclic_msg_canfd(byref(Msg))
    return r


# 删除所有循环发送报文
def tsapp_delete_cyclic_msgs():
    r = dll.tsapp_delete_cyclic_msgs()
    return r


# 是否使能总线数据统计
def tsapp_enable_bus_statistics(AEnable: c_bool):
    """
    tsapp_enable_bus_statistics(True)
    """
    r = dll.tsapp_enable_bus_statistics(AEnable)
    return r

#获取hw devices数量
#参数必须为变量
def tsapp_enumerate_hw_devices(ACount: c_int32):
    """
        ACount  = c_int32(0)
        tsapp_enumerate_hw_devices(ACount)
        print(ACount)
    """
    if isinstance(ACount,int) or isinstance(ACount,float):
        ACount = c_int32(ACount)
    r = dll.tsapp_enumerate_hw_devices(byref(ACount))
    return r

# 获取硬件信息

def tsapp_get_hw_info_by_index(AIndex: int, PLIBHWInfo: dll.TLIBHWInfo):
    """
    ACount  = c_int32(0)
    tsapp_enumerate_hw_devices(ACount)
    print("在线硬件数量有%#d个" % (ACount.value - 1))
    PTLIBHWInfo = dll.TLIBHWInfo()
    for i in range(ACount.value):
        tsapp_get_hw_info_by_index(i, PTLIBHWInfo)
        print(PTLIBHWInfo.FDeviceType, PTLIBHWInfo.FDeviceIndex, PTLIBHWInfo.FVendorName.decode("utf8"),
              PTLIBHWInfo.FDeviceName.decode("utf8"),
              PTLIBHWInfo.FSerialString.decode("utf8"))
    """
    r = dll.tsapp_get_hw_info_by_index(c_int32(AIndex), byref(PLIBHWInfo))
    return r


# 错误信息描述
def tsapp_get_error_description(ACode: c_int32):
    """
    ret = tsapp_connect()
    if ret != 0:
        tsapp_get_error_description(ret)
    """
    if ACode == 0:
        return "确定"
    else:
        ret = c_char_p()
        r = dll.tsapp_get_error_description(c_int32(ACode), ret)
        if r == 0:
            ADesc = ret.value
            return ADesc
        else:
            return r

def tsapp_enable_bus_statistics(AEnable:bool):

    return dll.tsapp_enable_bus_statistics(AEnable)


def tsapp_clear_bus_statistics():
    return dll.tsapp_clear_bus_statistics()

#arg[0] ABusType : None
#arg[1] AIdxChn : None
#arg[2] AIdxStat : None
#arg[3] AStat : None
def tsapp_get_bus_statistics(ABusType:dll.TLIBApplicationChannelType,AIdxChn:dll.s32,AIdxStat:dll.TLIBCANBusStatistics,AStat:dll.pdouble):
    return dll.tsapp_get_bus_statistics(ABusType,AIdxChn,AIdxStat,AStat)

# 获取can每秒帧数，需要先使能总线统计
def tsapp_get_fps_can(AIdxChn: c_int32, AIdentifier: c_int32, AFPS: c_int32):
    """
    tsapp_enable_bus_statistics(True)
    AFPS = c_int32(0)
    tsapp_get_fps_can(0,0X123,AFPS)
    print(AFPS)
    """
    if isinstance(AIdentifier,int) or isinstance(AIdentifier,float):
        AIdentifier = c_int32(AIdentifier)
    if isinstance(AFPS,int) or isinstance(AFPS,float):
        AFPS = c_int32(AFPS)
    r = dll.tsapp_get_fps_can(AIdxChn, AIdentifier, byref(AFPS))
    return r


# 获取canfd每秒帧数，需要先使能总线统计
def tsapp_get_fps_canfd(AIdxChn: c_int32, AIdentifier: c_int32, AFPS: c_int32):
    """
    tsapp_enable_bus_statistics(True)
    AFPS = c_int32(0)
    tsapp_get_fps_canfd(0,0X123,AFPS)
    print(AFPS)
    """
    if isinstance(AIdentifier,int) or isinstance(AIdentifier,float):
        AIdentifier = c_int32(AIdentifier)
    if isinstance(AFPS,int) or isinstance(AFPS,float):
        AFPS = c_int32(AFPS)
    r = dll.tsapp_get_fps_canfd(AIdxChn, AIdentifier, byref(AFPS))
    return r


# 获取canfd每秒帧数，需要先使能总线统计
def tsapp_get_fps_lin(AIdxChn: c_int32, AIdentifier: c_int32, AFPS: c_int32):
    """
    tsapp_enable_bus_statistics(True)
    AFPS = c_int32(0)
    tsapp_get_fps_lin(0,0X123,AFPS)
    print(AFPS)
    """
    if isinstance(AIdentifier,int) or isinstance(AIdentifier,float):
        AIdentifier = c_int32(AIdentifier)
    if isinstance(AFPS,int) or isinstance(AFPS,float):
        AFPS = c_int32(AFPS)
    r = dll.tsapp_get_fps_lin(AIdxChn, AIdentifier, byref(AFPS))
    return r


# 获取硬件映射信息
def tsapp_get_mapping(AMapping: dll.TLIBTSMapping):
    """
    AMapping = dll.TLIBTSMapping()
    tsapp_get_mapping(AMapping)
    print(AMapping.FHWDeviceSubType)
    """
    r = dll.tsapp_get_mapping(byref(AMapping))
    return r


# # 获取详细硬件映射信息
# def tsapp_get_mapping_verbose(APPName: bytes, ApplicationChannelType: TLIBApplicationChannelType, AMapping: dll.TLIBTSMapping):
#     """
#     AMapping = dll.TLIBTSMapping()
#     tsapp_get_mapping_verbose("APPName",TLIBApplicationChannelType.APP_CAN,AMapping)
#     print(AMapping.FHWDeviceSubType)
#     """
#     r = dll.tsapp_get_mapping_verbose(APPName, ApplicationChannelType, byref(AMapping))
#     return r


# 获取时间戳
def tsapp_get_timestamp(ATimestamp: c_int32):
    """
    ATimestamp = c_int32(0)
    tsapp_get_timestamp(ATimestamp)
    """
    if isinstance(ATimestamp,int) or isinstance(ATimestamp,float):
        ATimestamp = c_int32(ATimestamp)
    r = dll.tsapp_get_timestamp(byref(ATimestamp))
    return r


# # 获取极速模式是否开启
# def tsapp_get_turbo_mode(AEnable: c_bool):
#     r = dll.tsapp_get_turbo_mode(byref(AEnable))
#     return r


# # 是否开启极速模式
# def tsapp_set_turbo_mode(AEnable: c_bool):
#     r = dll.tsapp_set_turbo_mode(AEnable)
#     return r


# 开启接受FIFO模式
def tsfifo_enable_receive_fifo():
    """
    tsfifo_receive_can_msgs
    tsfifo_receive_canfd_msgs
    tsfifo_receive_lin_msgs
    tsfifo_receive_flexray_msgs
    等函数使用,需先开启tsfifo_enable_receive_fifo()
    """
    dll.tsfifo_enable_receive_fifo()


# 关闭接受FIFO模式
def tsfifo_disable_receive_fifo():
    dll.tsfifo_disable_receive_fifo()


# # 关闭错误帧接受模式
# def tsfifo_disable_receive_error_frames():
#     dll.tsfifo_disable_receive_error_frames()


# 读取通道can缓冲帧数量
def tsfifo_read_can_buffer_frame_count(AIdxChn: c_int32, ACount: c_int32):
    """
    ACount = c_int32(0)
    tsfifo_read_can_buffer_frame_count(0,ACount)
    print(ACount)
    """
    if isinstance(ACount,int) or isinstance(ACount,float):
        ACount = c_int32(ACount)
    r = dll.tsfifo_read_can_buffer_frame_count(AIdxChn, byref(ACount))
    return r


# 读取通道can Tx数量
def tsfifo_read_can_tx_buffer_frame_count(AIdxChn: c_int32, ACount: c_int32):
    """
    ACount = c_int32(0)
    tsfifo_read_can_tx_buffer_frame_count(0,ACount)
    print(ACount)
    """
    if isinstance(ACount,int) or isinstance(ACount,float):
        ACount = c_int32(ACount)
    r = dll.tsfifo_read_can_tx_buffer_frame_count(AIdxChn, byref(ACount))
    return r


# 读取通道can Rx数量
def tsfifo_read_can_rx_buffer_frame_count(AIdxChn: c_int32, ACount: c_int32):
    """
    ACount = c_int32(0)
    tsfifo_read_can_rx_buffer_frame_count(0,ACount)
    print(ACount)
    """
    if isinstance(ACount,int) or isinstance(ACount,float):
        ACount = c_int32(ACount)
    r = dll.tsfifo_read_can_rx_buffer_frame_count(AIdxChn, byref(ACount))
    return r


# 读取通道canfd Tx数量
def tsfifo_read_canfd_tx_buffer_frame_count(AIdxChn: c_int32, ACount: c_int32):
    """
    ACount = c_int32(0)
    tsfifo_read_canfd_tx_buffer_frame_count(0,ACount)
    print(ACount)
    """
    if isinstance(ACount,int) or isinstance(ACount,float):
        ACount = c_int32(ACount)
    r = dll.tsfifo_read_canfd_tx_buffer_frame_count(AIdxChn, byref(ACount))
    return r


# 读取通道canfd Rx数量
def tsfifo_read_canfd_rx_buffer_frame_count(AIdxChn: c_int32, ACount: c_int32):
    """
    ACount = c_int32(0)
    tsfifo_read_canfd_rx_buffer_frame_count(0,ACount)
    print(ACount)
    """
    if isinstance(ACount,int) or isinstance(ACount,float):
        ACount = c_int32(ACount)
    r = dll.tsfifo_read_canfd_rx_buffer_frame_count(AIdxChn, byref(ACount))
    return r


# 读取通道fastlin缓冲帧数量
def tsfifo_read_fastlin_buffer_frame_count(AIdxChn: c_int32, ACount: c_int32):
    """
    ACount = c_int32(0)
    tsfifo_read_fastlin_buffer_frame_count(0,ACount)
    print(ACount)
    """
    if isinstance(ACount,int) or isinstance(ACount,float):
        ACount = c_int32(ACount)
    r = dll.tsfifo_read_fastlin_buffer_frame_count(AIdxChn, byref(ACount))
    return r


# 读取通道fastlin Tx数量
def tsfifo_read_fastlin_tx_buffer_frame_count(AIdxChn: c_int32, ACount: c_int32):
    """
    ACount = c_int32(0)
    tsfifo_read_fastlin_tx_buffer_frame_count(0,ACount)
    print(ACount)
    """
    if isinstance(ACount,int) or isinstance(ACount,float):
        ACount = c_int32(ACount)
    r = dll.tsfifo_read_fastlin_tx_buffer_frame_count(AIdxChn, byref(ACount))
    return r


# 读取通道fastlin Rx数量
def tsfifo_read_fastlin_rx_buffer_frame_count(AIdxChn: c_int32, ACount: c_int32):
    """
    ACount = c_int32(0)
    tsfifo_read_fastlin_rx_buffer_frame_count(0,ACount)
    print(ACount)
    """
    if isinstance(ACount,int) or isinstance(ACount,float):
        ACount = c_int32(ACount)
    r = dll.tsfifo_read_fastlin_rx_buffer_frame_count(AIdxChn, byref(ACount))
    return r


# 读取通道lin缓冲帧数量
def tsfifo_read_lin_buffer_frame_count(AIdxChn: c_int32, ACount: c_int32):
    """
    ACount = c_int32(0)
    tsfifo_read_lin_buffer_frame_count(0,ACount)
    print(ACount)
    """
    if isinstance(ACount,int) or isinstance(ACount,float):
        ACount = c_int32(ACount)
    r = dll.tsfifo_read_lin_buffer_frame_count(AIdxChn, byref(ACount))
    return r


# 读取通道lin Tx数量
def tsfifo_read_lin_tx_buffer_frame_count(AIdxChn: c_int32, ACount: c_int32):
    """
    ACount = c_int32(0)
    tsfifo_read_lin_tx_buffer_frame_count(0,ACount)
    print(ACount)
    """
    if isinstance(ACount,int) or isinstance(ACount,float):
        ACount = c_int32(ACount)
    r = dll.tsfifo_read_lin_tx_buffer_frame_count(AIdxChn, byref(ACount))
    return r


# 读取通道lin Rx数量
def tsfifo_read_lin_rx_buffer_frame_count(AIdxChn: c_int32, ACount: c_int32):
    """
    ACount = c_int32(0)
    tsfifo_read_lin_rx_buffer_frame_count(0,ACount)
    print(ACount)
    """
    if isinstance(ACount,int) or isinstance(ACount,float):
        ACount = c_int32(ACount)
    r = dll.tsfifo_read_lin_rx_buffer_frame_count(AIdxChn, byref(ACount))
    return r


# 清除 通道can_receive_buffers
def tsfifo_clear_can_receive_buffers(AIdxChn: c_int32):
    """
    tsfifo_clear_can_receive_buffers(0)
    """
    r = dll.tsfifo_clear_can_receive_buffers(AIdxChn)
    return r


# 清除 通道canfd_receive_buffers
def tsfifo_clear_canfd_receive_buffers(AIdxChn: c_int32):
    """
    tsfifo_clear_canfd_receive_buffers(0)
    """
    r = dll.tsfifo_clear_canfd_receive_buffers(AIdxChn)
    return r


# 清除 通道fastlin_receive_buffers
def tsfifo_clear_fastlin_receive_buffers(AIdxChn: c_int32):
    """
    tsfifo_clear_fastlin_receive_buffers(0)
    """
    r = dll.tsfifo_clear_fastlin_receive_buffers(AIdxChn)
    return r


# 清除 通道lin_receive_buffers
def tsfifo_clear_lin_receive_buffers(AIdxChn: c_int32):
    """
    tsfifo_clear_lin_receive_buffers(0)
    """
    r = dll.tsfifo_clear_lin_receive_buffers(AIdxChn)
    return r


# 注册canfd预发送事件
def tsapp_register_pretx_event_canfd(obj: c_int32, OnFUNC):
    """
    obj = c_int32(0)
    #对通道1的 id为0x111的报文 数据1进行自增
    def On_CANFD_EVENT(OBJ, ACAN):
        if (ACAN.contents.FIdentifier == 0x111 and ACAN.contents.FIdxChn == 0):
            ACAN.contents.FData[0] +=1
    OnCANFDevent = TCANFDQueueEvent_Win32(On_CANFD_EVENT)
    tsapp_register_pretx_event_canfd(obj,OnCANFDevent)
    """
    if isinstance(obj,int) or isinstance(obj,float):
        obj = c_int32(obj)
    r = dll.tsapp_register_pretx_event_canfd(byref(obj), OnFUNC)
    return r


# 注册can预发送事件
def tsapp_register_pretx_event_can(obj: c_int32, OnFUNC):
    """
    obj = c_int32(0)
    #对通道1的 id为0x111的报文 数据1进行自增
    def On_CAN_EVENT(OBJ, ACAN):
        if (ACAN.contents.FIdentifier == 0x111 and ACAN.contents.FIdxChn == 0):
            ACAN.contents.FData[0] +=1
    OnCANevent = TCANQueueEvent_Win32(On_CAN_EVENT)
    tsapp_register_pretx_event_can(obj,OnCANevent)
    """
    if isinstance(obj,int) or isinstance(obj,float):
        obj = c_int32(obj)
    r = dll.tsapp_register_pretx_event_can(byref(obj), OnFUNC)
    return r


# 注册lin预发送事件
def tsapp_register_pretx_event_lin(obj: c_int32, OnFUNC):
    """
    obj = c_int32(0)
    #对通道1的 id为0x11的报文 数据1进行自增
    def On_LIN_EVENT(OBJ, ACAN):
        if (ACAN.contents.FIdentifier == 0x11 and ACAN.contents.FIdxChn == 0):
            ACAN.contents.FData[0] +=1
    OnLINevent = TLINQueueEvent_Win32(On_LIN_EVENT)
    tsapp_register_pretx_event_lin(obj,OnLINevent)
    """
    if isinstance(obj,int) or isinstance(obj,float):
        obj = c_int32(obj)
    r = dll.tsapp_register_pretx_event_lin(byref(obj), OnFUNC)
    return r


# 注册canfd发送—接收事件
def tsapp_register_event_canfd(obj: c_int32, OnFUNC):
    """
    obj = c_int32(0)
    #对通道1的 id为0x11的报文 数据1进行打印输出
    def On_CANFD_EVENT(OBJ, ACAN):
        if (ACAN.contents.FIdentifier == 0x11 and ACAN.contents.FIdxChn == 0):
            print(ACAN.FData[0])
    OnCANFDevent = TCANFDQueueEvent_Win32(On_CANFD_EVENT)
    tsapp_register_event_canfd(obj,OnCANFDevent)
    """
    if isinstance(obj,int) or isinstance(obj,float):
        obj = c_int32(obj)
    r = dll.tsapp_register_event_canfd(byref(obj), OnFUNC)
    return r


# 注册can发送—接收事件
def tsapp_register_event_can(obj: c_int32, OnFUNC):
    """
    obj = c_int32(0)
    #对通道1的 id为0x11的报文 数据1进行打印输出
    def On_CAN_EVENT(OBJ, ACAN):
        if (ACAN.contents.FIdentifier == 0x11 and ACAN.contents.FIdxChn == 0):
            print(ACAN.FData[0])
    OnCANevent = TCANQueueEvent_Win32(On_CAN_EVENT)
    tsapp_register_event_can(obj,OnCANevent)
    """
    if isinstance(obj,int) or isinstance(obj,float):
        obj = c_int32(obj)
    r = dll.tsapp_register_event_can(byref(obj), OnFUNC)
    return r


# 注册lin发送—接收事件
def tsapp_register_event_lin(obj: c_int32, OnFUNC):
    """
    obj = c_int32(0)
    #对通道1的 id为0x11的报文 数据1进行打印输出
    def On_LIN_EVENT(OBJ, ACAN):
        if (ACAN.contents.FIdentifier == 0x11 and ACAN.contents.FIdxChn == 0):
            print(ACAN.FData[0])
    OnLINevent = TCANQueueEvent_Win32(On_LIN_EVENT)
    tsapp_register_event_lin(obj,OnLINevent)
    """
    if isinstance(obj,int) or isinstance(obj,float):
        obj = c_int32(obj)
    r = dll.tsapp_register_event_lin(byref(obj), OnFUNC)
    return r


# 注销canfd预发送事件
def tsapp_unregister_pretx_event_canfd(obj: c_int32, OnFUNC):
    """
    obj = c_int32(0)
    #对通道1的 id为0x11的报文 数据1进行打印输出
    def On_CANFD_EVENT(OBJ, ACAN):
        if (ACAN.contents.FIdentifier == 0x11 and ACAN.contents.FIdxChn == 0):
            print(ACAN.FData[0])
    OnCANFDevent = TCANFDQueueEvent_Win32(On_CANFD_EVENT)
    tsapp_unregister_pretx_event_canfd(obj,OnCANFDevent)
    """
    if isinstance(obj,int) or isinstance(obj,float):
        obj = c_int32(obj)
    r = dll.tsapp_unregister_pretx_event_canfd(byref(obj), OnFUNC)
    return r


# 注销can预发送事件
def tsapp_unregister_pretx_event_can(obj: c_int32, OnFUNC):
    """
    obj = c_int32(0)
    #对通道1的 id为0x11的报文 数据1进行打印输出
    def On_CAN_EVENT(OBJ, ACAN):
        if (ACAN.contents.FIdentifier == 0x11 and ACAN.contents.FIdxChn == 0):
            print(ACAN.FData[0])
    OnCANevent = TCANQueueEvent_Win32(On_CAN_EVENT)
    tsapp_unregister_pretx_event_can(obj,OnCANevent)
    """
    if isinstance(obj,int) or isinstance(obj,float):
        obj = c_int32(obj)
    r = dll.tsapp_unregister_pretx_event_can(byref(obj), OnFUNC)
    return r


# 注销lin预发送事件
def tsapp_unregister_pretx_event_lin(obj: c_int32, OnFUNC):
    """
    obj = c_int32(0)
    #对通道1的 id为0x11的报文 数据1进行打印输出
    def On_LIN_EVENT(OBJ, ACAN):
        if (ACAN.contents.FIdentifier == 0x11 and ACAN.contents.FIdxChn == 0):
            print(ACAN.FData[0])
    OnLINevent = TCANQueueEvent_Win32(On_LIN_EVENT)
    tsapp_unregister_pretx_event_lin(obj,OnLINevent)
    """
    if isinstance(obj,int) or isinstance(obj,float):
        obj = c_int32(obj)
    r = dll.tsapp_unregister_pretx_event_lin(byref(obj), OnFUNC)
    return r


# 注销canfd发送—接收事件
def tsapp_unregister_event_canfd(obj: c_int32, OnFUNC):
    """
    obj = c_int32(0)
    #对通道1的 id为0x11的报文 数据1进行打印输出
    def On_CANFD_EVENT(OBJ, ACAN):
        if (ACAN.contents.FIdentifier == 0x11 and ACAN.contents.FIdxChn == 0):
            print(ACAN.FData[0])
    OnCANFDevent = TCANFDQueueEvent_Win32(On_CANFD_EVENT)
    tsapp_unregister_event_canfd(obj,OnCANFDevent)
    """
    if isinstance(obj,int) or isinstance(obj,float):
        obj = c_int32(obj)
    r = dll.tsapp_unregister_event_canfd(byref(obj), OnFUNC)
    return r


# 注销can发送—接收事件
def tsapp_unregister_event_can(obj: c_int32, OnFUNC):
    """
    obj = c_int32(0)
    #对通道1的 id为0x11的报文 数据1进行打印输出
    def On_CAN_EVENT(OBJ, ACAN):
        if (ACAN.contents.FIdentifier == 0x11 and ACAN.contents.FIdxChn == 0):
            print(ACAN.FData[0])
    OnCANevent = TCANQueueEvent_Win32(On_CAN_EVENT)
    tsapp_unregister_event_can(obj,OnCANevent)
    """
    if isinstance(obj,int) or isinstance(obj,float):
        obj = c_int32(obj)
    r = dll.tsapp_unregister_event_can(byref(obj), OnFUNC)
    return r


# 注销lin发送—接收事件
def tsapp_unregister_event_lin(obj: c_int32, OnFUNC):
    """
    obj = c_int32(0)
    #对通道1的 id为0x11的报文 数据1进行打印输出
    def On_LIN_EVENT(OBJ, ACAN):
        if (ACAN.contents.FIdentifier == 0x11 and ACAN.contents.FIdxChn == 0):
            print(ACAN.FData[0])
    OnLINevent = TCANQueueEvent_Win32(On_LIN_EVENT)
    tsapp_unregister_pretx_event_lin(obj,OnLINevent)
    """
    if isinstance(obj,int) or isinstance(obj,float):
        obj = c_int32(obj)
    r = dll.tsapp_unregister_event_lin(byref(obj), OnFUNC)
    return r


# 注销canfd预发送事件
def tsapp_unregister_pretx_events_canfd(obj: c_int32):
    """
    obj = c_int32(0)
    tsapp_unregister_pretx_events_canfd(obj)
    """
    if isinstance(obj,int) or isinstance(obj,float):
        obj = c_int32(obj)
    r = dll.tsapp_unregister_pretx_events_canfd(byref(obj))
    return r


# 注销can预发送事件
def tsapp_unregister_pretx_events_can(obj: c_int32):
    """
    obj = c_int32(0)
    tsapp_unregister_pretx_events_can(obj)
    """
    if isinstance(obj,int) or isinstance(obj,float):
        obj = c_int32(obj)
    r = dll.tsapp_unregister_pretx_events_can(byref(obj))
    return r


# 注销lin预发送事件
def tsapp_unregister_pretx_events_lin(obj: c_int32):
    """
    obj = c_int32(0)
    tsapp_unregister_pretx_events_lin(obj)
    """
    if isinstance(obj,int) or isinstance(obj,float):
        obj = c_int32(obj)
    r = dll.tsapp_unregister_pretx_events_lin(byref(obj))
    return r


# 注销canfd发送—接收事件
def tsapp_unregister_events_canfd(obj: c_int32):
    """
    obj = c_int32(0)
    tsapp_unregister_events_canfd(obj)
    """
    if isinstance(obj,int) or isinstance(obj,float):
        obj = c_int32(obj)
    r = dll.tsapp_unregister_events_canfd(byref(obj))
    return r


# 注销can发送—接收事件
def tsapp_unregister_events_can(obj: c_int32):
    """
    obj = c_int32(0)
    tsapp_unregister_events_can(obj)
    """
    if isinstance(obj,int) or isinstance(obj,float):
        obj = c_int32(obj)
    r = dll.tsapp_unregister_events_can(byref(obj))
    return r


# 注销lin发送—接收事件
def tsapp_unregister_events_lin(obj: c_int32):
    """
    obj = c_int32(0)
    tsapp_unregister_events_lin(obj)
    """
    if isinstance(obj,int) or isinstance(obj,float):
        obj = c_int32(obj)
    r = dll.tsapp_unregister_events_lin(byref(obj))
    return r


# 注销预发送事件
def tsapp_unregister_pretx_events_all(obj: c_int32):
    """
    obj = c_int32(0)
    tsapp_unregister_pretx_events_all(obj)
    """
    if isinstance(obj,int) or isinstance(obj,float):
        obj = c_int32(obj)
    r = dll.tsapp_unregister_pretx_events_all(byref(obj))
    return r


# 注销发送—接收事件
def tsapp_unregister_events_all(obj: c_int32):
    """
    obj = c_int32(0)
    tsapp_unregister_events_all(obj)
    """
    if isinstance(obj,int) or isinstance(obj,float):
        obj = c_int32(obj)
    r = dll.tsapp_unregister_events_all(byref(obj))
    return r


# 打开TsMaster窗口
def tsapp_show_tsmaster_window(AWindowName: str,AWaitClose:bool):
    """
    tsapp_show_tsmaster_window(b"Hardware",false)
    """
    r = dll.tsapp_show_tsmaster_window(AWindowName, AWaitClose)
    return r


# 开始录制报文
def tsapp_start_logging(filename: str):
    """
    tsapp_start_logging(b"D:/1.blf")
    """
    r = dll.tsapp_start_logging(filename)
    return r


# 停止录制报文
def tsapp_stop_logging():
    """
    tsapp_stop_logging()
    """
    r = dll.tsapp_stop_logging()
    return r


# 异步发送单帧can报文
def tsapp_transmit_can_async(Msg: dll.TLIBCAN):
    """
    ACAN = dll.TLIBCAN(FIdxChn=0, FDLC=8, FIdentifier=0x1, FProperties=1, FData=[1,2,3,4,5,6])
    tsapp_transmit_can_async(ACAN)
    """
    r = dll.tsapp_transmit_can_async(byref(Msg))
    return r


# can fifo接收
#ACANBuffers：TLIBCAN数组
def tsfifo_receive_can_msgs(ACANBuffers: dll.TLIBCAN, ACANBufferSize: c_uint, AIdxChn: c_int32,
                           ARxTx: c_int32):
    """
    listcanmsg = (dll.TLIBCAN * 100)()

    listcanfdmsg = (dll.TLIBCANFD * 100)()

    cansize = c_int32(100)

    canfdsize = c_int32(100)

    tsfifo_receive_can_msgs(listcanmsg, cansize, 0, 1) #READ_TX_RX_DEF.TX_RX_MESSAGES

    tsfifo_receive_canfd_msgs(listcanfdmsg, canfdsize, 0,0) # READ_TX_RX_DEF.TX_RX_MESSAGES
    """
    return dll.tsfifo_receive_can_msgs(ACANBuffers, byref(ACANBufferSize), AIdxChn, ARxTx)



# # 发送头帧接收数据
# def tsapp_transmit_header_and_receive_msg(AIdxChn: c_int32, ID: int, FDlc: c_uint8, receivedMsg: dll.TLIBLIN,
#                                           Timeout: c_int):
#     r = dll.tsapp_transmit_header_and_receive_msg(AChn, ID, FDlc, byref(receivedMsg), c_int32(Timeout))
#     return r


# 异步发送单帧canfd报文
def tsapp_transmit_canfd_async(Msg: dll.TLIBCANFD):
    """
    ACANFD = dll.TLIBCANFD(FIdxChn=0, FDLC=8, FIdentifier=0x1, FProperties=1, FData=[1,2,3,4,5,6])
    tsapp_transmit_canfd_async(ACANFD)
    """
    r = dll.tsapp_transmit_canfd_async(byref(Msg))
    return r


# canfd报文接收
#ACANFDBuffers：dll.TLIBCANFD数组
def tsfifo_receive_canfd_msgs(ACANFDBuffers, ACANFDBufferSize: c_uint32, AIdxChn: c_int32,
                             ARxTx: c_int32):
    """
    listcanmsg = (dll.TLIBCAN * 100)()

    listcanfdmsg = (dll.TLIBCANFD * 100)()

    cansize = c_int32(100)

    canfdsize = c_int32(100)

    tsfifo_receive_can_msgs(listcanmsg, cansize, 0, 1) #READ_TX_RX_DEF.TX_RX_MESSAGES

    tsfifo_receive_canfd_msgs(listcanfdmsg, canfdsize, 0,0) # READ_TX_RX_DEF.TX_RX_MESSAGES
    """
    return dll.tsfifo_receive_canfd_msgs(ACANFDBuffers, byref(ACANFDBufferSize), AIdxChn, ARxTx)



# 异步发送单帧lin报文
def tsapp_transmit_lin_async(Msg: dll.TLIBLIN):
    """
    ACANFD = dll.TLIBCANFD(FIdxChn=0, FDLC=8, FIdentifier=0x1, FProperties=1, FData=[1,2,3,4,5,6])
    tsapp_transmit_lin_async(ACANFD)
    """
    r = dll.tsapp_transmit_lin_async(byref(Msg))
    return r


# lin报文接收
#ALINBuffers：dll.TLIBLIN数组
def tsapp_receive_lin_msgs(ALINBuffers, ALINBufferSize: c_int, AIdxChn: c_int32,
                           ARxTx: c_int32):
    """
    listlinmsg = (dll.TLIBLIN * 100)()
    linsize = c_int32(100)
    tsapp_receive_lin_msgs(listlinmsg, linsize, 0, 1) # READ_TX_RX_DEF.TX_RX_MESSAGES
    """
    r = dll.tsfifo_receive_lin_msgs(ALINBuffers, byref(ALINBufferSize), AIdxChn, ARxTx)

    return r


# def tsfifo_receive_fastlin_msgs(ALINBuffers: dll.TLIBLIN, ALINBufferSize: c_int, AIdxChn: c_int32,
#                                 ARxTx: READ_TX_RX_DEF):
#     temp = copy.copy(c_uint32(ALINBufferSize))
#     data = POINTER(dll.TLIBLIN * len(ALINBuffers))((dll.TLIBLIN * len(ALINBuffers))(*ALINBuffers))
#     r = dll.tsfifo_receive_fastlin_msgs(data, byref(temp), AChn, ARxTx)
#     for i in range(len(data.contents)):
#         ALINBuffers[i] = data.contents[i]
#     return r, temp


# 同步发送单帧can报文
def tsapp_transmit_can_sync(Msg: dll.TLIBCAN, ATimeoutMS: c_int32):
    """
    ACAN = dll.TLIBCAN(FIdxChn=0, FDLC=8, FIdentifier=0x1, FProperties=1, FData=[1,2,3,4,5,6])
    tsapp_transmit_can_sync(ACANFD)
    """
    r = dll.tsapp_transmit_can_sync(byref(Msg), ATimeoutMS)
    return r


# 同步发送单帧canfd报文
def tsapp_transmit_canfd_sync(Msg: dll.TLIBCANFD, ATimeoutMS: c_int32):
    """
    ACANFD = dll.TLIBCAN(FIdxChn=0, FDLC=8, FIdentifier=0x1, FProperties=1, FData=[1,2,3,4,5,6])
    tsapp_transmit_canfd_sync(ACANFD)
    """
    r = dll.tsapp_transmit_canfd_sync(byref(Msg), ATimeoutMS)
    return r


# 同步发送单帧lin报文
def tsapp_transmit_lin_sync(Msg: dll.TLIBLIN, ATimeoutMS: c_int32):
    """
    ALIN = dll.TLIBLIN(FIdxChn=0, FDLC=8, FIdentifier=0x1, FProperties=1, FData=[1,2,3,4,5,6])
    tsapp_transmit_lin_sync(ALIN)
    """
    r = dll.tsapp_transmit_lin_sync(byref(Msg), ATimeoutMS)
    return r


# CAN RBS 相关示例可以参照  rbs_signal_wrie_read_demo.py github 地址为：https://github.com/sy950915/TSMasterAPI.git
# Flexray rbs 相关示例可以参照 flexray_demo.py github 地址为：https://github.com/sy950915/TSMasterAPI.git

# 开启rbs 
def tscom_can_rbs_start():
    r = dll.tscom_can_rbs_start()
    return r


# 停止rbs
def tscom_can_rbs_stop():
    r = dll.tscom_can_rbs_stop()
    return r


# rbs是否开启
def tscom_can_rbs_is_running(AIsRunning: c_bool):
    r = dll.tscom_can_rbs_is_running(byref(AIsRunning))
    return r


# rbs配置
def tscom_can_rbs_configure(AAutoStart: c_bool, AAutoSendOnModification: c_bool, AActivateNodeSimulation: c_bool,TLIBRBSInitValueOptions: c_int):
    r = dll.tscom_can_rbs_configure(AAutoStart, AAutoSendOnModification, AActivateNodeSimulation,
                                    TLIBRBSInitValueOptions)
    return r


def tscom_can_rbs_activate_network_by_name(AIdxChn:c_int32,AEnable: bool, ANetworkName: str, AIncludingChildren: bool):
    return dll.tscom_can_rbs_activate_network_by_name(AIdxChn,AEnable, ANetworkName, AIncludingChildren)


def tscom_can_rbs_activate_node_by_name(AIdxChn:c_int32,AEnable: bool, ANetworkName: str, NodeName: str, AIncludingChildren: bool):
    return dll.tscom_can_rbs_activate_node_by_name(AIdxChn,AEnable, ANetworkName, NodeName, AIncludingChildren)


def tscom_can_rbs_activate_message_by_name(AIdxChn:c_int32,AEnable: bool, ANetworkName: str, NodeName: str, MessageName: str):
    return dll.tscom_can_rbs_activate_message_by_name(AIdxChn,AEnable, ANetworkName, NodeName, MessageName)


def tscom_can_rbs_activate_all_networks(AEnable: bool, AIncludingChildren: bool):
    return dll.tscom_can_rbs_activate_all_networks(AEnable, AIncludingChildren)



def tscom_can_rbs_get_signal_value_by_address(ASymboladdress: str, Avalue: c_double):
    return dll.tscom_can_rbs_get_signal_value_by_address(ASymboladdress, byref(Avalue))


def tscom_can_rbs_get_signal_value_by_element(AIdchn: c_int32, ANetwork: str, ANodeName: str, AMessageName: str,
                                              ASignalName: str, Avalue: c_double):
    return dll.tscom_can_rbs_get_signal_value_by_element(AIdchn, ANetwork, ANodeName, AMessageName, ASignalName, byref(Avalue))


def tscom_can_rbs_set_message_cycle_by_name(AIntervalMs:c_float,ANetwork: str, ANodeName: str, AMessageName: str):
    return dll.tscom_can_rbs_set_message_cycle_by_name(AIntervalMs,ANetwork,ANodeName,AMessageName)


def tscom_can_rbs_set_signal_value_by_address(ASymboladdress: str, Avalue: c_double):
    return dll.tscom_can_rbs_set_signal_value_by_address(ASymboladdress, Avalue)


def tscom_can_rbs_set_signal_value_by_element(AIdchn: c_int32, ANetwork: str, ANodeName: str, AMessageName: str,ASignalName: str, Avalue: c_double):
    return dll.tscom_can_rbs_set_signal_value_by_element(AIdchn, ANetwork, ANodeName, AMessageName, ASignalName, Avalue)





# 获取can信号值
def tsdb_get_signal_value_can(ACAN: dll.TLIBCAN, AMsgName: str, ASgnName: str, AValue: c_double):
    """
    AValue = c_double(0)
    ACAN = dll.TLIBCAN(FIdxChn=0, FDLC=8, FIdentifier=0x1, FProperties=1, FData=[1,2,3,4,5,6])
    tsdb_get_signal_value_can(ACAN,b'msgname',b'siganlname',AValue)
    """
    if isinstance(AValue,int) or isinstance(AValue,float):
        AValue = c_int32(AValue)
    r = dll.tsdb_get_signal_value_can(byref(ACAN), AMsgName, ASgnName, byref(AValue))
    return r


# 获取canfd信号值
def tsdb_get_signal_value_canfd(ACANFD: dll.TLIBCANFD, AMsgName: str, ASgnName: str, AValue: c_double):
    """
    AValue = c_double(0)
    ACANFD = dll.TLIBCANFD(FIdxChn=0, FDLC=8, FIdentifier=0x1, FProperties=1, FData=[1,2,3,4,5,6])
    tsdb_get_signal_value_canfd(ACANFD,b'msgname',b'siganlname',AValue)
    """
    r = dll.tsdb_get_signal_value_canfd(ACANFD, AMsgName, ASgnName,AValue)
    return r


# 设置can信号值
def tsdb_set_signal_value_can(ACAN: dll.TLIBCAN, AMsgName: str, ASgnName: str, AValue: c_double):
    """
    AValue = c_double(20.0)
    ACAN = dll.TLIBCAN(FIdxChn=0, FDLC=8, FIdentifier=0x1, FProperties=1, FData=[1,2,3,4,5,6])
    tsdb_set_signal_value_can(ACAN,b'msgname',b'siganlname',AValue)
    """
    if isinstance(AValue,int) or isinstance(AValue,float):
        AValue = c_int32(AValue)
    r = dll.tsdb_set_signal_value_can(byref(ACAN), AMsgName.encode, ASgnName, AValue)
    return r


# 设置canfd信号值
def tsdb_set_signal_value_canfd(ACANFD: dll.TLIBCANFD, AMsgName: str, ASgnName: str, AValue: c_double):
    """
    AValue = c_double(20.0)
    ACANFD = dll.TLIBCANFD(FIdxChn=0, FDLC=8, FIdentifier=0x1, FProperties=1, FData=[1,2,3,4,5,6])
    tsdb_set_signal_value_canfd(ACANFD,b'msgname',b'siganlname',AValue)
    """
    r = dll.tsdb_set_signal_value_canfd(ACANFD, AMsgName, ASgnName, AValue)
    return r





# 获取dbc信息
def tsdb_get_can_db_info(ADatabaseId: c_int32, AType: c_int32, AIndex: c_int32, ASubIndex: c_int32):
    AValue = POINTER(POINTER(c_char))()
    r = dll.tsdb_get_can_db_info(ADatabaseId, c_int32(AType), c_int32(AIndex), c_uint32(ASubIndex), byref(AValue))
    AValue = string_at(AValue).decode("utf8")
    return r, AValue


# 添加在线回放配置
def tslog_add_online_replay_config(AFileName: str, AIndex: c_int32):
    r = dll.tslog_add_online_replay_config(AFileName.encode("utf8"), byref(AIndex))
    return r


# 设置在线回放配置
def tslog_set_online_replay_config(AIndex: c_int32, AName: str, AFileName: str, AAutoStart: c_bool,
                                   AIsRepetitiveMode: c_bool, AStartTimingMode: c_int32, AStartDelayTimeMs: c_int32,
                                   ASendTx: c_bool, ASendRx: c_bool, AMappings: c_char_p):
    r = dll.tslog_set_online_replay_config(AIndex, AName, AFileName, AAutoStart, AIsRepetitiveMode, AStartTimingMode,
                                           AStartDelayTimeMs, ASendTx, ASendRx, AMappings)
    return r


# 获取在线回放文件数量
def tslog_get_online_replay_count(ACount: c_int32):
    r = dll.tslog_get_online_replay_count(byref(ACount))
    return r


# 获取在线回放配置
def tslog_get_online_replay_config(AIndex: c_int32, AName: str, AFileName: str, AAutoStart: c_bool,
                                   AIsRepetitiveMode: c_bool, AStartTimingMode: c_int32, AStartDelayTimeMs: c_int32,
                                   ASendTx: c_bool, ASendRx: c_bool, AMappings: c_char_p):
    r = dll.tslog_get_online_replay_config(AIndex, byref(AName), byref(AFileName), byref(AAutoStart),
                                           byref(AIsRepetitiveMode), byref(AStartTimingMode), byref(AStartDelayTimeMs),
                                           byref(ASendTx), byref(ASendRx), byref(AMappings))
    return r


# 删除在线回放配置
def tslog_del_online_replay_config(AIndex: c_int32):
    r = dll.tslog_del_online_replay_config(AIndex)
    return r


# 删除所有在线回放配置
def tslog_del_online_replay_configs():
    r = dll.tslog_del_online_replay_configs()
    return r


# 开始在线回放
def tslog_start_online_replay(AInde: c_int32):
    r = dll.tslog_del_online_replay_configs(AInde)
    return r


# 所有文件开始回放
def tslog_start_online_replays():
    r = dll.tslog_start_online_replays()
    return r


# 暂停在线回放
def tslog_pause_online_replay(AInde: c_int32):
    r = dll.tslog_pause_online_replay(AInde)
    return r


# 所有文件暂停回放
def tslog_pause_online_replays():
    r = dll.tslog_pause_online_replays()
    return r


# 停止在线回放
def tslog_stop_online_replay(AInde: c_int32):
    r = dll.tslog_stop_online_replay(AInde)
    return r


# 所有文件停止回放
def tslog_stop_online_replays():
    r = dll.tslog_stop_online_replays()
    return r


# 获取在线回放状态
def tslog_get_online_replay_status(AIndex: c_int32, AStatus: c_int32, AProgressPercent100: c_float):
    r = dll.tslog_get_online_replay_status(AIndex, byref(AStatus), byref(AProgressPercent100))
    return r


# 开始读取blf
def tslog_blf_read_start(Pathfile: bytes, AHeadle: c_int32, ACount: c_int32):
    """
    blfID = c_int32(0)
    count = c_ulong(0)
    tslog_blf_read_start(b'D:/1.blf', blfID, count)
    print(blfID,count)
    """
    r = dll.tslog_blf_read_start(Pathfile, byref(AHeadle), byref(ACount))
    return r


def tslog_blf_read_object(AHandle: c_int32, AProgressedCnt: c_int32, AType: TSupportedObjType, ACAN: dll.TLIBCAN,
                          ALIN: dll.TLIBLIN, ACANFD: dll.TLIBCANFD):
    
    """
    blfID = c_int32(0)
    count = c_ulong(0)
    tslog_blf_read_start(b'D:/1.blf', blfID, count)
    realCount = c_ulong(0)
    messageType = TSupportedObjType.sotUnknown
    CANtemp = dll.TLIBCAN()
    CANFDtemp = dll.TLIBCANFD()
    LINtemp = dll.TLIBLIN()
    for i in range(count.value):
        tslog_blf_read_object(blfID, realCount, messageType, CANtemp, LINtemp, CANFDtemp)
        if messageType.value == TSupportedObjType.sotCAN.value:
            print(CANtemp.FTimeUs / 1000000, CANtemp.FIdxChn, CANtemp.FIdentifier, CANtemp.FProperties, CANtemp.FDLC,
                  CANtemp.FData[0], CANtemp.FData[1], CANtemp.FData[2], CANtemp.FData[3], CANtemp.FData[4],
                  CANtemp.FData[5], CANtemp.FData[6], CANtemp.FData[7])
    tslog_blf_read_end(blfID)
    """
    r = dll.tslog_blf_read_object(AHandle, byref(AProgressedCnt), byref(AType), byref(ACAN), byref(ALIN), byref(ACANFD))
    return r


def tslog_blf_read_end(AHeadle: c_int64):
    """
    blfID = c_int32(0)
    count = c_ulong(0)
    tslog_blf_read_start(b'D:/1.blf', blfID, count)
    realCount = c_ulong(0)
    messageType = TSupportedObjType.sotUnknown
    CANtemp = dll.TLIBCAN()
    CANFDtemp = dll.TLIBCANFD()
    LINtemp = dll.TLIBLIN()
    for i in range(count.value):
        tslog_blf_read_object(blfID, realCount, messageType, CANtemp, LINtemp, CANFDtemp)
        if messageType.value == TSupportedObjType.sotCAN.value:
            print(CANtemp.FTimeUs / 1000000, CANtemp.FIdxChn, CANtemp.FIdentifier, CANtemp.FProperties, CANtemp.FDLC,
                  CANtemp.FData[0], CANtemp.FData[1], CANtemp.FData[2], CANtemp.FData[3], CANtemp.FData[4],
                  CANtemp.FData[5], CANtemp.FData[6], CANtemp.FData[7])
    tslog_blf_read_end(blfID)
    """
    r = dll.tslog_blf_read_end(AHeadle)
    return r


def tslog_blf_write_start(Pathfile: str, AHeadle: c_int32):
    """
    writeHandle = c_int32(0)
    tslog_blf_write_start("D:/2.blf", writeHandle)
    """
    r = dll.tslog_blf_write_start(Pathfile, byref(AHeadle))
    return r


def tslog_blf_write_can(AHeadle: c_int32, ACAN: dll.TLIBCAN):
    """
    blfID = c_int32(0)
    count = c_ulong(0)
    tslog_blf_read_start(b'D:/1.blf', blfID, count)
    realCount = c_ulong(0)
    messageType = TSupportedObjType.sotUnknown
    CANtemp = dll.TLIBCAN()
    CANFDtemp = dll.TLIBCANFD()
    LINtemp = dll.TLIBLIN()
    for i in range(count.value):
        tslog_blf_read_object(blfID, realCount, messageType, CANtemp, LINtemp, CANFDtemp)
        if messageType.value == TSupportedObjType.sotCAN.value:
            CANtemp.FIdxChn = 2
            tslog_blf_write_can(writeHandle, CANtemp)
    tslog_blf_read_end(blfID)
    tslog_blf_write_end(writeHandle)
    """
    r = dll.tslog_blf_write_can(AHeadle, byref(ACAN))
    return r


def tslog_blf_write_can_fd(AHeadle: c_int32, ACANFD: dll.TLIBCANFD):
    """
    blfID = c_int32(0)
    count = c_ulong(0)
    tslog_blf_read_start(b'D:/1.blf', blfID, count)
    realCount = c_ulong(0)
    messageType = TSupportedObjType.sotUnknown
    CANtemp = dll.TLIBCAN()
    CANFDtemp = dll.TLIBCANFD()
    LINtemp = dll.TLIBLIN()
    for i in range(count.value):
        tslog_blf_read_object(blfID, realCount, messageType, CANtemp, LINtemp, CANFDtemp)
        if messageType.value == TSupportedObjType.sotCANFD.value:
            CANtemp.FIdxChn = 2
            tslog_blf_write_canfd(writeHandle, CANFDtemp)
    tslog_blf_read_end(blfID)
    tslog_blf_write_end(writeHandle)
    """
    r = dll.tslog_blf_write_can_fd(AHeadle, byref(ACANFD))
    return r


def tslog_blf_write_lin(AHeadle: c_int32, ALIN: dll.TLIBLIN):
    """
    blfID = c_int32(0)
    count = c_ulong(0)
    tslog_blf_read_start(b'D:/1.blf', blfID, count)
    realCount = c_ulong(0)
    messageType = TSupportedObjType.sotUnknown
    CANtemp = dll.TLIBCAN()
    CANFDtemp = dll.TLIBCANFD()
    LINtemp = dll.TLIBLIN()
    for i in range(count.value):
        tslog_blf_read_object(blfID, realCount, messageType, CANtemp, LINtemp, CANFDtemp)
        if messageType.value == TSupportedObjType.sotLIN.value:
            CANtemp.FIdxChn = 2
            tslog_blf_write_lin(writeHandle, LINtemp)
    tslog_blf_read_end(blfID)
    tslog_blf_write_end(writeHandle)
    """
    r = dll.tslog_blf_write_lin(AHeadle, byref(ALIN))
    return r


def tslog_blf_write_end(AHeadle: c_int64):
    """
    tslog_blf_write_end(writeHandle)
    """
    r = dll.tslog_blf_write_end(AHeadle)
    return r


# 诊断相关API

# 创建诊断服务
def tsdiag_can_create(udsHandle: c_int8, ChnIndex: c_int32, ASupportFD: c_byte, AMaxdlc: c_byte, reqID: c_int32,ARequestIDIsStd: c_bool,resID: c_int32, resIsStd: c_bool, AFctID: c_int32, fctIsStd: c_bool):
    
    """
    udsHandle = c_int8(0)
    ChnIndex = 0
    ASupportFD  = c_byte(1)
    AMaxdlc = c_byte(8)
    reqID = c_int32(0x7e0)
    ARequestIDIsStd = False
    resID = c_int32(0x7e3)
    resIsStd = False
    AFctID = c_int32(0x7df)
    fctIsStd = False
    tsdiag_can_create(udsHandle,ChnIndex,ASupportFD,AMaxdlc,reqID,resIsStd,resID,resIsStd,AFctID,fctIsStd)
    """
    r = dll.tsdiag_can_create(byref(udsHandle), ChnIndex, ASupportFD, AMaxdlc, reqID,
                              ARequestIDIsStd, resID, resIsStd, AFctID, fctIsStd)
    return r

def tsdiag_set_p2_extended(pDiagModuleIndex: c_int8,TimeOut:c_int32):
    """
    udsHandle = c_int8(0)
    ChnIndex = 0
    ASupportFD  = c_byte(1)
    AMaxdlc = c_byte(8)
    reqID = c_int32(0x7e0)
    ARequestIDIsStd = False
    resID = c_int32(0x7e3)
    resIsStd = False
    AFctID = c_int32(0x7df)
    fctIsStd = False
    tsdiag_can_create(udsHandle,ChnIndex,ASupportFD,AMaxdlc,reqID,resIsStd,resID,resIsStd,AFctID,fctIsStd)

    TimeOut = c_int32(200)
    tsdiag_set_p2_extended(udsHandle,TimeOut)
    """
    if isinstance(TimeOut,int)or isinstance(TimeOut,float):
        TimeOut = c_int32(TimeOut)
    r = dll.tsdiag_set_p2_extended(pDiagModuleIndex,TimeOut)
    return r

def tsdiag_set_p2_timeout(pDiagModuleIndex: c_int8,TimeOut):
    """
    udsHandle = c_int8(0)
    ChnIndex = 0
    ASupportFD  = c_byte(1)
    AMaxdlc = c_byte(8)
    reqID = c_int32(0x7e0)
    ARequestIDIsStd = False
    resID = c_int32(0x7e3)
    resIsStd = False
    AFctID = c_int32(0x7df)
    fctIsStd = False
    tsdiag_can_create(udsHandle,ChnIndex,ASupportFD,AMaxdlc,reqID,resIsStd,resID,resIsStd,AFctID,fctIsStd)

    TimeOut = c_int32(200)
    tsdiag_set_p2_timeout(udsHandle,TimeOut)
    """
    if isinstance(TimeOut,int)or isinstance(TimeOut,float):
        TimeOut = c_int32(TimeOut)
    r = dll.tsdiag_set_p2_timeout(pDiagModuleIndex,c_int32(TimeOut))
    return r

def tsdiag_set_s3_clienttime(pDiagModuleIndex: c_int8,TimeOut):
    """
    udsHandle = c_int8(0)
    ChnIndex = 0
    ASupportFD  = c_byte(1)
    AMaxdlc = c_byte(8)
    reqID = c_int32(0x7e0)
    ARequestIDIsStd = False
    resID = c_int32(0x7e3)
    resIsStd = False
    AFctID = c_int32(0x7df)
    fctIsStd = False
    tsdiag_can_create(udsHandle,ChnIndex,ASupportFD,AMaxdlc,reqID,resIsStd,resID,resIsStd,AFctID,fctIsStd)

    TimeOut = c_int32(200)
    tsdiag_set_s3_clienttime(udsHandle,TimeOut)
    """
    if isinstance(TimeOut,int)or isinstance(TimeOut,float):
        TimeOut = c_int32(TimeOut)
    r = dll.tsdiag_set_s3_clienttime(pDiagModuleIndex,c_int32(TimeOut))
    return r

def tsdiag_set_s3_servertime(pDiagModuleIndex: c_int8,TimeOut):
    """
    udsHandle = c_int8(0)
    ChnIndex = 0
    ASupportFD  = c_byte(1)
    AMaxdlc = c_byte(8)
    reqID = c_int32(0x7e0)
    ARequestIDIsStd = False
    resID = c_int32(0x7e3)
    resIsStd = False
    AFctID = c_int32(0x7df)
    fctIsStd = False
    tsdiag_can_create(udsHandle,ChnIndex,ASupportFD,AMaxdlc,reqID,resIsStd,resID,resIsStd,AFctID,fctIsStd)

    TimeOut = c_int32(200)
    tsdiag_set_s3_servertime(udsHandle,TimeOut)
    """
    if isinstance(TimeOut,int)or isinstance(TimeOut,float):
        TimeOut = c_int32(TimeOut)
    r = dll.tsdiag_set_s3_servertime(pDiagModuleIndex,c_int32(TimeOut))
    return r


def tsdiag_can_delete(pDiagModuleIndex: c_int8):
    """
    udsHandle = c_int8(0)
    ChnIndex = 0
    ASupportFD  = c_byte(1)
    AMaxdlc = c_byte(8)
    reqID = c_int32(0x7e0)
    ARequestIDIsStd = False
    resID = c_int32(0x7e3)
    resIsStd = False
    AFctID = c_int32(0x7df)
    fctIsStd = False
    tsdiag_can_create(udsHandle,ChnIndex,ASupportFD,AMaxdlc,reqID,resIsStd,resID,resIsStd,AFctID,fctIsStd)

    tsdiag_can_delete(udsHandle)
    """
    r = tsdiag_can_delete(pDiagModuleIndex)
    return r


def tsdiag_can_delete_all():
    r = dll.tsdiag_can_delete_all()
    return r


def tstp_can_send_functional(pDiagModuleIndex: c_int8, AReqDataArray: bytes, AReqDataSize: c_int32):
    """
    udsHandle = c_int8(0)
    ChnIndex = 0
    ASupportFD  = c_byte(1)
    AMaxdlc = c_byte(8)
    reqID = c_int32(0x7e0)
    ARequestIDIsStd = False
    resID = c_int32(0x7e3)
    resIsStd = False
    AFctID = c_int32(0x7df)
    fctIsStd = False
    tsdiag_can_create(udsHandle,ChnIndex,ASupportFD,AMaxdlc,reqID,resIsStd,resID,resIsStd,AFctID,fctIsStd)

    AReqDataArray = bytes([10,02])
    tstp_can_send_functional(udsHandle,AReqDataArray,len(AReqDataArray))

    """
    # data = POINTER(c_ubyte * len(AReqDataArray))((c_ubyte * len(AReqDataArray))(*AReqDataArray))
    r = dll.tstp_can_send_functional(pDiagModuleIndex, AReqDataArray, AReqDataSize)
    return r


def tstp_can_send_request(pDiagModuleIndex: c_int8, AReqDataArray: bytes, AReqDataSize: c_int32):
    # data = POINTER(c_ubyte * len(AReqDataArray))((c_ubyte * len(AReqDataArray))(*AReqDataArray))
    """
    udsHandle = c_int8(0)
    ChnIndex = 0
    ASupportFD  = c_byte(1)
    AMaxdlc = c_byte(8)
    reqID = c_int32(0x7e0)
    ARequestIDIsStd = False
    resID = c_int32(0x7e3)
    resIsStd = False
    AFctID = c_int32(0x7df)
    fctIsStd = False
    tsdiag_can_create(udsHandle,ChnIndex,ASupportFD,AMaxdlc,reqID,resIsStd,resID,resIsStd,AFctID,fctIsStd)

    AReqDataArray = bytes([10,02])
    tstp_can_send_request(udsHandle,AReqDataArray,len(AReqDataArray))

    """
    r = dll.tstp_can_send_request(pDiagModuleIndex, AReqDataArray, AReqDataSize)
    return r


def tstp_can_request_and_get_response(udsHandle: c_int8, dataIn: bytearray, ReqSize: c_int32, dataOut: bytes,resSize: c_int32):

    """
    udsHandle = c_int8(0)
    ChnIndex = 0
    ASupportFD  = c_byte(1)
    AMaxdlc = c_byte(8)
    reqID = c_int32(0x7e0)
    ARequestIDIsStd = False
    resID = c_int32(0x7e3)
    resIsStd = False
    AFctID = c_int32(0x7df)
    fctIsStd = False
    tsdiag_can_create(udsHandle,ChnIndex,ASupportFD,AMaxdlc,reqID,resIsStd,resID,resIsStd,AFctID,fctIsStd)

    AReqDataArray = bytes([0x10,0x02])
    max_len = 1000
    AResponseDataArray = (c_uint8 * max_len)()
    AResponseDataSize = c_uint32(len(AResdata))
    tstp_can_request_and_get_response(udsHandle,AReqDataArray,len(AReqDataArray),AResponseDataArray,AResponseDataSize)
    """
    r = dll.tstp_can_request_and_get_response(udsHandle, dataIn, ReqSize, dataOut, byref(resSize))
    return r

# 诊断服务

def tsdiag_can_session_control(pDiagModuleIndex: c_int8, ASubSession: c_byte):
    """
    udsHandle = c_int8(0)
    ChnIndex = 0
    ASupportFD  = c_byte(1)
    AMaxdlc = c_byte(8)
    reqID = c_int32(0x7e0)
    ARequestIDIsStd = False
    resID = c_int32(0x7e3)
    resIsStd = False
    AFctID = c_int32(0x7df)
    fctIsStd = False
    tsdiag_can_create(udsHandle,ChnIndex,ASupportFD,AMaxdlc,reqID,resIsStd,resID,resIsStd,AFctID,fctIsStd)

    tsdiag_can_session_control(udsHandle,c_uint8(1)) # 10 01
    """
    r = dll.tsdiag_can_session_control(pDiagModuleIndex, ASubSession)
    return r


def tsdiag_can_routine_control(pDiagModuleIndex: c_int8, ARoutineControlType: c_byte, ARoutintID: c_uint16,
                            ):
    """
    udsHandle = c_int8(0)
    ChnIndex = 0
    ASupportFD  = c_byte(1)
    AMaxdlc = c_byte(8)
    reqID = c_int32(0x7e0)
    ARequestIDIsStd = False
    resID = c_int32(0x7e3)
    resIsStd = False
    AFctID = c_int32(0x7df)
    fctIsStd = False
    tsdiag_can_create(udsHandle,ChnIndex,ASupportFD,AMaxdlc,reqID,resIsStd,resID,resIsStd,AFctID,fctIsStd)

    tsdiag_can_session_control(udsHandle,c_uint8(1),c_uint16(0xf100)) # 31 01 f1 00
    """
    r = dll.tsdiag_can_routine_control(pDiagModuleIndex, ARoutineControlType, ARoutintID)
    return r


def tsdiag_can_communication_control(pDiagModuleIndex: c_int8, AControlType: c_byte):
    """
    udsHandle = c_int8(0)
    ChnIndex = 0
    ASupportFD  = c_byte(1)
    AMaxdlc = c_byte(8)
    reqID = c_int32(0x7e0)
    ARequestIDIsStd = False
    resID = c_int32(0x7e3)
    resIsStd = False
    AFctID = c_int32(0x7df)
    fctIsStd = False
    tsdiag_can_create(udsHandle,ChnIndex,ASupportFD,AMaxdlc,reqID,resIsStd,resID,resIsStd,AFctID,fctIsStd)

    tsdiag_can_session_control(udsHandle,c_uint8(1)) # 28 01
    """
    r = dll.tsdiag_can_communication_control(pDiagModuleIndex, AControlType)
    return r


def tsdiag_can_security_access_request_seed(pDiagModuleIndex: c_int8, ALevel: c_int32, ARecSeed: bytearray,
                                            ARecSeedSize: c_int32):
    # AReqdata = POINTER(c_ubyte * len(ARecSeed))((c_ubyte * len(ARecSeed))(*ARecSeed))
    """
    udsHandle = c_int8(0)
    ChnIndex = 0
    ASupportFD  = c_byte(1)
    AMaxdlc = c_byte(8)
    reqID = c_int32(0x7e0)
    ARequestIDIsStd = False
    resID = c_int32(0x7e3)
    resIsStd = False
    AFctID = c_int32(0x7df)
    fctIsStd = False
    tsdiag_can_create(udsHandle,ChnIndex,ASupportFD,AMaxdlc,reqID,resIsStd,resID,resIsStd,AFctID,fctIsStd)

    max_len = 1000
    AResponseDataArray = (c_uint8 * max_len)()
    AResponseDataSize = c_uint32(len(AResdata))
    tsdiag_can_security_access_request_seed(udsHandle,1,AResponseDataArray,AResponseDataSize) 27 01 
    """
    r = dll.tsdiag_can_security_access_request_seed(pDiagModuleIndex, ALevel, ARecSeed, byref(ARecSeedSize))
    return r


def tsdiag_can_security_access_send_key(pDiagModuleIndex: c_int8, ALevel: c_int32, AKeyValue: bytearray,
                                        AKeySize: c_int32):
    # AReqdata = POINTER(c_ubyte * len(AKeyValue))((c_ubyte * len(AKeyValue))(*AKeyValue))
    """
    udsHandle = c_int8(0)
    ChnIndex = 0
    ASupportFD  = c_byte(1)
    AMaxdlc = c_byte(8)
    reqID = c_int32(0x7e0)
    ARequestIDIsStd = False
    resID = c_int32(0x7e3)
    resIsStd = False
    AFctID = c_int32(0x7df)
    fctIsStd = False
    tsdiag_can_create(udsHandle,ChnIndex,ASupportFD,AMaxdlc,reqID,resIsStd,resID,resIsStd,AFctID,fctIsStd)

    AReqDataArray = bytes([0x27,1,1,2,3,4])
    
    tsdiag_can_security_access_send_key(udsHandle,2,AReqDataArray,len(AReqDataArray)) 0x27 1 1 2 3 4 
    """
    r = dll.tsdiag_can_security_access_send_key(pDiagModuleIndex, ALevel, AKeyValue, AKeySize)
    return r


def tsdiag_can_request_download(pDiagModuleIndex: c_int8, AMemAddr: c_uint32, AMemSize: c_uint32):
    """
    udsHandle = c_int8(0)
    ChnIndex = 0
    ASupportFD  = c_byte(1)
    AMaxdlc = c_byte(8)
    reqID = c_int32(0x7e0)
    ARequestIDIsStd = False
    resID = c_int32(0x7e3)
    resIsStd = False
    AFctID = c_int32(0x7df)
    fctIsStd = False
    tsdiag_can_create(udsHandle,ChnIndex,ASupportFD,AMaxdlc,reqID,resIsStd,resID,resIsStd,AFctID,fctIsStd)
    AMemAddr = c_int32(0x80000010)
    AMemSize = c_int32(0x1000)
    tsdiag_can_request_download(udsHandle,AMemAddr,AMemSize) 34 44 80 00 00 10 00 00 10 00
    """
    r = dll.tsdiag_can_request_download(pDiagModuleIndex, AMemAddr, AMemSize)
    return r


def tsdiag_can_request_upload(pDiagModuleIndex: c_int8, AMemAddr: c_uint32, AMemSize: c_uint32):
    """
    udsHandle = c_int8(0)
    ChnIndex = 0
    ASupportFD  = c_byte(1)
    AMaxdlc = c_byte(8)
    reqID = c_int32(0x7e0)
    ARequestIDIsStd = False
    resID = c_int32(0x7e3)
    resIsStd = False
    AFctID = c_int32(0x7df)
    fctIsStd = False
    tsdiag_can_create(udsHandle,ChnIndex,ASupportFD,AMaxdlc,reqID,resIsStd,resID,resIsStd,AFctID,fctIsStd)
    AMemAddr = c_int32(0x80000010)
    AMemSize = c_int32(0x1000)
    tsdiag_can_request_upload(udsHandle,AMemAddr,AMemSize) 35 44 80 00 00 10 00 00 10 00
    """
    r = dll.tsdiag_can_request_upload(pDiagModuleIndex, AMemAddr, AMemSize)
    return r


def tsdiag_can_transfer_data(pDiagModuleIndex: c_int8, ASourceDatas: bytes, ADataSize: c_int32, AReqCase: c_int32):
    # AReqdata = POINTER(c_ubyte * len(ASourceDatas))((c_ubyte * len(ASourceDatas))(*ASourceDatas))
    """
    udsHandle = c_int8(0)
    ChnIndex = 0
    ASupportFD  = c_byte(1)
    AMaxdlc = c_byte(8)
    reqID = c_int32(0x7e0)
    ARequestIDIsStd = False
    resID = c_int32(0x7e3)
    resIsStd = False
    AFctID = c_int32(0x7df)
    fctIsStd = False
    tsdiag_can_create(udsHandle,ChnIndex,ASupportFD,AMaxdlc,reqID,resIsStd,resID,resIsStd,AFctID,fctIsStd)
    ASourceDatas = bytes[1,2,3,4,5,6,7,2,8]
    AMemSize = c_int32(0x1000)
    tsdiag_can_transfer_data(udsHandle,ASourceDatas,len(ASourceDatas),01) 36 01
    """
    return dll.tsdiag_can_transfer_data(pDiagModuleIndex, ASourceDatas, ADataSize, AReqCase)


def tsdiag_can_request_transfer_exit(pDiagModuleIndex: c_int8):
    """
    udsHandle = c_int8(0)
    ChnIndex = 0
    ASupportFD  = c_byte(1)
    AMaxdlc = c_byte(8)
    reqID = c_int32(0x7e0)
    ARequestIDIsStd = False
    resID = c_int32(0x7e3)
    resIsStd = False
    AFctID = c_int32(0x7df)
    fctIsStd = False
    tsdiag_can_create(udsHandle,ChnIndex,ASupportFD,AMaxdlc,reqID,resIsStd,resID,resIsStd,AFctID,fctIsStd)

    tsdiag_can_request_transfer_exit(udsHandle) 37 
    """
    r = dll.tsdiag_can_request_transfer_exit(pDiagModuleIndex)
    return r


def tsdiag_can_write_data_by_identifier(pDiagModuleIndex: c_int8, ADataIdentifier: c_uint16, AWriteData: bytearray,AWriteDataSize: c_int32):
    # AReqdata = POINTER(c_ubyte * len(AWriteData))((c_ubyte * len(AWriteData))(*AWriteData))
    """
    udsHandle = c_int8(0)
    ChnIndex = 0
    ASupportFD  = c_byte(1)
    AMaxdlc = c_byte(8)
    reqID = c_int32(0x7e0)
    ARequestIDIsStd = False
    resID = c_int32(0x7e3)
    resIsStd = False
    AFctID = c_int32(0x7df)
    fctIsStd = False
    tsdiag_can_create(udsHandle,ChnIndex,ASupportFD,AMaxdlc,reqID,resIsStd,resID,resIsStd,AFctID,fctIsStd)
    
    ADataIdentifier = c_int16(0xf190)
    ASourceDatas = bytes[1,2,3,4,5,6,7,2,8]

    tsdiag_can_request_transfer_exit(udsHandle,ADataIdentifier,ASourceDatas,len(ASourceDatas)) 2e f1 90 1... 

    """
    r = dll.tsdiag_can_write_data_by_identifier(pDiagModuleIndex, ADataIdentifier, AWriteData, AWriteDataSize)
    return r


def tsdiag_can_read_data_by_identifier(pDiagModuleIndex: c_int8, ADataIdentifier: c_uint16, AReturnArray: bytearray,AReturnArraySize: c_int32):
    """
    udsHandle = c_int8(0)
    ChnIndex = 0
    ASupportFD  = c_byte(1)
    AMaxdlc = c_byte(8)
    reqID = c_int32(0x7e0)
    ARequestIDIsStd = False
    resID = c_int32(0x7e3)
    resIsStd = False
    AFctID = c_int32(0x7df)
    fctIsStd = False
    tsdiag_can_create(udsHandle,ChnIndex,ASupportFD,AMaxdlc,reqID,resIsStd,resID,resIsStd,AFctID,fctIsStd)
    
    ADataIdentifier = c_int16(0xf190)
    AReturnArray = (c_uint8*100)()
    AReturnArraySize = c_int32(len(AReturnArray))
    tsdiag_can_request_transfer_exit(udsHandle,ADataIdentifier,AReturnArray,AReturnArraySize) 22 f1 90  

    """
    # AReqdata = POINTER(c_ubyte * len(AReturnArray))((c_ubyte * len(AReturnArray))(*AReturnArray))
    r = dll.tsdiag_can_read_data_by_identifier(pDiagModuleIndex, ADataIdentifier, AReturnArray, byref(AReturnArraySize))
    return r


# LIN诊断
def tstp_lin_master_request(AChnIdx: c_int32, ANAD: c_int8, AData: bytearray, ADataNum: c_int,
                            ATimeoutMs: c_int32):
    AReqdata = POINTER(c_ubyte * len(AData))((c_ubyte * len(AData))(*AData))
    r = dll.tstp_lin_master_request(AChnIdx, ANAD, byref(AReqdata), c_int32(ADataNum), c_int32(ATimeoutMs))
    return r


def tstp_lin_master_request_intervalms(AChnIdx: c_int32, AData: c_uint16):
    r = dll.tstp_lin_master_request_intervalms(AChnIdx, AData)
    return r


def tstp_lin_reset(AChnIdx: c_int32):
    r = dll.tstp_lin_reset(AChnIdx)
    return r


def tstp_lin_slave_response_intervalms(AChnIdx: c_int32, AData: c_uint16):
    r = dll.tstp_lin_slave_response_intervalms(AChnIdx, AData)
    return r


def tsdiag_lin_read_data_by_identifier(AChnIdx: c_int32, ANAD: c_int8, AId: c_ushort, AResNAD: c_byte,
                                       AResData: bytearray, AResDataNum: c_int32, ATimeoutMS: c_int32):
    Resdata = POINTER(c_ubyte * len(AResData))((c_ubyte * len(AResData))(*AResData))
    r = dll.tsdiag_lin_read_data_by_identifier(AChnIdx, c_int8(ANAD), c_ushort(AId), byref(AResNAD), Resdata,
                                               byref(AResDataNum), ATimeoutMS)
    return r


def tsdiag_lin_write_data_by_identifier(AChnIdx: c_int32, ANAD: c_int8, AId: c_ushort, AReqData: bytearray,
                                        AReqDataNum: c_int32,
                                        AResNAD: c_byte, AResData: bytearray, AResDataNum: c_int32,
                                        ATimeoutMS: c_int32):
    Reqdata = POINTER(c_ubyte * len(AReqData))((c_ubyte * len(AReqData))(*AReqData))
    Resdata = POINTER(c_ubyte * len(AResData))((c_ubyte * len(AResData))(*AResData))

    r = dll.tsdiag_lin_write_data_by_identifier(AChnIdx, c_int8(ANAD), c_ushort(AId), Reqdata, c_int32(AReqDataNum),
                                                byref(AResNAD), Resdata, byref(AResDataNum), ATimeoutMS)
    return r


def tsdiag_lin_session_control(AChnIdx: c_int32, ANAD: c_int8, ANewSession: c_byte, ATimeoutMS: c_int32):
    r = dll.tsdiag_lin_session_control(AChnIdx, c_int8(ANAD), c_byte(ANewSession), c_int32(ATimeoutMS))
    return r


def tsdiag_lin_fault_memory_read(AChnIdx: c_int32, ANAD: c_int8, ANewSession: c_byte, ATimeoutMS: c_int32):
    r = dll.tsdiag_lin_fault_memory_read(AChnIdx, c_int8(ANAD), c_byte(ANewSession), c_int32(ATimeoutMS))
    return r


def tsdiag_lin_fault_memory_clear(AChnIdx: c_int32, ANAD: c_int8, ANewSession: c_byte, ATimeoutMS: c_int32):
    r = dll.tsdiag_lin_fault_memory_clear(AChnIdx, c_int8(ANAD), c_byte(ANewSession), c_int32(ATimeoutMS))
    return r

#TLIBFlxeRay API
# Flexray报文同步发送
def tsapp_transmit_flexray_sync(AFlexRay:dll.TLIBFlexRay,ATimeout:c_int32):
    """
    AFlexray = dll.TLIBFlexRay(FIdxChn=0,FSlotId=1,FChannelMask=1,FActualPayloadLength=32,FCycleNumber=1,FData=[1,2,3,4,5,6,7])
    ATimeout = c_int32(10)
    tsapp_transmit_flexray_sync(AFlexray,ATimeout)
    """
    return dll.tsapp_transmit_flexray_sync(byref(AFlexRay),ATimeout)

# Flexray报文异步发送
def tsapp_transmit_flexray_async(AFlexRay:dll.TLIBFlexRay):
    """
    AFlexray = dll.TLIBFlexRay(FIdxChn=0,FSlotId=1,FChannelMask=1,FActualPayloadLength=32,FCycleNumber=1,FData=[1,2,3,4,5,6,7])
    tsapp_transmit_flexray_async(AFlexray)
    """
    return dll.tsapp_transmit_flexray_async(byref(AFlexRay))

# 清空flexray fifo buffer
def tsfifo_clear_flexray_receive_buffers(chn: c_int):
    """
    chn = 0
    tsfifo_clear_flexray_receive_buffers(chn)
    """
    return dll.tsfifo_clear_flexray_receive_buffers(chn)

# 读取flexray fifo buffer 总数量
def tsfifo_read_flexray_buffer_frame_count(AIdxChn: c_int, ACount: c_int32):
    """
    chn = 0
    ACount = c_int32(0)
    tsfifo_read_flexray_buffer_frame_count(chn,ACount)
    """
    return dll.tsfifo_read_flexray_buffer_frame_count(AIdxChn, byref(ACount))

# 读取flexray fifo buffer tx数量
def tsfifo_read_flexray_tx_buffer_frame_count( AIdxChn: c_int, ACount: c_int32):
    """
    chn = 0
    ACount = c_int32(0)
    tsfifo_read_flexray_tx_buffer_frame_count(chn,ACount)
    """
    return dll.tsfifo_read_flexray_tx_buffer_frame_count(AIdxChn, byref(ACount))

# 读取flexray fifo buffer rx数量
def tsfifo_read_flexray_rx_buffer_frame_count(AIdxChn: c_int, ACount: c_int):
    """
    chn = 0
    ACount = c_int32(0)
    tsfifo_read_flexray_rx_buffer_frame_count(chn,ACount)
    """
    return dll.tsfifo_read_flexray_rx_buffer_frame_count( AIdxChn, byref(ACount))

# 获取fifo中flexray报文 当ARXTX非0 时包含TX报文 为0时仅包含RX报文
def tsfifo_receive_flexray_msgs(ADataBuffers: dll.TLIBFlexRay, ADataBufferSize: c_int, chn: c_int,
                                ARxTx: c_int8):
    """
    ADataBuffers = (dll.TLIBFlexRay*100)()
    ADataBufferSize = c_int32(100)
    chn = 0
    ARxTx = 0
    tsfifo_receive_flexray_msgs(ADataBuffers,ADataBufferSize,chn,ARxTx)
    """
    return dll.tsfifo_receive_flexray_msgs(ADataBuffers, byref(ADataBufferSize), chn, ARxTx)

#启动flexray 网络
def tsflexray_start_net(AChnIdx: c_int32,ATimeout:c_int32):
    """
    chn = 0
    tsflexray_start_net(chn,c_int32(1000))
    """
    return dll.tsflexray_start_net(AChnIdx,ATimeout)

#停止flexray 网络
def tsflexray_stop_net(AChnIdx: c_int32,ATimeout:c_int32):
    """
    chn = 0
    tsflexray_stop_net(chn,c_int32(1000))
    """
    return dll.tsflexray_stop_net(AChnIdx,ATimeout)

# 唤醒flexray pattern
def tsflexray_wakeup_pattern(AChnIdx: c_int32,ATimeout:c_int32):
    """
    chn = 0
    tsflexray_wakeup_pattern(chn,c_int32(1000))
    """
    return dll.tsflexray_wakeup_pattern(AChnIdx,ATimeout)

#tsdb_Flexray api



# 通过地址获取数据库属性信息
def tsdb_get_flexray_db_properties_by_address_verbose(AAddr:str):
    '''
    db_msg =  app.db_get_flexray_database_properties_by_address(b"0/network1")
    print(db_msg)
    '''
    if not isinstance(AAddr,bytes):
        AAddr = bytes(AAddr)
    ADBIndex =c_int32(0)
    AFrameCount = c_int32(0)
    ASignalCount = c_int32(0)
    AECUCount = c_int32(0)
    ASupportedChannelMask = c_int32(0)
    AName = POINTER(POINTER(c_char))()
    AComment= POINTER(POINTER(c_char))()

    ret = dll.tsdb_get_flexray_db_properties_by_address_verbose(AAddr,byref(ADBIndex),byref(ASignalCount),byref(AFrameCount),byref(AECUCount),byref(ASupportedChannelMask),byref(AName),byref(AComment))
    if ret ==0:
        try:
            AComment = string_at(AComment).decode('utf8')
        except:
            AComment = ''
        return ADBIndex,AFrameCount,ASignalCount,AECUCount,ASupportedChannelMask,string_at(AName).decode('utf8'),AComment
    print(tsapp_get_error_description(ret))
    return AECUCount,AFrameCount,ASignalCount,ASupportedChannelMask,string_at(AName),AComment     

# 通过索引获取数据库属性信息
def tsdb_get_flexray_db_properties_by_index_verbose(ADBIndex:c_int32):
    '''
    db_msg =  app.db_get_flexray_database_properties_by_address(0)
    print(db_msg)
    '''
    AFrameCount = c_int32(0)
    ASignalCount = c_int32(0)
    AECUCount = c_int32(0)
    ASupportedChannelMask = c_int64(0)
    AName = POINTER(POINTER(c_char))()
    AComment = POINTER(POINTER(c_char))()

    ret = dll.tsdb_get_flexray_db_properties_by_index_verbose(ADBIndex,byref(ASignalCount),byref(AFrameCount),byref(AECUCount),byref(ASupportedChannelMask),byref(AName),byref(AComment))

    if ret ==0:
        try:
            AComment = string_at(AComment).decode('utf8')
        except:
            AComment = ''
        return AECUCount,AFrameCount,ASignalCount,ASupportedChannelMask,string_at(AName),AComment
    print(tsapp_get_error_description(ret))
    return AECUCount,AFrameCount,ASignalCount,ASupportedChannelMask,string_at(AName),AComment

# 通过地址获取数据库ECU信息
def tsdb_get_flexray_ecu_properties_by_address_verbose(AAddr:str):
    '''
    ecu_msg =  app.tsdb_get_flexray_ecu_properties_by_address_verbose(b"0/network1/ecu1")
    print(ecu_msg)
    '''
    if not isinstance(AAddr,bytes):
        AAddr = bytes(AAddr)
    ADBIndex =c_int32(0)
    AECUIndex = c_int32(0)
    ATxFrameCount = c_int32(0)
    ARxFrameCount = c_int32(0)
    AName = POINTER(POINTER(c_char))()
    AComment= POINTER(POINTER(c_char))()

    ret = dll.tsdb_get_flexray_ecu_properties_by_address_verbose(AAddr,byref(ADBIndex),byref(AECUIndex),byref(ATxFrameCount),byref(ARxFrameCount),byref(AName),byref(AComment))
    if ret ==0:
        try:
            AComment = string_at(AComment).decode('utf8')
        except:
            AComment = ''
        return ADBIndex,AECUIndex,ATxFrameCount,ARxFrameCount,string_at(AName).decode('utf8'),AComment
    print(tsapp_get_error_description(ret))
    return ADBIndex,AECUIndex,ATxFrameCount,ARxFrameCount,string_at(AName).decode('utf8'),AComment

# 通过索引获取数据库ECU信息
def tsdb_get_flexray_ecu_properties_by_index_verbose(ADBIndex:c_int32,AECUIndex:c_int32):
    '''
    ecu_msg =  app.tsdb_get_flexray_ecu_properties_by_index_verbose(0,0)
    print(ecu_msg)
    '''
    ATxFrameCount = c_int32(0)
    ARxFrameCount = c_int32(0)
    AName = POINTER(POINTER(c_char))()
    AComment= POINTER(POINTER(c_char))()

    ret = dll.tsdb_get_flexray_ecu_properties_by_index_verbose(ADBIndex,AECUIndex,byref(ATxFrameCount),byref(ARxFrameCount),byref(AName),byref(AComment))
    if ret ==0:
        try:
            AComment = string_at(AComment).decode('utf8')
        except:
            AComment = ''
        return ATxFrameCount,ARxFrameCount,string_at(AName).decode('utf8'),AComment
    print(tsapp_get_error_description(ret)) 
    return ATxFrameCount,ARxFrameCount,string_at(AName).decode('utf8'),AComment

# 通过地址获取数据库frame信息
def tsdb_get_flexray_frame_properties_by_address_verbose(AAddr:str):
    '''
    frame_msg =  app.tsdb_get_flexray_frame_properties_by_address_verbose(b"0/network1/ecu1/frame1")
    print(frame_msg)
    '''
    if not isinstance(AAddr,bytes):
        AAddr = bytes(AAddr)
    ADBIndex= c_int32(0)
    AECUIndex= c_int32(0)
    AFrameIndex= c_int32(0)
    AIsTx= c_bool()
    AFRChannelMask= c_int32(0)
    AFRBaseCycle= c_int32(0)
    AFRCycleRepetition= c_int32(0)
    AFRIsStartupFrame= c_bool()
    AFRSlotId= c_int32(0)
    AFRCycleMask= c_int64(0)
    ASignalCount= c_int32(0)
    AFRDLC = c_int32(0)
    AName = POINTER(POINTER(c_char))()
    AComment= POINTER(POINTER(c_char))()

    ret = dll.tsdb_get_flexray_frame_properties_by_address_verbose(AAddr,byref(ADBIndex),byref(AECUIndex),byref(AFrameIndex),byref(AIsTx),byref(AFRChannelMask),byref(AFRBaseCycle),byref(AFRCycleRepetition),byref(AFRIsStartupFrame),byref(AFRSlotId),byref(AFRCycleMask),byref(ASignalCount),byref(AFRDLC),byref(AName),byref(AComment))
    if ret ==0:
        try:
            AComment = string_at(AComment).decode('utf8')
        except:
            AComment = ''
        return ADBIndex,AECUIndex,AFrameIndex,AIsTx,AFRChannelMask,AFRBaseCycle,AFRCycleRepetition,AFRIsStartupFrame,AFRSlotId,AFRCycleMask,ASignalCount,AFRDLC,string_at(AName).decode('utf8'),AComment
    print(tsapp_get_error_description(ret)) 
    return ADBIndex,AECUIndex,AFrameIndex,AIsTx,AFRChannelMask,AFRBaseCycle,AFRCycleRepetition,AFRIsStartupFrame,AFRSlotId,AFRCycleMask,ASignalCount,AFRDLC,string_at(AName).decode('utf8'),AComment

# 通过索引获取数据库frame信息
def tsdb_get_flexray_frame_properties_by_index_verbose(ADBIndex:c_int32,AECUIndex:c_int32,AFrameIndex:c_int32,AIsTx:c_bool):
    '''
    frame_msg =  app.tsdb_get_flexray_frame_properties_by_index_verbose(0,0,0,Flase)
    print(frame_msg)
    '''
    AFRChannelMask= c_int32(0)
    AFRBaseCycle= c_int32(0)
    AFRCycleRepetition= c_int32(0)
    AFRIsStartupFrame= c_bool()
    AFRSlotId= c_int32(0)
    AFRCycleMask= c_int64(0)
    ASignalCount= c_int32(0)
    AFRDLC = c_int32(0)
    AName = POINTER(POINTER(c_char))()
    AComment= POINTER(POINTER(c_char))()
    ret = dll.tsdb_get_flexray_frame_properties_by_index_verbose(ADBIndex,AECUIndex,AFrameIndex,AIsTx,byref(AFRChannelMask),byref(AFRBaseCycle),byref(AFRCycleRepetition),byref(AFRIsStartupFrame),byref(AFRSlotId),byref(AFRCycleMask),byref(ASignalCount),byref(AFRDLC),byref(AName),byref(AComment))
    if ret ==0:
        try:
            AComment = string_at(AComment).decode('utf8')
        except:
            AComment = ''
        return AFRChannelMask,AFRBaseCycle,AFRCycleRepetition,AFRIsStartupFrame,AFRSlotId,AFRCycleMask,ASignalCount,AFRDLC,string_at(AName).decode('utf8'),AComment
    print(tsapp_get_error_description(ret)) 
    return AFRChannelMask,AFRBaseCycle,AFRCycleRepetition,AFRIsStartupFrame,AFRSlotId,AFRCycleMask,ASignalCount,AFRDLC,string_at(AName).decode('utf8'),AComment

# 通过地址获取数据库signal信息
def tsdb_get_flexray_signal_properties_by_address_verbose(AAddr:str):
    """
    signal_msg =  app.tsdb_get_flexray_signal_properties_by_address_verbose(b"0/network1/ecu1/frame1/signal1")
    print(signal_msg)
    """
    if not isinstance(AAddr,bytes):
        AAddr = bytes(AAddr)
    ADBIndex= c_int32(0)
    AECUIndex= c_int32(0)
    AFrameIndex= c_int32(0)
    ASignalIndex = c_int32(0)
    AIsTx= c_bool()
    ASignalType = c_int(0)
    ACompuMethod = c_int(0)
    AIsIntel = c_bool()
    AStartBit = c_int32(0)
    AUpdateBit = c_int32(0)
    ALength = c_int32(0)
    AFactor = c_double(0)
    AOffset = c_double(0)
    AInitValue = c_double(0)
    AName = POINTER(POINTER(c_char))()
    AComment= POINTER(POINTER(c_char))()

    ret = dll.tsdb_get_flexray_signal_properties_by_address_verbose(AAddr,byref(ADBIndex),byref(AECUIndex),byref(AFrameIndex),byref(ASignalIndex),byref(AIsTx),byref(ASignalType),byref(ACompuMethod),byref(AIsIntel),byref(AStartBit),byref(AUpdateBit),byref(ALength),byref(AFactor),byref(AOffset),byref(AInitValue),byref(AName),byref(AComment))
    if ret ==0:
        try:
            # AName = string_at(AName).encode('utf8')
            AComment = string_at(AComment).decode('utf8')
        except:
            AComment = ''
        return ADBIndex,AECUIndex,AFrameIndex,ASignalIndex,AIsTx,ASignalType,ACompuMethod,AIsIntel,AStartBit,AUpdateBit,ALength,AFactor,AOffset,AInitValue,string_at(AName).decode('utf8'),AComment
    print(tsapp_get_error_description(ret))
    return ADBIndex,AECUIndex,AFrameIndex,ASignalIndex,AIsTx,ASignalType,ACompuMethod,AIsIntel,AStartBit,AUpdateBit,ALength,AFactor,AOffset,AInitValue,AName,AComment


# 通过索引获取数据库signal信息
def tsdb_get_flexray_signal_properties_by_index_verbose(ADBIndex:c_int32,AECUIndex:c_int32,AFrameIndex:c_int32,ASignalIndex:c_int32,AIsTx:c_bool):
    """
    signal_msg =  app.tsdb_get_flexray_signal_properties_by_index_verbose(0,0,0,0,Flase)
    print(signal_msg)
    """
    ASignalType = c_int(0)
    ACompuMethod = c_int(0)
    AIsIntel = c_bool()
    AStartBit = c_int32(0)
    AUpdateBit = c_int32(0)
    ALength = c_int32(0)
    AFactor = c_double(0)
    AOffset = c_double(0)
    AInitValue = c_double(0)
    AName = POINTER(POINTER(c_char))()
    AComment= POINTER(POINTER(c_char))()

    ret = dll.tsdb_get_flexray_signal_properties_by_index_verbose(ADBIndex,AECUIndex,AFrameIndex,ASignalIndex,AIsTx,byref(ASignalType),byref(ACompuMethod),byref(AIsIntel),byref(AStartBit),byref(AUpdateBit),byref(ALength),byref(AFactor),byref(AOffset),byref(AInitValue),byref(AName),byref(AComment))
    try:
        # AName = string_at(AName).decode('utf8')
        AComment = string_at(AComment).decode('utf8')
    except:
        AComment = ''
        # AName = ''
        # print(AName)
    if ret ==0:
        return ASignalType,ACompuMethod,AIsIntel,AStartBit,AUpdateBit,ALength,AFactor,AOffset,AInitValue,string_at(AName).decode('utf8'),AComment
    print(tsapp_get_error_description(ret))
    return ASignalType,ACompuMethod,AIsIntel,AStartBit,AUpdateBit,ALength,AFactor,AOffset,AInitValue,AName,AComment



# 启动flexray rbs
def tscom_flexray_rbs_start():
    return dll.tscom_flexray_rbs_start()

# 停止flexray rbs
def tscom_flexray_rbs_stop():
    return dll.tscom_flexray_rbs_stop()

# flexray rbs是否启动
def tscom_flexray_rbs_is_running():
    AIsRunning = c_bool()
    ret = dll.tscom_flexray_rbs_is_running(byref(AIsRunning))
    if ret == 0 :
        return AIsRunning
    return tsapp_get_error_description(ret)

# flexray rbs设置
def tscom_flexray_rbs_configure(AAutoStart:c_bool,AAutoSendOnModification:c_bool,AActivateECUSimulation:c_bool,AInitValueOptions:c_int):
    '''
    //参数1 :是否自动启动rbs
    //参数2 :是否自动发送
    //参数3 :是否激活ECU仿真
    //参数4 :初始值选择
    tscom_flexray_rbs_configure(False,False,False,0)
    '''
    return dll.tscom_flexray_rbs_configure(AAutoStart,AAutoSendOnModification,AActivateECUSimulation,AInitValueOptions)

# 是否激活所以flexray rbs cluster 并包括所有子节点
def tscom_flexray_rbs_activate_all_clusters(AEnable:c_bool,AIncludingChildren:c_bool):
    """tscom_flexray_rbs_activate_all_clusters(True,False)"""
    return dll.tscc_flexray_rbs_activate_all_clusters(AEnable,AIncludingChildren)

# 通过name激活cluster 并是否包括子节点
def tscom_flexray_rbs_activate_cluster_by_name(AIdxChn:c_int,AEnable:c_bool,AClusterName:bytes,AIncludingChildren:c_bool):
    """tscom_flexray_rbs_activate_cluster_by_name(0,True,b"Network1",False)"""
    return dll.tscom_flexray_rbs_activate_cluster_by_name(AIdxChn,AEnable,AClusterName,AIncludingChildren)

# 通过name激活ecu 并是否包括子节点
def tscom_flexray_rbs_activate_ecu_by_name(AIdxChn:c_int,AEnable:c_bool,AClusterName:bytes,AECUName:bytes,AIncludingChildren:c_bool):
    """tscom_flexray_rbs_activate_ecu_by_name(0,True,b"Network1",b"ECU1",False)"""
    return dll.tscom_flexray_rbs_activate_ecu_by_name(AIdxChn,AEnable,AClusterName,AECUName,AIncludingChildren)

# 通过name激活msg 
def tscom_flexray_rbs_activate_frame_by_name(AIdxChn:c_int,AEnable:c_bool,AClusterName:bytes,AECUName:bytes,AFrameName:bytes):
    """tscom_flexray_rbs_activate_frame_by_name(0,True,b"Network1",b"ECU1",b'Frame1')"""
    return dll.tscom_flexray_rbs_activate_frame_by_name(AIdxChn,AEnable,AClusterName,AECUName,AFrameName)

# 通过element 获取信号值
def tscom_flexray_rbs_get_signal_value_by_element(AIdxChn:c_int32,AClusterName:bytes,AECUName:bytes,AFrameName:bytes,ASignalName:bytes):
    """
    value = tscom_flexray_rbs_get_signal_value_by_element(0,b'PowerTrain',b'BSC',b'BackLightInfo',b'BrakeLight')
    print(value)
    """
    if not isinstance(AClusterName,bytes):
        AClusterName = bytes(AClusterName)
    if not isinstance(AECUName,bytes):
        AECUName = bytes(AECUName)
    if not isinstance(AFrameName,bytes):
        AFrameName = bytes(AFrameName)
    if not isinstance(ASignalName,bytes):
        ASignalName = bytes(ASignalName)
    AValue = c_double(0)
    ret = dll.tscom_flexray_rbs_get_signal_value_by_element(AIdxChn,AClusterName,AECUName,AFrameName,ASignalName,byref(AValue))
    if ret == 0:
        return AValue.value
    return tsapp_get_error_description(ret)

# 通过地址 获取信号值
def tscom_flexray_rbs_get_signal_value_by_address(AAddr:bytes):
    """
    TSMasterAPI.tscom_flexray_rbs_get_signal_value_by_address(b'0/PowerTrain/BSC/BackLightInfo/BrakeLight')
    """
    AValue = c_double(0)
    ret = dll.tscom_flexray_rbs_get_signal_value_by_address(AAddr,byref(AValue))
    if ret == 0:
        return AValue.value
    return tsapp_get_error_description(ret)

# 通过element 设置信号值
def tscom_flexray_rbs_set_signal_value_by_element(AIdxChn:c_int32,AClusterName:bytes,AECUName:bytes,AFrameName:bytes,ASignalName:bytes,AValue:c_double):
    """
    value = c_double(1.0)
    tscom_flexray_rbs_set_signal_value_by_element(0,b'PowerTrain',b'BSC',b'BackLightInfo',b'BrakeLight'，value)
    """
    if not isinstance(AClusterName,bytes):
        AClusterName = bytes(AClusterName)
    if not isinstance(AECUName,bytes):
        AECUName = bytes(AECUName)
    if not isinstance(AFrameName,bytes):
        AFrameName = bytes(AFrameName)
    if not isinstance(ASignalName,bytes):
        ASignalName = bytes(ASignalName)
    return dll.tscom_flexray_rbs_set_signal_value_by_element(AIdxChn,AClusterName,AECUName,AFrameName,ASignalName,AValue)

# 通过地址 设置信号值
def tscom_flexray_rbs_set_signal_value_by_address(AAddr:bytes,AValue:c_double):
    # if not isinstance(AAddr,bytes):
    #     AAddr = bytes(AAddr)
    """
    value = c_double(1.0)
    tscom_flexray_rbs_set_signal_value_by_element(0,b'PowerTrain',b'BSC',b'BackLightInfo',b'BrakeLight'，value)
    """
    return dll.tscom_flexray_rbs_set_signal_value_by_address(AAddr,AValue)

# 使能/失能flexray rbs功能
def tscom_flexray_rbs_enable(AEnable:c_bool):
    """
    tscom_flexray_rbs_enable(True)
    tscom_flexray_rbs_enable(False)
    """
    return dll.tscom_flexray_rbs_enable(AEnable)

# 开始信号改值批处理
def tscom_flexray_rbs_batch_set_start():
    return dll.tscom_flexray_rbs_batch_set_start()

# 结束信号该值批处理
def tscom_flexray_rbs_batch_set_end():
    return dll.tscom_flexray_rbs_batch_set_end()

# 设置信号值
def tscom_flexray_rbs_batch_set_signal(AAddr:bytes,AValue:c_double):
    """
    启动信号批处理集操作，在此调用之后，所有信号设置都被缓存，直到调用can_rbs_batch_set_end，这确保了当设置其中的多个信号时只触发一帧
    tscom_flexray_rbs_batch_set_start();
    // message will not be triggered before can_rbs_batch_set_end
    tscom_flexray_rbs_batch_set_signal(b"0/cluster1/ecu1/frame1/sgn1", c_double(1.2));
    tscom_flexray_rbs_batch_set_signal(b"0/cluster1/ecu1/frame1/sgn2", c_double(3.4));
    // ...
    tscom_flexray_rbs_batch_set_end();
    """
    if not isinstance(AAddr,bytes):
        AAddr = bytes(AAddr)
    return dll.tscom_flexray_rbs_batch_set_signal(AAddr,AValue)

# 设置frame为tx或rx
def tscom_flexray_rbs_set_frame_direction(AIdxChn:c_int32,AIsTx:c_bool,AClusterName:bytes,AECUName:bytes,AFrameName:bytes):
    '''
    # 设置Cluster1 ECU1 Frame1 为发送报文
    tscom_flexray_rbs_set_frame_direction(CHNIdx.CH1, True, b"Cluster1", b"ECU1", b"Frame1")
    '''
    if not isinstance(AClusterName,bytes):
        AClusterName = bytes(AClusterName)
    if not isinstance(AECUName,bytes):
        AECUName = bytes(AECUName)
    if not isinstance(AFrameName,bytes):
        AFrameName = bytes(AFrameName)

    return dll.tscom_flexray_rbs_set_frame_direction(AIdxChn,AIsTx,AClusterName,AECUName,AFrameName)

# 设置信号为normal信号
def tscom_flexray_rbs_set_normal_signal(ASymbolAddress:bytes):
    """
    tscom_flexray_rbs_set_normal_signal(b"0/Cluster1/ecu1/frame1/signal1")
    """
    if not isinstance(ASymbolAddress,bytes):
        ASymbolAddress = bytes(ASymbolAddress)
    return dll.tscom_flexray_rbs_set_normal_signal(ASymbolAddress)

# 设置信号为rc信号
def tscom_flexray_rbs_set_rc_signal(ASymbolAddress:bytes):
    """
    tscom_flexray_rbs_set_rc_signal(b"0/Cluster1/ecu1/frame1/signal1")
    """
    if not isinstance(ASymbolAddress,bytes):
        ASymbolAddress = bytes(ASymbolAddress)
    return dll.tscom_flexray_rbs_set_rc_signal(ASymbolAddress)

# 设置rc信号值的限定范围
def tscom_flexray_rbs_set_rc_signal_with_limit(ASymbolAddress:bytes,ALowerLimit:c_int32,AUpperLimit:c_int32):
    """
    tscom_flexray_rbs_set_rc_signal_with_limit(b"0/Cluster1/ecu1/frame1/signal1",c_int32(0),c_int32(14))
    """
    if not isinstance(ASymbolAddress,bytes):
        ASymbolAddress = bytes(ASymbolAddress)
    return dll.tscom_flexray_rbs_set_rc_signal(ASymbolAddress,ALowerLimit,AUpperLimit)

# 设置信号为crc信号
def tscom_flexray_rbs_set_crc_signal(ASymbolAddress:bytes,AAlgorithmName:bytes,AIdxByteStart:c_int32,AByteCount:c_int32):
    """
    tscom_flexray_rbs_set_crc_signal(b"0/Cluster1/ecu1/frame1/signal1",b"mp.crc8",c_int32(0),c_int32(2))
    """
    if not isinstance(ASymbolAddress,bytes):
        ASymbolAddress = bytes(ASymbolAddress)
    if not isinstance(AAlgorithmName,bytes):
        AAlgorithmName = bytes(AAlgorithmName)
    return dll.tscom_flexray_rbs_set_crc_signal(ASymbolAddress,AAlgorithmName,AIdxByteStart,AByteCount)

#Flexray config 
def tsflexray_set_controller_frametrigger(ANodeIndex: c_uint,
                                        AControllerConfig: dll.TLIBFlexray_controller_config,
                                        AFrameLengthArray: bytearray,
                                        AFrameNum: c_int, AFrameTrigger: dll.TLIBTrigger_def,AFrameTriggerNum: c_int,
                                        ATimeoutMs: c_int):
    
    r = dll.tsflexray_set_controller_frametrigger(ANodeIndex, byref(AControllerConfig),
                                                AFrameLengthArray, AFrameNum, AFrameTrigger,
                                                AFrameTriggerNum, ATimeoutMs)
    return r


#Flexray 回调事件

# 注册 flexray 发送接收事件
def tsapp_register_event_flexray(obj:c_int32,FUNC:dll.TFlexRayQueueEvent_Win32):
    """
    obj = c_int32(0)
    def Flexray_RX(obj,AFlexray):
    '''
    回调事件 发送完成事件 接受事件 都在该函数中实现
    '''
    #(16,0,2)
    if(AFlexray.contents.FSlotId == 16 and AFlexray.contents.FCycleNumber%2==0):
        # ret = tsapp_transmit_flexray_async(AFlexray)
        # print(ret)
        pass
    On_Flexray = dll.TFlexRayQueueEvent_Win32(Flexray_RX)
    tsapp_register_event_flexray(obj,On_Flexray)
    """
    return dll.tsapp_register_event_flexray(byref(obj),FUNC)

# 注销 flexray 发送接收事件
def tsapp_unregister_event_flexray(obj:c_int32,FUNC:dll.TFlexRayQueueEvent_Win32):
    """
    obj = c_int32(0)
    def Flexray_RX(obj,AFlexray):
    '''
    回调事件 发送完成事件 接受事件 都在该函数中实现
    '''
    #(16,0,2)
    if(AFlexray.contents.FSlotId == 16 and AFlexray.contents.FCycleNumber%2==0):
        # ret = tsapp_transmit_flexray_async(AFlexray)
        # print(ret)
        pass
    On_Flexray = dll.TFlexRayQueueEvent_Win32(Flexray_RX)
    tsapp_register_event_flexray(obj,On_Flexray)
    tsapp_unregister_event_flexray(obj,On_Flexray)
    """
    return dll.tsapp_unregister_event_flexray(byref(obj),FUNC)

# 注销 所有 flexray 发送接收事件
def tsapp_unregister_events_flexray(obj:c_int32):
    """
    obj = c_int32(0)
    def Flexray_RX(obj,AFlexray):
    '''
    回调事件 发送完成事件 接受事件 都在该函数中实现
    '''
    #(16,0,2)
    if(AFlexray.contents.FSlotId == 16 and AFlexray.contents.FCycleNumber%2==0):
        # ret = tsapp_transmit_flexray_async(AFlexray)
        # print(ret)
        pass
    On_Flexray = dll.TFlexRayQueueEvent_Win32(Flexray_RX)
    tsapp_register_event_flexray(obj,On_Flexray)
    tsapp_unregister_events_flexray(obj)
    """
    return dll.tsapp_unregister_events_flexray(byref(obj))

# 注册flexray预发送事件
def tsapp_register_pretx_event_flexray(obj:c_int32,FUNC:dll.TFlexRayQueueEvent_Win32):
    """
    obj = c_int32(0)
    def Flexray_RX(obj,AFlexray):
    '''
    回调事件 发送完成事件 接受事件 都在该函数中实现
    '''
    #(16,0,2)
    if(AFlexray.contents.FSlotId == 16 and AFlexray.contents.FCycleNumber%2==0):
        # ret = tsapp_transmit_flexray_async(AFlexray)
        # print(ret)
        pass
    On_Flexray = dll.TFlexRayQueueEvent_Win32(Flexray_RX)
    tsapp_register_pretx_event_flexray(obj,On_Flexray)
    """
    return dll.tsapp_register_pretx_event_flexray(byref(obj),FUNC)

# 注销flexray预发送事件
def tsapp_unregister_pretx_event_flexray(obj:c_int32,FUNC:dll.TFlexRayQueueEvent_Win32):
    """
    obj = c_int32(0)
    def Flexray_RX(obj,AFlexray):
    '''
    回调事件 发送完成事件 接受事件 都在该函数中实现
    '''
    #(16,0,2)
    if(AFlexray.contents.FSlotId == 16 and AFlexray.contents.FCycleNumber%2==0):
        # ret = tsapp_transmit_flexray_async(AFlexray)
        # print(ret)
        pass
    On_Flexray = dll.TFlexRayQueueEvent_Win32(Flexray_RX)
    tsapp_register_pretx_event_flexray(obj,On_Flexray)
    tsapp_unregister_pretx_event_flexray(obj,On_Flexray)
    """
    return dll.tsapp_unregister_pretx_event_flexray(byref(obj),FUNC)

# 注销flexray所有预发送事件
def tsapp_unregister_pretx_events_flexray(obj:c_int32):
    """
    obj = c_int32(0)
    def Flexray_RX(obj,AFlexray):
    '''
    回调事件 发送完成事件 接受事件 都在该函数中实现
    '''
    #(16,0,2)
    if(AFlexray.contents.FSlotId == 16 and AFlexray.contents.FCycleNumber%2==0):
        # ret = tsapp_transmit_flexray_async(AFlexray)
        # print(ret)
        pass
    On_Flexray = dll.TFlexRayQueueEvent_Win32(Flexray_RX)
    tsapp_register_pretx_event_flexray(obj,On_Flexray)
    tsapp_unregister_pretx_events_flexray(obj)
    """
    return dll.tsapp_unregister_pretx_events_flexray(byref(obj))

# 获取数据库中信号定义
def tscom_flexray_get_signal_definition(ASignalAddress:bytes):
    """
    TSignal_ = tscom_flexray_get_signal_definition(b'0/PowerTrain/BSC/BackLightInfo/BrakeLight')
    print(TSignal_)
    """
    ASignalDef=dll.TMPFlexRaySignal()
    ret = dll.tscom_flexray_get_signal_definition(ASignalAddress,byref(ASignalDef))
    if ret == 0:
        return ASignalDef
    return None



def tscom_get_flexray_signal_value(AFlexRaySignal:dll.TMPFlexRaySignal,AData:bytes):
    '''
    # 设置flexray信号值
    TSignal_ = tscom_flexray_get_signal_definition(b'0/PowerTrain/BSC/BackLightInfo/BrakeLight')
    value= c_double(1.0)
    tscom_flexray_set_signal_value_in_raw_frame(TSignal_,bytes(AFlexray.contents.FData),value)
    '''
    return dll.tscom_get_flexray_signal_value(byref(AFlexRaySignal),AData)

def tscom_set_flexray_signal_value(AFlexRaySignal:dll.TMPFlexRaySignal,AData:bytes,AValue:c_double):
    '''
    # 设置flexray信号值
    TSignal_ = tscom_flexray_get_signal_definition(b'0/PowerTrain/BSC/BackLightInfo/BrakeLight')
    value= c_double(1.0)
    tscom_flexray_set_signal_value_in_raw_frame(TSignal_,bytes(AFlexray.contents.FData),value)
    '''
    return dll.tscom_set_flexray_signal_value(byref(AFlexRaySignal),AData,AValue)

# Flexray db info 
# 载入数据库
def tsdb_load_flexray_db(AFliepath:str,ASupportedChannels:str,AId:c_int32):
    """
    AId = c_int32(0)
    tsdb_load_flexray_db(b"C:/1.xml",b'0,1',AId)
    """
    if not isinstance(AFliepath,bytes):
        AFliepath = bytes(AFliepath)
    if not isinstance(ASupportedChannels,bytes):
        ASupportedChannels = bytes(ASupportedChannels)
    ret = dll.tsdb_load_flexray_db(AFliepath,ASupportedChannels,byref(AId))
    # if ret == 0:
    #     try:
    #         ret = flexray_db_parse((AId.value-1)) 
    #     except:
    #         return ret  
    return ret

# 卸载数据库
def tsdb_unload_flexray_db(AId:c_int32):
    """
    AId = c_int32(0)
    tsdb_load_flexray_db(b"C:/1.xml",b'0,1',AId)
    tsdb_unload_flexray_db(AId)
    """
    return dll.tsdb_unload_flexray_db(AId)

# 卸载所有数据库 
def tsdb_unload_flexray_dbs():
    """
    AId = c_int32(0)
    tsdb_load_flexray_db(b"C:/1.xml",b'0,1',AId)
    tsdb_unload_flexray_dbs()
    """
    return dll.tsdb_unload_flexray_dbs()

# 获取加载的数据库数量
def tsdb_get_flexray_db_count(Acount:c_int32):
    """
    Acount = c_int32(0)
    tsdb_get_flexray_db_count(Acount)
    """
    return dll.tsdb_get_flexray_db_count(byref(Acount))

# 通过索引获取数据库id
def tsdb_get_flexray_db_id(AIndex:c_int32):
    """
    Args:
        获取AIndex数据库的ID

    Returns:
        DBID  or  error description
    
    example:
        Acount = c_int32(0)
        tsdb_get_flexray_db_count(Acount)
        for i in range(0,Acount.value):
            dbid = tsdb_get_flexray_db_id(i)

    """
    Aid = c_int32(0)
    ret = dll.tsdb_get_flexray_db_id(AIndex,byref(Aid))
    if ret == 0 :
        return Aid
    return tsapp_get_error_description(ret)

def tsdb_get_flexray_db_properties_by_address(AAddr:bytes,Avalue:dll.TMPDBProperties):
    """
    Args:
        获取数据库信息
    Returns:
        error code  0:ok  other:error
    
    example:
        db = dll.TMPDBProperties()
        tsdb_get_flexray_db_properties_by_address(b'0/network1',db)

    """
    return dll.tsdb_get_flexray_db_properties_by_address(AAddr,byref(Avalue))

def tsdb_get_flexray_db_properties_by_index(Avalue:dll.TMPDBProperties):
    """
    Args:
        获取数据库信息
    Returns:
        error code  0:ok  other:error
    
    example:
        db = dll.TMPDBProperties()
        db.FDBIndex = 0
        tsdb_get_flexray_db_properties_by_index(db)
    """
    return dll.tsdb_get_flexray_db_properties_by_index(byref(Avalue))

def tsdb_get_flexray_db_ecu_properties_by_address(AAddr:bytes,Avalue:dll.TMPDBECUProperties):
    """
    Args:
        获取数据库ecu信息
    Returns:
        error code  0:ok  other:error
    
    example:
        db_ecu = dll.TMPDBECUProperties()
        tsdb_get_flexray_db_ecu_properties_by_address(b"0/network1/ecu1",db_ecu)
    """
    return dll.tsdb_get_flexray_db_ecu_properties_by_address(AAddr,byref(Avalue))

def tsdb_get_flexray_db_ecu_properties_by_index(Avalue:dll.TMPDBECUProperties):
    """
    Args:
        获取数据库ecu信息
    Returns:
        error code  0:ok  other:error
    
    example:
        db_ecu = dll.TMPDBECUProperties()
        db_ecu.FDBIndex = 0
        db_ecu.FECUIndex = 0
        tsdb_get_flexray_db_ecu_properties_by_index(db_ecu)
    """
    return dll.tsdb_get_flexray_db_ecu_properties_by_index(byref(Avalue))

def tsdb_get_flexray_db_frame_properties_by_address(AAddr:bytes,Avalue:dll.TMPDBFrameProperties):
    """
    Args:
        获取数据库frame信息
    Returns:
        error code  0:ok  other:error
    
    example:
        db_ecu_frame = dll.TMPDBFrameProperties()
        tsdb_get_flexray_db_frame_properties_by_address(b"0/network1/ecu1/frame1",db_ecu_frame)
    """
    return dll.tsdb_get_flexray_db_frame_properties_by_address(AAddr,byref(Avalue))

def tsdb_get_flexray_db_frame_properties_by_index(Avalue:dll.TMPDBECUProperties):
    """
    Args:
        获取数据库frame信息
    Returns:
        error code  0:ok  other:error
    
    example:
        db_ecu_frame = dll.TMPDBFrameProperties()
        db_ecu_frame.FDBIndex = 0
        db_ecu_frame.FECUIndex = 0
        db_ecu_frame.FFrameIndex = 0
        db_ecu_frame.FIsTx = 1
        tsdb_get_flexray_db_frame_properties_by_index(db_ecu_frame)
    """
    return dll.tsdb_get_flexray_db_frame_properties_by_index(byref(Avalue))

def tsdb_get_flexray_db_frame_properties_by_db_index(AIdxDB:c_int32,AIndex:c_int32,Avalue:dll.TMPDBFrameProperties):
    """
    Args:
        获取数据库frame信息
    Returns:
        error code  0:ok  other:error
    example:
        db_ecu_frame = dll.TMPDBFrameProperties()
        tsdb_get_flexray_db_frame_properties_by_db_index(0,0,db_ecu_frame)
    """
    return dll.tsdb_get_flexray_db_frame_properties_by_db_index(AIdxDB,AIndex,byref(Avalue))


def tsdb_get_flexray_db_signal_properties_by_address(AAddr:bytes,Avalue:dll.TMPDBSignalProperties):
    """
    Args:
        获取数据库signal信息
    Returns:
        error code  0:ok  other:error
    
    example:
        db_ecu_frame_signal = dll.TMPDBSignalProperties()
        tsdb_get_flexray_db_signal_properties_by_address(b"0/network1/ecu1/frame1/signal1",db_ecu_frame_signal)
    """
    return dll.tsdb_get_flexray_db_signal_properties_by_address(AAddr,byref(Avalue))

def tsdb_get_flexray_db_signal_properties_by_index(Avalue:dll.TMPDBSignalProperties):
    """
    Args:
        获取数据库signal信息
    Returns:
        error code  0:ok  other:error
    
    example:
        db_ecu_frame_signal = dll.TMPDBSignalProperties()
        db_ecu_frame_signal.FDBIndex = 0
        db_ecu_frame_signal.FECUIndex = 0
        db_ecu_frame_signal.FFrameIndex = 0
        db_ecu_frame_signal.FSignalIndex = 0
        db_ecu_frame_signal.FIsTx = 1
        tsdb_get_flexray_db_signal_properties_by_index(db_ecu_frame_signal)
    """
    return dll.tsdb_get_flexray_db_signal_properties_by_index(byref(Avalue))

# def tsdb_get_flexray_db_signal_properties_by_db_index(AIdxDB:c_int32,AIndex:c_int32,Avalue:dll.TMPDBSignalProperties):
#     """
#     Args:
#         获取数据库frame信息
#     Returns:
#         error code  0:ok  other:error
#     example:
#         db_ecu_frame_signal = dll.TMPDBSignalProperties()
#         tsdb_get_flexray_db_signal_properties_by_db_index(0,0,db_ecu_frame_signal)
#     """
#     return dll.tsdb_get_flexray_db_signal_properties_by_db_index(AIdxDB,AIndex,byref(Avalue))

def tsdb_get_flexray_db_signal_properties_by_frame_index(AIdxDB:c_int32,Frameidx:c_int32,AIndex:c_int32,Avalue:dll.TMPDBSignalProperties):
    """
    Args:
        获取数据库frame信息
    Returns:
        error code  0:ok  other:error
    example:
        db_ecu_frame_signal = dll.TMPDBSignalProperties()
        tsdb_get_flexray_db_signal_properties_by_frame_index(0,0,0,db_ecu_frame_signal)
    """
    return dll.tsdb_get_flexray_db_signal_properties_by_frame_index(AIdxDB,Frameidx,AIndex,byref(Avalue))

# can db info

# 加载dbc并绑定通道 注意idDBC 必须是c_uint32类型
def tsdb_load_can_db(AFliepath:str,ASupportedChannels:str,AId:c_int32):
    """
    AId = c_int32(0)
    tsdb_load_can_db(b"C:/1.xml",b'0,1',AId)
    """
    if not isinstance(AFliepath,bytes):
        AFliepath = bytes(AFliepath)
    if not isinstance(ASupportedChannels,bytes):
        ASupportedChannels = bytes(ASupportedChannels)
    ret = dll.tsdb_load_can_db(AFliepath,ASupportedChannels,byref(AId))
    # if ret == 0:
    #     try:
    #         ret = flexray_db_parse((AId.value-1)) 
    #     except:
    #         return ret  
    return ret

# 卸载数据库
def tsdb_unload_can_db(AId:c_int32):
    """
    AId = c_int32(0)
    tsdb_load_can_db(b"C:/1.xml",b'0,1',AId)
    tsdb_unload_can_db(AId)
    """
    return dll.tsdb_unload_can_db(AId)

# 卸载所有数据库 
def tsdb_unload_can_dbs():
    """
    AId = c_int32(0)
    tsdb_load_can_db(b"C:/1.xml",b'0,1',AId)
    tsdb_unload_can_dbs()
    """
    return dll.tsdb_unload_can_dbs()

# 获取加载的数据库数量
def tsdb_get_can_db_count(Acount:c_int32):
    """
    Acount = c_int32(0)
    tsdb_get_can_db_count(Acount)
    """
    return dll.tsdb_get_can_db_count(byref(Acount))

# 通过索引获取数据库id
def tsdb_get_can_db_id(AIndex:c_int32):
    """
    Args:
        获取AIndex数据库的ID

    Returns:
        DBID  or  error description
    
    example:
        Acount = c_int32(0)
        tsdb_get_can_db_count(Acount)
        for i in range(0,Acount.value):
            dbid = tsdb_get_can_db_id(i)

    """
    Aid = c_int32(0)
    ret = dll.tsdb_get_can_db_id(AIndex,byref(Aid))
    if ret == 0 :
        return Aid
    return tsapp_get_error_description(ret)

def tsdb_get_can_db_properties_by_address(AAddr:bytes,Avalue:dll.TMPDBProperties):
    """
    Args:
        获取数据库信息
    Returns:
        error code  0:ok  other:error
    
    example:
        db = dll.TMPDBProperties()
        tsdb_get_can_db_properties_by_address(b'0/network1',db)

    """
    return dll.tsdb_get_can_db_properties_by_address(AAddr,byref(Avalue))

def tsdb_get_can_db_properties_by_index(Avalue:dll.TMPDBProperties):
    """
    Args:
        获取数据库信息
    Returns:
        error code  0:ok  other:error
    
    example:
        db = dll.TMPDBProperties()
        db.FDBIndex = 0
        tsdb_get_can_db_properties_by_index(db)
    """
    return dll.tsdb_get_can_db_properties_by_index(byref(Avalue))

def tsdb_get_can_db_ecu_properties_by_address(AAddr:bytes,Avalue:dll.TMPDBECUProperties):
    """
    Args:
        获取数据库ecu信息
    Returns:
        error code  0:ok  other:error
    
    example:
        db_ecu = dll.TMPDBECUProperties()
        tsdb_get_can_db_ecu_properties_by_address(b"0/network1/ecu1",db_ecu)
    """
    return dll.tsdb_get_can_db_ecu_properties_by_address(AAddr,byref(Avalue))

def tsdb_get_can_db_ecu_properties_by_index(Avalue:dll.TMPDBECUProperties):
    """
    Args:
        获取数据库ecu信息
    Returns:
        error code  0:ok  other:error
    
    example:
        db_ecu = dll.TMPDBECUProperties()
        db_ecu.FDBIndex = 0
        db_ecu.FECUIndex = 0
        tsdb_get_can_db_ecu_properties_by_index(db_ecu)
    """
    return dll.tsdb_get_can_db_ecu_properties_by_index(byref(Avalue))

def tsdb_get_can_db_frame_properties_by_address(AAddr:bytes,Avalue:dll.TMPDBFrameProperties):
    """
    Args:
        获取数据库frame信息
    Returns:
        error code  0:ok  other:error
    
    example:
        db_ecu_frame = dll.TMPDBFrameProperties()
        tsdb_get_can_db_frame_properties_by_address(b"0/network1/ecu1/frame1",db_ecu_frame)
    """
    return dll.tsdb_get_can_db_frame_properties_by_address(AAddr,byref(Avalue))

def tsdb_get_can_db_frame_properties_by_index(Avalue:dll.TMPDBECUProperties):
    """
    Args:
        获取数据库frame信息
    Returns:
        error code  0:ok  other:error
    
    example:
        db_ecu_frame = dll.TMPDBFrameProperties()
        db_ecu_frame.FDBIndex = 0
        db_ecu_frame.FECUIndex = 0
        db_ecu_frame.FFrameIndex = 0
        db_ecu_frame.FIsTx = 1
        tsdb_get_can_db_frame_properties_by_index(db_ecu_frame)
    """
    return dll.tsdb_get_can_db_frame_properties_by_index(byref(Avalue))

def tsdb_get_can_db_frame_properties_by_db_index(AIdxDB:c_int32,AIndex:c_int32,Avalue:dll.TMPDBFrameProperties):
    """
    Args:
        获取数据库frame信息
    Returns:
        error code  0:ok  other:error
    example:
        db_ecu_frame = dll.TMPDBFrameProperties()
        tsdb_get_can_db_frame_properties_by_db_index(0,0,db_ecu_frame)
    """
    return dll.tsdb_get_can_db_frame_properties_by_db_index(AIdxDB,AIndex,byref(Avalue))


def tsdb_get_can_db_signal_properties_by_address(AAddr:bytes,Avalue:dll.TMPDBSignalProperties):
    """
    Args:
        获取数据库signal信息
    Returns:
        error code  0:ok  other:error
    
    example:
        db_ecu_frame_signal = dll.TMPDBSignalProperties()
        tsdb_get_can_db_signal_properties_by_address(b"0/network1/ecu1/frame1/signal1",db_ecu_frame_signal)
    """
    return dll.tsdb_get_can_db_signal_properties_by_address(AAddr,byref(Avalue))

def tsdb_get_can_db_signal_properties_by_index(Avalue:dll.TMPDBSignalProperties):
    """
    Args:
        获取数据库signal信息
    Returns:
        error code  0:ok  other:error
    
    example:
        db_ecu_frame_signal = dll.TMPDBSignalProperties()
        db_ecu_frame_signal.FDBIndex = 0
        db_ecu_frame_signal.FECUIndex = 0
        db_ecu_frame_signal.FFrameIndex = 0
        db_ecu_frame_signal.FSignalIndex = 0
        db_ecu_frame_signal.FIsTx = 1
        tsdb_get_can_db_signal_properties_by_index(db_ecu_frame_signal)
    """
    return dll.tsdb_get_can_db_signal_properties_by_index(byref(Avalue))

# def tsdb_get_can_db_signal_properties_by_db_index(AIdxDB:c_int32,AIndex:c_int32,Avalue:dll.TMPDBSignalProperties):
#     """
#     Args:
#         获取数据库frame信息
#     Returns:
#         error code  0:ok  other:error
#     example:
#         db_ecu_frame_signal = dll.TMPDBSignalProperties()
#         tsdb_get_can_db_signal_properties_by_db_index(0,0,db_ecu_frame_signal)
#     """
#     return dll.tsdb_get_can_db_signal_properties_by_db_index(AIdxDB,AIndex,byref(Avalue))

def tsdb_get_can_db_signal_properties_by_frame_index(AIdxDB:c_int32,Frameidx:c_int32,AIndex:c_int32,Avalue:dll.TMPDBSignalProperties):
    """
    Args:
        获取数据库frame信息
    Returns:
        error code  0:ok  other:error
    example:
        db_ecu_frame_signal = dll.TMPDBSignalProperties()
        tsdb_get_can_db_signal_properties_by_frame_index(0,0,0,db_ecu_frame_signal)
    """
    return dll.tsdb_get_can_db_signal_properties_by_frame_index(AIdxDB,Frameidx,AIndex,byref(Avalue))

# lin db info
def tsdb_load_lin_db(AFliepath:str,ASupportedChannels:str,AId:c_int32):
    """
    AId = c_int32(0)
    tsdb_load_lin_db(b"C:/1.xml",b'0,1',AId)
    """
    if not isinstance(AFliepath,bytes):
        AFliepath = bytes(AFliepath)
    if not isinstance(ASupportedChannels,bytes):
        ASupportedChannels = bytes(ASupportedChannels)
    ret = dll.tsdb_load_lin_db(AFliepath,ASupportedChannels,byref(AId))
    return ret

# 卸载数据库
def tsdb_unload_lin_db(AId:c_int32):
    """
    AId = c_int32(0)
    tsdb_load_lin_db(b"C:/1.xml",b'0,1',AId)
    tsdb_unload_lin_db(AId)
    """
    return dll.tsdb_unload_lin_db(AId)

# 卸载所有数据库 
def tsdb_unload_lin_dbs():
    """
    AId = c_int32(0)
    tsdb_load_lin_db(b"C:/1.xml",b'0,1',AId)
    tsdb_unload_lin_dbs()
    """
    return dll.tsdb_unload_lin_dbs()

# 获取加载的数据库数量
def tsdb_get_lin_db_count(Acount:c_int32):
    """
    Acount = c_int32(0)
    tsdb_get_lin_db_count(Acount)
    """
    return dll.tsdb_get_lin_db_count(byref(Acount))

# 通过索引获取数据库id
def tsdb_get_lin_db_id(AIndex:c_int32):
    """
    Args:
        获取AIndex数据库的ID

    Returns:
        DBID  or  error description
    
    example:
        Acount = c_int32(0)
        tsdb_get_lin_db_count(Acount)
        for i in range(0,Acount.value):
            dbid = tsdb_get_lin_db_id(i)

    """
    Aid = c_int32(0)
    ret = dll.tsdb_get_lin_db_id(AIndex,byref(Aid))
    if ret == 0 :
        return Aid
    return tsapp_get_error_description(ret)

def tsdb_get_lin_db_properties_by_address(AAddr:bytes,Avalue:dll.TMPDBProperties):
    """
    Args:
        获取数据库信息
    Returns:
        error code  0:ok  other:error
    
    example:
        db = dll.TMPDBProperties()
        tsdb_get_lin_db_properties_by_address(b'0/network1',db)

    """
    return dll.tsdb_get_lin_db_properties_by_address(AAddr,byref(Avalue))

def tsdb_get_lin_db_properties_by_index(Avalue:dll.TMPDBProperties):
    """
    Args:
        获取数据库信息
    Returns:
        error code  0:ok  other:error
    
    example:
        db = dll.TMPDBProperties()
        db.FDBIndex = 0
        tsdb_get_lin_db_properties_by_index(db)
    """
    return dll.tsdb_get_lin_db_properties_by_index(byref(Avalue))

def tsdb_get_lin_db_ecu_properties_by_address(AAddr:bytes,Avalue:dll.TMPDBECUProperties):
    """
    Args:
        获取数据库ecu信息
    Returns:
        error code  0:ok  other:error
    
    example:
        db_ecu = dll.TMPDBECUProperties()
        tsdb_get_lin_db_ecu_properties_by_address(b"0/network1/ecu1",db_ecu)
    """
    return dll.tsdb_get_lin_db_ecu_properties_by_address(AAddr,byref(Avalue))

def tsdb_get_lin_db_ecu_properties_by_index(Avalue:dll.TMPDBECUProperties):
    """
    Args:
        获取数据库ecu信息
    Returns:
        error code  0:ok  other:error
    
    example:
        db_ecu = dll.TMPDBECUProperties()
        db_ecu.FDBIndex = 0
        db_ecu.FECUIndex = 0
        tsdb_get_lin_db_ecu_properties_by_index(db_ecu)
    """
    return dll.tsdb_get_lin_db_ecu_properties_by_index(byref(Avalue))

def tsdb_get_lin_db_frame_properties_by_address(AAddr:bytes,Avalue:dll.TMPDBFrameProperties):
    """
    Args:
        获取数据库frame信息
    Returns:
        error code  0:ok  other:error
    
    example:
        db_ecu_frame = dll.TMPDBFrameProperties()
        tsdb_get_lin_db_frame_properties_by_address(b"0/network1/ecu1/frame1",db_ecu_frame)
    """
    return dll.tsdb_get_lin_db_frame_properties_by_address(AAddr,byref(Avalue))

def tsdb_get_lin_db_frame_properties_by_index(Avalue:dll.TMPDBECUProperties):
    """
    Args:
        获取数据库frame信息
    Returns:
        error code  0:ok  other:error
    
    example:
        db_ecu_frame = dll.TMPDBFrameProperties()
        db_ecu_frame.FDBIndex = 0
        db_ecu_frame.FECUIndex = 0
        db_ecu_frame.FFrameIndex = 0
        db_ecu_frame.FIsTx = 1
        tsdb_get_lin_db_frame_properties_by_index(db_ecu_frame)
    """
    return dll.tsdb_get_lin_db_frame_properties_by_index(byref(Avalue))

def tsdb_get_lin_db_frame_properties_by_db_index(AIdxDB:c_int32,AIndex:c_int32,Avalue:dll.TMPDBFrameProperties):
    """
    Args:
        获取数据库frame信息
    Returns:
        error code  0:ok  other:error
    example:
        db_ecu_frame = dll.TMPDBFrameProperties()
        tsdb_get_lin_db_frame_properties_by_db_index(0,0,db_ecu_frame)
    """
    return dll.tsdb_get_lin_db_frame_properties_by_db_index(AIdxDB,AIndex,byref(Avalue))


def tsdb_get_lin_db_signal_properties_by_address(AAddr:bytes,Avalue:dll.TMPDBSignalProperties):
    """
    Args:
        获取数据库signal信息
    Returns:
        error code  0:ok  other:error
    
    example:
        db_ecu_frame_signal = dll.TMPDBSignalProperties()
        tsdb_get_lin_db_signal_properties_by_address(b"0/network1/ecu1/frame1/signal1",db_ecu_frame_signal)
    """
    return dll.tsdb_get_lin_db_signal_properties_by_address(AAddr,byref(Avalue))

def tsdb_get_lin_db_signal_properties_by_index(Avalue:dll.TMPDBSignalProperties):
    """
    Args:
        获取数据库signal信息
    Returns:
        error code  0:ok  other:error
    
    example:
        db_ecu_frame_signal = dll.TMPDBSignalProperties()
        db_ecu_frame_signal.FDBIndex = 0
        db_ecu_frame_signal.FECUIndex = 0
        db_ecu_frame_signal.FFrameIndex = 0
        db_ecu_frame_signal.FSignalIndex = 0
        db_ecu_frame_signal.FIsTx = 1
        tsdb_get_lin_db_signal_properties_by_index(db_ecu_frame_signal)
    """
    return dll.tsdb_get_lin_db_signal_properties_by_index(byref(Avalue))

# def tsdb_get_lin_db_signal_properties_by_db_index(AIdxDB:c_int32,AIndex:c_int32,Avalue:dll.TMPDBSignalProperties):
#     """
#     Args:
#         获取数据库frame信息
#     Returns:
#         error code  0:ok  other:error
#     example:
#         db_ecu_frame_signal = dll.TMPDBSignalProperties()
#         tsdb_get_lin_db_signal_properties_by_db_index(0,0,db_ecu_frame_signal)
#     """
#     return dll.tsdb_get_lin_db_signal_properties_by_db_index(AIdxDB,AIndex,byref(Avalue))

def tsdb_get_lin_db_signal_properties_by_frame_index(AIdxDB:c_int32,Frameidx:c_int32,AIndex:c_int32,Avalue:dll.TMPDBSignalProperties):
    """
    Args:
        获取数据库frame信息
    Returns:
        error code  0:ok  other:error
    example:
        db_ecu_frame_signal = dll.TMPDBSignalProperties()
        tsdb_get_lin_db_signal_properties_by_frame_index(0,0,0,db_ecu_frame_signal)
    """
    return dll.tsdb_get_lin_db_signal_properties_by_frame_index(AIdxDB,Frameidx,AIndex,byref(Avalue))

# LIN schedule FUNCTION
def tslin_batch_set_schedule_start(AIndex:c_int32):
    return dll.tslin_batch_set_schedule_start(AIndex)

def tslin_batch_set_schedule_end(AIndex:c_int32):
    return dll.tslin_batch_set_schedule_end(AIndex)

def tslin_batch_add_schedule_frame(AIndex:c_int32,Msg:dll.TLIBLIN,ADelayMs:c_uint8):
    return dll.tslin_batch_add_schedule_frame(AIndex,Msg,ADelayMs)

def tslin_clear_schedule_tables(AIndex:c_int32):
    return dll.tslin_clear_schedule_tables(AIndex)

def tslin_switch_runtime_schedule_table(AIndex:c_int32):
    return dll.tslin_switch_runtime_schedule_table(AIndex)

def tslin_switch_idle_schedule_table(AIndex:c_int32):
    return dll.tslin_switch_idle_schedule_table(AIndex)

def tslin_switch_normal_schedule_table(AIndex:c_int32,ASchIndex:dll.s32):
    return dll.tslin_switch_normal_schedule_table(AIndex,ASchIndex)

def tslin_start_lin_channel(AIndex:c_int32):
    return dll.tslin_start_lin_channel(AIndex)

def tslin_stop_lin_channel(AIndex:c_int32):
    return dll.tslin_stop_lin_channel(AIndex)


# ETH Function

def tsapp_set_ethernet_channel_count(ACount:dll.s32):
    return dll.set_ethernet_channel_count(ACount)

def tsapp_get_ethernet_channel_count(ACount:dll.ps32):
    return dll.get_ethernet_channel_count(ACount)

def tsapp_ethernet_channel_compress_mode(ACount:dll.ps32,AOpen:c_bool):
    return dll.tsapp_ethernet_channel_compress_mode(ACount,AOpen)

def tsapp_transmit_ethernet_async(AMsg:dll.PLIBEthernetHeader):
    return dll.tsapp_transmit_ethernet_async(AMsg)

def tsapp_transmit_ethernet_sync(AMsg:dll.PLIBEthernetHeader):
    return dll.tsapp_transmit_ethernet_sync(AMsg)

def tslog_blf_write_ethernet(AMsg:dll.PLIBEthernetHeader):
    return dll.tslog_blf_write_ethernet(AMsg)

def set_flexray_ub_bit_auto_handle(AISAuto:dll.c_bool):
    return dll.set_flexray_ub_bit_auto_handle(AISAuto)

