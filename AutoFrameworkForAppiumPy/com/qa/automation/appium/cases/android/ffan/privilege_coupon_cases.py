#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))))))


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
from com.qa.automation.appium.pages.android.ffan.coupon_details_page import *
from com.qa.automation.appium.pages.android.ffan.square_coupon_page import SquareCouponPage
from com.qa.automation.appium.pages.android.ffan.square_module_page import SquareModulePage
from com.qa.automation.appium.utility.logger import Logger
from com.qa.automation.appium.utility.device_info_util import *



class PrivilegeCouponCases(TestCase):
    '''
    巡检checklist No.: 37
    自动化测试case No.: 37
    广场详情页点击优惠券可以进入通用券并可以成功领取优惠券在我的票券中显示
    '''

    def tearDown(self):
        self.driver.quit()
        #ClearAppData().clearData()

    def setUp(self):
        #ClearAppData().clearData()
        self.logger = Logger()
        self.driver = AppiumDriver(appPackage_ffan, appActivity_ffan, platformName_andr, DeviceInfoUtil().getBuildVersion() ,
                                   deviceName_andr, driver_url).getDriver()
        #TestPrepare(self, self.driver, self.logger).prepare()

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnSquareModule()

        squareModulePage = SquareModulePage(self, self.driver, self.logger)
        squareModulePage.validSelf()
        squareModulePage.clickOnCoupon()

        squareCouponPage = SquareCouponPage(self, self.driver, self.logger)
        squareCouponPage.validSelf()
        squareCouponPage.clickOnListItem()

        couponDetailPage = CouponDetailsPage(self, self.driver, self.logger)
        couponDetailPage.validSelf()

        couponDetailPage.clickOnReceiveFree()
        couponDetailPage.waitBySeconds(seconds=20)

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(PrivilegeCouponCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
