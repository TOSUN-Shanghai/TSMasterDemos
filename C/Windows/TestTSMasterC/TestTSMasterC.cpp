// TestTSMasterC.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include <iostream>
#include <windows.h>
#include "TSMaster.h"

#define USE_TOSUN_VIRTUAL
#undef  USE_XL_VIRTUAL
#undef  USE_TC1005
#define DBC_ABSOLUTE_ADDRESS "D:\\Projects\\TOSUN\\Projects\\TSMaster\\bin\\Data\\Demo\\Databases\\PowerTrain.dbc"
#define DBC_RELATIVE_ADDRESS ".\\PowerTrain.dbc" // relative to TSMaster.exe file path
#define DBC_ADDRESS DBC_ABSOLUTE_ADDRESS

s32 vErrorCode;

void __stdcall TSMasterLogger(const char* AStr, const s32 ALevel)
{
    std::cout << "TSMaster Logger: " << ALevel << ": " << AStr << "\n";
}

void __stdcall OnPreTxCANEvent(const ps32 AObj, const PCAN ACAN)
{
    if ((CH1 == ACAN->FIdxChn) && (0x64 == ACAN->FIdentifier)) {
        double d;       
        if (0 == tsdb_get_signal_value_can(ACAN, "EngineData", "EngPower", &d)) {
            d = d + 1;
            if (0 == tsdb_set_signal_value_can(ACAN, "EngineData", "EngPower", d)) {
                std::cout << "signal EngineData\\EngPower has been changed to: " << d << "\n";
            }
        }        
    }
}

bool CheckOK(const int ACode) 
{
    char* desc;
    vErrorCode = ACode;
    if (0 == ACode) return true;
    if (0 == tsapp_get_error_description(ACode, &desc)) {
        std::cout << "API error: " << desc << "\n";
    } else {
        std::cout << "API error code: " << ACode << "\n";
    }
    return false;
}

int main()
{
    std::cout << "TSMaster C Demo\n";
    std::cout << "This Demo demostrates how to start rbs and modify a signal value in rbs in real-time\n";
    setvbuf(stdout, NULL, _IONBF, 0);

    // [1] initialize library and set your application name
    if (!CheckOK(initialize_lib_tsmaster("TSMasterCDemo"))) return vErrorCode;
    std::cout << "Application initialized: TSMasterCDemo\n";
    if (!CheckOK(tsapp_set_logger(TSMasterLogger))) return vErrorCode;
    std::cout << "TSMaster logger redirected to the current program\n";

    do {        
        // [2] set CAN channel count
        if (!CheckOK(tsapp_set_can_channel_count(2))) break;
        std::cout << "TSMasterCDemo has 2 CAN channels\n";
        
        // [3] set each mapping: logical CH1 map to TC1005 CH1
        TLIBTSMapping m;
        m.init();
        sprintf_s(m.FAppName, "%s", "TSMasterCDemo");
        sprintf_s(m.FHWDeviceName, "%s", "TC1005");
        m.FAppChannelIndex = CH1;        
        m.FAppChannelType = APP_CAN;
#ifdef USE_TC1005
        m.FHWDeviceType = TS_TC1005_DEVICE;
        m.FHWDeviceSubType = -1;            // TC1005 has no series
        m.FHWIndex = 0;                     // the first hardware    
        m.FHWChannelIndex = CH1;            // channel 1/5 of TC1005
#endif
#ifdef USE_XL_VIRTUAL
        m.FHWDeviceType = XL_USB_DEVICE;
        m.FHWDeviceSubType = 1;             // 1 is virtual
        m.FHWIndex = 0;                     // the first hardware 
        m.FHWChannelIndex = CH1;            // channel 1/2 of Vector Virtual 1
#endif
#ifdef USE_TOSUN_VIRTUAL
        m.FHWDeviceType = TS_TCP_DEVICE;
        m.FHWDeviceSubType = -1;            // TS virtual has no series
        m.FHWIndex = 0;                     // the first hardware    
        m.FHWChannelIndex = CH1;            // channel 1/8 of TS virtual
#endif
        if (!CheckOK(tsapp_set_mapping(&m))) break;
        std::cout << "TSMasterCDemo logical CH1 mapped\n";

        // [4] set each mapping: logical CH2 map to TC1005 CH2
        m.FAppChannelIndex = CH2;
#ifdef USE_TC1005        
        m.FHWChannelIndex = CH2;            // channel 2/5 of TC1005
#endif
#ifdef USE_XL_VIRTUAL
        m.FHWIndex = 1;                     // the second hardware 
        m.FHWChannelIndex = CH1;            // channel 1/2 of Vector Virtual 2
#endif
#ifdef USE_TOSUN_VIRTUAL
        m.FHWDeviceType = TS_TCP_DEVICE;
        m.FHWDeviceSubType = -1;            // TS virtual has no series
        m.FHWIndex = 0;                     // the first hardware    
        m.FHWChannelIndex = CH2;            // channel 2/8 of TS virtual
#endif
        if (!CheckOK(tsapp_set_mapping(&m))) break;
        std::cout << "TSMasterCDemo logical CH2 mapped\n";
#ifdef USE_TC1005 
        // [5] configure CH1 baudrate
        if (!CheckOK(tsapp_configure_baudrate_can(CH1, 500.0, false, true))) break;
        std::cout << "TSMasterCDemo logical CH1 baudrate set to 500Kbps, with 120Ohm term. resistor\n";

        // [6] configure CH2 baudrate
        if (!CheckOK(tsapp_configure_baudrate_can(CH2, 500.0, false, true))) break;
        std::cout << "TSMasterCDemo logical CH2 baudrate set to 500Kbps, with 120Ohm term. resistor\n";
#endif
#ifdef USE_XL_VIRTUAL
        // [5] configure CH1 baudrate
        if (!CheckOK(tsapp_configure_baudrate_canfd(CH1, 500.0, 2000.0, fdtISOCANFD, fdmNormal, false))) break;
        std::cout << "TSMasterCDemo logical CH1 baudrate set to 500Kbps, with 120Ohm term. resistor\n";

        // [6] configure CH2 baudrate
        if (!CheckOK(tsapp_configure_baudrate_canfd(CH1, 500.0, 2000.0, fdtISOCANFD, fdmNormal, false))) break;
        std::cout << "TSMasterCDemo logical CH2 baudrate set to 500Kbps, with 120Ohm term. resistor\n";
#endif
        // [7] load dbc
        u32 idDBC;
        s32 obj;
        if (!CheckOK(tsdb_load_can_db(DBC_ADDRESS, "0", &idDBC))) break;
        std::cout << "DBC file is loaded, supported channels = CH1\n";

        // [9] configure can rbs
        if (!CheckOK(tscom_can_rbs_configure(false, true, true, rivUseDB))) break;
        std::cout << "CAN RBS is configured to not auto start (API version has no auto start capability)\n";

        // [10] activate everything in rbs
        if (!CheckOK(tscom_can_rbs_activate_all_networks(true, true))) break;
        std::cout << "Each signal in CAN RBS is now activated\n";
        if (!CheckOK(tsapp_enable_bus_statistics(true))) break;

        // [10.1] you can also start blf logging
        tsapp_start_logging("log1.blf");

        // [11] connect application
        if (!CheckOK(tsapp_connect())) break;
        std::cout << "TSMasterCDemo application connected, communication starts here...\n";

        // [12] start rbs
        if (!CheckOK(tscom_can_rbs_start())) break;
        std::cout << "CAN RBS is started...\n";
    
        // [13] register pre-tx event
        if (!CheckOK(tsapp_register_pretx_event_can(&obj, OnPreTxCANEvent))) break;
        std::cout << "Register pretx event succeeds\n";

        Sleep(100);
        // [14] set signal "1/PowerTrain/Engine/EngineData/EngSpeed"
        if (!CheckOK(tscom_can_rbs_set_signal_value_by_address("0/PowerTrain/Engine/EngineData/EngSpeed", 1234.56))) break;
        std::cout << "signal Engine/EngineData/EngSpeed has been changed\n";
        
        Sleep(1000);
        // [15] get signal "1/PowerTrain/Engine/EngineData/EngSpeed"
        double d;
        if (!CheckOK(tscom_can_rbs_get_signal_value_by_address("0/PowerTrain/Engine/EngineData/EngSpeed", &d))) break;
        std::cout << "signal Engine/EngineData/EngSpeed read value is: " << d << "\n";

        Sleep(3000);
        if (!CheckOK(tsapp_get_bus_statistics(APP_CAN, 0, cbsAllStdData, &d))) break;
        std::cout << "All std frame count is: " << d << "\n";
        if (!CheckOK(tsapp_get_bus_statistics(APP_CAN, 0, cbsPeakLoad, &d))) break;
        std::cout << "Bus peak load is: " << d << "\n";

        // [16] stop rbs
        if (!CheckOK(tscom_can_rbs_stop())) break;
        std::cout << "CAN RBS stopped\n";

        // [17] unregister pre-tx event
        if (!CheckOK(tsapp_unregister_pretx_event_can(&obj, OnPreTxCANEvent))) break;
        std::cout << "Unregister pretx event succeeds\n";

        // [18] disconnect application
        if (!CheckOK(tsapp_disconnect())) break;
        std::cout << "TSMasterCDemo application disconnected\n";

        // [19] logging also stopped finally
        tsapp_stop_logging();
    } while (0);

    // [20] finalize library
    finalize_lib_tsmaster();   
    std::cout << "TSMaster dll finalized\n";

    system("pause");
    return vErrorCode;
}

// 运行程序: Ctrl + F5 或调试 >“开始执行(不调试)”菜单
// 调试程序: F5 或调试 >“开始调试”菜单

// 入门使用技巧: 
//   1. 使用解决方案资源管理器窗口添加/管理文件
//   2. 使用团队资源管理器窗口连接到源代码管理
//   3. 使用输出窗口查看生成输出和其他消息
//   4. 使用错误列表窗口查看错误
//   5. 转到“项目”>“添加新项”以创建新的代码文件，或转到“项目”>“添加现有项”以将现有代码文件添加到项目
//   6. 将来，若要再次打开此项目，请转到“文件”>“打开”>“项目”并选择 .sln 文件
