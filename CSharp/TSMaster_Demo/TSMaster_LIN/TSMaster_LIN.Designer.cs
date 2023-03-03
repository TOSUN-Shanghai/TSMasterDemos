namespace TSMaster_LIN
{
    partial class TSMaster_LIN
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.btn_hw_config = new System.Windows.Forms.Button();
            this.btn_show_hw = new System.Windows.Forms.Button();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.lv_showmsg = new System.Windows.Forms.ListView();
            this.columnHeader6 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader8 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader2 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader3 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader7 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader4 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader5 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.btn_on_off = new System.Windows.Forms.Button();
            this.btn_slave = new System.Windows.Forms.Button();
            this.btn_Master = new System.Windows.Forms.Button();
            this.btn_send = new System.Windows.Forms.Button();
            this.btn_sendrecv = new System.Windows.Forms.Button();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // btn_hw_config
            // 
            this.btn_hw_config.Location = new System.Drawing.Point(20, 35);
            this.btn_hw_config.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.btn_hw_config.Name = "btn_hw_config";
            this.btn_hw_config.Size = new System.Drawing.Size(160, 40);
            this.btn_hw_config.TabIndex = 2;
            this.btn_hw_config.Text = "默认硬件配置";
            this.btn_hw_config.UseVisualStyleBackColor = true;
            this.btn_hw_config.Click += new System.EventHandler(this.btn_hw_config_Click);
            // 
            // btn_show_hw
            // 
            this.btn_show_hw.Location = new System.Drawing.Point(191, 35);
            this.btn_show_hw.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.btn_show_hw.Name = "btn_show_hw";
            this.btn_show_hw.Size = new System.Drawing.Size(207, 40);
            this.btn_show_hw.TabIndex = 3;
            this.btn_show_hw.Text = "打开硬件窗口配置";
            this.btn_show_hw.UseVisualStyleBackColor = true;
            this.btn_show_hw.Click += new System.EventHandler(this.btn_show_hw_Click);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.lv_showmsg);
            this.groupBox1.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.groupBox1.Location = new System.Drawing.Point(0, 268);
            this.groupBox1.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Padding = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.groupBox1.Size = new System.Drawing.Size(1467, 520);
            this.groupBox1.TabIndex = 7;
            this.groupBox1.TabStop = false;
            // 
            // lv_showmsg
            // 
            this.lv_showmsg.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.columnHeader6,
            this.columnHeader8,
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
            this.lv_showmsg.Size = new System.Drawing.Size(1455, 486);
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
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.btn_sendrecv);
            this.groupBox2.Controls.Add(this.btn_send);
            this.groupBox2.Controls.Add(this.btn_on_off);
            this.groupBox2.Controls.Add(this.btn_slave);
            this.groupBox2.Controls.Add(this.btn_Master);
            this.groupBox2.Controls.Add(this.btn_hw_config);
            this.groupBox2.Controls.Add(this.btn_show_hw);
            this.groupBox2.Dock = System.Windows.Forms.DockStyle.Fill;
            this.groupBox2.Location = new System.Drawing.Point(0, 0);
            this.groupBox2.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Padding = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.groupBox2.Size = new System.Drawing.Size(1467, 268);
            this.groupBox2.TabIndex = 8;
            this.groupBox2.TabStop = false;
            // 
            // btn_on_off
            // 
            this.btn_on_off.Location = new System.Drawing.Point(409, 35);
            this.btn_on_off.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.btn_on_off.Name = "btn_on_off";
            this.btn_on_off.Size = new System.Drawing.Size(138, 40);
            this.btn_on_off.TabIndex = 7;
            this.btn_on_off.Text = "连接";
            this.btn_on_off.UseVisualStyleBackColor = true;
            this.btn_on_off.Click += new System.EventHandler(this.btn_on_off_Click);
            // 
            // btn_slave
            // 
            this.btn_slave.Location = new System.Drawing.Point(706, 35);
            this.btn_slave.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.btn_slave.Name = "btn_slave";
            this.btn_slave.Size = new System.Drawing.Size(138, 40);
            this.btn_slave.TabIndex = 6;
            this.btn_slave.Text = "从节点";
            this.btn_slave.UseVisualStyleBackColor = true;
            this.btn_slave.Click += new System.EventHandler(this.btn_slave_Click);
            // 
            // btn_Master
            // 
            this.btn_Master.Location = new System.Drawing.Point(557, 35);
            this.btn_Master.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.btn_Master.Name = "btn_Master";
            this.btn_Master.Size = new System.Drawing.Size(138, 40);
            this.btn_Master.TabIndex = 4;
            this.btn_Master.Text = "主节点";
            this.btn_Master.UseVisualStyleBackColor = true;
            this.btn_Master.Click += new System.EventHandler(this.btn_Master_Click);
            // 
            // btn_send
            // 
            this.btn_send.Location = new System.Drawing.Point(20, 122);
            this.btn_send.Name = "btn_send";
            this.btn_send.Size = new System.Drawing.Size(150, 40);
            this.btn_send.TabIndex = 8;
            this.btn_send.Text = "发送发送报文";
            this.btn_send.UseVisualStyleBackColor = true;
            this.btn_send.Click += new System.EventHandler(this.button1_Click);
            // 
            // btn_sendrecv
            // 
            this.btn_sendrecv.Location = new System.Drawing.Point(191, 122);
            this.btn_sendrecv.Name = "btn_sendrecv";
            this.btn_sendrecv.Size = new System.Drawing.Size(150, 40);
            this.btn_sendrecv.TabIndex = 9;
            this.btn_sendrecv.Text = "发送接收报文";
            this.btn_sendrecv.UseVisualStyleBackColor = true;
            this.btn_sendrecv.Click += new System.EventHandler(this.btn_sendrecv_Click);
            // 
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // TSMaster_LIN
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(11F, 21F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1467, 788);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Margin = new System.Windows.Forms.Padding(6, 5, 6, 5);
            this.Name = "TSMaster_LIN";
            this.Text = "TSMaster_LIN";
            this.Load += new System.EventHandler(this.TSMaster_LIN_Load);
            this.Resize += new System.EventHandler(this.TSMaster_LIN_Resize);
            this.groupBox1.ResumeLayout(false);
            this.groupBox2.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btn_hw_config;
        private System.Windows.Forms.Button btn_show_hw;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.ListView lv_showmsg;
        private System.Windows.Forms.ColumnHeader columnHeader6;
        private System.Windows.Forms.ColumnHeader columnHeader8;
        private System.Windows.Forms.ColumnHeader columnHeader2;
        private System.Windows.Forms.ColumnHeader columnHeader3;
        private System.Windows.Forms.ColumnHeader columnHeader7;
        private System.Windows.Forms.ColumnHeader columnHeader4;
        private System.Windows.Forms.ColumnHeader columnHeader5;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.Button btn_on_off;
        private System.Windows.Forms.Button btn_slave;
        private System.Windows.Forms.Button btn_Master;
        private System.Windows.Forms.Button btn_sendrecv;
        private System.Windows.Forms.Button btn_send;
        private System.Windows.Forms.Timer timer1;
    }
}