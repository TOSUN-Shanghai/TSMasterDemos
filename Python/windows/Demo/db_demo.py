import TSMasterAPI as TS

ret = TS.initialize_lib_tsmaster(b"TSMaster")

TS.tsdb_unload_can_dbs()
TS.tsdb_unload_lin_dbs()
TS.tsdb_unload_flexray_dbs()

candb_AId = TS.c_int32(0)
lindb_AId = TS.c_int32(0)
flexraydb_AId = TS.c_int32(0)

ret = TS.tsdb_load_can_db(b"D:\\IDE\\TSMasterAPI\\TSMasterApi\\databases\\CAN_FD_Powertrain.dbc",b'0',candb_AId)
ret = TS.tsdb_load_lin_db(b"D:\\IDE\\TSMasterAPI\\TSMasterApi\\databases\\LINDemo.ldf",b'0',lindb_AId)
ret = TS.tsdb_load_flexray_db(b"D:\\IDE\\TSMasterAPI\\TSMasterApi\\databases\\PowerTrain_v2.xml",b'0',flexraydb_AId)
db_count = TS.c_int32(0)
ret = TS.tsdb_get_can_db_count(db_count)
Frame = {}
for i in range(db_count.value) :
    db = TS.TDBProperties()
    db.FDBIndex = i
    TS.tsdb_get_can_db_properties_by_index(db)
    Frame['CAN'] = {}
    for Frame_id in range(db.FFrameCount):
        frame = TS.TDBFrameProperties()
        ret = TS.tsdb_get_can_db_frame_properties_by_db_index(i,Frame_id,frame)
        Frame['CAN'][frame.FName] ={}
        for singal_index in range(frame.FSignalCount):
            Signal = TS.TDBSignalProperties()
            ret = TS.tsdb_get_can_db_signal_properties_by_frame_index(i,Frame_id,singal_index,Signal)
            Frame['CAN'][frame.FName][Signal.FName] = Signal.FCANSignal


for i in range(db_count.value) :
    db = TS.TDBProperties()
    db.FDBIndex = i
    TS.tsdb_get_can_db_properties_by_index(db)
    for ecu_count_index in range(db.FECUCount):
        Ecu = TS.TDBECUProperties()
        Ecu.FDBIndex = i
        Ecu.FECUIndex = ecu_count_index
        TS.tsdb_get_can_db_ecu_properties_by_index(Ecu)
        for tx_frame_index in range(Ecu.FTxFrameCount):
            TXframe = TS.TDBFrameProperties()
            TXframe.FDBIndex = i
            TXframe.FECUIndex = ecu_count_index
            TXframe.FFrameIndex = tx_frame_index
            TXframe.FIsTx = 1
            TS.tsdb_get_can_db_frame_properties_by_index(TXframe)
            for tx_singal_index in range(TXframe.FSignalCount):
                TXSignal = TS.TDBSignalProperties()
                TXSignal.FDBIndex = i
                TXSignal.FECUIndex = ecu_count_index
                TXSignal.FFrameIndex = tx_frame_index
                TXSignal.FSignalIndex = tx_singal_index
                TXSignal.FIsTx = 1
                TS.tsdb_get_can_db_signal_properties_by_index(TXSignal)

        for rx_frame_index in range(Ecu.FRxFrameCount):
            RXframe = TS.TDBFrameProperties()
            RXframe.FDBIndex = i
            RXframe.FECUIndex = ecu_count_index
            RXframe.FFrameIndex = rx_frame_index
            RXframe.FIsTx = 0
            TS.tsdb_get_can_db_frame_properties_by_index(RXframe)
            for rx_singal_index in range(RXframe.FSignalCount):
                RXSignal = TS.TDBSignalProperties()
                RXSignal.FDBIndex = i
                RXSignal.FECUIndex = ecu_count_index
                RXSignal.FFrameIndex = rx_frame_index
                RXSignal.FSignalIndex = rx_singal_index
                RXSignal.FIsTx = 0
                TS.tsdb_get_can_db_signal_properties_by_index(RXSignal)
ret = TS.tsdb_get_lin_db_count(db_count)

for i in range(db_count.value) :
    db = TS.TDBProperties()
    db.FDBIndex = i
    TS.tsdb_get_lin_db_properties_by_index(db)
    Frame['LIN'] = {}
    for Frame_id in range(db.FFrameCount):
        frame = TS.TDBFrameProperties()
        ret = TS.tsdb_get_lin_db_frame_properties_by_db_index(i,Frame_id,frame)
        Frame['LIN'][frame.FName] ={}
        for singal_index in range(frame.FSignalCount):
            Signal = TS.TDBSignalProperties()
            ret = TS.tsdb_get_lin_db_signal_properties_by_frame_index(i,Frame_id,singal_index,Signal)
            Frame['LIN'][frame.FName][Signal.FName] = Signal.FLINSignal

for i in range(db_count.value) :
    db = TS.TDBProperties()
    db.FDBIndex = i
    TS.tsdb_get_lin_db_properties_by_index(db)
    for ecu_count_index in range(db.FECUCount):
        Ecu = TS.TDBECUProperties()
        Ecu.FDBIndex = i
        Ecu.FECUIndex = ecu_count_index
        TS.tsdb_get_lin_db_ecu_properties_by_index(Ecu)
        for tx_frame_index in range(Ecu.FTxFrameCount):
            TXframe = TS.TDBFrameProperties()
            TXframe.FDBIndex = i
            TXframe.FECUIndex = ecu_count_index
            TXframe.FFrameIndex = tx_frame_index
            TXframe.FIsTx = 1
            TS.tsdb_get_lin_db_frame_properties_by_index(TXframe)
            for tx_singal_index in range(TXframe.FSignalCount):
                TXSignal = TS.TDBSignalProperties()
                TXSignal.FDBIndex = i
                TXSignal.FECUIndex = ecu_count_index
                TXSignal.FFrameIndex = tx_frame_index
                TXSignal.FSignalIndex = tx_singal_index
                TXSignal.FIsTx = 1
                TS.tsdb_get_lin_db_signal_properties_by_index(TXSignal)

        for rx_frame_index in range(Ecu.FRxFrameCount):
            RXframe = TS.TDBFrameProperties()
            RXframe.FDBIndex = i
            RXframe.FECUIndex = ecu_count_index
            RXframe.FFrameIndex = rx_frame_index
            RXframe.FIsTx = 0
            TS.tsdb_get_lin_db_frame_properties_by_index(RXframe)
            for rx_singal_index in range(RXframe.FSignalCount):
                RXSignal = TS.TDBSignalProperties()
                RXSignal.FDBIndex = i
                RXSignal.FECUIndex = ecu_count_index
                RXSignal.FFrameIndex = rx_frame_index
                RXSignal.FSignalIndex = rx_singal_index
                RXSignal.FIsTx = 0
                TS.tsdb_get_lin_db_signal_properties_by_index(RXSignal)
ret = TS.tsdb_get_flexray_db_count(db_count)

for i in range(db_count.value) :
    db = TS.TDBProperties()
    db.FDBIndex = i
    TS.tsdb_get_flexray_db_properties_by_index(db)
    Frame['Flexray'] = {}
    for Frame_id in range(db.FFrameCount):
        frame = TS.TDBFrameProperties()
        ret = TS.tsdb_get_flexray_db_frame_properties_by_db_index(i,Frame_id,frame)
        Frame['Flexray'][frame.FName] ={}
        for singal_index in range(frame.FSignalCount):
            Signal = TS.TDBSignalProperties()
            ret = TS.tsdb_get_flexray_db_signal_properties_by_frame_index(i,Frame_id,singal_index,Signal)
            Frame['Flexray'][frame.FName][Signal.FName] = Signal.FFlexRaySignal
            
for i in range(db_count.value) :
    db = TS.TDBProperties()
    db.FDBIndex = i
    TS.tsdb_get_flexray_db_properties_by_index(db)
    for ecu_count_index in range(db.FECUCount):
        Ecu = TS.TDBECUProperties()
        Ecu.FDBIndex = i
        Ecu.FECUIndex = ecu_count_index
        TS.tsdb_get_flexray_db_ecu_properties_by_index(Ecu)
        for tx_frame_index in range(Ecu.FTxFrameCount):
            TXframe = TS.TDBFrameProperties()
            TXframe.FDBIndex = i
            TXframe.FECUIndex = ecu_count_index
            TXframe.FFrameIndex = tx_frame_index
            TXframe.FIsTx = 1
            TS.tsdb_get_flexray_db_frame_properties_by_index(TXframe)
            for tx_singal_index in range(TXframe.FSignalCount):
                TXSignal = TS.TDBSignalProperties()
                TXSignal.FDBIndex = i
                TXSignal.FECUIndex = ecu_count_index
                TXSignal.FFrameIndex = tx_frame_index
                TXSignal.FSignalIndex = tx_singal_index
                TXSignal.FIsTx = 1
                TS.tsdb_get_flexray_db_signal_properties_by_index(TXSignal)

        for rx_frame_index in range(Ecu.FRxFrameCount):
            RXframe = TS.TDBFrameProperties()
            RXframe.FDBIndex = i
            RXframe.FECUIndex = ecu_count_index
            RXframe.FFrameIndex = rx_frame_index
            RXframe.FIsTx = 0
            TS.tsdb_get_flexray_db_frame_properties_by_index(RXframe)
            for rx_singal_index in range(RXframe.FSignalCount):
                RXSignal = TS.TDBSignalProperties()
                RXSignal.FDBIndex = i
                RXSignal.FECUIndex = ecu_count_index
                RXSignal.FFrameIndex = rx_frame_index
                RXSignal.FSignalIndex = rx_singal_index
                RXSignal.FIsTx = 0
                TS.tsdb_get_flexray_db_signal_properties_by_index(RXSignal)





TS.finalize_lib_tsmaster()

