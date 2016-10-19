# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from cases.android.ffan.common.clear_app_data import ClearAppData
from cases.android.ffan.common.test_prepare import TestPrepare
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from configs.driver_configs import platformName_andr
from driver.appium_driver import AppiumDriver
from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.goods_details_page import GoodsDetailsPage
from pages.android.ffan.square_module_page import SquareModulePage
from pages.android.ffan.search_page import SearchPage
from pages.android.ffan.square_shopping_category_page import SquareShoppingPage
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil


class GuangChangAiGouWuTestCase(TestCase):
    '''
    巡检 No.34
    用例名 广场爱购物
    广场详情页点击爱购物，进入购物模块，数据显示正常
    '''

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(appPackage_ffan,
                                   appActivity_ffan,
                                   platformName_andr,
                                   DeviceInfoUtil().getBuildVersion(),
                                   deviceName_andr,
                                   driver_url).getDriver()

        self.reset = ClearAppData(self.driver)
        self.reset.clearData()

        TestPrepare(self, self.driver, self.logger).prepare(False)

    def testGuangChangAiGouWu(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        searchPage = SearchPage(self, self.driver, self.logger)
        squarePage = SquareModulePage(self, self.driver, self.logger)

        # 绑定北京通州万达广场
        dashboardPage.validSelf()
        dashboardPage.clickOnSearchView()
        searchPage.validSelf()
        searchPage.inputText("北京通州万达广场")
        searchPage.clickOnSearch()
        searchPage.waitBySeconds(10)
        searchPage.clickOnSearchResultFirstItem()
        squarePage.validSelf()
        squarePage.waitBySeconds(10)
        squarePage.clickOnBornToShop()

        squareShoppingPage = SquareShoppingPage(self, self.driver, self.logger)
        squareShoppingPage.waitBySeconds(10)
        squareShoppingPage.validSelf()
        tempText = squareShoppingPage.clickOnSubCommodity()

        goodsDetailsPage = GoodsDetailsPage(self, self.driver, self.logger)
        goodsDetailsPage.waitBySeconds(10)
        goodsDetailsPage.validSelf()
        goodsDetailsPage.validKeywords(tempText)


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(GuangChangAiGouWuTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report', description='Result for test')
    runner.run(suite)
