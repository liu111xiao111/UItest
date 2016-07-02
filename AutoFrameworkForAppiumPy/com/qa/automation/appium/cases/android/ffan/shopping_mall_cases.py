#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Title: shopping_mall_cases.py
Package: com.qa.automation.appium.cases.android.ffan
Description: This is a test case for checking shopping mall.
Company: Neusoft
All rights Reserved, Designed By Zhaosheng Liu
@copyright: Copyright(C) 2016-2017
@author: Zhaosheng Liu
@date Jun 17, 2016 04:27:25 PM
Modification  History:
Date                Author                Version                Description
Jun 17, 2016        liuzhsh               V0.0.0.1               New file
Why & What is modified: TODO
'''

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
from com.qa.automation.appium.pages.android.ffan.shopping_mall_page import ShoppingMallPage
from com.qa.automation.appium.pages.android.ffan.square_module_page import SquareModulePage
from com.qa.automation.appium.utility.logger import Logger


sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))))


class ShoppingMallCases(TestCase):
    '''
    巡检checklist No.: 05
    自动化测试case No.: 05
    爱逛街进入购物中心确认广场距离排序顺序以及广场信息
    '''

    def tearDown(self):
        self.driver.quit()
        ClearAppData().clearData()

    def setUp(self):
        ClearAppData().clearData()
        self.logger = Logger()
        self.driver = AppiumDriver(appPackage_ffan, appActivity_ffan, platformName_andr, platformVersion, deviceName_andr, driver_url).getDriver()
        TestPrepare(self, self.driver, self.logger).prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnShoppingMall()

        shoppingMallPage = ShoppingMallPage(self, self.driver, self.logger)
        shoppingMallPage.validSelf()
        shoppingMallPage.clickOnTotal()
        shoppingMallPage.clickOnSpecificShoppingMall()

        squareModulePage = SquareModulePage(self, self.driver, self.logger)
        squareModulePage.validSelf()
        squareModulePage.clickBackKey()

        shoppingMallPage.validSelf()
        shoppingMallPage.clickBackKey()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(ShoppingMallCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
