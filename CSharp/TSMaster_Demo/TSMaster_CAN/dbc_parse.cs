using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Runtime.InteropServices;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using TSMaster;

namespace TSMaster_CAN
{


    public struct can_network
    {
        public string network_name;
        public can_node[] can_nodes;

    }
    public struct can_node
    {
        public string node_name;
        public can_message[] tx_can_Messages;
        public can_message[] rx_can_Messages;
    }
    public struct can_message
    {
        public string message_name;
        public string[] signals;
    }

    public struct _Msg_
    {
        public int msg_type;
        public int msg_id;
        public int msg_cyclic;
        public byte msg_dlc;
        public string msg_name;
        public string[] signal_Name;
        public int msg_brs;
        public TLIBCANFD ACANFD;
    }
    public enum Msg_Type
    {
        CAN = 0,
        CANFD = 1,
    }
    public enum DBCINFO
    {
        NETWORK_Name = 0,
        CAN_MSG_COUNT = 11,
        CANFD_MSG_COUNT = 12,
        NODE_COUNT = 14,
        SIGNAL_NAME = 33,
        CAN_MSG_TYPE = 40,
        CAN_MSG_DLC = 41,
        CAN_MSG_ID = 42,
        CAN_MSG_CYCLIC = 43,
        CAN_MSG_NAME = 44,
        CAN_MSG_SIGNAL_COUNT = 47,
        CAN_MSG_SIGNAL_NAME_INDEX = 48,
        CANFD_MSG_TYPE = 60,
        CANFD_MSG_DLC = 61,
        CANFD_MSG_ID = 62,
        CANFD_MSG_CYCLIC = 63,
        CANFD_MSG_NAME = 64,
        CANFD_MSG_SIGNAL_COUNT = 67,
        CANFD_MSG_SIGNAL_NAME_INDEX = 68,
        NODE_Name = 101,
        NODE_TX_CAN_COUNT = 103,
        NODE_TX_CAN_MESSAGE_INDEX = 104,
        NODE_RX_CAN_COUNT = 105,
        NODE_RX_CAN_MESSAGE_INDEX = 106,
        NODE_TX_CANFD_COUNT = 107,
        NODE_TX_CANFD_MESSAGE_INDEX = 108,
        NODE_RX_CANFD_COUNT = 109,
        NODE_RX_CANFD_MESSAGE_INDEX = 110,
    }
    
    public class dbc_parse
    {
        
        public static List<_Msg_>  msg_ = new List<_Msg_>();
        public static string tsdb_get_can_db_info(UInt32 ADatabaseId, int AType, int AIndex, int ASubIndex)
        {
            IntPtr tmpInt = new IntPtr();
            int ret = TsMasterApi.tsdb_get_can_db_info(ADatabaseId, AType, AIndex, ASubIndex, ref tmpInt);
            if (ret == 0)
            {
                return Marshal.PtrToStringAnsi(tmpInt);
            }
            else
                return "";
        }
        public static void parse(uint Aid)
        {
            int CANcount = int.Parse(tsdb_get_can_db_info(Aid, (int)DBCINFO.CAN_MSG_COUNT, 0, 0));
            for (int i = 0; i < CANcount; i++)
            {
                _Msg_ temp = new _Msg_();
                temp.msg_type = int.Parse(tsdb_get_can_db_info(Aid, (int)DBCINFO.CAN_MSG_TYPE, i, 0));
                temp.msg_dlc = byte.Parse(tsdb_get_can_db_info(Aid, (int)DBCINFO.CAN_MSG_DLC, i, 0));
                temp.msg_id = int.Parse(tsdb_get_can_db_info(Aid,(int)DBCINFO.CAN_MSG_ID, i,0));
                temp.msg_name = tsdb_get_can_db_info(Aid, (int)DBCINFO.CAN_MSG_NAME, i, 0);
                temp.msg_cyclic = int.Parse(tsdb_get_can_db_info(Aid, (int)DBCINFO.CAN_MSG_CYCLIC, i, 0));
                temp.signal_Name = new string[int.Parse(tsdb_get_can_db_info(Aid,(int)DBCINFO.CAN_MSG_SIGNAL_COUNT, i, 0))];
                for (int signalcount = 0; signalcount < temp.signal_Name.Length; signalcount++)
                {
                    temp.signal_Name[signalcount] = tsdb_get_can_db_info(Aid, (int)DBCINFO.SIGNAL_NAME, int.Parse(tsdb_get_can_db_info(Aid, (int)DBCINFO.CAN_MSG_SIGNAL_NAME_INDEX, i, signalcount)), 0);
                }
                temp.msg_brs = 0;
                temp.ACANFD = new TLIBCANFD(APP_CHANNEL.CHN1, temp.msg_id, true, (temp.msg_type == 1 || temp.msg_type == 4) ? true : false, false, temp.msg_dlc, (temp.msg_type<2) ? false : true, false);
                msg_.Add(temp);

            }

            CANcount = int.Parse(tsdb_get_can_db_info(Aid, (int)DBCINFO.CANFD_MSG_COUNT, 0, 0));
            for (int i = 0; i < CANcount; i++)
            {
                _Msg_ temp = new _Msg_();
                temp.msg_type = int.Parse(tsdb_get_can_db_info(Aid, (int)DBCINFO.CANFD_MSG_TYPE, i, 0));
                temp.msg_dlc = byte.Parse(tsdb_get_can_db_info(Aid, (int)DBCINFO.CANFD_MSG_DLC, i, 0));
                temp.msg_id = int.Parse(tsdb_get_can_db_info(Aid, (int)DBCINFO.CANFD_MSG_ID, i, 0));
                temp.msg_name = tsdb_get_can_db_info(Aid, (int)DBCINFO.CANFD_MSG_NAME, i, 0);
                temp.msg_cyclic = int.Parse(tsdb_get_can_db_info(Aid, (int)DBCINFO.CANFD_MSG_CYCLIC, i, 0));
                temp.signal_Name = new string[int.Parse(tsdb_get_can_db_info(Aid, (int)DBCINFO.CANFD_MSG_SIGNAL_COUNT, i, 0))];
                for (int signalcount = 0; signalcount < temp.signal_Name.Length; signalcount++)
                {
                    temp.signal_Name[signalcount] = tsdb_get_can_db_info(Aid,(int)DBCINFO.SIGNAL_NAME,int.Parse(tsdb_get_can_db_info(Aid,(int)DBCINFO.CANFD_MSG_SIGNAL_NAME_INDEX,i, signalcount)), 0);
                }
                temp.msg_brs = int.Parse(tsdb_get_can_db_info(Aid, 69, i, 0));
                temp.ACANFD = new TLIBCANFD(APP_CHANNEL.CHN1, temp.msg_id, true, (temp.msg_type == 1 || temp.msg_type == 4) ? true : false, false, temp.msg_dlc, (temp.msg_type < 2) ? false : true, temp.msg_brs==1?true:false);
                msg_.Add(temp);
            }
        }
        public static can_network rbs_parse(uint AID)
        {
            can_network  can_Network = new can_network();
            can_Network.network_name = tsdb_get_can_db_info(AID, (int)DBCINFO.NETWORK_Name, 0, 0);
            int Node_count = int.Parse(tsdb_get_can_db_info(AID, (int)DBCINFO.NODE_COUNT, 0, 0));
            can_Network.can_nodes = new can_node[Node_count];
            for (int i = 0; i < Node_count; i++)
            {
                can_Network.can_nodes[i].node_name = tsdb_get_can_db_info(AID, (int)DBCINFO.NODE_Name, i, 0);
                int tx_can_count = int.Parse(tsdb_get_can_db_info(AID, (int)DBCINFO.NODE_TX_CAN_COUNT, i, 0));
                int tx_canfd_count = int.Parse(tsdb_get_can_db_info(AID, (int)DBCINFO.NODE_TX_CANFD_COUNT, i, 0));

                int rx_can_count = int.Parse(tsdb_get_can_db_info(AID, (int)DBCINFO.NODE_RX_CAN_COUNT, i, 0));
                int rx_canfd_count = int.Parse(tsdb_get_can_db_info(AID, (int)DBCINFO.NODE_RX_CANFD_COUNT, i, 0));

                //获取tx_can结构体
                can_Network.can_nodes[i].tx_can_Messages = new can_message[tx_can_count+ tx_canfd_count];

                can_Network.can_nodes[i].rx_can_Messages = new can_message[rx_can_count + rx_canfd_count];
                //获取报文名以及信号名
                //1 get can_message idnex
                //2 get can message name 
                //3 get signal count
                //4 get signal name
                int tx_index = -1;
                for (int tx_can = 0; tx_can < tx_can_count; tx_can++)
                {
                    int can_message_idnex = int.Parse(tsdb_get_can_db_info(AID, (int)DBCINFO.NODE_TX_CAN_MESSAGE_INDEX,i, tx_can));
                    can_Network.can_nodes[i].tx_can_Messages[tx_can].message_name = tsdb_get_can_db_info(AID, (int)DBCINFO.CAN_MSG_NAME, can_message_idnex, 0);

                    can_Network.can_nodes[i].tx_can_Messages[tx_can].signals = new string[int.Parse(tsdb_get_can_db_info(AID, (int)DBCINFO.CAN_MSG_SIGNAL_COUNT, can_message_idnex, 0))];
                    for (int signalcount = 0; signalcount < can_Network.can_nodes[i].tx_can_Messages[tx_can].signals.Length; signalcount++)
                    {
                        can_Network.can_nodes[i].tx_can_Messages[tx_can].signals[signalcount] = tsdb_get_can_db_info(AID, (int)DBCINFO.SIGNAL_NAME, int.Parse(tsdb_get_can_db_info(AID, (int)DBCINFO.CAN_MSG_SIGNAL_NAME_INDEX, can_message_idnex, signalcount)), 0);
                    }

                    tx_index = tx_can;
                }
                for (int tx_can = 0; tx_can < tx_canfd_count; tx_can++, tx_index++)
                {
                    int can_message_idnex = int.Parse(tsdb_get_can_db_info(AID, (int)DBCINFO.NODE_TX_CANFD_MESSAGE_INDEX,i, tx_can));
                    can_Network.can_nodes[i].tx_can_Messages[tx_index+1].message_name = tsdb_get_can_db_info(AID, (int)DBCINFO.CANFD_MSG_NAME, can_message_idnex, 0);

                    can_Network.can_nodes[i].tx_can_Messages[tx_index + 1].signals = new string[int.Parse(tsdb_get_can_db_info(AID, (int)DBCINFO.CANFD_MSG_SIGNAL_COUNT, can_message_idnex, 0))];
                    for (int signalcount = 0; signalcount < can_Network.can_nodes[i].tx_can_Messages[tx_index + 1].signals.Length; signalcount++)
                    {
                        can_Network.can_nodes[i].tx_can_Messages[tx_index + 1].signals[signalcount] = tsdb_get_can_db_info(AID, (int)DBCINFO.SIGNAL_NAME, int.Parse(tsdb_get_can_db_info(AID, (int)DBCINFO.CANFD_MSG_SIGNAL_NAME_INDEX, can_message_idnex, signalcount)), 0);
                    }
                }

                int rx_index = -1;
                for (int tx_can = 0; tx_can < rx_can_count; tx_can++)
                {
                    int can_message_idnex = int.Parse(tsdb_get_can_db_info(AID, (int)DBCINFO.NODE_RX_CAN_MESSAGE_INDEX, i, tx_can));
                    can_Network.can_nodes[i].rx_can_Messages[tx_can].message_name = tsdb_get_can_db_info(AID, (int)DBCINFO.CAN_MSG_NAME, can_message_idnex, 0);

                    can_Network.can_nodes[i].rx_can_Messages[tx_can].signals = new string[int.Parse(tsdb_get_can_db_info(AID, (int)DBCINFO.CAN_MSG_SIGNAL_COUNT, can_message_idnex, 0))];
                    for (int signalcount = 0; signalcount < can_Network.can_nodes[i].rx_can_Messages[tx_can].signals.Length; signalcount++)
                    {
                        can_Network.can_nodes[i].rx_can_Messages[tx_can].signals[signalcount] = tsdb_get_can_db_info(AID, (int)DBCINFO.SIGNAL_NAME, int.Parse(tsdb_get_can_db_info(AID, (int)DBCINFO.CAN_MSG_SIGNAL_NAME_INDEX, can_message_idnex, signalcount)), 0);
                    }

                    rx_index = tx_can;
                }
                for (int tx_can = 0; tx_can < rx_canfd_count; tx_can++, rx_index++)
                {
                    int can_message_idnex = int.Parse(tsdb_get_can_db_info(AID, (int)DBCINFO.NODE_RX_CANFD_MESSAGE_INDEX, i, tx_can));
                    can_Network.can_nodes[i].rx_can_Messages[rx_index + 1].message_name = tsdb_get_can_db_info(AID, (int)DBCINFO.CANFD_MSG_NAME, can_message_idnex, 0);

                    can_Network.can_nodes[i].rx_can_Messages[rx_index + 1].signals = new string[int.Parse(tsdb_get_can_db_info(AID, (int)DBCINFO.CANFD_MSG_SIGNAL_COUNT, can_message_idnex, 0))];
                    for (int signalcount = 0; signalcount < can_Network.can_nodes[i].rx_can_Messages[rx_index + 1].signals.Length; signalcount++)
                    {
                        can_Network.can_nodes[i].rx_can_Messages[rx_index + 1].signals[signalcount] = tsdb_get_can_db_info(AID, (int)DBCINFO.SIGNAL_NAME, int.Parse(tsdb_get_can_db_info(AID, (int)DBCINFO.CANFD_MSG_SIGNAL_NAME_INDEX, can_message_idnex, signalcount)), 0);
                    }
                }
            }

            return can_Network;


        }
    }


}
