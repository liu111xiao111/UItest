# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.android.ffan.square_module_page import SquareModulePage
from com.qa.automation.appium.pages.android.ffan.square_food_category_page import SquareFoodPage
from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.utility.logger import Logger
from com.qa.automation.appium.utility.device_info_util import DeviceInfoUtil
from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData


class SquareFoodCases(TestCase):
    '''
    作者 刘涛
    巡检checklist #31
    自动化测试 #31
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

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        squarePage = SquareModulePage(self, self.driver, self.logger)
        squareFoodPage = SquareFoodPage(self, self.driver, self.logger)

        dashboardPage.validSelf()

        dashboardPage.clickOnSquareModule()
        squarePage.waitBySeconds(5)
        squarePage.validSelf()

        squarePage.scrollToFood()
        squarePage.clickOnFood()
        squareFoodPage.waitBySeconds(5)
        squareFoodPage.validSelf()

        squareFoodPage.clickOnFindRestaurant()
        squareFoodPage.waitBySeconds(2)
        squareFoodPage.validFindRestaurant()
        squareFoodPage.clickBackKey()
        squareFoodPage.waitBySeconds(2)

        squareFoodPage.clickOnFindFavourable()
        squareFoodPage.waitBySeconds(2)
        squareFoodPage.validFindFavourable()
        squareFoodPage.clickBackKey()
        squareFoodPage.waitBySeconds(2)

        squareFoodPage.clickOnQueue()
        squareFoodPage.waitBySeconds(2)
        squareFoodPage.validQueue()
        squareFoodPage.clickBackKey()
        squareFoodPage.waitBySeconds(2)

        squareFoodPage.clickOnStochastic()
        squareFoodPage.waitBySeconds(2)
        squareFoodPage.validStochastic()
        squareFoodPage.clickBackKey()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(SquareFoodCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath + 'food-test_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='food-test',
                                           description='Result for test')
    runner.run(suite)