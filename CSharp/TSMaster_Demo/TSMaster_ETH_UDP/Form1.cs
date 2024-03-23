using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Runtime.InteropServices;
using System.Runtime.InteropServices.ComTypes;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;
using TSMaster;

namespace TSMaster_ETH_UDP
{
    public partial class Form1 : Form
    {

        public Byte[] StructToBytes(Object structure)
        {
            Int32 size = Marshal.SizeOf(structure);
            Console.WriteLine(size);
            IntPtr buffer = Marshal.AllocHGlobal(size);
            try
            {
                Marshal.StructureToPtr(structure, buffer, false);
                Byte[] bytes = new Byte[size];
                Marshal.Copy(buffer, bytes, 0, size);
                return bytes;
            }
            finally
            {
                Marshal.FreeHGlobal(buffer);
            }
        }

        public Object BytesToStruct(Byte[] bytes, Type strcutType)
        {
            Int32 size = Marshal.SizeOf(strcutType);
            IntPtr buffer = Marshal.AllocHGlobal(size);
            try
            {
                Marshal.Copy(bytes, 0, buffer, size);
                return Marshal.PtrToStructure(buffer, strcutType);
            }
            finally
            {
                Marshal.FreeHGlobal(buffer);
            }
        }
        delegate void Callmsg(string msg);
        void log(string msg)
        {
            if (textBox1.InvokeRequired == false)
            {
                textBox1.AppendText(msg);
            }
            else
            {
                Callmsg callmsg = new Callmsg(log);
                textBox1.Invoke(callmsg, msg);
            }
        }
        public Form1()
        {
            InitializeComponent();
        }
        bool ISConnect = false;
        Tip4_addr_t ipaddr = new Tip4_addr_t();
        Tip4_addr_t gw = new Tip4_addr_t();
        Tip4_addr_t netmask = new Tip4_addr_t();
        private void btn_HWconfig_Click(object sender, EventArgs e)
        {
            if (!ISConnect)
            {
                TsMasterApi.tsapp_show_tsmaster_window("Hardware", true);
                
            }
        }

        private void btn_ONOFF_Click(object sender, EventArgs e)
        {
            if (!ISConnect)
            {
                TsMasterApi.tssocket_initialize(0);
                TsMasterApi.tssocket_aton("192.168.1.1", ref ipaddr);
                TsMasterApi.tssocket_aton("192.168.1.0", ref gw);
                TsMasterApi.tssocket_aton("255.255.255.0", ref netmask);
                byte[] buf = { 1, 2, 3, 4, 5, 50 };
                unsafe
                {
                    fixed (byte* p = buf)
                    {
                        //配置IPV4 网关 掩码
                        TsMasterApi.tssocket_add_device(0, p, ipaddr, netmask, gw, 1500);
                        TsMasterApi.tssocket_aton("192.168.1.2", ref ipaddr);
                        TsMasterApi.tssocket_add_device(0, p, ipaddr, netmask, gw, 1500);
                    }
                }
                if (0 == TsMasterApi.tsapp_connect())
                {
                    ISConnect = true;
                    btn_ONOFF.Text = "停止";
                }
            }
            else {
                if (0 == TsMasterApi.tsapp_disconnect())
                {
                    ISConnect = false;
                    if(IsCreateUDP)
                    {
                        IsCreateUDP = false;
                        TsMasterApi.tssocket_udp_close(serverSocket);
                    }
                   
                    btn_ONOFF.Text = "连接";
                }
            }
                
        }
        int sock = 0;//socket 句柄

        //暂时保留的回调函数
        tosun_recv_callback a = null;
        tosun_tcp_presend_callback b = null;
        tosun_tcp_ack_callback c = null;

        //udp 发送到指定ip port
        Tts_sockaddr dstaddr = new Tts_sockaddr();

        bool IsCreateUDP = false;

        bool isrecv = true;
        [DllImport(".\\TSMaster.dll", CallingConvention = CallingConvention.StdCall, CharSet = CharSet.Ansi)]
        public static extern unsafe int tssocket_recvfrom(int s, byte* mem, int len, int flags, ref Tts_sockaddr from, ref uint fromlen);
       
        int serverSocket = 0;
        private void btn_createUDP_Click(object sender, EventArgs e)
        {
            if (ISConnect && !IsCreateUDP)
            {

                if (0 != TsMasterApi.tssocket_udp(0, "192.168.1.1:20001", ref serverSocket))
                {
                    log("UDP Create failed\r\n");
                }
                IsCreateUDP = true;
                
            }
            else
            {
                MessageBox.Show("请先连接硬件");
            }
        }
        [DllImport(".\\TSMaster.dll", CallingConvention = CallingConvention.StdCall, CharSet = CharSet.Ansi)]
        public static extern unsafe int tssocket_sendto(int s, byte* mem, uint len, int flags, ref Tts_sockaddr ato, uint tolen);
        private void btn_sendUDP_Click(object sender, EventArgs e)
        {
            if (ISConnect && IsCreateUDP)
            {
                byte[] buf = new byte[1400];
                for (int i = 0; i < buf.Length; i++)
                {
                    buf[i] = (byte)i;
                }
                unsafe
                {
                    fixed (byte* p = buf)
                    {
                        int ret = TsMasterApi.tssocket_udp_sendto(serverSocket, "192.168.1.2:30001", p, 1400);
                    }
                }
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            TsMasterApi.initialize_lib_tsmaster("ETHUDPDemo");
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            if (IsCreateUDP)
            {
                IsCreateUDP = false;
                //TsMasterApi.tssocket_udp_close(serverSocket);
            }
        }
    }
}
