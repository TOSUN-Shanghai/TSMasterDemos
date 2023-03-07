                                                                
DBC_File_CAN = '..\..\..\Data\Demo\Databases\PowerTrain.dbc';         
DBC_File_CANFD = '..\..\..\Data\Demo\Databases\CAN_FD_Powertrain.dbc';
DBC_File_J1939 = '..\..\..\Data\Demo\Databases\J1939.dbc';            
                                                                
% retrieve TSMaster application management
app = actxserver('comTSMaster.TSApplication');
% retrieve db kernel
db = app.TSDB();
% parse classical CAN dbc
parse_dbc(db, DBC_File_CAN);
% parse CAN FD dbc
parse_dbc(db, DBC_File_CANFD);
% parse J1939 dbc
parse_dbc(db, DBC_File_J1939);

function chkResult = check(AResult)
    if 0 == AResult
        chkResult = true;
    else
        chkResult = false;
        fprintf("Query error with result %d\n", AResult);
    end
end
        
function parse_dbc(db, AFileName)
    DT_STR_Network_Name = 0                                       ; 
    DT_STR_DBC_FileName = 1                                       ; 
    DT_INT_Protocol_Type = 2                                      ; 
    DT_INT_3 = 3                                                  ; 
    DT_INT_4 = 4                                                  ; 
    DT_INT_5 = 5                                                  ; 
    DT_INT_6 = 6                                                  ; 
    DT_INT_7 = 7                                                  ; 
    DT_INT_8 = 8                                                  ; 
    DT_INT_9 = 9                                                  ; 
    DT_INT_Signal_List_Count = 10                                 ; 
    DT_INT_CAN_Message_List_Count = 11                            ; 
    DT_INT_CANFD_Message_List_Count = 12                          ; 
    DT_INT_CANJ1939_Message_List_Count = 13                       ; 
    DT_INT_Node_List_Count = 14                                   ; 
    DT_INT_EnvVar_List_Count = 15                                 ; 
    DT_INT_ValTab_List_Count = 16                                 ; 
    DT_INT_17 = 17                                                ; 
    DT_INT_18 = 18                                                ; 
    DT_INT_19 = 19                                                ; 
    DT_INT_Signal_List_Message_ID = 20                            ; 
    DT_INT_Signal_List_Value_Type = 21                            ; 
    DT_INT_Signal_List_Is_Motorola = 22                           ; 
    DT_INT_Signal_List_ValTab_Index = 23                          ; 
    DT_INT_Signal_List_Mux_Type = 24                              ; 
    DT_INT_Signal_List_Mux_Value = 25                             ; 
    DT_INT_Signal_List_Layout_Start = 26                          ; 
    DT_INT_Signal_List_Length = 27                                ; 
    DT_DBL_Signal_List_Factor = 28                                ; 
    DT_DBL_Signal_List_Offset = 29                                ; 
    DT_DBL_Signal_List_InitValue = 30                             ; 
    DT_DBL_Signal_List_Min = 31                                   ; 
    DT_DBL_Signal_List_Max = 32                                   ; 
    DT_STR_Signal_List_Name = 33                                  ; 
    DT_STR_Signal_List_Unit = 34                                  ; 
    DT_STR_Signal_List_Comment = 35                               ; 
    DT_INT_Signal_List_Message_Index = 36                         ; 
    DT_INT_Signal_List_Message_Type = 37                          ; 
    DT_STR_Signal_List_Struct = 38                                ; 
    DT_INT_39 = 39                                                ; 
    DT_INT_CAN_Message_List_Type = 40                             ; 
    DT_INT_CAN_Message_List_DLC = 41                              ; 
    DT_INT_CAN_Message_List_ID = 42                               ; 
    DT_INT_CAN_Message_List_CycleTime = 43                        ; 
    DT_STR_CAN_Message_List_Name = 44                             ; 
    DT_STR_CAN_Message_List_Comment = 45                          ; 
    DT_INT_CAN_Message_List_TX_Node_Index = 46                    ; 
    DT_INT_CAN_Message_List_Owned_Signal_List_Count = 47          ; 
    DT_INT_CAN_Message_List_Owned_Signal_List_Signal_Index = 48   ; 
    DT_STR_CAN_Message_List_Struct = 49                           ; 
    DT_INT_50 = 50                                                ; 
    DT_INT_51 = 51                                                ; 
    DT_INT_52 = 52                                                ; 
    DT_INT_53 = 53                                                ; 
    DT_INT_54 = 54                                                ; 
    DT_INT_55 = 55                                                ; 
    DT_INT_56 = 56                                                ; 
    DT_INT_57 = 57                                                ; 
    DT_INT_58 = 58                                                ; 
    DT_INT_59 = 59                                                ; 
    DT_INT_CANFD_Message_List_Type = 60                           ; 
    DT_INT_CANFD_Message_List_DLC = 61                            ; 
    DT_INT_CANFD_Message_List_ID = 62                             ; 
    DT_INT_CANFD_Message_List_CycleTime = 63                      ; 
    DT_STR_CANFD_Message_List_Name = 64                           ; 
    DT_STR_CANFD_Message_List_Comment = 65                        ; 
    DT_INT_CANFD_Message_List_TX_Node_Index = 66                  ; 
    DT_INT_CANFD_Message_List_Owned_Signal_List_Count = 67        ; 
    DT_INT_CANFD_Message_List_Owned_Signal_List_Signal_Index = 68 ; 
    DT_INT_CANFD_Message_List_BRS = 69                            ; 
    DT_STR_CANFD_Message_List_Struct = 70                         ; 
    DT_INT_71 = 71                                                ; 
    DT_INT_72 = 72                                                ; 
    DT_INT_73 = 73                                                ; 
    DT_INT_74 = 74                                                ; 
    DT_INT_75 = 75                                                ; 
    DT_INT_76 = 76                                                ; 
    DT_INT_77 = 77                                                ; 
    DT_INT_78 = 78                                                ; 
    DT_INT_79 = 79                                                ; 
    DT_INT_J1939_Message_List_Type = 80                           ; 
    DT_INT_J1939_Message_List_DLC = 81                            ; 
    DT_INT_J1939_Message_List_ID = 82                             ; 
    DT_INT_J1939_Message_List_CycleTime = 83                      ; 
    DT_STR_J1939_Message_List_Name = 84                           ; 
    DT_STR_J1939_Message_List_Comment = 85                        ; 
    DT_INT_J1939_Message_List_TX_Node_Index = 86                  ; 
    DT_INT_J1939_Message_List_Owned_Signal_List_Count = 87        ; 
    DT_INT_J1939_Message_List_Owned_Signal_List_Signal_Index = 88 ; 
    DT_STR_J1939_Message_List_Struct = 89                         ; 
    DT_INT_90 = 90                                                ; 
    DT_INT_91 = 91                                                ; 
    DT_INT_92 = 92                                                ; 
    DT_INT_93 = 93                                                ; 
    DT_INT_94 = 94                                                ; 
    DT_INT_95 = 95                                                ; 
    DT_INT_96 = 96                                                ; 
    DT_INT_97 = 97                                                ; 
    DT_INT_98 = 98                                                ; 
    DT_INT_99 = 99                                                ; 
    DT_INT_Node_List_Address = 100                                ; 
    DT_STR_Node_List_Name = 101                                   ; 
    DT_STR_Node_List_Comment = 102                                ; 
    DT_INT_Node_List_TX_CAN_Message_List_Count = 103              ; 
    DT_INT_Node_List_TX_CAN_Message_List_Message_Index = 104      ; 
    DT_INT_Node_List_RX_CAN_Message_List_Count = 105              ; 
    DT_INT_Node_List_RX_CAN_Message_List_Message_Index = 106      ; 
    DT_INT_Node_List_TX_FD_Message_List_Count = 107               ; 
    DT_INT_Node_List_TX_FD_Message_List_Message_Index = 108       ; 
    DT_INT_Node_List_RX_FD_Message_List_Count = 109               ; 
    DT_INT_Node_List_RX_FD_Message_List_Message_Index = 110       ; 
    DT_INT_Node_List_TX_J1939_Message_List_Count = 111            ; 
    DT_INT_Node_List_TX_J1939_Message_List_Message_Index = 112    ; 
    DT_INT_Node_List_RX_J1939_Message_List_Count = 113            ; 
    DT_INT_Node_List_RX_J1939_Message_List_Message_Index = 114    ; 
    DT_INT_Node_List_TX_Signal_List_Count = 115                   ; 
    DT_INT_Node_List_TX_Signal_List_Signal_Index = 116            ; 
    DT_INT_Node_List_RX_Signal_List_Count = 117                   ; 
    DT_INT_Node_List_RX_Signal_List_Signal_Index = 118            ; 
    DT_STR_Node_List_Struct = 119                                 ; 
    DT_INT_120 = 120                                              ; 
    DT_INT_121 = 121                                              ; 
    DT_INT_122 = 122                                              ; 
    DT_INT_123 = 123                                              ; 
    DT_INT_124 = 124                                              ; 
    DT_INT_125 = 125                                              ; 
    DT_INT_126 = 126                                              ; 
    DT_INT_127 = 127                                              ; 
    DT_INT_128 = 128                                              ; 
    DT_INT_129 = 129                                              ; 
    DT_INT_EnvVar_List_Value_Type = 130                           ; 
    DT_DBL_EnvVar_List_MIN = 131                                  ; 
    DT_DBL_EnvVar_List_MAX = 132                                  ; 
    DT_DBL_EnvVar_List_Init_Value = 133                           ; 
    DT_STR_EnvVar_List_Name = 134                                 ; 
    DT_STR_EnvVar_List_Unit = 135                                 ; 
    DT_STR_EnvVar_List_Comment = 136                              ; 
    DT_STR_EnvVar_List_Struct = 137                               ; 
    DT_INT_138 = 138                                              ; 
    DT_INT_139 = 139                                              ; 
    DT_INT_ValTab_List_Item_List_Count = 140                      ; 
    DT_INT_ValTab_List_Item_List_Name = 141                       ; 
    DT_DBL_ValTab_List_Item_List_Value = 142                      ; 
    DT_STR_ValTab_List_Struct = 143                               ; 

    % load a dbc, the file name can be relative path to TSMaster.exe, the supported channels are separated by ','
    id = db.load_can_db(AFileName, '0,1');
    fprintf('CAN/CAN-FD database loaded with Id = %d\n', id);

    % to retrieve total count of database already loaded
    n = db.get_can_db_count();
    fprintf('Loaded CAN database count = %d\n', n);

    % to iterate each database and get its Id
    for i = 0 : n-1
        id = db.get_can_db_id(i);
        fprintf('Id of CAN database index %d is %d\n', i, id);
    end
    
    % start extracting
    fprintf('\nStart extracting...\n');

    % extract network info...
    % network name
    [result, s] = db.get_can_db_info(id, DT_STR_Network_Name, -1, -1);
    if check(result)
        fprintf('Network name: %s\n', s);
    end
    % loaded dbc file name
    [result, s] = db.get_can_db_info(id, DT_STR_DBC_FileName, -1, -1);
    if check(result)
        fprintf('Loaded dbc file name: %s\n', s);
    end
    % protocol name
    [result, s] = db.get_can_db_info(id, DT_INT_Protocol_Type, -1, -1);
    if check(result)
        fprintf('DBC protocol type: %s\n', s);
    end
    
        % extract signal list ---------------------------------------------------------
    [result, s] = db.get_can_db_info(id, DT_INT_Signal_List_Count, -1, -1);
    if check(result)
        fprintf('\nSignal list count: %s\n', s)
    end
    n = str2num(s);
    for i = 0 : n-1
        sl = '';
        % get signal name
        [result, s] = db.get_can_db_info(id, DT_STR_Signal_List_Name, i, -1);
        if check(result)
            sl = [sl, 'Signal: ', s, ', '];
        end
        % get signal's message's identifier
        [result, s] = db.get_can_db_info(id, DT_INT_Signal_List_Message_ID, i, -1);
        if check(result)
            sl = [sl, 'Msg. Id=', s, ', '];
        end
        % get signal value type, 0: unsigned int; 1: signed int; 2: IEEE float 32; 3: IEEE float 64
        [result, s] = db.get_can_db_info(id, DT_INT_Signal_List_Value_Type, i, -1);
        if check(result)
            sl = [sl, 'Value Type=', s, ', '];
        end
        % get signal byte order, 0: intel; 1: motorola
        [result, s] = db.get_can_db_info(id, DT_INT_Signal_List_Is_Motorola, i, -1);
        if check(result)
            sl = [sl, 'Is Motorola=', s, ', '];
        end
        % get signal value table index
        [result, s] = db.get_can_db_info(id, DT_INT_Signal_List_ValTab_Index, i, -1);
        if check(result)
            sl = [sl,  'VT Index=',  s , ', '];
        end
        % get signal start bit in message
        [result, s] = db.get_can_db_info(id, DT_INT_Signal_List_Layout_Start, i, -1);
        if check(result)
            sl = [sl,  'Start bit=',  s , ', '];
        end
        % get signal length
        [result, s] = db.get_can_db_info(id, DT_INT_Signal_List_Length, i, -1);
        if check(result)
            sl = [sl,  'Len=',  s , ', '];
        end
        % get signal factor
        [result, s] = db.get_can_db_info(id, DT_DBL_Signal_List_Factor, i, -1);
        if check(result)
            sl = [sl,  'Factor=',  s , ', '];
        end
        % get signal offset
        [result, s] = db.get_can_db_info(id, DT_DBL_Signal_List_Offset, i, -1);
        if check(result)
            sl = [sl,  'Offset=',  s , ', '];
        end
        % get signal init value
        [result, s] = db.get_can_db_info(id, DT_DBL_Signal_List_InitValue, i, -1);
        if check(result)
            sl = [sl,  'Init=',  s , ', '];
        end
        % get signal min value
        [result, s] = db.get_can_db_info(id, DT_DBL_Signal_List_Min, i, -1);
        if check(result)
            sl = [sl,  'Min=',  s , ', '];
        end
        % get signal max value
        [result, s] = db.get_can_db_info(id, DT_DBL_Signal_List_Max, i, -1);
        if check(result)
            sl = [sl,  'Max=',  s , ', '];
        end
        % get signal unit
        [result, s] = db.get_can_db_info(id, DT_STR_Signal_List_Unit, i, -1);
        if check(result)
            sl = [sl,  'Unit=',  s , ', '];
        end
        % get signal comment
        [result, s] = db.get_can_db_info(id, DT_STR_Signal_List_Comment, i, -1);
        if check(result)
            sl = [sl,  'Comment=',  s , ', '];
        end
        % get signal's message index in message list
        [result, s] = db.get_can_db_info(id, DT_INT_Signal_List_Message_Index, i, -1);
        if check(result)
            sl = [sl,  'Msg. Index=',  s , ', '];
        end
        % get signal's message type, 0=CAN, 1=CAN FD, 2=J1939
        [result, s] = db.get_can_db_info(id, DT_INT_Signal_List_Message_Type, i, -1);
        if check(result)
            sl = [sl,  'Msg. Type=',  s , ', '];
        end
        fprintf([sl, '\n']);
    end
    
    % extract classical CAN message list ------------------------------------------
    [result, s] = db.get_can_db_info(id, DT_INT_CAN_Message_List_Count, -1, -1);
    if check(result)
        fprintf('\nClassical CAN Message list count: %s\n', s);
    end
    n = str2num(s);
    m = 0;
    for i = 0 : n-1
        sl = '';
        % get message name
        [result, s] = db.get_can_db_info(id, DT_STR_CAN_Message_List_Name, i, -1);
        if check(result)
            sl = [sl , 'CAN Message: ' , s , ', '];
        end
        % get message type, cftStdCAN = 0, cftExtCAN = 1, cftJ1939 = 2, cftStdCANFD = 3, cftExtCANFD = 4
        [result, s] = db.get_can_db_info(id, DT_INT_CAN_Message_List_Type, i, -1);
        if check(result)
            sl = [sl , 'Type=' , s , ', '];
        end
        % get message dlc
        [result, s] = db.get_can_db_info(id, DT_INT_CAN_Message_List_DLC, i, -1);
        if check(result)
            sl = [sl , 'DLC=' , s , ', '];
        end
        % get message identifier
        [result, s] = db.get_can_db_info(id, DT_INT_CAN_Message_List_ID, i, -1);
        if check(result)
            sl = [sl , 'ID=' , s , ', '];
        end
        % get message cycle time
        [result, s] = db.get_can_db_info(id, DT_INT_CAN_Message_List_CycleTime, i, -1);
        if check(result)
            sl = [sl , 'Cycle=' , s , ', '];
        end
        % get message comment
        [result, s] = db.get_can_db_info(id, DT_STR_CAN_Message_List_Comment, i, -1);
        if check(result)
            sl = [sl , 'Comment=' , s , ', '];
        end
        % get message's tx node index
        [result, s] = db.get_can_db_info(id, DT_INT_CAN_Message_List_TX_Node_Index, i, -1);
        if check(result)
            sl = [sl , 'Tx Node Index=' , s , ', '];
        end
        % get signal count of message
        [result, s] = db.get_can_db_info(id, DT_INT_CAN_Message_List_Owned_Signal_List_Count, i, -1);
        if check(result) 
            sl = [sl , 'Signal Count=' , s , ', '];
            m = str2num(s);
        end
        fprintf(sl);
        % print out its signals
        if m > 0
            for j = 0 : m-1
                % get message's signal index in signal list
                [result, s] = db.get_can_db_info(id, DT_INT_CAN_Message_List_Owned_Signal_List_Signal_Index, i, j);
                if check(result)
                    sl = ['        Signal Index=' , s , ', '];
                    % get signal properties bundle
                    [result, s] = db.get_can_db_info(id, DT_STR_Signal_List_Struct, str2num(s), -1);
                    if check(result)
                        sl = [sl , s];
                        fprintf([sl, '\n']);
                    end
                end
            end
        end
    end 
    
    % extract FD CAN message list -------------------------------------------------
    [result, s] = db.get_can_db_info(id, DT_INT_CANFD_Message_List_Count, -1, -1);
    if check(result)
        fprintf('\nFD CAN Message list count: %s\n', s);
    end
    n = str2num(s);
    m = 0;
    for i = 0 : n-1
        sl = '';
        % get message name
        [result, s] = db.get_can_db_info(id, DT_STR_CANFD_Message_List_Name, i, -1);
        if check(result)
            sl = [sl , 'CANFD Message: ' , s , ', '];
        end
        % get message type, cftStdCAN = 0, cftExtCAN = 1, cftJ1939 = 2, cftStdCANFD = 3, cftExtCANFD = 4
        [result, s] = db.get_can_db_info(id, DT_INT_CANFD_Message_List_Type, i, -1);
        if check(result)
            sl = [sl , 'Type=' , s , ', '];
        end
        % get message dlc
        [result, s] = db.get_can_db_info(id, DT_INT_CANFD_Message_List_DLC, i, -1);
        if check(result)
            sl = [sl , 'DLC=' , s , ', '];
        end
        % get message identifier
        [result, s] = db.get_can_db_info(id, DT_INT_CANFD_Message_List_ID, i, -1);
        if check(result)
            sl = [sl , 'ID=' , s , ', '];
        end
        % get message cycle time
        [result, s] = db.get_can_db_info(id, DT_INT_CANFD_Message_List_CycleTime, i, -1);
        if check(result)
            sl = [sl , 'Cycle=' , s , ', '];
        end
        % get message comment
        [result, s] = db.get_can_db_info(id, DT_STR_CANFD_Message_List_Comment, i, -1);
        if check(result)
            sl = [sl , 'Comment=' , s , ', '];
        end
        % get message's tx node index
        [result, s] = db.get_can_db_info(id, DT_INT_CANFD_Message_List_TX_Node_Index, i, -1);
        if check(result)
            sl = [sl , 'Tx Node Index=' , s , ', '];
        end
        % get BRS flag
        [result, s] = db.get_can_db_info(id, DT_INT_CANFD_Message_List_BRS, i, -1);
        if check(result)
            sl = [sl , 'BRS=' , s , ', '];
        end
        % get signal count of message
        [result, s] = db.get_can_db_info(id, DT_INT_CANFD_Message_List_Owned_Signal_List_Count, i, -1);
        if check(result) 
            sl = [sl , 'Signal Count=' , s , ', '];
            m = str2num(s);
        end
        fprintf([sl, '\n']);
        % print out its signals
        if m > 0
            for j = 0 : m-1
                % get message's signal index in signal list
                [result, s] = db.get_can_db_info(id, DT_INT_CANFD_Message_List_Owned_Signal_List_Signal_Index, i, j);
                if check(result)
                    sl = ['        Signal Index=' , s , ', '];
                    % get signal properties bundle
                    [result, s] = db.get_can_db_info(id, DT_STR_Signal_List_Struct, str2num(s), -1);
                    if check(result)
                        sl = [sl , s];
                        fprintf([sl, '\n']);
                    end
                end
            end
        end
    end

    % extract J1939 CAN message list ----------------------------------------------
    [result, s] = db.get_can_db_info(id, DT_INT_CANJ1939_Message_List_Count, -1, -1);
    if check(result)
        fprintf('\nJ1939 CAN Message list count: %s', s);
    end
    n = str2num(s);
    m = 0;
    for i = 0 : n-1
        sl = '';
        % get message name
        [result, s] = db.get_can_db_info(id, DT_STR_J1939_Message_List_Name, i, -1);
        if check(result)
            sl = [sl , 'J1939 Message: ' , s , ', '];
        end
        % get message type, cftStdCAN = 0, cftExtCAN = 1, cftJ1939 = 2, cftStdCANFD = 3, cftExtCANFD = 4
        [result, s] = db.get_can_db_info(id, DT_INT_J1939_Message_List_Type, i, -1);
        if check(result)
            sl = [sl , 'Type=' , s , ', '];
        end
        % get message dlc
        [result, s] = db.get_can_db_info(id, DT_INT_J1939_Message_List_DLC, i, -1);
        if check(result)
            sl = [sl , 'DLC=' , s , ', '];
        end
        % get message identifier
        [result, s] = db.get_can_db_info(id, DT_INT_J1939_Message_List_ID, i, -1);
        if check(result)
            sl = [sl , 'ID=' , s , ', '];
        end
        % get message cycle time
        [result, s] = db.get_can_db_info(id, DT_INT_J1939_Message_List_CycleTime, i, -1);
        if check(result)
            sl = [sl , 'Cycle=' , s , ', '];
        end
        % get message comment
        [result, s] = db.get_can_db_info(id, DT_STR_J1939_Message_List_Comment, i, -1);
        if check(result)
            sl = [sl , 'Comment=' , s , ', '];
        end
        % get message's tx node index
        [result, s] = db.get_can_db_info(id, DT_INT_J1939_Message_List_TX_Node_Index, i, -1);
        if check(result)
            sl = [sl , 'Tx Node Index=' , s , ', '];
        end
        % get signal count of message
        [result, s] = db.get_can_db_info(id, DT_INT_J1939_Message_List_Owned_Signal_List_Count, i, -1);
        if check(result) 
            sl = [sl , 'Signal Count=' , s , ', '];
            m = str2num(s);
        end
        fprintf([sl, '\n']);
        % print out its signals
        if m > 0
            for j = 0 : m-1
                % get message's signal index in signal list
                [result, s] = db.get_can_db_info(id, DT_INT_J1939_Message_List_Owned_Signal_List_Signal_Index, i, j);
                if check(result)
                    sl = ['        Signal Index=' , s , ', '];
                    % get signal properties bundle
                    [result, s] = db.get_can_db_info(id, DT_STR_Signal_List_Struct, str2num(s), -1);
                    if check(result)
                        sl = [sl , s];
                        fprintf([sl, '\n']);
                    end
                end
            end
        end
    end

    % extract node list -----------------------------------------------------------
    [result, s] = db.get_can_db_info(id, DT_INT_Node_List_Count, -1, -1);
    if check(result)
        fprintf('\nNode list count: %s\n', s);
    end
    n = str2num(s);
    mTxCAN = 0;
    mRxCAN = 0;
    mTxFD = 0;
    mRxFD = 0;
    mTxJ1939 = 0;
    mRxJ1939 = 0;
    mTxSgn = 0;
    mRxSgn = 0;
    for i = 0 : n-1
        sl = '';
        % get node name
        [result, s] = db.get_can_db_info(id, DT_STR_Node_List_Name, i, -1);
        if check(result)
            sl = [sl , 'Node Name: ' , s , ', '];
        end
        % get node address
        [result, s] = db.get_can_db_info(id, DT_INT_Node_List_Address, i, -1);
        if check(result)
            sl = [sl , 'Node Address=' , s , ', '];
        end
        % get node comment
        [result, s] = db.get_can_db_info(id, DT_STR_Node_List_Comment, i, -1);
        if check(result)
            sl = [sl , 'Node Comment=' , s , ', '];
        end
        % get node's tx CAN message list
        [result, s] = db.get_can_db_info(id, DT_INT_Node_List_TX_CAN_Message_List_Count, i, -1);
        if check(result) 
            sl = [sl , 'Tx CAN msg. Count=' , s , ', '];
            mTxCAN = str2num(s)
        end
        % get node's rx CAN message list
        [result, s] = db.get_can_db_info(id, DT_INT_Node_List_RX_CAN_Message_List_Count, i, -1);
        if check(result)
            sl = [sl , 'Rx CAN msg. Count=' , s , ', '];
            mRxCAN = str2num(s)
        end
        % get node's tx CAN FD message list
        [result, s] = db.get_can_db_info(id, DT_INT_Node_List_TX_FD_Message_List_Count, i, -1);
        if check(result)
            sl = [sl , 'Tx CAN FD Count=' , s , ', '];
            mTxFD = str2num(s)
        end
        % get node's rx CAN FD message list
        [result, s] = db.get_can_db_info(id, DT_INT_Node_List_RX_FD_Message_List_Count, i, -1);
        if check(result)
            sl = [sl , 'Rx CAN FD Count=' , s , ', '];
            mRxFD = str2num(s)
        end
        % get node's tx CAN J1939 message list
        [result, s] = db.get_can_db_info(id, DT_INT_Node_List_TX_J1939_Message_List_Count, i, -1);
        if check(result)
            sl = [sl , 'Tx CAN J1939 Count=' , s , ', '];
            mTxJ1939 = str2num(s)
        end
        % get node's rx CAN J1939 message list
        [result, s] = db.get_can_db_info(id, DT_INT_Node_List_RX_J1939_Message_List_Count, i, -1);
        if check(result)
            sl = [sl , 'Rx CAN J1939 Count=' , s , ', '];
            mRxJ1939 = str2num(s)
        end
        % get node's tx signal list
        [result, s] = db.get_can_db_info(id, DT_INT_Node_List_TX_Signal_List_Count, i, -1);
        if check(result)
            sl = [sl , 'Tx sgn. Count=' , s , ', '];
            mTxSgn = str2num(s)
        end
        % get node's rx signal list
        [result, s] = db.get_can_db_info(id, DT_INT_Node_List_RX_Signal_List_Count, i, -1);
        if check(result)
            sl = [sl , 'Rx sgn. Count=' , s , ', '];
            mRxSgn = str2num(s)
        end
        fprintf([sl, '\n']);
        % print each tx CAN message
        for j = 0 : mTxCAN - 1
            [result, s] = db.get_can_db_info(id, DT_INT_Node_List_TX_CAN_Message_List_Message_Index, i, j);
            if check(result)
                sl = ['        Tx CAN Index: ' , s , ', Content='];
                [result, s] = db.get_can_db_info(id, DT_STR_CAN_Message_List_Struct, str2num(s), -1);
                if check(result)
                    sl = [sl , s];
                    fprintf([sl, '\n']);
                end
            end
        end        
        % print each rx CAN message
        for j = 0 : mRxCAN - 1
            [result, s] = db.get_can_db_info(id, DT_INT_Node_List_RX_CAN_Message_List_Message_Index, i, j);
            if check(result)
                sl = ['        Rx CAN Index: ' , s , ', Content='];
                [result, s] = db.get_can_db_info(id, DT_STR_CAN_Message_List_Struct, str2num(s), -1);
                if check(result)
                    sl = [sl , s];
                    fprintf([sl, '\n']);
                end
            end
        end
        % print each tx FD message
        for j = 0 : mTxFD - 1
            [result, s] = db.get_can_db_info(id, DT_INT_Node_List_TX_FD_Message_List_Message_Index, i, j);
            if check(result)
                sl = ['        Tx FD Index: ' , s , ', Content='];
                [result, s] = db.get_can_db_info(id, DT_STR_CANFD_Message_List_Struct, str2num(s), -1);
                if check(result)
                    sl = [sl , s];
                    fprintf([sl, '\n']);
                end
            end
        end
        % print each rx FD message
        for j = 0 : mRxFD - 1
            [result, s] = db.get_can_db_info(id, DT_INT_Node_List_RX_FD_Message_List_Message_Index, i, j);
            if check(result)
                sl = ['        Rx FD Index: ' , s , ', Content='];
                [result, s] = db.get_can_db_info(id, DT_STR_CANFD_Message_List_Struct, str2num(s), -1);
                if check(result)
                    sl = [sl , s];
                    fprintf([sl, '\n']);
                end
            end
        end
        % print each tx J1939 message
        for j = 0 : mTxJ1939 - 1
            [result, s] = db.get_can_db_info(id, DT_INT_Node_List_TX_J1939_Message_List_Message_Index, i, j);
            if check(result)
                sl = ['        Tx J1939 Index: ' , s , ', Content='];
                [result, s] = db.get_can_db_info(id, DT_STR_J1939_Message_List_Struct, str2num(s), -1);
                if check(result)
                    sl = [sl , s];
                    fprintf([sl, '\n']);
                end
            end
        end
        % print each rx J1939 message
        for j = 0 : mRxJ1939 - 1
            [result, s] = db.get_can_db_info(id, DT_INT_Node_List_RX_J1939_Message_List_Message_Index, i, j);
            if check(result)
                sl = ['        Rx J1939 Index: ' , s , ', Content='];
                [result, s] = db.get_can_db_info(id, DT_STR_J1939_Message_List_Struct, str2num(s), -1);
                if check(result)
                    sl = [sl , s];
                    fprintf([sl, '\n']);
                end
            end
        end
        % print each tx signal
        for j = 0 : mTxSgn - 1
            [result, s] = db.get_can_db_info(id, DT_INT_Node_List_TX_Signal_List_Signal_Index, i, j);
            if check(result)
                sl = ['        Tx signal Index: ' , s , ', Content='];
                [result, s] = db.get_can_db_info(id, DT_STR_Signal_List_Struct, str2num(s), -1);
                if check(result)
                    sl = [sl , s];
                    fprintf([sl, '\n']);
                end
            end
        end
        % print each rx signal
        for j = 0 : mRxSgn - 1
            [result, s] = db.get_can_db_info(id, DT_INT_Node_List_RX_Signal_List_Signal_Index, i, j);
            if check(result)
                sl = ['        Rx signal Index: ' , s , ', Content='];
                [result, s] = db.get_can_db_info(id, DT_STR_Signal_List_Struct, str2num(s), -1);
                if check(result)
                    sl = [sl , s];
                    fprintf([sl, '\n']);
                end
            end
        end
    end

    % extract environment variable list ---------------------------------------------------------
    [result, s] = db.get_can_db_info(id, DT_INT_EnvVar_List_Count, -1, -1);
    if check(result)
        fprintf('\nEnvironment variable list count: %s\n', s);
    end
    n = str2num(s);
    for i = 0 : n-1
        sl = '';
        % get environment variable name
        [result, s] = db.get_can_db_info(id, DT_STR_EnvVar_List_Name, i, -1);
        if check(result)
            sl = [sl , 'Environment variable: ' , s , ', '];
        end
        % get environment variable value type, 0: int; 1: float; 2: string; 3: data
        [result, s] = db.get_can_db_info(id, DT_INT_EnvVar_List_Value_Type, i, -1);
        if check(result)
            sl = [sl , 'type=' , s , ', '];
        end
        % get environment variable min value
        [result, s] = db.get_can_db_info(id, DT_DBL_EnvVar_List_MIN, i, -1);
        if check(result)
            sl = [sl , 'min=' , s , ', '];
        end
        % get environment variable max value
        [result, s] = db.get_can_db_info(id, DT_DBL_EnvVar_List_MAX, i, -1);
        if check(result)
            sl = [sl , 'max=' , s , ', '];
        end
        % get environment variable init value
        [result, s] = db.get_can_db_info(id, DT_DBL_EnvVar_List_Init_Value, i, -1);
        if check(result)
            sl = [sl , 'init=' , s , ', '];
        end
        % get environment variable unit
        [result, s] = db.get_can_db_info(id, DT_STR_EnvVar_List_Unit, i, -1);
        if check(result)
            sl = [sl , 'Unit=' , s , ', '];
        end
        % get environment variable comment
        [result, s] = db.get_can_db_info(id, DT_STR_EnvVar_List_Comment, i, -1);
        if check(result)
            sl = [sl , 'Comment=' , s , ', '];
        end
        fprintf([sl, '\n']);
    end
        
    % extract value table list ---------------------------------------------------------
    [result, s] = db.get_can_db_info(id, DT_INT_ValTab_List_Count, -1, -1);
    if check(result)
        fprintf('\nValue table list count: %s\n', s);
    end
    n = str2num(s);
    for i = 0 : n-1
        [result, s] = db.get_can_db_info(id, DT_INT_ValTab_List_Item_List_Count, i, -1);
        if check(result)
            fprintf('\nValue table index %d, count: %s\n', i, s);
            m = str2num(s);
            for j = 0 : m-1
                sl = '';
                % get value table name
                [result, s] = db.get_can_db_info(id, DT_INT_ValTab_List_Item_List_Name, i, j);
                if check(result)
                    sl = [sl , '    Name=' , s , ', '];
                end
                % get value table value
                [result, s] = db.get_can_db_info(id, DT_DBL_ValTab_List_Item_List_Value, i, j);
                if check(result)
                    sl = [sl , 'Value=' , s , ', '];
                end
                fprintf([sl, '\n']);
            end
        end
    end
                        
    % unload all databases
    db.unload_can_dbs();
    fprintf('\nAll CAN/CAN-FD databases unloaded\n');
end

