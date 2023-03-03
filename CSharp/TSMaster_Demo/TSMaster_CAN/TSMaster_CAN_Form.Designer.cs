namespace TSMaster_CAN
{
    partial class TSMaster_CAN_Form
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(TSMaster_CAN_Form));
            this.btn_hw_config = new System.Windows.Forms.Button();
            this.btn_show_hw = new System.Windows.Forms.Button();
            this.btn_on_off = new System.Windows.Forms.Button();
            this.btn_load_candb = new System.Windows.Forms.Button();
            this.tabControl1 = new System.Windows.Forms.TabControl();
            this.tabPage1 = new System.Windows.Forms.TabPage();
            this.panle = new System.Windows.Forms.Panel();
            this.btn_pilter = new System.Windows.Forms.Button();
            this.label13 = new System.Windows.Forms.Label();
            this.tb_channel_pass = new System.Windows.Forms.TextBox();
            this.label14 = new System.Windows.Forms.Label();
            this.label15 = new System.Windows.Forms.Label();
            this.tb_id_pass = new System.Windows.Forms.TextBox();
            this.btn_stop_signal = new System.Windows.Forms.Button();
            this.btn_send_signal = new System.Windows.Forms.Button();
            this.tb_signal_value = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.cbb_signals = new System.Windows.Forms.ComboBox();
            this.cbb_msg_names = new System.Windows.Forms.ComboBox();
            this.btn_cyclic_msg = new System.Windows.Forms.Button();
            this.btn_send_one_msg = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            this.tabPage2 = new System.Windows.Forms.TabPage();
            this.button3 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.btn_uds_info = new System.Windows.Forms.TabPage();
            this.label10 = new System.Windows.Forms.Label();
            this.cbb_dlc = new System.Windows.Forms.ComboBox();
            this.label9 = new System.Windows.Forms.Label();
            this.cbb_datatype = new System.Windows.Forms.ComboBox();
            this.label8 = new System.Windows.Forms.Label();
            this.cbb_msgtype = new System.Windows.Forms.ComboBox();
            this.btn_uds_id = new System.Windows.Forms.Button();
            this.tb_function_id = new System.Windows.Forms.TextBox();
            this.label7 = new System.Windows.Forms.Label();
            this.tb_respond_id = new System.Windows.Forms.TextBox();
            this.label6 = new System.Windows.Forms.Label();
            this.tb_request_id = new System.Windows.Forms.TextBox();
            this.label5 = new System.Windows.Forms.Label();
            this.btn_send_pass_safe = new System.Windows.Forms.Button();
            this.label3 = new System.Windows.Forms.Label();
            this.btn_load_dll = new System.Windows.Forms.Button();
            this.tb_uds_msg_data = new System.Windows.Forms.TextBox();
            this.cbb_safe_level = new System.Windows.Forms.ComboBox();
            this.btn_send_uds_msg = new System.Windows.Forms.Button();
            this.tabPage3 = new System.Windows.Forms.TabPage();
            this.btn_set_signal_value = new System.Windows.Forms.Button();
            this.btn_get_signal_value = new System.Windows.Forms.Button();
            this.tb_read_write = new System.Windows.Forms.TextBox();
            this.lb_ASignaladdress = new System.Windows.Forms.Label();
            this.tv_rbs = new System.Windows.Forms.TreeView();
            this.contextMenuStrip1 = new System.Windows.Forms.ContextMenuStrip(this.components);
            this.tm_all_select = new System.Windows.Forms.ToolStripMenuItem();
            this.tm_all_not_select = new System.Windows.Forms.ToolStripMenuItem();
            this.lv_showmsg = new System.Windows.Forms.ListView();
            this.columnHeader6 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader8 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader1 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader2 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader3 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader7 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader4 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader5 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.panel2 = new System.Windows.Forms.Panel();
            this.panel1 = new System.Windows.Forms.Panel();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.tabControl1.SuspendLayout();
            this.tabPage1.SuspendLayout();
            this.panle.SuspendLayout();
            this.tabPage2.SuspendLayout();
            this.btn_uds_info.SuspendLayout();
            this.tabPage3.SuspendLayout();
            this.contextMenuStrip1.SuspendLayout();
            this.groupBox1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.groupBox2.SuspendLayout();
            this.panel2.SuspendLayout();
            this.panel1.SuspendLayout();
            this.SuspendLayout();
            // 
            // btn_hw_config
            // 
            this.btn_hw_config.Location = new System.Drawing.Point(6, 10);
            this.btn_hw_config.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.btn_hw_config.Name = "btn_hw_config";
            this.btn_hw_config.Size = new System.Drawing.Size(160, 40);
            this.btn_hw_config.TabIndex = 0;
            this.btn_hw_config.Text = "默认硬件配置";
            this.btn_hw_config.UseVisualStyleBackColor = true;
            this.btn_hw_config.Click += new System.EventHandler(this.btn_hw_config_Click);
            // 
            // btn_show_hw
            // 
            this.btn_show_hw.Location = new System.Drawing.Point(176, 10);
            this.btn_show_hw.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.btn_show_hw.Name = "btn_show_hw";
            this.btn_show_hw.Size = new System.Drawing.Size(207, 40);
            this.btn_show_hw.TabIndex = 1;
            this.btn_show_hw.Text = "打开硬件窗口配置";
            this.btn_show_hw.UseVisualStyleBackColor = true;
            this.btn_show_hw.Click += new System.EventHandler(this.btn_show_hw_Click);
            // 
            // btn_on_off
            // 
            this.btn_on_off.Location = new System.Drawing.Point(543, 10);
            this.btn_on_off.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.btn_on_off.Name = "btn_on_off";
            this.btn_on_off.Size = new System.Drawing.Size(138, 40);
            this.btn_on_off.TabIndex = 2;
            this.btn_on_off.Text = "连接";
            this.btn_on_off.UseVisualStyleBackColor = true;
            this.btn_on_off.Click += new System.EventHandler(this.btn_on_off_Click);
            // 
            // btn_load_candb
            // 
            this.btn_load_candb.Location = new System.Drawing.Point(394, 10);
            this.btn_load_candb.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.btn_load_candb.Name = "btn_load_candb";
            this.btn_load_candb.Size = new System.Drawing.Size(138, 40);
            this.btn_load_candb.TabIndex = 3;
            this.btn_load_candb.Text = "加载dbc";
            this.btn_load_candb.UseVisualStyleBackColor = true;
            this.btn_load_candb.Click += new System.EventHandler(this.btn_load_candb_Click);
            // 
            // tabControl1
            // 
            this.tabControl1.Controls.Add(this.tabPage1);
            this.tabControl1.Controls.Add(this.tabPage2);
            this.tabControl1.Controls.Add(this.btn_uds_info);
            this.tabControl1.Controls.Add(this.tabPage3);
            this.tabControl1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.tabControl1.Location = new System.Drawing.Point(0, 0);
            this.tabControl1.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.tabControl1.Name = "tabControl1";
            this.tabControl1.SelectedIndex = 0;
            this.tabControl1.Size = new System.Drawing.Size(1301, 348);
            this.tabControl1.TabIndex = 4;
            // 
            // tabPage1
            // 
            this.tabPage1.Controls.Add(this.panle);
            this.tabPage1.Controls.Add(this.btn_stop_signal);
            this.tabPage1.Controls.Add(this.btn_send_signal);
            this.tabPage1.Controls.Add(this.tb_signal_value);
            this.tabPage1.Controls.Add(this.label4);
            this.tabPage1.Controls.Add(this.label2);
            this.tabPage1.Controls.Add(this.label1);
            this.tabPage1.Controls.Add(this.cbb_signals);
            this.tabPage1.Controls.Add(this.cbb_msg_names);
            this.tabPage1.Controls.Add(this.btn_cyclic_msg);
            this.tabPage1.Controls.Add(this.btn_send_one_msg);
            this.tabPage1.Controls.Add(this.button1);
            this.tabPage1.Controls.Add(this.btn_hw_config);
            this.tabPage1.Controls.Add(this.btn_load_candb);
            this.tabPage1.Controls.Add(this.btn_show_hw);
            this.tabPage1.Controls.Add(this.btn_on_off);
            this.tabPage1.Location = new System.Drawing.Point(4, 31);
            this.tabPage1.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.tabPage1.Name = "tabPage1";
            this.tabPage1.Padding = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.tabPage1.Size = new System.Drawing.Size(1293, 313);
            this.tabPage1.TabIndex = 0;
            this.tabPage1.Text = "主界面";
            this.tabPage1.UseVisualStyleBackColor = true;
            // 
            // panle
            // 
            this.panle.Controls.Add(this.btn_pilter);
            this.panle.Controls.Add(this.label13);
            this.panle.Controls.Add(this.tb_channel_pass);
            this.panle.Controls.Add(this.label14);
            this.panle.Controls.Add(this.label15);
            this.panle.Controls.Add(this.tb_id_pass);
            this.panle.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.panle.Location = new System.Drawing.Point(6, 247);
            this.panle.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.panle.Name = "panle";
            this.panle.Size = new System.Drawing.Size(1281, 61);
            this.panle.TabIndex = 20;
            // 
            // btn_pilter
            // 
            this.btn_pilter.Location = new System.Drawing.Point(628, 14);
            this.btn_pilter.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.btn_pilter.Name = "btn_pilter";
            this.btn_pilter.Size = new System.Drawing.Size(138, 40);
            this.btn_pilter.TabIndex = 13;
            this.btn_pilter.Text = "确定";
            this.btn_pilter.UseVisualStyleBackColor = true;
            this.btn_pilter.Click += new System.EventHandler(this.btn_pilter_Click);
            // 
            // label13
            // 
            this.label13.AutoSize = true;
            this.label13.Location = new System.Drawing.Point(211, 24);
            this.label13.Margin = new System.Windows.Forms.Padding(6, 0, 6, 0);
            this.label13.Name = "label13";
            this.label13.Size = new System.Drawing.Size(76, 21);
            this.label13.TabIndex = 8;
            this.label13.Text = "Chnnal";
            // 
            // tb_channel_pass
            // 
            this.tb_channel_pass.Location = new System.Drawing.Point(297, 19);
            this.tb_channel_pass.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.tb_channel_pass.Name = "tb_channel_pass";
            this.tb_channel_pass.Size = new System.Drawing.Size(86, 31);
            this.tb_channel_pass.TabIndex = 7;
            // 
            // label14
            // 
            this.label14.AutoSize = true;
            this.label14.Location = new System.Drawing.Point(6, 24);
            this.label14.Margin = new System.Windows.Forms.Padding(6, 0, 6, 0);
            this.label14.Name = "label14";
            this.label14.Size = new System.Drawing.Size(180, 21);
            this.label14.TabIndex = 6;
            this.label14.Text = "过滤条件（pass）";
            // 
            // label15
            // 
            this.label15.AutoSize = true;
            this.label15.Location = new System.Drawing.Point(425, 24);
            this.label15.Margin = new System.Windows.Forms.Padding(6, 0, 6, 0);
            this.label15.Name = "label15";
            this.label15.Size = new System.Drawing.Size(65, 21);
            this.label15.TabIndex = 5;
            this.label15.Text = "CANID";
            // 
            // tb_id_pass
            // 
            this.tb_id_pass.Location = new System.Drawing.Point(512, 19);
            this.tb_id_pass.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.tb_id_pass.Name = "tb_id_pass";
            this.tb_id_pass.Size = new System.Drawing.Size(86, 31);
            this.tb_id_pass.TabIndex = 4;
            // 
            // btn_stop_signal
            // 
            this.btn_stop_signal.Location = new System.Drawing.Point(1137, 82);
            this.btn_stop_signal.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.btn_stop_signal.Name = "btn_stop_signal";
            this.btn_stop_signal.Size = new System.Drawing.Size(138, 40);
            this.btn_stop_signal.TabIndex = 18;
            this.btn_stop_signal.Text = "停止发送";
            this.btn_stop_signal.UseVisualStyleBackColor = true;
            this.btn_stop_signal.Click += new System.EventHandler(this.btn_stop_signal_Click);
            // 
            // btn_send_signal
            // 
            this.btn_send_signal.Location = new System.Drawing.Point(988, 82);
            this.btn_send_signal.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.btn_send_signal.Name = "btn_send_signal";
            this.btn_send_signal.Size = new System.Drawing.Size(138, 40);
            this.btn_send_signal.TabIndex = 17;
            this.btn_send_signal.Text = "发送";
            this.btn_send_signal.UseVisualStyleBackColor = true;
            this.btn_send_signal.Click += new System.EventHandler(this.btn_send_signal_Click);
            // 
            // tb_signal_value
            // 
            this.tb_signal_value.Location = new System.Drawing.Point(880, 80);
            this.tb_signal_value.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.tb_signal_value.Name = "tb_signal_value";
            this.tb_signal_value.Size = new System.Drawing.Size(94, 31);
            this.tb_signal_value.TabIndex = 16;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(728, 88);
            this.label4.Margin = new System.Windows.Forms.Padding(6, 0, 6, 0);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(142, 21);
            this.label4.TabIndex = 15;
            this.label4.Text = "Signal_value";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(356, 88);
            this.label2.Margin = new System.Windows.Forms.Padding(6, 0, 6, 0);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(131, 21);
            this.label2.TabIndex = 11;
            this.label2.Text = "Signal_Name";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(15, 88);
            this.label1.Margin = new System.Windows.Forms.Padding(6, 0, 6, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(98, 21);
            this.label1.TabIndex = 10;
            this.label1.Text = "Msg_Name";
            // 
            // cbb_signals
            // 
            this.cbb_signals.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cbb_signals.FormattingEnabled = true;
            this.cbb_signals.Location = new System.Drawing.Point(497, 82);
            this.cbb_signals.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.cbb_signals.Name = "cbb_signals";
            this.cbb_signals.Size = new System.Drawing.Size(218, 29);
            this.cbb_signals.TabIndex = 9;
            // 
            // cbb_msg_names
            // 
            this.cbb_msg_names.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cbb_msg_names.FormattingEnabled = true;
            this.cbb_msg_names.Location = new System.Drawing.Point(123, 82);
            this.cbb_msg_names.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.cbb_msg_names.Name = "cbb_msg_names";
            this.cbb_msg_names.Size = new System.Drawing.Size(218, 29);
            this.cbb_msg_names.TabIndex = 8;
            this.cbb_msg_names.SelectedIndexChanged += new System.EventHandler(this.cbb_msg_names_SelectedIndexChanged);
            // 
            // btn_cyclic_msg
            // 
            this.btn_cyclic_msg.Location = new System.Drawing.Point(988, 10);
            this.btn_cyclic_msg.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.btn_cyclic_msg.Name = "btn_cyclic_msg";
            this.btn_cyclic_msg.Size = new System.Drawing.Size(138, 40);
            this.btn_cyclic_msg.TabIndex = 6;
            this.btn_cyclic_msg.Text = "周期发送";
            this.btn_cyclic_msg.UseVisualStyleBackColor = true;
            this.btn_cyclic_msg.Click += new System.EventHandler(this.btn_cyclic_msg_Click);
            // 
            // btn_send_one_msg
            // 
            this.btn_send_one_msg.Location = new System.Drawing.Point(840, 10);
            this.btn_send_one_msg.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.btn_send_one_msg.Name = "btn_send_one_msg";
            this.btn_send_one_msg.Size = new System.Drawing.Size(138, 40);
            this.btn_send_one_msg.TabIndex = 5;
            this.btn_send_one_msg.Text = "单帧发送";
            this.btn_send_one_msg.UseVisualStyleBackColor = true;
            this.btn_send_one_msg.Click += new System.EventHandler(this.btn_send_one_msg_Click);
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(691, 10);
            this.button1.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(138, 40);
            this.button1.TabIndex = 4;
            this.button1.Text = "清空数据";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // tabPage2
            // 
            this.tabPage2.Controls.Add(this.button3);
            this.tabPage2.Controls.Add(this.button2);
            this.tabPage2.Location = new System.Drawing.Point(4, 31);
            this.tabPage2.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.tabPage2.Name = "tabPage2";
            this.tabPage2.Padding = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.tabPage2.Size = new System.Drawing.Size(1293, 313);
            this.tabPage2.TabIndex = 1;
            this.tabPage2.Text = "DBC信息";
            this.tabPage2.UseVisualStyleBackColor = true;
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(189, 10);
            this.button3.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(167, 40);
            this.button3.TabIndex = 2;
            this.button3.Text = "ASC转blf";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(11, 10);
            this.button2.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(167, 40);
            this.button2.TabIndex = 1;
            this.button2.Text = "blf转ASC";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // btn_uds_info
            // 
            this.btn_uds_info.Controls.Add(this.label10);
            this.btn_uds_info.Controls.Add(this.cbb_dlc);
            this.btn_uds_info.Controls.Add(this.label9);
            this.btn_uds_info.Controls.Add(this.cbb_datatype);
            this.btn_uds_info.Controls.Add(this.label8);
            this.btn_uds_info.Controls.Add(this.cbb_msgtype);
            this.btn_uds_info.Controls.Add(this.btn_uds_id);
            this.btn_uds_info.Controls.Add(this.tb_function_id);
            this.btn_uds_info.Controls.Add(this.label7);
            this.btn_uds_info.Controls.Add(this.tb_respond_id);
            this.btn_uds_info.Controls.Add(this.label6);
            this.btn_uds_info.Controls.Add(this.tb_request_id);
            this.btn_uds_info.Controls.Add(this.label5);
            this.btn_uds_info.Controls.Add(this.btn_send_pass_safe);
            this.btn_uds_info.Controls.Add(this.label3);
            this.btn_uds_info.Controls.Add(this.btn_load_dll);
            this.btn_uds_info.Controls.Add(this.tb_uds_msg_data);
            this.btn_uds_info.Controls.Add(this.cbb_safe_level);
            this.btn_uds_info.Controls.Add(this.btn_send_uds_msg);
            this.btn_uds_info.Location = new System.Drawing.Point(4, 31);
            this.btn_uds_info.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.btn_uds_info.Name = "btn_uds_info";
            this.btn_uds_info.Padding = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.btn_uds_info.Size = new System.Drawing.Size(1293, 313);
            this.btn_uds_info.TabIndex = 2;
            this.btn_uds_info.Text = "UDS";
            this.btn_uds_info.UseVisualStyleBackColor = true;
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.Location = new System.Drawing.Point(244, 47);
            this.label10.Margin = new System.Windows.Forms.Padding(6, 0, 6, 0);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(94, 21);
            this.label10.TabIndex = 19;
            this.label10.Text = "字节长度";
            // 
            // cbb_dlc
            // 
            this.cbb_dlc.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cbb_dlc.FormattingEnabled = true;
            this.cbb_dlc.Items.AddRange(new object[] {
            "8   (08)",
            "9   (12)",
            "10 (16)",
            "11 (20)",
            "12 (24) ",
            "13 (32)",
            "14 (48)",
            "15 (64)"});
            this.cbb_dlc.Location = new System.Drawing.Point(352, 44);
            this.cbb_dlc.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.cbb_dlc.Name = "cbb_dlc";
            this.cbb_dlc.Size = new System.Drawing.Size(132, 29);
            this.cbb_dlc.TabIndex = 18;
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Location = new System.Drawing.Point(1206, 47);
            this.label9.Margin = new System.Windows.Forms.Padding(6, 0, 6, 0);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(94, 21);
            this.label9.TabIndex = 17;
            this.label9.Text = "数据类型";
            // 
            // cbb_datatype
            // 
            this.cbb_datatype.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cbb_datatype.FormattingEnabled = true;
            this.cbb_datatype.Items.AddRange(new object[] {
            "数据帧",
            "扩展帧"});
            this.cbb_datatype.Location = new System.Drawing.Point(1314, 40);
            this.cbb_datatype.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.cbb_datatype.Name = "cbb_datatype";
            this.cbb_datatype.Size = new System.Drawing.Size(118, 29);
            this.cbb_datatype.TabIndex = 16;
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(4, 47);
            this.label8.Margin = new System.Windows.Forms.Padding(6, 0, 6, 0);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(94, 21);
            this.label8.TabIndex = 15;
            this.label8.Text = "报文类型";
            // 
            // cbb_msgtype
            // 
            this.cbb_msgtype.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cbb_msgtype.FormattingEnabled = true;
            this.cbb_msgtype.Items.AddRange(new object[] {
            "CAN",
            "CANFD"});
            this.cbb_msgtype.Location = new System.Drawing.Point(112, 42);
            this.cbb_msgtype.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.cbb_msgtype.Name = "cbb_msgtype";
            this.cbb_msgtype.Size = new System.Drawing.Size(118, 29);
            this.cbb_msgtype.TabIndex = 14;
            // 
            // btn_uds_id
            // 
            this.btn_uds_id.Location = new System.Drawing.Point(1443, 38);
            this.btn_uds_id.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.btn_uds_id.Name = "btn_uds_id";
            this.btn_uds_id.Size = new System.Drawing.Size(138, 40);
            this.btn_uds_id.TabIndex = 13;
            this.btn_uds_id.Text = "确认";
            this.btn_uds_id.UseVisualStyleBackColor = true;
            this.btn_uds_id.Click += new System.EventHandler(this.btn_uds_id_Click);
            // 
            // tb_function_id
            // 
            this.tb_function_id.Location = new System.Drawing.Point(1071, 42);
            this.tb_function_id.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.tb_function_id.Name = "tb_function_id";
            this.tb_function_id.Size = new System.Drawing.Size(121, 31);
            this.tb_function_id.TabIndex = 12;
            this.tb_function_id.Text = "0x789";
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(952, 47);
            this.label7.Margin = new System.Windows.Forms.Padding(6, 0, 6, 0);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(120, 21);
            this.label7.TabIndex = 11;
            this.label7.Text = "functionID";
            // 
            // tb_respond_id
            // 
            this.tb_respond_id.Location = new System.Drawing.Point(842, 42);
            this.tb_respond_id.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.tb_respond_id.Name = "tb_respond_id";
            this.tb_respond_id.Size = new System.Drawing.Size(105, 31);
            this.tb_respond_id.TabIndex = 10;
            this.tb_respond_id.Text = "0x456";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(722, 47);
            this.label6.Margin = new System.Windows.Forms.Padding(6, 0, 6, 0);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(109, 21);
            this.label6.TabIndex = 9;
            this.label6.Text = "respondID";
            // 
            // tb_request_id
            // 
            this.tb_request_id.Location = new System.Drawing.Point(618, 42);
            this.tb_request_id.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.tb_request_id.Name = "tb_request_id";
            this.tb_request_id.Size = new System.Drawing.Size(90, 31);
            this.tb_request_id.TabIndex = 8;
            this.tb_request_id.Text = "0x123";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(499, 47);
            this.label5.Margin = new System.Windows.Forms.Padding(6, 0, 6, 0);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(109, 21);
            this.label5.TabIndex = 7;
            this.label5.Text = "requestID";
            // 
            // btn_send_pass_safe
            // 
            this.btn_send_pass_safe.Location = new System.Drawing.Point(1093, 108);
            this.btn_send_pass_safe.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.btn_send_pass_safe.Name = "btn_send_pass_safe";
            this.btn_send_pass_safe.Size = new System.Drawing.Size(138, 40);
            this.btn_send_pass_safe.TabIndex = 6;
            this.btn_send_pass_safe.Text = "确认";
            this.btn_send_pass_safe.UseVisualStyleBackColor = true;
            this.btn_send_pass_safe.Click += new System.EventHandler(this.button4_Click);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(708, 116);
            this.label3.Margin = new System.Windows.Forms.Padding(6, 0, 6, 0);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(136, 21);
            this.label3.TabIndex = 5;
            this.label3.Text = "安全访问等级";
            // 
            // btn_load_dll
            // 
            this.btn_load_dll.Location = new System.Drawing.Point(1591, 10);
            this.btn_load_dll.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.btn_load_dll.Name = "btn_load_dll";
            this.btn_load_dll.Size = new System.Drawing.Size(165, 98);
            this.btn_load_dll.TabIndex = 3;
            this.btn_load_dll.Text = "载入seed&key.dll";
            this.btn_load_dll.UseVisualStyleBackColor = true;
            this.btn_load_dll.Click += new System.EventHandler(this.btn_load_dll_Click);
            // 
            // tb_uds_msg_data
            // 
            this.tb_uds_msg_data.Location = new System.Drawing.Point(7, 107);
            this.tb_uds_msg_data.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.tb_uds_msg_data.Name = "tb_uds_msg_data";
            this.tb_uds_msg_data.Size = new System.Drawing.Size(538, 31);
            this.tb_uds_msg_data.TabIndex = 2;
            this.tb_uds_msg_data.Text = "10 02";
            // 
            // cbb_safe_level
            // 
            this.cbb_safe_level.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cbb_safe_level.FormattingEnabled = true;
            this.cbb_safe_level.Location = new System.Drawing.Point(860, 108);
            this.cbb_safe_level.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.cbb_safe_level.Name = "cbb_safe_level";
            this.cbb_safe_level.Size = new System.Drawing.Size(218, 29);
            this.cbb_safe_level.TabIndex = 1;
            // 
            // btn_send_uds_msg
            // 
            this.btn_send_uds_msg.Location = new System.Drawing.Point(559, 107);
            this.btn_send_uds_msg.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.btn_send_uds_msg.Name = "btn_send_uds_msg";
            this.btn_send_uds_msg.Size = new System.Drawing.Size(138, 40);
            this.btn_send_uds_msg.TabIndex = 0;
            this.btn_send_uds_msg.Text = "发送";
            this.btn_send_uds_msg.UseVisualStyleBackColor = true;
            this.btn_send_uds_msg.Click += new System.EventHandler(this.btn_send_uds_msg_Click);
            // 
            // tabPage3
            // 
            this.tabPage3.Controls.Add(this.btn_set_signal_value);
            this.tabPage3.Controls.Add(this.btn_get_signal_value);
            this.tabPage3.Controls.Add(this.tb_read_write);
            this.tabPage3.Controls.Add(this.lb_ASignaladdress);
            this.tabPage3.Controls.Add(this.tv_rbs);
            this.tabPage3.Location = new System.Drawing.Point(4, 31);
            this.tabPage3.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.tabPage3.Name = "tabPage3";
            this.tabPage3.Padding = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.tabPage3.Size = new System.Drawing.Size(1293, 313);
            this.tabPage3.TabIndex = 3;
            this.tabPage3.Text = "RBS";
            this.tabPage3.UseVisualStyleBackColor = true;
            // 
            // btn_set_signal_value
            // 
            this.btn_set_signal_value.Location = new System.Drawing.Point(843, 93);
            this.btn_set_signal_value.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.btn_set_signal_value.Name = "btn_set_signal_value";
            this.btn_set_signal_value.Size = new System.Drawing.Size(138, 40);
            this.btn_set_signal_value.TabIndex = 4;
            this.btn_set_signal_value.Text = "set_value";
            this.btn_set_signal_value.UseVisualStyleBackColor = true;
            this.btn_set_signal_value.Click += new System.EventHandler(this.btn_set_signal_value_Click);
            // 
            // btn_get_signal_value
            // 
            this.btn_get_signal_value.Location = new System.Drawing.Point(992, 93);
            this.btn_get_signal_value.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.btn_get_signal_value.Name = "btn_get_signal_value";
            this.btn_get_signal_value.Size = new System.Drawing.Size(138, 40);
            this.btn_get_signal_value.TabIndex = 3;
            this.btn_get_signal_value.Text = "get_value";
            this.btn_get_signal_value.UseVisualStyleBackColor = true;
            this.btn_get_signal_value.Click += new System.EventHandler(this.btn_get_signal_value_Click);
            // 
            // tb_read_write
            // 
            this.tb_read_write.Location = new System.Drawing.Point(669, 96);
            this.tb_read_write.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.tb_read_write.Name = "tb_read_write";
            this.tb_read_write.Size = new System.Drawing.Size(160, 31);
            this.tb_read_write.TabIndex = 2;
            // 
            // lb_ASignaladdress
            // 
            this.lb_ASignaladdress.AutoSize = true;
            this.lb_ASignaladdress.Font = new System.Drawing.Font("宋体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.lb_ASignaladdress.Location = new System.Drawing.Point(667, 28);
            this.lb_ASignaladdress.Margin = new System.Windows.Forms.Padding(6, 0, 6, 0);
            this.lb_ASignaladdress.Name = "lb_ASignaladdress";
            this.lb_ASignaladdress.Size = new System.Drawing.Size(0, 28);
            this.lb_ASignaladdress.TabIndex = 1;
            // 
            // tv_rbs
            // 
            this.tv_rbs.ContextMenuStrip = this.contextMenuStrip1;
            this.tv_rbs.Dock = System.Windows.Forms.DockStyle.Left;
            this.tv_rbs.Location = new System.Drawing.Point(6, 5);
            this.tv_rbs.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.tv_rbs.Name = "tv_rbs";
            this.tv_rbs.Size = new System.Drawing.Size(648, 303);
            this.tv_rbs.TabIndex = 0;
            this.tv_rbs.AfterCheck += new System.Windows.Forms.TreeViewEventHandler(this.tv_rbs_AfterCheck);
            this.tv_rbs.Click += new System.EventHandler(this.tv_rbs_Click);
            this.tv_rbs.DoubleClick += new System.EventHandler(this.tv_rbs_DoubleClick);
            // 
            // contextMenuStrip1
            // 
            this.contextMenuStrip1.ImageScalingSize = new System.Drawing.Size(28, 28);
            this.contextMenuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.tm_all_select,
            this.tm_all_not_select});
            this.contextMenuStrip1.Name = "contextMenuStrip1";
            this.contextMenuStrip1.Size = new System.Drawing.Size(169, 72);
            // 
            // tm_all_select
            // 
            this.tm_all_select.Name = "tm_all_select";
            this.tm_all_select.Size = new System.Drawing.Size(168, 34);
            this.tm_all_select.Text = "全选";
            this.tm_all_select.Click += new System.EventHandler(this.tm_all_select_Click);
            // 
            // tm_all_not_select
            // 
            this.tm_all_not_select.Name = "tm_all_not_select";
            this.tm_all_not_select.Size = new System.Drawing.Size(168, 34);
            this.tm_all_not_select.Text = "取消全选";
            this.tm_all_not_select.Click += new System.EventHandler(this.tm_all_not_select_Click);
            // 
            // lv_showmsg
            // 
            this.lv_showmsg.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.columnHeader6,
            this.columnHeader8,
            this.columnHeader1,
            this.columnHeader2,
            this.columnHeader3,
            this.columnHeader7,
            this.columnHeader4,
            this.columnHeader5});
            this.lv_showmsg.Dock = System.Windows.Forms.DockStyle.Fill;
            this.lv_showmsg.FullRowSelect = true;
            this.lv_showmsg.GridLines = true;
            this.lv_showmsg.HideSelection = false;
            this.lv_showmsg.Location = new System.Drawing.Point(6, 29);
            this.lv_showmsg.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.lv_showmsg.Name = "lv_showmsg";
            this.lv_showmsg.Size = new System.Drawing.Size(1642, 494);
            this.lv_showmsg.TabIndex = 0;
            this.lv_showmsg.UseCompatibleStateImageBehavior = false;
            this.lv_showmsg.View = System.Windows.Forms.View.Details;
            // 
            // columnHeader6
            // 
            this.columnHeader6.Text = "msg_times";
            this.columnHeader6.Width = 110;
            // 
            // columnHeader8
            // 
            this.columnHeader8.Text = "chn";
            // 
            // columnHeader1
            // 
            this.columnHeader1.Text = "Type";
            // 
            // columnHeader2
            // 
            this.columnHeader2.Text = "time";
            // 
            // columnHeader3
            // 
            this.columnHeader3.Text = "id";
            // 
            // columnHeader7
            // 
            this.columnHeader7.Text = "dir";
            this.columnHeader7.Width = 30;
            // 
            // columnHeader4
            // 
            this.columnHeader4.Text = "dlc";
            // 
            // columnHeader5
            // 
            this.columnHeader5.Text = "FData";
            this.columnHeader5.Width = 477;
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.pictureBox1);
            this.groupBox1.Controls.Add(this.lv_showmsg);
            this.groupBox1.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.groupBox1.Location = new System.Drawing.Point(0, 382);
            this.groupBox1.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Padding = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.groupBox1.Size = new System.Drawing.Size(1654, 528);
            this.groupBox1.TabIndex = 5;
            this.groupBox1.TabStop = false;
            // 
            // pictureBox1
            // 
            this.pictureBox1.Image = ((System.Drawing.Image)(resources.GetObject("pictureBox1.Image")));
            this.pictureBox1.Location = new System.Drawing.Point(1612, 396);
            this.pictureBox1.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(170, 122);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictureBox1.TabIndex = 20;
            this.pictureBox1.TabStop = false;
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.panel2);
            this.groupBox2.Controls.Add(this.panel1);
            this.groupBox2.Dock = System.Windows.Forms.DockStyle.Fill;
            this.groupBox2.Location = new System.Drawing.Point(0, 0);
            this.groupBox2.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Padding = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.groupBox2.Size = new System.Drawing.Size(1654, 382);
            this.groupBox2.TabIndex = 6;
            this.groupBox2.TabStop = false;
            // 
            // panel2
            // 
            this.panel2.Controls.Add(this.tabControl1);
            this.panel2.Dock = System.Windows.Forms.DockStyle.Fill;
            this.panel2.Location = new System.Drawing.Point(6, 29);
            this.panel2.Name = "panel2";
            this.panel2.Size = new System.Drawing.Size(1301, 348);
            this.panel2.TabIndex = 1;
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.textBox1);
            this.panel1.Dock = System.Windows.Forms.DockStyle.Right;
            this.panel1.Location = new System.Drawing.Point(1307, 29);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(341, 348);
            this.panel1.TabIndex = 0;
            // 
            // textBox1
            // 
            this.textBox1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.textBox1.Location = new System.Drawing.Point(0, 0);
            this.textBox1.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.textBox1.Multiline = true;
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(341, 348);
            this.textBox1.TabIndex = 20;
            // 
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick_1);
            // 
            // TSMaster_CAN_Form
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(11F, 21F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1654, 910);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.Name = "TSMaster_CAN_Form";
            this.Text = "TSMaster_CAN";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.TSMaster_CAN_Form_FormClosing);
            this.Load += new System.EventHandler(this.TSMaster_CAN_Form_Load);
            this.Resize += new System.EventHandler(this.TSMaster_CAN_Form_Resize);
            this.tabControl1.ResumeLayout(false);
            this.tabPage1.ResumeLayout(false);
            this.tabPage1.PerformLayout();
            this.panle.ResumeLayout(false);
            this.panle.PerformLayout();
            this.tabPage2.ResumeLayout(false);
            this.btn_uds_info.ResumeLayout(false);
            this.btn_uds_info.PerformLayout();
            this.tabPage3.ResumeLayout(false);
            this.tabPage3.PerformLayout();
            this.contextMenuStrip1.ResumeLayout(false);
            this.groupBox1.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.groupBox2.ResumeLayout(false);
            this.panel2.ResumeLayout(false);
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btn_hw_config;
        private System.Windows.Forms.Button btn_show_hw;
        private System.Windows.Forms.Button btn_on_off;
        private System.Windows.Forms.Button btn_load_candb;
        private System.Windows.Forms.TabControl tabControl1;
        private System.Windows.Forms.TabPage tabPage1;
        private System.Windows.Forms.TabPage tabPage2;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.ListView lv_showmsg;
        private System.Windows.Forms.ColumnHeader columnHeader1;
        private System.Windows.Forms.ColumnHeader columnHeader2;
        private System.Windows.Forms.ColumnHeader columnHeader3;
        private System.Windows.Forms.ColumnHeader columnHeader4;
        private System.Windows.Forms.ColumnHeader columnHeader5;
        private System.Windows.Forms.ColumnHeader columnHeader6;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.ColumnHeader columnHeader7;
        private System.Windows.Forms.Button btn_cyclic_msg;
        private System.Windows.Forms.Button btn_send_one_msg;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.ComboBox cbb_signals;
        private System.Windows.Forms.ComboBox cbb_msg_names;
        private System.Windows.Forms.TextBox tb_signal_value;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Button btn_send_signal;
        private System.Windows.Forms.Button btn_stop_signal;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.TabPage btn_uds_info;
        private System.Windows.Forms.Button btn_load_dll;
        private System.Windows.Forms.TextBox tb_uds_msg_data;
        private System.Windows.Forms.ComboBox cbb_safe_level;
        private System.Windows.Forms.Button btn_send_uds_msg;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Button btn_send_pass_safe;
        private System.Windows.Forms.Button btn_uds_id;
        private System.Windows.Forms.TextBox tb_function_id;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.TextBox tb_respond_id;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.TextBox tb_request_id;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.ComboBox cbb_msgtype;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.ComboBox cbb_datatype;
        private System.Windows.Forms.Label label10;
        private System.Windows.Forms.ComboBox cbb_dlc;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.TabPage tabPage3;
        private System.Windows.Forms.TreeView tv_rbs;
        private System.Windows.Forms.ColumnHeader columnHeader8;
        private System.Windows.Forms.ContextMenuStrip contextMenuStrip1;
        private System.Windows.Forms.ToolStripMenuItem tm_all_select;
        private System.Windows.Forms.ToolStripMenuItem tm_all_not_select;
        private System.Windows.Forms.Label lb_ASignaladdress;
        private System.Windows.Forms.Button btn_set_signal_value;
        private System.Windows.Forms.Button btn_get_signal_value;
        private System.Windows.Forms.TextBox tb_read_write;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.Panel panle;
        private System.Windows.Forms.Button btn_pilter;
        private System.Windows.Forms.Label label13;
        private System.Windows.Forms.TextBox tb_channel_pass;
        private System.Windows.Forms.Label label14;
        private System.Windows.Forms.Label label15;
        private System.Windows.Forms.TextBox tb_id_pass;
        private System.Windows.Forms.Panel panel2;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.TextBox textBox1;
    }
}

