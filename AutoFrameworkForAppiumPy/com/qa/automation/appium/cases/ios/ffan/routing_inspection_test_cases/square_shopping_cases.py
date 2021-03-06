# -*- coding: utf-8 -*-

import os
import time
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from com.qa.automation.appium.cases.ios.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.ios.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.configs.ios_driver_configs import IosDriverConfigs as IDC
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.ios.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.ios.ffan.goods_details_page import GoodsDetailsPage
from com.qa.automation.appium.pages.ios.ffan.square_module_page import SquareModulePage
from com.qa.automation.appium.pages.ios.ffan.square_shopping_category_page import SquareShoppingPage
from com.qa.automation.appium.utility.logger import Logger
from com.qa.automation.appium.pages.ios.ffan.search_page import SearchPage
from com.qa.automation.appium.pages.ios.ffan.search_result_store_page import SearchResultStorePage


class SquareShoppingCases(TestCase):
    '''
    作者 宋波
    巡检checklist #32
    自动化测试 #32
    广场详情页点击爱购物，进入购物模块，数据显示正常
    '''

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(None, None, IDC.platformName, IDC.platformVersion,
                                   IDC.deviceName, IDC.driverUrl, IDC.bundleId, IDC.udid).getDriver()
        self.reset = ClearAppData(self.driver)
        self.reset.clearData()
        TestPrepare(self, self.driver, self.logger).prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        searchPage = SearchPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnSearchAll()
        searchPage.inputKeywords(u"北京通州万达广场")
        searchPage.clickOnSearch()
        searchPage.clickOnSpecificSquare()
        
        # searchPage = SearchPage(self, self.driver, self.logger)
        # searchPage.validSelf()
        # searchPage.inputStoreName()
        # searchPage.clickOnSearch()
        # searchPage.clickOnSearchResultFirstItem()

        # searchResultStorePage = SearchResultStorePage(self, self.driver, self.logger)
        # searchResultStorePage.validSelf()

        squareModulePage = SquareModulePage(self, self.driver, self.logger)
        squareModulePage.validSelf()
        squareModulePage.clickOnBornToShop()

        squareShoppingPage = SquareShoppingPage(self, self.driver, self.logger)
        squareShoppingPage.validSelf()
        tempText = squareShoppingPage.clickOnSubCommodity()

        goodsDetailsPage = GoodsDetailsPage(self, self.driver, self.logger)
        #5 second,wait Appium load page
        goodsDetailsPage.waitBySeconds(5)
        goodsDetailsPage.validSelf()
        goodsDetailsPage.validKeywords(tempText)


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(SquareShoppingCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'food-test_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='food-test',
                                           description='Result for test')
    runner.run(suite)
