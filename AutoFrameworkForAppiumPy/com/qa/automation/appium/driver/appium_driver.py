# -*- coding: utf-8 -*-

import os,sys
#sys.path.append(os.path.dirname(os.path.dirname(__file__)))



from time import sleep

from com.qa.automation.appium.configs.driver_configs import *

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class AppiumDriver():

    def __init__(self,app_package='com.ffan.bp.test',app_activity='.SplashActivity',
                 platform_name='Android',platform_version='4.4',device_name='Android',
                 driver_url='http://localhost:4723/wd/hub',bundle_id='com'):
        self.appPackage = app_package;
        self.appActivity = app_activity;
        self.platformName = platform_name;
        self.platformVersion = platform_version;
        self.deviceName = device_name;
        self.driver_url = driver_url;
        self.bundle_id = bundle_id

    def getDriver(self):
        # desired_caps = {}
        # desired_caps['platformName'] = self.platformName;
        # desired_caps['platformVersion'] = self.platformVersion;
        # desired_caps['deviceName'] = self.deviceName;
        # desired_caps['appPackage'] = self.appPackage;
        # desired_caps['appActivity'] = self.appActivity;
        if(self.platformName=="Android"):
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
                'appPackage': self.appPackage,
                'bundleId':self.bundle_id
        }
        return webdriver.Remote(self.driver_url, desired_caps)

    # def tearDown(self):
    #     self.driver.quit()

if __name__ == '__main__':
    pass