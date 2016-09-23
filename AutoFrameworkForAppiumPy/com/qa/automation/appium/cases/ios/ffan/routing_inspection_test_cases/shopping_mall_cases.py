# -*- coding:utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.cases.ios.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.ios.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.pages.ios.ffan.shopping_mall_page import ShoppingMallPage
from com.qa.automation.appium.pages.ios.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.configs.ios_driver_configs import IosDriverConfigs as IDC
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.utility.logger import Logger


class ShoppingMallCases(TestCase):
    '''
    作者 刘涛
    巡检checklist No.: 05
    自动化测试case No.: 05
    爱逛街进入购物中心确认广场距离排序顺序以及广场信息
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
        
        TestPrepare(self, self.driver, self.logger).prepare(False)

    def testCase(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        shoppingMallPage = ShoppingMallPage(self, self.driver, self.logger)

        # 验证主界面
        dashboardPage.validSelf()

        # 进入购物中心并验证
        dashboardPage.clickOnShoppingMall()
        shoppingMallPage.validSelf()

        # 点击 “全部” tab
        shoppingMallPage.clickOnTotalTab()
        shoppingMallPage.validListView()
        #shoppingMallPage.validDistance()

        # 点击 “购物中心” tab
        shoppingMallPage.clickOnShoppingTab()
        shoppingMallPage.validListView()
        #shoppingMallPage.validDistance()

        # 点击 “百货” tab
        shoppingMallPage.clickOnGoodsTab()
        shoppingMallPage.validListView()
        #shoppingMallPage.validDistance()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(ShoppingMallCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
