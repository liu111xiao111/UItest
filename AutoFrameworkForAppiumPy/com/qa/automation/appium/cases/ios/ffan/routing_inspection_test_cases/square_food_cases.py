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
from com.qa.automation.appium.pages.ios.ffan.square_food_category_page import SquareFoodPage
from com.qa.automation.appium.utility.logger import Logger


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
        squareFoodPage = SquareFoodPage(self, self.driver, self.logger)

        # 首页进入广场页
        dashboardPage.validSelf();
        dashboardPage.clickOnSquareModule()
        squarePage.validSelf();

        # 点击 "美食汇"
        squarePage.clickOnFood()
        squareFoodPage.validSelf()

        # 检查美食汇入口
        squareFoodPage.waitBySeconds(5)
        squareFoodPage.clickOnFindRestaurant()
        squareFoodPage.validFindRestaurant()
        squareFoodPage.clickBackKey()
        squareFoodPage.waitBySeconds(5)

        squareFoodPage.clickOnFindFavourable()
        squareFoodPage.validFindFavourable()
        squareFoodPage.clickBackKey()
        squareFoodPage.waitBySeconds(5)

        squareFoodPage.clickOnQueue()
        squareFoodPage.validQueue()
        squareFoodPage.clickBackKey()
        squareFoodPage.waitBySeconds(5)

        squareFoodPage.clickOnStochastic()
        squareFoodPage.validStochastic()
        squareFoodPage.clickBackKey()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(SquareFoodCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'food-test_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='food-test',
                                           description='Result for test')
    runner.run(suite)