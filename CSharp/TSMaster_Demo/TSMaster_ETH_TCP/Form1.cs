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
        Tip4_addr_t ipaddr = new Tip4_addr_t();
        Tip4_addr_t gw = new Tip4_addr_t();
        Tip4_addr_t netmask = new Tip4_addr_t();
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
        byte[] macaddr = { 1, 2, 3, 4, 5, 50 };
        private void btn_ONOFF_Click(object sender, EventArgs e)
        {
            if (!ISConnect)
            {
                TsMasterApi.tssocket_initialize(0);
                //ipaddress 
                TsMasterApi.tssocket_aton("192.168.1.1", ref ipaddr);
                //gateway
                TsMasterApi.tssocket_aton("192.168.1.0", ref gw);
                //mask
                TsMasterApi.tssocket_aton("255.255.255.0", ref netmask);

                //ipaddress 
                

                unsafe
                {
                    fixed (byte* maddr = macaddr)
                    {
                        TsMasterApi.tssocket_add_device(0, maddr, ipaddr, netmask, gw, 1500);
                        TsMasterApi.tssocket_aton("192.168.1.2", ref ipaddr);
                        TsMasterApi.tssocket_add_device(0, maddr, ipaddr, netmask, gw, 1500);
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
                    unsafe
                    {
                        fixed (byte* maddr = macaddr)
                        {
                            TsMasterApi.tssocket_remove_device(0, maddr, ref ipaddr);
                        }
                    }
                    if (ONTCPListen != null)
                    {
                        TsMasterApi.tssocket_unregister_tcp_listen_event(serverSocket, ONTCPListen);
                        TsMasterApi.tssocket_unregister_tcp_close_event(serverSocket, ONTCPDisConnect);
                        TsMasterApi.tssocket_unregister_tcp_receive_event(serverSocket, ONRECEIVE);
                        TsMasterApi.tssocket_unregister_tcp_receive_event(clientSocket, ONRECEIVE);
                        ONTCPListen = null;
                        ONTCPDisConnect = null;
                    }  
                    if (IsCreateTCP)
                    {
                        TsMasterApi.tssocket_tcp_close(serverSocket);
                        IsCreateTCP = false;
                    }
                    btn_ONOFF.Text = "连接";
                }
            }
        }
        
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

        [DllImport(".\\TSMaster.dll", CallingConvention = CallingConvention.StdCall, CharSet = CharSet.Ansi)]
        public static extern unsafe int tssocket_recv(int s, byte* mem, uint len, int flags);
        
        int serverSocket = 0;
        int clientSocket = 0;
        TSSocketReceiveEvent_Win32 ONRECEIVE = null;
        TSSocketListenEvent_Win32 ONTCPListen = null;
        TSSocketNotifyEvent_Win32 ONTCPDisConnect = null;
        bool IsAccept = false;

        string get_ip_address(uint AAddr, uint APort)
        {
            string ip = (AAddr >> 24).ToString("X2.") + ((AAddr >> 16) & 0XFF).ToString("X2.") + ((AAddr >> 8) & 0XFF).ToString("X2.") + (AAddr & 0XFF).ToString("X2.:") + APort.ToString();
            return ip;
        }
        void ontcplisten(ref int AObj, int ASocket, int AClientSocket, int AResult)
        {
            IsAccept = true;
            log("clint handle " + ASocket.ToString());
        }
        void ontcpdisconnect(ref int AObj, int ASocket, int AResult)
        {
            IsAccept = false;
        }

        unsafe void ontcpreceive(ref int AObj, int ASocket, int AResult, uint AAddr, uint APort, byte* AData, int ASize)
        {
            log(get_ip_address(AAddr, APort) + "\r\n");
        }
        private void btn_createTCP_Click(object sender, EventArgs e)
        {

            if (!IsCreateTCP)
            {
                int ret = TsMasterApi.tssocket_tcp(0, "192.168.1.1:20001", ref serverSocket);
                if (0 != ret)
                {
                    log("TCP Server create failed\r\n");
                    return;
                }
                ONTCPListen = ontcplisten;
                ONTCPDisConnect = ontcpdisconnect;
                TsMasterApi.tssocket_register_tcp_listen_event(serverSocket, ONTCPListen);
                TsMasterApi.tssocket_register_tcp_close_event(serverSocket, ONTCPDisConnect);
                ret = TsMasterApi.tssocket_tcp(0, "192.168.1.2:30001", ref clientSocket);
                if (0 != ret)
                {
                    log("TCP Server create failed\r\n");
                    return;
                }
                unsafe {
                    ONRECEIVE = ontcpreceive;
                    TsMasterApi.tssocket_register_tcp_receive_event(serverSocket, ONRECEIVE);
                    TsMasterApi.tssocket_register_tcp_receive_event(clientSocket, ONRECEIVE);
                }
                
                
                

                
                if (0 != TsMasterApi.tssocket_tcp_start_listen(serverSocket))
                {
                    log("TCP Server listen failed\r\n");
                    return;
                }
                ret =TsMasterApi.tssocket_tcp_connect(clientSocket, "192.168.1.1:20001");
                if (ret == 0)
                {
                    log("TCP clinet connect successful\r\n");
                }
                
                TsMasterApi.tssocket_tcp_start_receive(serverSocket);
                IsCreateTCP = true;
                log("TCP Server create Successful\r\n");
                return;
            }
            log("Do not create the same TCP more than once\r\n");

        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            if (ISConnect)
            {
                ISConnect = false;
                unsafe
                {
                    fixed (byte* maddr = macaddr)
                    {
                        TsMasterApi.tssocket_remove_device(0, maddr, ref ipaddr);
                    }
                }
            }
            if (ONTCPListen != null)
            {
                TsMasterApi.tssocket_unregister_tcp_listen_event(serverSocket, ONTCPListen);
                TsMasterApi.tssocket_unregister_tcp_close_event(serverSocket, ONTCPDisConnect);
                TsMasterApi.tssocket_unregister_tcp_receive_event(serverSocket, ONRECEIVE);
                TsMasterApi.tssocket_unregister_tcp_receive_event(clientSocket, ONRECEIVE);
                ONTCPListen = null;
                ONTCPDisConnect = null;
            }
            if (IsCreateTCP)
            {
                TsMasterApi.tssocket_tcp_close(serverSocket);
                IsCreateTCP = false;
            }
        }
        [DllImport(".\\TSMaster.dll", CallingConvention = CallingConvention.StdCall, CharSet = CharSet.Ansi)]
        public static extern unsafe int tssocket_send(int s, byte* mem, uint len, int flags);

        private void btn_sendTCP_Click(object sender, EventArgs e)
        {
            if (IsAccept)
            {
                byte[] datas = new byte[1400];
                unsafe {
                    fixed (byte* maddr = datas)
                    {
                        TsMasterApi.tssocket_tcp_sendto_client(serverSocket, "192.168.1.2:30001", maddr, 1400);
                    }
                }
                
            }
        }
    }
}
