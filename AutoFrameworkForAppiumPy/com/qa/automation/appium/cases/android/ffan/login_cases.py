# -*- coding: utf-8 -*-

import sys, os

sys.path.append(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))))

from com.qa.automation.appium.pages.android.ffan.dashboard_page import *;
from com.qa.automation.appium.pages.android.ffan.my_ffan_page import *;
from com.qa.automation.appium.configs.driver_configs import *;
from com.qa.automation.appium.driver.appium_driver import *;
from com.qa.automation.appium.utility.logger import Logger;
from com.qa.automation.appium.pages.android.ffan.login_page import *;
from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData

import unittest
import HTMLTestRunner


class LoginCases(unittest.TestCase):
    '''
        usage: 登陆case
    '''

    def tearDown(self):
        self.driver.quit()
        # clearAppData = ClearAppData()
        # clearAppData.clearData()

    def setUp(self):
        clearAppData = ClearAppData()
        clearAppData.clearData()

        self.logger = Logger()
        self.driver = AppiumDriver(app_package=appPackage_ffan, app_activity=appActivity_ffan,
                                   platform_name=platformName_andr, platform_version=platformVersion,
                                   device_name=deviceName_andr, driver_url=driver_url
                                   ).getDriver()
        # 登陆　升级
        testPrepare = TestPrepare(testcase=self, driver=self.driver, logger=self.logger)
        testPrepare.prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(testcase=self, driver=self.driver, logger=self.logger)
        myFfanPage = MyFfanPage(testcase=self, driver=self.driver, logger=self.logger)

        dashboardPage.clickOnMy()
        myFfanPage.clickOnLogin()
        loginPage = LoginPage(testcase=self, driver=self.driver, logger=self.logger)
        loginPage.validSelf()
        # loginPage.waitBySeconds(seconds=2)
        loginPage.switchToNormalLogin()
        loginPage.inputUserName();
        # loginPage.waitBySeconds(seconds=1)
        loginPage.inputPassWord()
        # loginPage.waitBySeconds(seconds=1)
        loginPage.clickOnLoginBtn();
        # loginPage.waitBySeconds(seconds=3)
        # dashboardPage.validSelf()
        # dashboardPage.clickOnMy()
        myFfanPage.validSelf()
        # myFfanPage.validLoginStatus()
        dashboardPage.waitBySeconds(seconds=2);


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)
