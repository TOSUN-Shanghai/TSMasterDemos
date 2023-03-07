#include <iostream>
#include <unistd.h>
#include "TSCANDef.hpp"
using namespace std;

#include <QDebug>
extern "C" void ReceiveCANMessage(const TLibCAN* AData);
extern "C" void ReceiveCANFDMessage(const TLibCANFD* AData);
int main()
{
    cout <<"libTSCAN Linux Api Demo"<<endl;
    initialize_lib_tscan(true,false,false);  //Intialization of libTSCAN Library
    uint32_t ADeviceCount;
    tscan_scan_devices(&ADeviceCount); 
    cout << "Online device num: "<<ADeviceCount << endl;
    char* AFManufacturer;
    char* AFProduct;
    char* AFSerial;
    for(uint32_t i = 0; i < ADeviceCount; i++)
    {
        tscan_get_device_info(
          i,
          &AFManufacturer,
          &AFProduct,
          &AFSerial
          );
        qDebug()<<"Manufacturer:"<<QString(AFManufacturer);
        qDebug()<<"Product No:"<<QString(AFProduct);
        qDebug()<<"Serial No:"<<QString(AFSerial);
    }

    if(ADeviceCount > 0)
    {

        u64 ADeviceHandle = 0x00;
        //const char * p = "";
        //u64 retValue = tscan_connect("", &ADeviceHandle);  //Connect default device
        u64 retValue = tscan_connect(AFSerial, &ADeviceHandle); //Connect the appointted device with serial no string: AFSerial
        if ((retValue == 0) || (retValue == 5))   //0:success; 5: isconnectted
        {
            qDebug()<<QString("Connect Device with handle:%1 connectted").arg(ADeviceHandle);
            {

                retValue = tscan_register_event_can(ADeviceHandle, ReceiveCANMessage);
                retValue = tscan_register_event_canfd(ADeviceHandle, ReceiveCANFDMessage);
                //Initlialization of baudrateL: arb: 500kbps, data:2000 kbps; controller:ISOFDCAN; mode:normal
                tscan_config_canfd_by_baudrate(ADeviceHandle, CHN1, 500,2000, lfdtISOCAN, lfdmNormal,1);
                tscan_config_canfd_by_baudrate(ADeviceHandle, CHN2, 500,2000, lfdtISOCAN, lfdmNormal,1);

                /*define classic can messge*/
                TLibCAN msg;
                msg.FIdentifier = 0x03;
                msg.FProperties.bits.remoteframe = 0x00; //not remote frame,standard frame
                msg.FProperties.bits.extframe = 0;
                msg.FDLC = 3;
                msg.FIdxChn = CHN1;
                /*Demo1: transmit can message*/
                for(int i = 0; i< 5; i++)
                {
                    msg.FIdentifier = i;
                    //retValue = tscan_transmit_can_async(ADeviceHandle, &msg);
                    if (retValue == 0)
                    {
                        qDebug()<<"CAN Device async send can message succes with id: "<<msg.FIdentifier;
                    }
                    else
                    {
                        qDebug()<<"CAN Device async send can message failed with id: "<<msg.FIdentifier;
                    }
                }
                /*define fdcan message*/
                TLibCANFD fdmsg;
                fdmsg.FIdentifier = 0x03;
                fdmsg.FProperties.bits.remoteframe = 0x00; //not remote frame,standard frame
                fdmsg.FProperties.bits.extframe = 0;
                fdmsg.FDLC = 3;
                fdmsg.FIdxChn = CHN1;
                fdmsg.FFDProperties.bits.EDL = 1; //FDMode
                fdmsg.FFDProperties.bits.BRS = 1;  //Open baudrate speed
                for(int i = 0; i< 5; i++)
                {
                    fdmsg.FIdentifier = i;
                    retValue = tscan_transmit_canfd_async(ADeviceHandle, &fdmsg);
                    if (retValue == 0)
                    {
                        qDebug()<<"CAN Device async send canfd message succes with id: "<<fdmsg.FIdentifier;
                    }
                    else
                    {
                        qDebug()<<"CAN Device async send canfd message failed with id: "<<fdmsg.FIdentifier;
                    }
                }
            }
            sleep(1);
            TLibCANFD readDataBuffer[20];  //Create buffers to save the data read from fifo of dirver
            int realDataSize = 20;
            //Reveive data from FIFO of Driver
            if(tsfifo_receive_canfd_msgs(ADeviceHandle,readDataBuffer,&realDataSize,CHN1,1) == 0x00)
            {
                for(int i = 0; i< realDataSize; i++)
                {
                    qDebug()<<"read frame from fifo with id 0x"<<QString::number(readDataBuffer[i].FIdentifier, 16);
                }
            }
            retValue = tscan_disconnect_by_handle(ADeviceHandle);
            if (retValue == 0)
            {
                qDebug()<<QString("Disconnect device with handle:%1 connectted").arg(ADeviceHandle);
            }
            finalize_lib_tscan();
            qDebug()<<QString("finalize libtscan driver and exit the tester program");
        }
    }
    return 0;
}

//Receive data in recall function: CANMessage Received Event
void ReceiveCANMessage(const TLibCAN* AData)
{
    if(AData->FProperties.bits.istx)
      qDebug()<<"tx frame with id 0x"<<QString::number(AData->FIdentifier, 16);
    else
      qDebug()<<"rx frame with id 0x"<<QString::number(AData->FIdentifier, 16);
}

//Receive data in recall function: CANMFDessage Received Event
void ReceiveCANFDMessage(const TLibCANFD* AFDData)
{
    if(AFDData->FProperties.bits.istx)
       qDebug()<<"tx frame with id 0x"<<QString::number(AFDData->FIdentifier, 16);
    else
       qDebug()<<"rx frame with id 0x"<<QString::number(AFDData->FIdentifier, 16);
}
