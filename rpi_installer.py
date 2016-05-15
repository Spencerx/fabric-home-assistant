#!/usr/bin/env python
import os
import time
print("""
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,, ,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,   ,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,     ,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,       ,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,         ,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,           ,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,             ,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,               ,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,       ,,,,.     ,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,       ,,,,,,,     ,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,       ,,,,,,,,,     ,,,     ,,,,,,,,,,
,,,,,,,,,,,,,,,,        ,,,   ,,,      ,,     ,,,,,,,,,,
,,,,,,,,,,,,,,,         ,,,   ,,,       ,     ,,,,,,,,,,
,,,,,,,,,,,,,,          ,,,   ,,,             ,,,,,,,,,,
,,,,,,,,,,,,,            ,,,,,,,              ,,,,,,,,,,
,,,,,,,,,,,,              ,,,,,               ,,,,,,,,,,
,,,,,,,,,,,                ,,,                ,,,,,,,,,,
,,,,,,,,,,                 ,,,                 ,,,,,,,,,
,,,,,,,,,        ,,,       ,,,       ,,,        ,,,,,,,,
,,,,,,,,       ,,,,,,,     ,,,     ,,,,,,,       ,,,,,,,
,,,,,,,       ,,,,,,,,,    ,,,    ,,,,,,,,,       ,,,,,,
,,,,,,        ,,,   ,,,    ,,,    ,,,   ,,,        ,,,,,
,,,,,         ,,,   ,,,    ,,,    ,,,   ,,,         ,,,,
,,,,,,,,,,,   ,,,   ,,,    ,,,    ,,,   ,,,   ,,,,,,,,,,
,,,,,,,,,,,    ,,,,,,,,    ,,,    ,,,,,,,,    ,,,,,,,,,,
,,,,,,,,,,,      ,,,,,,    ,,,    ,,,,,,      ,,,,,,,,,,
,,,,,,,,,,,        ,,,,,   ,,,   ,,,,,        ,,,,,,,,,,
,,,,,,,,,,,          ,,,, ,,,, ,,,,,          ,,,,,,,,,,
,,,,,,,,,,,           ,,,, ,,, ,,,,           ,,,,,,,,,,
,,,,,,,,,,,            ,,,,,,,,,,,            ,,,,,,,,,,
,,,,,,,,,,,             ,,,,,,,,,             ,,,,,,,,,,
,,,,,,,,,,,              ,,,,,,,              ,,,,,,,,,,
,,,,,,,,,,,               ,,,,,               ,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,                                   ,,,,,,,,,,
,,,,,,,,,,,   Welcome to the Home Assistant   ,,,,,,,,,,
,,,,,,,,,,, Raspberry Pi All-In-One Installer ,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
""")
#Try and Except: NEED TO ADD THIS
uinput = raw_input('Enter 1 for installation WITH virtualenv\nEnter 2 for installation WITHOUT virtualenv: ')
try:
    a = int(uinput)
    if a == 1:
        print("Your Raspberry Pi will reboot when the installer is complete.")
        time.sleep(3)
        print("Install is starting...")
        start_install1 = 'fab deploy -H localhost'
        os.system(start_install1)
    elif a== 2:
        print("Your Raspberry Pi will reboot when the installer is complete.")
        time.sleep(3)
        print("Install is starting...")
        start_install2 = 'fab deploy_novenv -H localhost'
        os.system(start_install2)
except:
    print("Please enter 1 use a VirtualEnv, or 2 do NOT use a VirtualEnv")
