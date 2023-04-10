<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="15008000">
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
		<Item Name="01-main.vi" Type="VI" URL="../01-main.vi"/>
		<Item Name="02-调小程序.vi" Type="VI" URL="../02-调小程序.vi"/>
		<Item Name="03-和tsmaster配合演示接收报文.vi" Type="VI" URL="../03-和tsmaster配合演示接收报文.vi"/>
		<Item Name="04-获取信号值.vi" Type="VI" URL="../04-获取信号值.vi"/>
		<Item Name="05-调用dotnetdll.vi" Type="VI" URL="../05-调用dotnetdll.vi"/>
		<Item Name="依赖关系" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="subTimeDelay.vi" Type="VI" URL="/&lt;vilib&gt;/express/express execution control/TimeDelayBlock.llb/subTimeDelay.vi"/>
			</Item>
			<Item Name="98-pubilc-html报表生成-精确时间及模糊时间命_带天数.vi" Type="VI" URL="/F/00_labview/02-public/98-pubilc-html报表生成-精确时间及模糊时间命_带天数.vi"/>
			<Item Name="Interop.TSMasterAPI.dll" Type="Document" URL="../Interop.TSMasterAPI.dll"/>
		</Item>
		<Item Name="程序生成规范" Type="Build"/>
	</Item>
</Project>
