using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using TSMaster;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace TSMaster_ETH_Demo
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        delegate void Callmsg(string msg);
        void log(string msg)
        {
            if (tb_statuMsgs.InvokeRequired == false)
            {
                tb_statuMsgs.AppendText(msg);
            }
            else
            {
                Callmsg callmsg = new Callmsg(log);
                tb_statuMsgs.Invoke(callmsg, msg);
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            TsMasterApi.initialize_lib_tsmaster(ETHConfig.APPName);

            TsMasterApi.get_ethernet_channel_count(ref ETHConfig.ETHCount);
            get_eth_chn();
        }
        void get_eth_chn()
        {
            TsMasterApi.get_ethernet_channel_count(ref ETHConfig.ETHCount);
            if (ETHConfig.ETHCount == 0)
            {
                ETHConfig.ISConfig = false;
                TsMasterApi.tsapp_disconnect();
                MessageBox.Show("Please Configer ETH channel");
                return;
            }
            cmb_ETHChnlist.Items.Clear();
            for (int i = 0; i < ETHConfig.ETHCount; i++)
            {
                cmb_ETHChnlist.Items.Add("CH" + (i + 1).ToString());
                tv_ethList.Nodes.Add("ETH" + (i + 1).ToString());
            }
            ETHConfig.ISConfig = true;
            cmb_ETHChnlist.SelectedIndex = 0;
        }
        private void btn_hwconfig_Click(object sender, EventArgs e)
        {
            TsMasterApi.tsapp_show_tsmaster_window("Hardware", true);
            get_eth_chn();
        }
        private void btn_connect_Click(object sender, EventArgs e)
        {
            if (!ETHConfig.ISConnect)
            {
                for (int i = 0; i < ETHConfig.ETHList.Count; i++)
                {
                    TsMasterApi.tssocket_add_device_ex(ETHConfig.ETHList[i].ETHChnidx, ETHConfig.ETHList[i].macaddr, ETHConfig.ETHList[i].ipaddr, ETHConfig.ETHList[i].network, ETHConfig.ETHList[i].getway,1500);
                }
                int ret = TsMasterApi.tsapp_connect();
                if (ret == 0)
                {
                    ETHConfig.ISConnect = !ETHConfig.ISConnect;
                    btn_connect.Text = "Disconnect";
                    log("Connect successed\r\n");
                    return;
                }
                MessageBox.Show("Connect failed ,error code is" + ret.ToString());
            }
            else
            {
                for (int i = 0; i < ETHConfig.ETHList.Count; i++)
                {
                    TsMasterApi.tssocket_remove_device_ex(ETHConfig.ETHList[i].ETHChnidx, ETHConfig.ETHList[i].macaddr, ETHConfig.ETHList[i].ipaddr);
                }
                int ret = TsMasterApi.tsapp_disconnect();
                if (ret == 0)
                {
                    ETHConfig.ISConnect = !ETHConfig.ISConnect;
                    btn_connect.Text = "Connect";
                    log("DisConnect successed\r\n");
                    return;
                } 
                MessageBox.Show("Disconnect failed ,error code is" + ret.ToString());
            }
            
        }
        private void btn_defaultconfig_Click(object sender, EventArgs e)
        {
            mask_macaddr.Text = "  1:  2:  3:  4:  5: 50";
            mask_ip.Text = "192.168.  1.  1";
            mask_net.Text = "255.255.255.  0";
            mask_getway.Text = "192.168.1.  0";

        }
        private void btn_addDev_Click(object sender, EventArgs e)
        {
            if (ETHConfig.ISConnect)
            {
                MessageBox.Show("Please add devices in disconnected state.");
            }
            else if (ETHConfig.ISConfig)
            {
                string macAddr = mask_macaddr.Text.Replace(" ", "");
                string ipAddr = mask_ip.Text.Replace(" ", "");
                string network = mask_net.Text.Replace(" ", "");
                string getway = mask_getway.Text.Replace(" ", "");
                int idx = cmb_ETHChnlist.SelectedIndex;
                if (macAddr == ":::::" || ipAddr == "..." || network == "..." || getway == "...")
                {
                    MessageBox.Show("Please enter the parameters correctly.");
                    return;
                }
                TsMasterApi.tssocket_initialize(idx);
                int ret = TsMasterApi.tssocket_add_device_ex(idx, macAddr, ipAddr, network, getway, 1500);
                if (ret == 0)
                {
                    log("Add device successed\r\n");
                    ETHMACAddr macconfig = new ETHMACAddr();
                    macconfig.ETHChnidx = idx;
                    macconfig.macaddr = macAddr;
                    macconfig.ipaddr = ipAddr;
                    macconfig.network = network;
                    macconfig.getway = getway;
                    ETHConfig.ETHList.Add(macconfig);
                    return;
                }
                MessageBox.Show("add device failed ,error code " + ret.ToString());
            }
            else
            {
                MessageBox.Show("Please set hadrware configer.");
            }
        }
        private void btn_removeDevice_Click(object sender, EventArgs e)
        {
            string macAddr = mask_macaddr.Text.Replace(" ", "");
            string ipAddr = mask_ip.Text.Replace(" ", "");
            string network = mask_net.Text.Replace(" ", "");
            string getway = mask_getway.Text.Replace(" ", "");
            int idx = cmb_ETHChnlist.SelectedIndex;
            if (macAddr == ":::::" || ipAddr == "..." || network == "..." || getway == "...")
            {
                MessageBox.Show("Please enter the parameters correctly.");
                return;
            }
            //TsMasterApi.tssocket_initialize(idx);
            TsMasterApi.tssocket_remove_device_ex(idx, macAddr, ipAddr);
            log("remove device successful\r\n");
        }
        private void btn_removeDevices_Click(object sender, EventArgs e)
        {
            for (int i = 0; i < ETHConfig.ETHList.Count; i++)
            {
                TsMasterApi.tssocket_remove_device_ex(ETHConfig.ETHList[i].ETHChnidx, ETHConfig.ETHList[i].macaddr, ETHConfig.ETHList[i].ipaddr);
            }
            ETHConfig.ETHList.Clear();
            log("remove all devices successful\r\n");
        }
        private void cb_client_CheckedChanged(object sender, EventArgs e)
        {
            mask_connectIP.Enabled = cb_client.Checked;
            mask_connectPort.Enabled = cb_client.Checked;
        }
        private void btn_tcpdefaultConfig_Click(object sender, EventArgs e)
        {
            mask_NowIP.Text = "192.168.  1.  1";
            mask_NowPort.Text ="20001" ;

            if (cb_client.Checked)
            {
                mask_connectIP.Text = "192.168.  1.  2";
                mask_connectPort.Text = "30001";
            }
        }
        private void btn_CreateTCP_Click(object sender, EventArgs e)
        { 
            string ipend = mask_NowIP.Text.Replace(" ","") + ":"+ mask_NowPort.Text.Replace(" ", "");
            
            if (ipend.IndexOf("..") != -1)
            {
                MessageBox.Show("Please enter the parameters correctly.");
                return;
            }
            
            if (ETHConfig.ISConnect && ETHConfig.ETHList.Count != 0)
            {
                int ret = TsMasterApi.tssocket_tcp(cmb_ETHChnlist.SelectedIndex, ipend, ref ETHConfig.tcpHandle);
                if (ret == 0)
                {
                    log("tcp create successful\r\n");
                    if (!cb_client.Checked)
                    {
                        TsMasterApi.tssocket_tcp_start_listen(ETHConfig.tcpHandle);
                        TsMasterApi.tssocket_tcp_start_receive(ETHConfig.tcpHandle);
                    }
                    
                    
                }
                else
                {
                    MessageBox.Show("tcp create failed ,error code " + ret.ToString());
                }
            }
            else
            {
                MessageBox.Show("Please Connect or add device");
            }
        }

        private void btn_ConnectServer_Click(object sender, EventArgs e)
        {
            string serveripend = "";
            if (cb_client.Checked)
            {
                serveripend = mask_connectIP.Text.Replace(" ", "") + ":" + mask_connectPort.Text.Replace(" ", "");
                if (serveripend.IndexOf("..") != -1)
                {
                    MessageBox.Show("Please enter the parameters correctly.");
                    return;
                }
                else
                {
                    int ret = TsMasterApi.tssocket_tcp_connect(ETHConfig.tcpHandle, serveripend);
                    if (ret == 0)
                    {
                        TsMasterApi.tssocket_tcp_start_receive(ETHConfig.tcpHandle);
                        return;
                    }
                    MessageBox.Show("Connect Server tcp failed,error code is "+ ret.ToString());

                }
            }

        }

        private void maskedTextBox1_KeyDown(object sender, KeyEventArgs e)
        {
            
            if (e.KeyCode == Keys.Decimal)
            {
                MaskedTextBox maskedTextBox = (MaskedTextBox)sender;

                int pos = maskedTextBox.SelectionStart;
                int max = (maskedTextBox.MaskedTextProvider.Length - maskedTextBox.MaskedTextProvider.EditPositionCount);
                int nextField = 0;

                for (int i = 0; i < maskedTextBox.MaskedTextProvider.Length; i++)
                {
                    if (!maskedTextBox.MaskedTextProvider.IsEditPosition(i) && (pos + max) >= i)
                        nextField = i;
                }
                nextField += 1;
                maskedTextBox.SelectionStart = nextField;

            }
        }

       
    }
}
