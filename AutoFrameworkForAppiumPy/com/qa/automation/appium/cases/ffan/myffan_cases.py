# -*- coding: utf-8 -*-

import sys,os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))))

from com.qa.automation.appium.pages.ffan.dashboard_page import *;
from com.qa.automation.appium.pages.ffan.my_ffan_page import *;
from com.qa.automation.appium.pages.ffan.login_page import *;
from com.qa.automation.appium.configs.driver_configs import *;
from com.qa.automation.appium.driver.appium_driver import *;
from com.qa.automation.appium.utility.logger import Logger;

import unittest
import HTMLTestRunner

class MyFfanCases(unittest.TestCase):

    def tearDown(self):
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(app_package=appPackage_ffan, app_activity=appActivity_ffan,
                                   platform_name=platformName_andr, platform_version=platformVersion,
                                   device_name=deviceName_andr, driver_url=driver_url
                                   ).getDriver()

    def test_login(self):
        dashboardPage = DashboardPage(testcase = self , driver = self.driver , logger = self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnMy()
        myFfanPage = MyFfanPage(testcase=self,driver=self.driver,logger=self.logger)
        myFfanPage.validSelf()
        myFfanPage.clickOnLogin()
        loginPage = LoginPage(testcase=self,driver=self.driver,logger=self.logger)
        loginPage.validSelf()
        loginPage.waitBySeconds(seconds=2)
        loginPage.switchToNormalLogin()
        loginPage.inputUserName();
        loginPage.waitBySeconds(seconds=1)
        loginPage.inputPassWord()
        loginPage.waitBySeconds(seconds=1)
        loginPage.clickOnLoginBtn();
        loginPage.waitBySeconds(seconds=3)
        myFfanPage.validLoginStatus()
        dashboardPage.waitBySeconds(seconds=10);


if __name__ == "__main__":
    pass