# -*- coding: utf-8 -*-


from com.qa.automation.appium.pages.android.ffan.dashboard_page import *;
from com.qa.automation.appium.pages.android.ffan.my_ffan_page import *;
from com.qa.automation.appium.pages.android.ffan.settings_page import *;
from com.qa.automation.appium.pages.android.ffan.login_page import *;
from com.qa.automation.appium.configs.driver_configs import *;
from com.qa.automation.appium.driver.appium_driver import *;
from com.qa.automation.appium.utility.logger import Logger;
from com.qa.automation.appium.utility.device_info_util import *;
from com.qa.automation.appium.cases.android.ffan.common.test_prepare import *

import unittest
import HTMLTestRunner


class MyFfanCases(unittest.TestCase):
    '''
        备注：原始版本的case，暂没作修改
    '''

    def tearDown(self):
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        deviceInfoUtil = DeviceInfoUtil();
        platform_Version = deviceInfoUtil.getBuildVersion();
        self.driver = AppiumDriver(app_package=appPackage_ffan, app_activity=appActivity_ffan,
                                   platform_name=platformName_andr, platform_version=platform_Version,
                                   device_name=deviceName_andr, driver_url=driver_url
                                   ).getDriver()

    def test_login(self):
        testPrepare = TestPrepare(testcase=self,driver=self.driver,logger=self.logger)
        testPrepare.validLogoutStatus()
        testPrepare.backToDashBoard()

        dashboardPage = DashboardPage(testcase=self, driver=self.driver, logger=self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnMy()
        myFfanPage = MyFfanPage(testcase=self, driver=self.driver, logger=self.logger)
        myFfanPage.validSelf()
        myFfanPage.clickOnLogin()
        loginPage = LoginPage(testcase=self, driver=self.driver, logger=self.logger)
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
        dashboardPage.waitBySeconds(seconds=2);

    def test_logout(self):
        dashboardPage = DashboardPage(testcase=self, driver=self.driver, logger=self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnMy()
        myFfanPage = MyFfanPage(testcase=self, driver=self.driver, logger=self.logger)
        myFfanPage.validSelf()
        myFfanPage.waitBySeconds(seconds=2)
        myFfanPage.clickOnSettings()
        settingPage = SettingsPage(testcase=self, driver=self.driver, logger=self.logger)
        settingPage.validSelf()
        settingPage.clickOnQuitAccountBtn()
        myFfanPage.waitBySeconds(seconds=2)


if __name__ == "__main__":
    print("path is %s." % (sys.path))
