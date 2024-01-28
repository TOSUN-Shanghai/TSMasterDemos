from TSMasterAPI import *
import threading
import inspect
import ctypes
def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")
def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)

def recv_tcp(recvsock,connAddress):
    p = (u8*7000)()
    while True:
        # 阻塞方式 接收udp
        tssocket_recv(0,recvsock,p,7000,0)
        print(f"{connAddress.sa_data.value} : {p.value}")
        # 非阻塞方式 接送udp
        # tssocket_recvfrom(0,sock,p,1400,TS_MSG_DONTWAIT,from_addr,len)
        # time.sleep(0.01)
    

initialize_lib_tsmaster(b"ETHUDPDemo")

tsapp_show_tsmaster_window(b"Hardware",True)

logger = TLogDebuggingInfo()

tssocket_initialize(0, logger)
ipaddr = Tip4_addr_t()
gw = Tip4_addr_t()
netmask = Tip4_addr_t()
# ip address
tssocket_aton(b"192.168.0.50", ipaddr)
# gateway
tssocket_aton(b"192.168.0.1", gw)
# mask
tssocket_aton(b"255.255.255.0", netmask)

macaddr = (u8*6)(1, 2, 3, 4, 5, 50)
# 添加设备 TE1051
ret= tssocket_add_device(0,macaddr, ipaddr,netmask, gw,1500)
# 配置完成后 启动设备
ret = tsapp_connect()
# 创建Socket
# 预留回调
a = tosun_recv_callback()
b = tosun_tcp_presend_callback()
c = tosun_tcp_ack_callback()
sock = tssocket(0, TS_AF_INET,TS_SOCK_STREAM, 0, a, b, c)

# 绑定ip port
self1_addr = Tts_sockaddr_in()
self1_addr.sin_family = TS_AF_INET
self1_addr.sin_port = tssocket_htons(51051)
tssocket_aton(b"192.168.0.50", self1_addr.sin_addr)
selfaddr = cast(byref(self1_addr) , Pts_sockaddr).contents
tssocket_bind(0,sock,selfaddr,16)
tssocket_listen(0,sock,1)
connAddress = Tts_sockaddr()
addrlen = u32(0)
recvsock = tssocket_accept(0,sock,connAddress,addrlen)
if recvsock != -1:
    print(connAddress.sa_data)
    t1 = threading.Thread(target=recv_tcp,args=(recvsock,connAddress))

p = (u8*1400)()
for i in range(1400):
    p[i] = i%256

while 1:
    key = input("please input the key:")
    if key == "q":
        stop_thread(t1)
        break
    elif key == "1":
        tssocket_send(0, connAddress, p, 1400, 0)

tssocket_close(0,sock)

tsapp_disconnect()

finalize_lib_tsmaster()



