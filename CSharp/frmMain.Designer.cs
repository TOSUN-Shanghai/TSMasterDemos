namespace TSMasterAPI_CSharp
{
    partial class frmMain
    {
        /// <summary>
        /// 必需的设计器变量。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清理所有正在使用的资源。
        /// </summary>
        /// <param name="disposing">如果应释放托管资源，为 true；否则为 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows 窗体设计器生成的代码

        /// <summary>
        /// 设计器支持所需的方法 - 不要修改
        /// 使用代码编辑器修改此方法的内容。
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(frmMain));
            this.MM = new System.Windows.Forms.TextBox();
            this.splitter1 = new System.Windows.Forms.Splitter();
            this.tabControl1 = new System.Windows.Forms.TabControl();
            this.tabPage1 = new System.Windows.Forms.TabPage();
            this.btnCreateEthernetDemo = new System.Windows.Forms.Button();
            this.btnConfigBaudrateRegs = new System.Windows.Forms.Button();
            this.btnAddFilter = new System.Windows.Forms.Button();
            this.btnDeleteFilter = new System.Windows.Forms.Button();
            this.btnShowHardwareConfig = new System.Windows.Forms.Button();
            this.btnStartLogging = new System.Windows.Forms.Button();
            this.tbDeviceInformation = new System.Windows.Forms.TextBox();
            this.cbbDeviceIndex = new System.Windows.Forms.ComboBox();
            this.btnGetAppointtedDeviceInfo = new System.Windows.Forms.Button();
            this.tBDeviceNumber = new System.Windows.Forms.TextBox();
            this.btnGetDeviceNum = new System.Windows.Forms.Button();
            this.btnGetAllHardwareInfos = new System.Windows.Forms.Button();
            this.btnDeleteChannelMapping = new System.Windows.Forms.Button();
            this.btnGetChannelMapping = new System.Windows.Forms.Button();
            this.btnCreateDemoConfiguration = new System.Windows.Forms.Button();
            this.label13 = new System.Windows.Forms.Label();
            this.tBCANFDDataBaudrate = new System.Windows.Forms.TextBox();
            this.label12 = new System.Windows.Forms.Label();
            this.tBCANFDArbBaudrate = new System.Windows.Forms.TextBox();
            this.chkCANFDResistor = new System.Windows.Forms.CheckBox();
            this.chkCANResistor = new System.Windows.Forms.CheckBox();
            this.label11 = new System.Windows.Forms.Label();
            this.tBCANBaudrate = new System.Windows.Forms.TextBox();
            this.cbbAppChannel_CANFD = new System.Windows.Forms.ComboBox();
            this.label7 = new System.Windows.Forms.Label();
            this.cbbAppChannel_CAN = new System.Windows.Forms.ComboBox();
            this.lblAppChannel = new System.Windows.Forms.Label();
            this.cbbAppChannelIndex = new System.Windows.Forms.ComboBox();
            this.label19 = new System.Windows.Forms.Label();
            this.btnSetCANFDBaudrate = new System.Windows.Forms.Button();
            this.btnSetCANBaudrate = new System.Windows.Forms.Button();
            this.label18 = new System.Windows.Forms.Label();
            this.cbbHardwareChannel1 = new System.Windows.Forms.ComboBox();
            this.cbbSubDeviceType1 = new System.Windows.Forms.ComboBox();
            this.cbbDeviceType1 = new System.Windows.Forms.ComboBox();
            this.label10 = new System.Windows.Forms.Label();
            this.label9 = new System.Windows.Forms.Label();
            this.label8 = new System.Windows.Forms.Label();
            this.cbbChannelType1 = new System.Windows.Forms.ComboBox();
            this.label6 = new System.Windows.Forms.Label();
            this.cbbWindowName = new System.Windows.Forms.ComboBox();
            this.btnReadTurboMode = new System.Windows.Forms.Button();
            this.btnEnableTurboMode = new System.Windows.Forms.Button();
            this.btnUnregisterRxEvents = new System.Windows.Forms.Button();
            this.btnRegisterRxEvents = new System.Windows.Forms.Button();
            this.btnDisconnectApplication = new System.Windows.Forms.Button();
            this.btnConnectApplication = new System.Windows.Forms.Button();
            this.btnSetApplicationChannel1Mapping = new System.Windows.Forms.Button();
            this.tbGetLINCount = new System.Windows.Forms.TextBox();
            this.tbGetCANCount = new System.Windows.Forms.TextBox();
            this.tbLINCount = new System.Windows.Forms.TextBox();
            this.tbCANCount = new System.Windows.Forms.TextBox();
            this.label5 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.btnGetApplicationLINCount = new System.Windows.Forms.Button();
            this.btnGetApplicationCANCount = new System.Windows.Forms.Button();
            this.btnSetApplicationLINCount = new System.Windows.Forms.Button();
            this.btnSetApplicationCANCount = new System.Windows.Forms.Button();
            this.tbApplicationList = new System.Windows.Forms.TextBox();
            this.btnGetApplicationList = new System.Windows.Forms.Button();
            this.btnAddApplication = new System.Windows.Forms.Button();
            this.btnDeleteApplication = new System.Windows.Forms.Button();
            this.tbApplicationName = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.tabPage2 = new System.Windows.Forms.TabPage();
            this.lblCount = new System.Windows.Forms.LinkLabel();
            this.btnReceiveCANFDMsgs = new System.Windows.Forms.Button();
            this.btnReceiveCANMsgs = new System.Windows.Forms.Button();
            this.tbAddPeriodCANIntervalTime = new System.Windows.Forms.TextBox();
            this.tbDelPeriodCANID = new System.Windows.Forms.TextBox();
            this.tbAddPeriodCANID = new System.Windows.Forms.TextBox();
            this.label17 = new System.Windows.Forms.Label();
            this.label16 = new System.Windows.Forms.Label();
            this.label15 = new System.Windows.Forms.Label();
            this.label14 = new System.Windows.Forms.Label();
            this.btnDeleteAllCANPeriodicMessages = new System.Windows.Forms.Button();
            this.btnDeleteCANPeridicMessage = new System.Windows.Forms.Button();
            this.btnAddCANPerodicMessage = new System.Windows.Forms.Button();
            this.btnTransmitCANFDSync = new System.Windows.Forms.Button();
            this.btnTransmitCANFDAsync = new System.Windows.Forms.Button();
            this.btnTransmitCANSync = new System.Windows.Forms.Button();
            this.btnTransmitCANAsync = new System.Windows.Forms.Button();
            this.tabPage3 = new System.Windows.Forms.TabPage();
            this.tBIntervalTimeMs = new System.Windows.Forms.TextBox();
            this.btnSetTPIntervalTime = new System.Windows.Forms.Button();
            this.btnSessionControl = new System.Windows.Forms.Button();
            this.btnReceiveLINMessages = new System.Windows.Forms.Button();
            this.btnTransmitLIN = new System.Windows.Forms.Button();
            this.btnClearScheduleTable = new System.Windows.Forms.Button();
            this.cbbLINNodeType = new System.Windows.Forms.ComboBox();
            this.btnSetLINNodeType = new System.Windows.Forms.Button();
            this.tabPage4 = new System.Windows.Forms.TabPage();
            this.grpDatabaseQury = new System.Windows.Forms.GroupBox();
            this.label25 = new System.Windows.Forms.Label();
            this.tbSubSubIdx = new System.Windows.Forms.TextBox();
            this.label24 = new System.Windows.Forms.Label();
            this.tbSubIdx = new System.Windows.Forms.TextBox();
            this.cbbQueryType = new System.Windows.Forms.ComboBox();
            this.label23 = new System.Windows.Forms.Label();
            this.tBQueryResult = new System.Windows.Forms.TextBox();
            this.label22 = new System.Windows.Forms.Label();
            this.tbDBCQueryHandle = new System.Windows.Forms.TextBox();
            this.btnQuery = new System.Windows.Forms.Button();
            this.panel2 = new System.Windows.Forms.Panel();
            this.btnUnloadDBC = new System.Windows.Forms.Button();
            this.tbDBCPath = new System.Windows.Forms.TextBox();
            this.btnLoadDBCPath = new System.Windows.Forms.Button();
            this.label21 = new System.Windows.Forms.Label();
            this.label20 = new System.Windows.Forms.Label();
            this.tBUnloadDBCHandle = new System.Windows.Forms.TextBox();
            this.panel1 = new System.Windows.Forms.Panel();
            this.grpDBCDemoCommand = new System.Windows.Forms.GroupBox();
            this.cbbDBCChannel = new System.Windows.Forms.ComboBox();
            this.tBSignalName = new System.Windows.Forms.TextBox();
            this.label27 = new System.Windows.Forms.Label();
            this.label26 = new System.Windows.Forms.Label();
            this.tBMessageName = new System.Windows.Forms.TextBox();
            this.lblSignalValue = new System.Windows.Forms.Label();
            this.btnSetCANSignalValue = new System.Windows.Forms.Button();
            this.btnReadCANSignalValue = new System.Windows.Forms.Button();
            this.tabPage5 = new System.Windows.Forms.TabPage();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.btnAddReplayEngine = new System.Windows.Forms.Button();
            this.tabPage6 = new System.Windows.Forms.TabPage();
            this.button3 = new System.Windows.Forms.Button();
            this.tabPage7 = new System.Windows.Forms.TabPage();
            this.btnDeletePreciseCyclicMessage = new System.Windows.Forms.Button();
            this.btnAddPreciseCyclicMessage = new System.Windows.Forms.Button();
            this.tabPage8 = new System.Windows.Forms.TabPage();
            this.btnTransmitData = new System.Windows.Forms.Button();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.timer2 = new System.Windows.Forms.Timer(this.components);
            this.btnEthernetCompressedMode = new System.Windows.Forms.Button();
            this.chkEtherCompressedMode = new System.Windows.Forms.CheckBox();
            this.tabControl1.SuspendLayout();
            this.tabPage1.SuspendLayout();
            this.tabPage2.SuspendLayout();
            this.tabPage3.SuspendLayout();
            this.tabPage4.SuspendLayout();
            this.grpDatabaseQury.SuspendLayout();
            this.panel2.SuspendLayout();
            this.panel1.SuspendLayout();
            this.grpDBCDemoCommand.SuspendLayout();
            this.tabPage5.SuspendLayout();
            this.tabPage6.SuspendLayout();
            this.tabPage7.SuspendLayout();
            this.tabPage8.SuspendLayout();
            this.SuspendLayout();
            // 
            // MM
            // 
            this.MM.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.MM.Location = new System.Drawing.Point(0, 627);
            this.MM.Multiline = true;
            this.MM.Name = "MM";
            this.MM.Size = new System.Drawing.Size(1281, 212);
            this.MM.TabIndex = 3;
            // 
            // splitter1
            // 
            this.splitter1.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.splitter1.Location = new System.Drawing.Point(0, 624);
            this.splitter1.Name = "splitter1";
            this.splitter1.Size = new System.Drawing.Size(1281, 3);
            this.splitter1.TabIndex = 4;
            this.splitter1.TabStop = false;
            // 
            // tabControl1
            // 
            this.tabControl1.Controls.Add(this.tabPage1);
            this.tabControl1.Controls.Add(this.tabPage2);
            this.tabControl1.Controls.Add(this.tabPage3);
            this.tabControl1.Controls.Add(this.tabPage4);
            this.tabControl1.Controls.Add(this.tabPage5);
            this.tabControl1.Controls.Add(this.tabPage6);
            this.tabControl1.Controls.Add(this.tabPage7);
            this.tabControl1.Controls.Add(this.tabPage8);
            this.tabControl1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.tabControl1.Location = new System.Drawing.Point(0, 0);
            this.tabControl1.Name = "tabControl1";
            this.tabControl1.SelectedIndex = 0;
            this.tabControl1.Size = new System.Drawing.Size(1281, 624);
            this.tabControl1.TabIndex = 5;
            // 
            // tabPage1
            // 
            this.tabPage1.Controls.Add(this.btnCreateEthernetDemo);
            this.tabPage1.Controls.Add(this.btnConfigBaudrateRegs);
            this.tabPage1.Controls.Add(this.btnAddFilter);
            this.tabPage1.Controls.Add(this.btnDeleteFilter);
            this.tabPage1.Controls.Add(this.btnShowHardwareConfig);
            this.tabPage1.Controls.Add(this.btnStartLogging);
            this.tabPage1.Controls.Add(this.tbDeviceInformation);
            this.tabPage1.Controls.Add(this.cbbDeviceIndex);
            this.tabPage1.Controls.Add(this.btnGetAppointtedDeviceInfo);
            this.tabPage1.Controls.Add(this.tBDeviceNumber);
            this.tabPage1.Controls.Add(this.btnGetDeviceNum);
            this.tabPage1.Controls.Add(this.btnGetAllHardwareInfos);
            this.tabPage1.Controls.Add(this.btnDeleteChannelMapping);
            this.tabPage1.Controls.Add(this.btnGetChannelMapping);
            this.tabPage1.Controls.Add(this.btnCreateDemoConfiguration);
            this.tabPage1.Controls.Add(this.label13);
            this.tabPage1.Controls.Add(this.tBCANFDDataBaudrate);
            this.tabPage1.Controls.Add(this.label12);
            this.tabPage1.Controls.Add(this.tBCANFDArbBaudrate);
            this.tabPage1.Controls.Add(this.chkCANFDResistor);
            this.tabPage1.Controls.Add(this.chkCANResistor);
            this.tabPage1.Controls.Add(this.label11);
            this.tabPage1.Controls.Add(this.tBCANBaudrate);
            this.tabPage1.Controls.Add(this.cbbAppChannel_CANFD);
            this.tabPage1.Controls.Add(this.label7);
            this.tabPage1.Controls.Add(this.cbbAppChannel_CAN);
            this.tabPage1.Controls.Add(this.lblAppChannel);
            this.tabPage1.Controls.Add(this.cbbAppChannelIndex);
            this.tabPage1.Controls.Add(this.label19);
            this.tabPage1.Controls.Add(this.btnSetCANFDBaudrate);
            this.tabPage1.Controls.Add(this.btnSetCANBaudrate);
            this.tabPage1.Controls.Add(this.label18);
            this.tabPage1.Controls.Add(this.cbbHardwareChannel1);
            this.tabPage1.Controls.Add(this.cbbSubDeviceType1);
            this.tabPage1.Controls.Add(this.cbbDeviceType1);
            this.tabPage1.Controls.Add(this.label10);
            this.tabPage1.Controls.Add(this.label9);
            this.tabPage1.Controls.Add(this.label8);
            this.tabPage1.Controls.Add(this.cbbChannelType1);
            this.tabPage1.Controls.Add(this.label6);
            this.tabPage1.Controls.Add(this.cbbWindowName);
            this.tabPage1.Controls.Add(this.btnReadTurboMode);
            this.tabPage1.Controls.Add(this.btnEnableTurboMode);
            this.tabPage1.Controls.Add(this.btnUnregisterRxEvents);
            this.tabPage1.Controls.Add(this.btnRegisterRxEvents);
            this.tabPage1.Controls.Add(this.btnDisconnectApplication);
            this.tabPage1.Controls.Add(this.btnConnectApplication);
            this.tabPage1.Controls.Add(this.btnSetApplicationChannel1Mapping);
            this.tabPage1.Controls.Add(this.tbGetLINCount);
            this.tabPage1.Controls.Add(this.tbGetCANCount);
            this.tabPage1.Controls.Add(this.tbLINCount);
            this.tabPage1.Controls.Add(this.tbCANCount);
            this.tabPage1.Controls.Add(this.label5);
            this.tabPage1.Controls.Add(this.label4);
            this.tabPage1.Controls.Add(this.label3);
            this.tabPage1.Controls.Add(this.label2);
            this.tabPage1.Controls.Add(this.btnGetApplicationLINCount);
            this.tabPage1.Controls.Add(this.btnGetApplicationCANCount);
            this.tabPage1.Controls.Add(this.btnSetApplicationLINCount);
            this.tabPage1.Controls.Add(this.btnSetApplicationCANCount);
            this.tabPage1.Controls.Add(this.tbApplicationList);
            this.tabPage1.Controls.Add(this.btnGetApplicationList);
            this.tabPage1.Controls.Add(this.btnAddApplication);
            this.tabPage1.Controls.Add(this.btnDeleteApplication);
            this.tabPage1.Controls.Add(this.tbApplicationName);
            this.tabPage1.Controls.Add(this.label1);
            this.tabPage1.Controls.Add(this.button1);
            this.tabPage1.Controls.Add(this.button2);
            this.tabPage1.Location = new System.Drawing.Point(4, 22);
            this.tabPage1.Name = "tabPage1";
            this.tabPage1.Padding = new System.Windows.Forms.Padding(3);
            this.tabPage1.Size = new System.Drawing.Size(1273, 598);
            this.tabPage1.TabIndex = 0;
            this.tabPage1.Text = "Application";
            this.tabPage1.UseVisualStyleBackColor = true;
            this.tabPage1.Click += new System.EventHandler(this.tabPage1_Click);
            // 
            // btnCreateEthernetDemo
            // 
            this.btnCreateEthernetDemo.Location = new System.Drawing.Point(941, 267);
            this.btnCreateEthernetDemo.Name = "btnCreateEthernetDemo";
            this.btnCreateEthernetDemo.Size = new System.Drawing.Size(223, 23);
            this.btnCreateEthernetDemo.TabIndex = 75;
            this.btnCreateEthernetDemo.Text = "创建Ethernet Demo Application连接";
            this.btnCreateEthernetDemo.UseVisualStyleBackColor = true;
            this.btnCreateEthernetDemo.Click += new System.EventHandler(this.btnCreateEthernetDemo_Click);
            // 
            // btnConfigBaudrateRegs
            // 
            this.btnConfigBaudrateRegs.Location = new System.Drawing.Point(569, 499);
            this.btnConfigBaudrateRegs.Name = "btnConfigBaudrateRegs";
            this.btnConfigBaudrateRegs.Size = new System.Drawing.Size(223, 23);
            this.btnConfigBaudrateRegs.TabIndex = 74;
            this.btnConfigBaudrateRegs.Text = "Set CANFD Channel 1 Baudrate Register";
            this.btnConfigBaudrateRegs.UseVisualStyleBackColor = true;
            this.btnConfigBaudrateRegs.Click += new System.EventHandler(this.btnConfigBaudrateRegs_Click);
            // 
            // btnAddFilter
            // 
            this.btnAddFilter.Location = new System.Drawing.Point(569, 456);
            this.btnAddFilter.Name = "btnAddFilter";
            this.btnAddFilter.Size = new System.Drawing.Size(224, 23);
            this.btnAddFilter.TabIndex = 73;
            this.btnAddFilter.Text = "Add Filter(0x128: Standard)";
            this.btnAddFilter.UseVisualStyleBackColor = true;
            this.btnAddFilter.Click += new System.EventHandler(this.btnAddFilter_Click);
            // 
            // btnDeleteFilter
            // 
            this.btnDeleteFilter.Location = new System.Drawing.Point(819, 456);
            this.btnDeleteFilter.Name = "btnDeleteFilter";
            this.btnDeleteFilter.Size = new System.Drawing.Size(228, 23);
            this.btnDeleteFilter.TabIndex = 73;
            this.btnDeleteFilter.Text = "DeleteFilter(0x128: Standard)";
            this.btnDeleteFilter.UseVisualStyleBackColor = true;
            this.btnDeleteFilter.Click += new System.EventHandler(this.btnDeleteFilter_Click);
            // 
            // btnShowHardwareConfig
            // 
            this.btnShowHardwareConfig.Location = new System.Drawing.Point(275, 557);
            this.btnShowHardwareConfig.Name = "btnShowHardwareConfig";
            this.btnShowHardwareConfig.Size = new System.Drawing.Size(223, 23);
            this.btnShowHardwareConfig.TabIndex = 72;
            this.btnShowHardwareConfig.Text = "Show HardwareConfig";
            this.btnShowHardwareConfig.UseVisualStyleBackColor = true;
            this.btnShowHardwareConfig.Click += new System.EventHandler(this.btnShowHardwareConfig_Click);
            // 
            // btnStartLogging
            // 
            this.btnStartLogging.Location = new System.Drawing.Point(686, 180);
            this.btnStartLogging.Name = "btnStartLogging";
            this.btnStartLogging.Size = new System.Drawing.Size(223, 23);
            this.btnStartLogging.TabIndex = 71;
            this.btnStartLogging.Text = "Start Logging";
            this.btnStartLogging.UseVisualStyleBackColor = true;
            this.btnStartLogging.Click += new System.EventHandler(this.btnStartLogging_Click);
            // 
            // tbDeviceInformation
            // 
            this.tbDeviceInformation.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.tbDeviceInformation.Location = new System.Drawing.Point(1030, 53);
            this.tbDeviceInformation.Multiline = true;
            this.tbDeviceInformation.Name = "tbDeviceInformation";
            this.tbDeviceInformation.Size = new System.Drawing.Size(201, 108);
            this.tbDeviceInformation.TabIndex = 70;
            // 
            // cbbDeviceIndex
            // 
            this.cbbDeviceIndex.FormattingEnabled = true;
            this.cbbDeviceIndex.Location = new System.Drawing.Point(926, 85);
            this.cbbDeviceIndex.Name = "cbbDeviceIndex";
            this.cbbDeviceIndex.Size = new System.Drawing.Size(74, 20);
            this.cbbDeviceIndex.TabIndex = 69;
            // 
            // btnGetAppointtedDeviceInfo
            // 
            this.btnGetAppointtedDeviceInfo.Location = new System.Drawing.Point(686, 82);
            this.btnGetAppointtedDeviceInfo.Name = "btnGetAppointtedDeviceInfo";
            this.btnGetAppointtedDeviceInfo.Size = new System.Drawing.Size(223, 23);
            this.btnGetAppointtedDeviceInfo.TabIndex = 68;
            this.btnGetAppointtedDeviceInfo.Text = "Get Appointted Device Info";
            this.btnGetAppointtedDeviceInfo.UseVisualStyleBackColor = true;
            this.btnGetAppointtedDeviceInfo.Click += new System.EventHandler(this.btnGetAppointtedDeviceInfo_Click);
            // 
            // tBDeviceNumber
            // 
            this.tBDeviceNumber.Location = new System.Drawing.Point(926, 53);
            this.tBDeviceNumber.Name = "tBDeviceNumber";
            this.tBDeviceNumber.Size = new System.Drawing.Size(74, 21);
            this.tBDeviceNumber.TabIndex = 67;
            // 
            // btnGetDeviceNum
            // 
            this.btnGetDeviceNum.Location = new System.Drawing.Point(686, 53);
            this.btnGetDeviceNum.Name = "btnGetDeviceNum";
            this.btnGetDeviceNum.Size = new System.Drawing.Size(223, 23);
            this.btnGetDeviceNum.TabIndex = 66;
            this.btnGetDeviceNum.Text = "GetDeviceNum";
            this.btnGetDeviceNum.UseVisualStyleBackColor = true;
            this.btnGetDeviceNum.Click += new System.EventHandler(this.btnGetDeviceNum_Click);
            // 
            // btnGetAllHardwareInfos
            // 
            this.btnGetAllHardwareInfos.Location = new System.Drawing.Point(686, 111);
            this.btnGetAllHardwareInfos.Name = "btnGetAllHardwareInfos";
            this.btnGetAllHardwareInfos.Size = new System.Drawing.Size(223, 23);
            this.btnGetAllHardwareInfos.TabIndex = 65;
            this.btnGetAllHardwareInfos.Text = "Get All hardware Infos";
            this.btnGetAllHardwareInfos.UseVisualStyleBackColor = true;
            this.btnGetAllHardwareInfos.Click += new System.EventHandler(this.btnGetAllHardwareInfos_Click);
            // 
            // btnDeleteChannelMapping
            // 
            this.btnDeleteChannelMapping.Location = new System.Drawing.Point(24, 354);
            this.btnDeleteChannelMapping.Name = "btnDeleteChannelMapping";
            this.btnDeleteChannelMapping.Size = new System.Drawing.Size(223, 23);
            this.btnDeleteChannelMapping.TabIndex = 64;
            this.btnDeleteChannelMapping.Text = "Delete Application Channelx Mapping";
            this.btnDeleteChannelMapping.UseVisualStyleBackColor = true;
            this.btnDeleteChannelMapping.Click += new System.EventHandler(this.btnDeleteChannelMapping_Click);
            // 
            // btnGetChannelMapping
            // 
            this.btnGetChannelMapping.Location = new System.Drawing.Point(24, 325);
            this.btnGetChannelMapping.Name = "btnGetChannelMapping";
            this.btnGetChannelMapping.Size = new System.Drawing.Size(223, 23);
            this.btnGetChannelMapping.TabIndex = 63;
            this.btnGetChannelMapping.Text = "Get Application Channelx Mapping";
            this.btnGetChannelMapping.UseVisualStyleBackColor = true;
            this.btnGetChannelMapping.Click += new System.EventHandler(this.btnGetChannelMapping_Click);
            // 
            // btnCreateDemoConfiguration
            // 
            this.btnCreateDemoConfiguration.Location = new System.Drawing.Point(686, 267);
            this.btnCreateDemoConfiguration.Name = "btnCreateDemoConfiguration";
            this.btnCreateDemoConfiguration.Size = new System.Drawing.Size(223, 23);
            this.btnCreateDemoConfiguration.TabIndex = 62;
            this.btnCreateDemoConfiguration.Text = "创建CAN Demo Application连接";
            this.btnCreateDemoConfiguration.UseVisualStyleBackColor = true;
            this.btnCreateDemoConfiguration.Click += new System.EventHandler(this.btnCreateDemoConfiguration_Click);
            // 
            // label13
            // 
            this.label13.AutoSize = true;
            this.label13.Location = new System.Drawing.Point(663, 423);
            this.label13.Name = "label13";
            this.label13.Size = new System.Drawing.Size(65, 12);
            this.label13.TabIndex = 61;
            this.label13.Text = "Data(kBps)";
            // 
            // tBCANFDDataBaudrate
            // 
            this.tBCANFDDataBaudrate.Location = new System.Drawing.Point(771, 420);
            this.tBCANFDDataBaudrate.Name = "tBCANFDDataBaudrate";
            this.tBCANFDDataBaudrate.Size = new System.Drawing.Size(100, 21);
            this.tBCANFDDataBaudrate.TabIndex = 60;
            this.tBCANFDDataBaudrate.Text = "2000";
            this.tBCANFDDataBaudrate.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // label12
            // 
            this.label12.AutoSize = true;
            this.label12.Location = new System.Drawing.Point(437, 422);
            this.label12.Name = "label12";
            this.label12.Size = new System.Drawing.Size(59, 12);
            this.label12.TabIndex = 59;
            this.label12.Text = "Arb(kBps)";
            // 
            // tBCANFDArbBaudrate
            // 
            this.tBCANFDArbBaudrate.Location = new System.Drawing.Point(532, 419);
            this.tBCANFDArbBaudrate.Name = "tBCANFDArbBaudrate";
            this.tBCANFDArbBaudrate.Size = new System.Drawing.Size(100, 21);
            this.tBCANFDArbBaudrate.TabIndex = 58;
            this.tBCANFDArbBaudrate.Text = "500";
            this.tBCANFDArbBaudrate.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // chkCANFDResistor
            // 
            this.chkCANFDResistor.AutoSize = true;
            this.chkCANFDResistor.Checked = true;
            this.chkCANFDResistor.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkCANFDResistor.Location = new System.Drawing.Point(891, 422);
            this.chkCANFDResistor.Name = "chkCANFDResistor";
            this.chkCANFDResistor.Size = new System.Drawing.Size(156, 16);
            this.chkCANFDResistor.TabIndex = 57;
            this.chkCANFDResistor.Text = "Install 120Ω Resistor";
            this.chkCANFDResistor.UseVisualStyleBackColor = true;
            // 
            // chkCANResistor
            // 
            this.chkCANResistor.AutoSize = true;
            this.chkCANResistor.Checked = true;
            this.chkCANResistor.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkCANResistor.Location = new System.Drawing.Point(665, 385);
            this.chkCANResistor.Name = "chkCANResistor";
            this.chkCANResistor.Size = new System.Drawing.Size(156, 16);
            this.chkCANResistor.TabIndex = 56;
            this.chkCANResistor.Text = "Install 120Ω Resistor";
            this.chkCANResistor.UseVisualStyleBackColor = true;
            // 
            // label11
            // 
            this.label11.AutoSize = true;
            this.label11.Location = new System.Drawing.Point(437, 391);
            this.label11.Name = "label11";
            this.label11.Size = new System.Drawing.Size(89, 12);
            this.label11.TabIndex = 55;
            this.label11.Text = "Baudrate(kBps)";
            // 
            // tBCANBaudrate
            // 
            this.tBCANBaudrate.Location = new System.Drawing.Point(532, 385);
            this.tBCANBaudrate.Name = "tBCANBaudrate";
            this.tBCANBaudrate.Size = new System.Drawing.Size(100, 21);
            this.tBCANBaudrate.TabIndex = 54;
            this.tBCANBaudrate.Text = "500";
            this.tBCANBaudrate.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // cbbAppChannel_CANFD
            // 
            this.cbbAppChannel_CANFD.FormattingEnabled = true;
            this.cbbAppChannel_CANFD.Items.AddRange(new object[] {
            "Channel 1",
            "Channel 2",
            "Channel 3",
            "Channel 4",
            "Channel 5",
            "Channel 6",
            "Channel 7",
            "Channel 8"});
            this.cbbAppChannel_CANFD.Location = new System.Drawing.Point(341, 417);
            this.cbbAppChannel_CANFD.Name = "cbbAppChannel_CANFD";
            this.cbbAppChannel_CANFD.Size = new System.Drawing.Size(90, 20);
            this.cbbAppChannel_CANFD.TabIndex = 53;
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(270, 420);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(65, 12);
            this.label7.TabIndex = 52;
            this.label7.Text = "AppChannel";
            // 
            // cbbAppChannel_CAN
            // 
            this.cbbAppChannel_CAN.FormattingEnabled = true;
            this.cbbAppChannel_CAN.Items.AddRange(new object[] {
            "Channel 1",
            "Channel 2",
            "Channel 3",
            "Channel 4",
            "Channel 5",
            "Channel 6",
            "Channel 7",
            "Channel 8"});
            this.cbbAppChannel_CAN.Location = new System.Drawing.Point(341, 386);
            this.cbbAppChannel_CAN.Name = "cbbAppChannel_CAN";
            this.cbbAppChannel_CAN.Size = new System.Drawing.Size(90, 20);
            this.cbbAppChannel_CAN.TabIndex = 51;
            // 
            // lblAppChannel
            // 
            this.lblAppChannel.AutoSize = true;
            this.lblAppChannel.Location = new System.Drawing.Point(270, 389);
            this.lblAppChannel.Name = "lblAppChannel";
            this.lblAppChannel.Size = new System.Drawing.Size(65, 12);
            this.lblAppChannel.TabIndex = 50;
            this.lblAppChannel.Text = "AppChannel";
            // 
            // cbbAppChannelIndex
            // 
            this.cbbAppChannelIndex.FormattingEnabled = true;
            this.cbbAppChannelIndex.Items.AddRange(new object[] {
            "Channel 1",
            "Channel 2",
            "Channel 3",
            "Channel 4",
            "Channel 5",
            "Channel 6",
            "Channel 7",
            "Channel 8"});
            this.cbbAppChannelIndex.Location = new System.Drawing.Point(508, 327);
            this.cbbAppChannelIndex.Name = "cbbAppChannelIndex";
            this.cbbAppChannelIndex.Size = new System.Drawing.Size(90, 20);
            this.cbbAppChannelIndex.TabIndex = 49;
            this.cbbAppChannelIndex.SelectedIndexChanged += new System.EventHandler(this.cbbAppChannelIndex_SelectedIndexChanged);
            // 
            // label19
            // 
            this.label19.AutoSize = true;
            this.label19.Location = new System.Drawing.Point(437, 330);
            this.label19.Name = "label19";
            this.label19.Size = new System.Drawing.Size(65, 12);
            this.label19.TabIndex = 48;
            this.label19.Text = "AppChannel";
            // 
            // btnSetCANFDBaudrate
            // 
            this.btnSetCANFDBaudrate.Location = new System.Drawing.Point(24, 415);
            this.btnSetCANFDBaudrate.Name = "btnSetCANFDBaudrate";
            this.btnSetCANFDBaudrate.Size = new System.Drawing.Size(223, 23);
            this.btnSetCANFDBaudrate.TabIndex = 47;
            this.btnSetCANFDBaudrate.Text = "Set CANFD Baudrate";
            this.btnSetCANFDBaudrate.UseVisualStyleBackColor = true;
            this.btnSetCANFDBaudrate.Click += new System.EventHandler(this.btnSetCANFDBaudrate_Click);
            // 
            // btnSetCANBaudrate
            // 
            this.btnSetCANBaudrate.Location = new System.Drawing.Point(24, 386);
            this.btnSetCANBaudrate.Name = "btnSetCANBaudrate";
            this.btnSetCANBaudrate.Size = new System.Drawing.Size(223, 23);
            this.btnSetCANBaudrate.TabIndex = 46;
            this.btnSetCANBaudrate.Text = "Set CAN Baudrate";
            this.btnSetCANBaudrate.UseVisualStyleBackColor = true;
            this.btnSetCANBaudrate.Click += new System.EventHandler(this.btnSetCANBaudrate_Click);
            // 
            // label18
            // 
            this.label18.AutoSize = true;
            this.label18.Location = new System.Drawing.Point(1183, 330);
            this.label18.Name = "label18";
            this.label18.Size = new System.Drawing.Size(77, 12);
            this.label18.TabIndex = 45;
            this.label18.Text = "设置逻辑通道";
            // 
            // cbbHardwareChannel1
            // 
            this.cbbHardwareChannel1.FormattingEnabled = true;
            this.cbbHardwareChannel1.Items.AddRange(new object[] {
            "Channel 1",
            "Channel 2",
            "Channel 3",
            "Channel 4",
            "Channel 5",
            "Channel 6",
            "Channel 7",
            "Channel 8"});
            this.cbbHardwareChannel1.Location = new System.Drawing.Point(1074, 327);
            this.cbbHardwareChannel1.Name = "cbbHardwareChannel1";
            this.cbbHardwareChannel1.Size = new System.Drawing.Size(90, 20);
            this.cbbHardwareChannel1.TabIndex = 38;
            // 
            // cbbSubDeviceType1
            // 
            this.cbbSubDeviceType1.FormattingEnabled = true;
            this.cbbSubDeviceType1.Items.AddRange(new object[] {
            "1",
            "2",
            "3"});
            this.cbbSubDeviceType1.Location = new System.Drawing.Point(877, 326);
            this.cbbSubDeviceType1.Name = "cbbSubDeviceType1";
            this.cbbSubDeviceType1.Size = new System.Drawing.Size(90, 20);
            this.cbbSubDeviceType1.TabIndex = 37;
            // 
            // cbbDeviceType1
            // 
            this.cbbDeviceType1.FormattingEnabled = true;
            this.cbbDeviceType1.Items.AddRange(new object[] {
            "Unknown",
            "TS Virtual Device",
            "Vector XL Device",
            "TS USB Device",
            "PEAK_USB_DEVICE",
            "KVASER_USB_DEVICE",
            "RESERVED_DEVICE",
            "ICS_USB_DEVICE",
            "TS_TC1005_DEVICE"});
            this.cbbDeviceType1.Location = new System.Drawing.Point(686, 326);
            this.cbbDeviceType1.Name = "cbbDeviceType1";
            this.cbbDeviceType1.Size = new System.Drawing.Size(90, 20);
            this.cbbDeviceType1.TabIndex = 36;
            this.cbbDeviceType1.SelectedIndexChanged += new System.EventHandler(this.cbbDeviceType1_SelectedIndexChanged);
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.Location = new System.Drawing.Point(973, 329);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(95, 12);
            this.label10.TabIndex = 35;
            this.label10.Text = "HardwareChannel";
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Location = new System.Drawing.Point(788, 329);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(83, 12);
            this.label9.TabIndex = 34;
            this.label9.Text = "DeviceSubType";
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(615, 330);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(65, 12);
            this.label8.TabIndex = 33;
            this.label8.Text = "DeviceType";
            // 
            // cbbChannelType1
            // 
            this.cbbChannelType1.FormattingEnabled = true;
            this.cbbChannelType1.Items.AddRange(new object[] {
            "CAN",
            "LIN"});
            this.cbbChannelType1.Location = new System.Drawing.Point(341, 326);
            this.cbbChannelType1.Name = "cbbChannelType1";
            this.cbbChannelType1.Size = new System.Drawing.Size(90, 20);
            this.cbbChannelType1.TabIndex = 31;
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(264, 330);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(71, 12);
            this.label6.TabIndex = 29;
            this.label6.Text = "ChannelType";
            // 
            // cbbWindowName
            // 
            this.cbbWindowName.FormattingEnabled = true;
            this.cbbWindowName.Items.AddRange(new object[] {
            "System Messages",
            "CAN Trace",
            "CAN Transmit",
            "Graphics",
            "CAN Statistics",
            "CAN Database",
            "Hardware",
            "Bus Logging",
            "Meter",
            "Bus Playback",
            "LIN Trace",
            "LIN Transmit",
            "LIN Database",
            "TS Channel Mapping",
            "TS Python Console",
            "CAN FD Transmit",
            "Python Script Editor",
            "C Script Editor",
            "CAN / CAN FD Trace",
            "System Information",
            "Panel",
            "CAN Remaining Bus Simulation",
            "MATLAB Automation Controller"});
            this.cbbWindowName.Location = new System.Drawing.Point(750, 560);
            this.cbbWindowName.Name = "cbbWindowName";
            this.cbbWindowName.Size = new System.Drawing.Size(359, 20);
            this.cbbWindowName.TabIndex = 28;
            // 
            // btnReadTurboMode
            // 
            this.btnReadTurboMode.Location = new System.Drawing.Point(275, 514);
            this.btnReadTurboMode.Name = "btnReadTurboMode";
            this.btnReadTurboMode.Size = new System.Drawing.Size(223, 23);
            this.btnReadTurboMode.TabIndex = 27;
            this.btnReadTurboMode.Text = "Read Turbo Mode";
            this.btnReadTurboMode.UseVisualStyleBackColor = true;
            // 
            // btnEnableTurboMode
            // 
            this.btnEnableTurboMode.Location = new System.Drawing.Point(24, 514);
            this.btnEnableTurboMode.Name = "btnEnableTurboMode";
            this.btnEnableTurboMode.Size = new System.Drawing.Size(223, 23);
            this.btnEnableTurboMode.TabIndex = 26;
            this.btnEnableTurboMode.Text = "EnableTurboMode";
            this.btnEnableTurboMode.UseVisualStyleBackColor = true;
            // 
            // btnUnregisterRxEvents
            // 
            this.btnUnregisterRxEvents.Location = new System.Drawing.Point(275, 485);
            this.btnUnregisterRxEvents.Name = "btnUnregisterRxEvents";
            this.btnUnregisterRxEvents.Size = new System.Drawing.Size(223, 23);
            this.btnUnregisterRxEvents.TabIndex = 25;
            this.btnUnregisterRxEvents.Text = "Unregister Rx Events";
            this.btnUnregisterRxEvents.UseVisualStyleBackColor = true;
            this.btnUnregisterRxEvents.Click += new System.EventHandler(this.btnUnregisterRxEvents_Click);
            // 
            // btnRegisterRxEvents
            // 
            this.btnRegisterRxEvents.Location = new System.Drawing.Point(24, 485);
            this.btnRegisterRxEvents.Name = "btnRegisterRxEvents";
            this.btnRegisterRxEvents.Size = new System.Drawing.Size(223, 23);
            this.btnRegisterRxEvents.TabIndex = 24;
            this.btnRegisterRxEvents.Text = "Register Rx Events";
            this.btnRegisterRxEvents.UseVisualStyleBackColor = true;
            this.btnRegisterRxEvents.Click += new System.EventHandler(this.btnRegisterRxEvents_Click);
            // 
            // btnDisconnectApplication
            // 
            this.btnDisconnectApplication.Location = new System.Drawing.Point(275, 456);
            this.btnDisconnectApplication.Name = "btnDisconnectApplication";
            this.btnDisconnectApplication.Size = new System.Drawing.Size(223, 23);
            this.btnDisconnectApplication.TabIndex = 23;
            this.btnDisconnectApplication.Text = "Disconnect Application";
            this.btnDisconnectApplication.UseVisualStyleBackColor = true;
            this.btnDisconnectApplication.Click += new System.EventHandler(this.btnDisconnectApplication_Click);
            // 
            // btnConnectApplication
            // 
            this.btnConnectApplication.Location = new System.Drawing.Point(24, 456);
            this.btnConnectApplication.Name = "btnConnectApplication";
            this.btnConnectApplication.Size = new System.Drawing.Size(223, 23);
            this.btnConnectApplication.TabIndex = 22;
            this.btnConnectApplication.Text = "Connect Application";
            this.btnConnectApplication.UseVisualStyleBackColor = true;
            this.btnConnectApplication.Click += new System.EventHandler(this.btnConnectApplication_Click);
            // 
            // btnSetApplicationChannel1Mapping
            // 
            this.btnSetApplicationChannel1Mapping.Location = new System.Drawing.Point(24, 296);
            this.btnSetApplicationChannel1Mapping.Name = "btnSetApplicationChannel1Mapping";
            this.btnSetApplicationChannel1Mapping.Size = new System.Drawing.Size(223, 23);
            this.btnSetApplicationChannel1Mapping.TabIndex = 20;
            this.btnSetApplicationChannel1Mapping.Text = "Set Application Channelx Mapping";
            this.btnSetApplicationChannel1Mapping.UseVisualStyleBackColor = true;
            this.btnSetApplicationChannel1Mapping.Click += new System.EventHandler(this.btnSetApplicationChannel1Mapping_Click);
            // 
            // tbGetLINCount
            // 
            this.tbGetLINCount.Location = new System.Drawing.Point(464, 269);
            this.tbGetLINCount.Name = "tbGetLINCount";
            this.tbGetLINCount.Size = new System.Drawing.Size(100, 21);
            this.tbGetLINCount.TabIndex = 19;
            this.tbGetLINCount.Text = "- -";
            // 
            // tbGetCANCount
            // 
            this.tbGetCANCount.Location = new System.Drawing.Point(464, 240);
            this.tbGetCANCount.Name = "tbGetCANCount";
            this.tbGetCANCount.Size = new System.Drawing.Size(100, 21);
            this.tbGetCANCount.TabIndex = 18;
            this.tbGetCANCount.Text = "- -";
            // 
            // tbLINCount
            // 
            this.tbLINCount.Location = new System.Drawing.Point(464, 211);
            this.tbLINCount.Name = "tbLINCount";
            this.tbLINCount.Size = new System.Drawing.Size(100, 21);
            this.tbLINCount.TabIndex = 17;
            this.tbLINCount.Text = "0";
            // 
            // tbCANCount
            // 
            this.tbCANCount.Location = new System.Drawing.Point(464, 182);
            this.tbCANCount.Name = "tbCANCount";
            this.tbCANCount.Size = new System.Drawing.Size(100, 21);
            this.tbCANCount.TabIndex = 16;
            this.tbCANCount.Text = "2";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(264, 272);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(167, 12);
            this.label5.TabIndex = 15;
            this.label5.Text = "LIN Channel Count Retrieved";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(264, 243);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(167, 12);
            this.label4.TabIndex = 14;
            this.label4.Text = "CAN Channel Count Retrieved";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(264, 214);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(149, 12);
            this.label3.TabIndex = 13;
            this.label3.Text = "LIN Channel Count To Set";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(264, 185);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(149, 12);
            this.label2.TabIndex = 12;
            this.label2.Text = "CAN Channel Count To Set";
            // 
            // btnGetApplicationLINCount
            // 
            this.btnGetApplicationLINCount.Location = new System.Drawing.Point(24, 267);
            this.btnGetApplicationLINCount.Name = "btnGetApplicationLINCount";
            this.btnGetApplicationLINCount.Size = new System.Drawing.Size(223, 23);
            this.btnGetApplicationLINCount.TabIndex = 11;
            this.btnGetApplicationLINCount.Text = "Get Application LIN Count";
            this.btnGetApplicationLINCount.UseVisualStyleBackColor = true;
            this.btnGetApplicationLINCount.Click += new System.EventHandler(this.btnGetApplicationLINCount_Click);
            // 
            // btnGetApplicationCANCount
            // 
            this.btnGetApplicationCANCount.Location = new System.Drawing.Point(24, 238);
            this.btnGetApplicationCANCount.Name = "btnGetApplicationCANCount";
            this.btnGetApplicationCANCount.Size = new System.Drawing.Size(223, 23);
            this.btnGetApplicationCANCount.TabIndex = 10;
            this.btnGetApplicationCANCount.Text = "Get Application CAN Count";
            this.btnGetApplicationCANCount.UseVisualStyleBackColor = true;
            this.btnGetApplicationCANCount.Click += new System.EventHandler(this.btnGetApplicationCANCount_Click);
            // 
            // btnSetApplicationLINCount
            // 
            this.btnSetApplicationLINCount.Location = new System.Drawing.Point(24, 209);
            this.btnSetApplicationLINCount.Name = "btnSetApplicationLINCount";
            this.btnSetApplicationLINCount.Size = new System.Drawing.Size(223, 23);
            this.btnSetApplicationLINCount.TabIndex = 9;
            this.btnSetApplicationLINCount.Text = "Set Application LIN Count";
            this.btnSetApplicationLINCount.UseVisualStyleBackColor = true;
            this.btnSetApplicationLINCount.Click += new System.EventHandler(this.btnSetApplicationLINCount_Click);
            // 
            // btnSetApplicationCANCount
            // 
            this.btnSetApplicationCANCount.Location = new System.Drawing.Point(24, 180);
            this.btnSetApplicationCANCount.Name = "btnSetApplicationCANCount";
            this.btnSetApplicationCANCount.Size = new System.Drawing.Size(223, 23);
            this.btnSetApplicationCANCount.TabIndex = 8;
            this.btnSetApplicationCANCount.Text = "Set Application CAN Count";
            this.btnSetApplicationCANCount.UseVisualStyleBackColor = true;
            this.btnSetApplicationCANCount.Click += new System.EventHandler(this.btnSetApplicationCANCount_Click);
            // 
            // tbApplicationList
            // 
            this.tbApplicationList.Location = new System.Drawing.Point(24, 140);
            this.tbApplicationList.Name = "tbApplicationList";
            this.tbApplicationList.Size = new System.Drawing.Size(608, 21);
            this.tbApplicationList.TabIndex = 7;
            // 
            // btnGetApplicationList
            // 
            this.btnGetApplicationList.Location = new System.Drawing.Point(24, 111);
            this.btnGetApplicationList.Name = "btnGetApplicationList";
            this.btnGetApplicationList.Size = new System.Drawing.Size(223, 23);
            this.btnGetApplicationList.TabIndex = 6;
            this.btnGetApplicationList.Text = "Get Application List";
            this.btnGetApplicationList.UseVisualStyleBackColor = true;
            this.btnGetApplicationList.Click += new System.EventHandler(this.btnGetApplicationList_Click);
            // 
            // btnAddApplication
            // 
            this.btnAddApplication.Location = new System.Drawing.Point(24, 82);
            this.btnAddApplication.Name = "btnAddApplication";
            this.btnAddApplication.Size = new System.Drawing.Size(223, 23);
            this.btnAddApplication.TabIndex = 5;
            this.btnAddApplication.Text = "Add Application";
            this.btnAddApplication.UseVisualStyleBackColor = true;
            this.btnAddApplication.Click += new System.EventHandler(this.btnAddApplication_Click);
            // 
            // btnDeleteApplication
            // 
            this.btnDeleteApplication.Location = new System.Drawing.Point(24, 53);
            this.btnDeleteApplication.Name = "btnDeleteApplication";
            this.btnDeleteApplication.Size = new System.Drawing.Size(223, 23);
            this.btnDeleteApplication.TabIndex = 4;
            this.btnDeleteApplication.Text = "Delete Application";
            this.btnDeleteApplication.UseVisualStyleBackColor = true;
            this.btnDeleteApplication.Click += new System.EventHandler(this.btnDeleteApplication_Click);
            // 
            // tbApplicationName
            // 
            this.tbApplicationName.Location = new System.Drawing.Point(139, 25);
            this.tbApplicationName.Name = "tbApplicationName";
            this.tbApplicationName.Size = new System.Drawing.Size(493, 21);
            this.tbApplicationName.TabIndex = 3;
            this.tbApplicationName.Text = "LibTSMasterDemo";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(22, 28);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(101, 12);
            this.label1.TabIndex = 2;
            this.label1.Text = "Application Name";
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(24, 558);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(223, 23);
            this.button1.TabIndex = 0;
            this.button1.Text = "Show Mapping Window";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(532, 558);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(212, 23);
            this.button2.TabIndex = 1;
            this.button2.Text = "Show TsMaster Window";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // tabPage2
            // 
            this.tabPage2.Controls.Add(this.lblCount);
            this.tabPage2.Controls.Add(this.btnReceiveCANFDMsgs);
            this.tabPage2.Controls.Add(this.btnReceiveCANMsgs);
            this.tabPage2.Controls.Add(this.tbAddPeriodCANIntervalTime);
            this.tabPage2.Controls.Add(this.tbDelPeriodCANID);
            this.tabPage2.Controls.Add(this.tbAddPeriodCANID);
            this.tabPage2.Controls.Add(this.label17);
            this.tabPage2.Controls.Add(this.label16);
            this.tabPage2.Controls.Add(this.label15);
            this.tabPage2.Controls.Add(this.label14);
            this.tabPage2.Controls.Add(this.btnDeleteAllCANPeriodicMessages);
            this.tabPage2.Controls.Add(this.btnDeleteCANPeridicMessage);
            this.tabPage2.Controls.Add(this.btnAddCANPerodicMessage);
            this.tabPage2.Controls.Add(this.btnTransmitCANFDSync);
            this.tabPage2.Controls.Add(this.btnTransmitCANFDAsync);
            this.tabPage2.Controls.Add(this.btnTransmitCANSync);
            this.tabPage2.Controls.Add(this.btnTransmitCANAsync);
            this.tabPage2.Location = new System.Drawing.Point(4, 22);
            this.tabPage2.Name = "tabPage2";
            this.tabPage2.Padding = new System.Windows.Forms.Padding(3);
            this.tabPage2.Size = new System.Drawing.Size(1273, 598);
            this.tabPage2.TabIndex = 1;
            this.tabPage2.Text = "CAN Communication";
            this.tabPage2.UseVisualStyleBackColor = true;
            // 
            // lblCount
            // 
            this.lblCount.AutoSize = true;
            this.lblCount.Location = new System.Drawing.Point(668, 48);
            this.lblCount.Name = "lblCount";
            this.lblCount.Size = new System.Drawing.Size(65, 12);
            this.lblCount.TabIndex = 17;
            this.lblCount.TabStop = true;
            this.lblCount.Text = "linkLabel1";
            // 
            // btnReceiveCANFDMsgs
            // 
            this.btnReceiveCANFDMsgs.Location = new System.Drawing.Point(382, 72);
            this.btnReceiveCANFDMsgs.Name = "btnReceiveCANFDMsgs";
            this.btnReceiveCANFDMsgs.Size = new System.Drawing.Size(243, 23);
            this.btnReceiveCANFDMsgs.TabIndex = 16;
            this.btnReceiveCANFDMsgs.Text = "Receive CANFD Messages";
            this.btnReceiveCANFDMsgs.UseVisualStyleBackColor = true;
            this.btnReceiveCANFDMsgs.Click += new System.EventHandler(this.button4_Click);
            // 
            // btnReceiveCANMsgs
            // 
            this.btnReceiveCANMsgs.Location = new System.Drawing.Point(382, 43);
            this.btnReceiveCANMsgs.Name = "btnReceiveCANMsgs";
            this.btnReceiveCANMsgs.Size = new System.Drawing.Size(243, 23);
            this.btnReceiveCANMsgs.TabIndex = 15;
            this.btnReceiveCANMsgs.Text = "Receive CAN Messages";
            this.btnReceiveCANMsgs.UseVisualStyleBackColor = true;
            this.btnReceiveCANMsgs.Click += new System.EventHandler(this.btnReceiveCANMsgs_Click);
            // 
            // tbAddPeriodCANIntervalTime
            // 
            this.tbAddPeriodCANIntervalTime.Location = new System.Drawing.Point(551, 176);
            this.tbAddPeriodCANIntervalTime.Name = "tbAddPeriodCANIntervalTime";
            this.tbAddPeriodCANIntervalTime.Size = new System.Drawing.Size(74, 21);
            this.tbAddPeriodCANIntervalTime.TabIndex = 13;
            this.tbAddPeriodCANIntervalTime.Text = "10";
            this.tbAddPeriodCANIntervalTime.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // tbDelPeriodCANID
            // 
            this.tbDelPeriodCANID.Location = new System.Drawing.Point(382, 205);
            this.tbDelPeriodCANID.Name = "tbDelPeriodCANID";
            this.tbDelPeriodCANID.Size = new System.Drawing.Size(74, 21);
            this.tbDelPeriodCANID.TabIndex = 12;
            this.tbDelPeriodCANID.Text = "0x55";
            this.tbDelPeriodCANID.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // tbAddPeriodCANID
            // 
            this.tbAddPeriodCANID.Location = new System.Drawing.Point(382, 176);
            this.tbAddPeriodCANID.Name = "tbAddPeriodCANID";
            this.tbAddPeriodCANID.Size = new System.Drawing.Size(74, 21);
            this.tbAddPeriodCANID.TabIndex = 11;
            this.tbAddPeriodCANID.Text = "0x55";
            this.tbAddPeriodCANID.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // label17
            // 
            this.label17.AutoSize = true;
            this.label17.Location = new System.Drawing.Point(641, 179);
            this.label17.Name = "label17";
            this.label17.Size = new System.Drawing.Size(227, 12);
            this.label17.TabIndex = 10;
            this.label17.Text = "Interval cannot be smaller than 0.5ms";
            // 
            // label16
            // 
            this.label16.AutoSize = true;
            this.label16.Location = new System.Drawing.Point(311, 208);
            this.label16.Name = "label16";
            this.label16.Size = new System.Drawing.Size(65, 12);
            this.label16.TabIndex = 9;
            this.label16.Text = "Identifier";
            // 
            // label15
            // 
            this.label15.AutoSize = true;
            this.label15.Location = new System.Drawing.Point(462, 179);
            this.label15.Name = "label15";
            this.label15.Size = new System.Drawing.Size(83, 12);
            this.label15.TabIndex = 8;
            this.label15.Text = "Interval(ms):";
            // 
            // label14
            // 
            this.label14.AutoSize = true;
            this.label14.Location = new System.Drawing.Point(311, 179);
            this.label14.Name = "label14";
            this.label14.Size = new System.Drawing.Size(65, 12);
            this.label14.TabIndex = 7;
            this.label14.Text = "Identifier";
            // 
            // btnDeleteAllCANPeriodicMessages
            // 
            this.btnDeleteAllCANPeriodicMessages.Location = new System.Drawing.Point(37, 232);
            this.btnDeleteAllCANPeriodicMessages.Name = "btnDeleteAllCANPeriodicMessages";
            this.btnDeleteAllCANPeriodicMessages.Size = new System.Drawing.Size(268, 23);
            this.btnDeleteAllCANPeriodicMessages.TabIndex = 6;
            this.btnDeleteAllCANPeriodicMessages.Text = "Delete all periodic CAN Messages";
            this.btnDeleteAllCANPeriodicMessages.UseVisualStyleBackColor = true;
            this.btnDeleteAllCANPeriodicMessages.Click += new System.EventHandler(this.btnDeleteAllCANPeriodicMessages_Click);
            // 
            // btnDeleteCANPeridicMessage
            // 
            this.btnDeleteCANPeridicMessage.Location = new System.Drawing.Point(37, 203);
            this.btnDeleteCANPeridicMessage.Name = "btnDeleteCANPeridicMessage";
            this.btnDeleteCANPeridicMessage.Size = new System.Drawing.Size(268, 23);
            this.btnDeleteCANPeridicMessage.TabIndex = 5;
            this.btnDeleteCANPeridicMessage.Text = "Delete CAN Message Periodlly";
            this.btnDeleteCANPeridicMessage.UseVisualStyleBackColor = true;
            this.btnDeleteCANPeridicMessage.Click += new System.EventHandler(this.btnDeleteCANPeridicMessage_Click);
            // 
            // btnAddCANPerodicMessage
            // 
            this.btnAddCANPerodicMessage.Location = new System.Drawing.Point(37, 174);
            this.btnAddCANPerodicMessage.Name = "btnAddCANPerodicMessage";
            this.btnAddCANPerodicMessage.Size = new System.Drawing.Size(268, 23);
            this.btnAddCANPerodicMessage.TabIndex = 4;
            this.btnAddCANPerodicMessage.Text = "Transmit CAN Message Periodlly";
            this.btnAddCANPerodicMessage.UseVisualStyleBackColor = true;
            this.btnAddCANPerodicMessage.Click += new System.EventHandler(this.btnAddCANPerodicMessage_Click);
            // 
            // btnTransmitCANFDSync
            // 
            this.btnTransmitCANFDSync.Location = new System.Drawing.Point(37, 130);
            this.btnTransmitCANFDSync.Name = "btnTransmitCANFDSync";
            this.btnTransmitCANFDSync.Size = new System.Drawing.Size(268, 23);
            this.btnTransmitCANFDSync.TabIndex = 3;
            this.btnTransmitCANFDSync.Text = "Transmit CANFD Message Synchronously";
            this.btnTransmitCANFDSync.UseVisualStyleBackColor = true;
            this.btnTransmitCANFDSync.Click += new System.EventHandler(this.btnTransmitCANFDSync_Click);
            // 
            // btnTransmitCANFDAsync
            // 
            this.btnTransmitCANFDAsync.Location = new System.Drawing.Point(37, 101);
            this.btnTransmitCANFDAsync.Name = "btnTransmitCANFDAsync";
            this.btnTransmitCANFDAsync.Size = new System.Drawing.Size(268, 23);
            this.btnTransmitCANFDAsync.TabIndex = 2;
            this.btnTransmitCANFDAsync.Text = "Transmit CANFD Message Asynchronously";
            this.btnTransmitCANFDAsync.UseVisualStyleBackColor = true;
            this.btnTransmitCANFDAsync.Click += new System.EventHandler(this.btnTransmitCANFDAsync_Click);
            // 
            // btnTransmitCANSync
            // 
            this.btnTransmitCANSync.Location = new System.Drawing.Point(37, 72);
            this.btnTransmitCANSync.Name = "btnTransmitCANSync";
            this.btnTransmitCANSync.Size = new System.Drawing.Size(268, 23);
            this.btnTransmitCANSync.TabIndex = 1;
            this.btnTransmitCANSync.Text = "Transmit CAN Message Synchronously";
            this.btnTransmitCANSync.UseVisualStyleBackColor = true;
            this.btnTransmitCANSync.Click += new System.EventHandler(this.btnTransmitCANSync_Click);
            // 
            // btnTransmitCANAsync
            // 
            this.btnTransmitCANAsync.Location = new System.Drawing.Point(37, 43);
            this.btnTransmitCANAsync.Name = "btnTransmitCANAsync";
            this.btnTransmitCANAsync.Size = new System.Drawing.Size(268, 23);
            this.btnTransmitCANAsync.TabIndex = 0;
            this.btnTransmitCANAsync.Text = "Transmit CAN Message Asynchronously";
            this.btnTransmitCANAsync.UseVisualStyleBackColor = true;
            this.btnTransmitCANAsync.Click += new System.EventHandler(this.btnTransmitCANAsync_Click);
            // 
            // tabPage3
            // 
            this.tabPage3.Controls.Add(this.tBIntervalTimeMs);
            this.tabPage3.Controls.Add(this.btnSetTPIntervalTime);
            this.tabPage3.Controls.Add(this.btnSessionControl);
            this.tabPage3.Controls.Add(this.btnReceiveLINMessages);
            this.tabPage3.Controls.Add(this.btnTransmitLIN);
            this.tabPage3.Controls.Add(this.btnClearScheduleTable);
            this.tabPage3.Controls.Add(this.cbbLINNodeType);
            this.tabPage3.Controls.Add(this.btnSetLINNodeType);
            this.tabPage3.Location = new System.Drawing.Point(4, 22);
            this.tabPage3.Name = "tabPage3";
            this.tabPage3.Size = new System.Drawing.Size(1273, 598);
            this.tabPage3.TabIndex = 2;
            this.tabPage3.Text = "LIN Communication";
            this.tabPage3.UseVisualStyleBackColor = true;
            // 
            // tBIntervalTimeMs
            // 
            this.tBIntervalTimeMs.Location = new System.Drawing.Point(401, 57);
            this.tBIntervalTimeMs.Name = "tBIntervalTimeMs";
            this.tBIntervalTimeMs.Size = new System.Drawing.Size(100, 21);
            this.tBIntervalTimeMs.TabIndex = 7;
            this.tBIntervalTimeMs.Text = "30";
            this.tBIntervalTimeMs.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // btnSetTPIntervalTime
            // 
            this.btnSetTPIntervalTime.Location = new System.Drawing.Point(517, 57);
            this.btnSetTPIntervalTime.Name = "btnSetTPIntervalTime";
            this.btnSetTPIntervalTime.Size = new System.Drawing.Size(185, 23);
            this.btnSetTPIntervalTime.TabIndex = 6;
            this.btnSetTPIntervalTime.Text = "SetTPIntervalTime";
            this.btnSetTPIntervalTime.UseVisualStyleBackColor = true;
            this.btnSetTPIntervalTime.Click += new System.EventHandler(this.btnSetTPIntervalTime_Click);
            // 
            // btnSessionControl
            // 
            this.btnSessionControl.Location = new System.Drawing.Point(33, 159);
            this.btnSessionControl.Name = "btnSessionControl";
            this.btnSessionControl.Size = new System.Drawing.Size(335, 23);
            this.btnSessionControl.TabIndex = 5;
            this.btnSessionControl.Text = "Session Control";
            this.btnSessionControl.UseVisualStyleBackColor = true;
            this.btnSessionControl.Click += new System.EventHandler(this.btnSessionControl_Click);
            // 
            // btnReceiveLINMessages
            // 
            this.btnReceiveLINMessages.Location = new System.Drawing.Point(33, 121);
            this.btnReceiveLINMessages.Name = "btnReceiveLINMessages";
            this.btnReceiveLINMessages.Size = new System.Drawing.Size(335, 23);
            this.btnReceiveLINMessages.TabIndex = 4;
            this.btnReceiveLINMessages.Text = "Receive LIN Message";
            this.btnReceiveLINMessages.UseVisualStyleBackColor = true;
            this.btnReceiveLINMessages.Click += new System.EventHandler(this.btnReceiveLINMessages_Click);
            // 
            // btnTransmitLIN
            // 
            this.btnTransmitLIN.Location = new System.Drawing.Point(33, 92);
            this.btnTransmitLIN.Name = "btnTransmitLIN";
            this.btnTransmitLIN.Size = new System.Drawing.Size(335, 23);
            this.btnTransmitLIN.TabIndex = 3;
            this.btnTransmitLIN.Text = "Transmit LIN Message";
            this.btnTransmitLIN.UseVisualStyleBackColor = true;
            this.btnTransmitLIN.Click += new System.EventHandler(this.btnTransmitLIN_Click);
            // 
            // btnClearScheduleTable
            // 
            this.btnClearScheduleTable.Location = new System.Drawing.Point(33, 26);
            this.btnClearScheduleTable.Name = "btnClearScheduleTable";
            this.btnClearScheduleTable.Size = new System.Drawing.Size(335, 23);
            this.btnClearScheduleTable.TabIndex = 2;
            this.btnClearScheduleTable.Text = "Clear LIN Schedule Table";
            this.btnClearScheduleTable.UseVisualStyleBackColor = true;
            this.btnClearScheduleTable.Click += new System.EventHandler(this.btnClearScheduleTable_Click);
            // 
            // cbbLINNodeType
            // 
            this.cbbLINNodeType.FormattingEnabled = true;
            this.cbbLINNodeType.Items.AddRange(new object[] {
            "MasterNode",
            "SlaveNode",
            "MonitorNode"});
            this.cbbLINNodeType.Location = new System.Drawing.Point(33, 55);
            this.cbbLINNodeType.Name = "cbbLINNodeType";
            this.cbbLINNodeType.Size = new System.Drawing.Size(121, 20);
            this.cbbLINNodeType.TabIndex = 1;
            // 
            // btnSetLINNodeType
            // 
            this.btnSetLINNodeType.Location = new System.Drawing.Point(177, 55);
            this.btnSetLINNodeType.Name = "btnSetLINNodeType";
            this.btnSetLINNodeType.Size = new System.Drawing.Size(191, 23);
            this.btnSetLINNodeType.TabIndex = 0;
            this.btnSetLINNodeType.Text = "Set LIN Node";
            this.btnSetLINNodeType.UseVisualStyleBackColor = true;
            this.btnSetLINNodeType.Click += new System.EventHandler(this.button8_Click);
            // 
            // tabPage4
            // 
            this.tabPage4.Controls.Add(this.grpDatabaseQury);
            this.tabPage4.Controls.Add(this.panel2);
            this.tabPage4.Controls.Add(this.panel1);
            this.tabPage4.Location = new System.Drawing.Point(4, 22);
            this.tabPage4.Name = "tabPage4";
            this.tabPage4.Size = new System.Drawing.Size(1273, 598);
            this.tabPage4.TabIndex = 3;
            this.tabPage4.Text = "DataBase";
            this.tabPage4.UseVisualStyleBackColor = true;
            // 
            // grpDatabaseQury
            // 
            this.grpDatabaseQury.Controls.Add(this.label25);
            this.grpDatabaseQury.Controls.Add(this.tbSubSubIdx);
            this.grpDatabaseQury.Controls.Add(this.label24);
            this.grpDatabaseQury.Controls.Add(this.tbSubIdx);
            this.grpDatabaseQury.Controls.Add(this.cbbQueryType);
            this.grpDatabaseQury.Controls.Add(this.label23);
            this.grpDatabaseQury.Controls.Add(this.tBQueryResult);
            this.grpDatabaseQury.Controls.Add(this.label22);
            this.grpDatabaseQury.Controls.Add(this.tbDBCQueryHandle);
            this.grpDatabaseQury.Controls.Add(this.btnQuery);
            this.grpDatabaseQury.Dock = System.Windows.Forms.DockStyle.Fill;
            this.grpDatabaseQury.Location = new System.Drawing.Point(0, 61);
            this.grpDatabaseQury.Name = "grpDatabaseQury";
            this.grpDatabaseQury.Size = new System.Drawing.Size(1273, 381);
            this.grpDatabaseQury.TabIndex = 10;
            this.grpDatabaseQury.TabStop = false;
            this.grpDatabaseQury.Text = "Database Query";
            // 
            // label25
            // 
            this.label25.AutoSize = true;
            this.label25.Location = new System.Drawing.Point(56, 134);
            this.label25.Name = "label25";
            this.label25.Size = new System.Drawing.Size(59, 12);
            this.label25.TabIndex = 15;
            this.label25.Text = "Sub Index";
            // 
            // tbSubSubIdx
            // 
            this.tbSubSubIdx.Location = new System.Drawing.Point(164, 134);
            this.tbSubSubIdx.Name = "tbSubSubIdx";
            this.tbSubSubIdx.Size = new System.Drawing.Size(84, 21);
            this.tbSubSubIdx.TabIndex = 14;
            this.tbSubSubIdx.Text = "0";
            this.tbSubSubIdx.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // label24
            // 
            this.label24.AutoSize = true;
            this.label24.Location = new System.Drawing.Point(56, 102);
            this.label24.Name = "label24";
            this.label24.Size = new System.Drawing.Size(35, 12);
            this.label24.TabIndex = 13;
            this.label24.Text = "Index";
            // 
            // tbSubIdx
            // 
            this.tbSubIdx.Location = new System.Drawing.Point(164, 93);
            this.tbSubIdx.Name = "tbSubIdx";
            this.tbSubIdx.Size = new System.Drawing.Size(84, 21);
            this.tbSubIdx.TabIndex = 12;
            this.tbSubIdx.Text = "0";
            this.tbSubIdx.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // cbbQueryType
            // 
            this.cbbQueryType.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.cbbQueryType.FormattingEnabled = true;
            this.cbbQueryType.Items.AddRange(new object[] {
            "DT_STR_Network_Name = 0                                       # 获取网络名称",
            "DT_STR_DBC_FileName = 1                                       # 获取dbc文件名",
            "DT_INT_Protocol_Type = 2                                      # 获取协议类型，0=CAN、1=J1" +
                "939",
            "DT_INT_3 = 3                                                  # unused",
            "DT_INT_4 = 4                                                  # unused",
            "DT_INT_5 = 5                                                  # unused",
            "DT_INT_6 = 6                                                  # unused",
            "DT_INT_7 = 7                                                  # unused",
            "DT_INT_8 = 8                                                  # unused",
            "DT_INT_9 = 9                                                  # unused",
            "DT_INT_Signal_List_Count = 10                                 # 获取信号表数量 = db.sgns" +
                ".count",
            "DT_INT_CAN_Message_List_Count = 11                            # 获取CAN报文表数量 = db.m" +
                "sgs.count",
            "DT_INT_CANFD_Message_List_Count = 12                          # 获取CAN FD报文表数量 = d" +
                "b.msgsFD.count",
            "DT_INT_CANJ1939_Message_List_Count = 13                       # 获取CAN J1939报文表数量 " +
                "= db.msgsJ1939.count",
            "DT_INT_Node_List_Count = 14                                   # 获取节点表数量 = db.node" +
                "s.count",
            "DT_INT_EnvVar_List_Count = 15                                 # 获取环境变量表数量 = db.en" +
                "vs.count",
            "DT_INT_ValTab_List_Count = 16                                 # 获取取值表数量 = db.valt" +
                "abs.count",
            "DT_INT_17 = 17                                                # unused",
            "DT_INT_18 = 18                                                # unused",
            "DT_INT_19 = 19                                                # unused",
            "DT_INT_Signal_List_Message_ID = 20                            # 获取信号表中第idx信号所在的报文" +
                "标识符 db.sgns[idx].message_id",
            "DT_INT_Signal_List_Value_Type = 21                            # 获取信号表中第idx信号值类型 0" +
                "-无符号整型 1-有符号整型 2-32位浮点 3-64位浮点",
            "DT_INT_Signal_List_Is_Motorola = 22                           # 获取信号表中第idx信号是否是Mo" +
                "torola格式，0-Intel格式、1-Motorola格式",
            "DT_INT_Signal_List_ValTab_Index = 23                          # 获取信号表中第idx信号所带的取值" +
                "表在取值表列表中的索引",
            "DT_INT_Signal_List_Mux_Type = 24                              # 获取信号表中第idx信号Mux类型" +
                "，0-普通信号, 1-multiplexor, 2-multiplexed信号",
            "DT_INT_Signal_List_Mux_Value = 25                             # 获取信号表中第idx信号作为mul" +
                "tiplexor的值",
            "DT_INT_Signal_List_Layout_Start = 26                          # 获取信号表中第idx信号在报文中的" +
                "起始位",
            "DT_INT_Signal_List_Length = 27                                # 获取信号表中第idx信号的信号长度" +
                "",
            "DT_DBL_Signal_List_Factor = 28                                # 获取信号表中第idx信号放大因子",
            "DT_DBL_Signal_List_Offset = 29                                # 获取信号表中第idx信号偏移量",
            "DT_DBL_Signal_List_InitValue = 30                             # 获取信号表中第idx信号初始值",
            "DT_DBL_Signal_List_Min = 31                                   # 获取信号表中第idx信号最小值",
            "DT_DBL_Signal_List_Max = 32                                   # 获取信号表中第idx信号最大值",
            "DT_STR_Signal_List_Name = 33                                  # 获取信号表中第idx信号名称",
            "DT_STR_Signal_List_Unit = 34                                  # 获取信号表中第idx信号单位",
            "DT_STR_Signal_List_Comment = 35                               # 获取信号表中第idx信号注释",
            "DT_INT_Signal_List_Message_Index = 36                         # 获取信号表中第idx信号所在的报文" +
                "在报文表中的索引 db.msgs[db.sgns[idx].message_idx]",
            "DT_INT_Signal_List_Message_Type = 37                          # 获取信号表中第idx信号所在的报文" +
                "的类型，0=CAN, 1=CANFD, 2=J1939",
            "DT_STR_Signal_List_Struct = 38                                # 获取信号表中第idx信号全部属性，" +
                "逗号分隔 db.sgns[idx]",
            "DT_INT_39 = 39                                                # unused",
            "DT_INT_CAN_Message_List_Type = 40                             # 获取CAN报文表中第idx报文类型" +
                "，cftStdCAN = 0, cftExtCAN = 1, cftJ1939 = 2, cftStdCANFD = 3, cftExtCANFD = 4",
            "DT_INT_CAN_Message_List_DLC = 41                              # 获取CAN报文表中第idx报文数据" +
                "长度",
            "DT_INT_CAN_Message_List_ID = 42                               # 获取CAN报文表中第idx报文标识" +
                "符",
            "DT_INT_CAN_Message_List_CycleTime = 43                        # 获取CAN报文表中第idx报文周期" +
                "",
            "DT_STR_CAN_Message_List_Name = 44                             # 获取CAN报文表中第idx报文名称" +
                "",
            "DT_STR_CAN_Message_List_Comment = 45                          # 获取CAN报文表中第idx报文注释" +
                "",
            "DT_INT_CAN_Message_List_TX_Node_Index = 46                    # 获取CAN报文表中第idx报文对应" +
                "的发送节点的索引",
            "DT_INT_CAN_Message_List_Owned_Signal_List_Count = 47          # 获取CAN报文表中第idx报文拥有" +
                "的信号数量 db.msgs[idx].sgns.count",
            "DT_INT_CAN_Message_List_Owned_Signal_List_Signal_Index = 48   # 获取CAN报文表中第idx报文中第" +
                "subidx信号在信号表中的索引 db.sgns[db.sgns.indexof(db.msgs[idx].sgns[subidx])]",
            "DT_STR_CAN_Message_List_Struct = 49                           # 获取CAN报文表中第idx报文全部" +
                "属性，逗号分隔 db.msgs[idx]",
            "DT_INT_50 = 50                                                # unused",
            "DT_INT_51 = 51                                                # unused",
            "DT_INT_52 = 52                                                # unused",
            "DT_INT_53 = 53                                                # unused",
            "DT_INT_54 = 54                                                # unused",
            "DT_INT_55 = 55                                                # unused",
            "DT_INT_56 = 56                                                # unused",
            "DT_INT_57 = 57                                                # unused",
            "DT_INT_58 = 58                                                # unused",
            "DT_INT_59 = 59                                                # unused",
            "DT_INT_CANFD_Message_List_Type = 60                           # 获取CANFD报文表中第idx报文" +
                "类型，cftStdCAN = 0, cftExtCAN = 1, cftJ1939 = 2, cftStdCANFD = 3, cftExtCANFD = 4",
            "DT_INT_CANFD_Message_List_DLC = 61                            # 获取CANFD报文表中第idx报文" +
                "数据长度",
            "DT_INT_CANFD_Message_List_ID = 62                             # 获取CANFD报文表中第idx报文" +
                "标识符",
            "DT_INT_CANFD_Message_List_CycleTime = 63                      # 获取CANFD报文表中第idx报文" +
                "周期",
            "DT_STR_CANFD_Message_List_Name = 64                           # 获取CANFD报文表中第idx报文" +
                "名称",
            "DT_STR_CANFD_Message_List_Comment = 65                        # 获取CANFD报文表中第idx报文" +
                "注释",
            "DT_INT_CANFD_Message_List_TX_Node_Index = 66                  # 获取CANFD报文表中第idx报文" +
                "对应的发送节点的索引",
            "DT_INT_CANFD_Message_List_Owned_Signal_List_Count = 67        # 获取CANFD报文表中第idx报文" +
                "拥有的信号数量 db.msgs[idx].sgns.count",
            "DT_INT_CANFD_Message_List_Owned_Signal_List_Signal_Index = 68 # 获取CANFD报文表中第idx报文" +
                "中第subidx信号在信号表中的索引 db.sgns[db.sgns.indexof(db.msgs[idx].sgns[subidx])]",
            "DT_INT_CANFD_Message_List_BRS = 69                            # 获取CANFD报文表中第idx报文" +
                "BRS，0-No BRS、1-BRS",
            "DT_STR_CANFD_Message_List_Struct = 70                         # 获取CANFD报文表中第idx报文" +
                "全部属性，逗号分隔 db.msgs[idx]",
            "DT_INT_71 = 71                                                # unused",
            "DT_INT_72 = 72                                                # unused",
            "DT_INT_73 = 73                                                # unused",
            "DT_INT_74 = 74                                                # unused",
            "DT_INT_75 = 75                                                # unused",
            "DT_INT_76 = 76                                                # unused",
            "DT_INT_77 = 77                                                # unused",
            "DT_INT_78 = 78                                                # unused",
            "DT_INT_79 = 79                                                # unused",
            "DT_INT_J1939_Message_List_Type = 80                           # 获取J1939报文表中第idx报文" +
                "类型，cftStdCAN = 0, cftExtCAN = 1, cftJ1939 = 2, cftStdCANFD = 3, cftExtCANFD = 4",
            "DT_INT_J1939_Message_List_DLC = 81                            # 获取J1939报文表中第idx报文" +
                "数据长度",
            "DT_INT_J1939_Message_List_ID = 82                             # 获取J1939报文表中第idx报文" +
                "标识符",
            "DT_INT_J1939_Message_List_CycleTime = 83                      # 获取J1939报文表中第idx报文" +
                "周期",
            "DT_STR_J1939_Message_List_Name = 84                           # 获取J1939报文表中第idx报文" +
                "名称",
            "DT_STR_J1939_Message_List_Comment = 85                        # 获取J1939报文表中第idx报文" +
                "注释",
            "DT_INT_J1939_Message_List_TX_Node_Index = 86                  # 获取J1939报文表中第idx报文" +
                "对应的发送节点的索引",
            "DT_INT_J1939_Message_List_Owned_Signal_List_Count = 87        # 获取J1939报文表中第idx报文" +
                "拥有的信号数量 db.msgs[idx].sgns.count",
            "DT_INT_J1939_Message_List_Owned_Signal_List_Signal_Index = 88 # 获取J1939报文表中第idx报文" +
                "中第subidx信号在信号表中的索引 db.sgns[db.sgns.indexof(db.msgs[idx].sgns[subidx])]",
            "DT_STR_J1939_Message_List_Struct = 89                         # 获取CAN报文表中第idx报文全部" +
                "属性，逗号分隔 db.msgs[idx]",
            "DT_INT_90 = 90                                                # unused",
            "DT_INT_91 = 91                                                # unused",
            "DT_INT_92 = 92                                                # unused",
            "DT_INT_93 = 93                                                # unused",
            "DT_INT_94 = 94                                                # unused",
            "DT_INT_95 = 95                                                # unused",
            "DT_INT_96 = 96                                                # unused",
            "DT_INT_97 = 97                                                # unused",
            "DT_INT_98 = 98                                                # unused",
            "DT_INT_99 = 99                                                # unused",
            "DT_INT_Node_List_Address = 100                                # 获取节点表中第idx节点地址，默认" +
                "为0",
            "DT_STR_Node_List_Name = 101                                   # 获取节点表中第idx节点名称",
            "DT_STR_Node_List_Comment = 102                                # 获取节点表中第idx节点注释",
            "DT_INT_Node_List_TX_CAN_Message_List_Count = 103              # 获取节点表中第idx节点所发送的C" +
                "AN报文数量 db.nodes[idx].txmsgs.count",
            "DT_INT_Node_List_TX_CAN_Message_List_Message_Index = 104      # 获取节点表中第idx节点所发送的s" +
                "ubidx报文在CAN报文表中的索引 db.msgs[db.msgs.indexof(db.nodes[idx].txmsgs[subidx])]",
            "DT_INT_Node_List_RX_CAN_Message_List_Count = 105              # 获取节点表中第idx节点所接收的C" +
                "AN报文数量",
            "DT_INT_Node_List_RX_CAN_Message_List_Message_Index = 106      # 获取节点表中第idx节点所接收的s" +
                "ubidx报文在CAN报文表中的索引",
            "DT_INT_Node_List_TX_FD_Message_List_Count = 107               # 获取节点表中第idx节点所发送的F" +
                "D报文数量 db.nodes[idx].txmsgs.count",
            "DT_INT_Node_List_TX_FD_Message_List_Message_Index = 108       # 获取节点表中第idx节点所发送的s" +
                "ubidx报文在FD报文表中的索引 db.msgs[db.msgs.indexof(db.nodes[idx].txmsgs[subidx])]",
            "DT_INT_Node_List_RX_FD_Message_List_Count = 109               # 获取节点表中第idx节点所接收的F" +
                "D报文数量",
            "DT_INT_Node_List_RX_FD_Message_List_Message_Index = 110       # 获取节点表中第idx节点所接收的s" +
                "ubidx报文在FD报文表中的索引",
            "DT_INT_Node_List_TX_J1939_Message_List_Count = 111            # 获取节点表中第idx节点所发送的J" +
                "1939报文数量 db.nodes[idx].txmsgs.count",
            "DT_INT_Node_List_TX_J1939_Message_List_Message_Index = 112    # 获取节点表中第idx节点所发送的s" +
                "ubidx报文在J1939报文表中的索引 db.msgs[db.msgs.indexof(db.nodes[idx].txmsgs[subidx])]",
            "DT_INT_Node_List_RX_J1939_Message_List_Count = 113            # 获取节点表中第idx节点所接收的J" +
                "1939报文数量",
            "DT_INT_Node_List_RX_J1939_Message_List_Message_Index = 114    # 获取节点表中第idx节点所接收的s" +
                "ubidx报文在J1939报文表中的索引",
            "DT_INT_Node_List_TX_Signal_List_Count = 115                   # 获取节点表中第idx节点所发送的信" +
                "号数量",
            "DT_INT_Node_List_TX_Signal_List_Signal_Index = 116            # 获取节点表中第idx节点所发送的s" +
                "ubidx信号在信号表中的索引",
            "DT_INT_Node_List_RX_Signal_List_Count = 117                   # 获取节点表中第idx节点所接收的信" +
                "号数量",
            "DT_INT_Node_List_RX_Signal_List_Signal_Index = 118            # 获取节点表中第idx节点所接收的s" +
                "ubidx信号在信号表中的索引",
            "DT_STR_Node_List_Struct = 119                                 # 获取节点表中第idx节点全部属性，" +
                "逗号分隔 db.nodes[idx]",
            "DT_INT_120 = 120                                              # unused",
            "DT_INT_121 = 121                                              # unused",
            "DT_INT_122 = 122                                              # unused",
            "DT_INT_123 = 123                                              # unused",
            "DT_INT_124 = 124                                              # unused",
            "DT_INT_125 = 125                                              # unused",
            "DT_INT_126 = 126                                              # unused",
            "DT_INT_127 = 127                                              # unused",
            "DT_INT_128 = 128                                              # unused",
            "DT_INT_129 = 129                                              # unused",
            "DT_INT_EnvVar_List_Value_Type = 130                           # 获取环境变量表中第idx环境变量值" +
                "类型，0-整型、1-浮点、2-字符串、3-数据",
            "DT_DBL_EnvVar_List_MIN = 131                                  # 获取环境变量表中第idx环境变量最" +
                "小值",
            "DT_DBL_EnvVar_List_MAX = 132                                  # 获取环境变量表中第idx环境变量最" +
                "大值",
            "DT_DBL_EnvVar_List_Init_Value = 133                           # 获取环境变量表中第idx环境变量初" +
                "始值",
            "DT_STR_EnvVar_List_Name = 134                                 # 获取环境变量表中第idx环境变量名" +
                "称",
            "DT_STR_EnvVar_List_Unit = 135                                 # 获取环境变量表中第idx环境变量单" +
                "位",
            "DT_STR_EnvVar_List_Comment = 136                              # 获取环境变量表中第idx环境变量注" +
                "释",
            "DT_STR_EnvVar_List_Struct = 137                               # 获取环境变量表中第idx环境变量全" +
                "部属性，逗号分隔 db.EnvVars[idx]",
            "DT_INT_138 = 138                                              # unused",
            "DT_INT_139 = 139                                              # unused",
            "DT_INT_ValTab_List_Item_List_Count = 140                      # 获取取值表中第idx取值表所包含的" +
                "值数量",
            "DT_INT_ValTab_List_Item_List_Name = 141                       # 获取取值表中第idx取值表名称",
            "DT_DBL_ValTab_List_Item_List_Value = 142                      # 获取取值表中第idx取值表中第su" +
                "bidx的值",
            "DT_STR_ValTab_List_Struct = 143                               # 获取取值表中第idx取值表全部属性" +
                "，逗号分隔 db.ValTabs[idx]"});
            this.cbbQueryType.Location = new System.Drawing.Point(90, 67);
            this.cbbQueryType.Name = "cbbQueryType";
            this.cbbQueryType.Size = new System.Drawing.Size(964, 20);
            this.cbbQueryType.TabIndex = 11;
            // 
            // label23
            // 
            this.label23.AutoSize = true;
            this.label23.Location = new System.Drawing.Point(56, 67);
            this.label23.Name = "label23";
            this.label23.Size = new System.Drawing.Size(65, 12);
            this.label23.TabIndex = 10;
            this.label23.Text = "Query Type";
            // 
            // tBQueryResult
            // 
            this.tBQueryResult.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.tBQueryResult.Location = new System.Drawing.Point(3, 172);
            this.tBQueryResult.Multiline = true;
            this.tBQueryResult.Name = "tBQueryResult";
            this.tBQueryResult.Size = new System.Drawing.Size(1267, 206);
            this.tBQueryResult.TabIndex = 9;
            this.tBQueryResult.Text = resources.GetString("tBQueryResult.Text");
            // 
            // label22
            // 
            this.label22.AutoSize = true;
            this.label22.Location = new System.Drawing.Point(56, 39);
            this.label22.Name = "label22";
            this.label22.Size = new System.Drawing.Size(65, 12);
            this.label22.TabIndex = 8;
            this.label22.Text = "DBC Handle";
            // 
            // tbDBCQueryHandle
            // 
            this.tbDBCQueryHandle.Location = new System.Drawing.Point(164, 36);
            this.tbDBCQueryHandle.Name = "tbDBCQueryHandle";
            this.tbDBCQueryHandle.Size = new System.Drawing.Size(84, 21);
            this.tbDBCQueryHandle.TabIndex = 7;
            this.tbDBCQueryHandle.Text = "1";
            this.tbDBCQueryHandle.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // btnQuery
            // 
            this.btnQuery.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.btnQuery.Location = new System.Drawing.Point(1095, 32);
            this.btnQuery.Name = "btnQuery";
            this.btnQuery.Size = new System.Drawing.Size(116, 114);
            this.btnQuery.TabIndex = 6;
            this.btnQuery.Text = "Query";
            this.btnQuery.UseVisualStyleBackColor = true;
            this.btnQuery.Click += new System.EventHandler(this.btnQuery_Click);
            // 
            // panel2
            // 
            this.panel2.Controls.Add(this.btnUnloadDBC);
            this.panel2.Controls.Add(this.tbDBCPath);
            this.panel2.Controls.Add(this.btnLoadDBCPath);
            this.panel2.Controls.Add(this.label21);
            this.panel2.Controls.Add(this.label20);
            this.panel2.Controls.Add(this.tBUnloadDBCHandle);
            this.panel2.Dock = System.Windows.Forms.DockStyle.Top;
            this.panel2.Location = new System.Drawing.Point(0, 0);
            this.panel2.Name = "panel2";
            this.panel2.Size = new System.Drawing.Size(1273, 61);
            this.panel2.TabIndex = 9;
            // 
            // btnUnloadDBC
            // 
            this.btnUnloadDBC.Location = new System.Drawing.Point(796, 19);
            this.btnUnloadDBC.Name = "btnUnloadDBC";
            this.btnUnloadDBC.Size = new System.Drawing.Size(75, 23);
            this.btnUnloadDBC.TabIndex = 4;
            this.btnUnloadDBC.Text = "UnLoad";
            this.btnUnloadDBC.UseVisualStyleBackColor = true;
            this.btnUnloadDBC.Click += new System.EventHandler(this.btnUnloadDBC_Click);
            // 
            // tbDBCPath
            // 
            this.tbDBCPath.Location = new System.Drawing.Point(138, 19);
            this.tbDBCPath.Name = "tbDBCPath";
            this.tbDBCPath.Size = new System.Drawing.Size(334, 21);
            this.tbDBCPath.TabIndex = 0;
            this.tbDBCPath.Text = "WhlSpeeds.dbc";
            // 
            // btnLoadDBCPath
            // 
            this.btnLoadDBCPath.Location = new System.Drawing.Point(478, 19);
            this.btnLoadDBCPath.Name = "btnLoadDBCPath";
            this.btnLoadDBCPath.Size = new System.Drawing.Size(75, 23);
            this.btnLoadDBCPath.TabIndex = 1;
            this.btnLoadDBCPath.Text = "Load";
            this.btnLoadDBCPath.UseVisualStyleBackColor = true;
            this.btnLoadDBCPath.Click += new System.EventHandler(this.btnLoadDBCPath_Click);
            // 
            // label21
            // 
            this.label21.AutoSize = true;
            this.label21.Location = new System.Drawing.Point(596, 26);
            this.label21.Name = "label21";
            this.label21.Size = new System.Drawing.Size(65, 12);
            this.label21.TabIndex = 5;
            this.label21.Text = "DBC Handle";
            // 
            // label20
            // 
            this.label20.AutoSize = true;
            this.label20.Location = new System.Drawing.Point(40, 24);
            this.label20.Name = "label20";
            this.label20.Size = new System.Drawing.Size(53, 12);
            this.label20.TabIndex = 2;
            this.label20.Text = "DBC Path";
            // 
            // tBUnloadDBCHandle
            // 
            this.tBUnloadDBCHandle.Location = new System.Drawing.Point(694, 21);
            this.tBUnloadDBCHandle.Name = "tBUnloadDBCHandle";
            this.tBUnloadDBCHandle.Size = new System.Drawing.Size(84, 21);
            this.tBUnloadDBCHandle.TabIndex = 3;
            this.tBUnloadDBCHandle.Text = "1";
            this.tBUnloadDBCHandle.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.grpDBCDemoCommand);
            this.panel1.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.panel1.Location = new System.Drawing.Point(0, 442);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(1273, 156);
            this.panel1.TabIndex = 8;
            // 
            // grpDBCDemoCommand
            // 
            this.grpDBCDemoCommand.Controls.Add(this.cbbDBCChannel);
            this.grpDBCDemoCommand.Controls.Add(this.tBSignalName);
            this.grpDBCDemoCommand.Controls.Add(this.label27);
            this.grpDBCDemoCommand.Controls.Add(this.label26);
            this.grpDBCDemoCommand.Controls.Add(this.tBMessageName);
            this.grpDBCDemoCommand.Controls.Add(this.lblSignalValue);
            this.grpDBCDemoCommand.Controls.Add(this.btnSetCANSignalValue);
            this.grpDBCDemoCommand.Controls.Add(this.btnReadCANSignalValue);
            this.grpDBCDemoCommand.Dock = System.Windows.Forms.DockStyle.Fill;
            this.grpDBCDemoCommand.Location = new System.Drawing.Point(0, 0);
            this.grpDBCDemoCommand.Name = "grpDBCDemoCommand";
            this.grpDBCDemoCommand.Size = new System.Drawing.Size(1273, 156);
            this.grpDBCDemoCommand.TabIndex = 0;
            this.grpDBCDemoCommand.TabStop = false;
            this.grpDBCDemoCommand.Text = "Demo Command";
            // 
            // cbbDBCChannel
            // 
            this.cbbDBCChannel.FormattingEnabled = true;
            this.cbbDBCChannel.Items.AddRange(new object[] {
            "CH1",
            "CH2",
            "CH3",
            "CH4"});
            this.cbbDBCChannel.Location = new System.Drawing.Point(279, 81);
            this.cbbDBCChannel.Name = "cbbDBCChannel";
            this.cbbDBCChannel.Size = new System.Drawing.Size(121, 20);
            this.cbbDBCChannel.TabIndex = 20;
            // 
            // tBSignalName
            // 
            this.tBSignalName.Location = new System.Drawing.Point(177, 80);
            this.tBSignalName.Name = "tBSignalName";
            this.tBSignalName.Size = new System.Drawing.Size(84, 21);
            this.tBSignalName.TabIndex = 19;
            this.tBSignalName.Text = "FL_Speed";
            this.tBSignalName.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // label27
            // 
            this.label27.AutoSize = true;
            this.label27.Location = new System.Drawing.Point(79, 83);
            this.label27.Name = "label27";
            this.label27.Size = new System.Drawing.Size(65, 12);
            this.label27.TabIndex = 18;
            this.label27.Text = "SignalName";
            // 
            // label26
            // 
            this.label26.AutoSize = true;
            this.label26.Location = new System.Drawing.Point(79, 44);
            this.label26.Name = "label26";
            this.label26.Size = new System.Drawing.Size(71, 12);
            this.label26.TabIndex = 17;
            this.label26.Text = "MessageName";
            // 
            // tBMessageName
            // 
            this.tBMessageName.Location = new System.Drawing.Point(177, 41);
            this.tBMessageName.Name = "tBMessageName";
            this.tBMessageName.Size = new System.Drawing.Size(84, 21);
            this.tBMessageName.TabIndex = 16;
            this.tBMessageName.Text = "Wheel_Speed";
            this.tBMessageName.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // lblSignalValue
            // 
            this.lblSignalValue.AutoSize = true;
            this.lblSignalValue.Location = new System.Drawing.Point(692, 50);
            this.lblSignalValue.Name = "lblSignalValue";
            this.lblSignalValue.Size = new System.Drawing.Size(23, 12);
            this.lblSignalValue.TabIndex = 2;
            this.lblSignalValue.Text = "0.0";
            // 
            // btnSetCANSignalValue
            // 
            this.btnSetCANSignalValue.Location = new System.Drawing.Point(419, 39);
            this.btnSetCANSignalValue.Name = "btnSetCANSignalValue";
            this.btnSetCANSignalValue.Size = new System.Drawing.Size(173, 23);
            this.btnSetCANSignalValue.TabIndex = 1;
            this.btnSetCANSignalValue.Text = "Set CAN Signal Value";
            this.btnSetCANSignalValue.UseVisualStyleBackColor = true;
            this.btnSetCANSignalValue.Click += new System.EventHandler(this.btnSetCANSignalValue_Click);
            // 
            // btnReadCANSignalValue
            // 
            this.btnReadCANSignalValue.Location = new System.Drawing.Point(419, 78);
            this.btnReadCANSignalValue.Name = "btnReadCANSignalValue";
            this.btnReadCANSignalValue.Size = new System.Drawing.Size(173, 23);
            this.btnReadCANSignalValue.TabIndex = 0;
            this.btnReadCANSignalValue.Text = "Read CAN Signal Value";
            this.btnReadCANSignalValue.UseVisualStyleBackColor = true;
            this.btnReadCANSignalValue.Click += new System.EventHandler(this.btnReadCANSignalValue_Click);
            // 
            // tabPage5
            // 
            this.tabPage5.Controls.Add(this.textBox1);
            this.tabPage5.Controls.Add(this.btnAddReplayEngine);
            this.tabPage5.Location = new System.Drawing.Point(4, 22);
            this.tabPage5.Name = "tabPage5";
            this.tabPage5.Size = new System.Drawing.Size(1273, 598);
            this.tabPage5.TabIndex = 4;
            this.tabPage5.Text = "OnlineReplay";
            this.tabPage5.UseVisualStyleBackColor = true;
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(275, 56);
            this.textBox1.Multiline = true;
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(645, 385);
            this.textBox1.TabIndex = 1;
            // 
            // btnAddReplayEngine
            // 
            this.btnAddReplayEngine.Location = new System.Drawing.Point(24, 56);
            this.btnAddReplayEngine.Name = "btnAddReplayEngine";
            this.btnAddReplayEngine.Size = new System.Drawing.Size(221, 23);
            this.btnAddReplayEngine.TabIndex = 0;
            this.btnAddReplayEngine.Text = "Add Replay Engine";
            this.btnAddReplayEngine.UseVisualStyleBackColor = true;
            this.btnAddReplayEngine.Click += new System.EventHandler(this.btnAddReplayEngine_Click);
            // 
            // tabPage6
            // 
            this.tabPage6.Controls.Add(this.button3);
            this.tabPage6.Location = new System.Drawing.Point(4, 22);
            this.tabPage6.Name = "tabPage6";
            this.tabPage6.Padding = new System.Windows.Forms.Padding(3);
            this.tabPage6.Size = new System.Drawing.Size(1273, 598);
            this.tabPage6.TabIndex = 5;
            this.tabPage6.Text = "UDS Diagnostic";
            this.tabPage6.UseVisualStyleBackColor = true;
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(138, 50);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(75, 23);
            this.button3.TabIndex = 0;
            this.button3.Text = "button3";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click_1);
            // 
            // tabPage7
            // 
            this.tabPage7.Controls.Add(this.btnDeletePreciseCyclicMessage);
            this.tabPage7.Controls.Add(this.btnAddPreciseCyclicMessage);
            this.tabPage7.Location = new System.Drawing.Point(4, 22);
            this.tabPage7.Name = "tabPage7";
            this.tabPage7.Size = new System.Drawing.Size(1273, 598);
            this.tabPage7.TabIndex = 6;
            this.tabPage7.Text = "tabPage7";
            this.tabPage7.UseVisualStyleBackColor = true;
            // 
            // btnDeletePreciseCyclicMessage
            // 
            this.btnDeletePreciseCyclicMessage.Location = new System.Drawing.Point(37, 110);
            this.btnDeletePreciseCyclicMessage.Name = "btnDeletePreciseCyclicMessage";
            this.btnDeletePreciseCyclicMessage.Size = new System.Drawing.Size(213, 23);
            this.btnDeletePreciseCyclicMessage.TabIndex = 1;
            this.btnDeletePreciseCyclicMessage.Text = "Delete Precise Cyclic Message";
            this.btnDeletePreciseCyclicMessage.UseVisualStyleBackColor = true;
            this.btnDeletePreciseCyclicMessage.Click += new System.EventHandler(this.button5_Click);
            // 
            // btnAddPreciseCyclicMessage
            // 
            this.btnAddPreciseCyclicMessage.Location = new System.Drawing.Point(37, 71);
            this.btnAddPreciseCyclicMessage.Name = "btnAddPreciseCyclicMessage";
            this.btnAddPreciseCyclicMessage.Size = new System.Drawing.Size(213, 23);
            this.btnAddPreciseCyclicMessage.TabIndex = 0;
            this.btnAddPreciseCyclicMessage.Text = "Add Precise Cyclic Message";
            this.btnAddPreciseCyclicMessage.UseVisualStyleBackColor = true;
            this.btnAddPreciseCyclicMessage.Click += new System.EventHandler(this.button4_Click_1);
            // 
            // tabPage8
            // 
            this.tabPage8.Controls.Add(this.chkEtherCompressedMode);
            this.tabPage8.Controls.Add(this.btnEthernetCompressedMode);
            this.tabPage8.Controls.Add(this.btnTransmitData);
            this.tabPage8.Location = new System.Drawing.Point(4, 22);
            this.tabPage8.Name = "tabPage8";
            this.tabPage8.Size = new System.Drawing.Size(1273, 598);
            this.tabPage8.TabIndex = 7;
            this.tabPage8.Text = "Ethernet";
            this.tabPage8.UseVisualStyleBackColor = true;
            // 
            // btnTransmitData
            // 
            this.btnTransmitData.Location = new System.Drawing.Point(128, 87);
            this.btnTransmitData.Name = "btnTransmitData";
            this.btnTransmitData.Size = new System.Drawing.Size(156, 23);
            this.btnTransmitData.TabIndex = 0;
            this.btnTransmitData.Text = "TransmitData";
            this.btnTransmitData.UseVisualStyleBackColor = true;
            this.btnTransmitData.Click += new System.EventHandler(this.button4_Click_2);
            // 
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Interval = 10;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // timer2
            // 
            this.timer2.Enabled = true;
            this.timer2.Tick += new System.EventHandler(this.timer2_Tick);
            // 
            // btnEthernetCompressedMode
            // 
            this.btnEthernetCompressedMode.Location = new System.Drawing.Point(128, 35);
            this.btnEthernetCompressedMode.Name = "btnEthernetCompressedMode";
            this.btnEthernetCompressedMode.Size = new System.Drawing.Size(156, 23);
            this.btnEthernetCompressedMode.TabIndex = 1;
            this.btnEthernetCompressedMode.Text = "Set Compressed Mode";
            this.btnEthernetCompressedMode.UseVisualStyleBackColor = true;
            this.btnEthernetCompressedMode.Click += new System.EventHandler(this.btnEthernetCompressedMode_Click);
            // 
            // chkEtherCompressedMode
            // 
            this.chkEtherCompressedMode.AutoSize = true;
            this.chkEtherCompressedMode.Checked = true;
            this.chkEtherCompressedMode.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkEtherCompressedMode.Location = new System.Drawing.Point(309, 39);
            this.chkEtherCompressedMode.Name = "chkEtherCompressedMode";
            this.chkEtherCompressedMode.Size = new System.Drawing.Size(120, 16);
            this.chkEtherCompressedMode.TabIndex = 2;
            this.chkEtherCompressedMode.Text = "IsCompressedMode";
            this.chkEtherCompressedMode.UseVisualStyleBackColor = true;
            // 
            // frmMain
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1281, 839);
            this.Controls.Add(this.tabControl1);
            this.Controls.Add(this.splitter1);
            this.Controls.Add(this.MM);
            this.Name = "frmMain";
            this.Text = "Form1";
            this.FormClosed += new System.Windows.Forms.FormClosedEventHandler(this.Form1_FormClosed);
            this.Load += new System.EventHandler(this.Form1_Load);
            this.tabControl1.ResumeLayout(false);
            this.tabPage1.ResumeLayout(false);
            this.tabPage1.PerformLayout();
            this.tabPage2.ResumeLayout(false);
            this.tabPage2.PerformLayout();
            this.tabPage3.ResumeLayout(false);
            this.tabPage3.PerformLayout();
            this.tabPage4.ResumeLayout(false);
            this.grpDatabaseQury.ResumeLayout(false);
            this.grpDatabaseQury.PerformLayout();
            this.panel2.ResumeLayout(false);
            this.panel2.PerformLayout();
            this.panel1.ResumeLayout(false);
            this.grpDBCDemoCommand.ResumeLayout(false);
            this.grpDBCDemoCommand.PerformLayout();
            this.tabPage5.ResumeLayout(false);
            this.tabPage5.PerformLayout();
            this.tabPage6.ResumeLayout(false);
            this.tabPage7.ResumeLayout(false);
            this.tabPage8.ResumeLayout(false);
            this.tabPage8.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox MM;
        private System.Windows.Forms.Splitter splitter1;
        private System.Windows.Forms.TabControl tabControl1;
        private System.Windows.Forms.TabPage tabPage1;
        private System.Windows.Forms.ComboBox cbbWindowName;
        private System.Windows.Forms.Button btnReadTurboMode;
        private System.Windows.Forms.Button btnEnableTurboMode;
        private System.Windows.Forms.Button btnUnregisterRxEvents;
        private System.Windows.Forms.Button btnRegisterRxEvents;
        private System.Windows.Forms.Button btnDisconnectApplication;
        private System.Windows.Forms.Button btnConnectApplication;
        private System.Windows.Forms.Button btnSetApplicationChannel1Mapping;
        private System.Windows.Forms.TextBox tbGetLINCount;
        private System.Windows.Forms.TextBox tbGetCANCount;
        private System.Windows.Forms.TextBox tbLINCount;
        private System.Windows.Forms.TextBox tbCANCount;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button btnGetApplicationLINCount;
        private System.Windows.Forms.Button btnGetApplicationCANCount;
        private System.Windows.Forms.Button btnSetApplicationLINCount;
        private System.Windows.Forms.Button btnSetApplicationCANCount;
        private System.Windows.Forms.TextBox tbApplicationList;
        private System.Windows.Forms.Button btnGetApplicationList;
        private System.Windows.Forms.Button btnAddApplication;
        private System.Windows.Forms.Button btnDeleteApplication;
        private System.Windows.Forms.TextBox tbApplicationName;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.TabPage tabPage2;
        private System.Windows.Forms.ComboBox cbbHardwareChannel1;
        private System.Windows.Forms.ComboBox cbbSubDeviceType1;
        private System.Windows.Forms.ComboBox cbbDeviceType1;
        private System.Windows.Forms.Label label10;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.ComboBox cbbChannelType1;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Button btnTransmitCANFDSync;
        private System.Windows.Forms.Button btnTransmitCANFDAsync;
        private System.Windows.Forms.Button btnTransmitCANSync;
        private System.Windows.Forms.Button btnTransmitCANAsync;
        private System.Windows.Forms.TabPage tabPage3;
        private System.Windows.Forms.TextBox tbAddPeriodCANIntervalTime;
        private System.Windows.Forms.TextBox tbDelPeriodCANID;
        private System.Windows.Forms.TextBox tbAddPeriodCANID;
        private System.Windows.Forms.Label label17;
        private System.Windows.Forms.Label label16;
        private System.Windows.Forms.Label label15;
        private System.Windows.Forms.Label label14;
        private System.Windows.Forms.Button btnDeleteAllCANPeriodicMessages;
        private System.Windows.Forms.Button btnDeleteCANPeridicMessage;
        private System.Windows.Forms.Button btnAddCANPerodicMessage;
        private System.Windows.Forms.Label label18;
        private System.Windows.Forms.ComboBox cbbAppChannelIndex;
        private System.Windows.Forms.Label label19;
        private System.Windows.Forms.Button btnSetCANFDBaudrate;
        private System.Windows.Forms.Button btnSetCANBaudrate;
        private System.Windows.Forms.ComboBox cbbAppChannel_CAN;
        private System.Windows.Forms.Label lblAppChannel;
        private System.Windows.Forms.Label label13;
        private System.Windows.Forms.TextBox tBCANFDDataBaudrate;
        private System.Windows.Forms.Label label12;
        private System.Windows.Forms.TextBox tBCANFDArbBaudrate;
        private System.Windows.Forms.CheckBox chkCANFDResistor;
        private System.Windows.Forms.CheckBox chkCANResistor;
        private System.Windows.Forms.Label label11;
        private System.Windows.Forms.TextBox tBCANBaudrate;
        private System.Windows.Forms.ComboBox cbbAppChannel_CANFD;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.Button btnReceiveCANMsgs;
        private System.Windows.Forms.Button btnReceiveCANFDMsgs;
        private System.Windows.Forms.Button btnCreateDemoConfiguration;
        private System.Windows.Forms.TabPage tabPage4;
        private System.Windows.Forms.Label label20;
        private System.Windows.Forms.Button btnLoadDBCPath;
        private System.Windows.Forms.TextBox tbDBCPath;
        private System.Windows.Forms.Label label21;
        private System.Windows.Forms.Button btnUnloadDBC;
        private System.Windows.Forms.TextBox tBUnloadDBCHandle;
        private System.Windows.Forms.GroupBox grpDatabaseQury;
        private System.Windows.Forms.Label label25;
        private System.Windows.Forms.TextBox tbSubSubIdx;
        private System.Windows.Forms.Label label24;
        private System.Windows.Forms.TextBox tbSubIdx;
        private System.Windows.Forms.ComboBox cbbQueryType;
        private System.Windows.Forms.Label label23;
        private System.Windows.Forms.TextBox tBQueryResult;
        private System.Windows.Forms.Label label22;
        private System.Windows.Forms.TextBox tbDBCQueryHandle;
        private System.Windows.Forms.Button btnQuery;
        private System.Windows.Forms.Panel panel2;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.GroupBox grpDBCDemoCommand;
        private System.Windows.Forms.Button btnReadCANSignalValue;
        private System.Windows.Forms.Button btnSetCANSignalValue;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.Label lblSignalValue;
        private System.Windows.Forms.TextBox tBSignalName;
        private System.Windows.Forms.Label label27;
        private System.Windows.Forms.Label label26;
        private System.Windows.Forms.TextBox tBMessageName;
        private System.Windows.Forms.Timer timer2;
        private System.Windows.Forms.LinkLabel lblCount;
        private System.Windows.Forms.Button btnDeleteChannelMapping;
        private System.Windows.Forms.Button btnGetChannelMapping;
        private System.Windows.Forms.ComboBox cbbDBCChannel;
        private System.Windows.Forms.Button btnGetAllHardwareInfos;
        private System.Windows.Forms.TextBox tbDeviceInformation;
        private System.Windows.Forms.ComboBox cbbDeviceIndex;
        private System.Windows.Forms.Button btnGetAppointtedDeviceInfo;
        private System.Windows.Forms.TextBox tBDeviceNumber;
        private System.Windows.Forms.Button btnGetDeviceNum;
        private System.Windows.Forms.Button btnStartLogging;
        private System.Windows.Forms.TabPage tabPage5;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.Button btnAddReplayEngine;
        private System.Windows.Forms.Button btnShowHardwareConfig;
        private System.Windows.Forms.Button btnDeleteFilter;
        private System.Windows.Forms.Button btnAddFilter;
        private System.Windows.Forms.TabPage tabPage6;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button btnConfigBaudrateRegs;
        private System.Windows.Forms.TabPage tabPage7;
        private System.Windows.Forms.Button btnDeletePreciseCyclicMessage;
        private System.Windows.Forms.Button btnAddPreciseCyclicMessage;
        private System.Windows.Forms.Button btnSetLINNodeType;
        private System.Windows.Forms.ComboBox cbbLINNodeType;
        private System.Windows.Forms.Button btnClearScheduleTable;
        private System.Windows.Forms.Button btnTransmitLIN;
        private System.Windows.Forms.Button btnReceiveLINMessages;
        private System.Windows.Forms.Button btnSessionControl;
        private System.Windows.Forms.Button btnSetTPIntervalTime;
        private System.Windows.Forms.TextBox tBIntervalTimeMs;
        private System.Windows.Forms.Button btnCreateEthernetDemo;
        private System.Windows.Forms.TabPage tabPage8;
        private System.Windows.Forms.Button btnTransmitData;
        private System.Windows.Forms.Button btnEthernetCompressedMode;
        private System.Windows.Forms.CheckBox chkEtherCompressedMode;
    }
}

