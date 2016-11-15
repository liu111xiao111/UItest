# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE


class DeviceInfoUtil:
    def __init__(self):
        pass

    def getBuildVersion(self):
        '''
        获取安卓设备系统版本号
        '''
        cmd = 'adb shell getprop ro.build.version.release'
        p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)

        out, err = p.communicate()
        # print("out is %s" % (type(out)));
        # print("Return code: ", p.returncode)
        # print(out.decode("utf-8").rstrip(), err.rstrip())
        return out.decode("utf-8").rstrip();


    def getAppVersion(self):
        '''
        获取安卓设备APP版本信息
        '''
        version = ''
        versionCmd = 'adb shell dumpsys package com.wanda.app.wanhui | grep versionName'
        ret = Popen(versionCmd, shell=True, stdout=PIPE, stderr=PIPE)
        out, err = ret.communicate()
        if out:
            version = out.decode('utf-8').split('=')[1].split('\r\n')[0]

        return version


    def getPhoneVersion(self):
        '''
        获取安卓设备型号信息
        '''
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


    def getDeviceID(self):
        '''
        获取Android设备ID信息
        '''
        id = ''
        versionCmd = 'adb devices'
        ret = Popen(versionCmd, shell=True, stdout=PIPE, stderr=PIPE)
        out, err = ret.communicate()
        if out:
            version = out.decode('utf-8').split('\n')[1].split('\t')[0]

        return version


    def getUdid(self):
        """
        获取iOS设备UDID,需要安装ideviceinstaller才能调用
        """
        cmd = 'idevice_id -l'
        p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)

        out, err = p.communicate()
        return out.decode("utf-8").rstrip()


    def getIProductVersion(self):
        '''
        获取iOS设备系统版本号
        :return:
        '''
        cmd = 'ideviceinfo -k ProductVersion'
        p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
        out, err = p.communicate()
        return out.decode("utf-8").strip()

    def getIPhoneType(self):
        '''
        获取 iphone 型号
        :return:
        '''
        iTypeDic = {'iPhone3,1':'iPhone 4',
                    'iPhone3,2':'iPhone 4',
                    'iPhone4,1':'iPhone 4S',
                    'iPhone5,1':'iPhone 5',
                    'iPhone5,2':'iPhone 5',
                    'iPhone5,3':'iPhone 5C',
                    'iPhone5,4':'iPhone 5C',
                    'iPhone6,2':'iPhone 5S',
                    'iPhone7,2':'iPhone 6',
                    'iPhone8,1':'iPhone 6S',
                    'iPhone7,1':'iPhone 6 Plus',
                    'iPhone8,2':'iPhone 6S Plus'}

        cmd = 'ideviceinfo -k ProductType'
        p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
        out, err = p.communicate()
        try:
            __type = iTypeDic[out.decode("utf-8").strip()]
        except KeyError:
            __type = 'iPhone 8*'
        print(__type)
        return __type


if __name__ == '__main__':
    deviceInfoUtil = DeviceInfoUtil()
    print(deviceInfoUtil.getDeviceID())
