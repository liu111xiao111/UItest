#!/usr/bin/env python
# -*- coding:utf-8 -*-


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
from com.qa.automation.appium.pages.android.ffan.flash_sales_square_page import FlashSalesSquarePage
from com.qa.automation.appium.pages.android.ffan.goods_details_page import GoodsDetailsPage
from com.qa.automation.appium.utility.logger import Logger


sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))))


class FlashSalesCases(TestCase):
    '''
    巡检checklist No.: 17
    自动化测试case No.: 17
    首页查看闪购，按距离显示最近的2个广场的闪购商品，查看更多，并选择一个商品下单支付退款（虚拟城市），并查看相应订单状态 （周一至周四无活动）
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
        dashboardPage = DashboardPage(self , self.driver , self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnFlashSalesMore()
        dashboardPage.waitBySeconds()

        flashSalesSquarePage = FlashSalesSquarePage(self , self.driver , self.logger)
        flashSalesSquarePage.validSelf()
        flashSalesSquarePage.clickOnGoods()

        goodsDetailsPage = GoodsDetailsPage(self , self.driver , self.logger)
        goodsDetailsPage.validSelf()
        goodsDetailsPage.clickBackKey()

        flashSalesSquarePage.validSelf()
        flashSalesSquarePage.clickBackKey()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(FlashSalesCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
