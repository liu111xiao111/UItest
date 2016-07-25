# -*- coding: utf-8 -*-

from appium import webdriver


class AppiumDriver():
    '''
    Appium Dirver初始化
    '''
    def __init__(self, app_package='com.ffan.bp.test', app_activity='.SplashActivity',
                 platform_name='Android', platform_version='4.4', device_name='Android',
                 driver_url='http://localhost:4723/wd/hub', bundle_id='com.dianshang.wanhui',ios_udid=""):
        self.appPackage = app_package;
        self.appActivity = app_activity;
        self.platformName = platform_name;
        self.platformVersion = platform_version;
        self.deviceName = device_name;
        self.driver_url = driver_url;
        self.bundle_id = bundle_id
        self.ios_udid = ios_udid

    def getDriver(self):
        '''
        usage: 获取driver方法
        '''
        if (self.platformName == "Android"):
            desired_caps = {
                'platformName': self.platformName,
                'platformVersion': self.platformVersion,
                'deviceName': self.deviceName,
                'appPackage': self.appPackage,
                'appActivity': self.appActivity,
                'unicodeKeyboard': 'True',
                'resetKeyboard': 'True'
            }
        else:
            desired_caps = {
                'platformName': self.platformName,
                'platformVersion': self.platformVersion,
                'deviceName': self.deviceName,
                'bundleId': self.bundle_id,
                'udid' : self.ios_udid
            }
        #print("desired caps %s" % (desired_caps));
        return webdriver.Remote(self.driver_url, desired_caps)
