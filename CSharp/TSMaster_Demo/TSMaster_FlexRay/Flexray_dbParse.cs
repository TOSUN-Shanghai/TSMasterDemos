using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using TSMaster;

namespace TSMaster_FlexRay
{
    public struct load_tree
    {
        public int dbc_index;
        public APP_CHANNEL[] chns;
        public TreeView treeView; 
        public flexray_network flexray_Network;


    }
    public struct flexray_network
    {
        public string network_name;
        public flexray_node[] flexray_nodes;

    }
    public struct flexray_node
    {
        public string node_name;
        public flexray_message[] tx_flexray_Messages;
        public flexray_message[] rx_flexray_Messages;
    }
    public struct flexray_message
    {
        public string message_name;
        public string[] signals;
    }
    public class Flexray_dbParse
    {
        public static flexray_network db_parse(int Aindex)
        {
            flexray_network flexray_Network = new flexray_network();
            int AFrameCount = 0;
            int ASignalCount = 0;
            int AECUcount = 0;
            //int ret1 = 0;
            long ASupportMask = 0;
            IntPtr temp1 = IntPtr.Zero;
            IntPtr temp2 = IntPtr.Zero;
            string AName = "";
            string AComment = "";
            long AFalgs = 0;
            //IntPtr Name = IntPtr.Zero;
            //IntPtr Comment = IntPtr.Zero;
            
            int ret = TsMasterApi.tsdb_get_flexray_db_properties_by_index_verbose(Aindex, ref ASignalCount, ref AFrameCount, ref  AECUcount, ref  ASupportMask,ref AFalgs, ref temp1, ref temp2);
            AName = Marshal.PtrToStringAnsi(temp1);
            AComment = Marshal.PtrToStringAnsi(temp2);
            flexray_Network.network_name = AName;
               // AECUcount = 5;
            flexray_Network.flexray_nodes = new flexray_node[AECUcount];
            for (int i = 0; i < AECUcount; i++)
            {
                int ATXFramecount = 0;
                int ARXFramecount = 0;

                TsMasterApi.tsdb_get_flexray_ecu_properties_by_index_verbose(Aindex, i, ref ATXFramecount, ref ARXFramecount, ref temp1, ref temp2);
                AName = Marshal.PtrToStringAnsi(temp1);
                flexray_Network.flexray_nodes[i].node_name = AName;
                flexray_Network.flexray_nodes[i].tx_flexray_Messages = new flexray_message[ATXFramecount];
                flexray_Network.flexray_nodes[i].rx_flexray_Messages = new flexray_message[ARXFramecount];
                //tx frame
                for (int txcount = 0; txcount < ATXFramecount; txcount++)
                {
                    int AFRChnnalMask = 0;
                    int AFRbasecycle = 0;
                    int ArepCycle = 0;
                    bool is_startup_frame = false;
                    int AslotID = 0;
                    long CycleMask = 0;
                    int AFRSignalCount = 0;
                    int AFRDLC = 0;
                    TsMasterApi.tsdb_get_flexray_frame_properties_by_index_verbose(Aindex, i, txcount, true, ref AFRChnnalMask, ref AFRbasecycle, ref ArepCycle, ref is_startup_frame, ref AslotID, ref CycleMask, ref AFRSignalCount, ref AFRDLC, ref temp1, ref temp2);
                    AName = Marshal.PtrToStringAnsi(temp1);
                    flexray_Network.flexray_nodes[i].tx_flexray_Messages[txcount].message_name = AName;
                    flexray_Network.flexray_nodes[i].tx_flexray_Messages[txcount].signals = new string[AFRSignalCount];
                    //Signal count 
                    for (int txsignalcount = 0; txsignalcount < AFRSignalCount; txsignalcount++)
                    {
                        TSignalType Asignaltype =(TSignalType)0;
                        TFlexRayCompuMethod ACompuMethod = (TFlexRayCompuMethod)0;
                        bool AIsIntel = false;
                        int AStartBit = 0;
                        int AUpdateBit = 0;
                        int ALength = 0;
                        double AFactor = 0;
                        double AOffset = 0;
                        double AInitValue = 0;
                        TsMasterApi.tsdb_get_flexray_signal_properties_by_index_verbose(Aindex, i, txcount, txsignalcount, true, ref Asignaltype, ref ACompuMethod, ref AIsIntel, ref AStartBit, ref AUpdateBit, ref ALength, ref AFactor, ref AOffset, ref AInitValue, ref temp1, ref temp2);
                        AName = Marshal.PtrToStringAnsi(temp1);
                        flexray_Network.flexray_nodes[i].tx_flexray_Messages[txcount].signals[txsignalcount] = AName;
                    }

                }

                for (int rxcount = 0; rxcount < ARXFramecount; rxcount++)
                {
                    int AFRChnnalMask = 0;
                    int AFRbasecycle = 0;
                    int ArepCycle = 0;
                    bool is_startup_frame = false;
                    int AslotID = 0;
                    long CycleMask = 0;
                    int AFRSignalCount = 0;
                    int AFRDLC = 0;
                    TsMasterApi.tsdb_get_flexray_frame_properties_by_index_verbose(Aindex, i, rxcount, false, ref AFRChnnalMask, ref AFRbasecycle, ref ArepCycle, ref is_startup_frame, ref AslotID, ref CycleMask, ref AFRSignalCount, ref AFRDLC, ref temp1, ref temp2);
                    AName = Marshal.PtrToStringAnsi(temp1);
                    flexray_Network.flexray_nodes[i].rx_flexray_Messages[rxcount].message_name = AName;
                    flexray_Network.flexray_nodes[i].rx_flexray_Messages[rxcount].signals = new string[AFRSignalCount];
                    //Signal count 
                    for (int rxsignalcount = 0; rxsignalcount < AFRSignalCount; rxsignalcount++)
                    {
                        TSignalType Asignaltype = (TSignalType)0;
                        TFlexRayCompuMethod ACompuMethod = (TFlexRayCompuMethod)0;
                        bool AIsIntel = false;
                        int AStartBit = 0;
                        int AUpdateBit = 0;
                        int ALength = 0;
                        double AFactor = 0;
                        double AOffset = 0;
                        double AInitValue = 0;
                        TsMasterApi.tsdb_get_flexray_signal_properties_by_index_verbose(Aindex, i, rxcount, rxsignalcount, false, ref Asignaltype, ref ACompuMethod, ref AIsIntel, ref AStartBit, ref AUpdateBit, ref ALength, ref AFactor, ref AOffset, ref AInitValue, ref temp1, ref temp2);
                        AName = Marshal.PtrToStringAnsi(temp1);
                        flexray_Network.flexray_nodes[i].rx_flexray_Messages[rxcount].signals[rxsignalcount] = AName;

                    }

                }
            }
            return flexray_Network;
        }


        


        public static void load_treeview(int dbc_index, APP_CHANNEL[] chns, TreeView tv_rbs, flexray_network flexray_Network)  
        {
            for (int i = 0; i < chns.Length; i++)
            {
                if (tv_rbs.Nodes.Count < chns.Length)
                {
                    tv_rbs.Nodes.Add("通道" + i.ToString());
                }

                tv_rbs.Nodes[i].Nodes.Add(flexray_Network.network_name);

                for (int node_inde = 0; node_inde < flexray_Network.flexray_nodes.Length; node_inde++)
                {
                    tv_rbs.Nodes[i].Nodes[dbc_index].Nodes.Add(flexray_Network.flexray_nodes[node_inde].node_name);

                    tv_rbs.Nodes[i].Nodes[dbc_index].Nodes[node_inde].Nodes.Add("TX_Message");
                    for (int txmsg_inde = 0; txmsg_inde < flexray_Network.flexray_nodes[node_inde].tx_flexray_Messages.Length; txmsg_inde++)
                    {
                        tv_rbs.Nodes[i].Nodes[dbc_index].Nodes[node_inde].Nodes[0].Nodes.Add(flexray_Network.flexray_nodes[node_inde].tx_flexray_Messages[txmsg_inde].message_name);
                        for (int signal_inde = 0; signal_inde < flexray_Network.flexray_nodes[node_inde].tx_flexray_Messages[txmsg_inde].signals.Length; signal_inde++)
                        {
                            tv_rbs.Nodes[i].Nodes[dbc_index].Nodes[node_inde].Nodes[0].Nodes[txmsg_inde].Nodes.Add(flexray_Network.flexray_nodes[node_inde].tx_flexray_Messages[txmsg_inde].signals[signal_inde]);
                        }
                    }
                    tv_rbs.Nodes[i].Nodes[dbc_index].Nodes[node_inde].Nodes.Add("RX_Message");
                    for (int txmsg_inde = 0; txmsg_inde < flexray_Network.flexray_nodes[node_inde].rx_flexray_Messages.Length; txmsg_inde++)
                    {
                        tv_rbs.Nodes[i].Nodes[dbc_index].Nodes[node_inde].Nodes[1].Nodes.Add(flexray_Network.flexray_nodes[node_inde].rx_flexray_Messages[txmsg_inde].message_name);
                        for (int signal_inde = 0; signal_inde < flexray_Network.flexray_nodes[node_inde].rx_flexray_Messages[txmsg_inde].signals.Length; signal_inde++)
                        {
                            tv_rbs.Nodes[i].Nodes[dbc_index].Nodes[node_inde].Nodes[1].Nodes[txmsg_inde].Nodes.Add(flexray_Network.flexray_nodes[node_inde].rx_flexray_Messages[txmsg_inde].signals[signal_inde]);
                        }
                    }
                }
            }
            tv_rbs.ExpandAll();
            foreach (TreeNode node in tv_rbs.Nodes)
            {
                tree_helper.HideCheckBox(tv_rbs, node);
                tree_helper.HideCheckBox(tv_rbs, node);
                foreach (TreeNode child in node.Nodes)
                    foreach (TreeNode second_child in child.Nodes)
                        foreach (TreeNode three_child in second_child.Nodes)
                        {
                            tree_helper.HideCheckBox(tv_rbs, three_child);
                            foreach (TreeNode four_child in three_child.Nodes)
                                foreach (TreeNode five_child in four_child.Nodes)
                                    tree_helper.HideCheckBox(tv_rbs, five_child);
                        }
            }
        }

        public static void load_treeview_thread(object load_Tree)
        {
            load_tree load_ = (load_tree)load_Tree;
            load_treeview(load_.dbc_index, load_.chns, load_.treeView, load_.flexray_Network);
        }

    }
}
