# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE

'''
    usage :  进入应用的首页
'''


class DeviceInfoUtil:
    def __init__(self):
        pass

    '''
        获取安卓设备系统版本号
    '''
    def getBuildVersion(self):
        cmd = 'adb shell getprop ro.build.version.release'
        p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)

        out, err = p.communicate()
        # print("out is %s" % (type(out)));
        # print("Return code: ", p.returncode)
        # print(out.decode("utf-8").rstrip(), err.rstrip())
        return out.decode("utf-8").rstrip();

    """
        获取iOS设备UDID,需要安装ideviceinstaller才能调用
    """

    def getUdid(self):
        cmd = 'idevice_id -l'
        p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)

        out, err = p.communicate()
        return out.decode("utf-8").rstrip();

    """

    """
    def get_product_version(self):
        cmd = 'ideviceinfo -k ProductVersion'
        p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
        out, err = p.communicate()
        return out.decode("utf-8").strip();



if __name__ == '__main__':
    deviceInfoUtil = DeviceInfoUtil()
    print(deviceInfoUtil.get_product_version())
