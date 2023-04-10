// test_tscan_dll.cpp : ���ļ����� "main" ����������ִ�н��ڴ˴���ʼ��������
//

#include <iostream>
#include <windows.h>  
#include "TSMasterApi.h"


#define TEST_CAN_API
#define TEST_LIN_API

extern void ProcessLINMsg(TLIBLIN AMsg);

/// <summary>
/// CAN���Ľ��ջص�����
/// </summary>
/// <param name="AData">CAN����ָ��</param>
/// <returns></returns>
void __stdcall ReceiveCANMessage(const TLIBCAN* AData)
{

}

/*���ע���˱��������������յ���һ֡LIN���Ĺ��󣬾ͻᴥ���˺���*/
/// <summary>
/// LIN���Ľ��ջص�����
/// </summary>
/// <param name="AData">LIN����ָ��</param>
/// <returns></returns>
void __stdcall ReceiveLINMessage(const TLIBLIN* AData)
{
	//ͨ���ص�������ȡ����
	printf("Receive Recall\n");
	ProcessLINMsg(*AData);
}


/*���ע���˱��������������յ���һ֡LIN���Ĺ��󣬾ͻᴥ���˺���*/
/// <summary>
/// LIN���Ľ��ջص�����
/// </summary>
/// <param name="AData">LIN����ָ��</param>
/// <returns></returns>
void __stdcall ReceiveFastLINMessage(const TLIBLIN* AData)
{
	//ͨ���ص�������ȡ����
	printf("Receive FastLIN Recall\n");
	ProcessLINMsg(*AData);
}

/// <summary>
/// �����յ���LIN��������
/// </summary>
/// <param name="AMsg">LIN����</param>
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
	/*����CAN���ͱ��ģ����������*/
	TLIBLIN msg;
	//�ѵ�ǰ�豸����Ϊ���ڵ�ģʽ�����ڵ�ģʽ�£����ܹ��������ȱ��ģ����ͱ���ͷ��
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
	//����ڲ�ldf�ļ�
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
	//ע����ջص������������ڽ����ж�
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
	//ע��FalstLIN���ջص������������ڽ����ж�
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
	//���ò�����
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
	//ͬ����������LIN����
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
		//ֱ�Ӷ�ȡ����
		retValue = receiveFunc(ADeviceHandle, recMessageBuffs, 5, CHN1, ONLY_RX_DATA);
		printf("%d  messages received\n", retValue);
		for (int i = 0; i < (int)retValue; i++)
		{
			ProcessLINMsg(recMessageBuffs[i]);
		}
	}
	//ע�⣺����LIN������˵�����Ҫ���ձ��ģ�ҲҪ���ñ��ķ��ͺ���sendMsgAsync����istx����Ϊ0��ʵ����
	//�ǰѱ���֡ͷ���ͳ�ȥ����ȡ�����ϵı���
	msg.FIdentifier = 0x31;
	msg.FProperties.value = 0x00;
	msg.FProperties.bits.istx = 0; // as rx frame
	msg.FDLC = 3;
	msg.FIdxChn = 0;
	SendLINASync_t sendMsgASync = (SendLINASync_t)GetProcAddress(hDll, "SendLINASync");  //�첽��������LIN����
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
	//���ڽ������͵ı��ģ�����ӽڵ�û�м�ʱ�ظ�����retValue =0,����ʧ��
	Sleep(10);
	if (receiveFunc != NULL)
	{
		retValue = 0;
		int cnt = 0;
		//������ʱ�ȴ��ķ�ʽ��ֱ����ȡ��LIN���Ļ��߳�ʱ
		while ((retValue == 0) && (cnt < 100))
		{
			retValue = receiveFunc(ADeviceHandle, recMessageBuffs, 5, CHN1, ONLY_RX_DATA);
			cnt++;
			Sleep(10);
		}
		//�����ʱ�����ղ������ݣ����������ʧ��
		printf("%d  messages received\n", retValue);
		for (int i = 0; i < (int)retValue; i++)
		{
			ProcessLINMsg(recMessageBuffs[i]);
		}
	}
	msg.FIdentifier = 0x32;
	SendFastLINAsync_t sendFastLINMsgAsync = (SendFastLINAsync_t)GetProcAddress(hDll, "SendFastLINAsync");  //�첽��������LIN����
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
	//���ڽ������͵ı��ģ�����ӽڵ�û�м�ʱ�ظ�����retValue =0,����ʧ��
	ReceiveFastLINMsgs_t receiveFastLINFunc = (ReceiveFastLINMsgs_t)GetProcAddress(hDll, "ReceiveFastLINMsgs");
	Sleep(10);
	if (receiveFastLINFunc != NULL)
	{
		retValue = 0;
		int cnt = 0;
		//������ʱ�ȴ��ķ�ʽ��ֱ����ȡ��LIN���Ļ��߳�ʱ
		while ((retValue == 0) && (cnt < 100))
		{
			retValue = receiveFastLINFunc(ADeviceHandle, recMessageBuffs, 5, CHN1, ONLY_RX_DATA);
			cnt++;
			Sleep(10);
		}
		//�����ʱ�����ղ������ݣ����������ʧ��
		printf("%d  messages received\n", retValue);
		for (int i = 0; i < (int)retValue; i++)
		{
			ProcessLINMsg(recMessageBuffs[i]);
		}
	}
	//��ע����ջص�����
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
	//��ע��FastLIN���ջص�����
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
	/*����CAN���ͱ��ģ����������*/
	TLIBCAN msg;
	msg.FIdentifier = 0x03;
	msg.FProperties.bits.remoteframe = 0x00; //not remote frame,standard frame
	msg.FProperties.bits.extframe = 0;
	msg.FDLC = 3;
	msg.FIdxChn = 0;
	//ע����ջص������������ڽ����ж�
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
	//���ò�����
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
	//ͬ����������CAN����
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
	//�첽��������CAN���ģ�
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
		//ɨ����ڵ��豸�����Ǳ�����õ�
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
		//ɨ����ڵ��豸�����Ǳ�����õ�
		if (ScanTSCANDevices != NULL)
		{
			ScanTSCANDevices(&ADeviceCount);
			printf("TSCAN Device Count:%d\n", ADeviceCount);
		}
		//�����豸��ʹ���豸ǰ�������
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
		//�ͷ�API��
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


