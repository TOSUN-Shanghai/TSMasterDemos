namespace TSMaster_ETH_TCP
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
            this.btn_sendTCP = new System.Windows.Forms.Button();
            this.btn_createTCP = new System.Windows.Forms.Button();
            this.btn_ONOFF = new System.Windows.Forms.Button();
            this.btn_HWconfig = new System.Windows.Forms.Button();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // btn_sendTCP
            // 
            this.btn_sendTCP.Location = new System.Drawing.Point(253, 10);
            this.btn_sendTCP.Name = "btn_sendTCP";
            this.btn_sendTCP.Size = new System.Drawing.Size(75, 23);
            this.btn_sendTCP.TabIndex = 11;
            this.btn_sendTCP.Text = "发送TCP";
            this.btn_sendTCP.UseVisualStyleBackColor = true;
            this.btn_sendTCP.Click += new System.EventHandler(this.btn_sendTCP_Click);
            // 
            // btn_createTCP
            // 
            this.btn_createTCP.Location = new System.Drawing.Point(172, 10);
            this.btn_createTCP.Name = "btn_createTCP";
            this.btn_createTCP.Size = new System.Drawing.Size(75, 23);
            this.btn_createTCP.TabIndex = 10;
            this.btn_createTCP.Text = "创建Socket";
            this.btn_createTCP.UseVisualStyleBackColor = true;
            this.btn_createTCP.Click += new System.EventHandler(this.btn_createTCP_Click);
            // 
            // btn_ONOFF
            // 
            this.btn_ONOFF.Location = new System.Drawing.Point(91, 10);
            this.btn_ONOFF.Name = "btn_ONOFF";
            this.btn_ONOFF.Size = new System.Drawing.Size(75, 23);
            this.btn_ONOFF.TabIndex = 9;
            this.btn_ONOFF.Text = "连接";
            this.btn_ONOFF.UseVisualStyleBackColor = true;
            this.btn_ONOFF.Click += new System.EventHandler(this.btn_ONOFF_Click);
            // 
            // btn_HWconfig
            // 
            this.btn_HWconfig.Location = new System.Drawing.Point(10, 10);
            this.btn_HWconfig.Name = "btn_HWconfig";
            this.btn_HWconfig.Size = new System.Drawing.Size(75, 23);
            this.btn_HWconfig.TabIndex = 8;
            this.btn_HWconfig.Text = "硬件配置";
            this.btn_HWconfig.UseVisualStyleBackColor = true;
            this.btn_HWconfig.Click += new System.EventHandler(this.btn_HWconfig_Click);
            // 
            // textBox1
            // 
            this.textBox1.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.textBox1.Location = new System.Drawing.Point(0, 140);
            this.textBox1.Multiline = true;
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(600, 220);
            this.textBox1.TabIndex = 12;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(600, 360);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.btn_sendTCP);
            this.Controls.Add(this.btn_createTCP);
            this.Controls.Add(this.btn_ONOFF);
            this.Controls.Add(this.btn_HWconfig);
            this.Margin = new System.Windows.Forms.Padding(2);
            this.Name = "Form1";
            this.Text = "Form1";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.Form1_FormClosing);
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btn_sendTCP;
        private System.Windows.Forms.Button btn_createTCP;
        private System.Windows.Forms.Button btn_ONOFF;
        private System.Windows.Forms.Button btn_HWconfig;
        private System.Windows.Forms.TextBox textBox1;
    }
}

