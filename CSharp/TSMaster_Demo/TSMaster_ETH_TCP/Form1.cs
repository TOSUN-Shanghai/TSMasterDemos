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
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace TSMaster_ETH_TCP
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            TsMasterApi.initialize_lib_tsmaster("ETHTCPDemo");
        }

        private void btn_HWconfig_Click(object sender, EventArgs e)
        {
            TsMasterApi.tsapp_show_tsmaster_window("Hardware", true);
        }

        bool ISConnect = false;
        TLogDebuggingInfo logger = null;
        Tip4_addr_t ipaddr = new Tip4_addr_t();
        Tip4_addr_t gw = new Tip4_addr_t();
        Tip4_addr_t netmask = new Tip4_addr_t();
        Thread t1;
        bool IsCreateTCP = false;
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
        private void btn_ONOFF_Click(object sender, EventArgs e)
        {
            if (!ISConnect)
            {
                TsMasterApi.tssocket_initialize(0, logger);
                TsMasterApi.tssocket_aton("192.168.0.50", ref ipaddr);
                TsMasterApi.tssocket_aton("192.168.0.1", ref gw);
                TsMasterApi.tssocket_aton("255.255.255.0", ref netmask);
                byte[] buf = { 1, 2, 3, 4, 5, 50 };
                unsafe
                {
                    fixed (byte* p = buf)
                    {
                        //配置IPV4 网关 掩码
                        TsMasterApi.tssocket_add_device(0, p, ipaddr, netmask, gw, 1500);
                    }
                }
                if (0 == TsMasterApi.tsapp_connect())
                {
                    ISConnect = true;
                    
                    btn_ONOFF.Text = "停止";
                }
            }
            else
            {
                if (0 == TsMasterApi.tsapp_disconnect())
                {
                    ISConnect = false;
                    isrecv = false;
                    if (IsCreateTCP)
                    {
                        IsCreateTCP = false;
                        t1.Abort();
                    }
                    TsMasterApi.tssocket_close(0, sock);
                    btn_ONOFF.Text = "连接";
                }
            }
        }
        int sock = 0;
        //暂时保留的回调函数
        tosun_recv_callback a = null;
        tosun_tcp_presend_callback b = null;
        tosun_tcp_ack_callback c = null;
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
        Tts_sockaddr srcaddr = new Tts_sockaddr();
        bool isrecv = false;
        int revsock = -1;
        void recvtcp()
        {
           // int err = TsMasterApi.tssocket_bind(0, sock, ref srcaddr, 16);
            int err = TsMasterApi.tssocket_listen(0, sock, 2000);
            
            Tts_sockaddr revaddr = new Tts_sockaddr() ;
            uint revlen = 16;
            revsock = TsMasterApi.tssocket_accept(0, sock,  ref revaddr,ref revlen);
            isrecv = true;
            if (revsock != -1)
            {
                while (true)
                {
                    byte[] buf = new byte[7000];

                    unsafe
                    {
                        fixed (byte* p = buf)
                        {
                            int count = TsMasterApi.tssocket_recv(0, revsock, p, 7000, 0);
                            if (count > 0)
                                log(buf.ToString() + "\r\n");
                        }
                    }

                }
            }
            
        }
        private void btn_createTCP_Click(object sender, EventArgs e)
        {
            if (ISConnect && !IsCreateTCP)
            {
                sock = TsMasterApi.tssocket(0, 2, 1, 0, a, b, c);
                if (sock == -1)
                {
                    MessageBox.Show("Create error");
                    return;
                }
                IsCreateTCP = true;
                Tts_sockaddr_in self_addr = new Tts_sockaddr_in();
                self_addr.sin_family = 2;
                self_addr.sin_port = TsMasterApi.tssocket_htons(51051);
                TsMasterApi.tssocket_aton("192.168.0.50", ref self_addr.sin_addr);

                //将Tts_sockaddr_in 转为 Tts_sockaddr
                Byte[] DataAddr = StructToBytes(self_addr);
                srcaddr = (Tts_sockaddr)BytesToStruct(DataAddr, srcaddr.GetType());

                int err = TsMasterApi.tssocket_bind(0, sock, ref srcaddr, 16);

                t1 = new Thread(new ThreadStart(recvtcp));
                t1.Start();
            }
            else
            {
                MessageBox.Show("请先连接硬件");
            }
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            if(IsCreateTCP)
            {
                IsCreateTCP = false;
                t1.Abort();
                TsMasterApi.tssocket_close(0, sock);
            }
        }

        private void btn_sendTCP_Click(object sender, EventArgs e)
        {
            if (isrecv)
            {
                byte[] buf =  new byte[1400];
                for(int i = 0; i < buf.Length; i++)
                    buf[i] = (byte)i;
                unsafe {
                    fixed (byte* p = buf)
                    {
                        int ret = TsMasterApi.tssocket_send(0, revsock, p, 1400, 0);
                    }
                }
               
            }
        }
    }
}
