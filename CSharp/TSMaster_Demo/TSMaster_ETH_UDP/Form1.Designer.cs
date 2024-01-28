namespace TSMaster_ETH_UDP
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
            this.btn_sendUDP = new System.Windows.Forms.Button();
            this.btn_createUDP = new System.Windows.Forms.Button();
            this.btn_ONOFF = new System.Windows.Forms.Button();
            this.btn_HWconfig = new System.Windows.Forms.Button();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // btn_sendUDP
            // 
            this.btn_sendUDP.Location = new System.Drawing.Point(327, 3);
            this.btn_sendUDP.Margin = new System.Windows.Forms.Padding(4);
            this.btn_sendUDP.Name = "btn_sendUDP";
            this.btn_sendUDP.Size = new System.Drawing.Size(100, 29);
            this.btn_sendUDP.TabIndex = 7;
            this.btn_sendUDP.Text = "发送UDP";
            this.btn_sendUDP.UseVisualStyleBackColor = true;
            this.btn_sendUDP.Click += new System.EventHandler(this.btn_sendUDP_Click);
            // 
            // btn_createUDP
            // 
            this.btn_createUDP.Location = new System.Drawing.Point(219, 3);
            this.btn_createUDP.Margin = new System.Windows.Forms.Padding(4);
            this.btn_createUDP.Name = "btn_createUDP";
            this.btn_createUDP.Size = new System.Drawing.Size(100, 29);
            this.btn_createUDP.TabIndex = 6;
            this.btn_createUDP.Text = "创建Socket";
            this.btn_createUDP.UseVisualStyleBackColor = true;
            this.btn_createUDP.Click += new System.EventHandler(this.btn_createUDP_Click);
            // 
            // btn_ONOFF
            // 
            this.btn_ONOFF.Location = new System.Drawing.Point(111, 3);
            this.btn_ONOFF.Margin = new System.Windows.Forms.Padding(4);
            this.btn_ONOFF.Name = "btn_ONOFF";
            this.btn_ONOFF.Size = new System.Drawing.Size(100, 29);
            this.btn_ONOFF.TabIndex = 5;
            this.btn_ONOFF.Text = "连接";
            this.btn_ONOFF.UseVisualStyleBackColor = true;
            this.btn_ONOFF.Click += new System.EventHandler(this.btn_ONOFF_Click);
            // 
            // btn_HWconfig
            // 
            this.btn_HWconfig.Location = new System.Drawing.Point(3, 3);
            this.btn_HWconfig.Margin = new System.Windows.Forms.Padding(4);
            this.btn_HWconfig.Name = "btn_HWconfig";
            this.btn_HWconfig.Size = new System.Drawing.Size(100, 29);
            this.btn_HWconfig.TabIndex = 4;
            this.btn_HWconfig.Text = "硬件配置";
            this.btn_HWconfig.UseVisualStyleBackColor = true;
            this.btn_HWconfig.Click += new System.EventHandler(this.btn_HWconfig_Click);
            // 
            // textBox1
            // 
            this.textBox1.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.textBox1.Location = new System.Drawing.Point(0, 141);
            this.textBox1.Multiline = true;
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(745, 241);
            this.textBox1.TabIndex = 8;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(745, 382);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.btn_sendUDP);
            this.Controls.Add(this.btn_createUDP);
            this.Controls.Add(this.btn_ONOFF);
            this.Controls.Add(this.btn_HWconfig);
            this.Name = "Form1";
            this.Text = "Form1";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.Form1_FormClosing);
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btn_sendUDP;
        private System.Windows.Forms.Button btn_createUDP;
        private System.Windows.Forms.Button btn_ONOFF;
        private System.Windows.Forms.Button btn_HWconfig;
        private System.Windows.Forms.TextBox textBox1;
    }
}

