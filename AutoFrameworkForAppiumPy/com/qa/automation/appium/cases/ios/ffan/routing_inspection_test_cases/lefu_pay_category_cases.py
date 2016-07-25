# -*- coding:utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.cases.ios.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.cases.ios.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.configs.ios_driver_configs import IosDriverConfigs as IDC
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.ios.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.ios.ffan.le_pay_details_page import LePayDetailsPage
from com.qa.automation.appium.pages.ios.ffan.le_pay_way_page import LePayWayPage
from com.qa.automation.appium.pages.ios.ffan.le_pay_page import LePayPage
from com.qa.automation.appium.utility.logger import Logger


class LefuPayCatergoryCases(TestCase):
    '''
    作者 刘涛
    巡检checklist #15
    自动化测试 #15-1
    首页进入乐付买单（城市维度），并下单，取消订单，支付（虚拟城市），并查看相应订单状态
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

        testPrepare = TestPrepare(testcase = self , driver = self.driver , logger = self.logger)
        testPrepare.prepare()

    def test_case(self):
        dashboardPage = DashboardPage(testcase=self, driver=self.driver, logger=self.logger)
        lePayPage = LePayPage(testcase=self,driver=self.driver,logger=self.logger)
        lePayDetailPage = LePayDetailsPage(self, self.driver, self.logger)
        lePayWayPage = LePayWayPage(self, self.driver, self.logger)

        # 首页点击乐付
        dashboardPage.validSelf()
        dashboardPage.click_lePay()
        lePayPage.validSelf()

        # 点击第一条乐付买单
        lePayPage.clickOnDetailsLePay()
        lePayDetailPage.validSelf()

        # 下单
        lePayDetailPage.inputMoney()
        lePayDetailPage.waitBySeconds(seconds=5)
        lePayDetailPage.clickOnPay()
        lePayWayPage.validSelf()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(LefuPayCatergoryCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)