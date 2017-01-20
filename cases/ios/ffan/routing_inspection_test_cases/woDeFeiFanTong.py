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
from pages.ios.ffan.dashboard_page import DashboardPage
from pages.ios.ffan.my_fei_fan_card_page import MyFeiFanCardPage
from pages.ios.ffan.my_fei_fan_page import MyFeiFanPage
from cases.logger import logger


class WoDeFeiFanTongTestCase(TestCase):
    '''
    我的飞凡通
    '''

    @classmethod
    def setUpClass(cls):
        '''
        初始化Appium driver
        '''

        cls.driver = AppiumDriver(None,
                                  None,
                                  IDC.platformName,
                                  IDC.platformVersion,
                                  IDC.deviceName,
                                  IDC.driverUrl,
                                  IDC.bundleId,
                                  IDC.udid).getDriver()
        logger.info("Appium client init completed")


    def setUp(self):
        self.logger = logger
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
        
        myFeiFanCardPage.clickOnLinghuaqian()
        myFeiFanCardPage.validLinghuaqian()
        
        '''
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
            paymentsSettingsPage.clickBackKey()
            myFeiFanCardPage.clickBackKey()
        '''

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(WoDeFeiFanTongTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
