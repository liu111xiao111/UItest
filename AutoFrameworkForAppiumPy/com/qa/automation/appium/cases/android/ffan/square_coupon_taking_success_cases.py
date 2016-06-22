# -*- coding: utf-8 -*-

import sys, os, time

sys.path.append(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))))

from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage;
from com.qa.automation.appium.pages.android.ffan.square_module_page import SquareModulePage;
from com.qa.automation.appium.pages.android.ffan.square_coupon_page import SquareCouponPage;
from com.qa.automation.appium.pages.android.ffan.square_coupon_detail_page import SquareCouponDetailPage;
from com.qa.automation.appium.pages.android.ffan.square_coupon_taking_success_page import SquareCouponTakingSuccessPage;
from com.qa.automation.appium.configs.driver_configs import *;
from com.qa.automation.appium.driver.appium_driver import AppiumDriver;
from com.qa.automation.appium.utility.logger import Logger;

from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData

import unittest
import HTMLTestRunner


class SquareCouponTakingSuccessCases(unittest.TestCase):
    '''
        巡检checklist No.: 22
        自动化测试case No.: 22
        广场详情页点击优惠券可以进入优惠券列表，并可以成功领取通用券、进入详情页，在我的票券中显示
    '''

    def tearDown(self):
        self.driver.quit()
        clearAppData = ClearAppData()
        clearAppData.clearData()

    def setUp(self):
        clearAppData = ClearAppData()
        clearAppData.clearData()

        self.logger = Logger()
        self.driver = AppiumDriver(app_package=appPackage_ffan, app_activity=appActivity_ffan,
                                   platform_name=platformName_andr, platform_version=platformVersion,
                                   device_name=deviceName_andr, driver_url=driver_url
                                   ).getDriver()
        # 登陆　升级
        testPrepare = TestPrepare(testcase=self, driver=self.driver, logger=self.logger)
        testPrepare.prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(testcase=self, driver=self.driver, logger=self.logger)
        squarePage = SquareModulePage(testcase=self, driver=self.driver, logger=self.logger)
        squareCouponPage = SquareCouponPage(testcase=self, driver=self.driver, logger=self.logger)
        squareCouponDetailPage = SquareCouponDetailPage(testcase=self, driver=self.driver, logger=self.logger)
        squareCouponTakingSuccessPage = SquareCouponTakingSuccessPage(testcase=self, driver=self.driver,
                                                                      logger=self.logger)

        dashboardPage.validSelf()
        dashboardPage.waitBySeconds(seconds=2)

        dashboardPage.clickOnSquareModule()
        squarePage.validSelf()

        squarePage.clickOnCoupon()
        squareCouponPage.validSelf()

        squareCouponPage.clickOnListItem()

        squareCouponDetailPage.validSelf()
        # squareCouponDetailPage.clickOnFreeTake()

        # squareCouponTakingSuccessPage.validSelf()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(SquareCouponTakingSuccessCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'food-test_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='food-test',
                                           description='Result for test')
    runner.run(suite)
