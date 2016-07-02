#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url
from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.configs.driver_configs import platformVersion
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.android.ffan.goods_details_page import GoodsDetailsPage
from com.qa.automation.appium.pages.android.ffan.square_module_page import SquareModulePage
from com.qa.automation.appium.pages.android.ffan.square_shopping_category_page import SquareShoppingPage


from com.qa.automation.appium.utility.logger import Logger;

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))))


class SquareShoppingCases(TestCase):
    '''
    巡检checklist No.: 32
    自动化测试case No.: 32
    广场详情页点击爱购物，进入购物模块，数据显示正常
    '''

    def tearDown(self):
        self.driver.quit()

        clearAppData = ClearAppData()
        clearAppData.clearData()

    def setUp(self):
        ClearAppData().clearData()
        self.logger = Logger()
        self.driver = AppiumDriver(appPackage_ffan, appActivity_ffan, platformName_andr, platformVersion, deviceName_andr, driver_url).getDriver()
        TestPrepare(self, self.driver, self.logger).prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(self , self.driver , self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnSquareModule()

        squareModulePage = SquareModulePage(self, self.driver, self.logger)
        squareModulePage.validSelf()
        squareModulePage.clickOnBornToShop()

        squareShoppingPage = SquareShoppingPage(self, self.driver, self.logger)
        squareShoppingPage.validSelf()
        tempText = squareShoppingPage.clickOnSubCommodity()

        goodsDetailsPage = GoodsDetailsPage(self, self.driver, self.logger)
        goodsDetailsPage.validSelf()
        goodsDetailsPage.validKeywords(tempText)
        goodsDetailsPage.clickBackKey()

        squareShoppingPage.validSelf()
        squareShoppingPage.clickBackKey()

        squareModulePage.validSelf()
        squareModulePage.clickBackKey()

        dashboardPage.validSelf()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(SquareShoppingCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'food-test_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='food-test',
                                           description='Result for test')
    runner.run(suite)
