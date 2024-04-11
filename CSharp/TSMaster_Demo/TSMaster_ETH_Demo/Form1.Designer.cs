namespace TSMaster_ETH_Demo
{
    partial class Form1
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
            this.tabControl1 = new System.Windows.Forms.TabControl();
            this.tab_tcp = new System.Windows.Forms.TabPage();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.btn_tcpdefaultConfig = new System.Windows.Forms.Button();
            this.cb_client = new System.Windows.Forms.CheckBox();
            this.btn_ConnectServer = new System.Windows.Forms.Button();
            this.mask_NowIP = new System.Windows.Forms.MaskedTextBox();
            this.btn_CreateTCP = new System.Windows.Forms.Button();
            this.label6 = new System.Windows.Forms.Label();
            this.label8 = new System.Windows.Forms.Label();
            this.mask_NowPort = new System.Windows.Forms.MaskedTextBox();
            this.mask_connectPort = new System.Windows.Forms.MaskedTextBox();
            this.label7 = new System.Windows.Forms.Label();
            this.label9 = new System.Windows.Forms.Label();
            this.mask_connectIP = new System.Windows.Forms.MaskedTextBox();
            this.tab_udp = new System.Windows.Forms.TabPage();
            this.panel2 = new System.Windows.Forms.Panel();
            this.tb_statuMsgs = new System.Windows.Forms.TextBox();
            this.btn_removeDevices = new System.Windows.Forms.Button();
            this.btn_removeDevice = new System.Windows.Forms.Button();
            this.btn_defaultconfig = new System.Windows.Forms.Button();
            this.label5 = new System.Windows.Forms.Label();
            this.cmb_ETHChnlist = new System.Windows.Forms.ComboBox();
            this.label4 = new System.Windows.Forms.Label();
            this.mask_getway = new System.Windows.Forms.MaskedTextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.mask_net = new System.Windows.Forms.MaskedTextBox();
            this.mask_ip = new System.Windows.Forms.MaskedTextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.mask_macaddr = new System.Windows.Forms.MaskedTextBox();
            this.btn_addDev = new System.Windows.Forms.Button();
            this.btn_connect = new System.Windows.Forms.Button();
            this.btn_hwconfig = new System.Windows.Forms.Button();
            this.panel1 = new System.Windows.Forms.Panel();
            this.panel5 = new System.Windows.Forms.Panel();
            this.panel3 = new System.Windows.Forms.Panel();
            this.tv_ethList = new System.Windows.Forms.TreeView();
            this.tabControl1.SuspendLayout();
            this.tab_tcp.SuspendLayout();
            this.groupBox1.SuspendLayout();
            this.panel2.SuspendLayout();
            this.panel1.SuspendLayout();
            this.panel5.SuspendLayout();
            this.panel3.SuspendLayout();
            this.SuspendLayout();
            // 
            // tabControl1
            // 
            this.tabControl1.Controls.Add(this.tab_tcp);
            this.tabControl1.Controls.Add(this.tab_udp);
            this.tabControl1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.tabControl1.Location = new System.Drawing.Point(0, 0);
            this.tabControl1.Name = "tabControl1";
            this.tabControl1.SelectedIndex = 0;
            this.tabControl1.Size = new System.Drawing.Size(684, 333);
            this.tabControl1.TabIndex = 0;
            // 
            // tab_tcp
            // 
            this.tab_tcp.Controls.Add(this.groupBox1);
            this.tab_tcp.Location = new System.Drawing.Point(4, 22);
            this.tab_tcp.Name = "tab_tcp";
            this.tab_tcp.Padding = new System.Windows.Forms.Padding(3);
            this.tab_tcp.Size = new System.Drawing.Size(676, 307);
            this.tab_tcp.TabIndex = 0;
            this.tab_tcp.Text = "TCP";
            this.tab_tcp.UseVisualStyleBackColor = true;
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.btn_tcpdefaultConfig);
            this.groupBox1.Controls.Add(this.cb_client);
            this.groupBox1.Controls.Add(this.btn_ConnectServer);
            this.groupBox1.Controls.Add(this.mask_NowIP);
            this.groupBox1.Controls.Add(this.btn_CreateTCP);
            this.groupBox1.Controls.Add(this.label6);
            this.groupBox1.Controls.Add(this.label8);
            this.groupBox1.Controls.Add(this.mask_NowPort);
            this.groupBox1.Controls.Add(this.mask_connectPort);
            this.groupBox1.Controls.Add(this.label7);
            this.groupBox1.Controls.Add(this.label9);
            this.groupBox1.Controls.Add(this.mask_connectIP);
            this.groupBox1.Dock = System.Windows.Forms.DockStyle.Top;
            this.groupBox1.Location = new System.Drawing.Point(3, 3);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(670, 100);
            this.groupBox1.TabIndex = 24;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "tcp config";
            // 
            // btn_tcpdefaultConfig
            // 
            this.btn_tcpdefaultConfig.Location = new System.Drawing.Point(3, 44);
            this.btn_tcpdefaultConfig.Name = "btn_tcpdefaultConfig";
            this.btn_tcpdefaultConfig.Size = new System.Drawing.Size(99, 29);
            this.btn_tcpdefaultConfig.TabIndex = 24;
            this.btn_tcpdefaultConfig.Text = "default config";
            this.btn_tcpdefaultConfig.UseVisualStyleBackColor = true;
            this.btn_tcpdefaultConfig.Click += new System.EventHandler(this.btn_tcpdefaultConfig_Click);
            // 
            // cb_client
            // 
            this.cb_client.AutoSize = true;
            this.cb_client.Location = new System.Drawing.Point(11, 20);
            this.cb_client.Name = "cb_client";
            this.cb_client.Size = new System.Drawing.Size(72, 16);
            this.cb_client.TabIndex = 0;
            this.cb_client.Text = "IsServer";
            this.cb_client.UseVisualStyleBackColor = true;
            this.cb_client.CheckedChanged += new System.EventHandler(this.cb_client_CheckedChanged);
            // 
            // btn_ConnectServer
            // 
            this.btn_ConnectServer.Location = new System.Drawing.Point(475, 52);
            this.btn_ConnectServer.Name = "btn_ConnectServer";
            this.btn_ConnectServer.Size = new System.Drawing.Size(109, 23);
            this.btn_ConnectServer.TabIndex = 23;
            this.btn_ConnectServer.Text = "Connect Server";
            this.btn_ConnectServer.UseVisualStyleBackColor = true;
            this.btn_ConnectServer.Click += new System.EventHandler(this.btn_ConnectServer_Click);
            // 
            // mask_NowIP
            // 
            this.mask_NowIP.Location = new System.Drawing.Point(200, 22);
            this.mask_NowIP.Mask = "000.000.000.000";
            this.mask_NowIP.Name = "mask_NowIP";
            this.mask_NowIP.PromptChar = ' ';
            this.mask_NowIP.Size = new System.Drawing.Size(100, 21);
            this.mask_NowIP.TabIndex = 14;
            // 
            // btn_CreateTCP
            // 
            this.btn_CreateTCP.Location = new System.Drawing.Point(475, 27);
            this.btn_CreateTCP.Name = "btn_CreateTCP";
            this.btn_CreateTCP.Size = new System.Drawing.Size(109, 23);
            this.btn_CreateTCP.TabIndex = 22;
            this.btn_CreateTCP.Text = "Create TCP";
            this.btn_CreateTCP.UseVisualStyleBackColor = true;
            this.btn_CreateTCP.Click += new System.EventHandler(this.btn_CreateTCP_Click);
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(117, 27);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(59, 12);
            this.label6.TabIndex = 15;
            this.label6.Text = "Nowipaddr";
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(306, 55);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(71, 12);
            this.label8.TabIndex = 21;
            this.label8.Text = "ConnectPort";
            // 
            // mask_NowPort
            // 
            this.mask_NowPort.Location = new System.Drawing.Point(383, 24);
            this.mask_NowPort.Mask = "99999";
            this.mask_NowPort.Name = "mask_NowPort";
            this.mask_NowPort.PromptChar = ' ';
            this.mask_NowPort.Size = new System.Drawing.Size(76, 21);
            this.mask_NowPort.TabIndex = 16;
            this.mask_NowPort.ValidatingType = typeof(int);
            // 
            // mask_connectPort
            // 
            this.mask_connectPort.Enabled = false;
            this.mask_connectPort.Location = new System.Drawing.Point(383, 52);
            this.mask_connectPort.Mask = "99999";
            this.mask_connectPort.Name = "mask_connectPort";
            this.mask_connectPort.PromptChar = ' ';
            this.mask_connectPort.Size = new System.Drawing.Size(76, 21);
            this.mask_connectPort.TabIndex = 20;
            this.mask_connectPort.ValidatingType = typeof(int);
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(306, 27);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(47, 12);
            this.label7.TabIndex = 17;
            this.label7.Text = "NowPort";
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Location = new System.Drawing.Point(111, 55);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(83, 12);
            this.label9.TabIndex = 19;
            this.label9.Text = "Connectipaddr";
            // 
            // mask_connectIP
            // 
            this.mask_connectIP.Enabled = false;
            this.mask_connectIP.Location = new System.Drawing.Point(200, 52);
            this.mask_connectIP.Mask = "000.000.000.000";
            this.mask_connectIP.Name = "mask_connectIP";
            this.mask_connectIP.PromptChar = ' ';
            this.mask_connectIP.Size = new System.Drawing.Size(100, 21);
            this.mask_connectIP.TabIndex = 18;
            // 
            // tab_udp
            // 
            this.tab_udp.Location = new System.Drawing.Point(4, 22);
            this.tab_udp.Name = "tab_udp";
            this.tab_udp.Padding = new System.Windows.Forms.Padding(3);
            this.tab_udp.Size = new System.Drawing.Size(874, 515);
            this.tab_udp.TabIndex = 1;
            this.tab_udp.Text = "UDP";
            this.tab_udp.UseVisualStyleBackColor = true;
            // 
            // panel2
            // 
            this.panel2.Controls.Add(this.tb_statuMsgs);
            this.panel2.Dock = System.Windows.Forms.DockStyle.Right;
            this.panel2.Location = new System.Drawing.Point(896, 0);
            this.panel2.Name = "panel2";
            this.panel2.Size = new System.Drawing.Size(263, 470);
            this.panel2.TabIndex = 2;
            // 
            // tb_statuMsgs
            // 
            this.tb_statuMsgs.Dock = System.Windows.Forms.DockStyle.Fill;
            this.tb_statuMsgs.Location = new System.Drawing.Point(0, 0);
            this.tb_statuMsgs.Multiline = true;
            this.tb_statuMsgs.Name = "tb_statuMsgs";
            this.tb_statuMsgs.Size = new System.Drawing.Size(263, 470);
            this.tb_statuMsgs.TabIndex = 0;
            // 
            // btn_removeDevices
            // 
            this.btn_removeDevices.Location = new System.Drawing.Point(591, 102);
            this.btn_removeDevices.Name = "btn_removeDevices";
            this.btn_removeDevices.Size = new System.Drawing.Size(99, 29);
            this.btn_removeDevices.TabIndex = 21;
            this.btn_removeDevices.Text = "Remove_Devices";
            this.btn_removeDevices.UseVisualStyleBackColor = true;
            this.btn_removeDevices.Click += new System.EventHandler(this.btn_removeDevices_Click);
            // 
            // btn_removeDevice
            // 
            this.btn_removeDevice.Location = new System.Drawing.Point(486, 102);
            this.btn_removeDevice.Name = "btn_removeDevice";
            this.btn_removeDevice.Size = new System.Drawing.Size(99, 29);
            this.btn_removeDevice.TabIndex = 20;
            this.btn_removeDevice.Text = "Remove_Device";
            this.btn_removeDevice.UseVisualStyleBackColor = true;
            this.btn_removeDevice.Click += new System.EventHandler(this.btn_removeDevice_Click);
            // 
            // btn_defaultconfig
            // 
            this.btn_defaultconfig.Location = new System.Drawing.Point(381, 48);
            this.btn_defaultconfig.Name = "btn_defaultconfig";
            this.btn_defaultconfig.Size = new System.Drawing.Size(99, 29);
            this.btn_defaultconfig.TabIndex = 19;
            this.btn_defaultconfig.Text = "default config";
            this.btn_defaultconfig.UseVisualStyleBackColor = true;
            this.btn_defaultconfig.Click += new System.EventHandler(this.btn_defaultconfig_Click);
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(177, 56);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(71, 12);
            this.label5.TabIndex = 18;
            this.label5.Text = "ETH_Channel";
            // 
            // cmb_ETHChnlist
            // 
            this.cmb_ETHChnlist.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cmb_ETHChnlist.FormattingEnabled = true;
            this.cmb_ETHChnlist.Location = new System.Drawing.Point(254, 53);
            this.cmb_ETHChnlist.Name = "cmb_ETHChnlist";
            this.cmb_ETHChnlist.Size = new System.Drawing.Size(121, 20);
            this.cmb_ETHChnlist.TabIndex = 17;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(13, 110);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(47, 12);
            this.label4.TabIndex = 16;
            this.label4.Text = "gateway";
            // 
            // mask_getway
            // 
            this.mask_getway.Location = new System.Drawing.Point(71, 107);
            this.mask_getway.Mask = "000.000.000.000";
            this.mask_getway.Name = "mask_getway";
            this.mask_getway.PromptChar = ' ';
            this.mask_getway.Size = new System.Drawing.Size(100, 21);
            this.mask_getway.TabIndex = 15;
            this.mask_getway.KeyDown += new System.Windows.Forms.KeyEventHandler(this.maskedTextBox1_KeyDown);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(15, 82);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(47, 12);
            this.label3.TabIndex = 14;
            this.label3.Text = "netmask";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(13, 49);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(41, 12);
            this.label2.TabIndex = 13;
            this.label2.Text = "ipaddr";
            // 
            // mask_net
            // 
            this.mask_net.Location = new System.Drawing.Point(71, 80);
            this.mask_net.Mask = "000.000.000.000";
            this.mask_net.Name = "mask_net";
            this.mask_net.PromptChar = ' ';
            this.mask_net.Size = new System.Drawing.Size(100, 21);
            this.mask_net.TabIndex = 12;
            this.mask_net.KeyDown += new System.Windows.Forms.KeyEventHandler(this.maskedTextBox1_KeyDown);
            // 
            // mask_ip
            // 
            this.mask_ip.Location = new System.Drawing.Point(71, 49);
            this.mask_ip.Mask = "000.000.000.000";
            this.mask_ip.Name = "mask_ip";
            this.mask_ip.PromptChar = ' ';
            this.mask_ip.Size = new System.Drawing.Size(100, 21);
            this.mask_ip.TabIndex = 11;
            this.mask_ip.KeyDown += new System.Windows.Forms.KeyEventHandler(this.maskedTextBox1_KeyDown);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(177, 107);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(47, 12);
            this.label1.TabIndex = 6;
            this.label1.Text = "macaddr";
            // 
            // mask_macaddr
            // 
            this.mask_macaddr.Location = new System.Drawing.Point(226, 107);
            this.mask_macaddr.Mask = "000:000:000:000:000:000";
            this.mask_macaddr.Name = "mask_macaddr";
            this.mask_macaddr.PromptChar = ' ';
            this.mask_macaddr.Size = new System.Drawing.Size(149, 21);
            this.mask_macaddr.TabIndex = 3;
            this.mask_macaddr.KeyDown += new System.Windows.Forms.KeyEventHandler(this.maskedTextBox1_KeyDown);
            // 
            // btn_addDev
            // 
            this.btn_addDev.Location = new System.Drawing.Point(381, 102);
            this.btn_addDev.Name = "btn_addDev";
            this.btn_addDev.Size = new System.Drawing.Size(99, 29);
            this.btn_addDev.TabIndex = 2;
            this.btn_addDev.Text = "ADD_Device";
            this.btn_addDev.UseVisualStyleBackColor = true;
            this.btn_addDev.Click += new System.EventHandler(this.btn_addDev_Click);
            // 
            // btn_connect
            // 
            this.btn_connect.Location = new System.Drawing.Point(99, 3);
            this.btn_connect.Name = "btn_connect";
            this.btn_connect.Size = new System.Drawing.Size(87, 29);
            this.btn_connect.TabIndex = 1;
            this.btn_connect.Text = "Connect";
            this.btn_connect.UseVisualStyleBackColor = true;
            this.btn_connect.Click += new System.EventHandler(this.btn_connect_Click);
            // 
            // btn_hwconfig
            // 
            this.btn_hwconfig.Location = new System.Drawing.Point(3, 3);
            this.btn_hwconfig.Name = "btn_hwconfig";
            this.btn_hwconfig.Size = new System.Drawing.Size(87, 29);
            this.btn_hwconfig.TabIndex = 0;
            this.btn_hwconfig.Text = "HW_Configer";
            this.btn_hwconfig.UseVisualStyleBackColor = true;
            this.btn_hwconfig.Click += new System.EventHandler(this.btn_hwconfig_Click);
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.tv_ethList);
            this.panel1.Dock = System.Windows.Forms.DockStyle.Left;
            this.panel1.Location = new System.Drawing.Point(0, 0);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(212, 470);
            this.panel1.TabIndex = 5;
            // 
            // panel5
            // 
            this.panel5.Controls.Add(this.btn_removeDevices);
            this.panel5.Controls.Add(this.btn_hwconfig);
            this.panel5.Controls.Add(this.btn_removeDevice);
            this.panel5.Controls.Add(this.btn_connect);
            this.panel5.Controls.Add(this.btn_defaultconfig);
            this.panel5.Controls.Add(this.btn_addDev);
            this.panel5.Controls.Add(this.label5);
            this.panel5.Controls.Add(this.mask_macaddr);
            this.panel5.Controls.Add(this.cmb_ETHChnlist);
            this.panel5.Controls.Add(this.label1);
            this.panel5.Controls.Add(this.label4);
            this.panel5.Controls.Add(this.mask_ip);
            this.panel5.Controls.Add(this.mask_getway);
            this.panel5.Controls.Add(this.mask_net);
            this.panel5.Controls.Add(this.label3);
            this.panel5.Controls.Add(this.label2);
            this.panel5.Dock = System.Windows.Forms.DockStyle.Top;
            this.panel5.Location = new System.Drawing.Point(212, 0);
            this.panel5.Name = "panel5";
            this.panel5.Size = new System.Drawing.Size(684, 137);
            this.panel5.TabIndex = 6;
            // 
            // panel3
            // 
            this.panel3.Controls.Add(this.tabControl1);
            this.panel3.Dock = System.Windows.Forms.DockStyle.Fill;
            this.panel3.Location = new System.Drawing.Point(212, 137);
            this.panel3.Name = "panel3";
            this.panel3.Size = new System.Drawing.Size(684, 333);
            this.panel3.TabIndex = 7;
            // 
            // tv_ethList
            // 
            this.tv_ethList.Dock = System.Windows.Forms.DockStyle.Fill;
            this.tv_ethList.Location = new System.Drawing.Point(0, 0);
            this.tv_ethList.Name = "tv_ethList";
            this.tv_ethList.Size = new System.Drawing.Size(212, 470);
            this.tv_ethList.TabIndex = 0;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1159, 470);
            this.Controls.Add(this.panel3);
            this.Controls.Add(this.panel5);
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.panel2);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.tabControl1.ResumeLayout(false);
            this.tab_tcp.ResumeLayout(false);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.panel2.ResumeLayout(false);
            this.panel2.PerformLayout();
            this.panel1.ResumeLayout(false);
            this.panel5.ResumeLayout(false);
            this.panel5.PerformLayout();
            this.panel3.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.TabControl tabControl1;
        private System.Windows.Forms.TabPage tab_tcp;
        private System.Windows.Forms.CheckBox cb_client;
        private System.Windows.Forms.TabPage tab_udp;
        private System.Windows.Forms.Panel panel2;
        private System.Windows.Forms.Button btn_hwconfig;
        private System.Windows.Forms.MaskedTextBox mask_macaddr;
        private System.Windows.Forms.Button btn_addDev;
        private System.Windows.Forms.Button btn_connect;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.MaskedTextBox mask_getway;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.MaskedTextBox mask_net;
        private System.Windows.Forms.MaskedTextBox mask_ip;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.ComboBox cmb_ETHChnlist;
        private System.Windows.Forms.TextBox tb_statuMsgs;
        private System.Windows.Forms.Button btn_defaultconfig;
        private System.Windows.Forms.Button btn_removeDevices;
        private System.Windows.Forms.Button btn_removeDevice;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.MaskedTextBox mask_NowPort;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.MaskedTextBox mask_NowIP;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.MaskedTextBox mask_connectPort;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.MaskedTextBox mask_connectIP;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Button btn_ConnectServer;
        private System.Windows.Forms.Button btn_CreateTCP;
        private System.Windows.Forms.Button btn_tcpdefaultConfig;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Panel panel5;
        private System.Windows.Forms.TreeView tv_ethList;
        private System.Windows.Forms.Panel panel3;
    }
}

