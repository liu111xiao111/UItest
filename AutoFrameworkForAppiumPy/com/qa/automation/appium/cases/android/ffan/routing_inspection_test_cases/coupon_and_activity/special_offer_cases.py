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
from com.qa.automation.appium.pages.android.ffan.activity_details_page import ActivityDetailsPage
from com.qa.automation.appium.pages.android.ffan.coupon_details_page import CouponDetailsPage
from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.android.ffan.hui_life_page import HuiLifePage
from com.qa.automation.appium.utility.logger import Logger

sys.path.append(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))))


class SpecialOfferCases(TestCase):
    '''
    巡检checklist No.: 38
    自动化测试case No.: 38
    首页-慧生活，查看优惠活动，按距离近远显示活动和优惠信息（城市维度）并选择一个优惠券领取在我的票券中显示，选择一个活动查看门店
    '''

    def tearDown(self):
        self.driver.quit()
        ClearAppData().clearData()

    def setUp(self):
        ClearAppData().clearData()
        self.logger = Logger()
        self.driver = AppiumDriver(appPackage_ffan, appActivity_ffan, platformName_andr, platformVersion,
                                   deviceName_andr, driver_url).getDriver()
        TestPrepare(self, self.driver, self.logger).prepare()

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnSmartLife()

        huiLifePage = HuiLifePage(self, self.driver, self.logger)
        huiLifePage.validSelf()
        huiLifePage.clickOnActivity()
        huiLifePage.clickOnSpecificActivity()

        activityDetailsPage = ActivityDetailsPage(self, self.driver, self.logger)
        activityDetailsPage.validSelf()
        activityDetailsPage.clickBackKey()

        huiLifePage.validSelf()
        huiLifePage.clickOnPrivilege()
        huiLifePage.clickOnSpecificPrivilege()

        couponDetailsPage = CouponDetailsPage(self, self.driver, self.logger)
        couponDetailsPage.validSelf()
        activityDetailsPage.clickBackKey()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(SpecialOfferCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
