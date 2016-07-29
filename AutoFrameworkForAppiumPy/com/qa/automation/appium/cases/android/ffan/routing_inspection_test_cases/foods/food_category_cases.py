# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.android.ffan.food_category_page import FoodCategoryPage
from com.qa.automation.appium.pages.android.ffan.sales_promotion_page import SalesPromotionPage
from com.qa.automation.appium.pages.android.ffan.square_lefu_pay_page import SquareLefuPayPage
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


class FoodCases(TestCase):
    '''
    作者 刘涛
    巡检checklist #7
    自动化测试 #7
    首页进入美食正常进入找餐厅找优惠，数据显示正常可点击进入
    备注：由于版本变化，页面元素缺失，case无法通过
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
        foodPage = FoodCategoryPage(self, self.driver, self.logger)
        salesPromotionPage = SalesPromotionPage(self, self.driver, self.logger)
        lefuPage = SquareLefuPayPage(self, self.driver, self.logger)

        dashboardPage.validSelf()

        dashboardPage.clickOnFood()
        foodPage.validFoodHomePage()

        # 检查所有子界面入口
        foodPage.validModules()

        # 检查优惠打折
        foodPage.clickOnCoupon()
        salesPromotionPage.validSelf()
        salesPromotionPage.clickBackKey()

        # 检查抢券
        foodPage.clickOnGrabCoupons()
        salesPromotionPage.validSelfCoupon()
        salesPromotionPage.clickBackKey()

        # 检查乐付
        foodPage.clickOnLePay()
        lefuPage.validSelf()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(FoodCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'food-test_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='food-test',
                                           description='Result for test')
    runner.run(suite)