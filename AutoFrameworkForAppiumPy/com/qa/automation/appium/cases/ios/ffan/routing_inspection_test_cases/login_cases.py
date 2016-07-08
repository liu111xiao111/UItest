#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from com.qa.automation.appium.cases.ios.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.ios.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.configs.ios_driver_configs import IosDriverConfigs as IDC
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.ios.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.ios.ffan.login_page import LoginPage
from com.qa.automation.appium.pages.ios.ffan.my_ffan_page import MyFfanPage
from com.qa.automation.appium.utility.logger import Logger


sys.path.append(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))))


class LoginCases(TestCase):
    '''
    This is a test case for login.
    '''

    def tearDown(self):
        self.driver.quit()
        ClearAppData().clearData()

    def setUp(self):
        ClearAppData().clearData()
        self.logger = Logger()
        self.driver = AppiumDriver(None, None, IDC.platformName, IDC.platformVersion,
                                   IDC.deviceName, IDC.driverUrl, IDC.bundleId, IDC.udid).getDriver()

        TestPrepare(self, self.driver, self.logger).prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.valid_self()
        dashboardPage.click_my()

        myFfanPage = MyFfanPage(self, self.driver, self.logger)
        myFfanPage.validSelf()
        myFfanPage.clickOnLogin()

        loginPage = LoginPage(self, self.driver, self.logger)
        loginPage.validSelf()
        loginPage.switchToNormalLogin()
        loginPage.inputUserName()
        loginPage.inputPassWord()
        loginPage.clickOnLoginBtn()
        loginPage.wait_by_seconds(5)

        myFfanPage.validSelf()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(LoginCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)
