using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;
using TSMaster;

namespace TSMaster_FlexRay
{
    public partial class TSMaster_FlexRay : Form
    {
        public TSMaster_FlexRay()
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



        string AppName = "TSMaster";
        List<ListViewItem> Item_list = new List<ListViewItem>();
        UInt32 msg_count = 0;
        string[] FChannelMask = { " ", "A", "B", "AB" };
        byte channel_p = 0;
        UInt16 slotid_p = 0;
        //byte cycle_p = 0;
        byte base_cycle;
        byte rep_cycle;
        void on_flexray(IntPtr AObj, ref TLIBFlexray AFlexRay)
        {
            if (channel_p != 0 && channel_p != (AFlexRay.FIdxChn + 1))
                return;
            if (slotid_p != 0 && slotid_p != AFlexRay.FSlotId)
                return;
            if ((base_cycle + rep_cycle) != 0 && (AFlexRay.FCycleNumber % rep_cycle != base_cycle))
                return;
            ListViewItem Item = new ListViewItem();
            msg_count++;
            Item.Text = msg_count.ToString();
            Item.SubItems.Add((AFlexRay.FIdxChn+1).ToString()+ FChannelMask[AFlexRay.FChannelMask>3?0: AFlexRay.FChannelMask]);
            Item.SubItems.Add(((double)AFlexRay.FTimeUs / 1000000).ToString());
            Item.SubItems.Add(AFlexRay.FSlotId.ToString());
            Item.SubItems.Add(AFlexRay.FCycleNumber.ToString());
            Item.SubItems.Add(AFlexRay.FDir==1 ? "TX" : "RX");
            Item.SubItems.Add(AFlexRay.FActualPayloadLength.ToString());
            string text = "";
            for (int i = 0; i < AFlexRay.FActualPayloadLength; i++)
            {
                text += AFlexRay.FData[i].ToString("X2") + " ";
            }
            Item.SubItems.Add(text);
            Item_list.Add(Item);
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

        void pre_tx_flexray(IntPtr AObj, ref TLIBFlexray AData)
        {

        }
        TFlexrayQueueEvent flexrayQueueEvent;
        TFlexrayQueueEvent pre_flexrayQueueEvent;
        private void TSMaster_FlexRay_Load(object sender, EventArgs e)
        {
            x = this.Width;
            y = this.Height;
            setTag(this);
            tv_rbs.CheckBoxes = true;
            flexrayQueueEvent = on_flexray;
            pre_flexrayQueueEvent = pre_tx_flexray;
        }
        //判断是否加载工程
        bool is_load_project = false;
        //
        IntPtr on_obj = IntPtr.Zero;
        IntPtr pre_obj = IntPtr.Zero;
        int db_count = 0;
        APP_CHANNEL[] chns = new APP_CHANNEL[] { APP_CHANNEL.CHN1, APP_CHANNEL.CHN2};


        delegate void tb_call(string msg);
        void log(string msg)
        {
            if (tb_msg.InvokeRequired == false)
            {
                tb_msg.AppendText(msg);
            }
            else
            {
                tb_call tb_Call = log;
                tb_msg.Invoke(tb_Call, msg);
            }
        }



        private void btn_loadproject_Click(object sender, EventArgs e)
        {
            FolderBrowserDialog dialog = new FolderBrowserDialog();
            dialog.Description = "请选择文件路径";
            if (dialog.ShowDialog() == DialogResult.OK)
            {
                if (is_load_project)
                {
                    TsMasterApi.finalize_lib_tsmaster();
                    //tv_rbs
                    is_load_project = false;
                }
                //String savePath = dialog.SelectedPath;
                int ret = TsMasterApi.initialize_lib_tsmaster_with_project(AppName, dialog.SelectedPath);

                if (ret == 0)
                {
                    uint AID = 0;
                    TsMasterApi.tsfifo_enable_receive_fifo();
                    TsMasterApi.tsdb_get_flexray_db_count(ref db_count);
                    for (int i = 0; i < db_count; i++)
                    {
                        //load_tree load_ = new load_tree();
                        //load_.dbc_index = i;
                        //load_.chns = chns;
                        //load_.treeView = tv_rbs;
                        //load_.flexray_Network = Flexray_dbParse.db_parse(i);
                        //Thread thread = new Thread(new ParameterizedThreadStart(Flexray_dbParse.load_treeview_thread));
                        //thread.Start(load_);
                        //Flexray_dbParse.load_treeview(i, chns, tv_rbs, Flexray_dbParse.db_parse(i));
                    }
                    is_load_project = true;
                    log("加载成功\r\n");
                }
                else
                {
                    MessageBox.Show(TsMasterApi.tsapp_get_error_description(ret));
                }
            }

        }

        bool _isconnect = false;
        private void btn_on_off_Click(object sender, EventArgs e)
        {
            if (!is_load_project)
            {
                MessageBox.Show("未加载工程");
                return;
            }
            if (btn_on_off.Text == "连接")
            {
                if (0 == TsMasterApi.tsapp_connect())
                {
                    TsMasterApi.tsapp_register_event_flexray(on_obj, flexrayQueueEvent);
                    TsMasterApi.tsapp_register_pretx_event_flexray(pre_obj, pre_flexrayQueueEvent);
                    TsMasterApi.tscom_flexray_rbs_enable(true);
                    TsMasterApi.tscom_flexray_rbs_start();

                    btn_on_off.Text = "断开";
                    _isconnect = true;
                }
            }
            else
            {
                if (0 == TsMasterApi.tsapp_disconnect())
                {

                    TsMasterApi.tscom_flexray_rbs_enable(false);
                    TsMasterApi.tscom_flexray_rbs_stop();
                    TsMasterApi.tsapp_unregister_event_flexray(on_obj, flexrayQueueEvent);
                    TsMasterApi.tsapp_unregister_pretx_event_flexray(pre_obj, pre_flexrayQueueEvent);
                    btn_on_off.Text = "连接";
                    Item_list.Clear();
                    msg_count = 0;
                    _isconnect = false;
                }
            }
        }

        private void TSMaster_FlexRay_Resize(object sender, EventArgs e)
        {
            float newx = (this.Width) / x;//窗体宽度缩放比例
            float newy = (this.Height) / y;//窗体高度缩放比例
            setControls(newx, newy, this);
        }

        private void tv_rbs_AfterCheck(object sender, TreeViewEventArgs e)
        {
            TreeNode node = e.Node;

            switch (node.Level)
            {
                case (int)NodeLevel.NetWork:
                    {
                        TsMasterApi.tscom_flexray_rbs_activate_cluster_by_name(node.Parent.Index, node.Checked, node.Text, false);
                        break;
                    }
                case (int)NodeLevel.Node:
                    {
                        TsMasterApi.tscom_flexray_rbs_activate_ecu_by_name(node.Parent.Parent.Index, node.Checked, node.Parent.Text, node.Text, false);
                        break;
                    }
                case (int)NodeLevel.Message:
                    {
                        TsMasterApi.tscom_flexray_rbs_activate_frame_by_name(node.Parent.Parent.Parent.Parent.Index, node.Checked, node.Parent.Parent.Parent.Text, node.Parent.Parent.Text, node.Text);
                        break;
                    }
            }
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

        private void btn_set_signal_value_Click(object sender, EventArgs e)
        {
            if (lb_ASignaladdress.Text.Trim().Length > 0 && tb_read_write.Text.Trim().Length > 0)
            {
                try
                {
                    double value = double.Parse(tb_read_write.Text.Trim());
                    TsMasterApi.tscom_flexray_rbs_set_signal_value_by_address(lb_ASignaladdress.Text, value);
                }
                catch (Exception ex)
                {
                    MessageBox.Show("input digital type");
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
                    TsMasterApi.tscom_flexray_rbs_get_signal_value_by_address(lb_ASignaladdress.Text, ref value);
                    tb_read_write.Text = value.ToString();
                }
                catch (Exception ex)
                {
                    //MessageBox.Show("input digital type");
                }
            }
        }

        private void TSMaster_FlexRay_FormClosing(object sender, FormClosingEventArgs e)
        {
            if (btn_on_off.Text == "断开")
            {
                if (0 == TsMasterApi.tsapp_disconnect())
                {

                    TsMasterApi.tscom_flexray_rbs_enable(false);
                    TsMasterApi.tscom_flexray_rbs_stop();
                    TsMasterApi.tsapp_unregister_event_flexray(on_obj, flexrayQueueEvent);
                    TsMasterApi.tsapp_unregister_pretx_event_flexray(pre_obj, pre_flexrayQueueEvent);
                    btn_on_off.Text = "连接";
                    Item_list.Clear();
                    msg_count = 0;
                    _isconnect = false;
                }
            }
                TsMasterApi.finalize_lib_tsmaster();
        }

        private void timer1_Tick(object sender, EventArgs e)
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

        private void btn_pilter_Click(object sender, EventArgs e)
        {
            try {
                channel_p = byte.Parse(tb_channel_pass.Text.Trim());
                slotid_p = UInt16.Parse(tb_id_pass.Text.Trim());
                base_cycle = byte.Parse(tb_bc_pass.Text.Trim());
                rep_cycle = byte.Parse(tb_bc_pass.Text.Trim());
            }

            catch (Exception ex){
                MessageBox.Show(ex.Message);
            }

        }

        private void btn_clear_msg_Click(object sender, EventArgs e)
        {
            lv_showmsg.Items.Clear();
        }
        byte[] HexStringSToByteArray(string data_list)
        {
            string[] msg_data_list = data_list.Split(' ');
            byte[] data = new byte[msg_data_list.Length];
            for (int i = 0; i < msg_data_list.Length; i++)
            {
                data[i] = Convert.ToByte(msg_data_list[i], 16);
            }
            return data;
        }
        private void tb_send_flexray_Click(object sender, EventArgs e)
        {
            try
            {
                byte[] data = new byte[byte.Parse(tb_dlc.Text.Trim())];
                if (tb_data.Text.Trim().Length > 0)
                {
                    data = HexStringSToByteArray(tb_data.Text.Trim());
                }
                byte channel = (byte)(((byte.Parse(tb_chn.Text.Trim()) - 1)<0)?0: (byte.Parse(tb_chn.Text.Trim()) - 1));
                 TLIBFlexray AFlexray = new TLIBFlexray(channel, byte.Parse(tb_Mask.Text.Trim()),byte.Parse(tb_dlc.Text.Trim()),(byte)(byte.Parse(tb_bc.Text.Trim())),ushort.Parse(tb_slotid.Text.Trim()),data);
               int ret  = TsMasterApi.tsapp_transmit_flexray_async(ref AFlexray);

            }

            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void btn_hwconfig_Click(object sender, EventArgs e)
        {
            if (!is_load_project)
            {
                MessageBox.Show("未加载工程");
                return;
            }
            TsMasterApi.tsapp_show_tsmaster_window("Hardware",false);
        }

        private void btn_receive_Click(object sender, EventArgs e)
        {
            int buffersize = 100;
            TLIBFlexray[] a = TsMasterApi.ReceiveFRMsgList(ref buffersize, 0, 0);

        }
    }
}
