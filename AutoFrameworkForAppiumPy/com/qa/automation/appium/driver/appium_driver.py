# -*- coding: utf-8 -*-

from appium import webdriver


class AppiumDriver():

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




if __name__ == '__main__':
    appiumDriver = AppiumDriver(platform_name="iOS",platform_version="9.3.1",device_name='iPhone',bundle_id="com.dianshang.wanhui",ios_udid="94f6c2802867d75fbca745af712e03b7f72d4cc1")
    appiumDriver.getDriver();
