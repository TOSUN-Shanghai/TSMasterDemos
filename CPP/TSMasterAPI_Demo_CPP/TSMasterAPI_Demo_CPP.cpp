#include "TSMasterApi.h"

#define TEST_CAN_API
#define TEST_LIN_API





void TSCANLINApi_CPP_Demo()
{
	TSMasterApi* tsCANLINAPIObj = new TSMasterApi("TSMasterAPIDemoCPP");

#ifdef TEST_CAN_API
	//TestCANAPI(tsCANLINAPIObj, ADeviceHandle);
#endif
#ifdef TEST_LIN_API
	//TestLINAPI(tsCANLINAPIObj, ADeviceHandle);
#endif
	Sleep(300);
	//释放API库
	free(tsCANLINAPIObj);
	//std::cout << "end dll!\n";
	printf("End C++ TSCANAPI CPP Demo\n");
}


