# -*- coding:utf-8 -*-

import os
import sys
import time

sys.path.append(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))))

from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.configs.ios_driver_configs import IosDriverConfigs as IDC
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.ios.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.ios.ffan.le_pay_details_page import LePayDetailsPage
from com.qa.automation.appium.pages.ios.ffan.le_pay_way_page import LePayWayPage
from com.qa.automation.appium.pages.ios.ffan.le_pay_page import LePayPage
from com.qa.automation.appium.utility.logger import Logger

from unittest import TestCase
from unittest import TestLoader
import HTMLTestRunner


class LefuPayCatergoryCases(TestCase):
    '''
        巡检checklist #15
        自动化测试 #15-1
        首页进入乐付买单（城市维度），并下单，取消订单，支付（虚拟城市），并查看相应订单状态
    '''

    def tearDown(self):
        self.driver.quit()
        ClearAppData().clearData()

    def setUp(self):
        ClearAppData().clearData()
        self.logger = Logger()
        self.driver = AppiumDriver(None, None, IDC.platformName, IDC.platformVersion,
                                   IDC.deviceName, IDC.driverUrl, IDC.bundleId, IDC.udid).getDriver()

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