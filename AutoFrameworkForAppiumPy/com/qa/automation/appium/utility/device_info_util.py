# -*- coding: utf-8 -*-

import os, sys
from subprocess import Popen, PIPE

# sys.path.append(os.path.dirname(os.path.dirname(__file__)))



# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

'''
    usage :  进入应用的首页
'''


class DeviceInfoUtil:
    def __init__(self):
        pass

    '''
        获取设备系统版本号
    '''
    def getBuildVersion(self):
        cmd = 'adb shell getprop ro.build.version.release'
        p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)

        out, err = p.communicate()
        # print("out is %s" % (type(out)));
        # print("Return code: ", p.returncode)
        # print(out.decode("utf-8").rstrip(), err.rstrip())
        return out.decode("utf-8").rstrip();


if __name__ == '__main__':
    clearAppData = DeviceInfoUtil()
    print(clearAppData.getBuildVersion())
