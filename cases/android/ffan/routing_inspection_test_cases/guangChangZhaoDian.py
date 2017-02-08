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
from utility.device_info_util import DeviceInfoUtil
from cases.logger import logger


class GuangChangZhaoDianTestCase(TestCase):
    '''
    回归用例： No.11
    用例名: 广场找店
    广场详情页点击找店，成功进入找店页面，数据显示正常，点击门店可进入门店详情页，数据显示正常 
    '''
    @classmethod
    def setUpClass(cls):
        '''
        初始化Appium driver
        '''
        cls.driver = AppiumDriver(appPackage_ffan,
                                   appActivity_ffan,
                                   platformName_andr,
                                   DeviceInfoUtil().getBuildVersion(),
                                   deviceName_andr,
                                   driver_url).getDriver()
        logger.info("Appium client init completed")

    def tearDown(self):
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        TestPrepare(self, self.driver, self.logger).prepare(False)

    def testGuangChangZhaoDian(self):
        # 验证首页
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.screenShot("aiGuangJie")

        # 首页(爱逛街页面)点击搜索,通过搜索进入“北京通州万达广场”
        dashboardPage.clickOnSearchView()
        searchPage = SearchPage(self, self.driver, self.logger)
        searchPage.validSelf()
        searchPage.screenShot("souSuo")
        searchPage.inputText("北京通州万达广场")
        searchPage.screenShot("souSuo")
        searchPage.clickOnSearch()
        searchPage.screenShot("souSuoJieGuo")
        searchPage.clickOnSearchResultFirstItem()
        squarePage = SquareModulePage(self, self.driver, self.logger)
        squarePage.waitBySeconds(10)
        squarePage.validSelf()
        squarePage.screenShot("guangChang")

        # 点击找店
        squarePage.clickOnFindStore()
        squareFindStorePage = SquareFindStorePage(self, self.driver, self.logger)
        squareFindStorePage.validSelf()
        squareFindStorePage.screenShot("zhaoDian")

        # 点击门店进入门店详情页
        squareFindStorePage.clickOnFirstItem()
        searchResultStorePage = SearchResultStorePage(self, self.driver, self.logger)
        searchResultStorePage.validSelf()
        searchResultStorePage.screenShot("zhaoDianJieGuo")


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(GuangChangZhaoDianTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'food-test_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='food-test',
                                           description='Result for test')
    runner.run(suite)