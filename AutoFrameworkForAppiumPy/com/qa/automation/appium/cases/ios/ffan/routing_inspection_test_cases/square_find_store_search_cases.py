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
from com.qa.automation.appium.pages.ios.ffan.square_module_page import SquareModulePage
from com.qa.automation.appium.pages.ios.ffan.square_find_store_category_page import SquareFindStorePage
from com.qa.automation.appium.pages.ios.ffan.search_page import SearchPage;
from com.qa.automation.appium.pages.ios.ffan.search_result_store_page import SearchResultStorePage
from com.qa.automation.appium.utility.logger import Logger


class SquareFindStoreSearchCases(TestCase):
    '''
    作者 刘涛
    巡检checklist No.: 21
    自动化测试case No.: 21
    广场详情页点击找店，成功进入找店页面，并成功完成一次搜索，数据显示正常，点击门店可进入门店详情页，数据显示正常
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
        testPrepare.prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        squarePage = SquareModulePage(self, self.driver, self.logger)
        squareFindStorePage = SquareFindStorePage(self, self.driver, self.logger)
        searchPage = SearchPage(self, self.driver, self.logger)
        searchResultStorePage = SearchResultStorePage(self, self.driver, self.logger)

        # 首页进入广场页
        dashboardPage.validSelf();
        dashboardPage.clickOnSquareModule()
        squarePage.validSelf();

        # 广场页点击找店
        squarePage.clicOnFindStore()
        squareFindStorePage.validSelf()
        squareFindStorePage.clickOnSearch()

        searchPage.validSelf()
        searchPage.inputKeywords("通州")
        searchPage.clickOnSearch()
        searchPage.clickOnSearchResultFirstItem()

        searchResultStorePage.validSelf()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(SquareFindStoreSearchCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'food-test_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='food-test',
                                           description='Result for test')
    runner.run(suite)