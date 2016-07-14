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
from com.qa.automation.appium.pages.ios.ffan.small_amount_password_less_payments_page import SmallAmountPasswordLessPaymentsPage
from com.qa.automation.appium.utility.logger import Logger


class SmallAmountPasswordLessPaymentCases(TestCase):
    '''
    巡检checklist No.: 57
    自动化测试case No.: 57_1
    点击设置，在账号管理中可以成功修改登录密码，支付密码，小额免密设置
    '''


    def tearDown(self):
        self.driver.quit()
        ClearAppData().clearData()

    def setUp(self):
        ClearAppData().clearData()
        self.logger = Logger()
        self.driver = AppiumDriver(None, None, IDC.platformName, IDC.platformVersion,
                                   IDC.deviceName, IDC.driverUrl, IDC.bundleId, IDC.udid).getDriver()
#         TestPrepare(self, self.driver, self.logger).prepare()

    def test_case(self):
        dashboardPage = DashboardPage(self , self.driver , self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnMy()

        myFeiFanPage = MyFeiFanPage(self, self.driver, self.logger)
        myFeiFanPage.validSelf()
        myFeiFanPage.validLoginStatus()
        myFeiFanPage.clickOnSettings()

        settingPage = SettingsPage(self, self.driver, self.logger)
        settingPage.validSelf()
        settingPage.clickOnAccountManagement()

        accountManagementPage = AccountManagementPage(self, self.driver, self.logger)
        accountManagementPage.validSelf()
        accountManagementPage.clickOnSmallAmountPasswordLessPayments()

        smallAmountPasswordLessPaymentsPage = SmallAmountPasswordLessPaymentsPage(self, self.driver, self.logger)
        smallAmountPasswordLessPaymentsPage.validSelf()
        if not smallAmountPasswordLessPaymentsPage.validSmallAmountPasswordLessPaymentsStatus():
            smallAmountPasswordLessPaymentsPage.clickOnSmallAmountPasswordLessPaymentsSwitch()
        if smallAmountPasswordLessPaymentsPage.validSmallAmountPasswordLessPaymentsStatus():
            smallAmountPasswordLessPaymentsPage.clickOnSmallAmountPasswordLessPaymentsSwitch()
        smallAmountPasswordLessPaymentsPage.clickBackKey()

        accountManagementPage.validSelf()
        accountManagementPage.clickBackKey()

        settingPage.validSelf()
        settingPage.clickBackKey()

        myFeiFanPage.validSelf()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(SmallAmountPasswordLessPaymentCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
