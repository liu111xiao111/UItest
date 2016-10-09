# -*- coding:utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url
from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.android.ffan.my_fei_fan_card_page import MyFeiFanCardPage
from com.qa.automation.appium.pages.android.ffan.my_fei_fan_page import MyFeiFanPage
from com.qa.automation.appium.pages.android.ffan.payments_settings_page import PaymentsSettingsPage
from com.qa.automation.appium.pages.android.ffan.small_amount_password_less_payments_page import SmallAmountPasswordLessPaymentsPage
from com.qa.automation.appium.pages.android.ffan.transaction_record_page import TransactionRecordPage
from com.qa.automation.appium.pages.android.ffan.update_payments_password_page import UpdatePaymentsPasswordPage
from com.qa.automation.appium.utility.logger import Logger
from com.qa.automation.appium.utility.device_info_util import DeviceInfoUtil


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
        self.driver = AppiumDriver(appPackage_ffan,
                                   appActivity_ffan,
                                   platformName_andr,
                                   DeviceInfoUtil().getBuildVersion(),
                                   deviceName_andr,
                                   driver_url).getDriver()

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
        '''myFeiFanCardPage.clickOnTransactionRecord()

        transactionRecordPage = TransactionRecordPage(self, self.driver, self.logger)
        transactionRecordPage.validSelf()
        transactionRecordPage.clickBackKey()

        myFeiFanCardPage.validSelf()
        myFeiFanCardPage.clickOnPayemntsSettings()

        paymentsSettingsPage = PaymentsSettingsPage(self, self.driver, self.logger)
        paymentsSettingsPage.validSelf()
        paymentsSettingsPage.clickOnUpdatePaymentsPassword()

        updatePaymentsPasswordPage = UpdatePaymentsPasswordPage(self, self.driver, self.logger)
        updatePaymentsPasswordPage.validSelf()
        updatePaymentsPasswordPage.clickBackKey()

        paymentsSettingsPage.validSelf()
        paymentsSettingsPage.clickOnSmallAmountPasswordLessPayments()

        smallAmountPasswordLessPaymentsPage = SmallAmountPasswordLessPaymentsPage(self, self.driver, self.logger)
        smallAmountPasswordLessPaymentsPage.validSelf()
        if not smallAmountPasswordLessPaymentsPage.validSmallAmountPasswordLessPaymentsStatus():
            smallAmountPasswordLessPaymentsPage.clickOnSmallAmountPasswordLessPaymentsSwitch()
        if smallAmountPasswordLessPaymentsPage.validSmallAmountPasswordLessPaymentsStatus():
            smallAmountPasswordLessPaymentsPage.clickOnSmallAmountPasswordLessPaymentsSwitch()
        smallAmountPasswordLessPaymentsPage.clickBackKey()
        paymentsSettingsPage.clickBackKey()
        myFeiFanCardPage.clickBackKey()'''

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(OneCardCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report', description='Result for test')
    runner.run(suite)
