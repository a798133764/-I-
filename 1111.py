#!/usr/bin/python
# coding: utf-8

import platform
import os

os_type = platform.system()
if "Linux" == os_type:
    fileDirPath = "%s/.pip" % os.path.expanduser('~')
    filePath = "%s/pip.conf" % fileDirPath
    if not os.path.isdir(fileDirPath):
        os.makedirs(fileDirPath)
    fo = open(filePath, "w")
    fo.write('''[global]
timeout = 6000
index-url=https://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host=mirrors.aliyun.com
''')
    fo.close()
    print ("Configuration is complete")
elif "Windows" == os_type:
    fileDirPath = "%s\\AppData\\Roaming\\pip" % os.path.expanduser('~')
    filePath = "%s\\pip.ini" % fileDirPath
    if not os.path.isdir(fileDirPath):
        os.makedirs(fileDirPath)
    fo = open(filePath, "w")
    fo.write('''[global]
timeout = 6000
index-url=https://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host=mirrors.aliyun.com
''')
    fo.close()
    print("Configuration is complete")
else:
    exit("Your platform is unknow!")