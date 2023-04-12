from libTOSUN import *
from ctypes import *
configs = [{'FChannel': 0, 'rate_baudrate': 500,
'data_baudrate': 2000, 'enable_120hm': True, 'is_fd': False}, {'FChannel': 1, 'rate_baudrate': 500,
'data_baudrate': 2000, 'enable_120hm': True, 'is_fd': False}, {'FChannel': 2, 'rate_baudrate': 500,
'data_baudrate': 2000, 'enable_120hm': True, 'is_fd': False}, {'FChannel': 3, 'rate_baudrate': 500,
'data_baudrate': 2000, 'enable_120hm': True, 'is_fd': False}]
hwhandle = TSMasterDevice(configs,is_recv_error=True, is_include_tx=True, hwserial=b"")
msg = can.Message(channel=0,arbitration_id=0x1,
is_extended_id=False, is_remote_frame=False, dlc=8, data=[1, 2, 3, 4, 5, 6, 7, 8])
hwhandle.send_msg(msg)
pDiagModuleIndex = c_int32(0) # 为 c 类型 传入的为指针，可以随意赋值，运行下方函数后，会对其赋值
hwhandle.tsdiag_can_create(pDiagModuleIndex, 0, 0, 8, 0x123, True, 0X456, True, 0X789, True)
# r 为函数执行返回值，为 0 表示执行成功
# 非 0 可以使用 hwhandle.tscan_get_error_description(r)获取错误信息
r, respond_data =hwhandle.tstp_can_request_and_get_response(pDiagModuleIndex, [0x10, 0x02])
print(list(respond_data))
hwhandle.shut_down()