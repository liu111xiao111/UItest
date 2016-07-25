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
from com.qa.automation.appium.pages.ios.ffan.account_management_page import AccountManagementPage
from com.qa.automation.appium.pages.ios.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.ios.ffan.my_fei_fan_page import MyFeiFanPage
from com.qa.automation.appium.pages.ios.ffan.settings_page import SettingsPage
from com.qa.automation.appium.pages.ios.ffan.update_login_password_page import UpdateLoginPasswordPage
from com.qa.automation.appium.utility.logger import Logger


class UpdateLoginPasswordCases(TestCase):
    '''
    作者 宋波
    巡检checklist #57
    自动化测试 #57-1
    点击设置，在账号管理中可以成功修改登录密码，支付密码，小额免密设置
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
        updateLoginPasswordPage.inputOldLoginPassword("9875321mgw")
        updateLoginPasswordPage.inputNewLoginPassword("9875321mgw")
        updateLoginPasswordPage.inputNewLoginPasswordAgain("9875321mgw")
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
    suite = TestLoader().loadTestsFromTestCase(UpdateLoginPasswordCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
