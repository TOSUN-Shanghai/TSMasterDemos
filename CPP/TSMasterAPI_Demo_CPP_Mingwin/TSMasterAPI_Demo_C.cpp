// test_tscan_dll.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include <iostream>
#include <windows.h>  
#include "TSMasterApi.h"


#define TEST_CAN_API
#define TEST_LIN_API

extern void ProcessLINMsg(TLIBLIN AMsg);

/// <summary>
/// CAN报文接收回调函数
/// </summary>
/// <param name="AData">CAN报文指针</param>
/// <returns></returns>
void __stdcall ReceiveCANMessage(const TLIBCAN* AData)
{

}

/*如果注册了本函数，当驱动收到了一帧LIN报文过后，就会触发此函数*/
/// <summary>
/// LIN报文接收回调函数
/// </summary>
/// <param name="AData">LIN报文指针</param>
/// <returns></returns>
void __stdcall ReceiveLINMessage(const TLIBLIN* AData)
{
	//通过回调函数读取数据
	printf("Receive Recall\n");
	ProcessLINMsg(*AData);
}


/*如果注册了本函数，当驱动收到了一帧LIN报文过后，就会触发此函数*/
/// <summary>
/// LIN报文接收回调函数
/// </summary>
/// <param name="AData">LIN报文指针</param>
/// <returns></returns>
void __stdcall ReceiveFastLINMessage(const TLIBLIN* AData)
{
	//通过回调函数读取数据
	printf("Receive FastLIN Recall\n");
	ProcessLINMsg(*AData);
}

/// <summary>
/// 处理收到的LIN报文数据
/// </summary>
/// <param name="AMsg">LIN报文</param>
/// <returns></returns>
void ProcessLINMsg(TLIBLIN AMsg)
{
	if (AMsg.FProperties.bits.istx)
	{
		printf("Translate message:");
	}
	else
	{
		printf("Receive message:");
	}
	printf("ID:%x ", AMsg.FIdentifier);
	printf("Datalength:%d ", AMsg.FDLC);
	printf("Datas:");
	for (int i = 0; i < AMsg.FDLC; i++)
	{
		printf(" %x", AMsg.FData.d[i]);
	}
	printf("\n");
}


void TestLINAPI(HMODULE hDll, size_t ADeviceHandle)
{
	uint32_t retValue;
	/*定义CAN发送报文，并填充数据*/
	TLIBLIN msg;
	//把当前设备设置为主节点模式：主节点模式下，才能够主动调度报文，发送报文头等
	lin_set_node_funtiontype_t setfunctionType = (lin_set_node_funtiontype_t)GetProcAddress(hDll, "lin_set_node_funtiontype");
	if (setfunctionType != NULL)
	{
		retValue = setfunctionType(ADeviceHandle, 0, (u8)MasterNode); //set as master node
		if (retValue == 0)
		{
			printf("LIN Device with handle:%zu set function type success\n", ADeviceHandle);
		}
		else
		{
			printf("LIN Device with handle:%zu set function type failed\n", ADeviceHandle);
		}
	}
	//清除内部ldf文件
	lin_apply_download_new_ldf_t appnewldf = (lin_apply_download_new_ldf_t)GetProcAddress(hDll, "lin_apply_download_new_ldf");
	if (appnewldf != NULL)
	{
		retValue = appnewldf(ADeviceHandle, 0);
		if (retValue == 0)
		{
			printf("LIN Device with handle:%zu apply new ldf callback success\n", ADeviceHandle);
		}
		else
		{
			printf("LIN Device with handle:%zu apply new ldf callback failed\n", ADeviceHandle);
		}
	}
	//注册接收回调函数：类似于接收中断
	RegisterLINRecvCallback_Win32_t registerRevCallback = (RegisterLINRecvCallback_Win32_t)GetProcAddress(hDll, "RegisterLINRecvCallback_Win32");
	if (registerRevCallback != NULL)
	{
		retValue = registerRevCallback(ADeviceHandle, ReceiveLINMessage);
		if (retValue == 0)
		{
			printf("LIN Device with handle:%zu register rev callback success\n", ADeviceHandle);
		}
		else
		{
			printf("LIN Device with handle:%zu register rev callback failed\n", ADeviceHandle);
		}
	}
	//注册FalstLIN接收回调函数：类似于接收中断
	RegisterFastLINRecvCallback_Win32_t registerFastLINRevCallback = (RegisterFastLINRecvCallback_Win32_t)GetProcAddress(hDll, "RegisterFastLINRecvCallback");
	if (registerFastLINRevCallback != NULL)
	{
		retValue = registerFastLINRevCallback(ADeviceHandle, ReceiveFastLINMessage);
		if (retValue == 0)
		{
			printf("LIN Device with handle:%zu register rev callback success\n", ADeviceHandle);
		}
		else
		{
			printf("LIN Device with handle:%zu register rev callback failed\n", ADeviceHandle);
		}
	}
	//设置波特率
	SetLINBaudrateByRate_t setBaudrate = (SetLINBaudrateByRate_t)GetProcAddress(hDll, "SetLINBaudrateByRate");
	if (setBaudrate != NULL)
	{
		retValue = setBaudrate(ADeviceHandle, 0, 100);  //100kbps
		if (retValue == 0)
		{
			printf("LIN Device with handle:%zu set baudrate success\n", ADeviceHandle);
		}
		else
		{
			printf("LIN Device with handle:%zu set baudrate failed\n", ADeviceHandle);
		}
	}
	//同步函数发送LIN报文
	msg.FIdentifier = 0x3C;
	msg.FDLC = 3;
	msg.FIdxChn = 0;
	msg.FProperties.value = 0x00;
	msg.FProperties.bits.istx = 1;
	msg.FData.d[0] = (byte)0x12;
	msg.FData.d[1] = (byte)0x34;
	msg.FData.d[2] = (byte)0x56;
	SendLINSync_t sendMsgSync = (SendLINSync_t)GetProcAddress(hDll, "SendLINSync");
	if (sendMsgSync != NULL)
	{
		retValue = sendMsgSync(ADeviceHandle, &msg, 500);
		if (retValue == 0)
		{
			printf("LIN Device with handle:%zu sync send lin message success\n", ADeviceHandle);
		}
		else
		{
			printf("LIN Device with handle:%zu sync send lin message failed\n", ADeviceHandle);
		}
	}
	//LIN Receive Function
	Sleep(3);
	ReceiveLINMsgs_t receiveFunc = (ReceiveLINMsgs_t)GetProcAddress(hDll, "ReceiveLINMsgs");
	TLIBLIN recMessageBuffs[5];
	if (receiveFunc != NULL)
	{
		//直接读取数据
		retValue = receiveFunc(ADeviceHandle, recMessageBuffs, 5, CHN1, ONLY_RX_DATA);
		printf("%d  messages received\n", retValue);
		for (int i = 0; i < (int)retValue; i++)
		{
			ProcessLINMsg(recMessageBuffs[i]);
		}
	}
	//注意：对于LIN总线来说，如果要接收报文，也要调用报文发送函数sendMsgAsync，把istx设置为0，实际上
	//是把报文帧头发送出去并读取总线上的报文
	msg.FIdentifier = 0x31;
	msg.FProperties.value = 0x00;
	msg.FProperties.bits.istx = 0; // as rx frame
	msg.FDLC = 3;
	msg.FIdxChn = 0;
	SendLINASync_t sendMsgASync = (SendLINASync_t)GetProcAddress(hDll, "SendLINASync");  //异步函数发送LIN报文
	if (sendMsgASync != NULL)
	{
		retValue = sendMsgASync(ADeviceHandle, &msg);
		if (retValue == 0)
		{
			printf("LIN Device with handle:%zu async send lin message success\n", ADeviceHandle);
		}
		else
		{
			printf("LIN Device with handle:%zu async send lin message failed\n", ADeviceHandle);
		}
	}
	//对于接收类型的报文，如果从节点没有及时回复，则retValue =0,接收失败
	Sleep(10);
	if (receiveFunc != NULL)
	{
		retValue = 0;
		int cnt = 0;
		//采用延时等待的方式，直到读取到LIN报文或者超时
		while ((retValue == 0) && (cnt < 100))
		{
			retValue = receiveFunc(ADeviceHandle, recMessageBuffs, 5, CHN1, ONLY_RX_DATA);
			cnt++;
			Sleep(10);
		}
		//如果超时都还收不到数据，则接收数据失败
		printf("%d  messages received\n", retValue);
		for (int i = 0; i < (int)retValue; i++)
		{
			ProcessLINMsg(recMessageBuffs[i]);
		}
	}
	msg.FIdentifier = 0x32;
	SendFastLINAsync_t sendFastLINMsgAsync = (SendFastLINAsync_t)GetProcAddress(hDll, "SendFastLINAsync");  //异步函数发送LIN报文
	if (sendFastLINMsgAsync != NULL)
	{
		retValue = sendFastLINMsgAsync(ADeviceHandle, &msg);
		if (retValue == 0)
		{
			printf("LIN Device with handle:%zu async fast lin send lin message success\n", ADeviceHandle);
		}
		else
		{
			printf("LIN Device with handle:%zu async fast lin send lin message failed\n", ADeviceHandle);
		}
	}
	//对于接收类型的报文，如果从节点没有及时回复，则retValue =0,接收失败
	ReceiveFastLINMsgs_t receiveFastLINFunc = (ReceiveFastLINMsgs_t)GetProcAddress(hDll, "ReceiveFastLINMsgs");
	Sleep(10);
	if (receiveFastLINFunc != NULL)
	{
		retValue = 0;
		int cnt = 0;
		//采用延时等待的方式，直到读取到LIN报文或者超时
		while ((retValue == 0) && (cnt < 100))
		{
			retValue = receiveFastLINFunc(ADeviceHandle, recMessageBuffs, 5, CHN1, ONLY_RX_DATA);
			cnt++;
			Sleep(10);
		}
		//如果超时都还收不到数据，则接收数据失败
		printf("%d  messages received\n", retValue);
		for (int i = 0; i < (int)retValue; i++)
		{
			ProcessLINMsg(recMessageBuffs[i]);
		}
	}
	//反注册接收回调函数
	UnregisterLINRecvCallback_Win32_t unregisterRevCallback = (UnregisterLINRecvCallback_Win32_t)GetProcAddress(hDll, "UnregisterLINRecvCallback_Win32");
	if (unregisterRevCallback != NULL)
	{
		retValue = unregisterRevCallback(ADeviceHandle, ReceiveLINMessage);
		if (retValue == 0)
		{
			printf("LIN Device with handle:%zu unregister rev callback success\n", ADeviceHandle);
		}
		else
		{
			printf("LIN Device with handle:%zu unregister rev callback failed\n", ADeviceHandle);
		}
	}
	//反注册FastLIN接收回调函数
	UnRegisterFastLINRecvCallback_Win32_t unregisterFastLINRevCallback = (UnRegisterFastLINRecvCallback_Win32_t)GetProcAddress(hDll, "UnRegisterFastLINRecvCallback");
	if (unregisterFastLINRevCallback != NULL)
	{
		retValue = unregisterFastLINRevCallback(ADeviceHandle, ReceiveFastLINMessage);
		if (retValue == 0)
		{
			printf("LIN Device with handle:%zu unregister rev callback success\n", ADeviceHandle);
		}
		else
		{
			printf("LIN Device with handle:%zu unregister rev callback failed\n", ADeviceHandle);
		}
	}
}


void TestCANAPI(HMODULE hDll, size_t ADeviceHandle)
{
	uint32_t retValue;
	/*定义CAN发送报文，并填充数据*/
	TLIBCAN msg;
	msg.FIdentifier = 0x03;
	msg.FProperties.bits.remoteframe = 0x00; //not remote frame,standard frame
	msg.FProperties.bits.extframe = 0;
	msg.FDLC = 3;
	msg.FIdxChn = 0;
	//注册接收回调函数：类似于接收中断
	RegisterCANRecvCallback_Win32_t registerRevCallback = (RegisterCANRecvCallback_Win32_t)GetProcAddress(hDll, "RegisterCANRecvCallback_Win32");
	if (registerRevCallback != NULL)
	{
		retValue = registerRevCallback(ADeviceHandle, ReceiveCANMessage);
		if (retValue == 0)
		{
			printf("CAN Device with handle:%zu register rev callback success\n", ADeviceHandle);
		}
		else
		{
			printf("CAN Device with handle:%zu register rev callback failed\n", ADeviceHandle);
		}
	}
	//设置波特率
	SetCANBaudrateByRate_t setBaudrate = (SetCANBaudrateByRate_t)GetProcAddress(hDll, "SetCANBaudrateByRate");
	if (setBaudrate != NULL)
	{
		retValue = setBaudrate(ADeviceHandle, 0, 500, 1);  //250kbps
		if (retValue == 0)
		{
			printf("CAN Device with handle:%zu set baudrate 500k success\n", ADeviceHandle);
		}
		else
		{
			printf("CAN Device with handle:%zu set baudrate 500k failed\n", ADeviceHandle);
		}
	}
	//同步函数发送CAN报文
	SendCANSync_t sendMsgSync = (SendCANSync_t)GetProcAddress(hDll, "SendCANSync");
	if (sendMsgSync != NULL)
	{
		retValue = sendMsgSync(ADeviceHandle, &msg, 500);
		if (retValue == 0)
		{
			printf("CAN Device with handle:%zu sync send can message success\n", ADeviceHandle);
		}
		else
		{
			printf("CAN Device with handle:%zu sync send can message failed\n", ADeviceHandle);
		}
	}
	//异步函数发送CAN报文：
	SendCANASync_t sendMsgAsync = (SendCANASync_t)GetProcAddress(hDll, "SendCANASync");
	if (sendMsgAsync != NULL)
	{
		retValue = sendMsgAsync(ADeviceHandle, &msg);
		if (retValue == 0)
		{
			printf("CAN Device with handle:%zu async send can message success\n", ADeviceHandle);
		}
		else
		{
			printf("CAN Device with handle:%zu async send can message failed\n", ADeviceHandle);
		}
	}
}



DWORD WINAPI ThreadProc(LPVOID lpParameter)
{
	return 0;
}


int TSCANLINApi_C_Demo()
{
	std::cout << "TOSUN TSMaster APIs C Demo Project Start!\n";
	HMODULE hDll = LoadLibrary(TEXT("./TSMaster.dll"));
	if (hDll != NULL)
	{
		std::cout << "find libTSCAN.dll!\n";
		uint32_t ADeviceCount;
		size_t ADeviceHandle;
		uint32_t retValue;
		initialize_lib_tsmaster_t initialTSCAN = (initialize_lib_tsmaster_t)GetProcAddress(hDll, "initialize_lib_tsmaster");
		//扫描存在的设备：不是必须调用的
		if (initialTSCAN != NULL)
		{
			initialTSCAN("TSMasterAPIDemoC");
			printf("Init TSMaster Api Success\n");
		}
		else
		{
			printf("Init TSMaster Api Failed\n");
			return 1;
		}
		//
		ScanTSCANDevices_t ScanTSCANDevices = (ScanTSCANDevices_t)GetProcAddress(hDll, "ScanTSCANDevices");
		//扫描存在的设备：不是必须调用的
		if (ScanTSCANDevices != NULL)
		{
			ScanTSCANDevices(&ADeviceCount);
			printf("TSCAN Device Count:%d\n", ADeviceCount);
		}
		//连接设备：使用设备前必须调用
		ConnectTSCAN_t connectDevice_f = (ConnectTSCAN_t)GetProcAddress(hDll, "ConnectTSCAN");
		if (connectDevice_f != NULL)
		{
			retValue = connectDevice_f(0, &ADeviceHandle);
			if ((retValue == 0) || (retValue == 5))
			{
				printf("Device with handle:%zu connectted\n", ADeviceHandle);
			}
		}
#ifdef TEST_CAN_API
		TestCANAPI(hDll, ADeviceHandle);
#endif
#ifdef TEST_LIN_API
		TestLINAPI(hDll, ADeviceHandle);
#endif
		Sleep(300);
		DisconnectTSCANByDevice_t disConnectDevice_f = (DisconnectTSCANByDevice_t)GetProcAddress(hDll, "DisconnectTSCANByDevice");
		if (disConnectDevice_f != NULL)
		{
			retValue = disConnectDevice_f(ADeviceHandle);
			if ((retValue == 0))
			{
				printf("Disconnect device with handle:%zu success\n", ADeviceHandle);
			}
		}
		Sleep(300);
		//释放API库
		finalize_lib_tsmaster_t freeTSCANApi_f = (finalize_lib_tsmaster_t)GetProcAddress(hDll, "finalize_lib_tsmaster");
		if (freeTSCANApi_f != NULL)
		{
			freeTSCANApi_f();
		}
		Sleep(3000);
		FreeLibrary(hDll);
	}
	std::cout << "end dll!\n";
	return 0;
	int i = 10000;
	HANDLE hThread = CreateThread(NULL, 0, ThreadProc, NULL, 0, NULL);
	while (i--)
	{
		Sleep(1000);
	}
	return 0;
}


