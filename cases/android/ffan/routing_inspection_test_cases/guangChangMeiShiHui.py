# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.square_module_page import SquareModulePage
from pages.android.ffan.square_food_category_page import SquareFoodPage
from pages.android.ffan.search_page import SearchPage
from configs.driver_configs import platformName_andr
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil
from cases.android.ffan.common.test_prepare import TestPrepare
from cases.android.ffan.common.clear_app_data import ClearAppData


class GuangChangMeiShiHuiTestCase(TestCase):
    '''
    巡检 No.33
    用例名: 广场美食汇
    广场详情页点击美食汇正常进入餐饮模块，数据显示正常可点击进入
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

    def testGuangChangMeiShiHui(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        squarePage = SquareModulePage(self, self.driver, self.logger)
        squareFoodPage = SquareFoodPage(self, self.driver, self.logger)
        searchPage = SearchPage(self, self.driver, self.logger)

        dashboardPage.validSelf()
        dashboardPage.clickOnSearchView()
        searchPage.validSelf()
        searchPage.inputText("北京通州万达广场")
        searchPage.clickOnSearch()
        searchPage.clickOnSearchResultFirstItem()
        squarePage.validSelf()
        squarePage.waitBySeconds(5)

        squarePage.scrollToFood()
        squarePage.clickOnFood()
        squareFoodPage.validSelf()

        squareFoodPage.clickOnFindRestaurant()
        squareFoodPage.validFindRestaurant()
        squareFoodPage.clickBackKey()

        squareFoodPage.clickOnFindFavourable()
        squareFoodPage.validFindFavourable()
        squareFoodPage.clickBackKey()
        squareFoodPage.waitBySeconds(2)

        squareFoodPage.clickOnQueue()
        squareFoodPage.validQueue()
        squareFoodPage.clickBackKey()

        squareFoodPage.clickOnStochastic()
        squareFoodPage.validStochastic()
        squareFoodPage.clickBackKey()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(GuangChangMeiShiHuiTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report', description='Result for test')
    runner.run(suite)
