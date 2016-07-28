# -*- coding:utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.cases.ios.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.configs.ios_driver_configs import IosDriverConfigs as IDC
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.ios.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.ios.ffan.shopping_category_page import ShoppingCategoryPage
from com.qa.automation.appium.pages.ios.ffan.shopping_details_category_page import ShoppingDetailsCategoryPage
from com.qa.automation.appium.utility.logger import Logger


class ShoppingCatergoryCases(TestCase):
    '''
    作者 刘涛
    巡检checklist #12
    自动化测试 #12
    首页进入购物模块，数据显示正常，点击进入详情页可以激活商品的提醒
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
        shoppingPage = ShoppingCategoryPage(self, self.driver, self.logger)
        shoppingDetailsPage = ShoppingDetailsCategoryPage(self, self.driver, self.logger)

        # 首页点击购物
        dashboardPage.validSelf();
        dashboardPage.clickOnShopping()
        shoppingPage.validSelf();

        # 点击商品，进入商品详情页
        shoppingPage.clickOnGoodsDetails();
        shoppingDetailsPage.validSelf();


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(ShoppingCatergoryCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)