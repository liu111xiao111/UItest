# -*- coding:utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from cases.ios.ffan.common.clearAppData import ClearAppData
from cases.ios.ffan.common.testPrepare import TestPrepare
from pages.ios.ffan.shopping_mall_page import ShoppingMallPage
from pages.ios.ffan.dashboard_page import DashboardPage
from configs.iosDriverConfig import IosDriverConfigs as IDC
from driver.appium_driver import AppiumDriver
from cases.logger import logger


class GouWuZhongXinTestCase(TestCase):
    '''
    作者 刘涛
    巡检checklist No.: 05
    自动化测试case No.: 05
    爱逛街进入购物中心确认广场距离排序顺序以及广场信息
    '''

    @classmethod
    def setUpClass(cls):
        '''
        初始化Appium driver
        '''

        cls.driver = AppiumDriver(None,
                                  None,
                                  IDC.platformName,
                                  IDC.platformVersion,
                                  IDC.deviceName,
                                  IDC.driverUrl,
                                  IDC.bundleId,
                                  IDC.udid).getDriver()
        logger.info("Appium client init completed")

    def setUp(self):
        self.logger = logger

        logger.info("Appium client init completed")
        self.reset = ClearAppData(self.driver)
        self.reset.clearData()
        logger.info("Clear data completed")
        
        TestPrepare(self, self.driver, self.logger).prepare(False)

    def test_case(self):
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

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(GouWuZhongXinTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
