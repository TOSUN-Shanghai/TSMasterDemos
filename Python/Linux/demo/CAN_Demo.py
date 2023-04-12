'''
Author: seven 865762826@qq.com
Date: 2023-02-17 13:09:40
LastEditors: seven 865762826@qq.com
LastEditTime: 2023-03-24 12:45:53
FilePath: \VSCode_Pro\Python_Pro\python_can\CAN_Demo.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from libTOSUN import *

def on_can_event(ACAN):
    print("回调事件：CAN报文",ACAN.contents)
oncan = OnTx_RxFUNC_CAN(on_can_event)

# TC1016 1 2通道短接为示例 
initialize_lib_tsmaster(True,True)

Hwhandle = c_size_t(0)

tsapp_connect("",Hwhandle)

tsapp_register_event_can(Hwhandle,oncan)

tsapp_configure_baudrate_canfd(Hwhandle,0,c_double(500),c_double(2000),TLIBCANFDControllerType.lfdtISOCAN,TLIBCANFDControllerMode.lfdmNormal,1)

tsapp_configure_baudrate_canfd(Hwhandle,1,c_double(500),c_double(2000),TLIBCANFDControllerType.lfdtISOCAN,TLIBCANFDControllerMode.lfdmNormal,1)

ACAN = TLIBCAN(FIdentifier= 0x123)

# 周期发送
tscan_add_cyclic_msg_can(Hwhandle,ACAN,c_float(100))

ACAN1 = TLIBCAN(FIdentifier= 0x124)

# 周期发送
tscan_add_cyclic_msg_can(Hwhandle,ACAN1,c_float(100))
# 单帧发送

tsapp_transmit_can_async(Hwhandle,ACAN)

ACANbuffer = (TLIBCAN*100)()
size = c_int32(100)

time.sleep(1)
tsfifo_clear_can_receive_buffers(Hwhandle,0)

time.sleep(2)
tsapp_receive_can_msgs(Hwhandle,ACANbuffer,size,0,1)

for i in range(size.value):
    print(ACANbuffer[i])

time.sleep(3)

tsapp_disconnect_all()

finalize_lib_tscan()

