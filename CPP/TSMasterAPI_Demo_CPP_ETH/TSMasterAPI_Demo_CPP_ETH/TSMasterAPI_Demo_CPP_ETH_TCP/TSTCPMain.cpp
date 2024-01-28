#include "../../../../bin_x86/TSMaster.h"
#pragma comment(lib, "../../../../bin_x86/TSMaster.lib")
#include <windows.h>
#include <thread>
#include <string>
#include <iostream>
using namespace std;

//#define TS_MSG_DONTWAIT 0x08

static bool thread_running;
void thread_tcp_server(int network, int sock) {
	u8 buf[2000];
	int count;
	while (thread_running)
	{

		count = tssocket_recv(network, sock, buf, 2000, 0);
		if (count > 0) {
			printf("tssocket_recv: %d  from ipaddr: %s, port: %d\n", count);
		}
		Sleep(10);
	}
}

std::wstring GetRegValue(HKEY hKeyType, DWORD dwType, LPCTSTR lpPath, LPCTSTR lpName)
{
	HKEY hKEY;
	DWORD dataSize = MAX_PATH;
	char data[MAX_PATH];
	std::string strValue("");
	if (RegOpenKeyEx(hKeyType, lpPath, NULL, KEY_READ, &hKEY) == ERROR_SUCCESS)        //如果无法打开hKEY,则中止程序的执行  
	{
		long lRet = RegQueryValueEx(hKEY, lpName, NULL, &dwType, (LPBYTE)data, &dataSize);
		if (lRet == ERROR_SUCCESS)
		{
			for (int i = 0; i < (int)dataSize; i++)
			{
				strValue = strValue + data[i];
			}
		}
		RegCloseKey(hKEY);        // 程序结束前要关闭已经打开的 hKEY。
	}
	else
	{
		RegCreateKeyEx(hKeyType, (LPCTSTR)lpPath, 0, NULL, NULL, KEY_WRITE, NULL, &hKEY, NULL);
		RegCloseKey(hKEY);        // 程序结束前要关闭已经打开的 hKEY。
	}
	std::wstring wstrValue((wchar_t*)strValue.data(), strValue.length() / 2);
	return wstrValue;
}

int main()
{
	s32 status;
	//延迟加载技术 以及调度表查找TSMaster.dll位置
	SetDefaultDllDirectories(7680);
	std::wstring strValue;
	strValue = GetRegValue(HKEY_CURRENT_USER, REG_SZ, L"Software\\TOSUN\\TSMaster", L"bin");
	AddDllDirectory(strValue.c_str());
	AddDllDirectory(L"./");

	initialize_lib_tsmaster("ETHUDPDemo");
	tsapp_show_tsmaster_window("Hardware", true);
	status = tssocket_initialize(0, (TLogDebuggingInfo)tsapp_log);
	Tip4_addr_t ipaddr, gw, netmask;
	//ipaddress 
	tssocket_aton("192.168.0.50", &ipaddr);
	//gateway
	tssocket_aton("192.168.0.1", &gw);
	//mask
	tssocket_aton("255.255.255.0", &netmask);

	//mac addresss
	u8 macaddr[6] = { 1,2,3,4,5,50 };

	status = tssocket_add_device(0, macaddr, ipaddr, netmask, gw, 1500);

	status = tsapp_connect();


	if (status != 0) return -1;
	int sock = tssocket(0, TS_AF_INET, TS_SOCK_STREAM, 0, NULL, NULL, NULL);

	if (sock == -1) return -1;
	int err = -1;
	Tts_sockaddr_in self1_addr;
	self1_addr.sin_family = TS_AF_INET;
	self1_addr.sin_port = tssocket_htons(51051);
	tssocket_aton("192.168.0.50", (Tip4_addr_t*)&self1_addr.sin_addr);

	err = tssocket_bind(CH1, sock, (Tts_sockaddr*)&self1_addr, sizeof(Tts_sockaddr));
	tssocket_listen(0, sock, 1);
	Tts_sockaddr connAddress;
	u32 addrlen = 0;
	int recvsock = tssocket_accept(0, sock, &connAddress, &addrlen);

	if (recvsock == -1) return -1;
	thread_running = true;
	std::thread t1(thread_tcp_server, CH1, recvsock);

	Tts_sockaddr_in dstaddr;
	dstaddr.sin_family = TS_AF_INET;
	dstaddr.sin_port = tssocket_htons(51051);
	tssocket_aton("192.168.0.51", (Tip4_addr_t*)&dstaddr.sin_addr);
	u8 buf[1400] = { 0 };
	for (s32 i = 0; i < 1400; i++)
		buf[i] = (u8)i;
	while (1)
	{
		int data;
		cin >> data;
		cout << data << endl;
		if (data == 1)
		{
			err = tssocket_send(CH1, recvsock, buf, 1400, 0);
		}
		else if (data == 2)
		{
			break;
		}
	}
	thread_running = false;
	t1.join();
	tssocket_close(CH1, sock);
	status = tsapp_disconnect();
	tssocket_remove_device(CH1, macaddr, &ipaddr);
	tssocket_finalize(CH1);
	finalize_lib_tsmaster();
	return 0;


}