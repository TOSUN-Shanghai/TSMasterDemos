import xml.etree.ElementTree as ET
class Fibex_parse():
    def __init__(self,xmlpath) -> ET:
        self.Cluster = {}
        self.Frames = {}
        self.Pdus = {}
        self.Triggers = {}
        self.Signals = {}
        self.Codings = {}
        self.Ecus = {}
        self.STATIC_SLOT = 30
        self.tree = ET.parse(xmlpath)
        self.parse(self.tree)
    def parse(self,tree):
        root = tree.getroot()
        CODINGS = root.findall('{http://www.asam.net/xml/fbx}PROCESSING-INFORMATION/{http://www.asam.net/xml/fbx}CODINGS/{http://www.asam.net/xml/fbx}CODING')
        if CODINGS!=None:
            for CODING in CODINGS:
                # _Coding = {}
                CODING_ID = CODING.attrib.get('ID',None)
                self.Codings[CODING_ID] = {}
                self.Codings[CODING_ID]['ENCODING'] = CODING.find('{http://www.asam.net/xml}CODED-TYPE').attrib.get('ENCODING','SIGNED')
                self.Codings[CODING_ID]['BIT-LENGTH'] = CODING.find('{http://www.asam.net/xml}CODED-TYPE/{http://www.asam.net/xml}BIT-LENGTH').text
                COMPU_NUMERATOR = CODING.find('{http://www.asam.net/xml}COMPU_NUMERATOR')
                if COMPU_NUMERATOR!= None:
                    self.Codings[CODING_ID]['offset'] = COMPU_NUMERATOR[0].text
                    self.Codings[CODING_ID]['factor'] = COMPU_NUMERATOR[1].text
                else:
                    self.Codings[CODING_ID]['offset'] = '0.0'
                    self.Codings[CODING_ID]['factor'] = '1.0'
        ELEMENTS = root.find('{http://www.asam.net/xml/fbx}ELEMENTS')
        if ELEMENTS!= None:
            CLUSTER = ELEMENTS.find('{http://www.asam.net/xml/fbx}CLUSTERS/{http://www.asam.net/xml/fbx}CLUSTER')
            if CLUSTER != None:
                self.STATIC_SLOT = int(CLUSTER.find('{http://www.asam.net/xml/fbx/flexray}STATIC-SLOT').text)
                self.Cluster['Name'] = CLUSTER.find('{http://www.asam.net/xml}SHORT-NAME').text
                self.Cluster['NETWORK_MANAGEMENT_VECTOR_LENGTH'] = int(CLUSTER.find('{http://www.asam.net/xml/fbx/flexray}NETWORK-MANAGEMENT-VECTOR-LENGTH').text)
                self.Cluster['PAYLOAD_LENGTH_STATIC'] = int(CLUSTER.find('{http://www.asam.net/xml/fbx/flexray}PAYLOAD-LENGTH-STATIC').text)
                self.Cluster['T_S_S_TRANSMITTER'] = int(CLUSTER.find('{http://www.asam.net/xml/fbx/flexray}T-S-S-TRANSMITTER').text)
                self.Cluster['CAS_RX_LOW_MAX'] = int(CLUSTER.find('{http://www.asam.net/xml/fbx/flexray}CAS-RX-LOW-MAX').text)
                self.Cluster['SPEED'] = 0 if CLUSTER.find('{http://www.asam.net/xml/fbx}SPEED').text=='10000000' else 1
                WAKE_UP = CLUSTER.find('{http://www.asam.net/xml/fbx/flexray}WAKE-UP')
                self.Cluster['WAKE_UP_SYMBOL_RX_WINDOW'] = int(WAKE_UP.find('{http://www.asam.net/xml/fbx/flexray}WAKE-UP-SYMBOL-RX-WINDOW').text)
                self.Cluster['WAKE_UP_SYMBOL_RX_IDLE'] = int(WAKE_UP.find('{http://www.asam.net/xml/fbx/flexray}WAKE-UP-SYMBOL-RX-IDLE').text)
                self.Cluster['WAKE_UP_SYMBOL_RX_LOW'] = int(WAKE_UP.find('{http://www.asam.net/xml/fbx/flexray}WAKE-UP-SYMBOL-RX-LOW').text)
                self.Cluster['WAKE_UP_SYMBOL_TX_IDLE'] = int(WAKE_UP.find('{http://www.asam.net/xml/fbx/flexray}WAKE-UP-SYMBOL-TX-IDLE').text)
                self.Cluster['WAKE_UP_SYMBOL_TX_LOW'] = int(WAKE_UP.find('{http://www.asam.net/xml/fbx/flexray}WAKE-UP-SYMBOL-TX-LOW').text)
                self.Cluster['COLD_START_ATTEMPTS'] = int(CLUSTER.find('{http://www.asam.net/xml/fbx/flexray}COLD-START-ATTEMPTS').text)
                self.Cluster['LISTEN_NOISE'] = int(CLUSTER.find('{http://www.asam.net/xml/fbx/flexray}LISTEN-NOISE').text)
                self.Cluster['MAX_WITHOUT_CLOCK_CORRECTION_PASSIVE'] = int(CLUSTER.find('{http://www.asam.net/xml/fbx/flexray}MAX-WITHOUT-CLOCK-CORRECTION-PASSIVE').text)
                self.Cluster['MAX_WITHOUT_CLOCK_CORRECTION_FATAL'] = int(CLUSTER.find('{http://www.asam.net/xml/fbx/flexray}MAX-WITHOUT-CLOCK-CORRECTION-FATAL').text)
                self.Cluster['MACRO_PER_CYCLE'] = int(CLUSTER.find('{http://www.asam.net/xml/fbx/flexray}MACRO-PER-CYCLE').text)
                self.Cluster['SYNC_NODE_MAX'] = int(CLUSTER.find('{http://www.asam.net/xml/fbx/flexray}SYNC-NODE-MAX').text)
                self.Cluster['N_I_T'] = int(CLUSTER.find('{http://www.asam.net/xml/fbx/flexray}N-I-T').text)
                self.Cluster['OFFSET_CORRECTION_START'] = int(CLUSTER.find('{http://www.asam.net/xml/fbx/flexray}OFFSET-CORRECTION-START').text)
                self.Cluster['CLUSTER_DRIFT_DAMPING'] = int(CLUSTER.find('{http://www.asam.net/xml/fbx/flexray}CLUSTER-DRIFT-DAMPING').text)
                self.Cluster['STATIC_SLOT'] = int(CLUSTER.find('{http://www.asam.net/xml/fbx/flexray}STATIC-SLOT').text)
                self.Cluster['NUMBER_OF_STATIC_SLOTS'] = int(CLUSTER.find('{http://www.asam.net/xml/fbx/flexray}NUMBER-OF-STATIC-SLOTS').text)
                self.Cluster['MINISLOT'] = int(CLUSTER.find('{http://www.asam.net/xml/fbx/flexray}MINISLOT').text)
                self.Cluster['NUMBER_OF_MINISLOTS'] = int(CLUSTER.find('{http://www.asam.net/xml/fbx/flexray}NUMBER-OF-MINISLOTS').text)
                self.Cluster['DYNAMIC_SLOT_IDLE_PHASE'] = int(CLUSTER.find('{http://www.asam.net/xml/fbx/flexray}DYNAMIC-SLOT-IDLE-PHASE').text)
                self.Cluster['ACTION_POINT_OFFSET'] = int(CLUSTER.find('{http://www.asam.net/xml/fbx/flexray}ACTION-POINT-OFFSET').text)
                self.Cluster['MINISLOT_ACTION_POINT_OFFSET'] = int(CLUSTER.find('{http://www.asam.net/xml/fbx/flexray}MINISLOT-ACTION-POINT-OFFSET').text)
            CHANNELS = ELEMENTS.find('{http://www.asam.net/xml/fbx}CHANNELS')
            if CHANNELS!= None:
                TRIGGERINGS = ELEMENTS.findall('{http://www.asam.net/xml/fbx}CHANNELS/{http://www.asam.net/xml/fbx}CHANNEL/{http://www.asam.net/xml/fbx}FRAME-TRIGGERINGS/{http://www.asam.net/xml/fbx}FRAME-TRIGGERING')
                for TRIGGERING in TRIGGERINGS:
                    # Trigger = {}
                    TRIGGERING_ID = TRIGGERING.attrib.get('ID',None)
                    FRAME_REF =TRIGGERING.find('{http://www.asam.net/xml/fbx}FRAME-REF')
                    if FRAME_REF != None:
                        ID_REF = FRAME_REF.attrib.get('ID-REF',None)
                        self.Triggers[ID_REF]={}
                        self.Triggers[TRIGGERING_ID]={}
                        self.Triggers[TRIGGERING_ID]['ID_REF']=ID_REF
                        self.Triggers[ID_REF]['TRIGGERING_ID']=TRIGGERING_ID
                    TIMING = TRIGGERING.find('{http://www.asam.net/xml/fbx}TIMINGS/{http://www.asam.net/xml/fbx}ABSOLUTELY-SCHEDULED-TIMING')
                    if TIMING!= None:
                        SLOT_ID = int(TIMING.find('{http://www.asam.net/xml/fbx}SLOT-ID').text)
                        BASE_CYCLE = int(TIMING.find('{http://www.asam.net/xml/fbx}BASE-CYCLE').text)
                        CYCLE_REPETITION =  int(TIMING.find('{http://www.asam.net/xml/fbx}CYCLE-REPETITION').text)
                        self.Triggers[TRIGGERING_ID]['SLOT-ID']=SLOT_ID
                        self.Triggers[ID_REF]['SLOT-ID'] = SLOT_ID
                        self.Triggers[TRIGGERING_ID]['BASE-CYCLE']=BASE_CYCLE
                        self.Triggers[ID_REF]['BASE-CYCLE'] = BASE_CYCLE
                        self.Triggers[TRIGGERING_ID]['CYCLE-REPETITION'] = CYCLE_REPETITION
                        self.Triggers[ID_REF]['CYCLE-REPETITION'] = CYCLE_REPETITION
                    del ID_REF,SLOT_ID,BASE_CYCLE,CYCLE_REPETITION,TRIGGERING_ID,
            SIGNALS = ELEMENTS.findall('{http://www.asam.net/xml/fbx}SIGNALS/{http://www.asam.net/xml/fbx}SIGNAL')
            if SIGNALS != None:
                for SIGNAL in SIGNALS:
                    SIGNAL_ID = SIGNAL.attrib.get('ID',None)
                    self.Signals[SIGNAL_ID] = {}
                    self.Signals[SIGNAL_ID]['SHORT-NAME'] = SIGNAL.find('{http://www.asam.net/xml}SHORT-NAME').text
                    self.Signals[SIGNAL_ID]['CODING-REF'] = SIGNAL.find('{http://www.asam.net/xml/fbx}CODING-REF').attrib['ID-REF']
                    self.Signals[SIGNAL_ID]['BIT-LENGTH'] = int(self.Codings[self.Signals[SIGNAL_ID]['CODING-REF']]['BIT-LENGTH'])
                    self.Signals[SIGNAL_ID]['offset'] = float(self.Codings[self.Signals[SIGNAL_ID]['CODING-REF']]['offset'])
                    self.Signals[SIGNAL_ID]['factor'] = float(self.Codings[self.Signals[SIGNAL_ID]['CODING-REF']]['factor'])
                    self.Signals[SIGNAL_ID]['ENCODING'] = False if self.Codings[self.Signals[SIGNAL_ID]['CODING-REF']]['ENCODING']== 'SIGNED' else True
                    del SIGNAL_ID
            PDUS = ELEMENTS.findall('{http://www.asam.net/xml/fbx}PDUS/{http://www.asam.net/xml/fbx}PDU')
            if len(PDUS) == 0:
                PDUS = ELEMENTS.findall('{http://www.asam.net/xml/fbx}FRAMES/{http://www.asam.net/xml/fbx}FRAME')
            for PDU in PDUS:
                pdu_id = PDU.attrib['ID']
                self.Pdus[pdu_id] = {}
                self.Pdus[pdu_id]['PDU_Name'] = PDU.find('{http://www.asam.net/xml}SHORT-NAME').text
                self.Pdus[pdu_id]['DLC'] = PDU.find('{http://www.asam.net/xml/fbx}BYTE-LENGTH').text
                SIGNAL_INSTANCES = PDU.findall('{http://www.asam.net/xml/fbx}SIGNAL-INSTANCES/{http://www.asam.net/xml/fbx}SIGNAL-INSTANCE')
                if SIGNAL_INSTANCES != None:
                    self.Pdus[pdu_id]['SIGNALS'] = {}
                    for SIGNAL_INSTANCE in SIGNAL_INSTANCES:
                        SIGNAL_REF = SIGNAL_INSTANCE.find('{http://www.asam.net/xml/fbx}SIGNAL-REF').attrib.get('ID-REF',None)
                        _Signal_Name = self.Signals[SIGNAL_REF]['SHORT-NAME']
                        self.Pdus[pdu_id]['SIGNALS'][_Signal_Name] = {}
                        self.Pdus[pdu_id]['SIGNALS'][_Signal_Name]['SHORT-NAME'] = self.Signals[SIGNAL_REF]['SHORT-NAME']
                        self.Pdus[pdu_id]['SIGNALS'][_Signal_Name]['BIT-POSITION'] = int(SIGNAL_INSTANCE.find('{http://www.asam.net/xml/fbx}BIT-POSITION').text)
                        self.Pdus[pdu_id]['SIGNALS'][_Signal_Name]['BIT-LENGTH'] = self.Signals[SIGNAL_REF]['BIT-LENGTH']
                        self.Pdus[pdu_id]['SIGNALS'][_Signal_Name]['offset'] = self.Signals[SIGNAL_REF]['offset']
                        self.Pdus[pdu_id]['SIGNALS'][_Signal_Name]['factor'] = self.Signals[SIGNAL_REF]['factor']
                        self.Pdus[pdu_id]['SIGNALS'][_Signal_Name]['ENCODING'] = self.Signals[SIGNAL_REF]['ENCODING']
                        self.Pdus[pdu_id]['SIGNALS'][_Signal_Name]['is_M'] = SIGNAL_INSTANCE.find('{http://www.asam.net/xml/fbx}IS-HIGH-LOW-BYTE-ORDER').text
                        self.Pdus[pdu_id]['SIGNALS'][_Signal_Name]['ub'] = int(SIGNAL_INSTANCE.find('{http://www.asam.net/xml/fbx}SIGNAL-UPDATE-BIT-POSITION').text) if SIGNAL_INSTANCE.find('{http://www.asam.net/xml/fbx}SIGNAL-UPDATE-BIT-POSITION') != None else -1
                        if self.Pdus[pdu_id]['SIGNALS'][_Signal_Name]['ub'] != -1:
                            ub_name = _Signal_Name+"_ub"
                            self.Pdus[pdu_id]['SIGNALS'][ub_name] = {}
                            self.Pdus[pdu_id]['SIGNALS'][ub_name]['SHORT-NAME'] = ub_name
                            self.Pdus[pdu_id]['SIGNALS'][ub_name]['BIT-POSITION'] = self.Pdus[pdu_id]['SIGNALS'][_Signal_Name]['ub']
                            self.Pdus[pdu_id]['SIGNALS'][ub_name]['BIT-LENGTH'] = 1
                            self.Pdus[pdu_id]['SIGNALS'][ub_name]['offset'] = 0
                            self.Pdus[pdu_id]['SIGNALS'][ub_name]['factor'] = 1
                            self.Pdus[pdu_id]['SIGNALS'][ub_name]['ENCODING'] = self.Signals[SIGNAL_REF]['ENCODING']
                            self.Pdus[pdu_id]['SIGNALS'][ub_name]['is_M'] = True
                            self.Pdus[pdu_id]['SIGNALS'][ub_name]['ub'] = '-1'
                        del _Signal_Name,SIGNAL_REF
                del pdu_id
            FRAMES = ELEMENTS.findall('{http://www.asam.net/xml/fbx}FRAMES/{http://www.asam.net/xml/fbx}FRAME')
            if FRAMES != None:
                for FRAME in FRAMES:
                    # _Frame ={}
                    FRAME_NAME = FRAME.find('{http://www.asam.net/xml}SHORT-NAME').text
                    self.Frames[FRAME_NAME] ={}
                    FRAME_ID = FRAME.attrib.get('ID',None)
                    self.Frames[FRAME_NAME]['SHORT-NAME'] = FRAME_NAME
                    # self.Frames[FRAME_NAME]['FRAME-ID'] = FRAME.attrib.get('ID',None)
                    self.Frames[FRAME_NAME]['SLOT-ID']= self.Triggers[FRAME_ID]['SLOT-ID']
                    self.Frames[FRAME_NAME]['BASE-CYCLE']= self.Triggers[FRAME_ID]['BASE-CYCLE']
                    self.Frames[FRAME_NAME]['CYCLE-REPETITION']= self.Triggers[FRAME_ID]['CYCLE-REPETITION']
                    _FDLC = int(FRAME.find('{http://www.asam.net/xml/fbx}BYTE-LENGTH').text)
                    self.Frames[FRAME_NAME]['FDLC'] = _FDLC
                    self.Triggers[FRAME_ID]['FDLC'] = _FDLC
                    self.Triggers[FRAME_ID]['Name'] = FRAME_NAME
                    self.Triggers[self.Triggers[FRAME_ID]['TRIGGERING_ID']]['FDLC'] = _FDLC
                    self.Triggers[self.Triggers[FRAME_ID]['TRIGGERING_ID']]['Name'] = FRAME_NAME
                    PDU_INSTANCES = FRAME.findall('{http://www.asam.net/xml/fbx}PDU-INSTANCES/{http://www.asam.net/xml/fbx}PDU-INSTANCE')
                    if len(PDU_INSTANCES) != 0:
                        self.Frames[FRAME_NAME]['PDUS'] = []
                        for PDU_INSTANCE in PDU_INSTANCES:
                            PDU_REF = PDU_INSTANCE.find('{http://www.asam.net/xml/fbx}PDU-REF').attrib.get('ID-REF',None)
                            PDU_1 = {}
                            PDU_1['PDU_Name'] = self.Pdus[PDU_REF]['PDU_Name']
                            PDU_1['BIT-POSITION'] = int(PDU_INSTANCE.find('{http://www.asam.net/xml/fbx}BIT-POSITION').text)
                            PDU_1['SIGNALS'] = self.Pdus[PDU_REF]['SIGNALS']
                            self.Frames[FRAME_NAME]['PDUS'].append(PDU_1)  # store all PDUs in a list for easier
                            # self.Frames[FRAME_NAME][self.Pdus[PDU_REF]['PDU_Name']]={}
                            # self.Frames[FRAME_NAME][self.Pdus[PDU_REF]['PDU_Name']]['BIT-POSITION']=int(PDU_INSTANCE.find('{http://www.asam.net/xml/fbx}BIT-POSITION').text)
                            # self.Frames[FRAME_NAME][self.Pdus[PDU_REF]['PDU_Name']]['SIGNALS'] = self.Pdus[PDU_REF]['SIGNALS']
                            del PDU_REF,PDU_1
                    else:
                        try:
                            self.Frames[FRAME_NAME]['SIGNALS'] = self.Pdus[FRAME_ID]['SIGNALS']
                        except:
                            pass
                    del FRAME_NAME,FRAME_ID,_FDLC
            ECUS = ELEMENTS.findall('{http://www.asam.net/xml/fbx}ECUS/{http://www.asam.net/xml/fbx}ECU')
            if ECUS != None:  
                for ECU in ECUS: 
                    ecu_name = ECU.find('{http://www.asam.net/xml}SHORT-NAME').text
                    self.Ecus[ecu_name] = {}
                    INPUT_PORTS = ECU.findall('{http://www.asam.net/xml/fbx}CONNECTORS/{http://www.asam.net/xml/fbx}CONNECTOR/{http://www.asam.net/xml/fbx}INPUTS/{http://www.asam.net/xml/fbx}INPUT-PORT')
                    OUTPUT_PORTS = ECU.findall('{http://www.asam.net/xml/fbx}CONNECTORS/{http://www.asam.net/xml/fbx}CONNECTOR/{http://www.asam.net/xml/fbx}OUTPUTS/{http://www.asam.net/xml/fbx}OUTPUT-PORT')
                    ECU = ECU.find('{http://www.asam.net/xml/fbx}CONTROLLERS/{http://www.asam.net/xml/fbx}CONTROLLER')
                    self.Ecus[ecu_name]['NETWORK_MANAGEMENT_VECTOR_LENGTH'] = self.Cluster['NETWORK_MANAGEMENT_VECTOR_LENGTH'] 
                    self.Ecus[ecu_name]['PAYLOAD_LENGTH_STATIC'] = self.Cluster['PAYLOAD_LENGTH_STATIC'] 
                    self.Ecus[ecu_name]['T_S_S_TRANSMITTER'] = self.Cluster['T_S_S_TRANSMITTER'] 
                    self.Ecus[ecu_name]['CAS_RX_LOW_MAX'] = self.Cluster['CAS_RX_LOW_MAX'] 
                    self.Ecus[ecu_name]['SPEED'] = self.Cluster['SPEED'] 
                    self.Ecus[ecu_name]['WAKE_UP_SYMBOL_RX_WINDOW'] = self.Cluster['WAKE_UP_SYMBOL_RX_WINDOW'] 
                    self.Ecus[ecu_name]['WAKE_UP_SYMBOL_RX_IDLE'] = self.Cluster['WAKE_UP_SYMBOL_RX_IDLE'] 
                    self.Ecus[ecu_name]['WAKE_UP_SYMBOL_RX_LOW'] = self.Cluster['WAKE_UP_SYMBOL_RX_LOW'] 
                    self.Ecus[ecu_name]['WAKE_UP_SYMBOL_TX_IDLE'] = self.Cluster['WAKE_UP_SYMBOL_TX_IDLE'] 
                    self.Ecus[ecu_name]['WAKE_UP_SYMBOL_TX_LOW'] = self.Cluster['WAKE_UP_SYMBOL_TX_LOW'] 
                    self.Ecus[ecu_name]['COLD_START_ATTEMPTS'] = self.Cluster['COLD_START_ATTEMPTS'] 
                    self.Ecus[ecu_name]['LISTEN_NOISE'] = self.Cluster['LISTEN_NOISE'] 
                    self.Ecus[ecu_name]['MAX_WITHOUT_CLOCK_CORRECTION_PASSIVE'] = self.Cluster['MAX_WITHOUT_CLOCK_CORRECTION_PASSIVE'] 
                    self.Ecus[ecu_name]['MAX_WITHOUT_CLOCK_CORRECTION_FATAL'] = self.Cluster['MAX_WITHOUT_CLOCK_CORRECTION_FATAL'] 
                    self.Ecus[ecu_name]['MACRO_PER_CYCLE'] = self.Cluster['MACRO_PER_CYCLE'] 
                    self.Ecus[ecu_name]['SYNC_NODE_MAX'] = self.Cluster['SYNC_NODE_MAX'] 
                    self.Ecus[ecu_name]['N_I_T'] = self.Cluster['N_I_T'] 
                    self.Ecus[ecu_name]['OFFSET_CORRECTION_START'] = self.Cluster['OFFSET_CORRECTION_START'] 
                    self.Ecus[ecu_name]['CLUSTER_DRIFT_DAMPING'] = self.Cluster['CLUSTER_DRIFT_DAMPING'] 
                    self.Ecus[ecu_name]['STATIC_SLOT'] = self.Cluster['STATIC_SLOT'] 
                    self.Ecus[ecu_name]['NUMBER_OF_STATIC_SLOTS'] = self.Cluster['NUMBER_OF_STATIC_SLOTS'] 
                    self.Ecus[ecu_name]['MINISLOT'] = self.Cluster['MINISLOT'] 
                    self.Ecus[ecu_name]['NUMBER_OF_MINISLOTS'] = self.Cluster['NUMBER_OF_MINISLOTS'] 
                    self.Ecus[ecu_name]['DYNAMIC_SLOT_IDLE_PHASE'] = self.Cluster['DYNAMIC_SLOT_IDLE_PHASE'] 
                    self.Ecus[ecu_name]['ACTION_POINT_OFFSET'] = self.Cluster['ACTION_POINT_OFFSET'] 
                    self.Ecus[ecu_name]['MINISLOT_ACTION_POINT_OFFSET'] = self.Cluster['MINISLOT_ACTION_POINT_OFFSET'] 
                    STARTUP_SYNC = ECU.find('{http://www.asam.net/xml/fbx/flexray}KEY-SLOT-USAGE/{http://www.asam.net/xml/fbx/flexray}STARTUP-SYNC')
                    if STARTUP_SYNC != None:
                        self.Ecus[ecu_name]['startupFrameTransmitted'] = 1
                        self.Ecus[ecu_name]['startupFrame_ID'] =int(STARTUP_SYNC.text) 
                    else:
                        self.Ecus[ecu_name]['startupFrameTransmitted'] = 0 
                        self.Ecus[ecu_name]['startupFrame_ID'] = 0
                    self.Ecus[ecu_name]['ACCEPTED_STARTUP_RANGE'] = int(ECU.find('{http://www.asam.net/xml/fbx/flexray}ACCEPTED-STARTUP-RANGE').text)
                    self.Ecus[ecu_name]['MAX_DRIFT'] = int(ECU.find('{http://www.asam.net/xml/fbx/flexray}MAX-DRIFT').text)
                    self.Ecus[ecu_name]['WAKE_UP_PATTERN'] = int(ECU.find('{http://www.asam.net/xml/fbx/flexray}WAKE-UP-PATTERN').text)
                    self.Ecus[ecu_name]['ALLOW_HALT_DUE_TO_CLOCK'] = 1 if ECU.find('{http://www.asam.net/xml/fbx/flexray}ALLOW-HALT-DUE-TO-CLOCK') == 'true' else 0
                    self.Ecus[ecu_name]['SINGLE_SLOT_ENABLED'] = 1 if ECU.find('{http://www.asam.net/xml/fbx/flexray}SINGLE-SLOT-ENABLED') == 'true' else 0
                    self.Ecus[ecu_name]['ALLOW_PASSIVE_TO_ACTIVE'] = int(ECU.find('{http://www.asam.net/xml/fbx/flexray}ALLOW-PASSIVE-TO-ACTIVE').text)
                    self.Ecus[ecu_name]['LISTEN_TIMEOUT'] = int(ECU.find('{http://www.asam.net/xml/fbx/flexray}LISTEN-TIMEOUT').text)
                    self.Ecus[ecu_name]['MICRO_PER_CYCLE'] = int(ECU.find('{http://www.asam.net/xml/fbx/flexray}MICRO-PER-CYCLE').text)
                    self.Ecus[ecu_name]['LATEST_TX'] = int(ECU.find('{http://www.asam.net/xml/fbx/flexray}LATEST-TX').text)
                    self.Ecus[ecu_name]['MICRO_INITIAL_OFFSET_A'] = int(ECU.find('{http://www.asam.net/xml/fbx/flexray}MICRO-INITIAL-OFFSET-A').text)
                    self.Ecus[ecu_name]['MICRO_INITIAL_OFFSET_B'] = int(ECU.find('{http://www.asam.net/xml/fbx/flexray}MICRO-INITIAL-OFFSET-B').text)
                    self.Ecus[ecu_name]['MACRO_INITIAL_OFFSET_A'] = int(ECU.find('{http://www.asam.net/xml/fbx/flexray}MACRO-INITIAL-OFFSET-A').text)
                    self.Ecus[ecu_name]['MACRO_INITIAL_OFFSET_B'] = int(ECU.find('{http://www.asam.net/xml/fbx/flexray}MACRO-INITIAL-OFFSET-B').text)
                    self.Ecus[ecu_name]['DELAY_COMPENSATION_A'] = int(ECU.find('{http://www.asam.net/xml/fbx/flexray}MACRO-INITIAL-OFFSET-A').text)
                    self.Ecus[ecu_name]['DELAY_COMPENSATION_B'] = int(ECU.find('{http://www.asam.net/xml/fbx/flexray}MACRO-INITIAL-OFFSET-B').text)
                    self.Ecus[ecu_name]['CLUSTER_DRIFT_DAMPING'] = int(ECU.find('{http://www.asam.net/xml/fbx/flexray}CLUSTER-DRIFT-DAMPING').text)
                    self.Ecus[ecu_name]['DECODING_CORRECTION'] = int(ECU.find('{http://www.asam.net/xml/fbx/flexray}DECODING-CORRECTION').text)
                    self.Ecus[ecu_name]['OFFSET_CORRECTION_OUT'] = int(ECU.find('{http://www.asam.net/xml/fbx/flexray}OFFSET-CORRECTION-OUT').text)
                    self.Ecus[ecu_name]['RATE_CORRECTION_OUT'] = int(ECU.find('{http://www.asam.net/xml/fbx/flexray}RATE-CORRECTION-OUT').text)
                    self.Ecus[ecu_name]['EXTERN_OFFSET_CORRECTION'] = int(ECU.find('{http://www.asam.net/xml/fbx/flexray}EXTERN-OFFSET-CORRECTION').text)
                    self.Ecus[ecu_name]['EXTERN_RATE_CORRECTION'] = int(ECU.find('{http://www.asam.net/xml/fbx/flexray}EXTERN-RATE-CORRECTION').text)
                    self.Ecus[ecu_name]['TX_Frame']=[]
                    self.Ecus[ecu_name]['RX_Frame']=[]
                    for INPUT_PORT in INPUT_PORTS:
                        _rx_frame = {}
                        Trgger_ID = INPUT_PORT.find('{http://www.asam.net/xml/fbx}FRAME-TRIGGERING-REF').attrib.get('ID-REF',None)
                        _rx_frame['SLOT-ID'] = self.Triggers[Trgger_ID]['SLOT-ID']
                        _rx_frame['BASE-CYCLE'] = self.Triggers[Trgger_ID]['BASE-CYCLE']
                        _rx_frame['CYCLE-REPETITION'] = self.Triggers[Trgger_ID]['CYCLE-REPETITION']
                        _rx_frame['FDLC'] = self.Triggers[Trgger_ID]['FDLC']
                        _rx_frame['Name'] = self.Triggers[Trgger_ID]['Name']
                        self.Ecus[ecu_name]['RX_Frame'].append(_rx_frame)
                        del Trgger_ID,_rx_frame
                    for OUTPUT_PORT in OUTPUT_PORTS:
                        _tx_frame = {}
                        Trgger_ID = OUTPUT_PORT.find('{http://www.asam.net/xml/fbx}FRAME-TRIGGERING-REF').attrib.get('ID-REF',None)
                        _tx_frame['SLOT-ID'] = self.Triggers[Trgger_ID]['SLOT-ID']
                        _tx_frame['BASE-CYCLE'] = self.Triggers[Trgger_ID]['BASE-CYCLE']
                        _tx_frame['CYCLE-REPETITION'] = self.Triggers[Trgger_ID]['CYCLE-REPETITION']
                        _tx_frame['FDLC'] = self.Triggers[Trgger_ID]['FDLC']
                        _tx_frame['Name'] = self.Triggers[Trgger_ID]['Name']
                        if self.Ecus[ecu_name]['startupFrame_ID'] == _tx_frame['SLOT-ID'] and len(self.Ecus[ecu_name]['TX_Frame'])!=0  :
                            self.Ecus[ecu_name]['TX_Frame'].append(self.Ecus[ecu_name]['TX_Frame'][0])
                            self.Ecus[ecu_name]['TX_Frame'][0] = _tx_frame
                        else:
                            self.Ecus[ecu_name]['TX_Frame'].append(_tx_frame)
                        del Trgger_ID,_tx_frame
                    del ecu_name