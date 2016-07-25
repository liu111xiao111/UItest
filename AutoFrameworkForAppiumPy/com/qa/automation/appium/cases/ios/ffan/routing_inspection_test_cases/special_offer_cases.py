# -*- coding:utf-8 -*-

import os
import time
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from com.qa.automation.appium.cases.ios.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.ios.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.configs.ios_driver_configs import IosDriverConfigs as IDC
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.ios.ffan.activity_details_page import ActivityDetailsPage
from com.qa.automation.appium.pages.ios.ffan.coupon_details_page import CouponDetailsPage
from com.qa.automation.appium.pages.ios.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.ios.ffan.hui_life_page import HuiLifePage
from com.qa.automation.appium.utility.logger import Logger


class SpecialOfferCases(TestCase):
    '''
    作者 宋波
    巡检checklist #38
    自动化测试 #38
    首页-慧生活，查看优惠活动，按距离近远显示活动和优惠信息（城市维度）并选择一个优惠券领取在我的票券中显示，选择一个活动查看门店
    '''

    def tearDown(self):
        self.driver.quit()
        ClearAppData().clearData()

    def setUp(self):
        ClearAppData().clearData()
        self.logger = Logger()
        self.driver = AppiumDriver(None, None, IDC.platformName, IDC.platformVersion,
                                   IDC.deviceName, IDC.driverUrl, IDC.bundleId, IDC.udid).getDriver()
        TestPrepare(self, self.driver, self.logger).prepare()

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnHuiLife()

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
