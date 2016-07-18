# -*- coding:utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.cases.ios.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.ios.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.configs.ios_driver_configs import IosDriverConfigs as IDC
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.ios.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.ios.ffan.my_fei_fan_card_page import MyFeiFanCardPage
from com.qa.automation.appium.pages.ios.ffan.my_fei_fan_page import MyFeiFanPage
from com.qa.automation.appium.pages.ios.ffan.payments_password_management_page import PaymentsPasswordManagementPage
from com.qa.automation.appium.pages.ios.ffan.payments_settings_page import PaymentsSettingsPage
from com.qa.automation.appium.pages.ios.ffan.small_amount_password_less_payments_page import SmallAmountPasswordLessPaymentsPage
from com.qa.automation.appium.pages.ios.ffan.transaction_record_page import TransactionRecordPage
from com.qa.automation.appium.utility.logger import Logger


class OneCardCases(TestCase):
    '''
    巡检checklist No.: 53
    自动化测试case No.: 53
    点击进入我的一卡通验证付款码显示正常交易记录显示正常，可以进行支付密码设置和小额免密开关
    '''

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(None,
                                   None,
                                   IDC.platformName,
                                   IDC.platformVersion,
                                   IDC.deviceName,
                                   IDC.driverUrl,
                                   IDC.bundleId,
                                   IDC.udid).getDriver()

        self.reset = ClearAppData(self.driver)
        self.reset.clearData()

        TestPrepare(self, self.driver, self.logger).prepare()

    def test_case(self):
        dashboardPage = DashboardPage(self , self.driver , self.logger)
        dashboardPage.waitBySeconds()
        dashboardPage.validSelf()
        dashboardPage.clickOnMy()

        myFeiFanPage = MyFeiFanPage(self, self.driver, self.logger)
        myFeiFanPage.waitBySeconds()
        myFeiFanPage.validSelf()
        myFeiFanPage.clickOnMyFeiFanCard()

        myFeiFanCardPage = MyFeiFanCardPage(self, self.driver, self.logger)
        myFeiFanCardPage.validSelf()
        myFeiFanCardPage.clickOnTransactionRecord()

        transactionRecordPage = TransactionRecordPage(self, self.driver, self.logger)
        transactionRecordPage.validSelf()
        transactionRecordPage.clickBackKey()

        myFeiFanCardPage.validSelf()
        myFeiFanCardPage.clickOnPayemntsSettings()

        paymentsSettingsPage = PaymentsSettingsPage(self, self.driver, self.logger)
        paymentsSettingsPage.validSelf()
        paymentsSettingsPage.clickOnPaymentsPasswordManagement()

        paymentsPasswordManagementPage = PaymentsPasswordManagementPage(self, self.driver, self.logger)
        paymentsPasswordManagementPage.validSelf()
        paymentsPasswordManagementPage.clickBackKey()

        paymentsSettingsPage.validSelf()
        paymentsSettingsPage.clickOnSmallAmountPasswordLessPayments()

        smallAmountPasswordLessPaymentsPage = SmallAmountPasswordLessPaymentsPage(self, self.driver, self.logger)
        smallAmountPasswordLessPaymentsPage.validSelf()
        if not smallAmountPasswordLessPaymentsPage.validSmallAmountPasswordLessPaymentsStatus():
            smallAmountPasswordLessPaymentsPage.clickOnSmallAmountPasswordLessPaymentsSwitch()
        if smallAmountPasswordLessPaymentsPage.validSmallAmountPasswordLessPaymentsStatus():
            smallAmountPasswordLessPaymentsPage.clickOnSmallAmountPasswordLessPaymentsSwitch()
        smallAmountPasswordLessPaymentsPage.clickBackKey()

        paymentsSettingsPage.validSelf()
        paymentsSettingsPage.clickBackKey()

        myFeiFanCardPage.validSelf()
        myFeiFanCardPage.clickBackKey()

        myFeiFanPage.validSelf()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(OneCardCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
