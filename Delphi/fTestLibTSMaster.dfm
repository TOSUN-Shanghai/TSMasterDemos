object frmTestLibTSMaster: TfrmTestLibTSMaster
  Left = 0
  Top = 0
  Caption = 'Test TSMaster Library'
  ClientHeight = 641
  ClientWidth = 1227
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Tahoma'
  Font.Style = []
  OnCreate = FormCreate
  OnDestroy = FormDestroy
  TextHeight = 13
  object Splitter1: TSplitter
    Left = 0
    Top = 549
    Width = 1227
    Height = 3
    Cursor = crVSplit
    Align = alBottom
  end
  object page: TPageControl
    Left = 0
    Top = 0
    Width = 1227
    Height = 549
    ActivePage = tsLogger
    Align = alClient
    TabOrder = 0
    object shtApplication: TTabSheet
      Caption = 'Application'
      DesignSize = (
        1219
        521)
      object Label1: TLabel
        Left = 488
        Top = 51
        Width = 82
        Height = 13
        Caption = 'Application Name'
      end
      object Label2: TLabel
        Left = 256
        Top = 114
        Width = 122
        Height = 13
        Caption = 'CAN channel count to set'
      end
      object Label3: TLabel
        Left = 256
        Top = 145
        Width = 117
        Height = 13
        Caption = 'LIN channel count to set'
      end
      object Label4: TLabel
        Left = 832
        Top = 145
        Width = 133
        Height = 13
        Caption = 'LIN channel count retrieved'
      end
      object Label5: TLabel
        Left = 832
        Top = 111
        Width = 138
        Height = 13
        Caption = 'CAN channel count retrieved'
      end
      object btnTurboMode: TSpeedButton
        Left = 24
        Top = 387
        Width = 209
        Height = 25
        AllowAllUp = True
        GroupIndex = 1
        Caption = 'Enable Turbo Mode'
        OnClick = btnTurboModeClick
      end
      object Label18: TLabel
        Left = 256
        Top = 268
        Width = 92
        Height = 13
        Caption = 'CAN channel to set'
      end
      object Label19: TLabel
        Left = 538
        Top = 268
        Width = 78
        Height = 13
        Caption = 'Baudrate (Kbps)'
      end
      object Label22: TLabel
        Left = 488
        Top = 82
        Width = 71
        Height = 13
        Caption = 'Application List'
      end
      object Label23: TLabel
        Left = 256
        Top = 299
        Width = 92
        Height = 13
        Caption = 'CAN channel to set'
      end
      object Label24: TLabel
        Left = 538
        Top = 299
        Width = 55
        Height = 13
        Caption = 'Arb. (Kbps)'
      end
      object Label25: TLabel
        Left = 776
        Top = 299
        Width = 57
        Height = 13
        Caption = 'Data (Kbps)'
      end
      object Label46: TLabel
        Left = 832
        Top = 51
        Width = 312
        Height = 13
        Caption = 
          'Note: Application name is initialized once and cannot be modifie' +
          'd!'
      end
      object Label52: TLabel
        Left = 488
        Top = 20
        Width = 112
        Height = 13
        Caption = 'libTSMaster.dll Location'
      end
      object edtApplication: TEdit
        Left = 584
        Top = 48
        Width = 205
        Height = 21
        Alignment = taCenter
        Anchors = [akLeft, akTop, akRight]
        Color = clSilver
        ReadOnly = True
        TabOrder = 2
        Text = 'LibTSMasterDemo'
      end
      object Button1: TButton
        Left = 256
        Top = 46
        Width = 209
        Height = 25
        Caption = 'Delete Application'
        TabOrder = 1
        OnClick = Button1Click
      end
      object Button2: TButton
        Left = 24
        Top = 46
        Width = 209
        Height = 25
        Caption = 'Add Application'
        TabOrder = 0
        OnClick = Button2Click
      end
      object Button3: TButton
        Left = 24
        Top = 109
        Width = 209
        Height = 25
        Caption = 'Set Application CAN Count'
        TabOrder = 6
        OnClick = Button3Click
      end
      object Button4: TButton
        Left = 24
        Top = 140
        Width = 209
        Height = 25
        Caption = 'Set Application LIN Count'
        TabOrder = 8
        OnClick = Button4Click
      end
      object Button5: TButton
        Left = 24
        Top = 201
        Width = 209
        Height = 25
        Caption = 'Set Application Channel 1 Mapping'
        TabOrder = 14
        OnClick = Button5Click
      end
      object Button6: TButton
        Left = 24
        Top = 325
        Width = 209
        Height = 25
        Caption = 'Connect Application'
        TabOrder = 27
        OnClick = Button6Click
      end
      object Button7: TButton
        Left = 256
        Top = 325
        Width = 209
        Height = 25
        Caption = 'Disconnect Application'
        TabOrder = 28
        OnClick = Button7Click
      end
      object edtCANChannelCountSet: TEdit
        Left = 400
        Top = 111
        Width = 121
        Height = 21
        TabOrder = 7
        Text = '2'
      end
      object edtLINChannelCountSet: TEdit
        Left = 400
        Top = 142
        Width = 121
        Height = 21
        TabOrder = 9
        Text = '0'
      end
      object Button9: TButton
        Left = 256
        Top = 77
        Width = 209
        Height = 25
        Caption = 'Get Application List'
        TabOrder = 4
        OnClick = Button9Click
      end
      object edtApplicationList: TEdit
        Left = 584
        Top = 79
        Width = 605
        Height = 21
        Anchors = [akLeft, akTop, akRight]
        ReadOnly = True
        TabOrder = 5
      end
      object edtLINChannelCountGet: TEdit
        Left = 976
        Top = 142
        Width = 121
        Height = 21
        TabOrder = 13
        Text = '2'
      end
      object edtCANChannelCountGet: TEdit
        Left = 976
        Top = 108
        Width = 121
        Height = 21
        TabOrder = 11
        Text = '2'
      end
      object Button10: TButton
        Left = 584
        Top = 140
        Width = 209
        Height = 25
        Caption = 'Get Application LIN Count'
        TabOrder = 12
        OnClick = Button10Click
      end
      object Button11: TButton
        Left = 584
        Top = 109
        Width = 209
        Height = 25
        Caption = 'Get Application CAN Count'
        TabOrder = 10
        OnClick = Button11Click
      end
      object Button12: TButton
        Left = 24
        Top = 232
        Width = 209
        Height = 25
        Caption = 'Set Application Channel 2 Mapping'
        TabOrder = 16
        OnClick = Button12Click
      end
      object Panel1: TPanel
        Left = 256
        Top = 201
        Width = 933
        Height = 25
        Anchors = [akLeft, akTop, akRight]
        TabOrder = 15
        object Label6: TLabel
          Left = 16
          Top = 6
          Width = 66
          Height = 13
          Caption = 'Channel Type'
        end
        object Label7: TLabel
          Left = 296
          Top = 5
          Width = 59
          Height = 13
          Caption = 'Device Type'
        end
        object Label8: TLabel
          Left = 520
          Top = 6
          Width = 80
          Height = 13
          Caption = 'Device Sub Type'
        end
        object Label9: TLabel
          Left = 752
          Top = 6
          Width = 120
          Height = 13
          Caption = 'Hardware Channel Index'
        end
        object Label44: TLabel
          Left = 173
          Top = 5
          Width = 63
          Height = 13
          Caption = 'Device Index'
        end
        object cbApplicationType1: TComboBox
          Left = 95
          Top = 2
          Width = 60
          Height = 21
          Style = csDropDownList
          ItemIndex = 0
          TabOrder = 0
          Text = 'CAN'
          Items.Strings = (
            'CAN'
            'LIN')
        end
        object cbDeviceType1: TComboBox
          Left = 366
          Top = 2
          Width = 121
          Height = 21
          Style = csDropDownList
          ItemIndex = 2
          TabOrder = 1
          Text = 'Vector XL Device'
          OnChange = cbDeviceType1Change
          Items.Strings = (
            'Unknown'
            'TS Virtual Device'
            'Vector XL Device'
            'TS USB Device')
        end
        object cbDeviceSubType1: TComboBox
          Left = 611
          Top = 2
          Width = 121
          Height = 21
          Style = csDropDownList
          TabOrder = 2
        end
        object cbHWChannel1: TComboBox
          Left = 883
          Top = 2
          Width = 50
          Height = 21
          ItemIndex = 0
          TabOrder = 3
          Text = '0'
          Items.Strings = (
            '0'
            '1'
            '2'
            '3'
            '4'
            '5'
            '6'
            '7')
        end
        object cbDevIndex1: TComboBox
          Left = 246
          Top = 2
          Width = 36
          Height = 21
          ItemIndex = 0
          TabOrder = 4
          Text = '0'
          Items.Strings = (
            '0'
            '1'
            '2'
            '3'
            '4'
            '5'
            '6'
            '7')
        end
      end
      object Panel2: TPanel
        Left = 256
        Top = 232
        Width = 933
        Height = 25
        Anchors = [akLeft, akTop, akRight]
        TabOrder = 17
        object Label10: TLabel
          Left = 16
          Top = 6
          Width = 66
          Height = 13
          Caption = 'Channel Type'
        end
        object Label11: TLabel
          Left = 296
          Top = 5
          Width = 59
          Height = 13
          Caption = 'Device Type'
        end
        object Label12: TLabel
          Left = 520
          Top = 6
          Width = 80
          Height = 13
          Caption = 'Device Sub Type'
        end
        object Label13: TLabel
          Left = 752
          Top = 6
          Width = 120
          Height = 13
          Caption = 'Hardware Channel Index'
        end
        object Label45: TLabel
          Left = 173
          Top = 6
          Width = 63
          Height = 13
          Caption = 'Device Index'
        end
        object cbApplicationType2: TComboBox
          Left = 95
          Top = 2
          Width = 60
          Height = 21
          Style = csDropDownList
          ItemIndex = 0
          TabOrder = 0
          Text = 'CAN'
          Items.Strings = (
            'CAN'
            'LIN')
        end
        object cbDeviceType2: TComboBox
          Left = 366
          Top = 2
          Width = 121
          Height = 21
          Style = csDropDownList
          ItemIndex = 2
          TabOrder = 1
          Text = 'Vector XL Device'
          OnChange = cbDeviceType2Change
          Items.Strings = (
            'Unknown'
            'TS Virtual Device'
            'Vector XL Device'
            'TS USB Device')
        end
        object cbDeviceSubType2: TComboBox
          Left = 611
          Top = 2
          Width = 121
          Height = 21
          Style = csDropDownList
          TabOrder = 2
        end
        object cbHWChannel2: TComboBox
          Left = 883
          Top = 2
          Width = 50
          Height = 21
          ItemIndex = 1
          TabOrder = 3
          Text = '1'
          Items.Strings = (
            '0'
            '1'
            '2'
            '3'
            '4'
            '5'
            '6'
            '7')
        end
        object cbDevIndex2: TComboBox
          Left = 246
          Top = 2
          Width = 36
          Height = 21
          ItemIndex = 0
          TabOrder = 4
          Text = '0'
          Items.Strings = (
            '0'
            '1'
            '2'
            '3'
            '4'
            '5'
            '6'
            '7')
        end
      end
      object Button14: TButton
        Left = 24
        Top = 356
        Width = 209
        Height = 25
        Caption = 'Register Rx Events'
        TabOrder = 29
        OnClick = Button14Click
      end
      object Button15: TButton
        Left = 256
        Top = 356
        Width = 209
        Height = 25
        Caption = 'Unregister Rx Events'
        TabOrder = 30
        OnClick = Button15Click
      end
      object Button16: TButton
        Left = 256
        Top = 387
        Width = 209
        Height = 25
        Caption = 'Read Turbo Mode'
        TabOrder = 31
        OnClick = Button16Click
      end
      object Button19: TButton
        Left = 24
        Top = 418
        Width = 209
        Height = 25
        Caption = 'Show channel mapping window'
        TabOrder = 32
        OnClick = Button19Click
      end
      object Button20: TButton
        Left = 488
        Top = 418
        Width = 209
        Height = 25
        Caption = 'Show TSMaster window'
        TabOrder = 34
        OnClick = Button20Click
      end
      object cbTSMasterWindow: TComboBox
        Left = 728
        Top = 420
        Width = 460
        Height = 21
        Style = csDropDownList
        ItemIndex = 0
        TabOrder = 35
        Text = 'Channel Selection'
        Items.Strings = (
          'Channel Selection'
          'System Messages'
          'Graphics'
          'CAN Statistics'
          'CAN Database'
          'Hardware'
          'Bus Logging'
          'Meter'
          'Bus Playback'
          'CAN / CAN FD Trace'
          'CAN / CAN FD Transmit'
          'LIN Trace'
          'LIN Transmit'
          'LIN Database'
          'TS Channel Mapping'
          'C Script Editor'
          'System Information'
          'Panel'
          'CAN Remaining Bus Simulation'
          'Test System'
          'Mini Program Library'
          'Diagnostics'
          'Calibration'
          'System Variable Management'
          'Measurement Setup'
          'Measurement Filter'
          'Documents'
          'LIN Remaining Bus Simulation'
          'Application Window Host'
          'Automotive File Converter'
          'Symbol Mapping'
          'Stimulation'
          'Parameter Curve'
          'Video Replay'
          'Excel Test Module')
      end
      object Button24: TButton
        Left = 256
        Top = 418
        Width = 209
        Height = 25
        Caption = 'Show hardware configuration window'
        TabOrder = 33
        OnClick = Button24Click
      end
      object Button25: TButton
        Left = 24
        Top = 263
        Width = 209
        Height = 25
        Caption = 'Set CAN channel baudrate'
        TabOrder = 18
        OnClick = Button25Click
      end
      object edtCANChannelBaudrate: TEdit
        Left = 401
        Top = 265
        Width = 121
        Height = 21
        Alignment = taCenter
        TabOrder = 19
        Text = '1'
      end
      object edtBaudrateCAN: TEdit
        Left = 622
        Top = 265
        Width = 121
        Height = 21
        Alignment = taCenter
        TabOrder = 20
        Text = '500'
      end
      object chkTerm120: TCheckBox
        Left = 776
        Top = 267
        Width = 212
        Height = 17
        Caption = 'Install 120 Ohm termination resistor'
        Checked = True
        State = cbChecked
        TabOrder = 21
      end
      object Button26: TButton
        Left = 24
        Top = 77
        Width = 209
        Height = 25
        Caption = 'Get Application Mappings'
        TabOrder = 3
        OnClick = Button26Click
      end
      object Button29: TButton
        Left = 24
        Top = 294
        Width = 209
        Height = 25
        Caption = 'Set CAN FD channel baudrate'
        TabOrder = 22
        OnClick = Button29Click
      end
      object edtCANFDChannelBaudrate: TEdit
        Left = 400
        Top = 296
        Width = 121
        Height = 21
        Alignment = taCenter
        TabOrder = 23
        Text = '1'
      end
      object edtBaudrateCANFDArb: TEdit
        Left = 622
        Top = 296
        Width = 121
        Height = 21
        Alignment = taCenter
        TabOrder = 24
        Text = '500'
      end
      object edtBaudrateCANFDData: TEdit
        Left = 867
        Top = 296
        Width = 121
        Height = 21
        Alignment = taCenter
        TabOrder = 25
        Text = '2000'
      end
      object chkTerm120FD: TCheckBox
        Left = 1008
        Top = 298
        Width = 212
        Height = 17
        Caption = 'Install 120 Ohm termination resistor'
        Checked = True
        State = cbChecked
        TabOrder = 26
      end
      object Button39: TButton
        Left = 24
        Top = 449
        Width = 209
        Height = 25
        Caption = 'Start Logging'
        TabOrder = 36
        OnClick = Button39Click
      end
      object Button40: TButton
        Left = 256
        Top = 449
        Width = 209
        Height = 25
        Caption = 'Stop Logging'
        TabOrder = 37
        OnClick = Button40Click
      end
      object Button50: TButton
        Left = 24
        Top = 170
        Width = 209
        Height = 25
        Caption = 'Get All Hardware Information'
        TabOrder = 38
        OnClick = Button50Click
      end
      object Button52: TButton
        Left = 488
        Top = 449
        Width = 209
        Height = 25
        Caption = 'Show Log Dir'
        TabOrder = 39
        OnClick = Button52Click
      end
      object chkVendor: TCheckBox
        Left = 488
        Top = 329
        Width = 200
        Height = 17
        Caption = 'Enable All Vendors Detection'
        Checked = True
        State = cbChecked
        TabOrder = 40
        OnClick = chkVendorClick
      end
      object Button66: TButton
        Left = 24
        Top = 15
        Width = 209
        Height = 25
        Caption = 'Get default libTSMaster.dll location'
        TabOrder = 41
        OnClick = Button66Click
      end
      object Button67: TButton
        Left = 256
        Top = 15
        Width = 209
        Height = 25
        Caption = 'Set another libTSMaster.dll distribution'
        TabOrder = 42
        OnClick = Button67Click
      end
      object edtLibTSMaster: TEdit
        Left = 640
        Top = 17
        Width = 549
        Height = 21
        Anchors = [akLeft, akTop, akRight]
        TabOrder = 43
      end
      object Button80: TButton
        Left = 256
        Top = 170
        Width = 209
        Height = 25
        Caption = 'Get Software Information'
        TabOrder = 44
        OnClick = Button80Click
      end
    end
    object shtCAN: TTabSheet
      Caption = 'CAN Communication'
      ImageIndex = 1
      object Label14: TLabel
        Left = 304
        Top = 142
        Width = 48
        Height = 13
        Caption = 'Identifier:'
      end
      object Label15: TLabel
        Left = 304
        Top = 173
        Width = 48
        Height = 13
        Caption = 'Identifier:'
      end
      object Label16: TLabel
        Left = 561
        Top = 142
        Width = 66
        Height = 13
        Caption = 'Interval (ms):'
      end
      object Label17: TLabel
        Left = 712
        Top = 142
        Width = 182
        Height = 13
        Caption = 'Interval cannot be smaller than 0.5ms'
      end
      object Label20: TLabel
        Left = 432
        Top = 142
        Width = 43
        Height = 13
        Caption = 'Channel:'
      end
      object Label21: TLabel
        Left = 432
        Top = 173
        Width = 43
        Height = 13
        Caption = 'Channel:'
      end
      object Label26: TLabel
        Left = 432
        Top = 235
        Width = 43
        Height = 13
        Caption = 'Channel:'
      end
      object Label27: TLabel
        Left = 432
        Top = 204
        Width = 43
        Height = 13
        Caption = 'Channel:'
      end
      object Label28: TLabel
        Left = 712
        Top = 204
        Width = 182
        Height = 13
        Caption = 'Interval cannot be smaller than 0.5ms'
      end
      object Label29: TLabel
        Left = 561
        Top = 204
        Width = 66
        Height = 13
        Caption = 'Interval (ms):'
      end
      object Label30: TLabel
        Left = 304
        Top = 235
        Width = 48
        Height = 13
        Caption = 'Identifier:'
      end
      object Label31: TLabel
        Left = 304
        Top = 204
        Width = 48
        Height = 13
        Caption = 'Identifier:'
      end
      object Button13: TButton
        Left = 24
        Top = 13
        Width = 265
        Height = 25
        Caption = 'Transmit CAN Message asynchronously'
        TabOrder = 0
        OnClick = Button13Click
      end
      object Button8: TButton
        Left = 24
        Top = 44
        Width = 265
        Height = 25
        Caption = 'Transmit CAN Message synchronously'
        TabOrder = 1
        OnClick = Button8Click
      end
      object Button17: TButton
        Left = 24
        Top = 106
        Width = 265
        Height = 25
        Caption = 'Transmit CAN FD Message synchronously'
        TabOrder = 3
        OnClick = Button17Click
      end
      object Button18: TButton
        Left = 24
        Top = 75
        Width = 265
        Height = 25
        Caption = 'Transmit CAN FD Message asynchronously'
        TabOrder = 2
        OnClick = Button18Click
      end
      object Button21: TButton
        Left = 24
        Top = 137
        Width = 265
        Height = 25
        Caption = 'Transmit CAN Message periodically'
        TabOrder = 4
        OnClick = Button21Click
      end
      object Button22: TButton
        Left = 24
        Top = 168
        Width = 265
        Height = 25
        Caption = 'Delete periodic CAN Message'
        TabOrder = 8
        OnClick = Button22Click
      end
      object Button23: TButton
        Left = 24
        Top = 261
        Width = 265
        Height = 25
        Caption = 'Delete all periodic CAN Messages'
        TabOrder = 18
        OnClick = Button23Click
      end
      object edtAddPeriodicCAN: TEdit
        Left = 360
        Top = 139
        Width = 65
        Height = 21
        Alignment = taCenter
        TabOrder = 5
        Text = '0x55'
      end
      object edtDelPeriodicCAN: TEdit
        Left = 360
        Top = 170
        Width = 65
        Height = 21
        Alignment = taCenter
        TabOrder = 9
        Text = '0x55'
      end
      object edtCyclicCANPeriod: TEdit
        Left = 641
        Top = 139
        Width = 65
        Height = 21
        Alignment = taCenter
        TabOrder = 7
        Text = '1'
      end
      object edtPeriodicChannel: TEdit
        Left = 488
        Top = 139
        Width = 65
        Height = 21
        Alignment = taCenter
        TabOrder = 6
        Text = '1'
      end
      object edtChnPeriodDelete: TEdit
        Left = 488
        Top = 170
        Width = 65
        Height = 21
        Alignment = taCenter
        TabOrder = 10
        Text = '1'
      end
      object Button30: TButton
        Left = 24
        Top = 199
        Width = 265
        Height = 25
        Caption = 'Transmit CAN FD Message periodically'
        TabOrder = 11
        OnClick = Button30Click
      end
      object edtChnPeriodDeleteFD: TEdit
        Left = 488
        Top = 232
        Width = 65
        Height = 21
        Alignment = taCenter
        TabOrder = 17
        Text = '1'
      end
      object edtPeriodicChannelFD: TEdit
        Left = 488
        Top = 201
        Width = 65
        Height = 21
        Alignment = taCenter
        TabOrder = 13
        Text = '1'
      end
      object edtCyclicCANPeriodFD: TEdit
        Left = 641
        Top = 201
        Width = 65
        Height = 21
        Alignment = taCenter
        TabOrder = 14
        Text = '1'
      end
      object edtDelPeriodicCANFD: TEdit
        Left = 360
        Top = 232
        Width = 65
        Height = 21
        Alignment = taCenter
        TabOrder = 16
        Text = '0x55'
      end
      object edtAddPeriodicCANFD: TEdit
        Left = 360
        Top = 201
        Width = 65
        Height = 21
        Alignment = taCenter
        TabOrder = 12
        Text = '0x55'
      end
      object Button31: TButton
        Left = 24
        Top = 230
        Width = 265
        Height = 25
        Caption = 'Delete periodic CAN FD Message'
        TabOrder = 15
        OnClick = Button31Click
      end
      object GroupBox1: TGroupBox
        Left = 24
        Top = 304
        Width = 682
        Height = 193
        Caption = 'CAN Bus Statistics'
        TabOrder = 19
        object Label32: TLabel
          Left = 224
          Top = 91
          Width = 48
          Height = 13
          Caption = 'Identifier:'
        end
        object Label33: TLabel
          Left = 224
          Top = 122
          Width = 48
          Height = 13
          Caption = 'Identifier:'
        end
        object Label34: TLabel
          Left = 224
          Top = 153
          Width = 48
          Height = 13
          Caption = 'Identifier:'
        end
        object Label35: TLabel
          Left = 427
          Top = 91
          Width = 43
          Height = 13
          Caption = 'Channel:'
        end
        object Label36: TLabel
          Left = 427
          Top = 122
          Width = 43
          Height = 13
          Caption = 'Channel:'
        end
        object Label37: TLabel
          Left = 427
          Top = 153
          Width = 43
          Height = 13
          Caption = 'Channel:'
        end
        object Button32: TButton
          Left = 24
          Top = 24
          Width = 169
          Height = 25
          Caption = 'Enable Bus Statistics'
          TabOrder = 0
          OnClick = Button32Click
        end
        object Button33: TButton
          Left = 224
          Top = 24
          Width = 169
          Height = 25
          Caption = 'Disable Bus Statistics'
          TabOrder = 1
          OnClick = Button33Click
        end
        object Button34: TButton
          Left = 427
          Top = 24
          Width = 169
          Height = 25
          Caption = 'Clear Bus Statistics'
          TabOrder = 2
          OnClick = Button34Click
        end
        object Button35: TButton
          Left = 24
          Top = 55
          Width = 169
          Height = 25
          Caption = 'Get Bus Statistics'
          TabOrder = 3
          OnClick = Button35Click
        end
        object cbBusStatistics: TComboBox
          Left = 427
          Top = 57
          Width = 169
          Height = 21
          Style = csDropDownList
          ItemIndex = 0
          TabOrder = 6
          Text = 'cbsBusLoad'
          Items.Strings = (
            'cbsBusLoad'
            'cbsPeakLoad'
            'cbsFpsStdData'
            'cbsAllStdData'
            'cbsFpsExtData'
            'cbsAllExtData'
            'cbsFpsStdRemote'
            'cbsAllStdRemote'
            'cbsFpsExtRemote'
            'cbsAllExtRemote'
            'cbsFpsErrorFrame'
            'cbsAllErrorFrame')
        end
        object cbBusStatBusType: TComboBox
          Left = 224
          Top = 57
          Width = 73
          Height = 21
          Style = csDropDownList
          ItemIndex = 0
          TabOrder = 4
          Text = 'CAN'
          Items.Strings = (
            'CAN'
            'LIN')
        end
        object Button36: TButton
          Left = 24
          Top = 86
          Width = 169
          Height = 25
          Caption = 'Get CAN FPS'
          TabOrder = 7
          OnClick = Button36Click
        end
        object edtFPSCAN: TEdit
          Left = 280
          Top = 88
          Width = 65
          Height = 21
          Alignment = taCenter
          TabOrder = 8
          Text = '0x55'
        end
        object Button37: TButton
          Left = 24
          Top = 117
          Width = 169
          Height = 25
          Caption = 'Get CAN FD FPS'
          TabOrder = 10
          OnClick = Button37Click
        end
        object edtFPSCANFD: TEdit
          Left = 280
          Top = 119
          Width = 65
          Height = 21
          Alignment = taCenter
          TabOrder = 11
          Text = '0x55'
        end
        object Button38: TButton
          Left = 24
          Top = 148
          Width = 169
          Height = 25
          Caption = 'Get LIN FPS'
          TabOrder = 13
          OnClick = Button38Click
        end
        object edtFPSLIN: TEdit
          Left = 280
          Top = 150
          Width = 65
          Height = 21
          Alignment = taCenter
          TabOrder = 14
          Text = '0x55'
        end
        object cbStatChn: TComboBox
          Left = 320
          Top = 57
          Width = 73
          Height = 21
          Style = csDropDownList
          ItemIndex = 0
          TabOrder = 5
          Text = '1'
          Items.Strings = (
            '1'
            '2'
            '3'
            '4'
            '5'
            '6'
            '7'
            '8')
        end
        object edtFPSCANChn: TEdit
          Left = 483
          Top = 88
          Width = 65
          Height = 21
          Alignment = taCenter
          TabOrder = 9
          Text = '1'
        end
        object edtFPSCANFDChn: TEdit
          Left = 483
          Top = 119
          Width = 65
          Height = 21
          Alignment = taCenter
          TabOrder = 12
          Text = '1'
        end
        object edtFPSLINChn: TEdit
          Left = 483
          Top = 150
          Width = 65
          Height = 21
          Alignment = taCenter
          TabOrder = 15
          Text = '1'
        end
      end
      object btnReceiveCANMsgs: TButton
        Left = 362
        Top = 13
        Width = 265
        Height = 25
        Caption = 'Receive CAN Messages'
        TabOrder = 20
        OnClick = btnReceiveCANMsgsClick
      end
      object btnReceiveCANFDMsgs: TButton
        Left = 362
        Top = 75
        Width = 265
        Height = 25
        Caption = 'Receive CANFD Messages'
        TabOrder = 21
        OnClick = btnReceiveCANFDMsgsClick
      end
    end
    object shtCANDatabase: TTabSheet
      Caption = 'CAN Database'
      ImageIndex = 2
      DesignSize = (
        1219
        521)
      object Label38: TLabel
        Left = 256
        Top = 16
        Width = 62
        Height = 13
        Caption = 'CAN dbc file:'
      end
      object Label39: TLabel
        Left = 256
        Top = 47
        Width = 58
        Height = 13
        Caption = 'CAN dbc Id:'
      end
      object edtDBCFile: TEdit
        Left = 336
        Top = 13
        Width = 845
        Height = 21
        Anchors = [akLeft, akTop, akRight]
        TabOrder = 1
        Text = '.\Data\Demo\Databases\WhlSpeeds.dbc'
      end
      object Button41: TButton
        Left = 32
        Top = 11
        Width = 201
        Height = 25
        Caption = 'Load DBC File'
        TabOrder = 0
        OnClick = Button41Click
      end
      object Button42: TButton
        Left = 32
        Top = 42
        Width = 201
        Height = 25
        Caption = 'Unload DBC File'
        TabOrder = 2
        OnClick = Button42Click
      end
      object edtDBCId: TEdit
        Left = 336
        Top = 44
        Width = 845
        Height = 21
        Alignment = taCenter
        Anchors = [akLeft, akTop, akRight]
        TabOrder = 3
        Text = '1'
      end
      object Button43: TButton
        Left = 32
        Top = 73
        Width = 201
        Height = 25
        Caption = 'Unload all DBC files'
        TabOrder = 4
        OnClick = Button43Click
      end
      object GroupBox2: TGroupBox
        AlignWithMargins = True
        Left = 3
        Top = 110
        Width = 1213
        Height = 408
        Margins.Top = 110
        Align = alClient
        Caption = 'DBC Query'
        TabOrder = 5
        object pnlQuery: TPanel
          Left = 2
          Top = 15
          Width = 1209
          Height = 391
          Align = alClient
          TabOrder = 0
          object Label40: TLabel
            Left = 34
            Top = 7
            Width = 78
            Height = 13
            Caption = 'database index:'
          end
          object Label41: TLabel
            Left = 34
            Top = 34
            Width = 57
            Height = 13
            Caption = 'query type:'
          end
          object Label42: TLabel
            Left = 34
            Top = 61
            Width = 30
            Height = 13
            Caption = 'index:'
          end
          object Label43: TLabel
            Left = 34
            Top = 88
            Width = 50
            Height = 13
            Caption = 'sub index:'
          end
          object cbType: TComboBox
            AlignWithMargins = True
            Left = 151
            Top = 31
            Width = 1054
            Height = 21
            Margins.Left = 150
            Align = alTop
            Style = csDropDownList
            DropDownCount = 32
            ItemIndex = 0
            TabOrder = 1
            Text = 
              'DT_STR_Network_Name = 0                                       # ' +
              #33719#21462#32593#32476#21517#31216
            Items.Strings = (
              
                'DT_STR_Network_Name = 0                                       # ' +
                #33719#21462#32593#32476#21517#31216
              
                'DT_STR_DBC_FileName = 1                                       # ' +
                #33719#21462'dbc'#25991#20214#21517
              
                'DT_INT_Protocol_Type = 2                                      # ' +
                #33719#21462#21327#35758#31867#22411#65292'0=CAN'#12289'1=J1939'
              
                'DT_INT_3 = 3                                                  # ' +
                'unused'
              
                'DT_INT_4 = 4                                                  # ' +
                'unused'
              
                'DT_INT_5 = 5                                                  # ' +
                'unused'
              
                'DT_INT_6 = 6                                                  # ' +
                'unused'
              
                'DT_INT_7 = 7                                                  # ' +
                'unused'
              
                'DT_INT_8 = 8                                                  # ' +
                'unused'
              
                'DT_INT_9 = 9                                                  # ' +
                'unused'
              
                'DT_INT_Signal_List_Count = 10                                 # ' +
                #33719#21462#20449#21495#34920#25968#37327' = db.sgns.count'
              
                'DT_INT_CAN_Message_List_Count = 11                            # ' +
                #33719#21462'CAN'#25253#25991#34920#25968#37327' = db.msgs.count'
              
                'DT_INT_CANFD_Message_List_Count = 12                          # ' +
                #33719#21462'CAN FD'#25253#25991#34920#25968#37327' = db.msgsFD.count'
              
                'DT_INT_CANJ1939_Message_List_Count = 13                       # ' +
                #33719#21462'CAN J1939'#25253#25991#34920#25968#37327' = db.msgsJ1939.count'
              
                'DT_INT_Node_List_Count = 14                                   # ' +
                #33719#21462#33410#28857#34920#25968#37327' = db.nodes.count'
              
                'DT_INT_EnvVar_List_Count = 15                                 # ' +
                #33719#21462#29615#22659#21464#37327#34920#25968#37327' = db.envs.count'
              
                'DT_INT_ValTab_List_Count = 16                                 # ' +
                #33719#21462#21462#20540#34920#25968#37327' = db.valtabs.count'
              
                'DT_INT_17 = 17                                                # ' +
                'unused'
              
                'DT_INT_18 = 18                                                # ' +
                'unused'
              
                'DT_INT_19 = 19                                                # ' +
                'unused'
              
                'DT_INT_Signal_List_Message_ID = 20                            # ' +
                #33719#21462#20449#21495#34920#20013#31532'idx'#20449#21495#25152#22312#30340#25253#25991#26631#35782#31526' db.sgns[idx].message_id'
              
                'DT_INT_Signal_List_Value_Type = 21                            # ' +
                #33719#21462#20449#21495#34920#20013#31532'idx'#20449#21495#20540#31867#22411' 0-'#26080#31526#21495#25972#22411' 1-'#26377#31526#21495#25972#22411' 2-32'#20301#28014#28857' 3-64'#20301#28014#28857
              
                'DT_INT_Signal_List_Is_Motorola = 22                           # ' +
                #33719#21462#20449#21495#34920#20013#31532'idx'#20449#21495#26159#21542#26159'Motorola'#26684#24335#65292'0-Intel'#26684#24335#12289'1-Motorola'#26684#24335
              
                'DT_INT_Signal_List_ValTab_Index = 23                          # ' +
                #33719#21462#20449#21495#34920#20013#31532'idx'#20449#21495#25152#24102#30340#21462#20540#34920#22312#21462#20540#34920#21015#34920#20013#30340#32034#24341
              
                'DT_INT_Signal_List_Mux_Type = 24                              # ' +
                #33719#21462#20449#21495#34920#20013#31532'idx'#20449#21495'Mux'#31867#22411#65292'0-'#26222#36890#20449#21495', 1-multiplexor, 2-multiplexed'#20449#21495
              
                'DT_INT_Signal_List_Mux_Value = 25                             # ' +
                #33719#21462#20449#21495#34920#20013#31532'idx'#20449#21495#20316#20026'multiplexor'#30340#20540
              
                'DT_INT_Signal_List_Layout_Start = 26                          # ' +
                #33719#21462#20449#21495#34920#20013#31532'idx'#20449#21495#22312#25253#25991#20013#30340#36215#22987#20301
              
                'DT_INT_Signal_List_Length = 27                                # ' +
                #33719#21462#20449#21495#34920#20013#31532'idx'#20449#21495#30340#20449#21495#38271#24230
              
                'DT_DBL_Signal_List_Factor = 28                                # ' +
                #33719#21462#20449#21495#34920#20013#31532'idx'#20449#21495#25918#22823#22240#23376
              
                'DT_DBL_Signal_List_Offset = 29                                # ' +
                #33719#21462#20449#21495#34920#20013#31532'idx'#20449#21495#20559#31227#37327
              
                'DT_DBL_Signal_List_InitValue = 30                             # ' +
                #33719#21462#20449#21495#34920#20013#31532'idx'#20449#21495#21021#22987#20540
              
                'DT_DBL_Signal_List_Min = 31                                   # ' +
                #33719#21462#20449#21495#34920#20013#31532'idx'#20449#21495#26368#23567#20540
              
                'DT_DBL_Signal_List_Max = 32                                   # ' +
                #33719#21462#20449#21495#34920#20013#31532'idx'#20449#21495#26368#22823#20540
              
                'DT_STR_Signal_List_Name = 33                                  # ' +
                #33719#21462#20449#21495#34920#20013#31532'idx'#20449#21495#21517#31216
              
                'DT_STR_Signal_List_Unit = 34                                  # ' +
                #33719#21462#20449#21495#34920#20013#31532'idx'#20449#21495#21333#20301
              
                'DT_STR_Signal_List_Comment = 35                               # ' +
                #33719#21462#20449#21495#34920#20013#31532'idx'#20449#21495#27880#37322
              
                'DT_INT_Signal_List_Message_Index = 36                         # ' +
                #33719#21462#20449#21495#34920#20013#31532'idx'#20449#21495#25152#22312#30340#25253#25991#22312#25253#25991#34920#20013#30340#32034#24341' db.msgs[db.sgns[idx].message_idx]'
              
                'DT_INT_Signal_List_Message_Type = 37                          # ' +
                #33719#21462#20449#21495#34920#20013#31532'idx'#20449#21495#25152#22312#30340#25253#25991#30340#31867#22411#65292'0=CAN, 1=CANFD, 2=J1939'
              
                'DT_STR_Signal_List_Struct = 38                                # ' +
                #33719#21462#20449#21495#34920#20013#31532'idx'#20449#21495#20840#37096#23646#24615#65292#36887#21495#20998#38548' db.sgns[idx]'
              
                'DT_INT_39 = 39                                                # ' +
                'unused'
              
                'DT_INT_CAN_Message_List_Type = 40                             # ' +
                #33719#21462'CAN'#25253#25991#34920#20013#31532'idx'#25253#25991#31867#22411#65292'cftStdCAN = 0, cftExtCAN = 1, cftJ1939 = 2, cf' +
                'tStdCANFD = 3, cftExtCANFD = 4'
              
                'DT_INT_CAN_Message_List_DLC = 41                              # ' +
                #33719#21462'CAN'#25253#25991#34920#20013#31532'idx'#25253#25991#25968#25454#38271#24230
              
                'DT_INT_CAN_Message_List_ID = 42                               # ' +
                #33719#21462'CAN'#25253#25991#34920#20013#31532'idx'#25253#25991#26631#35782#31526
              
                'DT_INT_CAN_Message_List_CycleTime = 43                        # ' +
                #33719#21462'CAN'#25253#25991#34920#20013#31532'idx'#25253#25991#21608#26399
              
                'DT_STR_CAN_Message_List_Name = 44                             # ' +
                #33719#21462'CAN'#25253#25991#34920#20013#31532'idx'#25253#25991#21517#31216
              
                'DT_STR_CAN_Message_List_Comment = 45                          # ' +
                #33719#21462'CAN'#25253#25991#34920#20013#31532'idx'#25253#25991#27880#37322
              
                'DT_INT_CAN_Message_List_TX_Node_Index = 46                    # ' +
                #33719#21462'CAN'#25253#25991#34920#20013#31532'idx'#25253#25991#23545#24212#30340#21457#36865#33410#28857#30340#32034#24341
              
                'DT_INT_CAN_Message_List_Owned_Signal_List_Count = 47          # ' +
                #33719#21462'CAN'#25253#25991#34920#20013#31532'idx'#25253#25991#25317#26377#30340#20449#21495#25968#37327' db.msgs[idx].sgns.count'
              
                'DT_INT_CAN_Message_List_Owned_Signal_List_Signal_Index = 48   # ' +
                #33719#21462'CAN'#25253#25991#34920#20013#31532'idx'#25253#25991#20013#31532'subidx'#20449#21495#22312#20449#21495#34920#20013#30340#32034#24341' db.sgns[db.sgns.indexof(db.msg' +
                's[idx].sgns[subidx])]'
              
                'DT_STR_CAN_Message_List_Struct = 49                           # ' +
                #33719#21462'CAN'#25253#25991#34920#20013#31532'idx'#25253#25991#20840#37096#23646#24615#65292#36887#21495#20998#38548' db.msgs[idx]'
              
                'DT_INT_50 = 50                                                # ' +
                'unused'
              
                'DT_INT_51 = 51                                                # ' +
                'unused'
              
                'DT_INT_52 = 52                                                # ' +
                'unused'
              
                'DT_INT_53 = 53                                                # ' +
                'unused'
              
                'DT_INT_54 = 54                                                # ' +
                'unused'
              
                'DT_INT_55 = 55                                                # ' +
                'unused'
              
                'DT_INT_56 = 56                                                # ' +
                'unused'
              
                'DT_INT_57 = 57                                                # ' +
                'unused'
              
                'DT_INT_58 = 58                                                # ' +
                'unused'
              
                'DT_INT_59 = 59                                                # ' +
                'unused'
              
                'DT_INT_CANFD_Message_List_Type = 60                           # ' +
                #33719#21462'CANFD'#25253#25991#34920#20013#31532'idx'#25253#25991#31867#22411#65292'cftStdCAN = 0, cftExtCAN = 1, cftJ1939 = 2, ' +
                'cftStdCANFD = 3, cftExtCANFD = 4'
              
                'DT_INT_CANFD_Message_List_DLC = 61                            # ' +
                #33719#21462'CANFD'#25253#25991#34920#20013#31532'idx'#25253#25991#25968#25454#38271#24230
              
                'DT_INT_CANFD_Message_List_ID = 62                             # ' +
                #33719#21462'CANFD'#25253#25991#34920#20013#31532'idx'#25253#25991#26631#35782#31526
              
                'DT_INT_CANFD_Message_List_CycleTime = 63                      # ' +
                #33719#21462'CANFD'#25253#25991#34920#20013#31532'idx'#25253#25991#21608#26399
              
                'DT_STR_CANFD_Message_List_Name = 64                           # ' +
                #33719#21462'CANFD'#25253#25991#34920#20013#31532'idx'#25253#25991#21517#31216
              
                'DT_STR_CANFD_Message_List_Comment = 65                        # ' +
                #33719#21462'CANFD'#25253#25991#34920#20013#31532'idx'#25253#25991#27880#37322
              
                'DT_INT_CANFD_Message_List_TX_Node_Index = 66                  # ' +
                #33719#21462'CANFD'#25253#25991#34920#20013#31532'idx'#25253#25991#23545#24212#30340#21457#36865#33410#28857#30340#32034#24341
              
                'DT_INT_CANFD_Message_List_Owned_Signal_List_Count = 67        # ' +
                #33719#21462'CANFD'#25253#25991#34920#20013#31532'idx'#25253#25991#25317#26377#30340#20449#21495#25968#37327' db.msgs[idx].sgns.count'
              
                'DT_INT_CANFD_Message_List_Owned_Signal_List_Signal_Index = 68 # ' +
                #33719#21462'CANFD'#25253#25991#34920#20013#31532'idx'#25253#25991#20013#31532'subidx'#20449#21495#22312#20449#21495#34920#20013#30340#32034#24341' db.sgns[db.sgns.indexof(db.m' +
                'sgs[idx].sgns[subidx])]'
              
                'DT_INT_CANFD_Message_List_BRS = 69                            # ' +
                #33719#21462'CANFD'#25253#25991#34920#20013#31532'idx'#25253#25991'BRS'#65292'0-No BRS'#12289'1-BRS'
              
                'DT_STR_CANFD_Message_List_Struct = 70                         # ' +
                #33719#21462'CANFD'#25253#25991#34920#20013#31532'idx'#25253#25991#20840#37096#23646#24615#65292#36887#21495#20998#38548' db.msgs[idx]'
              
                'DT_INT_71 = 71                                                # ' +
                'unused'
              
                'DT_INT_72 = 72                                                # ' +
                'unused'
              
                'DT_INT_73 = 73                                                # ' +
                'unused'
              
                'DT_INT_74 = 74                                                # ' +
                'unused'
              
                'DT_INT_75 = 75                                                # ' +
                'unused'
              
                'DT_INT_76 = 76                                                # ' +
                'unused'
              
                'DT_INT_77 = 77                                                # ' +
                'unused'
              
                'DT_INT_78 = 78                                                # ' +
                'unused'
              
                'DT_INT_79 = 79                                                # ' +
                'unused'
              
                'DT_INT_J1939_Message_List_Type = 80                           # ' +
                #33719#21462'J1939'#25253#25991#34920#20013#31532'idx'#25253#25991#31867#22411#65292'cftStdCAN = 0, cftExtCAN = 1, cftJ1939 = 2, ' +
                'cftStdCANFD = 3, cftExtCANFD = 4'
              
                'DT_INT_J1939_Message_List_DLC = 81                            # ' +
                #33719#21462'J1939'#25253#25991#34920#20013#31532'idx'#25253#25991#25968#25454#38271#24230
              
                'DT_INT_J1939_Message_List_ID = 82                             # ' +
                #33719#21462'J1939'#25253#25991#34920#20013#31532'idx'#25253#25991#26631#35782#31526
              
                'DT_INT_J1939_Message_List_CycleTime = 83                      # ' +
                #33719#21462'J1939'#25253#25991#34920#20013#31532'idx'#25253#25991#21608#26399
              
                'DT_STR_J1939_Message_List_Name = 84                           # ' +
                #33719#21462'J1939'#25253#25991#34920#20013#31532'idx'#25253#25991#21517#31216
              
                'DT_STR_J1939_Message_List_Comment = 85                        # ' +
                #33719#21462'J1939'#25253#25991#34920#20013#31532'idx'#25253#25991#27880#37322
              
                'DT_INT_J1939_Message_List_TX_Node_Index = 86                  # ' +
                #33719#21462'J1939'#25253#25991#34920#20013#31532'idx'#25253#25991#23545#24212#30340#21457#36865#33410#28857#30340#32034#24341
              
                'DT_INT_J1939_Message_List_Owned_Signal_List_Count = 87        # ' +
                #33719#21462'J1939'#25253#25991#34920#20013#31532'idx'#25253#25991#25317#26377#30340#20449#21495#25968#37327' db.msgs[idx].sgns.count'
              
                'DT_INT_J1939_Message_List_Owned_Signal_List_Signal_Index = 88 # ' +
                #33719#21462'J1939'#25253#25991#34920#20013#31532'idx'#25253#25991#20013#31532'subidx'#20449#21495#22312#20449#21495#34920#20013#30340#32034#24341' db.sgns[db.sgns.indexof(db.m' +
                'sgs[idx].sgns[subidx])]'
              
                'DT_STR_J1939_Message_List_Struct = 89                         # ' +
                #33719#21462'CAN'#25253#25991#34920#20013#31532'idx'#25253#25991#20840#37096#23646#24615#65292#36887#21495#20998#38548' db.msgs[idx]'
              
                'DT_INT_90 = 90                                                # ' +
                'unused'
              
                'DT_INT_91 = 91                                                # ' +
                'unused'
              
                'DT_INT_92 = 92                                                # ' +
                'unused'
              
                'DT_INT_93 = 93                                                # ' +
                'unused'
              
                'DT_INT_94 = 94                                                # ' +
                'unused'
              
                'DT_INT_95 = 95                                                # ' +
                'unused'
              
                'DT_INT_96 = 96                                                # ' +
                'unused'
              
                'DT_INT_97 = 97                                                # ' +
                'unused'
              
                'DT_INT_98 = 98                                                # ' +
                'unused'
              
                'DT_INT_99 = 99                                                # ' +
                'unused'
              
                'DT_INT_Node_List_Address = 100                                # ' +
                #33719#21462#33410#28857#34920#20013#31532'idx'#33410#28857#22320#22336#65292#40664#35748#20026'0'
              
                'DT_STR_Node_List_Name = 101                                   # ' +
                #33719#21462#33410#28857#34920#20013#31532'idx'#33410#28857#21517#31216
              
                'DT_STR_Node_List_Comment = 102                                # ' +
                #33719#21462#33410#28857#34920#20013#31532'idx'#33410#28857#27880#37322
              
                'DT_INT_Node_List_TX_CAN_Message_List_Count = 103              # ' +
                #33719#21462#33410#28857#34920#20013#31532'idx'#33410#28857#25152#21457#36865#30340'CAN'#25253#25991#25968#37327' db.nodes[idx].txmsgs.count'
              
                'DT_INT_Node_List_TX_CAN_Message_List_Message_Index = 104      # ' +
                #33719#21462#33410#28857#34920#20013#31532'idx'#33410#28857#25152#21457#36865#30340'subidx'#25253#25991#22312'CAN'#25253#25991#34920#20013#30340#32034#24341' db.msgs[db.msgs.indexof(db.n' +
                'odes[idx].txmsgs[subidx])]'
              
                'DT_INT_Node_List_RX_CAN_Message_List_Count = 105              # ' +
                #33719#21462#33410#28857#34920#20013#31532'idx'#33410#28857#25152#25509#25910#30340'CAN'#25253#25991#25968#37327
              
                'DT_INT_Node_List_RX_CAN_Message_List_Message_Index = 106      # ' +
                #33719#21462#33410#28857#34920#20013#31532'idx'#33410#28857#25152#25509#25910#30340'subidx'#25253#25991#22312'CAN'#25253#25991#34920#20013#30340#32034#24341
              
                'DT_INT_Node_List_TX_FD_Message_List_Count = 107               # ' +
                #33719#21462#33410#28857#34920#20013#31532'idx'#33410#28857#25152#21457#36865#30340'FD'#25253#25991#25968#37327' db.nodes[idx].txmsgs.count'
              
                'DT_INT_Node_List_TX_FD_Message_List_Message_Index = 108       # ' +
                #33719#21462#33410#28857#34920#20013#31532'idx'#33410#28857#25152#21457#36865#30340'subidx'#25253#25991#22312'FD'#25253#25991#34920#20013#30340#32034#24341' db.msgs[db.msgs.indexof(db.no' +
                'des[idx].txmsgs[subidx])]'
              
                'DT_INT_Node_List_RX_FD_Message_List_Count = 109               # ' +
                #33719#21462#33410#28857#34920#20013#31532'idx'#33410#28857#25152#25509#25910#30340'FD'#25253#25991#25968#37327
              
                'DT_INT_Node_List_RX_FD_Message_List_Message_Index = 110       # ' +
                #33719#21462#33410#28857#34920#20013#31532'idx'#33410#28857#25152#25509#25910#30340'subidx'#25253#25991#22312'FD'#25253#25991#34920#20013#30340#32034#24341
              
                'DT_INT_Node_List_TX_J1939_Message_List_Count = 111            # ' +
                #33719#21462#33410#28857#34920#20013#31532'idx'#33410#28857#25152#21457#36865#30340'J1939'#25253#25991#25968#37327' db.nodes[idx].txmsgs.count'
              
                'DT_INT_Node_List_TX_J1939_Message_List_Message_Index = 112    # ' +
                #33719#21462#33410#28857#34920#20013#31532'idx'#33410#28857#25152#21457#36865#30340'subidx'#25253#25991#22312'J1939'#25253#25991#34920#20013#30340#32034#24341' db.msgs[db.msgs.indexof(db' +
                '.nodes[idx].txmsgs[subidx])]'
              
                'DT_INT_Node_List_RX_J1939_Message_List_Count = 113            # ' +
                #33719#21462#33410#28857#34920#20013#31532'idx'#33410#28857#25152#25509#25910#30340'J1939'#25253#25991#25968#37327
              
                'DT_INT_Node_List_RX_J1939_Message_List_Message_Index = 114    # ' +
                #33719#21462#33410#28857#34920#20013#31532'idx'#33410#28857#25152#25509#25910#30340'subidx'#25253#25991#22312'J1939'#25253#25991#34920#20013#30340#32034#24341
              
                'DT_INT_Node_List_TX_Signal_List_Count = 115                   # ' +
                #33719#21462#33410#28857#34920#20013#31532'idx'#33410#28857#25152#21457#36865#30340#20449#21495#25968#37327
              
                'DT_INT_Node_List_TX_Signal_List_Signal_Index = 116            # ' +
                #33719#21462#33410#28857#34920#20013#31532'idx'#33410#28857#25152#21457#36865#30340'subidx'#20449#21495#22312#20449#21495#34920#20013#30340#32034#24341
              
                'DT_INT_Node_List_RX_Signal_List_Count = 117                   # ' +
                #33719#21462#33410#28857#34920#20013#31532'idx'#33410#28857#25152#25509#25910#30340#20449#21495#25968#37327
              
                'DT_INT_Node_List_RX_Signal_List_Signal_Index = 118            # ' +
                #33719#21462#33410#28857#34920#20013#31532'idx'#33410#28857#25152#25509#25910#30340'subidx'#20449#21495#22312#20449#21495#34920#20013#30340#32034#24341
              
                'DT_STR_Node_List_Struct = 119                                 # ' +
                #33719#21462#33410#28857#34920#20013#31532'idx'#33410#28857#20840#37096#23646#24615#65292#36887#21495#20998#38548' db.nodes[idx]'
              
                'DT_INT_120 = 120                                              # ' +
                'unused'
              
                'DT_INT_121 = 121                                              # ' +
                'unused'
              
                'DT_INT_122 = 122                                              # ' +
                'unused'
              
                'DT_INT_123 = 123                                              # ' +
                'unused'
              
                'DT_INT_124 = 124                                              # ' +
                'unused'
              
                'DT_INT_125 = 125                                              # ' +
                'unused'
              
                'DT_INT_126 = 126                                              # ' +
                'unused'
              
                'DT_INT_127 = 127                                              # ' +
                'unused'
              
                'DT_INT_128 = 128                                              # ' +
                'unused'
              
                'DT_INT_129 = 129                                              # ' +
                'unused'
              
                'DT_INT_EnvVar_List_Value_Type = 130                           # ' +
                #33719#21462#29615#22659#21464#37327#34920#20013#31532'idx'#29615#22659#21464#37327#20540#31867#22411#65292'0-'#25972#22411#12289'1-'#28014#28857#12289'2-'#23383#31526#20018#12289'3-'#25968#25454
              
                'DT_DBL_EnvVar_List_MIN = 131                                  # ' +
                #33719#21462#29615#22659#21464#37327#34920#20013#31532'idx'#29615#22659#21464#37327#26368#23567#20540
              
                'DT_DBL_EnvVar_List_MAX = 132                                  # ' +
                #33719#21462#29615#22659#21464#37327#34920#20013#31532'idx'#29615#22659#21464#37327#26368#22823#20540
              
                'DT_DBL_EnvVar_List_Init_Value = 133                           # ' +
                #33719#21462#29615#22659#21464#37327#34920#20013#31532'idx'#29615#22659#21464#37327#21021#22987#20540
              
                'DT_STR_EnvVar_List_Name = 134                                 # ' +
                #33719#21462#29615#22659#21464#37327#34920#20013#31532'idx'#29615#22659#21464#37327#21517#31216
              
                'DT_STR_EnvVar_List_Unit = 135                                 # ' +
                #33719#21462#29615#22659#21464#37327#34920#20013#31532'idx'#29615#22659#21464#37327#21333#20301
              
                'DT_STR_EnvVar_List_Comment = 136                              # ' +
                #33719#21462#29615#22659#21464#37327#34920#20013#31532'idx'#29615#22659#21464#37327#27880#37322
              
                'DT_STR_EnvVar_List_Struct = 137                               # ' +
                #33719#21462#29615#22659#21464#37327#34920#20013#31532'idx'#29615#22659#21464#37327#20840#37096#23646#24615#65292#36887#21495#20998#38548' db.EnvVars[idx]'
              
                'DT_INT_138 = 138                                              # ' +
                'unused'
              
                'DT_INT_139 = 139                                              # ' +
                'unused'
              
                'DT_INT_ValTab_List_Item_List_Count = 140                      # ' +
                #33719#21462#21462#20540#34920#20013#31532'idx'#21462#20540#34920#25152#21253#21547#30340#20540#25968#37327
              
                'DT_INT_ValTab_List_Item_List_Name = 141                       # ' +
                #33719#21462#21462#20540#34920#20013#31532'idx'#21462#20540#34920#21517#31216
              
                'DT_DBL_ValTab_List_Item_List_Value = 142                      # ' +
                #33719#21462#21462#20540#34920#20013#31532'idx'#21462#20540#34920#20013#31532'subidx'#30340#20540
              
                'DT_STR_ValTab_List_Struct = 143                               # ' +
                #33719#21462#21462#20540#34920#20013#31532'idx'#21462#20540#34920#20840#37096#23646#24615#65292#36887#21495#20998#38548' db.ValTabs[idx]')
          end
          object edtSubIdx: TEdit
            AlignWithMargins = True
            Left = 151
            Top = 58
            Width = 1054
            Height = 21
            Margins.Left = 150
            Align = alTop
            Alignment = taCenter
            NumbersOnly = True
            TabOrder = 2
            Text = '0'
          end
          object edtSubSubIdx: TEdit
            AlignWithMargins = True
            Left = 151
            Top = 85
            Width = 1054
            Height = 21
            Margins.Left = 150
            Align = alTop
            Alignment = taCenter
            NumbersOnly = True
            TabOrder = 3
            Text = '0'
          end
          object MMDBCResults: TMemo
            AlignWithMargins = True
            Left = 4
            Top = 141
            Width = 1201
            Height = 246
            Align = alClient
            Font.Charset = ANSI_CHARSET
            Font.Color = clWindowText
            Font.Height = -13
            Font.Name = 'Consolas'
            Font.Style = []
            Lines.Strings = (
              #21462#31532'0'#20010#25968#25454#24211#31532'3'#20010#33410#28857#21457#36865#30340#31532'4'#26465#25253#25991'DLC:'
              '[1] '#39318#20808#21462#24471#25253#25991#22312#25253#25991#24635#21015#34920#20013#30340#32034#24341' idx'
              'if 0 = tsdb_get_can_db_info('
              '  0,   // '#31532'0'#20010#25968#25454#24211
              
                '  DT_INT_Node_List_TX_Message_List_Message_Index, // '#33410#28857#21015#34920#20013#30340#21457#36865#25253#25991#21015 +
                #34920#30340'item'#23646#24615
              '  3,   // '#31532'3'#20010#33410#28857
              '  4,   // '#31532'4'#26465#25253#25991
              '  @p   // '#36820#22238#20540#65292#22343#26159#23383#31526#20018
              ') then begin'
              '  idx := strtointdef(string(ansistring(p)), -1);'
              '  // [2] '#20877#21040#25253#25991#21015#34920#20013#21462#20986#20301#20110'idx'#32034#24341#22788#30340#25253#25991'DLC'#23646#24615
              '  if DBCToolkit_GetDBC('
              '    0,     // '#31532'0'#20010#25968#25454#24211
              '    DT_INT_Message_List_DLC, // '#25253#25991#21015#34920#20013#30340'item'#23646#24615
              '    idx,   // '#31532'idx'#20010#25253#25991
              '    -1,    // '#27492#21442#25968#26080#29992
              '    @p     // '#36820#22238#20540#65292#22343#26159#23383#31526#20018
              '  ) begin'
              '    dlc := strtointdef(string(ansistring(p)), -1);'
              '  end;'
              'end;')
            ParentFont = False
            ReadOnly = True
            ScrollBars = ssVertical
            TabOrder = 5
          end
          object btnQuery: TBitBtn
            AlignWithMargins = True
            Left = 151
            Top = 112
            Width = 1054
            Height = 23
            Margins.Left = 150
            Align = alTop
            Caption = 'Query'
            Default = True
            Glyph.Data = {
              DE010000424DDE01000000000000760000002800000024000000120000000100
              0400000000006801000000000000000000001000000000000000000000000000
              80000080000000808000800000008000800080800000C0C0C000808080000000
              FF0000FF000000FFFF00FF000000FF00FF00FFFF0000FFFFFF00333333333333
              3333333333333333333333330000333333333333333333333333F33333333333
              00003333344333333333333333388F3333333333000033334224333333333333
              338338F3333333330000333422224333333333333833338F3333333300003342
              222224333333333383333338F3333333000034222A22224333333338F338F333
              8F33333300003222A3A2224333333338F3838F338F33333300003A2A333A2224
              33333338F83338F338F33333000033A33333A222433333338333338F338F3333
              0000333333333A222433333333333338F338F33300003333333333A222433333
              333333338F338F33000033333333333A222433333333333338F338F300003333
              33333333A222433333333333338F338F00003333333333333A22433333333333
              3338F38F000033333333333333A223333333333333338F830000333333333333
              333A333333333333333338330000333333333333333333333333333333333333
              0000}
            NumGlyphs = 2
            TabOrder = 4
            OnClick = btnQueryClick
          end
          object edtDBIdx: TEdit
            AlignWithMargins = True
            Left = 151
            Top = 4
            Width = 1054
            Height = 21
            Margins.Left = 150
            Align = alTop
            Alignment = taCenter
            NumbersOnly = True
            TabOrder = 0
            Text = '1'
          end
        end
      end
    end
    object shtOnlineReplay: TTabSheet
      Caption = 'Online Replay'
      ImageIndex = 3
      OnShow = shtOnlineReplayShow
      object GroupBox3: TGroupBox
        AlignWithMargins = True
        Left = 3
        Top = 3
        Width = 1213
        Height = 515
        Align = alClient
        Caption = 'Replay Engines'
        TabOrder = 0
        object Panel3: TPanel
          Left = 2
          Top = 15
          Width = 311
          Height = 498
          Align = alLeft
          TabOrder = 0
          object btnGetOnlineReplayEngines: TButton
            Left = 1
            Top = 26
            Width = 309
            Height = 25
            Align = alTop
            Caption = 'Get Replay Engines'
            TabOrder = 1
            OnClick = btnGetOnlineReplayEnginesClick
          end
          object Button28: TButton
            Left = 1
            Top = 51
            Width = 309
            Height = 25
            Align = alTop
            Caption = 'Get Selected Replay Engine Info'
            TabOrder = 2
            OnClick = Button28Click
          end
          object Button44: TButton
            Left = 1
            Top = 1
            Width = 309
            Height = 25
            Align = alTop
            Caption = 'Add Replay Engine'
            TabOrder = 0
            OnClick = Button44Click
          end
          object Button27: TButton
            Left = 1
            Top = 126
            Width = 309
            Height = 25
            Align = alTop
            Caption = 'Start All Replay Engines'
            TabOrder = 5
            OnClick = Button27Click
          end
          object Button45: TButton
            Left = 1
            Top = 151
            Width = 309
            Height = 25
            Align = alTop
            Caption = 'Pause All Replay Engines'
            TabOrder = 6
            OnClick = Button45Click
          end
          object Button46: TButton
            Left = 1
            Top = 176
            Width = 309
            Height = 25
            Align = alTop
            Caption = 'Stop All Replay Engines'
            TabOrder = 7
            OnClick = Button46Click
          end
          object Button47: TButton
            Left = 1
            Top = 101
            Width = 309
            Height = 25
            Align = alTop
            Caption = 'Delete All Replay Engines'
            TabOrder = 4
            OnClick = Button47Click
          end
          object Button48: TButton
            Left = 1
            Top = 76
            Width = 309
            Height = 25
            Align = alTop
            Caption = 'Delete Selected Replay Engine'
            TabOrder = 3
            OnClick = Button48Click
          end
          object Button49: TButton
            Left = 1
            Top = 201
            Width = 309
            Height = 25
            Align = alTop
            Caption = 'Get Selected Replay Progress (%)'
            TabOrder = 8
            OnClick = Button49Click
          end
        end
        object lstOnlineReplay: TListView
          Left = 313
          Top = 15
          Width = 898
          Height = 498
          Align = alClient
          Columns = <
            item
              Caption = 'Index'
              Width = 40
            end
            item
              Alignment = taCenter
              Caption = 'Name'
              Width = 200
            end
            item
              AutoSize = True
              Caption = 'File Path'
            end>
          HideSelection = False
          ReadOnly = True
          RowSelect = True
          TabOrder = 1
          ViewStyle = vsReport
        end
      end
    end
    object shtMiniProgramLibrary: TTabSheet
      Caption = 'Mini Program Library'
      ImageIndex = 4
      DesignSize = (
        1219
        521)
      object Label48: TLabel
        Left = 480
        Top = 202
        Width = 71
        Height = 13
        Caption = 'Function Name'
      end
      object Label49: TLabel
        Left = 736
        Top = 202
        Width = 84
        Height = 13
        Caption = 'Input Parameters'
      end
      object Label50: TLabel
        Left = 480
        Top = 233
        Width = 71
        Height = 13
        Caption = 'Function Name'
      end
      object Label51: TLabel
        Left = 480
        Top = 264
        Width = 71
        Height = 13
        Caption = 'Function Name'
      end
      object Button53: TButton
        Left = 24
        Top = 11
        Width = 265
        Height = 25
        Caption = 'Load a mp library'
        TabOrder = 0
        OnClick = Button53Click
      end
      object edtMPLibraryFileName: TEdit
        Left = 312
        Top = 13
        Width = 885
        Height = 21
        Anchors = [akLeft, akTop, akRight]
        TabOrder = 1
        Text = '.\Data\MPLibraries\Excel\mExcel.mp'
      end
      object Button54: TButton
        Left = 24
        Top = 42
        Width = 265
        Height = 25
        Caption = 'Unload a mp library'
        TabOrder = 2
        OnClick = Button54Click
      end
      object edtUnloadMPLib: TEdit
        Left = 312
        Top = 44
        Width = 885
        Height = 21
        Anchors = [akLeft, akTop, akRight]
        TabOrder = 3
        Text = 'mExcel'
      end
      object Button55: TButton
        Left = 24
        Top = 73
        Width = 265
        Height = 25
        Caption = 'Unload all mp libraries'
        TabOrder = 4
        OnClick = Button55Click
      end
      object Button56: TButton
        Left = 24
        Top = 104
        Width = 265
        Height = 25
        Caption = 'Run mp library'
        TabOrder = 5
        OnClick = Button56Click
      end
      object edtRunMPLib: TEdit
        Left = 312
        Top = 106
        Width = 885
        Height = 21
        Anchors = [akLeft, akTop, akRight]
        TabOrder = 6
        Text = 'mExcel'
      end
      object Button57: TButton
        Left = 24
        Top = 135
        Width = 265
        Height = 25
        Caption = 'Check mp library is running'
        TabOrder = 7
        OnClick = Button57Click
      end
      object edtCheckMPRun: TEdit
        Left = 312
        Top = 137
        Width = 885
        Height = 21
        Anchors = [akLeft, akTop, akRight]
        TabOrder = 8
        Text = 'mExcel'
      end
      object Button58: TButton
        Left = 24
        Top = 166
        Width = 265
        Height = 25
        Caption = 'Stop mp library'
        TabOrder = 9
        OnClick = Button58Click
      end
      object edtStopMPLib: TEdit
        Left = 312
        Top = 168
        Width = 885
        Height = 21
        Anchors = [akLeft, akTop, akRight]
        TabOrder = 10
        Text = 'mExcel'
      end
      object Button59: TButton
        Left = 312
        Top = 73
        Width = 265
        Height = 25
        Caption = 'Run all mp libraries'
        TabOrder = 11
        OnClick = Button59Click
      end
      object Button60: TButton
        Left = 600
        Top = 73
        Width = 265
        Height = 25
        Caption = 'Stop all mp libraries'
        TabOrder = 12
        OnClick = Button60Click
      end
      object Button61: TButton
        Left = 24
        Top = 197
        Width = 265
        Height = 25
        Caption = 'Call mp function'
        TabOrder = 13
        OnClick = Button61Click
      end
      object edtCallMPFunc: TEdit
        Left = 312
        Top = 199
        Width = 145
        Height = 21
        TabOrder = 14
        Text = 'mExcel'
      end
      object edtCallMPFuncName: TEdit
        Left = 568
        Top = 199
        Width = 145
        Height = 21
        TabOrder = 15
        Text = 'load'
      end
      object edtFuncInputPara: TEdit
        Left = 840
        Top = 199
        Width = 357
        Height = 21
        Anchors = [akLeft, akTop, akRight]
        TabOrder = 16
        Text = '.\Data\Demo\Excels\ExcelDemo.xlsx'
      end
      object Button62: TButton
        Left = 24
        Top = 228
        Width = 265
        Height = 25
        Caption = 'Get function address'
        TabOrder = 17
        OnClick = Button62Click
      end
      object edtFuncGetAddr: TEdit
        Left = 312
        Top = 230
        Width = 145
        Height = 21
        TabOrder = 18
        Text = 'mExcel'
      end
      object edtFuncNameGetAdddr: TEdit
        Left = 568
        Top = 230
        Width = 145
        Height = 21
        TabOrder = 19
        Text = 'load'
      end
      object Button63: TButton
        Left = 24
        Top = 259
        Width = 265
        Height = 25
        Caption = 'Get function prototype'
        TabOrder = 20
        OnClick = Button63Click
      end
      object edtFuncPrototypeName: TEdit
        Left = 312
        Top = 261
        Width = 145
        Height = 21
        TabOrder = 21
        Text = 'mExcel'
      end
      object edtFuncPrototypeFuncName: TEdit
        Left = 568
        Top = 261
        Width = 145
        Height = 21
        TabOrder = 22
        Text = 'load'
      end
      object Button64: TButton
        Left = 890
        Top = 73
        Width = 265
        Height = 25
        Caption = 'Get mp list'
        TabOrder = 23
        OnClick = Button64Click
      end
      object Button65: TButton
        Left = 24
        Top = 290
        Width = 265
        Height = 25
        Caption = 'Get function list'
        TabOrder = 24
        OnClick = Button65Click
      end
      object edtMPFuncList: TEdit
        Left = 312
        Top = 292
        Width = 145
        Height = 21
        TabOrder = 25
        Text = 'mExcel'
      end
    end
    object shtLoggingLibrary: TTabSheet
      Caption = 'Logging'
      ImageIndex = 7
      DesignSize = (
        1219
        521)
      object Label53: TLabel
        Left = 67
        Top = 19
        Width = 117
        Height = 13
        Caption = 'Specify blf log file name:'
      end
      object Label54: TLabel
        Left = 91
        Top = 51
        Width = 93
        Height = 13
        Caption = 'Current file handle:'
      end
      object Button71: TButton
        Left = 8
        Top = 84
        Width = 161
        Height = 25
        Caption = 'Start Logging'
        TabOrder = 0
        OnClick = Button71Click
      end
      object Button72: TButton
        Left = 8
        Top = 115
        Width = 161
        Height = 25
        Caption = 'Adding 10 CAN Frames'
        TabOrder = 1
        OnClick = Button72Click
      end
      object Button73: TButton
        Left = 8
        Top = 271
        Width = 161
        Height = 25
        Caption = 'Stop Logging'
        TabOrder = 2
        OnClick = Button73Click
      end
      object Button74: TButton
        Left = 200
        Top = 84
        Width = 161
        Height = 25
        Caption = 'Start Reading'
        TabOrder = 3
        OnClick = Button74Click
      end
      object Button75: TButton
        Left = 200
        Top = 115
        Width = 161
        Height = 25
        Caption = 'Reading CAN Frames'
        TabOrder = 4
        OnClick = Button75Click
      end
      object Button76: TButton
        Left = 200
        Top = 146
        Width = 161
        Height = 25
        Caption = 'Stop Reading'
        TabOrder = 5
        OnClick = Button76Click
      end
      object Button77: TButton
        Left = 392
        Top = 84
        Width = 161
        Height = 25
        Caption = 'BLF -> ASC'
        TabOrder = 6
        OnClick = Button77Click
      end
      object Button78: TButton
        Left = 392
        Top = 115
        Width = 161
        Height = 25
        Caption = 'ASC -> BLF'
        TabOrder = 7
        OnClick = Button78Click
      end
      object Button79: TButton
        Left = 8
        Top = 178
        Width = 161
        Height = 25
        Caption = 'Adding 10 LIN Frames'
        TabOrder = 8
        OnClick = Button79Click
      end
      object Button81: TButton
        Left = 8
        Top = 209
        Width = 161
        Height = 25
        Caption = 'Adding many CAN LIN Frames'
        TabOrder = 9
        OnClick = Button81Click
      end
      object Button83: TButton
        Left = 8
        Top = 146
        Width = 161
        Height = 25
        Caption = 'Adding 10 CAN FD Frames'
        TabOrder = 10
        OnClick = Button83Click
      end
      object edtBlfFile: TEdit
        Left = 200
        Top = 16
        Width = 989
        Height = 21
        Anchors = [akLeft, akTop, akRight]
        TabOrder = 11
        Text = '.\log1.blf'
      end
      object edtBLFHandle: TEdit
        Left = 200
        Top = 48
        Width = 353
        Height = 21
        Alignment = taCenter
        Enabled = False
        ReadOnly = True
        TabOrder = 12
        Text = '0'
      end
      object edtBlfToASC: TEdit
        Left = 561
        Top = 86
        Width = 353
        Height = 21
        Enabled = False
        ReadOnly = True
        TabOrder = 13
        Text = '.\log1.blf'
      end
      object edtASCToBlf: TEdit
        Left = 561
        Top = 117
        Width = 353
        Height = 21
        Enabled = False
        ReadOnly = True
        TabOrder = 14
        Text = '.\log1.asc'
      end
      object prgConvert: TProgressBar
        AlignWithMargins = True
        Left = 3
        Top = 501
        Width = 1213
        Height = 17
        Align = alBottom
        TabOrder = 15
      end
      object Button82: TButton
        Left = 8
        Top = 240
        Width = 161
        Height = 25
        Caption = 'Adding realtime comment'
        TabOrder = 16
        OnClick = Button82Click
      end
    end
    object shtMisc: TTabSheet
      Caption = 'Miscellaneous'
      ImageIndex = 5
      DesignSize = (
        1219
        521)
      object Button51: TButton
        Left = 16
        Top = 11
        Width = 209
        Height = 70
        Caption = 'Execute Arbitrary Python Code'
        TabOrder = 0
        OnClick = Button51Click
      end
      object MMPython: TMemo
        AlignWithMargins = True
        Left = 240
        Top = 3
        Width = 976
        Height = 89
        Margins.Left = 240
        Align = alTop
        Lines.Strings = (
          'import sys'
          'import win32api, win32con'
          
            'win32api.MessageBox(0, '#39'This is a dialog from python, arguments ' +
            '= '#39' + sys.argv[1] + '#39', '#39' + sys.argv[2], '#39'python dialog'#39', win32co' +
            'n.MB_OK)'
          'print('#39'OK'#39')')
        ScrollBars = ssVertical
        TabOrder = 1
      end
      object MMExcel: TMemo
        AlignWithMargins = True
        Left = 240
        Top = 98
        Width = 976
        Height = 89
        Margins.Left = 240
        Align = alTop
        Lines.Strings = (
          'line1'
          'line2'
          'line3'
          'line4'
          'line5')
        ScrollBars = ssVertical
        TabOrder = 2
      end
      object Button69: TButton
        Left = 16
        Top = 112
        Width = 209
        Height = 25
        Caption = 'Save Excel Content'
        TabOrder = 3
        OnClick = Button69Click
      end
      object Button70: TButton
        Left = 16
        Top = 152
        Width = 209
        Height = 25
        Caption = 'Load Excel Content'
        TabOrder = 4
        OnClick = Button70Click
      end
      object Button84: TButton
        Left = 16
        Top = 224
        Width = 209
        Height = 25
        Caption = 'Get System Var "StatisticsCAN1.StdData"'
        TabOrder = 5
        OnClick = Button84Click
      end
      object GroupBox4: TGroupBox
        Left = 16
        Top = 272
        Width = 1196
        Height = 113
        Anchors = [akLeft, akTop, akRight]
        Caption = 'Vendor Detect Options'
        TabOrder = 6
        object Button85: TButton
          Left = 16
          Top = 32
          Width = 193
          Height = 25
          Caption = 'Get Vendor Detect Options'
          TabOrder = 0
          OnClick = Button85Click
        end
        object Button86: TButton
          Left = 16
          Top = 63
          Width = 193
          Height = 25
          Caption = 'Set Vendor Detect Options'
          TabOrder = 1
          OnClick = Button86Click
        end
        object chkTOSUN: TCheckBox
          Left = 224
          Top = 48
          Width = 75
          Height = 17
          Caption = 'TOSUN'
          Checked = True
          State = cbChecked
          TabOrder = 2
        end
        object chkVector: TCheckBox
          Left = 305
          Top = 48
          Width = 76
          Height = 17
          Caption = 'Vector'
          Checked = True
          State = cbChecked
          TabOrder = 3
        end
        object chkPeak: TCheckBox
          Left = 387
          Top = 48
          Width = 75
          Height = 17
          Caption = 'PEAK'
          TabOrder = 4
        end
        object chkKvaser: TCheckBox
          Left = 468
          Top = 48
          Width = 75
          Height = 17
          Caption = 'Kvaser'
          TabOrder = 5
        end
        object chkZLG: TCheckBox
          Left = 549
          Top = 48
          Width = 76
          Height = 17
          Caption = 'ZLG'
          TabOrder = 6
        end
        object chkIntrepidcs: TCheckBox
          Left = 631
          Top = 48
          Width = 75
          Height = 17
          Caption = 'Intrepidcs'
          TabOrder = 7
        end
        object chkCANable: TCheckBox
          Left = 712
          Top = 48
          Width = 97
          Height = 17
          Caption = 'CANable'
          TabOrder = 8
        end
      end
      object Button87: TButton
        Left = 16
        Top = 193
        Width = 209
        Height = 25
        Caption = 'Get Unique Computer Fingerprint'
        TabOrder = 7
        OnClick = Button87Click
      end
    end
    object shtLINCom: TTabSheet
      Caption = 'LIN Communication'
      ImageIndex = 6
      object grpLINTpLayer: TGroupBox
        Left = 0
        Top = 105
        Width = 1219
        Height = 129
        Align = alTop
        Caption = 'LIN Transport Layer'
        TabOrder = 0
        object lblNAD: TLabel
          Left = 175
          Top = 30
          Width = 21
          Height = 13
          Caption = 'NAD'
        end
        object lblTPExecuteTime: TLabel
          Left = 1146
          Top = 38
          Width = 100
          Height = 13
          Caption = 'TP Execute Time(ms)'
        end
        object Label47: TLabel
          Left = 32
          Top = 32
          Width = 74
          Height = 13
          Caption = 'Tp Internal(ms)'
        end
        object lblDatas: TLabel
          Left = 49
          Top = 61
          Width = 28
          Height = 13
          Caption = 'Datas'
        end
        object btnTPSetIntervalTime: TButton
          Left = 305
          Top = 25
          Width = 200
          Height = 25
          Caption = 'TP_Set_MasterRequest_IntervalTime'
          TabOrder = 0
          OnClick = btnTPSetIntervalTimeClick
        end
        object btnTPResetRequest: TButton
          Left = 715
          Top = 25
          Width = 179
          Height = 25
          Caption = 'Reset Master Request'
          TabOrder = 1
          OnClick = btnTPResetRequestClick
        end
        object btnTpMasterRequest: TButton
          Left = 900
          Top = 24
          Width = 133
          Height = 25
          Caption = 'Tp_Master_Request'
          TabOrder = 2
          OnClick = btnTpMasterRequestClick
        end
        object btnTpResponse: TButton
          Left = 900
          Top = 56
          Width = 133
          Height = 25
          Caption = 'Tp_Master_Response'
          TabOrder = 3
        end
        object edtNAD: TEdit
          Left = 203
          Top = 27
          Width = 79
          Height = 21
          Alignment = taCenter
          TabOrder = 4
          Text = '7F'
        end
        object edtTpIntervalTime: TEdit
          Left = 108
          Top = 27
          Width = 61
          Height = 21
          Alignment = taCenter
          TabOrder = 5
          Text = '100'
        end
        object BtnLINReadDataByID: TButton
          Left = 305
          Top = 56
          Width = 200
          Height = 25
          Caption = 'Read Data By ID'
          TabOrder = 6
          OnClick = btnLINReadDataByIDClick
        end
        object memoLINDatas: TMemo
          Left = 109
          Top = 58
          Width = 173
          Height = 55
          Lines.Strings = (
            'F18C')
          TabOrder = 7
        end
        object btnSetLINDiagSlaveResponseIntervalTime: TButton
          Left = 511
          Top = 25
          Width = 198
          Height = 25
          Caption = 'TP_Set_SlaveResonse_IntervalTime'
          TabOrder = 8
          OnClick = btnSetLINDiagSlaveResponseIntervalTimeClick
        end
        object Button68: TButton
          Left = 305
          Top = 87
          Width = 200
          Height = 25
          Caption = 'Write Data By ID'
          TabOrder = 9
          OnClick = Button68Click
        end
      end
      object grpLINNormalAPI: TGroupBox
        Left = 0
        Top = 0
        Width = 1219
        Height = 105
        Align = alTop
        Caption = 'LIN Normal API'
        TabOrder = 1
        object lblLINBaudrate: TLabel
          Left = 330
          Top = 20
          Width = 74
          Height = 13
          Caption = 'Baudrate(kbps)'
        end
        object lblLINRecallRevCnt: TLabel
          Left = 700
          Top = 22
          Width = 6
          Height = 13
          Caption = '0'
        end
        object lblReadRevLINCnt: TLabel
          Left = 700
          Top = 54
          Width = 6
          Height = 13
          Caption = '0'
        end
        object btnSetAsMasterMode: TButton
          Left = 14
          Top = 15
          Width = 144
          Height = 25
          Caption = 'Set As Master Mode'
          TabOrder = 0
          OnClick = btnSetAsMasterModeClick
        end
        object btnApplyNewLDF: TButton
          Left = 164
          Top = 15
          Width = 160
          Height = 25
          Caption = 'Apply New LDF'
          TabOrder = 1
          OnClick = btnApplyNewLDFClick
        end
        object edtLINBaudrate: TEdit
          Left = 410
          Top = 17
          Width = 95
          Height = 21
          Alignment = taCenter
          TabOrder = 2
          Text = '100'
        end
        object btnSetLINBaudrate: TButton
          Left = 511
          Top = 15
          Width = 154
          Height = 25
          Caption = 'Set LIN Baudrate'
          TabOrder = 3
          OnClick = btnSetLINBaudrateClick
        end
        object btnRegisterFastLIN: TButton
          Left = 14
          Top = 65
          Width = 117
          Height = 25
          Caption = 'Register Fast LIN '
          TabOrder = 4
          OnClick = btnRegisterFastLINClick
        end
        object btnSendTxFrame: TButton
          Left = 137
          Top = 65
          Width = 118
          Height = 25
          Caption = 'Send Tx Frame'
          TabOrder = 5
          OnClick = btnSendTxFrameClick
        end
        object btnSendRxFrame: TButton
          Left = 261
          Top = 65
          Width = 124
          Height = 25
          Caption = 'Send Rx Frame'
          TabOrder = 6
          OnClick = btnSendRxFrameClick
        end
        object btnStartSednMsgThread: TButton
          Left = 391
          Top = 65
          Width = 144
          Height = 25
          Caption = 'Start Send Msg Thread'
          TabOrder = 7
        end
        object btnStopSendMsgThread: TButton
          Left = 541
          Top = 65
          Width = 124
          Height = 25
          Caption = 'Stop Thread'
          TabOrder = 8
        end
        object mmLINMsgs: TMemo
          Left = 874
          Top = 15
          Width = 343
          Height = 88
          Align = alRight
          Lines.Strings = (
            'mmLINMsgs')
          TabOrder = 9
        end
      end
    end
    object tsLogger: TTabSheet
      Caption = 'tsLogger'
      ImageIndex = 8
      object tvDataLogger: TTreeView
        Left = 0
        Top = 0
        Width = 1219
        Height = 521
        Align = alClient
        Indent = 19
        PopupMenu = pm1
        ReadOnly = True
        TabOrder = 0
        Items.NodeData = {
          0301000000280000000000000000000000FFFFFFFFFFFFFFFF00000000000000
          00000000000105460069006C0065007300}
      end
    end
  end
  object MM: TMemo
    Left = 0
    Top = 552
    Width = 1227
    Height = 89
    Align = alBottom
    ReadOnly = True
    ScrollBars = ssVertical
    TabOrder = 1
  end
  object pbPrg: TProgressBar
    Left = 856
    Top = 616
    Width = 150
    Height = 17
    TabOrder = 2
  end
  object pm1: TPopupMenu
    Left = 260
    Top = 120
    object ConnectTLog1: TMenuItem
      Caption = 'Connect TLog'
    end
    object RefreshDataLoggerList1: TMenuItem
      Caption = 'Refresh Data Logger List'
      OnClick = RefreshDataLoggerList1Click
    end
    object StartLoggerReplay1: TMenuItem
      Caption = 'Start Logger Replay'
    end
    object StopLoggerReplay1: TMenuItem
      Caption = 'Stop Logger Replay'
    end
    object EraseLogger1: TMenuItem
      Caption = 'Erase Logger'
    end
    object ExportBlfFile1: TMenuItem
      Caption = 'Export Blf File'
      OnClick = ExportBlfFile1Click
    end
    object ResetGPSModule1: TMenuItem
      Caption = 'Reset GPS Module'
    end
  end
  object dlgSaveBlf: TSaveDialog
    DefaultExt = '*.blf'
    Filter = 'Blf|*.blf'
    Left = 224
    Top = 280
  end
  object LCTime: TTimer
    OnTimer = LCTimeTimer
    Left = 384
    Top = 304
  end
end
