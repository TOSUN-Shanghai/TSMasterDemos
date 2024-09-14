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
dll_path = ''
try:
    TSMaster_location = r"Software\TOSUN\TSMaster"

    _curr_path = os.path.dirname(__file__)

    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, TSMaster_location)

    _arch, _os = platform.architecture()

    i = 0
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
except:
    pass
if dll_path != '':
    try:
        dll_path = os.path.split(dll_path)[0] + '/TSMaster.dll'
        dllPath = os.path.split(dll_path)[0]
        dll = WinDLL(dll_path)
    except Exception as r:
        try:
            if _arch == '32bit':
                dll_path = _curr_path + "\\windows\\bin\\TSMaster.dll"
            else:
                dll_path = _curr_path + "\\windows\\bin64\\TSMaster.dll"
            dll = WinDLL(dll_path)
        except Exception as r:
            print(r"Could not load the TOSUN DLL from '%s'. Error: %s" % (dll_path, r))
else:
    try:
        if _arch == '32bit':
            dll_path = _curr_path + "\\windows\\bin\\TSMaster.dll"
        else:
            dll_path = _curr_path + "\\windows\\bin64\\TSMaster.dll"
        dll = WinDLL(dll_path)
    except Exception as r:
        print(r"Could not load the TOSUN DLL from '%s'. Error: %s" % (dll_path, r))
