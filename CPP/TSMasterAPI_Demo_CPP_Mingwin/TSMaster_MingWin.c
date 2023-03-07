#include "TSMaster_MingWin.h"

// load data bytes -------------------------------------------
void can_load_data_array(PCAN ACANData, u8* a) {
    for (u32 i = 0; i < 8; i++) {
        ACANData->FData[i] = *a++;
    }
}
void can_set_data(PCAN ACANData,  const u8 d0, const u8 d1, const u8 d2, const u8 d3, const u8 d4, const u8 d5, const u8 d6, const u8 d7) {
    ACANData->FData[0] = d0;
    ACANData->FData[1] = d1;
    ACANData->FData[2] = d2;
    ACANData->FData[3] = d3;
    ACANData->FData[4] = d4;
    ACANData->FData[5] = d5;
    ACANData->FData[6] = d6;
    ACANData->FData[7] = d7;
}
// initialize with standard identifier -----------------------
void can_init_w_std_id(PCAN ACANData,  s32 AId, s32 ADLC) {
    ACANData->FIdxChn = 0;
    ACANData->FIdentifier = AId;
    ACANData->FDLC = ADLC;
    ACANData->FReserved = 0;
    ACANData->FProperties = 0;
    set_rx(ACANData);
    set_standard(ACANData);
    set_data(ACANData);
    *(u64*)(&(ACANData->FData[0])) = 0;
    ACANData->FTimeUs = 0;
}
// initialize with extended identifier -----------------------
void can_init_w_ext_id(PCAN ACANData, s32 AId, s32 ADLC) {
    ACANData->FIdxChn = 0;
    ACANData->FIdentifier = AId;
    ACANData->FDLC = ADLC;
    ACANData->FReserved = 0;
    ACANData->FProperties = 0;
    set_rx(ACANData);
    set_extended(ACANData);
    set_data(ACANData);
    *(u64*)(&(ACANData->FData[0])) = 0;
    ACANData->FTimeUs = 0;
}

// load data bytes -------------------------------------------
void canfd_load_data(PCANFD ACANFDData, u8* a) {
    for (u32 i = 0; i < 64; i++) {
        ACANFDData->FData[i] = *a++;
    }
}
// initialize with standard identifier -----------------------
void canfd_init_w_std_id(PCANFD ACANFDData, s32 AId, s32 ADLC) {
    s32 i;
    ACANFDData->FIdxChn = 0;
    ACANFDData->FIdentifier = AId;
    ACANFDData->FDLC = ADLC;
    ACANFDData->FProperties = 0;
    ACANFDData->FFDProperties = MASK_CANFDProp_IS_FD;
    set_rx(ACANFDData);
    set_standard(ACANFDData);
    set_data(ACANFDData);
    for (i = 0; i < 64; i++) ACANFDData->FData[i] = 0;
    ACANFDData->FTimeUs = 0;
}
// initialize with extended identifier -----------------------
void canfd_init_w_ext_id(PCANFD ACANFDData, s32 AId, s32 ADLC) {
    s32 i;
    ACANFDData->FIdxChn = 0;
    ACANFDData->FIdentifier = AId;
    ACANFDData->FDLC = ADLC;
    ACANFDData->FFDProperties = MASK_CANFDProp_IS_FD;
    ACANFDData->FProperties = 0;
    set_rx(ACANFDData);
    set_extended(ACANFDData);
    set_data(ACANFDData);
    for (i = 0; i < 64; i++) ACANFDData->FData[i] = 0;
    ACANFDData->FTimeUs = 0;
}
// get fd data length ----------------------------------------
s32 canfd_get_data_length(PCANFD ACANFDData) {
    s32 l = MIN(ACANFDData->FDLC, 15);
    l = MAX(l, 0);
    return DLC_DATA_BYTE_CNT[l];
}



// initialize with identifier --------------------------------
void init_w_id(PLIN ALINData, const s32 AId, const s32 ADLC) {
    ALINData->FIdxChn = 0;
    ALINData->FErrStatus = 0;
    ALINData->FProperties = 0;
    ALINData->FDLC = ADLC;
    ALINData->FIdentifier = AId;
    *(__int64*)(&(ALINData->FData[0])) = 0;
    ALINData->FChecksum = 0;
    ALINData->FStatus = 0;
    ALINData->FTimeUs = 0;
}

// load data bytes -------------------------------------------
void load_data(PLIN ALINData, u8* a) {
    for (u32 i = 0; i < 8; i++) {
        ALINData->FData[i] = *a++;
    }
}

//Mapping
void HWMapping_Init(PLIBTSMapping AMapping) {
    s32 i;
    for (i = 0; i < APP_DEVICE_NAME_LENGTH; i++) {
        AMapping->FAppName[i] = 0;
        AMapping->FHWDeviceName[i] = 0;
    }
    AMapping->FAppChannelIndex = 0;
    AMapping->FAppChannelType = APP_CAN;
    AMapping->FHWDeviceType = TS_USB_DEVICE;
    AMapping->FHWIndex = 0;
    AMapping->FHWChannelIndex = 0;
    AMapping->FHWDeviceSubType = 0;
    AMapping->FMappingDisabled = false;
}
