# -*- coding: utf-8 -*-

import sys, os
import unittest

import HTMLTestRunner

from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare


sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))))

from com.qa.automation.appium.pages.android.ffan.dashboard_page import *;
from com.qa.automation.appium.pages.android.ffan.square_module_page import *;
from com.qa.automation.appium.pages.android.ffan.square_sign_on_page import *;
from com.qa.automation.appium.pages.android.ffan.square_find_store_category_page import *;
from com.qa.automation.appium.pages.android.ffan.search_page import *;
from com.qa.automation.appium.pages.android.ffan.search_result_store_page import SearchResultStorePage;
from com.qa.automation.appium.pages.android.ffan.my_ffan_page import *;
from com.qa.automation.appium.configs.driver_configs import *;
from com.qa.automation.appium.driver.appium_driver import *;
from com.qa.automation.appium.utility.logger import Logger;


class SquareSearchCases(unittest.TestCase):
    '''
        usage : No.19 首页进入广场详情页， 广场详情页点击搜索进入搜索，搜索服务和门店，有正常结果显示（广场维度）
    '''

    def tearDown(self):
        self.driver.quit()

        clearAppData = ClearAppData()
        clearAppData.clearData()

    def setUp(self):
        clearAppData = ClearAppData()
        clearAppData.clearData()

        self.logger = Logger()
        self.driver = AppiumDriver(app_package=appPackage_ffan, app_activity=appActivity_ffan,
                                   platform_name=platformName_andr, platform_version=platformVersion,
                                   device_name=deviceName_andr, driver_url=driver_url
                                   ).getDriver()

        # 登陆　升级
        testPrepare = TestPrepare(testcase=self, driver=self.driver, logger=self.logger)
        testPrepare.prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(testcase=self, driver=self.driver, logger=self.logger)
        squarePage = SquareModulePage(testcase=self, driver=self.driver, logger=self.logger)
        squareFindStorePage = SquareFindStorePage(testcase=self, driver=self.driver, logger=self.logger)
        searchPage = SearchPage(testcase=self, driver=self.driver, logger=self.logger)
        searchResultStorePage = SearchResultStorePage(testcase=self, driver=self.driver, logger=self.logger)

        dashboardPage.validSelf()
        squarePage.waitBySeconds(seconds=2)

        dashboardPage.clickOnSquareModule()
        squarePage.validSelf()

        squarePage.clickOnSearch()

        searchPage.validSelf()
        searchPage.inputStoreName()
        searchPage.clickOnSearch()
        tempText = searchPage.clickOnSearchResultFirstItem()

        searchResultStorePage.validSelf()
        searchResultStorePage.validKeywords(tempText)
        searchResultStorePage.clickBackKey()

        searchPage.clickBackKey()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(SquareSearchCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'food-test_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='food-test',
                                           description='Result for test')
    runner.run(suite)