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
from pages.ios.ffan.square_module_page import SquareModulePage
from pages.ios.ffan.square_food_category_page import SquareFoodPage
from pages.ios.ffan.search_page import SearchPage
from pages.ios.ffan.search_result_store_page import SearchResultStorePage
from cases.logger import logger


class GuangChangMeiShiHuiTestCase(TestCase):
    '''
    作者 刘涛
    巡检checklist #31
    自动化测试 #31
    广场详情页点击美食汇正常进入餐饮模块，数据显示正常可点击进入
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

        testPrepare = TestPrepare(testcase=self, driver=self.driver, logger=self.logger)
        testPrepare.prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        squarePage = SquareModulePage(self, self.driver, self.logger)
        squareFoodPage = SquareFoodPage(self, self.driver, self.logger)

        # 首页进入广场页
        dashboardPage.validSelf()
        dashboardPage.clickOnSearchAll()

        searchPage = SearchPage(self, self.driver, self.logger)
        searchPage.validSelf()
        searchPage.inputStoreName()
        searchPage.clickOnSearch()
        searchPage.clickOnSearchResultFirstItem()

        searchResultStorePage = SearchResultStorePage(self, self.driver, self.logger)
        searchResultStorePage.validSelf()

        # 点击 "美食汇"
        squarePage.clickOnFood()
        squareFoodPage.validSelf()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(GuangChangMeiShiHuiTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'food-test_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='food-test',
                                           description='Result for test')
    runner.run(suite)
