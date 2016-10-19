# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.square_module_page import SquareModulePage
from pages.android.ffan.square_find_store_category_page import SquareFindStorePage
from pages.android.ffan.search_page import SearchPage
from pages.android.ffan.search_result_store_page import SearchResultStorePage
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from configs.driver_configs import platformName_andr
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from cases.android.ffan.common.test_prepare import TestPrepare
from cases.android.ffan.common.clear_app_data import ClearAppData
from utility.device_info_util import DeviceInfoUtil


class GuangChangZhaoDianTestCase(TestCase):
    '''
    巡检checklist No.: 21
    自动化测试case No.: 21
    广场详情页点击找店，成功进入找店页面，并成功完成一次搜索，数据显示正常，点击门店可进入门店详情页，数据显示正常
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

    def testGuangChangZhaoDian(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        squarePage = SquareModulePage(self, self.driver, self.logger)
        squareFindStorePage = SquareFindStorePage(self, self.driver, self.logger)
        searchPage = SearchPage(self, self.driver, self.logger)
        searchResultStorePage = SearchResultStorePage(self, self.driver, self.logger)

        # 绑定北京通州万达广场
        dashboardPage.validSelf()
        dashboardPage.clickOnSearchView()
        searchPage.validSelf()
        searchPage.inputText("北京通州万达广场")
        searchPage.clickOnSearch()
        searchPage.clickOnSearchResultFirstItem()
        squarePage.waitBySeconds(10)
        squarePage.validSelf()

        # 点击找店
        squarePage.clicOnFindStore()
        squareFindStorePage.validSelf()

        # 检索门店
        '''squareFindStorePage.clickOnSearch()
        searchPage.validSelf()
        searchPage.inputText("adidas")
        searchPage.clickOnSearch()'''
        squareFindStorePage.clickOnFirstItem()
        searchResultStorePage.validSelf()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(GuangChangZhaoDianTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'food-test_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='food-test',
                                           description='Result for test')
    runner.run(suite)