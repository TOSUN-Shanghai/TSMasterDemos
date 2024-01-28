'''
Author: seven 865762826@qq.com
Date: 2023-04-21 11:19:14
LastEditors: seven 865762826@qq.com
LastEditTime: 2023-07-07 15:59:38
github:https://github.com/sy950915/TSMasterAPI.git
'''
import time
from .TSCommon import *

Kbps_mapping = {
    "CAN":[[500,2000],[500,2000],[500,2000],[500,2000]],
    "LIN":[19.2,19.2,19.2,19.2],
}

mapping = {
    "CAN":{"CHNCount":4,"HW_Names":["TC1014","TC1014","TC1014"],"HW_Chns":["0,1","0","3"]},
    "LIN":{"CHNCount":4,"HW_Names":["TC1016","TC1016","TC1016"],"HW_Chns":["0,1","0","1"]},
    "Flexray":{"CHNCount":4,"HW_Names":["TC1034","TC1034","TC1034"],"HW_Chns":["0,1","0","1"]},
    "Kbps_mapping":Kbps_mapping,
}

def set_mapping(mapping):
    """
    set mapping for channel names and HW channels. 描述了TSMaster的软件通道名称和硬件channal名称映射。
    """
    AppName = c_char_p()
    tsapp_get_current_application(AppName)
    if 'CAN' in mapping and "CHNCount"in mapping['CAN'] and "HW_Names"in mapping['CAN'] and "HW_Chns"in mapping['CAN']:
        tsapp_set_can_channel_count(mapping['CAN']['CHNCount'])
        HW_Names_len = len(mapping['CAN']['HW_Names'])
        HW_Chns_len = len(mapping['CAN']['HW_Chns'])
        if(HW_Names_len != HW_Chns_len):
            raise Exception("Length of HW_Names and HW_Chns must match")
        Mapping_channel_count = 0
        for i in range(HW_Chns_len):
            Mapping_channel_count += len(mapping['CAN']['HW_Chns'][i].split(','))
        if Mapping_channel_count>mapping['CAN']['CHNCount']:
            raise Exception("Number of channels in mapping is higher than number of channels on the board")
        FCount = 0
        hw = []
        for i in range(HW_Names_len):
            hw.append(mapping['CAN']['HW_Names'][i])
            hw_sub_index = hw.count(mapping['CAN']['HW_Names'][i]) - 1
            chn_str = mapping['CAN']['HW_Chns'][i].split(',')
            for chn in chn_str:
                tsapp_set_mapping_verbose(AppName,TLIBApplicationChannelType.APP_CAN,FCount,mapping['CAN']['HW_Names'][i].encode('utf8'),3,HW_dict[mapping['CAN']['HW_Names'][i]],hw_sub_index,int(chn),True)
                FCount += 1
    else:
        tsapp_set_can_channel_count(0)
    if 'LIN' in mapping and "CHNCount"in mapping['LIN'] and "HW_Names"in mapping['LIN'] and "HW_Chns"in mapping['LIN']:
        tsapp_set_lin_channel_count(mapping['LIN']['CHNCount'])
        HW_Names_len = len(mapping['LIN']['HW_Names'])
        HW_Chns_len = len(mapping['LIN']['HW_Chns'])
        if(HW_Names_len != HW_Chns_len):
            raise Exception("Length of HW_Names and HW_Chns must match")
        Mapping_channel_count = 0
        for i in range(HW_Chns_len):
            Mapping_channel_count += len(mapping['LIN']['HW_Chns'][i].split(','))
        if Mapping_channel_count>mapping['LIN']['CHNCount']:
            raise Exception("Number of channels in mapping is higher than number of channels on the board")
        FCount = 0
        hw = []
        for i in range(HW_Names_len):
            hw.append(mapping['LIN']['HW_Names'][i])
            hw_sub_index = hw.count(mapping['LIN']['HW_Names'][i]) - 1
            chn_str = mapping['LIN']['HW_Chns'][i].split(',')
            for chn in chn_str:
                tsapp_set_mapping_verbose(AppName,TLIBApplicationChannelType.APP_LIN,FCount,mapping['LIN']['HW_Names'][i].encode('utf8'),3,HW_dict[mapping['LIN']['HW_Names'][i]],hw_sub_index,int(chn),True)
                FCount += 1
    else:
        tsapp_set_lin_channel_count(0)
    if 'Flexray' in mapping and "CHNCount"in mapping['Flexray'] and "HW_Names"in mapping['Flexray'] and "HW_Chns"in mapping['Flexray']:
        tsapp_set_flexray_channel_count(mapping['Flexray']['CHNCount'])
        HW_Names_len = len(mapping['Flexray']['HW_Names'])
        HW_Chns_len = len(mapping['Flexray']['HW_Chns'])
        if(HW_Names_len != HW_Chns_len):
            raise Exception("Length of HW_Names and HW_Chns must match")
        Mapping_channel_count = 0
        for i in range(HW_Chns_len):
            Mapping_channel_count += len(mapping['Flexray']['HW_Chns'][i].split(','))
        if Mapping_channel_count>mapping['Flexray']['CHNCount']:
            raise Exception("Number of channels in mapping is higher than number of channels on the board")
        FCount = 0
        hw = []
        for i in range(HW_Names_len):
            hw.append(mapping['Flexray']['HW_Names'][i])
            hw_sub_index = hw.count(mapping['Flexray']['HW_Names'][i]) - 1
            chn_str = mapping['Flexray']['HW_Chns'][i].split(',')
            for chn in chn_str:
                tsapp_set_mapping_verbose(AppName,TLIBApplicationChannelType.APP_FlexRay,FCount,mapping['Flexray']['HW_Names'][i].encode('utf8'),3,HW_dict[mapping['Flexray']['HW_Names'][i]],hw_sub_index,int(chn),True)
                FCount += 1
    else:
        tsapp_set_flexray_channel_count(0)
    if 'Kbps_mapping' in mapping and 'CAN' in mapping['Kbps_mapping'] and len(mapping['Kbps_mapping']['CAN']) == mapping['CAN']['CHNCount']:
        for i in range(mapping['CAN']['CHNCount']):
            if(len(mapping['Kbps_mapping']['CAN'][i])>1):
                tsapp_configure_baudrate_canfd(i,mapping['Kbps_mapping']['CAN'][i][0],mapping['Kbps_mapping']['CAN'][i][1],TLIBCANFDControllerType.lfdtISOCAN,TLIBCANFDControllerMode.lfdmNormal, True)
            elif len(mapping['Kbps_mapping']['CAN'][i]) == 1:
                tsapp_configure_baudrate_can(i,mapping['Kbps_mapping']['CAN'][i][0],False, True)
            else:
                raise Exception("TSDriverOperationError: CAN Kbps "+ str(i) +" IS NULL")
    else:
        for i in range(mapping['CAN']['CHNCount']):
            if(len(mapping['Kbps_mapping']['CAN'][i])>1):
                tsapp_configure_baudrate_canfd(i,500,2000,TLIBCANFDControllerType.lfdtISOCAN,TLIBCANFDControllerMode.lfdmNormal, True)
    if 'Kbps_mapping' in mapping and 'LIN' in mapping['Kbps_mapping'] and len(mapping['Kbps_mapping']['LIN']) == mapping['LIN']['CHNCount']:
            for i in range(mapping['LIN']['CHNCount']):
                    tsapp_configure_baudrate_lin(i,mapping['Kbps_mapping']['LIN'][i],LIN_PROTOCOL.LIN_PROTOCOL_21)
    else:
        for i in range(mapping['LIN']['CHNCount']):
                    tsapp_configure_baudrate_lin(i,19.2,LIN_PROTOCOL.LIN_PROTOCOL_21)
def send_msg(msg:TLIBCAN or TLIBCANFD or TLIBLIN or TLIBFlexray,is_async = True,is_cycle = False,timeout = 0.1):
    """
    if is_cycle == True, timeout表示周期,单位为s,可以为小数,比如1ms 为0.001
    if is_cycle == Flase, is_async == False,timeout 表示超时参数,单位为s
    if is_cycle == Flase, is_async == True,timeout 表示无意义
    """
    if isinstance(msg,PCAN or TLIBCAN):
        if is_cycle:
            return tsapp_add_cyclic_msg_can(msg,timeout*1000)
        elif is_async:
            return tsapp_transmit_can_async(msg)
        return tsapp_transmit_can_sync(msg,timeout*1000)
    elif isinstance(msg,PCANFD or TLIBCANFD):
        if is_cycle:
            return tsapp_add_cyclic_msg_canfd(msg,timeout*1000)
        elif is_async:
            return tsapp_transmit_canfd_async(msg)
        return tsapp_transmit_canfd_sync(msg,timeout*1000)
    elif isinstance(msg,PLIN or TLIBLIN):
        if is_async:
            return tsapp_transmit_lin_async(msg)
        return tsapp_transmit_lin_sync(msg,timeout*1000)
    elif isinstance(msg,PFlexray or TLIBFlexray):
        if is_async:
            return tsapp_transmit_flexray_async(msg)
        return tsapp_transmit_flexray_async(msg,timeout*1000)
def del_cycle_msg(msg:TLIBCAN or TLIBCANFD,is_all_cycle_msg:False):
    if is_all_cycle_msg:
        return tsapp_delete_cyclic_msgs()
    if isinstance(msg,TLIBCAN or PCAN):
        return tsapp_delete_cyclic_msg_can(msg)
    elif isinstance(msg,TLIBCANFD or PCANFD):
        return tsapp_delete_cyclic_msg_canfd(msg)
def clear_fifo_buffer(Achannel:int,msgType:MSGType):
    if msgType == MSGType.CANMSG:
        return tsfifo_clear_can_receive_buffers(Achannel)
    if msgType == MSGType.CANFDMSG:
        return tsfifo_clear_canfd_receive_buffers(Achannel)
    if msgType == MSGType.LINMSG:
        return tsfifo_clear_lin_receive_buffers(Achannel)
    if msgType == MSGType.FlexrayMSG:
        return tsfifo_clear_flexray_receive_buffers(Achannel)
def recv_msg(channelidx:CHANNEL_INDEX,msgType:MSGType,is_includeTX:False,timeout=0.1):
    if msgType == MSGType.CANMSG:
        start_time = time.perf_counter()  
        Msg_list = (TLIBCAN*1)()
        while time.perf_counter() - start_time < timeout:
            buffer_size = s32(1)
            ret = tsfifo_receive_can_msgs(Msg_list,buffer_size,channelidx,is_includeTX)
            if ret == 0 and buffer_size == 1:
                return Msg_list[0]
        return None  # Timed out or failed to receive message.
    elif msgType == MSGType.CANFDMSG:
        start_time = time.perf_counter()  
        Msg_list = (TLIBCANFD*1)()
        while time.perf_counter() - start_time < timeout:
            buffer_size = s32(1)
            ret = tsfifo_receive_canfd_msgs(Msg_list,buffer_size,channelidx,is_includeTX)
            if ret == 0 and buffer_size == 1:
                return Msg_list[0]
        return None  # Timed out or failed to receive message.
    elif msgType == MSGType.LINMSG:
        start_time = time.perf_counter()  # Time when the message was first received.
        Msg_list = (TLIBLIN*1)()
        while time.perf_counter() - start_time < timeout:
            buffer_size = s32(1)
            ret = tsfifo_receive_lin_msgs(Msg_list,buffer_size,channelidx,is_includeTX)
            if ret == 0 and buffer_size == 1:
                return Msg_list[0]
        return None  # Timed out or failed to receive message.
    elif msgType == MSGType.FlexrayMSG:
        start_time = time.perf_counter()  # Time when the message was first received.
        Msg_list = (TLIBFlexray*1)()
        while time.perf_counter() - start_time < timeout:
            buffer_size = s32(1)
            ret = tsfifo_receive_flexray_msgs(Msg_list,buffer_size,channelidx,is_includeTX)
            if ret == 0 and buffer_size == 1:
                return Msg_list[0]
        return None  # Timed out or failed to receive message.
def recv_msgs(channelidx:CHANNEL_INDEX,msgType:MSGType,Anumber:int,is_includeTX:False,timeout=0.1):  
    # Receive messages from a TSFIFO.  Blocks until a message is available.  Return a list of messages.  If no messages are available, return None. 
    if msgType == MSGType.CANMSG:
        start_time = time.perf_counter()  
        Msg_list = (TLIBCAN*Anumber)()
        while time.perf_counter() - start_time < timeout:
            buffer_size = s32(Anumber)
            ret = tsfifo_receive_can_msgs(Msg_list,buffer_size,channelidx,is_includeTX)
            if ret == 0 and buffer_size != 0:
                return Msg_list[0:buffer_size.value]
        return None  # Timed out or failed to receive message.
    elif msgType == MSGType.CANFDMSG:
        start_time = time.perf_counter()  
        Msg_list = (TLIBCANFD*Anumber)()
        while time.perf_counter() - start_time < timeout:
            buffer_size = s32(Anumber)
            ret = tsfifo_receive_canfd_msgs(Msg_list,buffer_size,channelidx,is_includeTX)
            if ret == 0 and buffer_size != 0:
                return Msg_list[0:buffer_size.value]
        return None  # Timed out or failed to receive message.
    elif msgType == MSGType.LINMSG:
        start_time = time.perf_counter()  # Time when the message was first received.
        Msg_list = (TLIBLIN*Anumber)()
        while time.perf_counter() - start_time < timeout:
            buffer_size = s32(Anumber)
            ret = tsfifo_receive_lin_msgs(Msg_list,buffer_size,channelidx,is_includeTX)
            if ret == 0 and buffer_size != 0:
                return Msg_list[0:buffer_size.value]
        return None  # Timed out or failed to receive message.
    elif msgType == MSGType.FlexrayMSG:
        start_time = time.perf_counter()  # Time when the message was first received.
        Msg_list = (TLIBFlexray*Anumber)()
        while time.perf_counter() - start_time < timeout:
            buffer_size = s32(Anumber)
            ret = tsfifo_receive_flexray_msgs(Msg_list,buffer_size,channelidx,is_includeTX)
            if ret == 0 and buffer_size != 0:
                return Msg_list[0:buffer_size.value]
        return None  # Timed out or failed to receive message.
def start_logging_msg(blf_pathName:bytes):
    if isinstance(blf_pathName,str):
        blf_pathName = blf_pathName.encode('utf-8')  # Convert string to bytes.
    tsapp_start_logging(blf_pathName)
def stop_logging_msg():
    tsapp_stop_logging()
def get_db_info(msgType:MSGType,db_idx:int):
    """
    获取的dict 结构如下：
    db:
        ECU0:
            TX_Frames:
                    Frame0:
                        signls
                    Frame1:
                        signls
            RX_Frames:
                    Frame0:
                        signls
                    Frame1:
                        signls            
        ECU1:
            TX_Frames:
                    Frame0:
                        signls
                    Frame1:
                        signls
            RX_Frames:
                    Frame0:
                        signls
                    Frame1:
                        signls 
    """
    db_info = {}
    if msgType == MSGType.CANMSG or msgType == MSGType.CANFDMSG :
        db = TDBProperties()
        db.FDBIndex = db_idx
        tsdb_get_can_db_properties_by_index(db)
        for ecu_idx in range(db.FECUCount):
            db_ecu = TDBECUProperties()
            db_ecu.FDBIndex = db_idx
            db_ecu.FECUIndex = ecu_idx
            tsdb_get_can_db_ecu_properties_by_index(db_ecu)
            db_info[db_ecu.FName.decode('utf8')] = {}
            db_info[db_ecu.FName.decode('utf8')]['TX'] = {}
            db_info[db_ecu.FName.decode('utf8')]['RX'] = {}
            for TXframe_idx in range(db_ecu.FTxFrameCount):
                db_tx_frame = TDBFrameProperties()
                db_tx_frame.FDBIndex = db_idx
                db_tx_frame.FECUIndex = ecu_idx
                db_tx_frame.FFrameIndex = TXframe_idx
                db_tx_frame.FIsTx = True
                tsdb_get_can_db_frame_properties_by_index(db_tx_frame)
                db_info[db_ecu.FName.decode('utf8')]['TX'][db_tx_frame.FName.decode('utf8')] = {}
                db_info[db_ecu.FName.decode('utf8')]['TX'][db_tx_frame.FName.decode('utf8')]['FCANIsDataFrame'] = db_tx_frame.FCANIsDataFrame
                db_info[db_ecu.FName.decode('utf8')]['TX'][db_tx_frame.FName.decode('utf8')]['FCANIsStdFrame'] = db_tx_frame.FCANIsStdFrame
                db_info[db_ecu.FName.decode('utf8')]['TX'][db_tx_frame.FName.decode('utf8')]['FCANIsEdl'] = db_tx_frame.FCANIsEdl
                db_info[db_ecu.FName.decode('utf8')]['TX'][db_tx_frame.FName.decode('utf8')]['FCANIsBrs'] = db_tx_frame.FCANIsBrs
                db_info[db_ecu.FName.decode('utf8')]['TX'][db_tx_frame.FName.decode('utf8')]['FIdentifier'] = db_tx_frame.FCANIdentifier
                db_info[db_ecu.FName.decode('utf8')]['TX'][db_tx_frame.FName.decode('utf8')]['FDLC'] = db_tx_frame.FCANDLC
                db_info[db_ecu.FName.decode('utf8')]['TX'][db_tx_frame.FName.decode('utf8')]['Signals'] = {}
                for Signal_idx in range(db_tx_frame.FSignalCount):
                    db_frame_signal = TDBSignalProperties()
                    db_frame_signal.FDBIndex = db_idx
                    db_frame_signal.FECUIndex = ecu_idx
                    db_frame_signal.FFrameIndex = TXframe_idx
                    db_frame_signal.FSignalIndex = Signal_idx
                    db_frame_signal.FIsTx = True
                    tsdb_get_can_db_signal_properties_by_index(db_frame_signal)
                    db_info[db_ecu.FName.decode('utf8')]['TX'][db_tx_frame.FName.decode('utf8')]['Signals'][db_frame_signal.FName.decode('utf8')] = {}
                    db_info[db_ecu.FName.decode('utf8')]['TX'][db_tx_frame.FName.decode('utf8')]['Signals'][db_frame_signal.FName.decode('utf8')]['def'] = db_frame_signal.FCANSignal
                    db_info[db_ecu.FName.decode('utf8')]['TX'][db_tx_frame.FName.decode('utf8')]['Signals'][db_frame_signal.FName.decode('utf8')]['value'] = db_frame_signal.FInitValue
                    del db_frame_signal
                del db_tx_frame
            for RXframe_idx in range(db_ecu.FRxFrameCount):
                db_rx_frame = TDBFrameProperties()
                db_rx_frame.FDBIndex = db_idx
                db_rx_frame.FECUIndex = ecu_idx
                db_rx_frame.FFrameIndex = RXframe_idx
                db_rx_frame.FIsTx = False
                tsdb_get_can_db_frame_properties_by_index(db_rx_frame)
                db_info[db_ecu.FName.decode('utf8')]['RX'][db_rx_frame.FName.decode('utf8')] = {}
                db_info[db_ecu.FName.decode('utf8')]['RX'][db_rx_frame.FName.decode('utf8')]['FCANIsDataFrame'] = db_rx_frame.FCANIsDataFrame
                db_info[db_ecu.FName.decode('utf8')]['RX'][db_rx_frame.FName.decode('utf8')]['FCANIsStdFrame'] = db_rx_frame.FCANIsStdFrame
                db_info[db_ecu.FName.decode('utf8')]['RX'][db_rx_frame.FName.decode('utf8')]['FCANIsEdl'] = db_rx_frame.FCANIsEdl
                db_info[db_ecu.FName.decode('utf8')]['RX'][db_rx_frame.FName.decode('utf8')]['FCANIsBrs'] = db_rx_frame.FCANIsBrs
                db_info[db_ecu.FName.decode('utf8')]['RX'][db_rx_frame.FName.decode('utf8')]['FIdentifier'] = db_rx_frame.FCANIdentifier
                db_info[db_ecu.FName.decode('utf8')]['RX'][db_rx_frame.FName.decode('utf8')]['FDLC'] = db_rx_frame.FCANDLC
                db_info[db_ecu.FName.decode('utf8')]['RX'][db_rx_frame.FName.decode('utf8')]['Signals'] = {}
                for Signal_idx in range(db_rx_frame.FSignalCount):
                    db_frame_signal = TDBSignalProperties()
                    db_frame_signal.FDBIndex = db_idx
                    db_frame_signal.FECUIndex = ecu_idx
                    db_frame_signal.FFrameIndex = RXframe_idx
                    db_frame_signal.FSignalIndex = Signal_idx
                    db_frame_signal.FIsTx = False
                    tsdb_get_can_db_signal_properties_by_index(db_frame_signal)
                    db_info[db_ecu.FName.decode('utf8')]['RX'][db_rx_frame.FName.decode('utf8')]['Signals'][db_frame_signal.FName.decode('utf8')] = {}
                    db_info[db_ecu.FName.decode('utf8')]['RX'][db_rx_frame.FName.decode('utf8')]['Signals'][db_frame_signal.FName.decode('utf8')]['def'] = db_frame_signal.FCANSignal
                    db_info[db_ecu.FName.decode('utf8')]['RX'][db_rx_frame.FName.decode('utf8')]['Signals'][db_frame_signal.FName.decode('utf8')]['value'] = db_frame_signal.FInitValue
                    del db_frame_signal
                del db_rx_frame
            del db_ecu
    if msgType == MSGType.LINMSG:
        db = TDBProperties()
        db.FDBIndex = db_idx
        tsdb_get_lin_db_properties_by_index(db)
        for ecu_idx in range(db.FECUCount):
            db_ecu = TDBECUProperties()
            db_ecu.FDBIndex = db_idx
            db_ecu.FECUIndex = ecu_idx
            tsdb_get_lin_db_ecu_properties_by_index(db_ecu)
            db_info[db_ecu.FName.decode('utf8')] = {}
            db_info[db_ecu.FName.decode('utf8')]['TX'] = {}
            db_info[db_ecu.FName.decode('utf8')]['RX'] = {}
            for TXframe_idx in range(db_ecu.FTxFrameCount):
                db_tx_frame = TDBFrameProperties()
                db_tx_frame.FDBIndex = db_idx
                db_tx_frame.FECUIndex = ecu_idx
                db_tx_frame.FFrameIndex = TXframe_idx
                db_tx_frame.FIsTx = True
                tsdb_get_lin_db_frame_properties_by_index(db_tx_frame)
                db_info[db_ecu.FName.decode('utf8')]['TX'][db_tx_frame.FName.decode('utf8')] = {}
                db_info[db_ecu.FName.decode('utf8')]['TX'][db_tx_frame.FName.decode('utf8')]['FIdentifier'] = db_tx_frame.FLINIdentifier
                db_info[db_ecu.FName.decode('utf8')]['TX'][db_tx_frame.FName.decode('utf8')]['FDLC'] = db_tx_frame.FLINDLC
                db_info[db_ecu.FName.decode('utf8')]['TX'][db_tx_frame.FName.decode('utf8')]['Signals'] = {}
                for Signal_idx in range(db_tx_frame.FSignalCount):
                    db_frame_signal = TDBSignalProperties()
                    db_frame_signal.FDBIndex = db_idx
                    db_frame_signal.FECUIndex = ecu_idx
                    db_frame_signal.FFrameIndex = TXframe_idx
                    db_frame_signal.FSignalIndex = Signal_idx
                    db_frame_signal.FIsTx = True
                    tsdb_get_lin_db_signal_properties_by_index(db_frame_signal)
                    db_info[db_ecu.FName.decode('utf8')]['TX'][db_tx_frame.FName.decode('utf8')]['Signals'][db_frame_signal.FName.decode('utf8')] = {}
                    db_info[db_ecu.FName.decode('utf8')]['TX'][db_tx_frame.FName.decode('utf8')]['Signals'][db_frame_signal.FName.decode('utf8')]['def'] = db_frame_signal.FLINSignal
                    db_info[db_ecu.FName.decode('utf8')]['TX'][db_tx_frame.FName.decode('utf8')]['Signals'][db_frame_signal.FName.decode('utf8')]['value'] = db_frame_signal.FInitValue
                    del db_frame_signal
                del db_tx_frame
            for RXframe_idx in range(db_ecu.FRxFrameCount):
                db_rx_frame = TDBFrameProperties()
                db_rx_frame.FDBIndex = db_idx
                db_rx_frame.FECUIndex = ecu_idx
                db_rx_frame.FFrameIndex = RXframe_idx
                db_rx_frame.FIsTx = False
                tsdb_get_lin_db_frame_properties_by_index(db_rx_frame)
                db_info[db_ecu.FName.decode('utf8')]['RX'][db_rx_frame.FName.decode('utf8')] = {}
                db_info[db_ecu.FName.decode('utf8')]['RX'][db_rx_frame.FName.decode('utf8')]['FIdentifier'] = db_rx_frame.FLINIdentifier
                db_info[db_ecu.FName.decode('utf8')]['RX'][db_rx_frame.FName.decode('utf8')]['FDLC'] = db_rx_frame.FLINDLC
                db_info[db_ecu.FName.decode('utf8')]['RX'][db_rx_frame.FName.decode('utf8')]['Signals'] = {}
                for Signal_idx in range(db_rx_frame.FSignalCount):
                    db_frame_signal = TDBSignalProperties()
                    db_frame_signal.FDBIndex = db_idx
                    db_frame_signal.FECUIndex = ecu_idx
                    db_frame_signal.FFrameIndex = RXframe_idx
                    db_frame_signal.FSignalIndex = Signal_idx
                    db_frame_signal.FIsTx = False
                    tsdb_get_lin_db_signal_properties_by_index(db_frame_signal)
                    db_info[db_ecu.FName.decode('utf8')]['RX'][db_rx_frame.FName.decode('utf8')]['Signals'][db_frame_signal.FName.decode('utf8')] = {}
                    db_info[db_ecu.FName.decode('utf8')]['RX'][db_rx_frame.FName.decode('utf8')]['Signals'][db_frame_signal.FName.decode('utf8')]['def'] = db_frame_signal.FLINSignal
                    db_info[db_ecu.FName.decode('utf8')]['RX'][db_rx_frame.FName.decode('utf8')]['Signals'][db_frame_signal.FName.decode('utf8')]['value'] = db_frame_signal.FInitValue
                    del db_frame_signal
                del db_rx_frame
            del db_ecu
    if msgType == MSGType.FlexrayMSG:
        db = TDBProperties()
        db.FDBIndex = db_idx
        tsdb_get_flexray_db_properties_by_index(db)
        for ecu_idx in range(db.FECUCount):
            db_ecu = TDBECUProperties()
            db_ecu.FDBIndex = db_idx
            db_ecu.FECUIndex = ecu_idx
            tsdb_get_flexray_db_ecu_properties_by_index(db_ecu)
            db_info[db_ecu.FName.decode('utf8')] = {}
            db_info[db_ecu.FName.decode('utf8')]['TX'] = {}
            db_info[db_ecu.FName.decode('utf8')]['RX'] = {}
            for TXframe_idx in range(db_ecu.FTxFrameCount):
                db_tx_frame = TDBFrameProperties()
                db_tx_frame.FDBIndex = db_idx
                db_tx_frame.FECUIndex = ecu_idx
                db_tx_frame.FFrameIndex = TXframe_idx
                db_tx_frame.FIsTx = True
                tsdb_get_flexray_db_frame_properties_by_index(db_tx_frame)
                db_info[db_ecu.FName.decode('utf8')]['TX'][db_tx_frame.FName.decode('utf8')] = {}
                db_info[db_ecu.FName.decode('utf8')]['TX'][db_tx_frame.FName.decode('utf8')]['FSlotId'] = db_tx_frame.FFRSlotId
                db_info[db_ecu.FName.decode('utf8')]['TX'][db_tx_frame.FName.decode('utf8')]['FBaseCycle'] = db_tx_frame.FFRBaseCycle
                db_info[db_ecu.FName.decode('utf8')]['TX'][db_tx_frame.FName.decode('utf8')]['FCycleRepetition'] = db_tx_frame.FFRCycleRepetition
                db_info[db_ecu.FName.decode('utf8')]['TX'][db_tx_frame.FName.decode('utf8')]['FDLC'] = db_tx_frame.FFRDLC
                db_info[db_ecu.FName.decode('utf8')]['TX'][db_tx_frame.FName.decode('utf8')]['Signals'] = {}
                for Signal_idx in range(db_tx_frame.FSignalCount):
                    db_frame_signal = TDBSignalProperties()
                    db_frame_signal.FDBIndex = db_idx
                    db_frame_signal.FECUIndex = ecu_idx
                    db_frame_signal.FFrameIndex = TXframe_idx
                    db_frame_signal.FSignalIndex = Signal_idx
                    db_frame_signal.FIsTx = True
                    tsdb_get_flexray_db_signal_properties_by_index(db_frame_signal)
                    db_info[db_ecu.FName.decode('utf8')]['TX'][db_tx_frame.FName.decode('utf8')]['Signals'][db_frame_signal.FName.decode('utf8')] = {}
                    db_info[db_ecu.FName.decode('utf8')]['TX'][db_tx_frame.FName.decode('utf8')]['Signals'][db_frame_signal.FName.decode('utf8')]['def'] = db_frame_signal.FFlexRaySignal
                    db_info[db_ecu.FName.decode('utf8')]['TX'][db_tx_frame.FName.decode('utf8')]['Signals'][db_frame_signal.FName.decode('utf8')]['value'] = db_frame_signal.FInitValue
                    del db_frame_signal
                del db_tx_frame
            for RXframe_idx in range(db_ecu.FRxFrameCount):
                db_rx_frame = TDBFrameProperties()
                db_rx_frame.FDBIndex = db_idx
                db_rx_frame.FECUIndex = ecu_idx
                db_rx_frame.FFrameIndex = RXframe_idx
                db_rx_frame.FIsTx = False
                tsdb_get_flexray_db_frame_properties_by_index(db_rx_frame)
                db_info[db_ecu.FName.decode('utf8')]['RX'][db_rx_frame.FName.decode('utf8')] = {}
                db_info[db_ecu.FName.decode('utf8')]['RX'][db_rx_frame.FName.decode('utf8')]['FSlotId'] = db_rx_frame.FFRSlotId
                db_info[db_ecu.FName.decode('utf8')]['RX'][db_rx_frame.FName.decode('utf8')]['FBaseCycle'] = db_rx_frame.FFRBaseCycle
                db_info[db_ecu.FName.decode('utf8')]['RX'][db_rx_frame.FName.decode('utf8')]['FCycleRepetition'] = db_rx_frame.FFRCycleRepetition
                db_info[db_ecu.FName.decode('utf8')]['RX'][db_rx_frame.FName.decode('utf8')]['FDLC'] = db_rx_frame.FFRDLC
                db_info[db_ecu.FName.decode('utf8')]['RX'][db_rx_frame.FName.decode('utf8')]['Signals'] = {}
                for Signal_idx in range(db_rx_frame.FSignalCount):
                    db_frame_signal = TDBSignalProperties()
                    db_frame_signal.FDBIndex = db_idx
                    db_frame_signal.FECUIndex = ecu_idx
                    db_frame_signal.FFrameIndex = RXframe_idx
                    db_frame_signal.FSignalIndex = Signal_idx
                    db_frame_signal.FIsTx = False
                    tsdb_get_flexray_db_signal_properties_by_index(db_frame_signal)
                    db_info[db_ecu.FName.decode('utf8')]['RX'][db_rx_frame.FName.decode('utf8')]['Signals'][db_frame_signal.FName.decode('utf8')] = {}
                    db_info[db_ecu.FName.decode('utf8')]['RX'][db_rx_frame.FName.decode('utf8')]['Signals'][db_frame_signal.FName.decode('utf8')]['def'] = db_frame_signal.FFlexRaySignal
                    db_info[db_ecu.FName.decode('utf8')]['RX'][db_rx_frame.FName.decode('utf8')]['Signals'][db_frame_signal.FName.decode('utf8')]['value'] = db_frame_signal.FInitValue
                    del db_frame_signal
                del db_rx_frame
            del db_ecu
    return db_info
def get_db_frame_info(msgType:MSGType,db_idx:int):
    """
    获取的dict 结构如下：
    Frame0:
        signls
    Frame1:
        signls
    Frame2:
        signls
    Frame3:
        signls
        ...
    FrameN:
        signls
    """
    db = TDBProperties()
    db.FDBIndex = db_idx
    if msgType == MSGType.FlexrayMSG:
        tsdb_get_flexray_db_properties_by_index(db)
        Frame = {}
        for Frame_id in range(db.FFrameCount):
            frame = TDBFrameProperties()
            tsdb_get_flexray_db_frame_properties_by_db_index(db_idx,Frame_id,frame)
            Frame[frame.FName.decode('utf8')] ={}
            Frame[frame.FName.decode('utf8')]['FSlotId'] = frame.FFRSlotId
            Frame[frame.FName.decode('utf8')]['FBaseCycle'] = frame.FFRBaseCycle
            Frame[frame.FName.decode('utf8')]['FCycleRepetition'] = frame.FFRCycleRepetition
            Frame[frame.FName.decode('utf8')]['FDLC'] = frame.FFRDLC
            Frame[frame.FName.decode('utf8')]['Signals'] = {}
            if frame.FName.decode('utf8') == "CemBackBoneFr02":
                print(1)
            for singal_index in range(frame.FSignalCount):
                Signal = TDBSignalProperties()
                tsdb_get_flexray_db_signal_properties_by_frame_index(db_idx,Frame_id,singal_index,Signal)
                Frame[frame.FName.decode('utf8')]['Signals'][Signal.FName.decode('utf8')] = {}
                Frame[frame.FName.decode('utf8')]['Signals'][Signal.FName.decode('utf8')]['def'] = Signal.FFlexRaySignal
                Frame[frame.FName.decode('utf8')]['Signals'][Signal.FName.decode('utf8')]['value'] = 0
                del Signal
            del frame
    elif msgType == MSGType.CANMSG or msgType == MSGType.CANFDMSG:
        tsdb_get_can_db_properties_by_index(db)
        Frame = {}
        for Frame_id in range(db.FFrameCount):
            frame = TDBFrameProperties()
            tsdb_get_can_db_frame_properties_by_db_index(db_idx,Frame_id,frame)
            Frame[frame.FName.decode('utf8')] ={}
            Frame[frame.FName.decode('utf8')]['FCANIsDataFrame'] = frame.FCANIsDataFrame
            Frame[frame.FName.decode('utf8')]['FCANIsStdFrame'] = frame.FCANIsStdFrame
            Frame[frame.FName.decode('utf8')]['FCANIsEdl'] = frame.FCANIsEdl
            Frame[frame.FName.decode('utf8')]['FCANIsBrs'] = frame.FCANIsBrs
            Frame[frame.FName.decode('utf8')]['FIdentifier'] = frame.FCANIdentifier
            Frame[frame.FName.decode('utf8')]['FDLC'] = frame.FCANDLC
            Frame[frame.FName.decode('utf8')]['Signals'] = {}
            for singal_index in range(frame.FSignalCount):
                Signal = TDBSignalProperties()
                tsdb_get_can_db_signal_properties_by_frame_index(db_idx,Frame_id,singal_index,Signal)
                Frame[frame.FName.decode('utf8')]['Signals'][Signal.FName.decode('utf8')] = {}
                Frame[frame.FName.decode('utf8')]['Signals'][Signal.FName.decode('utf8')]['def'] = Signal.FCANSignal
                Frame[frame.FName.decode('utf8')]['Signals'][Signal.FName.decode('utf8')]['value'] = 0
                del Signal
            del frame
    elif msgType == MSGType.LINMSG :
        tsdb_get_lin_db_properties_by_index(db)
        Frame = {}
        for Frame_id in range(db.FFrameCount):
            frame = TDBFrameProperties()
            tsdb_get_lin_db_frame_properties_by_db_index(db_idx,Frame_id,frame)
            Frame[frame.FName.decode('utf8')] ={}
            Frame[frame.FName.decode('utf8')]['FIdentifier'] = frame.FLINIdentifier
            Frame[frame.FName.decode('utf8')]['FDLC'] = frame.FLINDLC
            Frame[frame.FName.decode('utf8')]['Signals'] = {}
            for singal_index in range(frame.FSignalCount):
                Signal = TDBSignalProperties()
                tsdb_get_lin_db_signal_properties_by_frame_index(db_idx,Frame_id,singal_index,Signal)
                Frame[frame.FName.decode('utf8')]['Signals'][Signal.FName.decode('utf8')] = {}
                Frame[frame.FName.decode('utf8')]['Signals'][Signal.FName.decode('utf8')]['def'] = Signal.FLINSignal
                Frame[frame.FName.decode('utf8')]['Signals'][Signal.FName.decode('utf8')]['value'] = 0
                del Signal
            del frame
    return Frame
def get_signals_value(Msg_info:dict,msg:TLIBCAN or TLIBCANFD or TLIBLIN or TLIBFlexray):
    """
    Msg_info:为get_db_info 或者 get_db_frame_info中的Frame字典
    比如:1、get_db_info 得到的字典中的 db_info['ecu1']['TX']['Frame1']
        2、get_db_frame_info 得到的字典的 Frame_info['Frame1']
    """
    if isinstance(msg,TLIBCANFD) or isinstance(msg,TLIBCAN) or isinstance(msg,PCANFD) or isinstance(msg,PCAN):
        if isinstance(Msg_info, dict) and (Msg_info['FIdentifier'] == msg.FIdentifier):
            value = {}
            for key in Msg_info['Signals']:
                value[key] = tscom_get_can_signal_value(Msg_info['Signals'][key]['def'],msg.FData)
                Msg_info['Signals'][key]['value'] = value[key]
            return value
    elif isinstance(msg,PLIN) or isinstance(msg,TLIBLIN):
        if isinstance(Msg_info, dict)and (Msg_info['FLINIdentifier'] == msg.FIdentifier):
            value = {}
            for key in Msg_info:
                value[key] = tscom_get_lin_signal_value(Msg_info['Signals'][key]['def'],msg.FData) 
                Msg_info['Signals'][key]['value'] = value[key]
            return value   
    elif isinstance(msg,PFlexray)or isinstance(msg,TLIBFlexray):
        if isinstance(Msg_info, dict) and (Msg_info['FFRSlotId'] == msg.FFSlotId and msg.FCycleNumber % Msg_info['FFRCycleRepetition'] == Msg_info['FFRBaseCycle']):
            value = {}
            for key in Msg_info['Signals']:
                value[key] = tscom_get_flexray_signal_value(Msg_info['Signals'][key]['def'],msg.FData)
                Msg_info['Signals'][key]['value'] = value[key]
            return value 
    return None  # if not supported type or not supported msg type, return None
def set_signals_value(Msg_info:dict,msg:TLIBCAN or TLIBCANFD or TLIBLIN or TLIBFlexray):
    """
    Msg_info:为get_db_info 或者 get_db_frame_info中的Frame字典
    比如:1、get_db_info 得到的字典中的 db_info['ecu1']['TX']['Frame1']
        2、get_db_frame_info 得到的字典的 Frame_info['Frame1']
    """
    if isinstance(msg,TLIBCANFD) or isinstance(msg,TLIBCAN) or isinstance(msg,PCANFD) or isinstance(msg,PCAN):
        if isinstance(Msg_info, dict) and (Msg_info['FIdentifier'] == msg.FIdentifier):
            msg.FDLC = Msg_info['FDLC']
            for key in Msg_info['Signals']:
                tscom_set_can_signal_value(Msg_info['Signals'][key]['def'],msg.FData,Msg_info['Signals'][key]['value'])
    elif isinstance(msg,PLIN) or isinstance(msg,TLIBLIN):
        if isinstance(Msg_info, dict) and (Msg_info['FIdentifier'] == msg.FIdentifier):
            msg.FDLC = Msg_info['FDLC']
            for key in Msg_info:
                tscom_set_lin_signal_value(Msg_info['Signals'][key]['def'],msg.FData,Msg_info['Signals'][key]['value'])  
    elif isinstance(msg,PFlexray)or isinstance(msg,TLIBFlexray):
        if isinstance(Msg_info, dict) and (Msg_info['FSlotId'] == msg.FFSlotId and msg.FCycleNumber % Msg_info['FCycleRepetition'] == Msg_info['FBaseCycle']):
            msg.FDLC = Msg_info['FDLC']
            for key in Msg_info['Signals']:
                tscom_set_flexray_signal_value(Msg_info['Signals'][key]['def'],msg.FData,Msg_info['Signals'][key]['value'])  
    return None  # if not supported type or not supported msg type, return None
def get_xml_info(xmlpathname:str):
    return Fibex_parse(xmlpathname)
def set_controller_config(xml_info_node,is_open_a=True, is_open_b=True, wakeup_chn=0, enable100_a=True, enable100_b=True,is_show_nullframe=True, is_Bridging=False):
    fr_config = TLibFlexray_controller_config()
    fr_config.NETWORK_MANAGEMENT_VECTOR_LENGTH = xml_info_node['NETWORK_MANAGEMENT_VECTOR_LENGTH']
    fr_config.PAYLOAD_LENGTH_STATIC = xml_info_node['PAYLOAD_LENGTH_STATIC']
    fr_config.LATEST_TX = xml_info_node['LATEST_TX']
    fr_config.T_S_S_TRANSMITTER = xml_info_node['T_S_S_TRANSMITTER']
    fr_config.CAS_RX_LOW_MAX = xml_info_node['CAS_RX_LOW_MAX']
    fr_config.SPEED = xml_info_node['SPEED']
    fr_config.WAKE_UP_SYMBOL_RX_WINDOW = xml_info_node['WAKE_UP_SYMBOL_RX_WINDOW']
    fr_config.WAKE_UP_PATTERN = xml_info_node['WAKE_UP_PATTERN']
    fr_config.WAKE_UP_SYMBOL_RX_IDLE = xml_info_node['WAKE_UP_SYMBOL_RX_IDLE']
    fr_config.WAKE_UP_SYMBOL_RX_LOW = xml_info_node['WAKE_UP_SYMBOL_RX_LOW']
    fr_config.WAKE_UP_SYMBOL_TX_IDLE = xml_info_node['WAKE_UP_SYMBOL_TX_IDLE']
    fr_config.WAKE_UP_SYMBOL_TX_LOW = xml_info_node['WAKE_UP_SYMBOL_TX_LOW']
    fr_config.channelAConnectedNode = 1 if is_open_a else 0
    fr_config.channelBConnectedNode = 1 if is_open_b else 0
    fr_config.channelASymbolTransmitted = 1  
    fr_config.channelBSymbolTransmitted = 1  
    fr_config.ALLOW_HALT_DUE_TO_CLOCK = xml_info_node['ALLOW_HALT_DUE_TO_CLOCK']
    fr_config.SINGLE_SLOT_ENABLED = xml_info_node['SINGLE_SLOT_ENABLED']
    fr_config.wake_up_idx = wakeup_chn
    fr_config.ALLOW_PASSIVE_TO_ACTIVE = xml_info_node['ALLOW_PASSIVE_TO_ACTIVE']
    fr_config.COLD_START_ATTEMPTS = xml_info_node['COLD_START_ATTEMPTS']
    fr_config.synchFrameTransmitted = 1
    fr_config.startupFrameTransmitted = xml_info_node['startupFrameTransmitted']
    fr_config.LISTEN_TIMEOUT = xml_info_node['LISTEN_TIMEOUT']
    fr_config.LISTEN_NOISE = xml_info_node['LISTEN_NOISE']
    fr_config.MAX_WITHOUT_CLOCK_CORRECTION_PASSIVE = xml_info_node['MAX_WITHOUT_CLOCK_CORRECTION_PASSIVE']
    fr_config.MAX_WITHOUT_CLOCK_CORRECTION_FATAL = xml_info_node['MAX_WITHOUT_CLOCK_CORRECTION_FATAL']
    fr_config.MICRO_PER_CYCLE = xml_info_node['MICRO_PER_CYCLE']
    fr_config.Macro_Per_Cycle = xml_info_node['MACRO_PER_CYCLE']
    fr_config.SYNC_NODE_MAX = xml_info_node['SYNC_NODE_MAX']
    fr_config.MICRO_INITIAL_OFFSET_A = xml_info_node['MICRO_INITIAL_OFFSET_A']
    fr_config.MICRO_INITIAL_OFFSET_B = xml_info_node['MICRO_INITIAL_OFFSET_B']
    fr_config.MACRO_INITIAL_OFFSET_A = xml_info_node['MACRO_INITIAL_OFFSET_A']
    fr_config.MACRO_INITIAL_OFFSET_B = xml_info_node['MACRO_INITIAL_OFFSET_B']
    fr_config.N_I_T = xml_info_node['N_I_T']
    fr_config.OFFSET_CORRECTION_START = xml_info_node['OFFSET_CORRECTION_START']
    fr_config.DELAY_COMPENSATION_A = xml_info_node['DELAY_COMPENSATION_A']
    fr_config.DELAY_COMPENSATION_B = xml_info_node['DELAY_COMPENSATION_B']
    fr_config.CLUSTER_DRIFT_DAMPING = xml_info_node['CLUSTER_DRIFT_DAMPING']
    fr_config.DECODING_CORRECTION = xml_info_node['DECODING_CORRECTION']
    fr_config.ACCEPTED_STARTUP_RANGE = xml_info_node['ACCEPTED_STARTUP_RANGE']
    fr_config.MAX_DRIFT = xml_info_node['MAX_DRIFT']
    fr_config.STATIC_SLOT = xml_info_node['STATIC_SLOT']
    fr_config.NUMBER_OF_STATIC_SLOTS = xml_info_node['NUMBER_OF_STATIC_SLOTS']
    fr_config.MINISLOT = xml_info_node['MINISLOT']
    fr_config.NUMBER_OF_MINISLOTS = xml_info_node['NUMBER_OF_MINISLOTS']
    fr_config.DYNAMIC_SLOT_IDLE_PHASE = xml_info_node['DYNAMIC_SLOT_IDLE_PHASE']
    fr_config.ACTION_POINT_OFFSET = xml_info_node['ACTION_POINT_OFFSET']
    fr_config.MINISLOT_ACTION_POINT_OFFSET = xml_info_node['MINISLOT_ACTION_POINT_OFFSET']
    fr_config.OFFSET_CORRECTION_OUT = xml_info_node['OFFSET_CORRECTION_OUT']
    fr_config.RATE_CORRECTION_OUT = xml_info_node['RATE_CORRECTION_OUT']
    fr_config.EXTERN_OFFSET_CORRECTION = xml_info_node['EXTERN_OFFSET_CORRECTION']
    fr_config.EXTERN_RATE_CORRECTION = xml_info_node['EXTERN_RATE_CORRECTION']
    fr_config.config1_byte = 1
        # if
    fr_config.config_byte = 0xc
    if is_Bridging:
            fr_config.config_byte = 0x3c
    fr_config.config_byte = fr_config.config_byte | (0x1 if enable100_a else 0x00) | (0x2 if enable100_b else 0x00) | (0x40 if is_show_nullframe else 0x00)
    return fr_config
def set_controller_frametrigger(ANodeIndex: s32,
                                            AControllerConfig: TLibFlexray_controller_config,
                                            AFrameLengthArray: bytearray,
                                            AFrameNum: s32, AFrameTrigger: TLibTrigger_def, AFrameTriggerNum: s32,
                                            ATimeoutMs: s32):
    tsflexray_set_controller_frametrigger(ANodeIndex,AControllerConfig,AFrameLengthArray,AFrameNum,AFrameTrigger,AFrameTriggerNum,ATimeoutMs)
def flexray_network_start(chnidx:s32,timeout:s32):
    tsflexray_start_net(chnidx,timeout)
def flexray_network_stop(chnidx:s32,timeout:s32):
    tsflexray_stop_net(chnidx,timeout)

# uds
def create_uds():
    pass

if __name__ == "__main__":
    initialize_lib_tsmaster(b"TSMaster")
    set_mapping(mapping)
    ACAN = TLIBCANFD(FIdentifier= 0x701,FDLC=9,FData=[1,23,4,2,5,6,7])
    xml_info = get_xml_info(r"C:\Users\yueto\Desktop\SDB21206_HX11_Low_BackboneFR_220513.xml")
    controller =  set_controller_config(xml_info.Ecus['VGM'])
    can_db_info = get_db_info(MSGType.CANMSG,0)
    RET = get_signals_value(can_db_info['Engine']['TX']['FallbackMessage'],ACAN)
    print(RET)
    for key in can_db_info['Engine']['TX']['FallbackMessage']['Signals']:
        can_db_info['Engine']['TX']['FallbackMessage']['Signals'][key]['value'] = 1
    set_signals_value(can_db_info['Engine']['TX']['FallbackMessage'],ACAN)
    print(ACAN)
    RET = get_signals_value(can_db_info['Engine']['TX']['FallbackMessage'],ACAN)
    print(RET)
    
    can_info = get_db_frame_info(MSGType.CANMSG,0)
    RET = get_signals_value(can_info['FallbackMessage'],ACAN)
    print(RET)
    for key in can_info['FallbackMessage']['Signals']:
        can_info['FallbackMessage']['Signals'][key]['value'] = 100
    set_signals_value(can_info['FallbackMessage'],ACAN)

    print(ACAN)

    finalize_lib_tsmaster()
    

