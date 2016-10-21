# -*- coding: utf-8 -*-

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
from pages.ios.ffan.goods_details_page import GoodsDetailsPage
from pages.ios.ffan.square_module_page import SquareModulePage
from pages.ios.ffan.square_shopping_category_page import SquareShoppingPage
from utility.logger import Logger
from pages.ios.ffan.search_page import SearchPage
from pages.ios.ffan.search_result_store_page import SearchResultStorePage


class AiGouWuTestCase(TestCase):
    '''
    作者 宋波
    广场爱购物
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
        self.logger.i("tempText: " + tempText)
        goodsDetailsPage = GoodsDetailsPage(self, self.driver, self.logger)
        # 5 second,wait Appium load page
        goodsDetailsPage.waitBySeconds(5)
        goodsDetailsPage.validSelf()
        goodsDetailsPage.validKeywords(tempText)


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(AiGouWuTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'food-test_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='food-test',
                                           description='Result for test')
    runner.run(suite)
