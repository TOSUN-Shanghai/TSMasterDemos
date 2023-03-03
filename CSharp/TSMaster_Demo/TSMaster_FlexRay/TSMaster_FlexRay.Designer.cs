namespace TSMaster_FlexRay
{
    partial class TSMaster_FlexRay
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(TSMaster_FlexRay));
            this.btn_loadproject = new System.Windows.Forms.Button();
            this.btn_on_off = new System.Windows.Forms.Button();
            this.tabControl1 = new System.Windows.Forms.TabControl();
            this.tabPage1 = new System.Windows.Forms.TabPage();
            this.btn_hwconfig = new System.Windows.Forms.Button();
            this.Channle_Mask = new System.Windows.Forms.Label();
            this.tb_Mask = new System.Windows.Forms.TextBox();
            this.label11 = new System.Windows.Forms.Label();
            this.tb_chn = new System.Windows.Forms.TextBox();
            this.btn_clear_msg = new System.Windows.Forms.Button();
            this.panle = new System.Windows.Forms.Panel();
            this.btn_pilter = new System.Windows.Forms.Button();
            this.label9 = new System.Windows.Forms.Label();
            this.tb_rc_pass = new System.Windows.Forms.TextBox();
            this.label10 = new System.Windows.Forms.Label();
            this.tb_bc_pass = new System.Windows.Forms.TextBox();
            this.label8 = new System.Windows.Forms.Label();
            this.tb_channel_pass = new System.Windows.Forms.TextBox();
            this.label7 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.tb_id_pass = new System.Windows.Forms.TextBox();
            this.tb_send_flexray = new System.Windows.Forms.Button();
            this.label5 = new System.Windows.Forms.Label();
            this.tb_dlc = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.tb_data = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.tb_rc = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.tb_bc = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.tb_slotid = new System.Windows.Forms.TextBox();
            this.tabPage2 = new System.Windows.Forms.TabPage();
            this.btn_get_signal_value = new System.Windows.Forms.Button();
            this.tb_read_write = new System.Windows.Forms.TextBox();
            this.btn_set_signal_value = new System.Windows.Forms.Button();
            this.lb_ASignaladdress = new System.Windows.Forms.Label();
            this.tv_rbs = new System.Windows.Forms.TreeView();
            this.contextMenuStrip1 = new System.Windows.Forms.ContextMenuStrip(this.components);
            this.tm_all_select = new System.Windows.Forms.ToolStripMenuItem();
            this.tm_all_not_select = new System.Windows.Forms.ToolStripMenuItem();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.panel3 = new System.Windows.Forms.Panel();
            this.panel1 = new System.Windows.Forms.Panel();
            this.panel2 = new System.Windows.Forms.Panel();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.tb_msg = new System.Windows.Forms.TextBox();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.lv_showmsg = new System.Windows.Forms.ListView();
            this.columnHeader6 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader8 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader2 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader3 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader1 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader7 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader4 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader5 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.tabControl1.SuspendLayout();
            this.tabPage1.SuspendLayout();
            this.panle.SuspendLayout();
            this.tabPage2.SuspendLayout();
            this.contextMenuStrip1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.panel3.SuspendLayout();
            this.panel1.SuspendLayout();
            this.panel2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // btn_loadproject
            // 
            this.btn_loadproject.Location = new System.Drawing.Point(6, 6);
            this.btn_loadproject.Name = "btn_loadproject";
            this.btn_loadproject.Size = new System.Drawing.Size(75, 23);
            this.btn_loadproject.TabIndex = 0;
            this.btn_loadproject.Text = "加载工程";
            this.btn_loadproject.UseVisualStyleBackColor = true;
            this.btn_loadproject.Click += new System.EventHandler(this.btn_loadproject_Click);
            // 
            // btn_on_off
            // 
            this.btn_on_off.Location = new System.Drawing.Point(168, 7);
            this.btn_on_off.Name = "btn_on_off";
            this.btn_on_off.Size = new System.Drawing.Size(75, 23);
            this.btn_on_off.TabIndex = 1;
            this.btn_on_off.Text = "连接";
            this.btn_on_off.UseVisualStyleBackColor = true;
            this.btn_on_off.Click += new System.EventHandler(this.btn_on_off_Click);
            // 
            // tabControl1
            // 
            this.tabControl1.Controls.Add(this.tabPage1);
            this.tabControl1.Controls.Add(this.tabPage2);
            this.tabControl1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.tabControl1.Location = new System.Drawing.Point(0, 0);
            this.tabControl1.Name = "tabControl1";
            this.tabControl1.SelectedIndex = 0;
            this.tabControl1.Size = new System.Drawing.Size(834, 213);
            this.tabControl1.TabIndex = 2;
            // 
            // tabPage1
            // 
            this.tabPage1.Controls.Add(this.btn_hwconfig);
            this.tabPage1.Controls.Add(this.Channle_Mask);
            this.tabPage1.Controls.Add(this.tb_Mask);
            this.tabPage1.Controls.Add(this.label11);
            this.tabPage1.Controls.Add(this.tb_chn);
            this.tabPage1.Controls.Add(this.btn_clear_msg);
            this.tabPage1.Controls.Add(this.panle);
            this.tabPage1.Controls.Add(this.tb_send_flexray);
            this.tabPage1.Controls.Add(this.label5);
            this.tabPage1.Controls.Add(this.tb_dlc);
            this.tabPage1.Controls.Add(this.label4);
            this.tabPage1.Controls.Add(this.tb_data);
            this.tabPage1.Controls.Add(this.label3);
            this.tabPage1.Controls.Add(this.tb_rc);
            this.tabPage1.Controls.Add(this.label2);
            this.tabPage1.Controls.Add(this.tb_bc);
            this.tabPage1.Controls.Add(this.label1);
            this.tabPage1.Controls.Add(this.tb_slotid);
            this.tabPage1.Controls.Add(this.btn_loadproject);
            this.tabPage1.Controls.Add(this.btn_on_off);
            this.tabPage1.Location = new System.Drawing.Point(4, 22);
            this.tabPage1.Name = "tabPage1";
            this.tabPage1.Padding = new System.Windows.Forms.Padding(3);
            this.tabPage1.Size = new System.Drawing.Size(826, 187);
            this.tabPage1.TabIndex = 0;
            this.tabPage1.Text = "主界面";
            this.tabPage1.UseVisualStyleBackColor = true;
            // 
            // btn_hwconfig
            // 
            this.btn_hwconfig.Location = new System.Drawing.Point(87, 6);
            this.btn_hwconfig.Name = "btn_hwconfig";
            this.btn_hwconfig.Size = new System.Drawing.Size(75, 23);
            this.btn_hwconfig.TabIndex = 19;
            this.btn_hwconfig.Text = "硬件配置";
            this.btn_hwconfig.UseVisualStyleBackColor = true;
            this.btn_hwconfig.Click += new System.EventHandler(this.btn_hwconfig_Click);
            // 
            // Channle_Mask
            // 
            this.Channle_Mask.AutoSize = true;
            this.Channle_Mask.Location = new System.Drawing.Point(108, 65);
            this.Channle_Mask.Name = "Channle_Mask";
            this.Channle_Mask.Size = new System.Drawing.Size(77, 12);
            this.Channle_Mask.TabIndex = 18;
            this.Channle_Mask.Text = "Channle_Mask";
            // 
            // tb_Mask
            // 
            this.tb_Mask.Location = new System.Drawing.Point(191, 62);
            this.tb_Mask.Name = "tb_Mask";
            this.tb_Mask.Size = new System.Drawing.Size(49, 21);
            this.tb_Mask.TabIndex = 17;
            // 
            // label11
            // 
            this.label11.AutoSize = true;
            this.label11.Location = new System.Drawing.Point(3, 65);
            this.label11.Name = "label11";
            this.label11.Size = new System.Drawing.Size(41, 12);
            this.label11.TabIndex = 16;
            this.label11.Text = "Chnnal";
            // 
            // tb_chn
            // 
            this.tb_chn.Location = new System.Drawing.Point(50, 62);
            this.tb_chn.Name = "tb_chn";
            this.tb_chn.Size = new System.Drawing.Size(49, 21);
            this.tb_chn.TabIndex = 15;
            // 
            // btn_clear_msg
            // 
            this.btn_clear_msg.Location = new System.Drawing.Point(248, 7);
            this.btn_clear_msg.Name = "btn_clear_msg";
            this.btn_clear_msg.Size = new System.Drawing.Size(88, 23);
            this.btn_clear_msg.TabIndex = 14;
            this.btn_clear_msg.Text = "清除报文信息";
            this.btn_clear_msg.UseVisualStyleBackColor = true;
            this.btn_clear_msg.Click += new System.EventHandler(this.btn_clear_msg_Click);
            // 
            // panle
            // 
            this.panle.Controls.Add(this.btn_pilter);
            this.panle.Controls.Add(this.label9);
            this.panle.Controls.Add(this.tb_rc_pass);
            this.panle.Controls.Add(this.label10);
            this.panle.Controls.Add(this.tb_bc_pass);
            this.panle.Controls.Add(this.label8);
            this.panle.Controls.Add(this.tb_channel_pass);
            this.panle.Controls.Add(this.label7);
            this.panle.Controls.Add(this.label6);
            this.panle.Controls.Add(this.tb_id_pass);
            this.panle.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.panle.Location = new System.Drawing.Point(3, 149);
            this.panle.Name = "panle";
            this.panle.Size = new System.Drawing.Size(820, 35);
            this.panle.TabIndex = 13;
            // 
            // btn_pilter
            // 
            this.btn_pilter.Location = new System.Drawing.Point(586, 9);
            this.btn_pilter.Name = "btn_pilter";
            this.btn_pilter.Size = new System.Drawing.Size(75, 23);
            this.btn_pilter.TabIndex = 13;
            this.btn_pilter.Text = "确定";
            this.btn_pilter.UseVisualStyleBackColor = true;
            this.btn_pilter.Click += new System.EventHandler(this.btn_pilter_Click);
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Location = new System.Drawing.Point(459, 14);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(59, 12);
            this.label9.TabIndex = 12;
            this.label9.Text = "rep_cycle";
            // 
            // tb_rc_pass
            // 
            this.tb_rc_pass.Location = new System.Drawing.Point(524, 11);
            this.tb_rc_pass.Name = "tb_rc_pass";
            this.tb_rc_pass.Size = new System.Drawing.Size(44, 21);
            this.tb_rc_pass.TabIndex = 11;
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.Location = new System.Drawing.Point(334, 14);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(65, 12);
            this.label10.TabIndex = 10;
            this.label10.Text = "base_cycle";
            // 
            // tb_bc_pass
            // 
            this.tb_bc_pass.Location = new System.Drawing.Point(405, 11);
            this.tb_bc_pass.Name = "tb_bc_pass";
            this.tb_bc_pass.Size = new System.Drawing.Size(48, 21);
            this.tb_bc_pass.TabIndex = 9;
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(115, 14);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(41, 12);
            this.label8.TabIndex = 8;
            this.label8.Text = "Chnnal";
            // 
            // tb_channel_pass
            // 
            this.tb_channel_pass.Location = new System.Drawing.Point(162, 11);
            this.tb_channel_pass.Name = "tb_channel_pass";
            this.tb_channel_pass.Size = new System.Drawing.Size(49, 21);
            this.tb_channel_pass.TabIndex = 7;
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(3, 14);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(101, 12);
            this.label7.TabIndex = 6;
            this.label7.Text = "过滤条件（pass）";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(232, 14);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(41, 12);
            this.label6.TabIndex = 5;
            this.label6.Text = "SlotID";
            // 
            // tb_id_pass
            // 
            this.tb_id_pass.Location = new System.Drawing.Point(279, 11);
            this.tb_id_pass.Name = "tb_id_pass";
            this.tb_id_pass.Size = new System.Drawing.Size(49, 21);
            this.tb_id_pass.TabIndex = 4;
            // 
            // tb_send_flexray
            // 
            this.tb_send_flexray.Location = new System.Drawing.Point(699, 89);
            this.tb_send_flexray.Name = "tb_send_flexray";
            this.tb_send_flexray.Size = new System.Drawing.Size(75, 23);
            this.tb_send_flexray.TabIndex = 12;
            this.tb_send_flexray.Text = "发送";
            this.tb_send_flexray.UseVisualStyleBackColor = true;
            this.tb_send_flexray.Click += new System.EventHandler(this.tb_send_flexray_Click);
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(593, 65);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(23, 12);
            this.label5.TabIndex = 11;
            this.label5.Text = "dlc";
            // 
            // tb_dlc
            // 
            this.tb_dlc.Location = new System.Drawing.Point(622, 62);
            this.tb_dlc.Name = "tb_dlc";
            this.tb_dlc.Size = new System.Drawing.Size(49, 21);
            this.tb_dlc.TabIndex = 10;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(6, 92);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(29, 12);
            this.label4.TabIndex = 9;
            this.label4.Text = "data";
            // 
            // tb_data
            // 
            this.tb_data.Location = new System.Drawing.Point(41, 89);
            this.tb_data.Name = "tb_data";
            this.tb_data.Size = new System.Drawing.Size(630, 21);
            this.tb_data.TabIndex = 8;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(475, 65);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(59, 12);
            this.label3.TabIndex = 7;
            this.label3.Text = "rep_cycle";
            // 
            // tb_rc
            // 
            this.tb_rc.Location = new System.Drawing.Point(540, 62);
            this.tb_rc.Name = "tb_rc";
            this.tb_rc.Size = new System.Drawing.Size(49, 21);
            this.tb_rc.TabIndex = 6;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(350, 65);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(65, 12);
            this.label2.TabIndex = 5;
            this.label2.Text = "base_cycle";
            // 
            // tb_bc
            // 
            this.tb_bc.Location = new System.Drawing.Point(421, 62);
            this.tb_bc.Name = "tb_bc";
            this.tb_bc.Size = new System.Drawing.Size(49, 21);
            this.tb_bc.TabIndex = 4;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(246, 65);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(41, 12);
            this.label1.TabIndex = 3;
            this.label1.Text = "SlotID";
            // 
            // tb_slotid
            // 
            this.tb_slotid.Location = new System.Drawing.Point(293, 62);
            this.tb_slotid.Name = "tb_slotid";
            this.tb_slotid.Size = new System.Drawing.Size(49, 21);
            this.tb_slotid.TabIndex = 2;
            // 
            // tabPage2
            // 
            this.tabPage2.Controls.Add(this.btn_get_signal_value);
            this.tabPage2.Controls.Add(this.tb_read_write);
            this.tabPage2.Controls.Add(this.btn_set_signal_value);
            this.tabPage2.Controls.Add(this.lb_ASignaladdress);
            this.tabPage2.Controls.Add(this.tv_rbs);
            this.tabPage2.Location = new System.Drawing.Point(4, 22);
            this.tabPage2.Name = "tabPage2";
            this.tabPage2.Padding = new System.Windows.Forms.Padding(3);
            this.tabPage2.Size = new System.Drawing.Size(826, 187);
            this.tabPage2.TabIndex = 1;
            this.tabPage2.Text = "RBS";
            this.tabPage2.UseVisualStyleBackColor = true;
            // 
            // btn_get_signal_value
            // 
            this.btn_get_signal_value.Location = new System.Drawing.Point(489, 60);
            this.btn_get_signal_value.Name = "btn_get_signal_value";
            this.btn_get_signal_value.Size = new System.Drawing.Size(75, 23);
            this.btn_get_signal_value.TabIndex = 4;
            this.btn_get_signal_value.Text = "get_value";
            this.btn_get_signal_value.UseVisualStyleBackColor = true;
            this.btn_get_signal_value.Click += new System.EventHandler(this.btn_get_signal_value_Click);
            // 
            // tb_read_write
            // 
            this.tb_read_write.Location = new System.Drawing.Point(300, 60);
            this.tb_read_write.Name = "tb_read_write";
            this.tb_read_write.Size = new System.Drawing.Size(100, 21);
            this.tb_read_write.TabIndex = 3;
            // 
            // btn_set_signal_value
            // 
            this.btn_set_signal_value.Location = new System.Drawing.Point(408, 60);
            this.btn_set_signal_value.Name = "btn_set_signal_value";
            this.btn_set_signal_value.Size = new System.Drawing.Size(75, 23);
            this.btn_set_signal_value.TabIndex = 2;
            this.btn_set_signal_value.Text = "set_value";
            this.btn_set_signal_value.UseVisualStyleBackColor = true;
            this.btn_set_signal_value.Click += new System.EventHandler(this.btn_set_signal_value_Click);
            // 
            // lb_ASignaladdress
            // 
            this.lb_ASignaladdress.AutoSize = true;
            this.lb_ASignaladdress.Font = new System.Drawing.Font("宋体", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.lb_ASignaladdress.Location = new System.Drawing.Point(300, 13);
            this.lb_ASignaladdress.Name = "lb_ASignaladdress";
            this.lb_ASignaladdress.Size = new System.Drawing.Size(0, 12);
            this.lb_ASignaladdress.TabIndex = 1;
            // 
            // tv_rbs
            // 
            this.tv_rbs.ContextMenuStrip = this.contextMenuStrip1;
            this.tv_rbs.Dock = System.Windows.Forms.DockStyle.Left;
            this.tv_rbs.Location = new System.Drawing.Point(3, 3);
            this.tv_rbs.Name = "tv_rbs";
            this.tv_rbs.Size = new System.Drawing.Size(291, 181);
            this.tv_rbs.TabIndex = 0;
            this.tv_rbs.AfterCheck += new System.Windows.Forms.TreeViewEventHandler(this.tv_rbs_AfterCheck);
            this.tv_rbs.DoubleClick += new System.EventHandler(this.tv_rbs_DoubleClick);
            // 
            // contextMenuStrip1
            // 
            this.contextMenuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.tm_all_select,
            this.tm_all_not_select});
            this.contextMenuStrip1.Name = "contextMenuStrip1";
            this.contextMenuStrip1.Size = new System.Drawing.Size(125, 48);
            // 
            // tm_all_select
            // 
            this.tm_all_select.Name = "tm_all_select";
            this.tm_all_select.Size = new System.Drawing.Size(124, 22);
            this.tm_all_select.Text = "全选";
            this.tm_all_select.Click += new System.EventHandler(this.tm_all_select_Click);
            // 
            // tm_all_not_select
            // 
            this.tm_all_not_select.Name = "tm_all_not_select";
            this.tm_all_not_select.Size = new System.Drawing.Size(124, 22);
            this.tm_all_not_select.Text = "取消全选";
            this.tm_all_not_select.Click += new System.EventHandler(this.tm_all_not_select_Click);
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.panel3);
            this.groupBox2.Controls.Add(this.panel1);
            this.groupBox2.Dock = System.Windows.Forms.DockStyle.Top;
            this.groupBox2.Location = new System.Drawing.Point(0, 0);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(1040, 233);
            this.groupBox2.TabIndex = 4;
            this.groupBox2.TabStop = false;
            // 
            // panel3
            // 
            this.panel3.Controls.Add(this.tabControl1);
            this.panel3.Dock = System.Windows.Forms.DockStyle.Fill;
            this.panel3.Location = new System.Drawing.Point(3, 17);
            this.panel3.Name = "panel3";
            this.panel3.Size = new System.Drawing.Size(834, 213);
            this.panel3.TabIndex = 4;
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.panel2);
            this.panel1.Dock = System.Windows.Forms.DockStyle.Right;
            this.panel1.Location = new System.Drawing.Point(837, 17);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(200, 213);
            this.panel1.TabIndex = 3;
            // 
            // panel2
            // 
            this.panel2.Controls.Add(this.pictureBox1);
            this.panel2.Controls.Add(this.tb_msg);
            this.panel2.Dock = System.Windows.Forms.DockStyle.Right;
            this.panel2.Location = new System.Drawing.Point(0, 0);
            this.panel2.Name = "panel2";
            this.panel2.Size = new System.Drawing.Size(200, 213);
            this.panel2.TabIndex = 4;
            // 
            // pictureBox1
            // 
            this.pictureBox1.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.pictureBox1.Image = ((System.Drawing.Image)(resources.GetObject("pictureBox1.Image")));
            this.pictureBox1.Location = new System.Drawing.Point(107, 139);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(93, 70);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictureBox1.TabIndex = 20;
            this.pictureBox1.TabStop = false;
            // 
            // tb_msg
            // 
            this.tb_msg.Dock = System.Windows.Forms.DockStyle.Fill;
            this.tb_msg.Location = new System.Drawing.Point(0, 0);
            this.tb_msg.Multiline = true;
            this.tb_msg.Name = "tb_msg";
            this.tb_msg.Size = new System.Drawing.Size(200, 213);
            this.tb_msg.TabIndex = 21;
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.lv_showmsg);
            this.groupBox1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.groupBox1.Location = new System.Drawing.Point(0, 233);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(1040, 385);
            this.groupBox1.TabIndex = 6;
            this.groupBox1.TabStop = false;
            // 
            // lv_showmsg
            // 
            this.lv_showmsg.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.columnHeader6,
            this.columnHeader8,
            this.columnHeader2,
            this.columnHeader3,
            this.columnHeader1,
            this.columnHeader7,
            this.columnHeader4,
            this.columnHeader5});
            this.lv_showmsg.Dock = System.Windows.Forms.DockStyle.Fill;
            this.lv_showmsg.FullRowSelect = true;
            this.lv_showmsg.GridLines = true;
            this.lv_showmsg.HideSelection = false;
            this.lv_showmsg.Location = new System.Drawing.Point(3, 17);
            this.lv_showmsg.Name = "lv_showmsg";
            this.lv_showmsg.Size = new System.Drawing.Size(1034, 365);
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
            // columnHeader2
            // 
            this.columnHeader2.Text = "time";
            // 
            // columnHeader3
            // 
            this.columnHeader3.Text = "id";
            // 
            // columnHeader1
            // 
            this.columnHeader1.Text = "cycle";
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
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // TSMaster_FlexRay
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1040, 618);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.groupBox2);
            this.Name = "TSMaster_FlexRay";
            this.Text = "Form1";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.TSMaster_FlexRay_FormClosing);
            this.Load += new System.EventHandler(this.TSMaster_FlexRay_Load);
            this.Resize += new System.EventHandler(this.TSMaster_FlexRay_Resize);
            this.tabControl1.ResumeLayout(false);
            this.tabPage1.ResumeLayout(false);
            this.tabPage1.PerformLayout();
            this.panle.ResumeLayout(false);
            this.panle.PerformLayout();
            this.tabPage2.ResumeLayout(false);
            this.tabPage2.PerformLayout();
            this.contextMenuStrip1.ResumeLayout(false);
            this.groupBox2.ResumeLayout(false);
            this.panel3.ResumeLayout(false);
            this.panel1.ResumeLayout(false);
            this.panel2.ResumeLayout(false);
            this.panel2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.groupBox1.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btn_loadproject;
        private System.Windows.Forms.Button btn_on_off;
        private System.Windows.Forms.TabControl tabControl1;
        private System.Windows.Forms.TabPage tabPage1;
        private System.Windows.Forms.TabPage tabPage2;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.ListView lv_showmsg;
        private System.Windows.Forms.ColumnHeader columnHeader6;
        private System.Windows.Forms.ColumnHeader columnHeader8;
        private System.Windows.Forms.ColumnHeader columnHeader1;
        private System.Windows.Forms.ColumnHeader columnHeader2;
        private System.Windows.Forms.ColumnHeader columnHeader3;
        private System.Windows.Forms.ColumnHeader columnHeader7;
        private System.Windows.Forms.ColumnHeader columnHeader4;
        private System.Windows.Forms.ColumnHeader columnHeader5;
        private System.Windows.Forms.Panel panel3;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Panel panel2;
        private System.Windows.Forms.TreeView tv_rbs;
        private System.Windows.Forms.Label lb_ASignaladdress;
        private System.Windows.Forms.Button btn_get_signal_value;
        private System.Windows.Forms.TextBox tb_read_write;
        private System.Windows.Forms.Button btn_set_signal_value;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.TextBox tb_msg;
        private System.Windows.Forms.ContextMenuStrip contextMenuStrip1;
        private System.Windows.Forms.ToolStripMenuItem tm_all_select;
        private System.Windows.Forms.ToolStripMenuItem tm_all_not_select;
        private System.Windows.Forms.Button tb_send_flexray;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.TextBox tb_dlc;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TextBox tb_data;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox tb_rc;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox tb_bc;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox tb_slotid;
        private System.Windows.Forms.Panel panle;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.TextBox tb_channel_pass;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.TextBox tb_id_pass;
        private System.Windows.Forms.Button btn_pilter;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.TextBox tb_rc_pass;
        private System.Windows.Forms.Label label10;
        private System.Windows.Forms.TextBox tb_bc_pass;
        private System.Windows.Forms.Button btn_clear_msg;
        private System.Windows.Forms.Label label11;
        private System.Windows.Forms.TextBox tb_chn;
        private System.Windows.Forms.Label Channle_Mask;
        private System.Windows.Forms.TextBox tb_Mask;
        private System.Windows.Forms.Button btn_hwconfig;
    }
}

