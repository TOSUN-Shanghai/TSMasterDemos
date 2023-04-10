#include "TSMasterApi.h"


#define IDX_ERR_DLL_NOT_READY           (77)
#define IDX_CMD_OK                      (0)
#define IDX_CMD_LOADAPI_ERR             (2)
#define IDX_FUNCTION_POINTER_NOT_READY  (3)

TSMasterApi::TSMasterApi(const char* AAppName)
{
	dllIsLoaded = 0;
	LoadAPI();	
	pInitLibTSMaster(AAppName);
}


TSMasterApi::~TSMasterApi()
{
	if (hDll != NULL)
	{
		pFinalizeTSMaster();
		FreeLibrary(hDll);
		hDll = NULL;
	}
	InitializePointers();
}


byte TSMasterApi::LoadAPI()
{
	// Initializes pointers
	InitializePointers();
	// Loads the DLL
	hDll = LoadLibrary(TEXT("./TSMaster.dll"));
	if (hDll == NULL)
	{
		return IDX_CMD_LOADAPI_ERR;
	}
	// Loads API functions
	pInitLibTSMaster = (Tinitialize_lib_tsmaster)GetProcAddress(hDll, "initialize_lib_tsmaster");
	pFinalizeTSMaster = (Tfinalize_lib_tsmaster)GetProcAddress(hDll, "finalize_lib_tsmaster");
	//
	tscom_can_rbs_get_signal_value_by_element = (TCANRBSGetSignalValueByElement)GetProcAddress(hDll, "tscom_can_rbs_get_signal_value_by_element");
	tscom_can_rbs_get_signal_value_by_address = (TCANRBSGetSignalValueByAddress)GetProcAddress(hDll, "tscom_can_rbs_get_signal_value_by_address");
	tscom_can_rbs_set_signal_value_by_element = (TCANRBSSetSignalValueByElement)GetProcAddress(hDll, "tscom_can_rbs_set_signal_value_by_element");
	tscom_can_rbs_set_signal_value_by_address = (TCANRBSSetSignalValueByAddress)GetProcAddress(hDll, "tscom_can_rbs_set_signal_value_by_address");

	// Checks that all functions are loaded
	dllIsLoaded = tscom_can_rbs_get_signal_value_by_element && tscom_can_rbs_get_signal_value_by_address && tscom_can_rbs_set_signal_value_by_element 
		          && tscom_can_rbs_set_signal_value_by_address;
	if (dllIsLoaded)
		return IDX_CMD_OK;
	else
		return IDX_FUNCTION_POINTER_NOT_READY;
}

void TSMasterApi::InitializePointers()
{
	// Initializes thepointers for the PCANBasic functions
	//function Pointers
	tscom_can_rbs_set_signal_value_by_element = NULL;
	tscom_can_rbs_set_signal_value_by_address = NULL;
}

//注册LIN报文接收回调函数
s32 TSMasterApi::CANRBSSetSignalValueByElement(const s32 AIdxChn, const char* ANetworkName, const char* ANodeName, const char* AMsgName, const char* ASignalName, const double AValue)
{
	if (NULL != tscom_can_rbs_set_signal_value_by_element)
	{
		return tscom_can_rbs_set_signal_value_by_element(AIdxChn, ANetworkName, ANodeName, AMsgName, ASignalName, AValue);
	}
	return IDX_ERR_DLL_NOT_READY;
}

s32 TSMasterApi::CANRBSSetSignalValueByAddress(const char* ASymbolAddress, const double AValue)
{
	if (NULL != tscom_can_rbs_set_signal_value_by_address)
	{
		return tscom_can_rbs_set_signal_value_by_address(ASymbolAddress, AValue);
	}
	return IDX_ERR_DLL_NOT_READY;
}

s32  TSMasterApi::CANRBSGetSignalValueByElement(const s32 AIdxChn, const char* ANetworkName, const char* ANodeName, const char* AMsgName, const char* ASignalName, double* AValue)
{
	if (NULL != tscom_can_rbs_get_signal_value_by_element)
	{
		return tscom_can_rbs_get_signal_value_by_element(AIdxChn, ANetworkName, ANodeName, AMsgName, ASignalName, AValue);
	}
	return IDX_ERR_DLL_NOT_READY;
}

s32  TSMasterApi::CANRBSGetSignalValueByAddress(const char* ASymbolAddress, double* AValue)
{
	if (NULL != tscom_can_rbs_get_signal_value_by_address)
	{
		return tscom_can_rbs_get_signal_value_by_address(ASymbolAddress, AValue);
	}
	return IDX_ERR_DLL_NOT_READY;
}
