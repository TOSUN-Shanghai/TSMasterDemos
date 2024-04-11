using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TSMaster_ETH_Demo
{
    public struct ETHMACAddr { 
        public int ETHChnidx;
        public string macaddr;
        public string ipaddr;
        public string network;
        public string getway;
    }
    public class ETHConfig
    {
        public static string APPName = "ETHDemo";
        public static bool ISConnect = false;
        public static bool ISConfig = false;
        public static int ETHCount = 0;
        public static List<ETHMACAddr> ETHList = new List<ETHMACAddr>();
        public static int tcpHandle = 0;

    }
}
