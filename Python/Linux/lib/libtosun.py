'''
Author: seven 865762826@qq.com
Date: 2023-02-21 16:56:50
LastEditors: seven 865762826@qq.com
LastEditTime: 2023-03-28 13:28:27
FilePath: \VSCode_Prod:\IDE\TSMaster\libtosun.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from libTOSUN.libTOSUN import *
import can
from typing import List, Optional, Tuple, Union, Deque, Any
from can.bus import LOG


class libtosunBus(can.BusABC):
    def __init__(self, channel: Any = None, *,
                 configs: [dict],
                 is_include_tx=False,
                 can_filters: Optional[can.typechecking.CanFilters] = None,
                 hwserial: bytes = b"",
                 filter:dict={},
                 **kwargs: object):
        super().__init__(channel, can_filters, **kwargs)
        self.device = TSMasterDevice(configs=configs,  hwserial=hwserial,
                                            is_include_tx=is_include_tx,filter= filter,
                                            #   is_start_recv = is_start_recv,
                                            #   is_recv_error=is_recv_error
                                              )

    def send(self, msg: can.Message, timeout: Optional[float] = 0.1, sync: bool = False,
             is_cyclic: bool = False) -> None:
        self.device.send_msg(msg, timeout, sync, is_cyclic)

    def _recv_internal(self, chn:int=0,timeout: Optional[float]=0.1) -> Tuple[Optional[can.Message], bool]:
        return self.device.recv(chn,timeout), False

    def shutdown(self) -> None:
        LOG.debug('TSMaster - shutdown.')
        super().shutdown()
        finalize_lib_tscan()
