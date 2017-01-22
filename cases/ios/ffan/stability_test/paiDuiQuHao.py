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
from pages.ios.ffan.square_module_page import SquareModulePage
from pages.ios.ffan.square_queue_page import SquareQueuePage
from cases.logger import logger
from pages.ios.ffan.search_page import SearchPage


class PaiDuiQuHaoTestCase(TestCase):
    '''
    作者 刘涛
    巡检checklist: No.24
    自动化测试: No.24
    广场详情页点击排队取号进入排队取号页面，可以成功排队
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

        testPrepare = TestPrepare(testcase=self , driver=self.driver , logger=self.logger)
        testPrepare.prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        searchPage = SearchPage(self, self.driver, self.logger)
        squareModulePage = SquareModulePage(self, self.driver, self.logger)

        dashboardPage.validSelf()

        # 首页选择北京通州万达广场
        dashboardPage.validSelf()
        dashboardPage.clickOnSearchAll()
        searchPage.validSelf()
        searchPage.inputKeywords(u"北京通州万达广场")
        searchPage.clickOnSearch()
        searchPage.clickOnSpecificSquare()
        squareModulePage.validSelf()

        squarePage = SquareModulePage(self, self.driver, self.logger)
        squarePage.validSelf()
        squarePage.clicOnPaiDui()

        queuePage = SquareQueuePage(self, self.driver, self.logger)
        queuePage.validSelf()
        if queuePage.validKeyword(u"取号"):
            pass


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(PaiDuiQuHaoTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)
