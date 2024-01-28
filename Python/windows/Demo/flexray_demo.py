'''
Author: seven 865762826@qq.com
Date: 2023-02-12 18:18:44
LastEditors: seven 865762826@qq.com
LastEditTime: 2023-05-06 16:53:21
'''
import time
import TSMasterAPI
import ctypes

APPName = b'TSMaster'
# TSMasterAPI.initialize_lib_tsmaster(APPName)
TSMasterAPI.initialize_lib_tsmaster_with_project(APPName,b'.\\test')

def e2e_crc8(data):
    polynomial = 0x1d
    initValue = 00^0X00
    for i in range(len(data)):
        initValue = initValue ^ data[i]
        for j in range(8):
            if(initValue & 0x80 == 0x80):
                initValue = ((initValue << 1) & 0xff)
                initValue = initValue ^ polynomial
            else:
                initValue = ((initValue << 1) & 0xff)
    initValue = initValue ^ 0x00
    return initValue&0xff
TSignal_ = TSMasterAPI.TMPFlexRaySignal()
TSMasterAPI.tscom_flexray_get_signal_definition(b'0/PowerTrain/BSC/BackLightInfo/BrakeLight',TSignal_)
# 该函数为回调事件 可以查看报文实时记录
def Flexray_RX(obj,AFlexray):
    '''
    回调事件 发送完成事件 接受事件 都在该函数中实现
    '''
    #(16,0,2)
    if(AFlexray.contents.FSlotId == 16 and AFlexray.contents.FCycleNumber%2==0):
        # ret = TSMasterAPI.tsapp_transmit_flexray_async(AFlexray)
        # print(ret)
        pass
# 该函数为pre_tx函数，即预发送事件
def Flexray_Pre(obj,AFlexray):
    '''
    #UB bit auto set and clear implemented in FlexRay RBS 
    #only calc checksum and crc
    '''
    if(AFlexray.contents.FSlotId == 16 and AFlexray.contents.FCycleNumber%2==0):
        value = TSMasterAPI.tscom_flexray_get_signal_value_in_raw_frame(TSignal_,bytes(AFlexray.contents.FData))
        value += 1
        TSMasterAPI.tscom_flexray_set_signal_value_in_raw_frame(TSignal_,AFlexray.contents.FData,ctypes.c_double(value))
                


On_Flexray = TSMasterAPI.TFlexRayQueueEvent_Win32(Flexray_RX)

on_pre_flexray = TSMasterAPI.TFlexRayQueueEvent_Win32(Flexray_Pre)




TSMasterAPI.tsfifo_enable_receive_fifo()

AID = ctypes.c_int32(0)

obj = ctypes.c_int32(0)

obj1 = ctypes.c_int32(0)

ret =  TSMasterAPI.tsapp_connect()

# # 0/BackboneFR/BBM/BbmBackBoneFr04/BrkSysWarnIndcnReqSec
ret = TSMasterAPI.tscom_flexray_rbs_activate_cluster_by_name(1,True,b"PowerTrain",False)
ret = TSMasterAPI.tscom_flexray_rbs_activate_ecu_by_name(1,True,b"PowerTrain",b"BSC",True)
ret = TSMasterAPI.tscom_flexray_rbs_enable(True)
ret = TSMasterAPI.tscom_flexray_rbs_start()

ret = TSMasterAPI.tsapp_register_event_flexray(obj,On_Flexray)

ret = TSMasterAPI.tsapp_register_pretx_event_flexray(obj1,on_pre_flexray)

print(ret)

time.sleep(3)


# TSMasterAPI.tsfifo_clear_flexray_receive_buffers(0)

AValue = 0.0
while 1:
    key = input()
    if key == 'q':
        break
    elif key == 's':
        TSMasterAPI.tsflexray_start_net(0,1000)
        TSMasterAPI.tsflexray_start_net(1,1000)
    elif key == 'P':
        TSMasterAPI.tsflexray_stop_net(0,1000)
        TSMasterAPI.tsflexray_stop_net(1,1000)
    elif key == '1':
        TSMasterAPI.tsfifo_clear_flexray_receive_buffers(0)
    elif key == '3':
        ACount = ctypes.c_int32(0)
        ret = TSMasterAPI.tsfifo_read_flexray_buffer_frame_count(0,ACount)
        print(ret, '  ',ACount)
    elif key == "4":
        AValue += 1
        if AValue>14:
            AValue = 0.0
        ret = TSMasterAPI.tscom_flexray_rbs_set_signal_value_by_address(b'0/PowerTrain/BSC/BackLightInfo/BrakeLight',ctypes.c_double(AValue))
        print('AValue = ',AValue)
        signal_value =  TSMasterAPI.tscom_flexray_rbs_get_signal_value_by_address(b'0/PowerTrain/BSC/BackLightInfo/BrakeLight')
        print("signal_value = ",signal_value)
ret = TSMasterAPI.tscom_flexray_rbs_enable(False)
ret = TSMasterAPI.tscom_flexray_rbs_stop()    
TSMasterAPI.finalize_lib_tsmaster()
