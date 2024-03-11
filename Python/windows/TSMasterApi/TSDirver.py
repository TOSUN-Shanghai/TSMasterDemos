'''
Author: seven 865762826@qq.com
Date: 2023-04-21 11:21:33
LastEditors: seven 865762826@qq.com
LastEditTime: 2023-11-22 10:26:17
'''
from ctypes import WinDLL
import os
import winreg
import platform

TSMaster_location = r"Software\TOSUN\TSMaster"

key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, TSMaster_location)

_arch, _os = platform.architecture()

i = 0
dll_path = ''
while True:
    try:
        if _arch == '32bit':
        # 获取注册表对应位置的键和值
            if  winreg.EnumValue(key, i)[0] == 'libTSMaster_x86':
                dll_path = winreg.EnumValue(key, i)[1]
                winreg.CloseKey(key)
                break
        else:
            if  winreg.EnumValue(key, i)[0] == 'libTSMaster_x64':
                dll_path = winreg.EnumValue(key, i)[1]
                winreg.CloseKey(key)
                break
        i += 1
    except OSError as error:
        # 一定要关闭这个键
        winreg.CloseKey(key)
        break

if dll_path != '':
    try:
        dll_path = os.path.split(dll_path)[0] + '/TSMaster.dll'
        dllPath = os.path.split(dll_path)[0]
        dll = WinDLL(dll_path)
    except Exception as r:
        print(r"Could not load the TOSUN DLL from '%s'. Error: %s" % (dll_path, r))
else:
    print(r"Could not load the TOSUN DLL Error: Registry not found")
