using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Xml.Linq;
using TSMaster;
using static System.Net.Mime.MediaTypeNames;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace TSMaster_CAN
{


    public partial class TSMaster_CAN_Form : Form
    {
        public TSMaster_CAN_Form()
        {
            InitializeComponent();
        }

        private float x;//定义当前窗体的宽度
        private float y;//定义当前窗体的高度
        private void setTag(Control cons)
        {
            foreach (Control con in cons.Controls)
            {
                con.Tag = con.Width + ":" + con.Height + ":" + con.Left + ":" + con.Top + ":" + con.Font.Size;
                if (con.Controls.Count > 0)
                {
                    setTag(con);
                }
            }
        }
        //根据窗体大小调整字体大小
        private void setControls(float newx, float newy, Control cons)
        {
            //遍历窗体中的控件,重新设置控件的值
            foreach (Control con in cons.Controls)
            {
                //获取控件的Tag属性值，并分割后存储字符串数组
                if (con.Tag != null)
                {
                    string[] mytag = con.Tag.ToString().Split(new char[] { ':' });//获得控件Tag属性值，并分割后存储字符
                    //根据窗体缩放的比例确定控件的值
                    con.Width = Convert.ToInt32(System.Convert.ToSingle(mytag[0]) * newx);//宽度
                    con.Height = Convert.ToInt32(System.Convert.ToSingle(mytag[1]) * newy);//高度
                    con.Left = Convert.ToInt32(System.Convert.ToSingle(mytag[2]) * newx);//左边距
                    con.Top = Convert.ToInt32(System.Convert.ToSingle(mytag[3]) * newy);//顶边距
                    Single currentSize = System.Convert.ToSingle(mytag[4]) * newy;//字体大小
                    con.Font = new Font(con.Font.Name, currentSize, con.Font.Style, con.Font.Unit);
                    if (con.Controls.Count > 0)
                    {
                        setControls(newx, newy, con);
                    }
                }
            }
        }



        string appname = "TSMaster_CAN";
        int cancount = 2;
        int lincount = 0;
        List<ListViewItem> Item_list = new List<ListViewItem>();
        byte[] array = new byte[16]
            {
                0, 1, 2, 3, 4, 5, 6, 7, 8, 12,
                16, 20, 24, 32, 48, 64
            };
        UInt32 msg_count = 0;
        byte channel_p = 0;
        int id_p = 0;
        void onrxtx_event(ref int obj, ref TLIBCANFD ACANFD)
        {
            if ((ACANFD.FProperties & 0x80) == 0x80)
                return;
            if (channel_p != 0 && channel_p != (ACANFD.FIdxChn + 1))
                return;
            if (id_p != 0 && id_p != ACANFD.FIdentifier)
                return;
            ListViewItem Item = new ListViewItem();
            msg_count++;
            Item.Text = msg_count.ToString();
            Item.SubItems.Add(((ACANFD.FIdxChn.ToString())));
            Item.SubItems.Add((ACANFD.FFDProperties&1)==1 ? "CANFD" : "CAN");
            Item.SubItems.Add(((double)ACANFD.FTimeUS / 1000000).ToString());
            Item.SubItems.Add(ACANFD.FIdentifier.ToString("X8"));
            Item.SubItems.Add((ACANFD.FProperties & 1) == 1 ? "TX" : "RX");
            Item.SubItems.Add(ACANFD.FDLC.ToString());
            string text = "";
            for (int i = 0; i < array[ACANFD.FDLC]; i++)
            {
                text += ACANFD.FData[i].ToString("X2") + " ";
            }

            Item.SubItems.Add(text);
            //if (Item_list.Count >= 1000)
            //{
            //    Item_list.RemoveAt(0);
            //}
            Item_list.Add(Item);
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


        private void TSMaster_CAN_Form_Load(object sender, EventArgs e)
        {
            x = this.Width;
            y = this.Height;
            setTag(this);
            // DoubleBufferListView.DoubleBufferedListView(lv_showmsg, true);
            //初始化函数，使用TSMaster.dll中的函数，必须先调用该函数
            cbb_msgtype.SelectedIndex = 0;
            cbb_datatype.SelectedIndex = 0;
            cbb_dlc.SelectedIndex = 0;
            tv_rbs.CheckBoxes = true;

            for (int i = 1; i < 100; i += 2)
            {
                cbb_safe_level.Items.Add(i.ToString("X2"));
            }
            cbb_safe_level.SelectedIndex = 0;
            TsMasterApi.initialize_lib_tsmaster(appname);
            TsMasterApi.tsdb_unload_can_dbs();
            //tv_dbc.CheckBoxes = true;
            canfd_event = onrxtx_event;
            //Thread thread = new Thread(new ThreadStart(lvupdate));
            //thread.Start();

        }

        private void btn_hw_config_Click(object sender, EventArgs e)
        {
            //当前示例设置CAN 2个通道
            TsMasterApi.tsapp_set_can_channel_count(cancount);
            TsMasterApi.tsapp_set_lin_channel_count(lincount);

            //通道映射
            //更换其他同星产品 只需修改第6个参数
            TsMasterApi.tsapp_set_mapping_verbose(appname,(int) TLIBApplicationChannelType.APP_CAN, 0, "TC1016", TLIBBusToolDeviceType.TS_USB_DEVICE, (int)TLIB_TS_Device_Sub_Type.TC1016, 0, 0,true);

            TsMasterApi.tsapp_set_mapping_verbose(appname, (int)TLIBApplicationChannelType.APP_CAN, 1, "TC1016", TLIBBusToolDeviceType.TS_USB_DEVICE, (int)TLIB_TS_Device_Sub_Type.TC1016, 0, 1,true);

            //硬件参数配置
            TsMasterApi.tsapp_configure_baudrate_canfd(0, 500, 2000, TLIBCANFDControllerType.lfdtISOCAN, TLIBCANFDControllerMode.lfdmNormal, true);
            TsMasterApi.tsapp_configure_baudrate_canfd(1, 500, 2000, TLIBCANFDControllerType.lfdtISOCAN, TLIBCANFDControllerMode.lfdmNormal, true);


        }
        private void btn_show_hw_Click(object sender, EventArgs e)
        {
            TsMasterApi.tsapp_show_tsmaster_window("Hardware", false);
            //TsMasterApi.tsapp_get_can_channel_count(ref can_count);
        }

        private void TSMaster_CAN_Form_FormClosing(object sender, FormClosingEventArgs e)
        {
            TsMasterApi.finalize_lib_tsmaster();
        }
        int obj = 0;
        TCANFDQueueEvent_Win32 canfd_event;
        bool _isconnect = false;
        private void btn_on_off_Click(object sender, EventArgs e)
        {
            if (btn_on_off.Text == "连接")
            {
                if (0 == TsMasterApi.tsapp_connect())
                {
                    //TsMasterApi.tscom_can_rbs_enable(true);
                    TsMasterApi.tscom_can_rbs_start();
                    //timer1.Start();
                    TsMasterApi.tsapp_register_event_canfd(ref obj, canfd_event);
                    btn_on_off.Text = "断开";
                    _isconnect = true;
                }
            }
            else
            {
                if (0 == TsMasterApi.tsapp_disconnect())
                {
                    //TsMasterApi.tscom_can_rbs_enable(false);
                    TsMasterApi.tscom_can_rbs_stop();
                    TsMasterApi.tsapp_unregister_event_canfd(ref obj, canfd_event);
                    btn_on_off.Text = "连接";
                   // timer1.Stop();
                    Item_list.Clear();
                    msg_count = 0;
                    _isconnect = false;
                }
            }
        }
        //APP_CHANNEL[] chns = new APP_CHANNEL[] { APP_CHANNEL.CHN1, APP_CHANNEL.CHN2, APP_CHANNEL.CHN3, APP_CHANNEL.CHN4 };
        uint DBAId = 0;
        int dbc_index = 0;
        void load_dbc_form(object AID)
        {
            uint DBAId = (uint)AID;
            dbc_parse.parse(DBAId);
            can_network can_Network = dbc_parse.rbs_parse(DBAId);

            cbb_msg_names.Items.Clear();
            for (int index = 0; index < dbc_parse.msg_.Count; index++)
            {
                //cbb_msg_type.Items.Add(dbc_parse.msg_[index].msg_type==0?"CAN":"CANFD");
                cbb_msg_names.Items.Add(dbc_parse.msg_[index].msg_name);
            }
            if (cbb_msg_names.Items.Count > 0)
                cbb_msg_names.SelectedIndex = 0;
            for (int i = 0; i < 4; i++)
            {
                if (tv_rbs.Nodes.Count < 4)
                {
                    tv_rbs.Nodes.Add("通道" + i.ToString());
                }

                tv_rbs.Nodes[i].Nodes.Add(can_Network.network_name);

                for (int node_inde = 0; node_inde < can_Network.can_nodes.Length; node_inde++)
                {
                    tv_rbs.Nodes[i].Nodes[dbc_index].Nodes.Add(can_Network.can_nodes[node_inde].node_name);

                    tv_rbs.Nodes[i].Nodes[dbc_index].Nodes[node_inde].Nodes.Add("TX_Message");
                    for (int txmsg_inde = 0; txmsg_inde < can_Network.can_nodes[node_inde].tx_can_Messages.Length; txmsg_inde++)
                    {
                        tv_rbs.Nodes[i].Nodes[dbc_index].Nodes[node_inde].Nodes[0].Nodes.Add(can_Network.can_nodes[node_inde].tx_can_Messages[txmsg_inde].message_name);
                        for (int signal_inde = 0; signal_inde < can_Network.can_nodes[node_inde].tx_can_Messages[txmsg_inde].signals.Length; signal_inde++)
                        {
                            tv_rbs.Nodes[i].Nodes[dbc_index].Nodes[node_inde].Nodes[0].Nodes[txmsg_inde].Nodes.Add(can_Network.can_nodes[node_inde].tx_can_Messages[txmsg_inde].signals[signal_inde]);
                        }
                    }
                    tv_rbs.Nodes[i].Nodes[dbc_index].Nodes[node_inde].Nodes.Add("RX_Message");
                    for (int txmsg_inde = 0; txmsg_inde < can_Network.can_nodes[node_inde].rx_can_Messages.Length; txmsg_inde++)
                    {
                        tv_rbs.Nodes[i].Nodes[dbc_index].Nodes[node_inde].Nodes[1].Nodes.Add(can_Network.can_nodes[node_inde].rx_can_Messages[txmsg_inde].message_name);
                        for (int signal_inde = 0; signal_inde < can_Network.can_nodes[node_inde].rx_can_Messages[txmsg_inde].signals.Length; signal_inde++)
                        {
                            tv_rbs.Nodes[i].Nodes[dbc_index].Nodes[node_inde].Nodes[1].Nodes[txmsg_inde].Nodes.Add(can_Network.can_nodes[node_inde].rx_can_Messages[txmsg_inde].signals[signal_inde]);
                        }
                    }
                }
            }
            dbc_index++;
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
        private void btn_load_candb_Click(object sender, EventArgs e)
        {
            OpenFileDialog dialog = new OpenFileDialog();
            dialog.Filter = "(*.dbc)|*.dbc|(*.pdbc)|*.pdbc";
            if (dialog.ShowDialog() == DialogResult.OK)
            {
                int ret = TsMasterApi.tsdb_load_can_db(dialog.FileName, "0,1,2,3", ref DBAId);
                if (ret == 0)
                {
                    log("加载成功" + "\r\n");
                    load_dbc_form(DBAId);
                    //thread.Start(DBAId);
                }
            }
        }

        delegate void lvadd(ListViewItem item);

        public void lv_add(ListViewItem item)
        {
            try
            {
                if (lv_showmsg.InvokeRequired == false)
                {

                    lv_showmsg.Items.Add(item);
                    this.lv_showmsg.EnsureVisible(this.lv_showmsg.Items.Count - 1);
                    this.lv_showmsg.Items[this.lv_showmsg.Items.Count - 1].Checked = true;

                }
                else
                {

                    lvadd LVadd = new lvadd(lv_add);
                    lv_showmsg.Invoke(LVadd, item);


                }
            }
            catch (Exception ex) { }
        }
        delegate void lvdel();

        public void lv_del()
        {
            try
            {
                if (lv_showmsg.InvokeRequired == false)
                {
                    //lv_showmsg.Items.RemoveAt(0);
                    lv_showmsg.Items.Clear();
                }
                else
                {
                    lvdel LVdel = new lvdel(lv_del);
                    lv_showmsg.Invoke(LVdel);
                }
            }
            catch { }
        }
        bool thread_stop = false;
        bool thread_start = true;
        public void lvupdate()
        {
            while (thread_start)
            {
                int size = Item_list.Count;
                for (int i = 0; i < size; i++)
                {
                    lv_add(Item_list[i]);
                    if (lv_showmsg.Items.Count >= 1000)
                    {
                        lv_del();
                    }
                }
                if (_isconnect)
                    Item_list.RemoveRange(0, size);
                Thread.Sleep(10);

            }
            thread_stop = true;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            //timer1.Stop();
            //int size = Item_list.Count;
            //if(size>1000)
            //{ 
            //    size = 1000; 
            //}
            //for (int i = 0; i < size; i++)
            //{
            //    if (Item_list.Count == 0)
            //        return;
            //    lv_showmsg.Items.Add(Item_list[i]);
            //    this.lv_showmsg.EnsureVisible(this.lv_showmsg.Items.Count - 1);
            //    this.lv_showmsg.Items[this.lv_showmsg.Items.Count - 1].Checked = true;
            //    if (lv_showmsg.Items.Count >= 1000)
            //    {
            //        lv_showmsg.Items.RemoveAt(0);
            //    }
            //}
            //if (size !=0)
            //    Item_list.RemoveRange(0, size);
            ////timer1.Start();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            lv_showmsg.Items.Clear();
            msg_count = 0;
        }

        private void btn_send_one_msg_Click(object sender, EventArgs e)
        {
            if (btn_on_off.Text == "连接")
            {
                btn_on_off_Click(sender, e);
            }
            if (btn_on_off.Text == "连接")
            {
                MessageBox.Show("请确认硬件是否配置成功");
                return;
            }
            TLIBCAN ACAN = new TLIBCAN(0, 0X1, true, false, false, 8, new byte[] { 1, 2, 3, 4, 5, 6, 7, 8 });
            TsMasterApi.tsapp_transmit_can_async(ref ACAN);

            TLIBCANFD ACANFD = new TLIBCANFD(0, 0X2, true, false, false, 8, new byte[] { 1, 2, 3, 4, 5, 6, 7, 8 });
            TsMasterApi.tsapp_transmit_canfd_async(ref ACANFD);


        }

        private void btn_cyclic_msg_Click(object sender, EventArgs e)
        {
            if (!_isconnect)
                btn_on_off_Click(sender, e);
            if (!_isconnect)
            {
                MessageBox.Show("请确认硬件是否配置成功");
                return;
            }
            TLIBCAN ACAN = new TLIBCAN(0, 0X3, true, false, false, 8, new byte[] { 1, 2, 3, 4, 5, 6, 7, 8 });
            TsMasterApi.tsapp_add_cyclic_msg_can(ref ACAN, 100);

            TLIBCANFD ACANFD = new TLIBCANFD(0, 0X4, true, false, false, 8, new byte[] { 1, 2, 3, 4, 5, 6, 7, 8 });
            TsMasterApi.tsapp_add_cyclic_msg_canfd(ref ACANFD, 100);
        }

        private void cbb_msg_names_SelectedIndexChanged(object sender, EventArgs e)
        {
            cbb_signals.Items.Clear();
            for (int index = 0; index < dbc_parse.msg_[cbb_msg_names.SelectedIndex].signal_Name.Length; index++)
            {
                cbb_signals.Items.Add(dbc_parse.msg_[cbb_msg_names.SelectedIndex].signal_Name[index]);
            }
            if (cbb_signals.Items.Count > 0)
                cbb_signals.SelectedIndex = 0;
        }

        private void btn_send_signal_Click(object sender, EventArgs e)
        {
            if (!_isconnect)
                btn_on_off_Click(sender, e);
            if (!_isconnect)
            {
                MessageBox.Show("请确认硬件是否配置成功");
                return;
            }
            if (cbb_msg_names.Text.Trim().Length > 0) {
                _Msg_ temp = dbc_parse.msg_[cbb_msg_names.SelectedIndex];
                if (dbc_parse.msg_[cbb_msg_names.SelectedIndex].msg_cyclic != 0)
                {
                    //
                    if (cbb_signals.Text.Trim().Length > 0 && tb_signal_value.Text.Trim().Length > 0)
                        TsMasterApi.tsdb_set_signal_value_canfd(ref temp.ACANFD, cbb_msg_names.Text, cbb_signals.Text, double.Parse(tb_signal_value.Text));
                    dbc_parse.msg_[cbb_msg_names.SelectedIndex] = temp;
                    TsMasterApi.tsapp_add_cyclic_msg_canfd(ref temp.ACANFD, temp.msg_cyclic);
                }
                else
                {
                    if (cbb_signals.Text.Trim().Length > 0 && tb_signal_value.Text.Trim().Length > 0)
                        TsMasterApi.tsdb_set_signal_value_canfd(ref temp.ACANFD, cbb_msg_names.Text, cbb_signals.Text, double.Parse(tb_signal_value.Text));
                    dbc_parse.msg_[cbb_msg_names.SelectedIndex] = temp;
                    TsMasterApi.tsapp_transmit_canfd_async(ref temp.ACANFD);
                }
            }
        }

        private void btn_stop_signal_Click(object sender, EventArgs e)
        {
            _Msg_ temp = dbc_parse.msg_[cbb_msg_names.SelectedIndex];
            TsMasterApi.tsapp_delete_cyclic_msg_canfd(ref temp.ACANFD);
        }

        IntPtr readblfhandle = IntPtr.Zero;
        int readcount = 0;
        string blf_name = "";
        private void btn_load_blf_Click(object sender, EventArgs e)
        {
            OpenFileDialog dialog = new OpenFileDialog();
            dialog.Filter = "(*.blf)|*.blf|(*.*)|*.*";
            if (dialog.ShowDialog() == DialogResult.OK)
            {
                int ret = TsMasterApi.tslog_blf_read_start(dialog.FileName, ref readblfhandle, ref readcount);
                if (ret != 0)
                {
                    MessageBox.Show("load db failed");
                }
                else
                {
                    blf_name = dialog.FileName;
                    log(dialog.FileName + "载入成功\r\n");
                    TsMasterApi.tslog_blf_read_end(readblfhandle);
                }

            }
        }
        //BLF 转 asc
        static void readProgress(ref int obj, double AProgress100)
        {
            
        }
        TReadProgressCallback readProgressCallback = readProgress;


        private void button2_Click(object sender, EventArgs e)
        {
            OpenFileDialog dlg = new OpenFileDialog();
            dlg.Multiselect = true;
            dlg.DefaultExt = ".blf";
            dlg.Filter = "(*.blf)|*.blf";
            bool flag = dlg.ShowDialog() == DialogResult.OK;
            if (flag)
            {
                //string blfnames = string.Join(",", dlg.FileNames);
                log("加载完成\r\n 开始转换\r\n");
                for (int i = 0; i < dlg.FileNames.Length; i++)
                {
                    int obj1 = 0;
                    string data = dlg.FileNames[i].Substring(0, dlg.FileNames[i].LastIndexOf('.')) + ".asc";
                    TsMasterApi.tslog_blf_to_asc(ref obj1, dlg.FileNames[i], dlg.FileNames[i].Substring(0, dlg.FileNames[i].LastIndexOf('.'))+"asc", readProgressCallback);
                }
            }
        }

        private void btn_load_dll_Click(object sender, EventArgs e)
        {
            OpenFileDialog dialog = new OpenFileDialog();
            dialog.Filter = "(*.dll)|*.dll";
            if (dialog.ShowDialog() == DialogResult.OK)
            {
                DLL_Load.load_seed_key(dialog.FileName);
            }
        }

        private void btn_test_Click(object sender, EventArgs e)
        {
            byte[] datas = { 0x1, 2, 3, 4 };
            byte[] data = new byte[4];
            int size = 10;
            unsafe {
                fixed (byte* ptr = datas, ptr2 = data)
                {

                    DLL_Load.key_handle(ptr, 4, 1, "", ptr2, 10, ref size);

                }
            }
        }

        bool is_create_uds = false;

        private void button4_Click(object sender, EventArgs e)
        {
            if (!is_create_uds)
            {
                MessageBox.Show("请先创建诊断模块");
                return;
            }
            if (DLL_Load.key_handle == null)
            {
                MessageBox.Show("请先载入seed&key.dll");
                return;
            }
            int level = (2 * cbb_safe_level.SelectedIndex + 1);
            byte[] resdata = new byte[32];
            byte[] keydata = new byte[32];
            unsafe {
                fixed (byte* res = resdata,key = keydata)
                {   
                    int reslen = resdata.Length;
                    int keylen = keydata.Length;
                    int ret = TsMasterApi.tsdiag_can_security_access_request_seed(udsHandle, level, res, ref reslen);
                    if (0 == ret)
                    {
                        DLL_Load.key_handle(res, (uint)reslen, (uint)level, "", key, (uint)keydata.Length, ref keylen);
                        TsMasterApi.tsdiag_can_security_access_send_key(udsHandle, level + 1, key, keylen);
                    }
                    else
                        MessageBox.Show("get respond failed");
                }
                
            }
        }
        int udsHandle = 0;
        private void btn_uds_id_Click(object sender, EventArgs e)
        {
            if (tb_request_id.Text.Trim().Length > 0 && tb_respond_id.Text.Trim().Length > 0 && tb_function_id.Text.Trim().Length > 0)
            {
                TsMasterApi.tsdiag_can_delete(udsHandle);
                is_create_uds = false;
                bool is_std = (cbb_datatype.SelectedIndex == 0);
                uint request_id = (uint)Convert.ToInt32(tb_request_id.Text.Trim(), 16);
                uint respond_id = (uint)Convert.ToInt32(tb_respond_id.Text.Trim(), 16);
                uint function_id = (uint)Convert.ToInt32(tb_function_id.Text.Trim(), 16);
                if (0 == TsMasterApi.tsdiag_can_create(ref udsHandle, 0, (byte)cbb_msgtype.SelectedIndex, (byte)(cbb_dlc.SelectedIndex + 8), request_id, is_std, respond_id, is_std, function_id, is_std))
                {
                    is_create_uds = true;
                }
            }
        }


        byte[] HexStringSToByteArray(string data_list)
        {
            string[] msg_data_list = data_list.Split(' ');
            byte[] data = new byte[msg_data_list.Length];
            for (int i = 0; i < msg_data_list.Length; i++)
            {
                data[i] = Convert.ToByte(msg_data_list[i],16);
            }
            return data;
        }

        private void btn_send_uds_msg_Click(object sender, EventArgs e)
        {
            if (!is_create_uds)
            {
                MessageBox.Show("请先创建诊断模块");
                return;
            }
            if (tb_uds_msg_data.Text.Trim().Length > 0)
            {
                byte[] data = HexStringSToByteArray(tb_uds_msg_data.Text.Trim());
                byte[] msg = new byte[1000];
                int size = msg.Length;
                unsafe
                {
                    fixed (byte* req = data, res = msg)
                    {
                        TsMasterApi.tstp_can_request_and_get_response(udsHandle, req, data.Length, res, ref size);
                    }
                }
                
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            OpenFileDialog dlg = new OpenFileDialog();
            dlg.Multiselect = true;
            dlg.DefaultExt = ".asc";
            dlg.Filter = "(*.asc)|*.asc";
            bool flag = dlg.ShowDialog() == DialogResult.OK;
            if (flag)
            {
                //string blfnames = string.Join(",", dlg.FileNames);
                log("加载完成\r\n 开始转换\r\n");
                for (int i = 0; i < dlg.FileNames.Length; i++)
                {
                    int obj1 = 0;
                    string data = dlg.FileNames[i].Substring(0, dlg.FileNames[i].LastIndexOf('.')) + ".asc";
                    TsMasterApi.tslog_blf_to_asc(ref obj1, dlg.FileNames[i], dlg.FileNames[i].Substring(0, dlg.FileNames[i].LastIndexOf('.')) + "blf", readProgressCallback);
                }
            }
        }

        private void TSMaster_CAN_Form_Resize(object sender, EventArgs e)
        {
            float newx = (this.Width) / x;//窗体宽度缩放比例
            float newy = (this.Height) / y;//窗体高度缩放比例
            setControls(newx, newy, this);
            //this.Resize += new EventHandler(Form1_Resize);//窗体调整大小时引发事件
        }


        private void tv_rbs_AfterCheck(object sender, TreeViewEventArgs e)
        {
            TreeNode node = e.Node;
            
            switch (node.Level)
            {
                case (int)NodeLevel.NetWork:
                    {
                        TsMasterApi.tscom_can_rbs_activate_network_by_name(node.Parent.Index, node.Checked, node.Text, false);
                        break;
                    }
                case (int)NodeLevel.Node:
                    {
                        TsMasterApi.tscom_can_rbs_activate_node_by_name(node.Parent.Parent.Index, node.Checked, node.Parent.Text, node.Text, false);
                        break;
                    }
                case (int)NodeLevel.Message:
                    {
                        TsMasterApi.tscom_can_rbs_activate_message_by_name(node.Parent.Parent.Parent.Parent.Index, node.Checked, node.Parent.Parent.Parent.Text, node.Parent.Parent.Text, node.Text);
                        break;
                    }
            }
        }

        private void tm_all_select_Click(object sender, EventArgs e)
        {
            TreeNode node = tv_rbs.SelectedNode;
            if (node != null)
            {
                switch (node.Level)
                {
                    case (int)NodeLevel.NetWork:
                        {
                            foreach (TreeNode second_child in node.Nodes)
                            {
                                second_child.Checked = true;
                                foreach (TreeNode three_child in second_child.Nodes)
                                    foreach (TreeNode four_child in three_child.Nodes)
                                        four_child.Checked = true;
                            }
                            break;
                        }
                    case (int)NodeLevel.Node:
                        {
                           
                            foreach (TreeNode three_child in node.Nodes)
                                foreach (TreeNode four_child in three_child.Nodes)
                                    four_child.Checked = true;
                            break;
                        }
                }
            }
        }

        private void tm_all_not_select_Click(object sender, EventArgs e)
        {
            TreeNode node = tv_rbs.SelectedNode;
            if (node != null)
            {
                switch (node.Level)
                {
                    case (int)NodeLevel.NetWork:
                        {
                            foreach (TreeNode second_child in node.Nodes)
                            {
                                second_child.Checked = false;
                                foreach (TreeNode three_child in second_child.Nodes)
                                    foreach (TreeNode four_child in three_child.Nodes)
                                        four_child.Checked = false;
                            }
                            break;
                        }
                    case (int)NodeLevel.Node:
                        {

                            foreach (TreeNode three_child in node.Nodes)
                                foreach (TreeNode four_child in three_child.Nodes)
                                    four_child.Checked = false;
                            break;
                        }
                }
            }
        }

        private void tv_rbs_Click(object sender, EventArgs e)
        {
            //TreeNode node = tv_rbs.SelectedNode;
            //if (node != null)
            //{
            //    if (node.Level == (int)NodeLevel.Signal)
            //    {
            //        lb_ASignaladdress.Text = node.Parent.Parent.Parent.Parent.Text + "/" + node.Parent.Parent.Parent.Text + "/" + node.Parent.Text + "/" + node.Text;

            //    }
            //}
            
        }

        private void tv_rbs_DoubleClick(object sender, EventArgs e)
        {
            TreeNode node = tv_rbs.SelectedNode;
            if (node != null)
            {
                if (node.Level == (int)NodeLevel.Signal)
                {
                    lb_ASignaladdress.Text = node.Parent.Parent.Parent.Parent.Parent.Index.ToString() + "/" + node.Parent.Parent.Parent.Parent.Text + "/" + node.Parent.Parent.Parent.Text + "/" + node.Parent.Text + "/" + node.Text;

                }
            }
        }

        private void btn_get_signal_value_Click(object sender, EventArgs e)
        {
            
            if (lb_ASignaladdress.Text.Trim().Length > 0)
            {
                try
                {
                    double value = 0;
                    TsMasterApi.tscom_can_rbs_get_signal_value_by_address(lb_ASignaladdress.Text, ref value);
                    tb_read_write.Text = value.ToString();
                }
                catch (Exception ex)
                {
                    //MessageBox.Show("input digital type");
                }
            }
        }

        private void btn_set_signal_value_Click(object sender, EventArgs e)
        {
            if (lb_ASignaladdress.Text.Trim().Length > 0 && tb_read_write.Text.Trim().Length > 0)
            {
                try
                {
                    double value = double.Parse(tb_read_write.Text.Trim());
                    TsMasterApi.tscom_can_rbs_set_signal_value_by_address(lb_ASignaladdress.Text, value);
                }
                catch (Exception ex)
                {
                    MessageBox.Show("input digital type");
                }
            }
        }

        private void timer1_Tick_1(object sender, EventArgs e)
        {
            int size = Item_list.Count;
            for (int i = 0; i < size; i++)
            {
                if (Item_list.Count != 0)
                {
                    lv_add(Item_list[i]);
                    if (lv_showmsg.Items.Count >= 1000)
                    {
                        lv_del();
                    }
                }
            }
            if (_isconnect)
            {
                if (Item_list.Count != 0)
                    Item_list.RemoveRange(0, size);
            }
        }

        private void btn_pilter_Click(object sender, EventArgs e)
        {
            channel_p = byte.Parse(tb_channel_pass.Text.Trim());
            id_p = int.Parse(tb_id_pass.Text.Trim());
        }
    }
}
