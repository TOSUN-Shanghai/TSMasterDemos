﻿using System;
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

namespace TSMasterAPI_CSharp
{
    public partial class frmMain : Form
    {
        public frmMain()
        {
            InitializeComponent();
        }

        private string FProgramName = "LibTSMasterDemo";
        private void Form1_Load(object sender, EventArgs e)
        {
            FProgramName = Path.GetFileNameWithoutExtension(Application.ExecutablePath);  //首先获取应用程序名称
            tbApplicationName.Text = FProgramName;        
            LoadDefaultState();
            //
            //初始化API模块:这是后续调用所有TsMasterApi函数的前提
            TsMasterApi.initialize_lib_tsmaster(FProgramName);
            //设置需要探测的硬件
            TsMasterApi.tsapp_set_vendor_detect_preferences(true, true, true, false, false, false);
            //
            vCANQueueEventObj += new TCANQueueEvent(OnCANRxEvent);
            vCANFDQueueEventObj += new TCANFDQueueEvent(OnCANFDRxEvent);
            vLINQueueEventObj += new TLINQueueEvent(OnLINRxEvent);
            //注册接收回调函数：在每一次的回调函数vCANQueueEventObj中刷新数据段
            if (TsMasterApi.tsapp_register_event_can((IntPtr)0, vCANQueueEventObj) != 0x00)
            {
                Log("Register CANRx Failed!");
            }
            cbbQueryType.SelectedIndex = 0;
        }

        private void CreateApplicationDemo()
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
            if (TsMasterApi.tsapp_set_mapping_verbose(FProgramName, TLIBApplicationChannelType.APP_CAN,
                  APP_CHANNEL.CHN1, "TC1005", TLIBBusToolDeviceType.TS_TC1005_DEVICE, 0, 0, HARDWARE_CHANNEL.CHN1) == 0)
            {
            }
            if (TsMasterApi.tsapp_set_mapping_verbose(FProgramName, TLIBApplicationChannelType.APP_CAN,
                  APP_CHANNEL.CHN2, "TC1005", TLIBBusToolDeviceType.TS_TC1005_DEVICE, 0, 0, HARDWARE_CHANNEL.CHN2) == 0)
            { }
            //把TC1005板卡的硬件通道1映射到驱动的逻辑通道1上面
            if (TsMasterApi.tsapp_set_mapping_verbose(FProgramName, TLIBApplicationChannelType.APP_CAN,
              APP_CHANNEL.CHN3, "TC1005", TLIBBusToolDeviceType.TS_TC1005_DEVICE, 0, 0, HARDWARE_CHANNEL.CHN3) == 0)
            {
                Log("Mappings of channel " + (1 + (int)0).ToString() + " has been set");
            }
            //把TC1005板卡的硬件通道2映射到驱动的逻辑通道2上面
            if (TsMasterApi.tsapp_set_mapping_verbose(FProgramName, TLIBApplicationChannelType.APP_CAN,
                  APP_CHANNEL.CHN4, "TC1005", TLIBBusToolDeviceType.TS_TC1005_DEVICE, 0, 0, HARDWARE_CHANNEL.CHN4) == 0)
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
            string connectResult = TsMasterApi.tsapp_get_error_description(TsMasterApi.tsapp_connect());
            if (connectResult == "OK")
            {
                Log("Connect Application Success!");
                TsMasterApi.tsfifo_enable_receive_fifo();
                Log("Start Receive FIFO!");  //如果不使能内部FIFO，无法使用Receive函数读取内部报文
            }
            else
            {
                Log(connectResult);
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
            cbbHardwareChannel1.SelectedIndex = (int)HARDWARE_CHANNEL.CHN1;  //默认选择该硬件设备的物理通道0
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
            TsMasterApi.finalize_lib_tsmaster();
        }

        private static TCANQueueEvent   vCANQueueEventObj;
        private static TCANFDQueueEvent vCANFDQueueEventObj;
        private static TLINQueueEvent vLINQueueEventObj;
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
            if (TsMasterApi.tsapp_get_application_list(ref applicationList) == 0)
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
                Log("Start Receive FIFO!");  //如果不使能内部FIFO，无法使用Receive函数读取内部报文
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
                                    (APP_CHANNEL)cbbAppChannelIndex.SelectedIndex, cbbDeviceType1.Text, (TLIBBusToolDeviceType)cbbDeviceType1.SelectedIndex, -1, 0, (HARDWARE_CHANNEL)0x51) == 0)
                {
                    Log("Mappings of channel " + (1 + (int)0).ToString() + " has been set");
                }
            }
            else
            {
                if (TsMasterApi.tsapp_set_mapping_verbose(tbApplicationName.Text, (TLIBApplicationChannelType)cbbChannelType1.SelectedIndex,
                    (APP_CHANNEL)cbbAppChannelIndex.SelectedIndex, cbbDeviceType1.Text, (TLIBBusToolDeviceType)cbbDeviceType1.SelectedIndex, cbbSubDeviceType1.SelectedIndex, 0, (HARDWARE_CHANNEL)cbbHardwareChannel1.SelectedIndex) == 0)
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
                        for (iTS = TLIB_TS_Device_Sub_Type.TS_UNKNOWN_DEVICE; iTS < TLIB_TS_Device_Sub_Type.TSCANFD2517; iTS++)
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
                case TLIBBusToolDeviceType.RESERVED_DEVICE: 
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
                if (TsMasterApi.tsapp_configure_baudrate_canfd(i, b, c, TLIBCANFDControllerType.lfdtISOFDCAN,
                             TLIBCANFDControllerMode.lfdmNormal, chkCANResistor.Checked) == 0)
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
            int revCnt = 0;
            revCnt = TsMasterApi.tsfifo_receive_can_message_list(ref canBuffer, 100, APP_CHANNEL.CHN1, READ_TX_RX_DEF.TX_RX_MESSAGES);  //如果执行失败，请检查是否通过TsMasterApi.tsapp_enable_receive_fifo();开启了内部Buffer
            if (revCnt == 0)
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
            revCnt = TsMasterApi.tsfifo_receive_canfd_message_list(ref canBuffer, 10, APP_CHANNEL.CHN1, READ_TX_RX_DEF.TX_RX_MESSAGES);  //如果执行失败，请检查是否通过TsMasterApi.tsapp_enable_receive_fifo();开启了内部Buffer
            if (revCnt == 0)
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



        private UInt32 FDBCHandle = 0;
        private void btnLoadDBCPath_Click(object sender, EventArgs e)
        {
            if (CheckResultOK(TsMasterApi.tsdb_unload_can_dbs()))
            {
                Log("Unload DBC Success!");
            }  
            //Database必须是绝对路径
            if (CheckResultOK(TsMasterApi.tsdb_load_can_db(Application.StartupPath  +  @".\" + tbDBCPath.Text, 
                new APP_CHANNEL[] { APP_CHANNEL.CHN1, APP_CHANNEL.CHN2, APP_CHANNEL.CHN3, APP_CHANNEL.CHN4 }, ref FDBCHandle)))
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
                Log("Error occured: " + TsMasterApi.tsapp_get_error_description(AResultCode));
                return false;
            }
        }

        private void btnUnloadDBC_Click(object sender, EventArgs e)
        {
            try
            {
                UInt32 ADBCHandle = Convert.ToUInt32(tBUnloadDBCHandle.Text);
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
            string retMsg = TsMasterApi.tsdb_get_can_db_info(
              Convert.ToUInt32(tbDBCQueryHandle.Text),
              cbbQueryType.SelectedIndex,
              Convert.ToInt32(tbSubIdx.Text),
              Convert.ToInt32(tbSubSubIdx.Text)
              );
            if(retMsg != "")  
             {
                tBQueryResult.Text += retMsg + "\r\n";
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
            if (TsMasterApi.tsapp_get_mapping_verbose(FProgramName,(TLIBApplicationChannelType)cbbChannelType1.SelectedIndex,
                (APP_CHANNEL)cbbAppChannelIndex.SelectedIndex, ref m) == 0)
            {
                Log("Get Mapping Success");
                MessageBox.Show("HardwareName:" + m.GetHWDeviceName() + "HardwareChannel:" + m.FHWChannelIndex.ToString()); 
            }
        }

        private void btnDeleteChannelMapping_Click(object sender, EventArgs e)
        {
            if (TsMasterApi.tsapp_del_mapping_verbose(FProgramName, (TLIBApplicationChannelType)cbbChannelType1.SelectedIndex,
                (APP_CHANNEL)cbbAppChannelIndex.SelectedIndex) == 0)
            {
                Log("Delete Mapping Success");
            }
        }

        private void btnGetAllHardwareInfos_Click(object sender, EventArgs e)
        {
            int hardwareNum = 0;
            TLIBHWInfo tmpDeviceInfo = new TLIBHWInfo(0);
            string retMessage = TsMasterApi.tsapp_get_error_description(TsMasterApi.tsapp_enumerate_hw_devices(out hardwareNum));
            if (retMessage == "OK")
            {
                LogDeviceInformation("Hardware Num:" + hardwareNum.ToString());
            }
            else
            {
                Log(retMessage);
                LogDeviceInformation("Enum hardware Info Failed！");
            }
            for (int i = 0; i < hardwareNum; i++)
            {
                if (TsMasterApi.tsapp_get_hw_info_by_index(i, ref tmpDeviceInfo) == 0)
                {
                    LogDeviceInformation(tmpDeviceInfo.FDeviceInformation);
                }
            }
        }

        private void btnCreateDemoConfiguration_Click(object sender, EventArgs e)
        {
            CreateApplicationDemo();
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
            TLIBHWInfo tmp = new TLIBHWInfo(0);
            string retMessage = TsMasterApi.tsapp_get_error_description(TsMasterApi.tsapp_enumerate_hw_devices(out hardwareNum));
            if (retMessage == "OK")
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
                LogDeviceInformation(retMessage);               
            }
        }

        private void btnGetAppointtedDeviceInfo_Click(object sender, EventArgs e)
        {
            if (cbbDeviceIndex.SelectedIndex < 0)
            {
                LogDeviceInformation("Please select device Index first!");
                return;
            }
            TLIBHWInfo tmpDeviceInfo = new TLIBHWInfo(0);
            if (TsMasterApi.tsapp_get_hw_info_by_index(cbbDeviceIndex.SelectedIndex, ref tmpDeviceInfo) == 0)
            {
                LogDeviceInformation(tmpDeviceInfo.FDeviceInformation);
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
                    true, TsMasterApi.TLIBOnlineReplayTimingMode.ortImmediately, 0, true, false,
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
    }
}
