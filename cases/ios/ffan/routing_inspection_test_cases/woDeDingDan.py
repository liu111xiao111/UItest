# -*- coding:utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader
from cases.logger import logger
from driver.appium_driver import AppiumDriver
from cases.ios.ffan.common.clearAppData import ClearAppData
from configs.iosDriverConfig import IosDriverConfigs as IDC
from cases.ios.ffan.common.testPrepare import TestPrepare
from pages.ios.ffan.my_ffan_page import MyFfanPage
from pages.ios.ffan.my_ffan_my_order_page import MyFfanMyOrderPage
from pages.ios.ffan.dashboard_page import DashboardPage


class WoDeDingDanTestCase(TestCase):
    '''
    作者 刘涛
    我的订单
    '''

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

    def setUp(self):
        self.logger = logger
        self.driver = AppiumDriver(None,
                                   None,
                                   IDC.platformName,
                                   IDC.platformVersion,
                                   IDC.deviceName,
                                   IDC.driverUrl,
                                   IDC.bundleId,
                                   IDC.udid).getDriver()
        logger.info("Appium client init completed")

        self.reset = ClearAppData(self.driver)
        self.reset.clearData()
        logger.info("Clear data completed")

        testPrepare = TestPrepare(testcase = self , driver = self.driver , logger = self.logger)
        testPrepare.prepare()

    def test_case(self):
        dashboardPage = DashboardPage(testcase=self, driver=self.driver, logger=self.logger)
        myFfanPage = MyFfanPage(self, self.driver, self.logger)
        myOrderPage = MyFfanMyOrderPage(self, self.driver, self.logger)


        #点击我的
        dashboardPage.clickOnMy()
        myFfanPage.validSelf()
        #点击我的订单
        myFfanPage.clickOnMyOrder()
        myOrderPage.validSelf()
        myOrderPage.clickBackKey()

        #myOrderPage.clickOnDaifukuan()






if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(WoDeDingDanTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)