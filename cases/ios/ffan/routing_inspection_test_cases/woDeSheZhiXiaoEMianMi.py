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
from pages.ios.ffan.my_fei_fan_page import MyFeiFanPage
from pages.ios.ffan.settings_page import SettingsPage
from pages.ios.ffan.small_amount_password_less_payments_page import SmallAmountPasswordLessPaymentsPage
from cases.logger import logger


class WoDeSheZhiXiaoEMianMiTestCase(TestCase):
    '''
    作者 宋波
    巡检checklist #57
    自动化测试 #57-2
    点击设置，在账号管理中可以成功修改登录密码，支付密码，小额免密设置
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
        dashboardPage.validSelf()
        dashboardPage.clickOnMy()

        myFeiFanPage = MyFeiFanPage(self, self.driver, self.logger)
        myFeiFanPage.validSelf()
        myFeiFanPage.validLoginStatus()
        myFeiFanPage.clickOnSettings()

        settingPage = SettingsPage(self, self.driver, self.logger)
        settingPage.validSelf()
        #settingPage.clickOnAccountManagement()
        #点击支付设置
        settingPage.clickOnPaySettings()
        #点击免支付密
        settingPage.clickOnMianmiPaySettings()


        # accountManagementPage = AccountManagementPage(self, self.driver, self.logger)
        # accountManagementPage.validSelf()
        # accountManagementPage.clickOnSmallAmountPasswordLessPayments()

        smallAmountPasswordLessPaymentsPage = SmallAmountPasswordLessPaymentsPage(self, self.driver, self.logger)
        smallAmountPasswordLessPaymentsPage.validSelf()
        if not smallAmountPasswordLessPaymentsPage.validSmallAmountPasswordLessPaymentsStatus():
            smallAmountPasswordLessPaymentsPage.clickOnSmallAmountPasswordLessPaymentsSwitch()
        if smallAmountPasswordLessPaymentsPage.validSmallAmountPasswordLessPaymentsStatus():
            smallAmountPasswordLessPaymentsPage.clickOnSmallAmountPasswordLessPaymentsSwitch()
        smallAmountPasswordLessPaymentsPage.clickBackKey()

        #accountManagementPage.validSelf()
        settingPage.clickBackKey()

        settingPage.validSelf()
        settingPage.clickBackKey()

        myFeiFanPage.validSelf()

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(WoDeSheZhiXiaoEMianMiTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
