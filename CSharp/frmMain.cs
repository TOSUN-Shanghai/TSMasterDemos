using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using TSMaster;
using System.Runtime.InteropServices;
using System.IO;
using System.Runtime.Remoting;

namespace TSMasterAPI_CSharp
{
    
    public partial class frmMain : Form
    {
        public frmMain()
        {
            InitializeComponent();
        }

        private string FProgramName = "LibTSMasterDemo";
        private int vDiagModuleHandle = -1;
        private void Form1_Load(object sender, EventArgs e)
        {
            FProgramName = Path.GetFileNameWithoutExtension(Application.ExecutablePath);  //首先获取应用程序名称
            tbApplicationName.Text = FProgramName;        
            LoadDefaultState();
            //对于无法通过注册表查询TSMaster安装目录的程序，直接调用下面的函数接口设置路径，如果可以查询路径，则不需要
            //TsMasterApi.set_libtsmaster_location(@"D:\Program Files (x86)\TOSUN\TSMaster\bin");
            //初始化API模块:这是后续调用所有TsMasterApi函数的前提
            int ret = TsMasterApi.initialize_lib_tsmaster(FProgramName);
            //设置需要探测的硬件
            TsMasterApi.tsapp_set_vendor_detect_preferences(true, true, true, false, false, false, false);
            //
            vCANQueueEventObj += new TCANQueueEvent_Win32(OnCANRxEvent);
            vCANFDQueueEventObj += new TCANFDQueueEvent_Win32(OnCANFDRxEvent);
            vLINQueueEventObj += new TLINQueueEvent_Win32(OnLINRxEvent);
            //注册接收回调函数：在每一次的回调函数vCANQueueEventObj中刷新数据段
            if (TsMasterApi.tsapp_register_event_can((IntPtr)0, vCANQueueEventObj) != 0x00)
            {
                Log("Register CANRx Failed!");
            }
            cbbQueryType.SelectedIndex = 0;
        }

        private void CreateApplicationCANDemo()
        {
            //FProgramName:唯一名称，后面的各种映射跟他绑定
            //第一步：初始化API模块,如果已经调用，这里则不需要调用
            //TsMasterApi.initialize_lib_tsmaster(FProgramName);
            //第二步：按需设置需要的通道数，比如，这里需要2个CAN通道，0个LIN通道   
            if (TsMasterApi.tsapp_set_can_channel_count(4) == 0)
            {
                Log("Set CAN Channel Count Success!");
            }
            else
                Log("Set CAN Channel Count Failed!");
            if (TsMasterApi.tsapp_set_lin_channel_count(0) == 0)
            {
                Log("Set LIN Channel Count Success!");
            }
            else
                Log("Set LIN Channel Count Failed!");
            //第三步：按需创建通道映射:
            if (TsMasterApi.tsapp_set_mapping_verbose(FProgramName, (int)TLIBApplicationChannelType.APP_CAN,
                  (int)APP_CHANNEL.CHN1, "TC1005", TLIBBusToolDeviceType.TS_TC1005_DEVICE, 0, 0, (int)APP_CHANNEL.CHN1,true) == 0)
            {
            }
            if (TsMasterApi.tsapp_set_mapping_verbose(FProgramName, (int)TLIBApplicationChannelType.APP_CAN,
                  (int)APP_CHANNEL.CHN2, "TC1005", TLIBBusToolDeviceType.TS_TC1005_DEVICE, 0, 0, (int)APP_CHANNEL.CHN2, true) == 0)
            { }
            //把TC1005板卡的硬件通道1映射到驱动的逻辑通道1上面
            if (TsMasterApi.tsapp_set_mapping_verbose(FProgramName, (int)TLIBApplicationChannelType.APP_CAN,
              (int)APP_CHANNEL.CHN3, "TC1005", TLIBBusToolDeviceType.TS_TC1005_DEVICE, 0, 0, (int)APP_CHANNEL.CHN3, true) == 0)
            {
                Log("Mappings of channel " + (1 + (int)0).ToString() + " has been set");
            }
            //把TC1005板卡的硬件通道2映射到驱动的逻辑通道2上面
            if (TsMasterApi.tsapp_set_mapping_verbose(FProgramName, (int)TLIBApplicationChannelType.APP_CAN,
                  (int)APP_CHANNEL.CHN4, "TC1005", TLIBBusToolDeviceType.TS_TC1005_DEVICE, 0, 0, (int)APP_CHANNEL.CHN4, true) == 0)
            {
                Log("Mappings of channel " + (1 + (int)1).ToString() + " has been set");
            }
            //第四步：初始化通道参数
            if (TsMasterApi.tsapp_configure_baudrate_can((int)APP_CHANNEL.CHN1, 500, false, true) == 0)
            {
                Log("CAN Channel " + (0 + 1).ToString() + " baudrate has been configured");
            }
            else
            {
                Log("CAN Channel " + (0 + 1).ToString() + " baudrate failed");
            }
            if (TsMasterApi.tsapp_configure_baudrate_can((int)APP_CHANNEL.CHN2, 500, false, true) == 0)
            {
                Log("CAN Channel " + (1 + 1).ToString() + " baudrate has been configured");
            }
            else
            {
                Log("CAN Channel " + (1 + 1).ToString() + " baudrate failed");
            }
            if (TsMasterApi.tsapp_configure_baudrate_can((int)APP_CHANNEL.CHN3, 500, false, true) == 0)
            {
                Log("CAN Channel " + (2 + 1).ToString() + " baudrate has been configured");
            }
            else
            {
                Log("CAN Channel " + (2 + 1).ToString() + " baudrate failed");
            }
            if (TsMasterApi.tsapp_configure_baudrate_can((int)APP_CHANNEL.CHN4, 500, false, true) == 0)
            {
                Log("CAN Channel " + (3 + 1).ToString() + " baudrate has been configured");
            }
            else
            {
                Log("CAN Channel " + (3 + 1).ToString() + " baudrate failed");
            }
            //第五步：连接application：连接硬件通道并开启接收FIFO
            int connectResult = TsMasterApi.tsapp_connect();
            if (connectResult == 0)
            {
                Log("Connect Application Success!");
                TsMasterApi.tsfifo_enable_receive_fifo();
                Log("Start Receive FIFO!");  //如果不使能内部FIFO，无法使用Receive函数读取内部报文
            }
            else
            {
                
                Log("Connect Application Failed! Please check the mapping table and whether the Hardware is Ready?!");
            }
        }

        private void CreateApplicationLINDemo()
        {
            //FProgramName:唯一名称，后面的各种映射跟他绑定
            //第一步：初始化API模块,如果已经调用，这里则不需要调用
            //TsMasterApi.initialize_lib_tsmaster(FProgramName);
            //第二步：按需设置需要的通道数，比如，这里需要2个CAN通道，0个LIN通道   
            if (TsMasterApi.tsapp_set_can_channel_count(0) == 0)
            {
                Log("Set CAN Channel Count Success!");
            }
            else
                Log("Set CAN Channel Count Failed!");
            if (TsMasterApi.tsapp_set_lin_channel_count(1) == 0)
            {
                Log("Set LIN Channel Count Success!");
            }
            else
                Log("Set LIN Channel Count Failed!");
            //第三步：按需创建通道映射:
            if (TsMasterApi.tsapp_set_mapping_verbose(FProgramName, TLIBApplicationChannelType.APP_LIN,
                  (int)APP_CHANNEL.CHN1, "TC1026", TLIBBusToolDeviceType.TS_USB_DEVICE,  (int)TLIB_TS_Device_Sub_Type.TC1026, 0, (int)APP_CHANNEL.CHN1,true) == 0)
            {
            }
            //第四步：初始化通道参数
            if (TsMasterApi.tsapp_configure_baudrate_lin((int)APP_CHANNEL.CHN1, (float)19.2 , (int)LIN_PROTOCOL.LIN_PROTOCOL_21) == 0)
            {
                Log("LIN Channel " + (0 + 1).ToString() + " baudrate has been configured");
            }
            else
            {
                Log("LIN Channel " + (0 + 1).ToString() + " baudrate failed");
            }
            //第五步：连接application：连接硬件通道并开启接收FIFO
            int connectResult = TsMasterApi.tsapp_connect();
            if (connectResult == 0)
            {
                Log("Connect Application Success!");
                TsMasterApi.tsfifo_enable_receive_fifo();
                Log("Start Receive FIFO!");  //如果不使能内部FIFO，无法使用Receive函数读取内部报文
            }
            else
            {
               // Log(connectResult);
                Log("Connect Application Failed! Please check the mapping table and whether the Hardware is Ready?!");
            }
        }

        private void LoadDefaultState()
        {
            //Demo Controls
            //逻辑通道1相关
            //通道类型
            cbbChannelType1.SelectedIndex = (int)TLIBApplicationChannelType.APP_CAN; //默认通道类型为CAN
            cbbAppChannelIndex.SelectedIndex = (int)APP_CHANNEL.CHN1;
            cbbDeviceType1.SelectedIndex = (int)TLIBBusToolDeviceType.TS_TC1005_DEVICE; //默认载入TOSUN TC1005设备                                                                         //逻辑通道2相关
            cbbHardwareChannel1.SelectedIndex = (int)APP_CHANNEL.CHN1;  //默认选择该硬件设备的物理通道0
            ////逻辑通道2 相关
            //cbbChannelType2.SelectedIndex = (int)TLIBApplicationChannelType.APP_CAN; //默认通道类型为CAN
            //cbbDeviceType2.SelectedIndex = (int)TLIBBusToolDeviceType.TS_TC1005_DEVICE; //设备类型：默认载入TOSUN TC1005设备
            //cbbHardwareChannel2.SelectedIndex = 1;  //默认选择该硬件设备的物理通道1
            //
            cbbAppChannel_CAN.SelectedIndex = 0;
            cbbAppChannel_CANFD.SelectedIndex = 0;
        }

        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            //TsMasterApi.tsapp_set_logger(nil);
            InternalUnregisterEvents();
            TsMasterApi.tsapp_disconnect();
            //TsMasterApi.tsdiag_can_delete_all();
            TsMasterApi.finalize_lib_tsmaster();
        }

        private static TCANQueueEvent_Win32   vCANQueueEventObj;
        private static TCANFDQueueEvent_Win32 vCANFDQueueEventObj;
        private static TLINQueueEvent_Win32 vLINQueueEventObj;
        private void InternalUnregisterEvents()
        {
            TsMasterApi.tsapp_unregister_event_can((IntPtr)0, vCANQueueEventObj);
            TsMasterApi.tsapp_unregister_event_canfd((IntPtr)0, vCANFDQueueEventObj);         
            TsMasterApi.tsapp_unregister_event_lin((IntPtr)0, vLINQueueEventObj);
        }
        private void InternalRegisterEvents()
        {
            // register only one of them: CAN or CANFD
            TsMasterApi.tsapp_register_event_can((IntPtr)0, vCANQueueEventObj);
            TsMasterApi.tsapp_register_event_canfd((IntPtr)0, vCANFDQueueEventObj);
            TsMasterApi.tsapp_register_event_lin((IntPtr)0, vLINQueueEventObj);
        }
        double testSignalValue = 0;
        private void OnCANRxEvent(IntPtr AObj, ref TLIBCAN AData)
        {
            if (AData.FIsTx)
            {
                byte canid = Convert.ToByte(tbAddPeriodCANID.Text, 16);
                if (AData.FIdentifier == canid)
                {
                    AData.FData[0]++;
                    AData.FData[1]--;
                    //更新数据还是采用tsapp_add_cyclic_msg_can函数，不新增API
                    if (TsMasterApi.tsapp_add_cyclic_msg_can(ref AData, Convert.ToSingle(tbAddPeriodCANIntervalTime.Text)) == 0)
                    {
                       //避免直接跨线程操作界面控件！
                    }
                }
            }
            if (AData.FIdentifier == 0x123)
            {
                if (TsMasterApi.tsdb_get_signal_value_can(ref AData, tBMessageName.Text,tBSignalName.Text, ref testSignalValue) == 0x00)
                {
                    //ReadData Success
                }
            }
        }

        private void OnCANFDRxEvent(IntPtr AObj, ref TLIBCANFD AData)
        {
            //

        }

        private void OnLINRxEvent(IntPtr AObj, ref TLIBLIN AData)
        {
            //frm:= TfrmTestLibTSMaster(aobj);
            //c:= adata ^;
            //frm.DisplayThreadedEventMessage(c.ToString);
        }
        private void button1_Click(object sender, EventArgs e)
        {
            TsMasterApi.tsapp_show_channel_mapping_window();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (cbbWindowName.Text.Trim() == "")
            {
                MessageBox.Show("请先选择一个窗体名称！","警告",MessageBoxButtons.OK,MessageBoxIcon.Warning);
                return;
            }
            TsMasterApi.tsapp_show_tsmaster_window(cbbWindowName.Text.Trim(), false);
        }

        private void btnGetApplicationList_Click(object sender, EventArgs e)
        {
            IntPtr applicationList = new IntPtr();
            int ret = TsMasterApi.tsapp_get_application_list(ref applicationList);
            if (ret == 0)
            {
                string appList = Marshal.PtrToStringAnsi(applicationList);
                tbApplicationList.Text = appList;
            }
        }

        private void btnRegisterRxEvents_Click(object sender, EventArgs e)
        {
            InternalRegisterEvents();
        }

        private void btnUnregisterRxEvents_Click(object sender, EventArgs e)
        {
            InternalUnregisterEvents();
        }

        /// <summary>
        /// 常见错误：通道映射错误。比如设置了2路CAN，2路LIN。为CAN映射了硬件，但是没有为LIN通道映射硬件通道，就会造成错误！
        /// 解决办法：如果不用对应的通道，则把对应通道数设置为0
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void btnConnectApplication_Click(object sender, EventArgs e)
        {
            if (CheckResultOK(TsMasterApi.tsapp_connect()))
            {
                Log("Connect Application Success!");
                TsMasterApi.tsfifo_enable_receive_fifo();
                TsMasterApi.tsfifo_add_can_canfd_pass_filter((int)APP_CHANNEL.CHN1, 0x123, false);
                TsMasterApi.tsfifo_add_can_canfd_pass_filter((int)APP_CHANNEL.CHN1, 0x124, true);
                Log("Start Receive FIFO!");  //如果不使能内部FIFO，无法使用Receive函数读取内部报文
                //
                if (TsMasterApi.tsdiag_can_create(ref vDiagModuleHandle, (int)APP_CHANNEL.CHN1, 0, 0, 0x7C0, true, 0x7C8, true, 0x7DF, true) == 0x00)
                {
                    Log("Start diagnostic module, module handle is :" + vDiagModuleHandle.ToString());
                }
                else
                {
                    Log("Start diagnostic module failed");
                }
                //
            }
            else
            {
                Log("Connect Application Failed! Please check the mapping table and whether the Hardware is Ready?!");
            }
        }

        private void Log(string msg)
        {
            if (MM.Lines.Count() > 1000)
            {
                MM.Text = "";
            }
            MM.Text += msg + "\r\n";
        }

        private void btnTransmitCANAsync_Click(object sender, EventArgs e)
        {
            TLIBCAN canMsg = new TLIBCAN(0, 0x456, true, false, false, 8);
            if (TsMasterApi.tsapp_transmit_can_async(ref canMsg) == 0)
            {
                Log("ASync Send CAN Message Success!");
            }
            else
            {
                Log("ASync Send CAN Message Failed");
            }
        }

        private void btnTransmitCANSync_Click(object sender, EventArgs e)
        {
            TLIBCAN canMsg = new TLIBCAN(0, 0x456, true, false, false, 8);
            if (TsMasterApi.tsapp_transmit_can_sync(ref canMsg, 100) == 0)
            {
                Log("Sync Send CAN Message Success!");
            }
            else
            {
                Log("Sync Send CAN Message Failed");
            }
        }

        private void btnTransmitCANFDAsync_Click(object sender, EventArgs e)
        {
            TLIBCANFD canMsg = new TLIBCANFD(0, 0x456, true, false, false, 8);
            if (TsMasterApi.tsapp_transmit_canfd_async(ref canMsg) == 0)
            {
                Log("ASync Send CANFD Message Success!");
            }
            else
            {
                Log("ASync Send CANFD Message Failed");
            }
        }

        private void btnTransmitCANFDSync_Click(object sender, EventArgs e)
        {
            TLIBCANFD canMsg = new TLIBCANFD(0, 0x456, true, false, false, 8);
            if (TsMasterApi.tsapp_transmit_canfd_sync(ref canMsg, 200) == 0)
            {
                Log("Sync Send CANFD Message Success!");
            }
            else
            {
                Log("Sync Send CANFD Message Failed");
            }
        }

        private void btnDeleteApplication_Click(object sender, EventArgs e)
        {
            if (TsMasterApi.tsapp_del_application(tbApplicationName.Text) == 0)
            {
                Log("Delete Application Success:" + tbApplicationName.Text);
            }
        }

        private void btnAddApplication_Click(object sender, EventArgs e)
        {
            if (TsMasterApi.tsapp_add_application(tbApplicationName.Text) == 0)
            {
                Log("Add Application Success:" + tbApplicationName.Text);
            }
        }

        private void btnSetApplicationCANCount_Click(object sender, EventArgs e)
        {
            try
            {
                int chnCount = Convert.ToInt32(tbCANCount.Text);
                if (TsMasterApi.tsapp_set_can_channel_count(chnCount) == 0)
                {
                    Log("Set CAN Channel Count Success!");
                }
            }
            catch
            {

            }
        }

        private void btnSetApplicationLINCount_Click(object sender, EventArgs e)
        {
            try
            {
                int chnCount = Convert.ToInt32(tbLINCount.Text);
                if (TsMasterApi.tsapp_set_lin_channel_count(chnCount) == 0)
                {
                    Log("Set LIN Channel Count Success!");
                }
            }
            catch
            {

            }
        }

        private void btnGetApplicationCANCount_Click(object sender, EventArgs e)
        {
            try
            {
                int chnCount = 0;
                if (TsMasterApi.tsapp_get_can_channel_count(ref chnCount) == 0)
                {
                    tbGetCANCount.Text = chnCount.ToString();
                    Log("Set LIN Channel Count Success!");
                }
            }
            catch
            {

            }
        }

        private void btnGetApplicationLINCount_Click(object sender, EventArgs e)
        {
            try
            {
                int chnCount = 0;
                if (TsMasterApi.tsapp_get_lin_channel_count(ref chnCount) == 0)
                {
                    tbGetLINCount.Text = chnCount.ToString();
                    Log("Set LIN Channel Count Success!");
                }
            }
            catch
            {

            }
        }

        private void btnDisconnectApplication_Click(object sender, EventArgs e)
        {
            if (TsMasterApi.tsapp_disconnect() == 0)
            {
                Log("Disconnect Application Success:" + FProgramName);
            }
            else
            {
                Log("Disconnect Application Failed:" + FProgramName);
            }
        }

        private void btnAddCANPerodicMessage_Click(object sender, EventArgs e)
        {
            try
            {
                byte canid = Convert.ToByte(tbAddPeriodCANID.Text, 16);
                TLIBCAN canObj = new TLIBCAN(0, canid, true, false, false, 0);
                canObj.FDLC = 8;
                canObj.FData[0] = 0xAA;
                canObj.FData[1] = 0xBB;
                Single intervalTime = Convert.ToSingle(tbAddPeriodCANIntervalTime.Text);
                if (TsMasterApi.tsapp_add_cyclic_msg_can(ref canObj, intervalTime) == 0)
                {
                    Log("Add Period CAN Message Success!");
                }
            }
            catch
            {

            }
        }

        private void btnDeleteCANPeridicMessage_Click(object sender, EventArgs e)
        {
            try
            {
                byte canid = Convert.ToByte(tbDelPeriodCANID.Text, 16);
                TLIBCAN canObj = new TLIBCAN(0, canid, true, false, false, 0);
                if (TsMasterApi.tsapp_delete_cyclic_msg_can(ref canObj) == 0)
                {
                    Log("Delete Period CAN Message Success!");
                }
            }
            catch
            {

            }
        }

        private void btnDeleteAllCANPeriodicMessages_Click(object sender, EventArgs e)
        {
            if (TsMasterApi.tsapp_delete_cyclic_msgs() == 0)
            {
                Log("Delete All Period CAN Message Success!");
            }
        }

        private void btnSetApplicationChannel1Mapping_Click(object sender, EventArgs e)
        {
            if ((TLIBBusToolDeviceType)cbbDeviceType1.SelectedIndex == TLIBBusToolDeviceType.PEAK_USB_DEVICE)
            {
                if (TsMasterApi.tsapp_set_mapping_verbose(tbApplicationName.Text, (TLIBApplicationChannelType)cbbChannelType1.SelectedIndex,
                                    (int)(APP_CHANNEL)cbbAppChannelIndex.SelectedIndex, cbbDeviceType1.Text, (TLIBBusToolDeviceType)cbbDeviceType1.SelectedIndex, -1, 0, (int)(APP_CHANNEL)0x51,true) == 0)
                {
                    Log("Mappings of channel " + (1 + (int)0).ToString() + " has been set");
                }
            }
            else
            {
                if (TsMasterApi.tsapp_set_mapping_verbose(tbApplicationName.Text, (TLIBApplicationChannelType)cbbChannelType1.SelectedIndex,
                    (int)(APP_CHANNEL)cbbAppChannelIndex.SelectedIndex, cbbDeviceType1.Text, (TLIBBusToolDeviceType)cbbDeviceType1.SelectedIndex, cbbSubDeviceType1.SelectedIndex, 0, (int)(APP_CHANNEL)cbbHardwareChannel1.SelectedIndex,true) == 0)
                {
                    Log("Mappings of channel " + (1 + (int)0).ToString() + " has been set");
                }
            }
        }
       

        private void button3_Click(object sender, EventArgs e)
        {
            string str1 = "character string1";
            var strToBytes1 = System.Text.Encoding.UTF8.GetBytes(str1);
            string str2 = "character string2";
            var strToBytes2 = System.Text.Encoding.Default.GetBytes(str2);
            string str3 = "character string3";
            var strToBytes3 = System.Text.Encoding.Unicode.GetBytes(str3);
            string str4 = "character string4";
            var strToBytes4 = System.Text.Encoding.ASCII.GetBytes(str4);
        }

        private void cbbDeviceType1_SelectedIndexChanged(object sender, EventArgs e)
        {
            SetDeviceSubType((TLIBBusToolDeviceType)cbbDeviceType1.SelectedIndex, cbbSubDeviceType1);
        }

        private void SetDeviceSubType(TLIBBusToolDeviceType ADevType, ComboBox ASubTypeCombo)
        {
            int j;
            TLIB_XL_Device_Sub_Type iXL;
            TLIB_TS_Device_Sub_Type iTS;
            ASubTypeCombo.Items.Clear();
            switch ((TLIBBusToolDeviceType)ADevType)
            {
                case TLIBBusToolDeviceType.XL_USB_DEVICE:
                    {
                        for (iXL = TLIB_XL_Device_Sub_Type.XL_NONE; iXL < TLIB_XL_Device_Sub_Type.XL_VN1531; iXL++)
                        {
                            j = (int)(iXL);
                            ASubTypeCombo.Items.Add(TCANHardwareInfo.XL_HWTYPE_NAMES[j]);
                        }
                        // set default
                        ASubTypeCombo.SelectedIndex = 0; // vector virtual can
                    };
                    break;
                case TLIBBusToolDeviceType.TS_USB_DEVICE:
                    {
                        for (iTS = TLIB_TS_Device_Sub_Type.TS_UNKNOWN_DEVICE; iTS <= TLIB_TS_Device_Sub_Type.TC1013; iTS++)
                        {
                            j = (int)(iTS);
                            ASubTypeCombo.Items.Add(TCANHardwareInfo.TS_HWTYPE_NAMES[j]);
                        }
                        // set default
                        ASubTypeCombo.SelectedIndex = 3; // TSCAN mini
                    };
                    break;
                case TLIBBusToolDeviceType.PEAK_USB_DEVICE:
                    {
                        ASubTypeCombo.Items.Add("Peak");
                        ASubTypeCombo.SelectedIndex = 0;
                    };
                    break;
                case TLIBBusToolDeviceType.BUS_UNKNOWN_TYPE:
                case TLIBBusToolDeviceType.KVASER_USB_DEVICE:
                case TLIBBusToolDeviceType.ICS_USB_DEVICE:
                case TLIBBusToolDeviceType.TS_TCP_DEVICE:
                case TLIBBusToolDeviceType.TS_TC1005_DEVICE:
                    {
                        ASubTypeCombo.Items.Clear();
                        ASubTypeCombo.SelectedIndex = -1;
                        ASubTypeCombo.Text = "Default";
                    }
                    break;
            }

        }


        private void tabPage1_Click(object sender, EventArgs e)
        {

        }

        private void cbbAppChannelIndex_SelectedIndexChanged(object sender, EventArgs e)
        {
            btnSetApplicationChannel1Mapping.Text = "Set Application Channel" + (cbbAppChannelIndex.SelectedIndex + 1).ToString() + " Mapping";
            btnGetChannelMapping.Text = "Get Application Channel" + (cbbAppChannelIndex.SelectedIndex + 1).ToString() + " Mapping";
            btnDeleteChannelMapping.Text = "Delete Application Channel" + (cbbAppChannelIndex.SelectedIndex + 1).ToString() + " Mapping";
        }

        private void btnSetCANBaudrate_Click(object sender, EventArgs e)
        { 
            int i;
            Single b;
            try
            {
                i = cbbAppChannel_CAN.SelectedIndex;
                b = Convert.ToSingle(tBCANBaudrate.Text);
                if (TsMasterApi.tsapp_configure_baudrate_can(i, b, false, chkCANResistor.Checked) == 0)
                {
                    Log("CAN Channel " + (i + 1).ToString() + " baudrate has been configured");
                }
                else
                {
                    Log("CAN Channel " + (i + 1).ToString() + " baudrate failed");
                }
            }
            catch
            { 
            
            }
        }

        private void btnSetCANFDBaudrate_Click(object sender, EventArgs e)
        {
            int i;
            Single b, c;
            try
            {
                i = cbbAppChannel_CANFD.SelectedIndex;
                b = Convert.ToSingle(tBCANFDArbBaudrate.Text);
                c = Convert.ToSingle(tBCANFDDataBaudrate.Text);
                if (TsMasterApi.tsapp_configure_baudrate_canfd(i, b, c, TLIBCANFDControllerType.lfdtISOCAN,
                             (int)TLIBCANFDControllerMode.lfdmNormal, chkCANResistor.Checked) == 0)
                {
                    Log("CANFD Channel " + (i + 1).ToString() + " baudrate has been configured");
                }
                else
                {
                    Log("CANFD Channel " + (i + 1).ToString() + " baudrate failed");
                }
            }
            catch
            {

            }
        }

        private int msgcount = 0;
        private void btnReceiveCANMsgs_Click(object sender, EventArgs e)
        {
            TLIBCAN[] canBuffer = new TLIBCAN[100];
            int revCnt = 100;

            int ret = TsMasterApi.tsfifo_receive_can_msgs_list(ref canBuffer, ref revCnt, (int)APP_CHANNEL.CHN1, true);  //如果执行失败，请检查是否通过TsMasterApi.tsapp_enable_receive_fifo();开启了内部Buffer
            if (revCnt != 0)
            {
                //Log("No Message Received！");
                return;
            }
            msgcount += revCnt;
            lblCount.Text = msgcount.ToString();
            for (int i = 0; i < revCnt; i++)
            {
                string msg = "CAN Msg: ";
                if (canBuffer[i].FIsTx)
                    msg += "Tx ";
                else
                    msg += "Rx ";
                msg += canBuffer[i].FIdentifier.ToString("X8");
                Log(msg);
            }

        }

        private void button4_Click(object sender, EventArgs e)
        {
            TLIBCANFD[] canBuffer = new TLIBCANFD[10];
            int revCnt = 0;

            int ret = TsMasterApi.tsfifo_receive_canfd_msgs_list(ref canBuffer, ref revCnt, (int)APP_CHANNEL.CHN1, true);  //如果执行失败，请检查是否通过TsMasterApi.tsapp_enable_receive_fifo();开启了内部Buffer
            if (ret != 0)
            {
                Log("No Message Received！");
                return;
            }
            for (int i = 0; i < revCnt; i++)
            {
                string msg = "CANFD Msg: ";
                if (canBuffer[i].FIsTx)
                    msg += "Tx ";
                else
                    msg += "Rx ";
                msg += canBuffer[i].FIdentifier.ToString("X8");
                Log(msg);
            }
            
        }



        private uint FDBCHandle = 0;
        private void btnLoadDBCPath_Click(object sender, EventArgs e)
        {
            if (CheckResultOK(TsMasterApi.tsdb_unload_can_dbs()))
            {
                Log("Unload DBC Success!");
            }
            //Database必须是绝对路径
            string dbcPath = tbDBCPath.Text;
            if (File.Exists(tbDBCPath.Text) == false)
            {
                dbcPath = Application.StartupPath + @".\" + tbDBCPath.Text;
            }
            if (CheckResultOK(TsMasterApi.tsdb_load_can_db(dbcPath,"0,1,2,3", ref FDBCHandle)))
            {
                tBUnloadDBCHandle.Text = FDBCHandle.ToString();
                tbDBCQueryHandle.Text = FDBCHandle.ToString();
                Log("Load DBC Success!");
            }
        }

        private Boolean CheckResultOK(int AResultCode)
        {
            if (AResultCode == 0)
                return true;
            else
            {
                Log("Error occured: " );
                return false;
            }
        }

        private void btnUnloadDBC_Click(object sender, EventArgs e)
        {
            try
            {
                uint ADBCHandle = Convert.ToUInt32(tBUnloadDBCHandle.Text);
                if (CheckResultOK(TsMasterApi.tsdb_unload_can_db(ADBCHandle)))
                {
                    Log("Log DBC Success!");
                }
            }
            catch
            {
                MessageBox.Show("DBC Handle is UINT32 data type","Warning",MessageBoxButtons.OK,MessageBoxIcon.Warning);
            }
        }

        private void btnQuery_Click(object sender, EventArgs e)
        {
            IntPtr retMsg = IntPtr.Zero;
            int ret = TsMasterApi.tsdb_get_can_db_info(
              Convert.ToUInt32(tbDBCQueryHandle.Text),
              cbbQueryType.SelectedIndex,
              Convert.ToInt32(tbSubIdx.Text),
              Convert.ToInt32(tbSubSubIdx.Text),
              ref retMsg
              );
            if(ret == 0)  
             {

                tBQueryResult.Text += Marshal.PtrToStringAnsi(retMsg) + "\r\n";
                Log("Query success");
             }
            else
            {
                Log("Database index invalid or parameter invalid");
            }
            // string retMsg1 = "";

            if (TsMasterApi.tsdb_get_can_db_info(
                Convert.ToUInt32(tbDBCQueryHandle.Text),
                cbbQueryType.SelectedIndex,
                Convert.ToInt32(tbSubIdx.Text),
                Convert.ToInt32(tbSubSubIdx.Text),
                ref retMsg
                ) == 0x00)
            {
                tBQueryResult.Text += Marshal.PtrToStringAnsi(retMsg) + "\r\n";
                Log("Query success");
            }
            else
            {
                Log("Database index invalid or parameter invalid");
            }
                
            
        }

        private void btnReadCANSignalValue_Click(object sender, EventArgs e)
        {
            //输入原始的CAN报文，报文名称，信号名称，直接提取出对应的信号名称
            if (cbbDBCChannel.SelectedIndex < 0)
            {
                Log("Please Select DBC Channel First!");
                return;
            }
            TLIBCAN canObj = new TLIBCAN((APP_CHANNEL)cbbDBCChannel.SelectedIndex, 0x551, true, false, false, 8);
            for (int i = 0; i < 8; i++)
            {
                canObj.FData[i] = 0xFF;
            }
            double sigValue = 0;
            if (CheckResultOK(TsMasterApi.tsdb_get_signal_value_can(ref canObj, "Wheel_Speed", "FL_Speed", ref sigValue)))
            {
                Log("SignalValue is:" + sigValue.ToString());
            }
        }

        double srcSignalValue = 0.5;
        private void btnSetCANSignalValue_Click(object sender, EventArgs e)
        {
            //输入原始的CAN报文，报文名称，信号名称，直接提取出对应的信号名称
            TLIBCAN canObj = new TLIBCAN(0, 0x123, true, false, false, 8); //也可以创建一个全局的CAN报文，每次只修改信号值
            srcSignalValue += 1;
            if (CheckResultOK(TsMasterApi.tsdb_set_signal_value_can(ref canObj, tBMessageName.Text, tBSignalName.Text, srcSignalValue)))
            {
                Log("Set SignalValue:" + srcSignalValue.ToString("F2")  + " Success!");
            }
            TsMasterApi.tsapp_add_cyclic_msg_can(ref canObj, 10);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            lblSignalValue.Text = testSignalValue.ToString("F2");
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            btnReceiveCANMsgs_Click(null, null);
        }

        private void btnGetChannelMapping_Click(object sender, EventArgs e)
        {
            TLIBTSMapping m = new TLIBTSMapping();
            if (TsMasterApi.tsapp_get_mapping(ref m) == 0)
            {
                Log("Get Mapping Success");
                MessageBox.Show("HardwareName:" + m.FHWDeviceName + "HardwareChannel:" + m.FHWChannelIndex.ToString()); 
            }
        }

        private void btnDeleteChannelMapping_Click(object sender, EventArgs e)
        {
            if (TsMasterApi.tsapp_del_mapping_verbose(FProgramName, (TLIBApplicationChannelType)cbbChannelType1.SelectedIndex,
                (int)(APP_CHANNEL)cbbAppChannelIndex.SelectedIndex) == 0)
            {
                Log("Delete Mapping Success");
            }
        }

        private void btnGetAllHardwareInfos_Click(object sender, EventArgs e)
        {
            int hardwareNum = 0;
            TLIBHWInfo tmpDeviceInfo = new TLIBHWInfo();
            int retMessage = TsMasterApi.tsapp_enumerate_hw_devices(ref hardwareNum);
            if (retMessage == 0)
            {
                LogDeviceInformation("Hardware Num:" + hardwareNum.ToString());
            }
            else
            {
                //Log(retMessage);
                LogDeviceInformation("Enum hardware Info Failed！");
            }
            for (int i = 0; i < hardwareNum; i++)
            {
                if (TsMasterApi.tsapp_get_hw_info_by_index(i, ref tmpDeviceInfo) == 0)
                {
                    LogDeviceInformation(tmpDeviceInfo.FDeviceName.ToString());
                }
            }
        }

        private void btnCreateDemoConfiguration_Click(object sender, EventArgs e)
        {
            CreateApplicationCANDemo();
        }
        private void LogDeviceInformation(string AMsg)
        {
            tbDeviceInformation.Text += AMsg + "\r\n";
        }

        /// <summary>
        /// tsapp_enumerate_hw_devices函数必须在App未连接状态下才能够执行！
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void btnGetDeviceNum_Click(object sender, EventArgs e)
        {
            int hardwareNum = 0;
            int retMessage = TsMasterApi.tsapp_enumerate_hw_devices(ref hardwareNum);
            if (retMessage == 0)
            {
                LogDeviceInformation("Hardware Num:" + hardwareNum.ToString());
                tBDeviceNumber.Text = hardwareNum.ToString();
                cbbDeviceIndex.Items.Clear();
                for (int i = 0; i < hardwareNum; i++)
                {
                    cbbDeviceIndex.Items.Add(i.ToString());
                }
                if (hardwareNum > 0)
                    cbbDeviceIndex.SelectedIndex = 0;
            }
            else
            {
                //LogDeviceInformation(retMessage);               
            }
        }

        private void btnGetAppointtedDeviceInfo_Click(object sender, EventArgs e)
        {
            if (cbbDeviceIndex.SelectedIndex < 0)
            {
                LogDeviceInformation("Please select device Index first!");
                return;
            }
            TLIBHWInfo tmpDeviceInfo = new TLIBHWInfo();
            if (TsMasterApi.tsapp_get_hw_info_by_index(cbbDeviceIndex.SelectedIndex, ref tmpDeviceInfo) == 0)
            {
                LogDeviceInformation(tmpDeviceInfo.FDeviceName.ToString());
            }
        }

        private void btnStartLogging_Click(object sender, EventArgs e)
        {
            if (btnStartLogging.Text == "Start Logging")
            {
                TsMasterApi.tsapp_start_logging(@".\TestData" + DateTime.Now.ToString("dd-HH-mm-ss") /*+ ".blf"*/);
                btnStartLogging.Text = "Stop Logging";
            }
            else
            {
                TsMasterApi.tsapp_stop_logging();
                btnStartLogging.Text = "Start Logging";
            }
        }

        private void btnAddReplayEngine_Click(object sender, EventArgs e)
        {
            int AReplayIndex = 0;
            OpenFileDialog openFileObj = new OpenFileDialog();
            openFileObj.Filter = "blfFile|*.blf";
            openFileObj.FilterIndex = 0;
            if (openFileObj.ShowDialog() == DialogResult.OK)
            {
                string fileName = openFileObj.FileName;
                TsMasterApi.tslog_stop_online_replays();
                int retValue = TsMasterApi.tslog_del_online_replay_configs();
                if (retValue != 0)
                {
                    MessageBox.Show("Error:" + retValue.ToString(), "Warning", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                    return;
                }
                retValue = TsMasterApi.tslog_add_online_replay_config(fileName, ref AReplayIndex);
                if (retValue != 0)
                {
                    MessageBox.Show("Error:" + retValue.ToString(),"Warning",MessageBoxButtons.OK,MessageBoxIcon.Warning);
                    return;
                }
                retValue = TsMasterApi.tslog_set_online_replay_config(AReplayIndex, "Test", fileName, false,
                    true, 0, 0, true, false,
                    "1,0,0,0,0,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32"); //必须32个数字，否则Mapping失败
                if (retValue != 0)
                {
                    MessageBox.Show("Error:" + retValue.ToString(), "Warning", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                    return;
                }
                retValue = TsMasterApi.tslog_start_online_replay(AReplayIndex);
                if (retValue != 0)
                {
                    MessageBox.Show("Error:" + retValue.ToString(), "Warning", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                    return;
                }
                Log("Load Blf File Success！");
            }
        }

        private void btnShowHardwareConfig_Click(object sender, EventArgs e)
        {
            TsMasterApi.tsapp_show_tsmaster_window("Hardware", false);
        }

        private void btnDeleteFilter_Click(object sender, EventArgs e)
        {
            TsMasterApi.tsfifo_delete_can_canfd_pass_filter((int)APP_CHANNEL.CHN1, 0x128);
        }

        private void btnAddFilter_Click(object sender, EventArgs e)
        {
            TsMasterApi.tsfifo_add_can_canfd_pass_filter((int)APP_CHANNEL.CHN1, 0x128,true);
        }

        private void button3_Click_1(object sender, EventArgs e)
        {
            if (TsMasterApi.tsdiag_can_session_control(vDiagModuleHandle, 0x01) == 0x00)
            {
                Log("Session Control success!");
            }
        }

        private void btnConfigBaudrateRegs_Click(object sender, EventArgs e)
        {
            TsMasterApi.tsapp_configure_canfd_regs((int)APP_CHANNEL.CHN1, 500, 33, 6, 2, 6, 2000, 15, 4, 1, 3, TLIBCANFDControllerType.lfdtISOCAN,
                (int)TLIBCANFDControllerMode.lfdmNormal, 1);
        }
        [DllImport(".\\TSMaster.dll", CallingConvention = CallingConvention.StdCall, CharSet = CharSet.Ansi)]
        public static extern int tsapp_add_precise_cyclic_message(int AID, int AChnidx, bool ISExt, float ACycle, int ATimeOut);
        [DllImport(".\\TSMaster.dll", CallingConvention = CallingConvention.StdCall, CharSet = CharSet.Ansi)]
        public static extern int tsapp_delete_precise_cyclic_message(int AID, int AChnidx, bool ISExt, int ATimeOut);

        private void button4_Click_1(object sender, EventArgs e)
        {
            if (tsapp_add_precise_cyclic_message(0x123, 0, false, 10, 2000) == 0)
            {
                Log("Add precise cyclic message success");
            }
            else
                Log("Add precise cyclic message fail");
            if (tsapp_add_precise_cyclic_message(0x456, 0, false, 10, 2000) == 0)
            {
                Log("Add precise cyclic message success");
            }
            else
                Log("Add precise cyclic message fail");
            if (tsapp_add_precise_cyclic_message(0x789, 0, false, 10, 2000) == 0)
            {
                Log("Add precise cyclic message success");
            }
            else
                Log("Add precise cyclic message fail");
            if (tsapp_add_precise_cyclic_message(0x100, 0, false, 10, 2000) == 0)
            {
                Log("Add precise cyclic message success");
            }
            else
                Log("Add precise cyclic message fail");
        }

        private void button5_Click(object sender, EventArgs e)
        {
            if (tsapp_delete_precise_cyclic_message(0x123, 0, false, 2000) == 0)
            {
                Log("Delete precise cyclic message success");
            }
            else
                Log("Delete precise cyclic message fail");
            if (tsapp_delete_precise_cyclic_message(0x456, 0, false, 2000) == 0)
            {
                Log("Delete precise cyclic message success");
            }
            else
                Log("Delete precise cyclic message fail");
            if (tsapp_delete_precise_cyclic_message(0x789, 0, false, 2000) == 0)
            {
                Log("Delete precise cyclic message success");
            }
            else
                Log("Delete precise cyclic message fail");
            if (tsapp_delete_precise_cyclic_message(0x100, 0, false, 2000) == 0)
            {
                Log("Delete precise cyclic message success");
            }
            else
                Log("Delete precise cyclic message fail");
        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {
            if (cbbLINNodeType.SelectedIndex < -1)
            {
                MessageBox.Show("请先选择LIN节点类型","警告",MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }
            TsMasterApi.tslin_set_node_functiontype((int)APP_CHANNEL.CHN1, (TLINNodeType)cbbLINNodeType.SelectedIndex);
        }

        private void btnClearScheduleTable_Click(object sender, EventArgs e)
        {
            TsMasterApi.tslin_clear_schedule_tables((int)APP_CHANNEL.CHN1);
        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void btnTransmitLIN_Click(object sender, EventArgs e)
        {
            TLIBLIN FLIN = new TLIBLIN((byte)APP_CHANNEL.CHN1, 0x3C, 8, true);
            FLIN.FData[0] = 0x64;  //NAD
            FLIN.FData[1] = 0x02;                //Data Length
            FLIN.FData[2] = 0x10;
            FLIN.FData[3] = 0x02; //Identifier
            for (int j = 4; j < 7; j++)
            {
                FLIN.FData[j] = 0xFF;
            }
            if (TsMasterApi.tsapp_transmit_lin_async(
                      ref FLIN
                      ) == (uint)0) //Means Read Success
            {
            }
        }

        private void btnReceiveLINMessages_Click(object sender, EventArgs e)
        {
            TLIBLIN[] revMsgList = new TLIBLIN[100];
            int retNum = 100;

                    int ret = TsMasterApi.tsfifo_receive_lin_msgs_list( ref revMsgList, ref retNum, (int)APP_CHANNEL.CHN1, true);
                    Log("Received:" + retNum.ToString());
            
        }

        private void btnSessionControl_Click(object sender, EventArgs e)
        {
            byte[] datas = new byte[11];
            unsafe
            {
                datas[0] = 0x34;
                datas[1] = 0x00;
                datas[2] = 0x44;
                datas[3] = 0x08;
                datas[4] = 0x00;
                datas[5] = 0xD0;
                datas[6] = 0x00;
                datas[7] = 0x00;
                datas[8] = 0x01;
                datas[9] = 0x30;
                datas[10] = 0x00;
                //TsCANApi.tsfifo_clear_lin_receive_buffers((IntPtr)vTSToolHandle, CHANNEL_INDEX.CHN1);
                fixed (byte* pData = &datas[0])
                {
                    if(TsMasterApi.tstp_lin_master_request((int)APP_CHANNEL.CHN1, 0x64, pData, 11, 1000) == 0x00)
                        Log("Transmit TP Package Success!");
                    else
                        Log("Transmit TP Package Failed!");
                }
            }
        }

        private void btnSetTPIntervalTime_Click(object sender, EventArgs e)
        {
            try
            {
                int intervalTime = Convert.ToInt32(tBIntervalTimeMs.Text);
                if (TsMasterApi.tstp_lin_master_request_intervalms((int)APP_CHANNEL.CHN1, (byte)intervalTime) == 0x00)
                    Log("Set TP Interval Time Success!");
                else
                    Log("Set TP Interval Time Failed!");
            }
            catch
            {
                Log("Convert Interval time failed");
            }
        }

        private void btnCreateEthernetDemo_Click(object sender, EventArgs e)
        {
            //FProgramName:唯一名称，后面的各种映射跟他绑定
            //第一步：初始化API模块,如果已经调用，这里则不需要调用
            //TsMasterApi.initialize_lib_tsmaster(FProgramName);
            //第二步：按需设置需要的通道数，比如，这里需要2个CAN通道，0个LIN通道   
            if (TsMasterApi.tsapp_set_can_channel_count(0) == 0)
            {
                Log("Set CAN Channel Count Success!");
            }
            else
                Log("Set CAN Channel Count Failed!");
            if (TsMasterApi.tsapp_set_lin_channel_count(0) == 0)
            {
                Log("Set LIN Channel Count Success!");
            }
            else
                Log("Set LIN Channel Count Failed!");
            if (TsMasterApi.set_ethernet_channel_count(1) == 0)
            {
                Log("Set Ethernet Channel Count Success!");
            }
            else
                Log("Set Ethernet Channel Count Failed!");
            //第三步：按需创建通道映射:
            if (TsMasterApi.tsapp_set_mapping_verbose(FProgramName, TLIBApplicationChannelType.APP_Ethernet,
                   (int)APP_CHANNEL.CHN1, "TE1051", TLIBBusToolDeviceType.TS_USB_DEVICE_EX, (int)TLIB_TS_Device_Sub_Type.TE1051, 0, (int)APP_CHANNEL.CHN1,true) == 0)
            {
            }
            //if (TsMasterApi.tsapp_configure_baudrate_can((int)APP_CHANNEL.CHN2, 500, false, true) == 0)
            //{
            //    Log("CAN Channel " + (1 + 1).ToString() + " baudrate has been configured");
            //}
            //else
            //{
            //    Log("CAN Channel " + (1 + 1).ToString() + " baudrate failed");
            //}
            //第五步：连接application：连接硬件通道并开启接收FIFO
            int connectResult = TsMasterApi.tsapp_connect();
            if (connectResult == 0)
            {
                Log("Connect Application Success!");
                TsMasterApi.tsfifo_enable_receive_fifo();
                Log("Start Receive FIFO!");  //如果不使能内部FIFO，无法使用Receive函数读取内部报文
            }
            else
            {
                //Log(connectResult);
                Log("Connect Application Failed! Please check the mapping table and whether the Hardware is Ready?!");
            }
        }

        private void button4_Click_2(object sender, EventArgs e)
        {
            unsafe
            {
                TLIBEthernetHeader data = new TLIBEthernetHeader();
                data.FIdxChn = 0;
                byte[] FDatas = new byte[1612];
                int i = 0;
                for (i = 0; i < 12; i++)
                {
                    FDatas[i] = 0xFF;
                }
                FDatas[12] = 0x04;
                FDatas[13] = 0x00;
                for (i = 0; i < 1024; i++)
                {
                    FDatas[i + 14] = (byte)i;
                }
                data.FEthernetPayloadLength = 1024;
                fixed (byte* p = &FDatas[0]) {
                    data.FEthernetDataAddr = p;
                    TsMasterApi.tsapp_transmit_ethernet_async(ref data);
                }
            }
        }

        private void btnEthernetCompressedMode_Click(object sender, EventArgs e)
        {
            TsMasterApi.tsapp_ethernet_channel_compress_mode(0, chkEtherCompressedMode.Checked);
        }

        private IntPtr FClientHandle;

        private void btnCreateRPCClient_Click(object sender, EventArgs e)
        {
            if (0 == TsMasterApi.rpc_tsmaster_create_client("TSMaster", ref FClientHandle))
            {
               Log("Add client success: " + FClientHandle.ToString());
                TsMasterApi.rpc_tsmaster_activate_client(FClientHandle, true);
            }
        }

        private void btnRemoveRPCClient_Click(object sender, EventArgs e)
        {
            if (0 == TsMasterApi.rpc_tsmaster_delete_client(FClientHandle))
            {
                Log("Remove client success: " + FClientHandle.ToString());
            }
        }

        private void btnCallSystemAPI_Click(object sender, EventArgs e)
        {
            byte[] ret = new byte[2056];
            unsafe
            {
                fixed (byte* pArg = &ret[0])
                {
                    TsMasterApi.rpc_tsmaster_call_system_api(FClientHandle, "com.cal_get_ecu_a2l_list", 1, 2056, (IntPtr)(&pArg));
                    string msg = Encoding.UTF8.GetString(ret);
                    MessageBox.Show(msg);
                }
            }
        }

        private void btnCallSystemAPI1_Click(object sender, EventArgs e)
        {
            byte[] ret = new byte[2056];
            unsafe
            {
                fixed (byte* pArg = &ret[0])
                {
                    TsMasterApi.rpc_tsmaster_call_system_api(FClientHandle, "app.get_configuration_file_path", 1, 2056, (IntPtr)(&pArg));
                    string msg = Encoding.UTF8.GetString(ret);
                    MessageBox.Show(msg);
                }
            }
        }
    }

    public class TCANHardwareInfo
    {
        public const int BUS_TOOL_DEVICE_TYPE_COUNT = 9;
        public static string[] BUS_TOOL_DEVICE_NAMES = new string[BUS_TOOL_DEVICE_TYPE_COUNT] {
            "Unknown bus tool",
            "TS Virtual Device",
            "Vector",
            "TOSUN",
            "PEAK",
            "Kvaser",
            "ZLG",
            "IntrepidCS",
            "TOSUN TC1005"
        };
        public const int TS_HWTYPE_MAX_CNT = 16;
        public static string[] TS_HWTYPE_NAMES = new string[TS_HWTYPE_MAX_CNT] {
            "Unknown",
            "TS.CAN Pro",
            "TS.CAN Lite1",
            "TC1001", //"TS.CAN Mini",
            "TL1001", //"TS.LIN Mini",
            "TC1011", //"TS.CAN FD Mini",
            "TS.LIN IO",
            "TC1002", //"TS.CAN Lite2",
            "TC1014",  //"TS.CAN.LIN"
            "TS.CAN FD 2517",
            "TC1026",  //TC1026 = 10,
            "TC1016",  //TC1016 = 11,
            "TC1012",  //TC1012 = 12,
            "TC1013",  //TC1013 = 13
            "TC7012",  //TC1013 = 14
            "TC1034"
        };
        public const int XL_HWTYPE_MAX_CNT = 114;
        public static string[] XL_HWTYPE_NAMES = new string[XL_HWTYPE_MAX_CNT]{
            "None",             // 0
            "VIRTUAL",             // 1
            "CANCARDX",             // 2
            "None",             // 3
            "None",             // 4
            "None",             // 5
            "CANAC2PCI",             // 6
            "None",             // 7
            "None",             // 8
            "None",             // 9
            "None",             // 10
            "None",             // 11
            "CANCARDY",             // 12
            "None",             // 13
            "None",             // 14
            "CANCARDXL",             // 15
            "None",             // 16
            "None",             // 17
            "None",             // 18
            "None",             // 19
            "None",             // 20
            "CANCASEXL",             // 21
            "None",             // 22
            "CANCASEXL_LOG_OBSOLETE",             // 23
            "None",             // 24
            "CANBOARDXL",             // 25
            "None",             // 26
            "CANBOARDXL_PXI",             // 27
            "None",             // 28
            "VN2600",             // 29
            "None",             // 30
            "None",             // 31
            "None",             // 32
            "None",             // 33
            "None",             // 34
            "None",             // 35
            "None",             // 36
            "VN3300",             // 37
            "None",             // 38
            "VN3600",             // 39
            "None",             // 40
            "VN7600",             // 41
            "None",             // 42
            "CANCARDXLE",             // 43
            "None",             // 44
            "VN8900",             // 45
            "None",             // 46
            "VN8950",             // 47
            "None",             // 48
            "None",             // 49
            "None",             // 50
            "None",             // 51
            "None",             // 52
            "VN2640",             // 53
            "None",             // 54
            "VN1610",             // 55
            "None",             // 56
            "VN1630",             // 57
            "None",             // 58
            "VN1640",             // 59
            "None",             // 60
            "VN8970",             // 61
            "None",             // 62
            "VN1611",             // 63
            "None",             // 64
            "VN5610",             // 65
            "VN5620",             // 66
            "VN7570",             // 67
            "None",             // 68
            "IPCLIENT",             // 69
            "None",             // 70
            "IPSERVER",             // 71
            "None",             // 72
            "VX1121",             // 73
            "None",             // 74
            "VX1131",             // 75
            "None",             // 76
            "VT6204",             // 77
            "None",             // 78
            "VN1630_LOG",             // 79
            "None",             // 80
            "VN7610",             // 81
            "None",             // 82
            "VN7572",             // 83
            "None",             // 84
            "VN8972",             // 85
            "None",             // 86
            "VN0601",             // 87
            "None",             // 88
            "VN5640",             // 89
            "None",             // 90
            "VX0312",             // 91
            "None",             // 92
            "None",             // 93
            "VH6501",             // 94
            "VN8800",             // 95
            "IPCL8800",             // 96
            "IPSRV8800",             // 97
            "CSMCAN",             // 98
            "None",             // 99
            "None",             // 100
            "VN5610A",             // 101
            "VN7640",             // 102
            "None",             // 103
            "VX1135",             // 104
            "VN4610",             // 105
            "None",             // 106
            "VT6306",             // 107
            "VT6104A",             // 108
            "VN5430",             // 109
            "None",             // 110
            "None",             // 111
            "VN1530",             // 112
            "VN1531"             // 113
            };
    }

}
