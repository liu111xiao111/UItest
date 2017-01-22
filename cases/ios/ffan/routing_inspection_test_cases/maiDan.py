# -*- coding:utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from cases.ios.ffan.common.testPrepare import TestPrepare
from configs.iosDriverConfig import IosDriverConfigs as IDC
from driver.appium_driver import AppiumDriver
from pages.ios.ffan.dashboard_page import DashboardPage
from pages.ios.ffan.le_pay_details_page import LePayDetailsPage
from pages.ios.ffan.le_pay_way_page import LePayWayPage
from pages.ios.ffan.le_pay_page import LePayPage
from cases.logger import logger


class MaiDanTestCase(TestCase):
    '''
    作者 刘涛
    巡检checklist #15
    自动化测试 #15-2
    首页进入乐付买单（城市维度），并下单，取消订单，支付（虚拟城市），并查看相应订单状态
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

        testPrepare = TestPrepare(testcase = self , driver = self.driver , logger = self.logger)
        testPrepare.prepare()

    def test_case(self):
        dashboardPage = DashboardPage(testcase=self, driver=self.driver, logger=self.logger)
        lePayPage = LePayPage(testcase=self,driver=self.driver,logger=self.logger)
        lePayDetailPage = LePayDetailsPage(self, self.driver, self.logger)
        lePayWayPage = LePayWayPage(self, self.driver, self.logger)

        # 首页点击乐付
        dashboardPage.validSelf()
        dashboardPage.clickOnLePay()
        lePayPage.validSelf()

        # 点击第一条乐付买单
        lePayPage.clickOnDetailsLePay()
        lePayDetailPage.validSelf()

        # 下单
        lePayDetailPage.inputMoney()
        lePayDetailPage.waitBySeconds(seconds=5)
        lePayDetailPage.clickOnPay()
        lePayWayPage.validSelf()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(MaiDanTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)
