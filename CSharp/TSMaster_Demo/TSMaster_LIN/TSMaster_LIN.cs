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

namespace TSMaster_LIN
{
    public partial class TSMaster_LIN : Form
    {
        public TSMaster_LIN()
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
        string appname = "TSMaster_LIN";
        TLINQueueEvent_Win32 LINQueueEvent;

        private void TSMaster_LIN_Load(object sender, EventArgs e)
        {
            x = this.Width; y = this.Height;
            setTag(this);
            TsMasterApi.initialize_lib_tsmaster(appname);
            LINQueueEvent = onrxtx_event;
        }

        private void TSMaster_LIN_Resize(object sender, EventArgs e)
        {
            float newx = (this.Width) / x;//窗体宽度缩放比例
            float newy = (this.Height) / y;//窗体高度缩放比例
            setControls(newx, newy, this);
        }
        int cancount = 0; int lincount = 1;
        private void btn_hw_config_Click(object sender, EventArgs e)
        {
            //当前示例设置CAN 2个通道
            TsMasterApi.tsapp_set_can_channel_count(cancount);
            TsMasterApi.tsapp_set_lin_channel_count(lincount);

            //通道映射
            //更换其他同星产品 只需修改第6个参数
            TsMasterApi.tsapp_set_mapping_verbose(appname, TLIBApplicationChannelType.APP_LIN, (int)APP_CHANNEL.CHN1, "TC1016", TLIBBusToolDeviceType.TS_USB_DEVICE, (int)TLIB_TS_Device_Sub_Type.TC1016, 0, (int)APP_CHANNEL.CHN1,true);
            TsMasterApi.tsapp_configure_baudrate_lin(0, (float)19.2,(int)LIN_PROTOCOL.LIN_PROTOCOL_21);
        }
        bool _isconnect = false;
        int obj = 0;
        List<ListViewItem> Item_list = new List<ListViewItem>();
        UInt32 msg_count = 0;
        byte channel_p = 0;
        int id_p = 0;
        void onrxtx_event(ref int obj, ref TLIBLIN ALIN)
        {
            if (channel_p != 0 && channel_p != (ALIN.FIdxChn + 1))
                return;
            if (id_p != 0 && id_p != ALIN.FIdentifier)
                return;
            ListViewItem Item = new ListViewItem();
            msg_count++;
            Item.Text = msg_count.ToString();
            Item.SubItems.Add(((ALIN.FIdxChn.ToString())));
            Item.SubItems.Add(((double)ALIN.FTimeUS / 1000000).ToString());
            Item.SubItems.Add(ALIN.FIdentifier.ToString("X8"));
            Item.SubItems.Add(ALIN.FIsTx ? "TX" : "RX");
            Item.SubItems.Add(ALIN.FDLC.ToString());
            string text = "";
            for (int i = 0; i < ALIN.FDLC; i++)
            {
                text += ALIN.FData[i].ToString("X2") + " ";
            }

            Item.SubItems.Add(text);
            Item_list.Add(Item);
        }

        private void btn_on_off_Click(object sender, EventArgs e)
        {
            if (btn_on_off.Text == "连接")
            {
                if (0 == TsMasterApi.tsapp_connect())
                {
                    TsMasterApi.tsapp_register_event_lin(ref obj, LINQueueEvent);

                    btn_on_off.Text = "断开";
                    _isconnect = true;
                }
            }
            else
            {
                if (0 == TsMasterApi.tsapp_disconnect())
                {
                    TsMasterApi.tsapp_unregister_event_lin(ref obj, LINQueueEvent);
                    btn_on_off.Text = "连接";

                    _isconnect = false;
                }
            }
        }

        private void btn_show_hw_Click(object sender, EventArgs e)
        {
            TsMasterApi.tsapp_show_tsmaster_window("Hardware",false);
        }

        private void btn_Master_Click(object sender, EventArgs e)
        {
            TsMasterApi.tslin_set_node_functiontype(0, (int)TLINNodeType.T_MasterNode);
        }

        private void btn_slave_Click(object sender, EventArgs e)
        {
            TsMasterApi.tslin_set_node_functiontype(0, TLINNodeType.T_SlaveNode);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            TLIBLIN ALIN = new TLIBLIN(0,0X1,8,true);
            TsMasterApi.tsapp_transmit_lin_async(ref ALIN);
        }

        private void btn_sendrecv_Click(object sender, EventArgs e)
        {
            TLIBLIN ALIN = new TLIBLIN(0, 0X1, 8, false);
            TsMasterApi.tsapp_transmit_lin_async(ref ALIN);
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
    }
}
