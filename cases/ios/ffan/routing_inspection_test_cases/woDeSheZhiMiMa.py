# -*- coding:utf-8 -*-

import os
import time
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from cases.ios.ffan.common.clearAppData import ClearAppData
from cases.ios.ffan.common.testPrepare import TestPrepare
from configs.iosDriverConfig import IosDriverConfigs as IDC
from driver.appium_driver import AppiumDriver
from pages.ios.ffan.account_management_page import AccountManagementPage
from pages.ios.ffan.dashboard_page import DashboardPage
from pages.ios.ffan.my_fei_fan_page import MyFeiFanPage
from pages.ios.ffan.settings_page import SettingsPage
from pages.ios.ffan.update_login_password_page import UpdateLoginPasswordPage
from utility.logger import Logger


class WoDeSheZhiMiMaTestCase(TestCase):
    '''
    我的设置
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
        settingPage.clickOnAccountManagement()

        accountManagementPage = AccountManagementPage(self, self.driver, self.logger)
        accountManagementPage.waitBySeconds()
        accountManagementPage.validSelf()
        accountManagementPage.clickOnUpdatePassword()

        updateLoginPasswordPage = UpdateLoginPasswordPage(self, self.driver, self.logger)
        updateLoginPasswordPage.waitBySeconds()
        updateLoginPasswordPage.validSelf()
        updateLoginPasswordPage.inputOldLoginPassword("liutao-123qwe")
        updateLoginPasswordPage.inputNewLoginPassword("liutao-123qwe")
        updateLoginPasswordPage.inputNewLoginPasswordAgain("liutao-123qwe")
        updateLoginPasswordPage.clickOnConfirm()

        accountManagementPage.waitBySeconds()
        accountManagementPage.validSelf()
        accountManagementPage.clickBackKey()

        settingPage.waitBySeconds()
        settingPage.validSelf()
        settingPage.clickBackKey()

        myFeiFanPage.waitBySeconds()
        myFeiFanPage.validSelf()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(WoDeSheZhiMiMaTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
