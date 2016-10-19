# -*- coding: utf-8 -*-

import os
import time
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from cases.ios.ffan.common.clearAppData import ClearAppData
from cases.ios.ffan.common.testPrepare import TestPrepare
from configs.ios_driver_configs import IosDriverConfigs as IDC
from driver.appium_driver import AppiumDriver
from pages.ios.ffan.dashboard_page import DashboardPage
from pages.ios.ffan.login_page import LoginPage
from pages.ios.ffan.my_fei_fan_page import MyFeiFanPage
from utility.logger import Logger
from pages.ios.ffan.settings_page import SettingsPage


class WoDeDengLuTestCase(TestCase):
    '''
    作者 宋波
    巡检checklist #48
    自动化测试 #48
    启动app，能够正常登陆
    '''

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(None, None, IDC.platformName, IDC.platformVersion,
                                   IDC.deviceName, IDC.driverUrl, IDC.bundleId, IDC.udid).getDriver()
        self.reset = ClearAppData(self.driver)
        self.reset.clearData()
        TestPrepare(self, self.driver, self.logger).prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnMy()

        myFeiFanPage = MyFeiFanPage(self, self.driver, self.logger)
        myFeiFanPage.validSelf()
        if myFeiFanPage.validLoginStatus(False):
            myFeiFanPage.clickOnSettings()

            settingPage = SettingsPage(self, self.driver, self.logger)
            settingPage.waitBySeconds()
            settingPage.validSelf()
            settingPage.clickOnQuitAccountBtn()

            myFeiFanPage.waitBySeconds()
            myFeiFanPage.validLogoutStatus()
        myFeiFanPage.clickOnLogin()

        loginPage = LoginPage(self, self.driver, self.logger)
        loginPage.validSelf()
        loginPage.switchToNormalLogin()
        loginPage.inputUserName()
        loginPage.inputPassWord()
        loginPage.clickOnLoginBtn()

        #verificationPage = VerificationPage(self, self.driver, self.logger)
        #verificationPage.validSelf()
        #verificationPage.clickOnSkip()

        myFeiFanPage.waitBySeconds(5)
        myFeiFanPage.validLoginStatus()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(WoDeDengLuTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)
