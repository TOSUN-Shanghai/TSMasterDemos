<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="13008000">
	<Item Name="我的电脑" Type="My Computer">
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">我的电脑/VI服务器</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">我的电脑/VI服务器</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="Function" Type="Folder">
			<Item Name="TSCAN ChannelCount.vi" Type="VI" URL="../TSCAN ChannelCount.vi"/>
			<Item Name="TSCAN Close.vi" Type="VI" URL="../TSCAN Close.vi"/>
			<Item Name="TSCAN DBCAnalysisReceive.vi" Type="VI" URL="../TSCAN DBCAnalysisReceive.vi"/>
			<Item Name="TSCAN DBCAnalysisTransmit.vi" Type="VI" URL="../TSCAN DBCAnalysisTransmit.vi"/>
			<Item Name="TSCAN Dll.vi" Type="VI" URL="../TSCAN Dll.vi"/>
			<Item Name="TSCAN Init.vi" Type="VI" URL="../TSCAN Init.vi"/>
			<Item Name="TSCAN LoadDBC.vi" Type="VI" URL="../TSCAN LoadDBC.vi"/>
			<Item Name="TSCAN Open.vi" Type="VI" URL="../TSCAN Open.vi"/>
			<Item Name="TSCAN Receive.vi" Type="VI" URL="../TSCAN Receive.vi"/>
			<Item Name="TSCAN SetMapping.vi" Type="VI" URL="../TSCAN SetMapping.vi"/>
			<Item Name="TSCAN Transmit.vi" Type="VI" URL="../TSCAN Transmit.vi"/>
			<Item Name="TSCANFD Receive.vi" Type="VI" URL="../TSCANFD Receive.vi"/>
			<Item Name="TSCANFD SetMapping.vi" Type="VI" URL="../TSCANFD SetMapping.vi"/>
			<Item Name="TSCANFD Transmit.vi" Type="VI" URL="../TSCANFD Transmit.vi"/>
			<Item Name="TSLIN ChannelCount.vi" Type="VI" URL="../TSLIN ChannelCount.vi"/>
			<Item Name="TSLIN Open.vi" Type="VI" URL="../TSLIN Open.vi"/>
			<Item Name="TSLIN SetMapping.vi" Type="VI" URL="../TSLIN SetMapping.vi"/>
			<Item Name="TSLIN Transmit.vi" Type="VI" URL="../TSLIN Transmit.vi"/>
			<Item Name="TSlIN TransmitHeader&amp;Receive.vi" Type="VI" URL="../TSlIN TransmitHeader&amp;Receive.vi"/>
		</Item>
		<Item Name="Example.vi" Type="VI" URL="../Example.vi"/>
		<Item Name="TSCAN Demo TC1001.vi" Type="VI" URL="../TSCAN Demo TC1001.vi"/>
		<Item Name="TSCAN Demo TC1011.vi" Type="VI" URL="../TSCAN Demo TC1011.vi"/>
		<Item Name="TSCAN.vi" Type="VI" URL="../TSCAN.vi"/>
		<Item Name="依赖关系" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="1D String Array to Delimited String.vi" Type="VI" URL="/&lt;vilib&gt;/AdvancedString/1D String Array to Delimited String.vi"/>
				<Item Name="Application Directory.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Application Directory.vi"/>
				<Item Name="Clear Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Clear Errors.vi"/>
				<Item Name="Error Cluster From Error Code.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Cluster From Error Code.vi"/>
				<Item Name="List Directory and LLBs.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/libraryn.llb/List Directory and LLBs.vi"/>
				<Item Name="NI_FileType.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/lvfile.llb/NI_FileType.lvlib"/>
				<Item Name="Recursive File List.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/libraryn.llb/Recursive File List.vi"/>
				<Item Name="Space Constant.vi" Type="VI" URL="/&lt;vilib&gt;/dlg_ctls.llb/Space Constant.vi"/>
			</Item>
		</Item>
		<Item Name="程序生成规范" Type="Build"/>
	</Item>
</Project>
