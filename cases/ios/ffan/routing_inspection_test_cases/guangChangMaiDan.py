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
from pages.ios.ffan.le_pay_page import LePayPage
from pages.ios.ffan.search_page import SearchPage
from pages.ios.ffan.square_module_page import SquareModulePage
from cases.logger import logger


class GuangChangMaiDanTestCase(TestCase):
    '''
    作者 刘涛
    巡检checklist #27
    自动化测试 #27
    广场详情页点击进入乐付买单
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

        testPrepare = TestPrepare(testcase=self , driver=self.driver , logger=self.logger)
        testPrepare.prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        searchPage = SearchPage(self, self.driver, self.logger)
        squareModulePage = SquareModulePage(self, self.driver, self.logger)
        lePayPage = LePayPage(self, self.driver, self.logger)

        # 首页选择北京通州万达广场
        dashboardPage.validSelf()
        dashboardPage.clickOnSearchAll()
        searchPage.validSelf()
        searchPage.inputKeywords(u"北京通州万达广场")
        searchPage.clickOnSearch()
        searchPage.clickOnSpecificSquare()
        squareModulePage.validSelf()

        # 点击 "乐付买单"
        squareModulePage.clicOnLefuPay();
        lePayPage.validSelf()
        lePayPage.clickOnDetailsLePay()
        lePayPage.inputSumOfConsumption()
        lePayPage.clickOnConfirmPurchase()
        lePayPage.clickBackKey()
        lePayPage.clickOnConfirmCancel()

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(GuangChangMaiDanTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)
