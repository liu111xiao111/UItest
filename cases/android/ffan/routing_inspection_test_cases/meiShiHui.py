# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.food_category_page import FoodCategoryPage
#from pages.android.ffan.sales_promotion_page import SalesPromotionPage
#from pages.android.ffan.square_lefu_pay_page import SquareLefuPayPage
from configs.driver_configs import platformName_andr
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil
from cases.android.ffan.common.test_prepare import TestPrepare
from cases.logger import logger


class MeiShiHuiTestCase(TestCase):
    '''
    巡检 NO.7
    用例名: 美食汇
    首页进入美食正常进入找餐厅找优惠，数据显示正常可点击进入
    备注：由于版本变化，页面元素缺失，case无法通过
    '''
    @classmethod
    def setUpClass(cls):
        '''
        初始化Appium driver
        '''
        cls.driver = AppiumDriver(appPackage_ffan,
                                   appActivity_ffan,
                                   platformName_andr,
                                   DeviceInfoUtil().getBuildVersion(),
                                   deviceName_andr,
                                   driver_url).getDriver()
        logger.info("Appium client init completed")

    def tearDown(self):
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        TestPrepare(self, self.driver, self.logger).prepare(False)

    def testMeiShiHui(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        foodPage = FoodCategoryPage(self, self.driver, self.logger)
        #salesPromotionPage = SalesPromotionPage(self, self.driver, self.logger)
        #lefuPage = SquareLefuPayPage(self, self.driver, self.logger)

        dashboardPage.validSelf()
        dashboardPage.screenShot("aiGuangJie")

        dashboardPage.clickOnFood()
        foodPage.validFoodHomePage()
        foodPage.screenShot("meiShiHui")

        # 检查抢券入口
        foodPage.clickOnGrabCoupons()
        foodPage.validGrabCoupons()
        foodPage.screenShot("youHuiQuan")
        foodPage.clickBackKey()

        # 检查美食分类及门店列表
        foodPage.validModules()

        '''# 检查优惠打折
        foodPage.clickOnCoupon()
        salesPromotionPage.validSelf()
        salesPromotionPage.clickBackKey()

        # 检查抢券
        oodPage.clickOnGrabCoupons()
        salesPromotionPage.validSelfCoupon()
        salesPromotionPage.clickBackKey()

        # 检查乐付
        foodPage.clickOnLePay()
        lefuPage.validSelf()'''

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(MeiShiHuiTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report', description='Result for test')
    runner.run(suite)