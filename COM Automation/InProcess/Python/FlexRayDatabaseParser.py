import win32com.client
import pythoncom
import win32api
import time
import os
from win32com.client import VARIANT

FIBEX_File_FLEXRAY = r'.\Data\Demo\Databases\PowerTrain_v2.xml'

def check(AResult):
    if 0 == AResult:
        return True
    else:
        print('Query error with result', AResult)
        return False

def parse_fibex(db, AFileName):
    # load a fibex, the file name can be relative path to TSMaster.exe, the supported channels are separated by ','
    id = db.load_flexray_db(AFileName, '0,1')
    print('FlexRay database loaded with Id =', id)

    # to retrieve total count of database already loaded
    n = db.get_flexray_db_count()
    print('Loaded FlexRay database count =', n)

    # to iterate each database and get its Id
    for i in range(n):
        id = db.get_flexray_db_id(i)
        print('Id of FlexRay database index', i, 'is', id)

    # start extracting
    print('\nStart extracting...')

    # extract network info...
    # each network info
    sgnCount, fmeCount, ecuCount, supportedChannelMask, flags, sName, sComment = db.get_flexray_db_properties_by_index(0)
    print('Network name:', sName, ', Network comment:', sComment, ', signal count =', sgnCount, ', frame count =', fmeCount, ', ecu count =', ecuCount)

    # each ecu info
    for idxECU in range(ecuCount):
        ATxFrameCount, ARxFrameCount, sName, sComment = db.get_flexray_ecu_properties_by_index(0, idxECU)
        print('  ECU', idxECU+1, ', name:', sName, ', comment:', sComment, ', tx frame count:', ATxFrameCount, ', rx frame count:', ARxFrameCount)
        # each tx frame info
        for idxFme in range(ATxFrameCount):
            chnMask, baseCycle, cycleRep, isStartup, slotId, cycleMask, sgnCount, dlc, sName, sComment = db.get_flexray_frame_properties_by_index(0, idxECU, idxFme, True)
            print('    Tx Frame', sName, ', comment:', sComment, ', base cycle:', baseCycle, ', cycle repetition:', cycleRep, ', slot Id:', slotId, ', cycle mask:', hex(cycleMask), ', signal count:', sgnCount)
            # each tx signal info
            for idxSgn in range(sgnCount):
                sgnType, compuMethod, isIntel, startBit, updateBit, sgnLen, factor, offset, initValue, sName, sComment = db.get_flexray_signal_properties_by_index(0, idxECU, idxFme, idxSgn, True)
                print('      Tx Signal', sName, ', comment:', sComment, ', start bit:', startBit, ', len:', sgnLen, ', factor:', factor, ', offset:', offset)                
        for idxFme in range(ARxFrameCount):
            chnMask, baseCycle, cycleRep, isStartup, slotId, cycleMask, sgnCount, dlc, sName, sComment = db.get_flexray_frame_properties_by_index(0, idxECU, idxFme, False)
            print('    Rx Frame', sName, ', comment:', sComment, ', base cycle:', baseCycle, ', cycle repetition:', cycleRep, ', slot Id:', slotId, ', cycle mask:', hex(cycleMask), ', signal count:', sgnCount)
            # each rx signal info
            for idxSgn in range(sgnCount):
                sgnType, compuMethod, isIntel, startBit, updateBit, sgnLen, factor, offset, initValue, sName, sComment = db.get_flexray_signal_properties_by_index(0, idxECU, idxFme, idxSgn, False)
                print('      Rx Signal', sName, ', comment:', sComment, ', start bit:', startBit, ', len:', sgnLen, ', factor:', factor, ', offset:', offset)


# retrieve TSMaster application management
#pythoncom.CoInitialize() # enable multithread
app = win32com.client.Dispatch("comTSMaster.TSApplication")
# retrieve db kernel
db = app.TSDB()
# parse fibex file
db.unload_flexray_dbs()
parse_fibex(db, FIBEX_File_FLEXRAY)

