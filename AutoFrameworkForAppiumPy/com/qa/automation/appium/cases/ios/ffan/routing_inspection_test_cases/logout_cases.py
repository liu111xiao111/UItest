# -*- coding:utf-8 -*-

import os
import time
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from com.qa.automation.appium.cases.ios.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.ios.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.configs.ios_driver_configs import IosDriverConfigs as IDC
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.ios.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.ios.ffan.my_fei_fan_page import MyFeiFanPage
from com.qa.automation.appium.pages.ios.ffan.settings_page import SettingsPage
from com.qa.automation.appium.utility.logger import Logger


class LogoutCases(TestCase):
    '''
    作者 宋波
    巡检checklist #59
    自动化测试 #59
    退出登录，正常退出APP
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
        TestPrepare(self, self.driver, self.logger).prepare()

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.waitBySeconds()
        dashboardPage.validSelf()
        dashboardPage.clickOnMy()

        myFeiFanPage = MyFeiFanPage(self, self.driver, self.logger)
        myFeiFanPage.waitBySeconds()
        myFeiFanPage.validSelf()
        myFeiFanPage.validLoginStatus()
        myFeiFanPage.clickOnSettings()

        settingPage = SettingsPage(self, self.driver, self.logger)
        settingPage.waitBySeconds()
        settingPage.validSelf()
        settingPage.clickOnQuitAccountBtn()

        myFeiFanPage.waitBySeconds()
        myFeiFanPage.validLogoutStatus()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(LogoutCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
