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

    '''
        获取安卓设备APP版本信息
    '''
    def getAppVersion(self):
        version = ''
        versionCmd = 'adb shell dumpsys package com.wanda.app.wanhui | grep versionName'
        ret = Popen(versionCmd, shell=True, stdout=PIPE, stderr=PIPE)
        out, err = ret.communicate()
        if out:
            version = out.decode('utf-8').split('=')[1].split('\r\n')[0]

        return version

    '''
        获取安卓设备型号信息
    '''
    def getPhoneVersion(self):
        brand = ''
        mode = ''
        brandCmd = 'adb shell cat /system/build.prop | grep "product.brand"'
        modeCmd = 'adb shell cat /system/build.prop | grep "product.mode"'
        ret = Popen(brandCmd, shell=True, stdout=PIPE, stderr=PIPE)
        out, err = ret.communicate()
        if out:
            brand = out.decode('utf-8').split('=')[1].split('\r\n')[0]
        ret = Popen(modeCmd, shell=True, stdout=PIPE, stderr=PIPE)
        out, err = ret.communicate()
        if out:
            mode = out.decode('utf-8').split('=')[1].split('\r\n')[0]

        return brand.upper() + ' ' + mode.upper()

    '''
        获取Android设备ID信息
    '''
    def getDeviceID(self):
        id = ''
        versionCmd = 'adb devices'
        ret = Popen(versionCmd, shell=True, stdout=PIPE, stderr=PIPE)
        out, err = ret.communicate()
        if out:
            version = out.decode('utf-8').split('\n')[1].split('\t')[0]

        return version

    """
        获取iOS设备UDID,需要安装ideviceinstaller才能调用
    """

    def getUdid(self):
        cmd = 'idevice_id -l'
        p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)

        out, err = p.communicate()
        return out.decode("utf-8").rstrip()

    """

    """
    def get_product_version(self):
        cmd = 'ideviceinfo -k ProductVersion'
        p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
        out, err = p.communicate()
        return out.decode("utf-8").strip()


if __name__ == '__main__':
    deviceInfoUtil = DeviceInfoUtil()
    print(deviceInfoUtil.getDeviceID())
