import win32com.client
import pythoncom
import win32api
import time
import os
from win32com.client import VARIANT

DBC_File_CAN = r'..\..\..\Data\Demo\Databases\PowerTrain.dbc'
DBC_File_CANFD = r'..\..\..\Data\Demo\Databases\CAN_FD_Powertrain.dbc'
DBC_File_J1939 = r'..\..\..\Data\Demo\Databases\J1939.dbc'

class constants:
    DT_STR_Network_Name = 0                                       # 获取网络名称
    DT_STR_DBC_FileName = 1                                       # 获取dbc文件名
    DT_INT_Protocol_Type = 2                                      # 获取协议类型，0=CAN; 1=FD; 2=J1939
    DT_INT_3 = 3                                                  # unused
    DT_INT_4 = 4                                                  # unused
    DT_INT_5 = 5                                                  # unused
    DT_INT_6 = 6                                                  # unused
    DT_INT_7 = 7                                                  # unused
    DT_INT_8 = 8                                                  # unused
    DT_INT_9 = 9                                                  # unused
    DT_INT_Signal_List_Count = 10                                 # 获取信号表数量 = db.sgns.count
    DT_INT_CAN_Message_List_Count = 11                            # 获取CAN报文表数量 = db.msgs.count
    DT_INT_CANFD_Message_List_Count = 12                          # 获取CAN FD报文表数量 = db.msgsFD.count
    DT_INT_CANJ1939_Message_List_Count = 13                       # 获取CAN J1939报文表数量 = db.msgsJ1939.count
    DT_INT_Node_List_Count = 14                                   # 获取节点表数量 = db.nodes.count
    DT_INT_EnvVar_List_Count = 15                                 # 获取环境变量表数量 = db.envs.count
    DT_INT_ValTab_List_Count = 16                                 # 获取取值表数量 = db.valtabs.count
    DT_INT_17 = 17                                                # unused
    DT_INT_18 = 18                                                # unused
    DT_INT_19 = 19                                                # unused
    DT_INT_Signal_List_Message_ID = 20                            # 获取信号表中第idx信号所在的报文标识符 db.sgns[idx].message_id
    DT_INT_Signal_List_Value_Type = 21                            # 获取信号表中第idx信号值类型 0-无符号整型 1-有符号整型 2-32位浮点 3-64位浮点
    DT_INT_Signal_List_Is_Motorola = 22                           # 获取信号表中第idx信号是否是Motorola格式，0-Intel格式、1-Motorola格式
    DT_INT_Signal_List_ValTab_Index = 23                          # 获取信号表中第idx信号所带的取值表在取值表列表中的索引
    DT_INT_Signal_List_Mux_Type = 24                              # 获取信号表中第idx信号Mux类型，0-普通信号, 1-multiplexor, 2-multiplexed信号
    DT_INT_Signal_List_Mux_Value = 25                             # 获取信号表中第idx信号作为multiplexor的值
    DT_INT_Signal_List_Layout_Start = 26                          # 获取信号表中第idx信号在报文中的起始位
    DT_INT_Signal_List_Length = 27                                # 获取信号表中第idx信号的信号长度
    DT_DBL_Signal_List_Factor = 28                                # 获取信号表中第idx信号放大因子
    DT_DBL_Signal_List_Offset = 29                                # 获取信号表中第idx信号偏移量
    DT_DBL_Signal_List_InitValue = 30                             # 获取信号表中第idx信号初始值
    DT_DBL_Signal_List_Min = 31                                   # 获取信号表中第idx信号最小值
    DT_DBL_Signal_List_Max = 32                                   # 获取信号表中第idx信号最大值
    DT_STR_Signal_List_Name = 33                                  # 获取信号表中第idx信号名称
    DT_STR_Signal_List_Unit = 34                                  # 获取信号表中第idx信号单位
    DT_STR_Signal_List_Comment = 35                               # 获取信号表中第idx信号注释
    DT_INT_Signal_List_Message_Index = 36                         # 获取信号表中第idx信号所在的报文在报文表中的索引 db.msgs[db.sgns[idx].message_idx]
    DT_INT_Signal_List_Message_Type = 37                          # 获取信号表中第idx信号所在的报文的类型，0=CAN, 1=CANFD, 2=J1939
    DT_STR_Signal_List_Struct = 38                                # 获取信号表中第idx信号全部属性，逗号分隔 db.sgns[idx]
    DT_INT_39 = 39                                                # unused
    DT_INT_CAN_Message_List_Type = 40                             # 获取CAN报文表中第idx报文类型，cftStdCAN = 0, cftExtCAN = 1, cftJ1939 = 2, cftStdCANFD = 3, cftExtCANFD = 4
    DT_INT_CAN_Message_List_DLC = 41                              # 获取CAN报文表中第idx报文数据长度
    DT_INT_CAN_Message_List_ID = 42                               # 获取CAN报文表中第idx报文标识符
    DT_INT_CAN_Message_List_CycleTime = 43                        # 获取CAN报文表中第idx报文周期
    DT_STR_CAN_Message_List_Name = 44                             # 获取CAN报文表中第idx报文名称
    DT_STR_CAN_Message_List_Comment = 45                          # 获取CAN报文表中第idx报文注释
    DT_INT_CAN_Message_List_TX_Node_Index = 46                    # 获取CAN报文表中第idx报文对应的发送节点的索引
    DT_INT_CAN_Message_List_Owned_Signal_List_Count = 47          # 获取CAN报文表中第idx报文拥有的信号数量 db.msgs[idx].sgns.count
    DT_INT_CAN_Message_List_Owned_Signal_List_Signal_Index = 48   # 获取CAN报文表中第idx报文中第subidx信号在信号表中的索引 db.sgns[db.sgns.indexof(db.msgs[idx].sgns[subidx])]
    DT_STR_CAN_Message_List_Struct = 49                           # 获取CAN报文表中第idx报文全部属性，逗号分隔 db.msgs[idx]
    DT_INT_50 = 50                                                # unused
    DT_INT_51 = 51                                                # unused
    DT_INT_52 = 52                                                # unused
    DT_INT_53 = 53                                                # unused
    DT_INT_54 = 54                                                # unused
    DT_INT_55 = 55                                                # unused
    DT_INT_56 = 56                                                # unused
    DT_INT_57 = 57                                                # unused
    DT_INT_58 = 58                                                # unused
    DT_INT_59 = 59                                                # unused
    DT_INT_CANFD_Message_List_Type = 60                           # 获取CANFD报文表中第idx报文类型，cftStdCAN = 0, cftExtCAN = 1, cftJ1939 = 2, cftStdCANFD = 3, cftExtCANFD = 4
    DT_INT_CANFD_Message_List_DLC = 61                            # 获取CANFD报文表中第idx报文数据长度
    DT_INT_CANFD_Message_List_ID = 62                             # 获取CANFD报文表中第idx报文标识符
    DT_INT_CANFD_Message_List_CycleTime = 63                      # 获取CANFD报文表中第idx报文周期
    DT_STR_CANFD_Message_List_Name = 64                           # 获取CANFD报文表中第idx报文名称
    DT_STR_CANFD_Message_List_Comment = 65                        # 获取CANFD报文表中第idx报文注释
    DT_INT_CANFD_Message_List_TX_Node_Index = 66                  # 获取CANFD报文表中第idx报文对应的发送节点的索引
    DT_INT_CANFD_Message_List_Owned_Signal_List_Count = 67        # 获取CANFD报文表中第idx报文拥有的信号数量 db.msgs[idx].sgns.count
    DT_INT_CANFD_Message_List_Owned_Signal_List_Signal_Index = 68 # 获取CANFD报文表中第idx报文中第subidx信号在信号表中的索引 db.sgns[db.sgns.indexof(db.msgs[idx].sgns[subidx])]
    DT_INT_CANFD_Message_List_BRS = 69                            # 获取CANFD报文表中第idx报文BRS，0-No BRS、1-BRS
    DT_STR_CANFD_Message_List_Struct = 70                         # 获取CANFD报文表中第idx报文全部属性，逗号分隔 db.msgs[idx]
    DT_INT_71 = 71                                                # unused
    DT_INT_72 = 72                                                # unused
    DT_INT_73 = 73                                                # unused
    DT_INT_74 = 74                                                # unused
    DT_INT_75 = 75                                                # unused
    DT_INT_76 = 76                                                # unused
    DT_INT_77 = 77                                                # unused
    DT_INT_78 = 78                                                # unused
    DT_INT_79 = 79                                                # unused
    DT_INT_J1939_Message_List_Type = 80                           # 获取J1939报文表中第idx报文类型，cftStdCAN = 0, cftExtCAN = 1, cftJ1939 = 2, cftStdCANFD = 3, cftExtCANFD = 4
    DT_INT_J1939_Message_List_DLC = 81                            # 获取J1939报文表中第idx报文数据长度
    DT_INT_J1939_Message_List_ID = 82                             # 获取J1939报文表中第idx报文标识符
    DT_INT_J1939_Message_List_CycleTime = 83                      # 获取J1939报文表中第idx报文周期
    DT_STR_J1939_Message_List_Name = 84                           # 获取J1939报文表中第idx报文名称
    DT_STR_J1939_Message_List_Comment = 85                        # 获取J1939报文表中第idx报文注释
    DT_INT_J1939_Message_List_TX_Node_Index = 86                  # 获取J1939报文表中第idx报文对应的发送节点的索引
    DT_INT_J1939_Message_List_Owned_Signal_List_Count = 87        # 获取J1939报文表中第idx报文拥有的信号数量 db.msgs[idx].sgns.count
    DT_INT_J1939_Message_List_Owned_Signal_List_Signal_Index = 88 # 获取J1939报文表中第idx报文中第subidx信号在信号表中的索引 db.sgns[db.sgns.indexof(db.msgs[idx].sgns[subidx])]
    DT_STR_J1939_Message_List_Struct = 89                         # 获取CAN报文表中第idx报文全部属性，逗号分隔 db.msgs[idx]
    DT_INT_90 = 90                                                # unused
    DT_INT_91 = 91                                                # unused
    DT_INT_92 = 92                                                # unused
    DT_INT_93 = 93                                                # unused
    DT_INT_94 = 94                                                # unused
    DT_INT_95 = 95                                                # unused
    DT_INT_96 = 96                                                # unused
    DT_INT_97 = 97                                                # unused
    DT_INT_98 = 98                                                # unused
    DT_INT_99 = 99                                                # unused
    DT_INT_Node_List_Address = 100                                # 获取节点表中第idx节点地址，默认为0
    DT_STR_Node_List_Name = 101                                   # 获取节点表中第idx节点名称
    DT_STR_Node_List_Comment = 102                                # 获取节点表中第idx节点注释
    DT_INT_Node_List_TX_CAN_Message_List_Count = 103              # 获取节点表中第idx节点所发送的CAN报文数量 db.nodes[idx].txmsgs.count
    DT_INT_Node_List_TX_CAN_Message_List_Message_Index = 104      # 获取节点表中第idx节点所发送的subidx报文在CAN报文表中的索引 db.msgs[db.msgs.indexof(db.nodes[idx].txmsgs[subidx])]
    DT_INT_Node_List_RX_CAN_Message_List_Count = 105              # 获取节点表中第idx节点所接收的CAN报文数量
    DT_INT_Node_List_RX_CAN_Message_List_Message_Index = 106      # 获取节点表中第idx节点所接收的subidx报文在CAN报文表中的索引
    DT_INT_Node_List_TX_FD_Message_List_Count = 107               # 获取节点表中第idx节点所发送的FD报文数量 db.nodes[idx].txmsgs.count
    DT_INT_Node_List_TX_FD_Message_List_Message_Index = 108       # 获取节点表中第idx节点所发送的subidx报文在FD报文表中的索引 db.msgs[db.msgs.indexof(db.nodes[idx].txmsgs[subidx])]
    DT_INT_Node_List_RX_FD_Message_List_Count = 109               # 获取节点表中第idx节点所接收的FD报文数量
    DT_INT_Node_List_RX_FD_Message_List_Message_Index = 110       # 获取节点表中第idx节点所接收的subidx报文在FD报文表中的索引
    DT_INT_Node_List_TX_J1939_Message_List_Count = 111            # 获取节点表中第idx节点所发送的J1939报文数量 db.nodes[idx].txmsgs.count
    DT_INT_Node_List_TX_J1939_Message_List_Message_Index = 112    # 获取节点表中第idx节点所发送的subidx报文在J1939报文表中的索引 db.msgs[db.msgs.indexof(db.nodes[idx].txmsgs[subidx])]
    DT_INT_Node_List_RX_J1939_Message_List_Count = 113            # 获取节点表中第idx节点所接收的J1939报文数量
    DT_INT_Node_List_RX_J1939_Message_List_Message_Index = 114    # 获取节点表中第idx节点所接收的subidx报文在J1939报文表中的索引
    DT_INT_Node_List_TX_Signal_List_Count = 115                   # 获取节点表中第idx节点所发送的信号数量
    DT_INT_Node_List_TX_Signal_List_Signal_Index = 116            # 获取节点表中第idx节点所发送的subidx信号在信号表中的索引
    DT_INT_Node_List_RX_Signal_List_Count = 117                   # 获取节点表中第idx节点所接收的信号数量
    DT_INT_Node_List_RX_Signal_List_Signal_Index = 118            # 获取节点表中第idx节点所接收的subidx信号在信号表中的索引
    DT_STR_Node_List_Struct = 119                                 # 获取节点表中第idx节点全部属性，逗号分隔 db.nodes[idx]
    DT_INT_120 = 120                                              # unused
    DT_INT_121 = 121                                              # unused
    DT_INT_122 = 122                                              # unused
    DT_INT_123 = 123                                              # unused
    DT_INT_124 = 124                                              # unused
    DT_INT_125 = 125                                              # unused
    DT_INT_126 = 126                                              # unused
    DT_INT_127 = 127                                              # unused
    DT_INT_128 = 128                                              # unused
    DT_INT_129 = 129                                              # unused
    DT_INT_EnvVar_List_Value_Type = 130                           # 获取环境变量表中第idx环境变量值类型，0-整型、1-浮点、2-字符串、3-数据
    DT_DBL_EnvVar_List_MIN = 131                                  # 获取环境变量表中第idx环境变量最小值
    DT_DBL_EnvVar_List_MAX = 132                                  # 获取环境变量表中第idx环境变量最大值
    DT_DBL_EnvVar_List_Init_Value = 133                           # 获取环境变量表中第idx环境变量初始值
    DT_STR_EnvVar_List_Name = 134                                 # 获取环境变量表中第idx环境变量名称
    DT_STR_EnvVar_List_Unit = 135                                 # 获取环境变量表中第idx环境变量单位
    DT_STR_EnvVar_List_Comment = 136                              # 获取环境变量表中第idx环境变量注释
    DT_STR_EnvVar_List_Struct = 137                               # 获取环境变量表中第idx环境变量全部属性，逗号分隔 db.EnvVars[idx]
    DT_INT_138 = 138                                              # unused
    DT_INT_139 = 139                                              # unused
    DT_INT_ValTab_List_Item_List_Count = 140                      # 获取取值表中第idx取值表所包含的值数量
    DT_INT_ValTab_List_Item_List_Name = 141                       # 获取取值表中第idx取值表名称
    DT_DBL_ValTab_List_Item_List_Value = 142                      # 获取取值表中第idx取值表中第subidx的值
    DT_STR_ValTab_List_Struct = 143                               # 获取取值表中第idx取值表全部属性，逗号分隔 db.ValTabs[idx]


def check(AResult):
    if 0 == AResult:
        return True
    else:
        print('Query error with result', AResult)
        return False

def parse_dbc(db, AFileName):
    # load a dbc, the file name can be relative path to TSMaster.exe, the supported channels are separated by ','
    id = db.load_can_db(AFileName, '0,1')
    print('CAN/CAN-FD database loaded with Id =', id)

    # to retrieve total count of database already loaded
    n = db.get_can_db_count()
    print('Loaded CAN database count =', n)

    # to iterate each database and get its Id
    for i in range(n):
        id = db.get_can_db_id(i)
        print('Id of CAN database index', i, 'is', id)

    # start extracting
    print('\nStart extracting...')

    # extract network info...
    # network name
    result, s = db.get_can_db_info(id, constants.DT_STR_Network_Name, -1, -1)
    if check(result): print('Network name:', s)
    # loaded dbc file name
    result, s = db.get_can_db_info(id, constants.DT_STR_DBC_FileName, -1, -1)
    if check(result): print('Loaded dbc file name:', os.path.basename(s))
    # protocol name
    result, s = db.get_can_db_info(id, constants.DT_INT_Protocol_Type, -1, -1)
    if check(result): print('DBC protocol type:', s)

    # extract signal list ---------------------------------------------------------
    result, s = db.get_can_db_info(id, constants.DT_INT_Signal_List_Count, -1, -1)
    if check(result): print('\nSignal list count:', s)
    n = int(s)
    for i in range(n):
        sl = ''
        # get signal name
        result, s = db.get_can_db_info(id, constants.DT_STR_Signal_List_Name, i, -1)
        if check(result): sl = sl + 'Signal: ' + s + ', '
        # get signal's message's identifier
        result, s = db.get_can_db_info(id, constants.DT_INT_Signal_List_Message_ID, i, -1)
        if check(result): sl = sl + 'Msg. Id=' + s + ', '
        # get signal value type, 0: unsigned int; 1: signed int; 2: IEEE float 32; 3: IEEE float 64
        result, s = db.get_can_db_info(id, constants.DT_INT_Signal_List_Value_Type, i, -1)
        if check(result): sl = sl + 'Value Type=' + s + ', '
        # get signal byte order, 0: intel; 1: motorola
        result, s = db.get_can_db_info(id, constants.DT_INT_Signal_List_Is_Motorola, i, -1)
        if check(result): sl = sl + 'Is Motorola=' + s + ', '
        # get signal value table index
        result, s = db.get_can_db_info(id, constants.DT_INT_Signal_List_ValTab_Index, i, -1)
        if check(result): sl = sl + 'VT Index=' + s + ', '
        # get signal start bit in message
        result, s = db.get_can_db_info(id, constants.DT_INT_Signal_List_Layout_Start, i, -1)
        if check(result): sl = sl + 'Start bit=' + s + ', '
        # get signal length
        result, s = db.get_can_db_info(id, constants.DT_INT_Signal_List_Length, i, -1)
        if check(result): sl = sl + 'Len=' + s + ', '
        # get signal factor
        result, s = db.get_can_db_info(id, constants.DT_DBL_Signal_List_Factor, i, -1)
        if check(result): sl = sl + 'Factor=' + s + ', '
        # get signal offset
        result, s = db.get_can_db_info(id, constants.DT_DBL_Signal_List_Offset, i, -1)
        if check(result): sl = sl + 'Offset=' + s + ', '
        # get signal init value
        result, s = db.get_can_db_info(id, constants.DT_DBL_Signal_List_InitValue, i, -1)
        if check(result): sl = sl + 'Init=' + s + ', '
        # get signal min value
        result, s = db.get_can_db_info(id, constants.DT_DBL_Signal_List_Min, i, -1)
        if check(result): sl = sl + 'Min=' + s + ', '
        # get signal max value
        result, s = db.get_can_db_info(id, constants.DT_DBL_Signal_List_Max, i, -1)
        if check(result): sl = sl + 'Max=' + s + ', '
        # get signal unit
        result, s = db.get_can_db_info(id, constants.DT_STR_Signal_List_Unit, i, -1)
        if check(result): sl = sl + 'Unit=' + s + ', '
        # get signal comment
        result, s = db.get_can_db_info(id, constants.DT_STR_Signal_List_Comment, i, -1)
        if check(result): sl = sl + 'Comment=' + s + ', '
        # get signal's message index in message list
        result, s = db.get_can_db_info(id, constants.DT_INT_Signal_List_Message_Index, i, -1)
        if check(result): sl = sl + 'Msg. Index=' + s + ', '
        # get signal's message type, 0=CAN, 1=CAN FD, 2=J1939
        result, s = db.get_can_db_info(id, constants.DT_INT_Signal_List_Message_Type, i, -1)
        if check(result): sl = sl + 'Msg. Type=' + s + ', '
        print(sl)

    # extract classical CAN message list ------------------------------------------
    result, s = db.get_can_db_info(id, constants.DT_INT_CAN_Message_List_Count, -1, -1)
    if check(result): print('\nClassical CAN Message list count:', s)
    n = int(s)
    m = 0
    for i in range(n):
        sl = ''
        # get message name
        result, s = db.get_can_db_info(id, constants.DT_STR_CAN_Message_List_Name, i, -1)
        if check(result): sl = sl + 'CAN Message: ' + s + ', '
        # get message type, cftStdCAN = 0, cftExtCAN = 1, cftJ1939 = 2, cftStdCANFD = 3, cftExtCANFD = 4
        result, s = db.get_can_db_info(id, constants.DT_INT_CAN_Message_List_Type, i, -1)
        if check(result): sl = sl + 'Type=' + s + ', '
        # get message dlc
        result, s = db.get_can_db_info(id, constants.DT_INT_CAN_Message_List_DLC, i, -1)
        if check(result): sl = sl + 'DLC=' + s + ', '
        # get message identifier
        result, s = db.get_can_db_info(id, constants.DT_INT_CAN_Message_List_ID, i, -1)
        if check(result): sl = sl + 'ID=' + s + ', '
        # get message cycle time
        result, s = db.get_can_db_info(id, constants.DT_INT_CAN_Message_List_CycleTime, i, -1)
        if check(result): sl = sl + 'Cycle=' + s + ', '
        # get message comment
        result, s = db.get_can_db_info(id, constants.DT_STR_CAN_Message_List_Comment, i, -1)
        if check(result): sl = sl + 'Comment=' + s + ', '
        # get message's tx node index
        result, s = db.get_can_db_info(id, constants.DT_INT_CAN_Message_List_TX_Node_Index, i, -1)
        if check(result): sl = sl + 'Tx Node Index=' + s + ', '
        # get signal count of message
        result, s = db.get_can_db_info(id, constants.DT_INT_CAN_Message_List_Owned_Signal_List_Count, i, -1)
        if check(result): 
            sl = sl + 'Signal Count=' + s + ', '
            m = int(s)
        print(sl)
        # print out its signals
        if m > 0:
            for j in range(m):
                # get message's signal index in signal list
                result, s = db.get_can_db_info(id, constants.DT_INT_CAN_Message_List_Owned_Signal_List_Signal_Index, i, j)
                if check(result):
                    sl = '        Signal Index=' + s + ', '
                    # get signal properties bundle
                    result, s = db.get_can_db_info(id, constants.DT_STR_Signal_List_Struct, int(s), -1)
                    if check(result):
                        sl = sl + s
                        print(sl)

    # extract FD CAN message list -------------------------------------------------
    result, s = db.get_can_db_info(id, constants.DT_INT_CANFD_Message_List_Count, -1, -1)
    if check(result): print('\nFD CAN Message list count:', s)
    n = int(s)
    m = 0
    for i in range(n):
        sl = ''
        # get message name
        result, s = db.get_can_db_info(id, constants.DT_STR_CANFD_Message_List_Name, i, -1)
        if check(result): sl = sl + 'CANFD Message: ' + s + ', '
        # get message type, cftStdCAN = 0, cftExtCAN = 1, cftJ1939 = 2, cftStdCANFD = 3, cftExtCANFD = 4
        result, s = db.get_can_db_info(id, constants.DT_INT_CANFD_Message_List_Type, i, -1)
        if check(result): sl = sl + 'Type=' + s + ', '
        # get message dlc
        result, s = db.get_can_db_info(id, constants.DT_INT_CANFD_Message_List_DLC, i, -1)
        if check(result): sl = sl + 'DLC=' + s + ', '
        # get message identifier
        result, s = db.get_can_db_info(id, constants.DT_INT_CANFD_Message_List_ID, i, -1)
        if check(result): sl = sl + 'ID=' + s + ', '
        # get message cycle time
        result, s = db.get_can_db_info(id, constants.DT_INT_CANFD_Message_List_CycleTime, i, -1)
        if check(result): sl = sl + 'Cycle=' + s + ', '
        # get message comment
        result, s = db.get_can_db_info(id, constants.DT_STR_CANFD_Message_List_Comment, i, -1)
        if check(result): sl = sl + 'Comment=' + s + ', '
        # get message's tx node index
        result, s = db.get_can_db_info(id, constants.DT_INT_CANFD_Message_List_TX_Node_Index, i, -1)
        if check(result): sl = sl + 'Tx Node Index=' + s + ', '
        # get BRS flag
        result, s = db.get_can_db_info(id, constants.DT_INT_CANFD_Message_List_BRS, i, -1)
        if check(result): sl = sl + 'BRS=' + s + ', '
        # get signal count of message
        result, s = db.get_can_db_info(id, constants.DT_INT_CANFD_Message_List_Owned_Signal_List_Count, i, -1)
        if check(result): 
            sl = sl + 'Signal Count=' + s + ', '
            m = int(s)
        print(sl)
        # print out its signals
        if m > 0:
            for j in range(m):
                # get message's signal index in signal list
                result, s = db.get_can_db_info(id, constants.DT_INT_CANFD_Message_List_Owned_Signal_List_Signal_Index, i, j)
                if check(result):
                    sl = '        Signal Index=' + s + ', '
                    # get signal properties bundle
                    result, s = db.get_can_db_info(id, constants.DT_STR_Signal_List_Struct, int(s), -1)
                    if check(result):
                        sl = sl + s
                        print(sl)

    # extract J1939 CAN message list ----------------------------------------------
    result, s = db.get_can_db_info(id, constants.DT_INT_CANJ1939_Message_List_Count, -1, -1)
    if check(result): print('\nJ1939 CAN Message list count:', s)
    n = int(s)
    m = 0
    for i in range(n):
        sl = ''
        # get message name
        result, s = db.get_can_db_info(id, constants.DT_STR_J1939_Message_List_Name, i, -1)
        if check(result): sl = sl + 'J1939 Message: ' + s + ', '
        # get message type, cftStdCAN = 0, cftExtCAN = 1, cftJ1939 = 2, cftStdCANFD = 3, cftExtCANFD = 4
        result, s = db.get_can_db_info(id, constants.DT_INT_J1939_Message_List_Type, i, -1)
        if check(result): sl = sl + 'Type=' + s + ', '
        # get message dlc
        result, s = db.get_can_db_info(id, constants.DT_INT_J1939_Message_List_DLC, i, -1)
        if check(result): sl = sl + 'DLC=' + s + ', '
        # get message identifier
        result, s = db.get_can_db_info(id, constants.DT_INT_J1939_Message_List_ID, i, -1)
        if check(result): sl = sl + 'ID=' + s + ', '
        # get message cycle time
        result, s = db.get_can_db_info(id, constants.DT_INT_J1939_Message_List_CycleTime, i, -1)
        if check(result): sl = sl + 'Cycle=' + s + ', '
        # get message comment
        result, s = db.get_can_db_info(id, constants.DT_STR_J1939_Message_List_Comment, i, -1)
        if check(result): sl = sl + 'Comment=' + s + ', '
        # get message's tx node index
        result, s = db.get_can_db_info(id, constants.DT_INT_J1939_Message_List_TX_Node_Index, i, -1)
        if check(result): sl = sl + 'Tx Node Index=' + s + ', '
        # get signal count of message
        result, s = db.get_can_db_info(id, constants.DT_INT_J1939_Message_List_Owned_Signal_List_Count, i, -1)
        if check(result): 
            sl = sl + 'Signal Count=' + s + ', '
            m = int(s)
        print(sl)
        # print out its signals
        if m > 0:
            for j in range(m):
                # get message's signal index in signal list
                result, s = db.get_can_db_info(id, constants.DT_INT_J1939_Message_List_Owned_Signal_List_Signal_Index, i, j)
                if check(result):
                    sl = '        Signal Index=' + s + ', '
                    # get signal properties bundle
                    result, s = db.get_can_db_info(id, constants.DT_STR_Signal_List_Struct, int(s), -1)
                    if check(result):
                        sl = sl + s
                        print(sl)

    # extract node list -----------------------------------------------------------
    result, s = db.get_can_db_info(id, constants.DT_INT_Node_List_Count, -1, -1)
    if check(result): print('\nNode list count:', s)
    n = int(s)
    mTxCAN = 0
    mRxCAN = 0
    mTxFD = 0
    mRxFD = 0
    mTxJ1939 = 0
    mRxJ1939 = 0
    mTxSgn = 0
    mRxSgn = 0
    for i in range(n):
        sl = ''
        # get node name
        result, s = db.get_can_db_info(id, constants.DT_STR_Node_List_Name, i, -1)
        if check(result): sl = sl + 'Node Name: ' + s + ', '
        # get node address
        result, s = db.get_can_db_info(id, constants.DT_INT_Node_List_Address, i, -1)
        if check(result): sl = sl + 'Node Address=' + s + ', '
        # get node comment
        result, s = db.get_can_db_info(id, constants.DT_STR_Node_List_Comment, i, -1)
        if check(result): sl = sl + 'Node Comment=' + s + ', '
        # get node's tx CAN message list
        result, s = db.get_can_db_info(id, constants.DT_INT_Node_List_TX_CAN_Message_List_Count, i, -1)
        if check(result): 
            sl = sl + 'Tx CAN msg. Count=' + s + ', '
            mTxCAN = int(s)
        # get node's rx CAN message list
        result, s = db.get_can_db_info(id, constants.DT_INT_Node_List_RX_CAN_Message_List_Count, i, -1)
        if check(result): 
            sl = sl + 'Rx CAN msg. Count=' + s + ', '
            mRxCAN = int(s)
        # get node's tx CAN FD message list
        result, s = db.get_can_db_info(id, constants.DT_INT_Node_List_TX_FD_Message_List_Count, i, -1)
        if check(result): 
            sl = sl + 'Tx CAN FD Count=' + s + ', '
            mTxFD = int(s)
        # get node's rx CAN FD message list
        result, s = db.get_can_db_info(id, constants.DT_INT_Node_List_RX_FD_Message_List_Count, i, -1)
        if check(result): 
            sl = sl + 'Rx CAN FD Count=' + s + ', '
            mRxFD = int(s)
        # get node's tx CAN J1939 message list
        result, s = db.get_can_db_info(id, constants.DT_INT_Node_List_TX_J1939_Message_List_Count, i, -1)
        if check(result): 
            sl = sl + 'Tx CAN J1939 Count=' + s + ', '
            mTxJ1939 = int(s)
        # get node's rx CAN J1939 message list
        result, s = db.get_can_db_info(id, constants.DT_INT_Node_List_RX_J1939_Message_List_Count, i, -1)
        if check(result): 
            sl = sl + 'Rx CAN J1939 Count=' + s + ', '
            mRxJ1939 = int(s)
        # get node's tx signal list
        result, s = db.get_can_db_info(id, constants.DT_INT_Node_List_TX_Signal_List_Count, i, -1)
        if check(result): 
            sl = sl + 'Tx sgn. Count=' + s + ', '
            mTxSgn = int(s)
        # get node's rx signal list
        result, s = db.get_can_db_info(id, constants.DT_INT_Node_List_RX_Signal_List_Count, i, -1)
        if check(result): 
            sl = sl + 'Rx sgn. Count=' + s + ', '
            mRxSgn = int(s)
        print(sl)
        # print each tx CAN message
        for j in range(mTxCAN):
            result, s = db.get_can_db_info(id, constants.DT_INT_Node_List_TX_CAN_Message_List_Message_Index, i, j)
            if check(result):
                sl = '        Tx CAN Index: ' + s + ', Content='
                result, s = db.get_can_db_info(id, constants.DT_STR_CAN_Message_List_Struct, int(s), -1)
                if check(result):
                    sl = sl + s
                    print(sl)
        # print each rx CAN message
        for j in range(mRxCAN):
            result, s = db.get_can_db_info(id, constants.DT_INT_Node_List_RX_CAN_Message_List_Message_Index, i, j)
            if check(result):
                sl = '        Rx CAN Index: ' + s + ', Content='
                result, s = db.get_can_db_info(id, constants.DT_STR_CAN_Message_List_Struct, int(s), -1)
                if check(result):
                    sl = sl + s
                    print(sl)
        # print each tx FD message
        for j in range(mTxFD):
            result, s = db.get_can_db_info(id, constants.DT_INT_Node_List_TX_FD_Message_List_Message_Index, i, j)
            if check(result):
                sl = '        Tx FD Index: ' + s + ', Content='
                result, s = db.get_can_db_info(id, constants.DT_STR_CANFD_Message_List_Struct, int(s), -1)
                if check(result):
                    sl = sl + s
                    print(sl)
        # print each rx FD message
        for j in range(mRxFD):
            result, s = db.get_can_db_info(id, constants.DT_INT_Node_List_RX_FD_Message_List_Message_Index, i, j)
            if check(result):
                sl = '        Rx FD Index: ' + s + ', Content='
                result, s = db.get_can_db_info(id, constants.DT_STR_CANFD_Message_List_Struct, int(s), -1)
                if check(result):
                    sl = sl + s
                    print(sl)
        # print each tx J1939 message
        for j in range(mTxJ1939):
            result, s = db.get_can_db_info(id, constants.DT_INT_Node_List_TX_J1939_Message_List_Message_Index, i, j)
            if check(result):
                sl = '        Tx J1939 Index: ' + s + ', Content='
                result, s = db.get_can_db_info(id, constants.DT_STR_J1939_Message_List_Struct, int(s), -1)
                if check(result):
                    sl = sl + s
                    print(sl)
        # print each rx J1939 message
        for j in range(mRxJ1939):
            result, s = db.get_can_db_info(id, constants.DT_INT_Node_List_RX_J1939_Message_List_Message_Index, i, j)
            if check(result):
                sl = '        Rx J1939 Index: ' + s + ', Content='
                result, s = db.get_can_db_info(id, constants.DT_STR_J1939_Message_List_Struct, int(s), -1)
                if check(result):
                    sl = sl + s
                    print(sl)
        # print each tx signal
        for j in range(mTxSgn):
            result, s = db.get_can_db_info(id, constants.DT_INT_Node_List_TX_Signal_List_Signal_Index, i, j)
            if check(result):
                sl = '        Tx signal Index: ' + s + ', Content='
                result, s = db.get_can_db_info(id, constants.DT_STR_Signal_List_Struct, int(s), -1)
                if check(result):
                    sl = sl + s
                    print(sl)
        # print each rx signal
        for j in range(mRxSgn):
            result, s = db.get_can_db_info(id, constants.DT_INT_Node_List_RX_Signal_List_Signal_Index, i, j)
            if check(result):
                sl = '        Rx signal Index: ' + s + ', Content='
                result, s = db.get_can_db_info(id, constants.DT_STR_Signal_List_Struct, int(s), -1)
                if check(result):
                    sl = sl + s
                    print(sl)

    # extract environment variable list ---------------------------------------------------------
    result, s = db.get_can_db_info(id, constants.DT_INT_EnvVar_List_Count, -1, -1)
    if check(result): print('\nEnvironment variable list count:', s)
    n = int(s)
    for i in range(n):
        sl = ''
        # get environment variable name
        result, s = db.get_can_db_info(id, constants.DT_STR_EnvVar_List_Name, i, -1)
        if check(result): sl = sl + 'Environment variable: ' + s + ', '
        # get environment variable value type, 0: int; 1: float; 2: string; 3: data
        result, s = db.get_can_db_info(id, constants.DT_INT_EnvVar_List_Value_Type, i, -1)
        if check(result): sl = sl + 'type=' + s + ', '
        # get environment variable min value
        result, s = db.get_can_db_info(id, constants.DT_DBL_EnvVar_List_MIN, i, -1)
        if check(result): sl = sl + 'min=' + s + ', '
        # get environment variable max value
        result, s = db.get_can_db_info(id, constants.DT_DBL_EnvVar_List_MAX, i, -1)
        if check(result): sl = sl + 'max=' + s + ', '
        # get environment variable init value
        result, s = db.get_can_db_info(id, constants.DT_DBL_EnvVar_List_Init_Value, i, -1)
        if check(result): sl = sl + 'init=' + s + ', '
        # get environment variable unit
        result, s = db.get_can_db_info(id, constants.DT_STR_EnvVar_List_Unit, i, -1)
        if check(result): sl = sl + 'Unit=' + s + ', '
        # get environment variable comment
        result, s = db.get_can_db_info(id, constants.DT_STR_EnvVar_List_Comment, i, -1)
        if check(result): sl = sl + 'Comment=' + s + ', '
        print(sl)
        
    # extract value table list ---------------------------------------------------------
    result, s = db.get_can_db_info(id, constants.DT_INT_ValTab_List_Count, -1, -1)
    if check(result): print('\nValue table list count:', s)
    n = int(s)
    for i in range(n):
        result, s = db.get_can_db_info(id, constants.DT_INT_ValTab_List_Item_List_Count, i, -1)
        if check(result): 
            print('\nValue table index', i, 'count:', s)
            m = int(s)
            for j in range(m):
                sl = ''
                # get value table name
                result, s = db.get_can_db_info(id, constants.DT_INT_ValTab_List_Item_List_Name, i, j)
                if check(result): sl = sl + '    Name=' + s + ', '
                # get value table value
                result, s = db.get_can_db_info(id, constants.DT_DBL_ValTab_List_Item_List_Value, i, j)
                if check(result): sl = sl + 'Value=' + s + ', '
                print(sl)
        
    # unload all databases
    db.unload_can_dbs()
    print('\nAll CAN/CAN-FD databases unloaded')


# retrieve TSMaster application management
#pythoncom.CoInitialize() # enable multithread
app = win32com.client.Dispatch("comTSMaster.TSApplication")
# retrieve db kernel
db = app.TSDB()
# parse classical CAN dbc
parse_dbc(db, DBC_File_CAN)
# parse CAN FD dbc
parse_dbc(db, DBC_File_CANFD)
# parse J1939 dbc
parse_dbc(db, DBC_File_J1939)

