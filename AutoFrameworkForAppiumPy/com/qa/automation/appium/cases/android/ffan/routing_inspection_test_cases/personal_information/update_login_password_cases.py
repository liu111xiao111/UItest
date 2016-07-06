#!/usr/bin/env python
# -*- coding:utf-8 -*-


import os
import sys
import time
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url
from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.configs.driver_configs import platformVersion
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.android.ffan.account_management_page import AccountManagementPage
from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.android.ffan.my_fei_fan_page import MyFeiFanPage
from com.qa.automation.appium.pages.android.ffan.settings_page import SettingsPage
from com.qa.automation.appium.pages.android.ffan.update_login_password_page import UpdateLoginPasswordPage
from com.qa.automation.appium.utility.logger import Logger

sys.path.append(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))))


class UpdateLoginPasswordCases(TestCase):
    '''
    巡检checklist No.: 57
    自动化测试case No.: 57
    点击设置，在账号管理中可以成功修改登录密码，支付密码，小额免密设置
    '''

    def tearDown(self):
        self.driver.quit()
        ClearAppData().clearData()

    def setUp(self):
        ClearAppData().clearData()
        self.logger = Logger()
        self.driver = AppiumDriver(appPackage_ffan, appActivity_ffan, platformName_andr, platformVersion,
                                   deviceName_andr, driver_url).getDriver()
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

        settingPage.waitBySeconds()
        myFeiFanPage.validSelf()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(UpdateLoginPasswordCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
