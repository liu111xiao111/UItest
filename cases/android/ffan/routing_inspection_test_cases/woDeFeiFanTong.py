# -*- coding:utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from cases.android.ffan.common.clear_app_data import ClearAppData
from cases.android.ffan.common.test_prepare import TestPrepare
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from configs.driver_configs import platformName_andr
from driver.appium_driver import AppiumDriver
from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.my_fei_fan_card_page import MyFeiFanCardPage
from pages.android.ffan.my_fei_fan_page import MyFeiFanPage
from pages.android.ffan.payments_settings_page import PaymentsSettingsPage
from pages.android.ffan.small_amount_password_less_payments_page import SmallAmountPasswordLessPaymentsPage
from pages.android.ffan.transaction_record_page import TransactionRecordPage
from pages.android.ffan.update_payments_password_page import UpdatePaymentsPasswordPage
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil


class WoDeFeiFanTongTestCase(TestCase):
    '''
    巡检 No.56
    用例名 我的飞凡通
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

    def testWoDeFeiFanTong(self):
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
    suite = TestLoader().loadTestsFromTestCase(WoDeFeiFanTongTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report', description='Result for test')
    runner.run(suite)
