# -*- coding:utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from cases.ios.ffan.common.testPrepare import TestPrepare
from cases.ios.ffan.common.clearAppData import ClearAppData
from configs.iosDriverConfig import IosDriverConfigs as IDC
from driver.appium_driver import AppiumDriver
from pages.ios.ffan.dashboard_page import DashboardPage
from pages.ios.ffan.food_category_page import FoodCategoryPage
from cases.logger import logger


class MeiShiHuiTestCase(TestCase):
    '''
    作者 刘涛
    巡检checklist #7
    自动化测试 #7
    首页进入美食正常进入找餐厅找优惠，数据显示正常可点击进入
    备注：由于版本变化，页面元素缺失，case无法通过
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
        self.reset = ClearAppData(self.driver)
        self.reset.clearData()

        testPrepare = TestPrepare(testcase = self , driver = self.driver , logger = self.logger)
        testPrepare.prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        foodPage = FoodCategoryPage(self, self.driver, self.logger)

        # 首页点击美食汇
        dashboardPage.validSelf();
        dashboardPage.clickOnFood();
        foodPage.validSelf();

        '''# 检查所有子界面入口
        foodPage.validModules();

        # 检查优惠打折
        foodPage.clickOnCoupon();
        foodPage.validCoupon();
        dashboardPage.clickBackKey();

        # 检查抢券
        foodPage.clickOnGrabCoupons();
        foodPage.validGrabCoupons();
        dashboardPage.clickBackKey();

        # 检查乐付
        foodPage.clickOnLePay();
        foodPage.validLePay();'''

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(MeiShiHuiTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='food-test',
                                           description='Result for test')
    runner.run(suite)