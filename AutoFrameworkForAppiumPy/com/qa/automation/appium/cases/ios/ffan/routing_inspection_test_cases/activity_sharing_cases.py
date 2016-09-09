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
from com.qa.automation.appium.pages.ios.ffan.activity_and_privilege_coupon_page import ActivityAndPrivilegeCouponPage
from com.qa.automation.appium.pages.ios.ffan.activity_details_page import ActivityDetailsPage
from com.qa.automation.appium.pages.ios.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.ios.ffan.sharing_page import SharingPage
from com.qa.automation.appium.utility.logger import Logger


class ActivitySharingCases(TestCase):
    '''
    作者 宋波
    巡检checklist #11
    自动化测试 #11
    首页进入优惠简单浏览活动内容，城市维度，且按距离排序，点击验证活动可以进入活动详情，并查看适用门店，最后进行分享
    '''

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(None, None, IDC.platformName, IDC.platformVersion,
                                   IDC.deviceName, IDC.driverUrl, IDC.bundleId, IDC.udid).getDriver()
        self.reset = ClearAppData(self.driver)
        self.reset.clearData()
        TestPrepare(self, self.driver, self.logger).prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnPrivilege()

        activityAndPrivilegeCouponPage = ActivityAndPrivilegeCouponPage(self, self.driver, self.logger)
        activityAndPrivilegeCouponPage.validSelf()
        activityAndPrivilegeCouponPage.clickOnActivity()
        activityAndPrivilegeCouponPage.clickOnSpecificActivity()

        activityDetailsPage = ActivityDetailsPage(self, self.driver, self.logger)
        activityDetailsPage.validSelf()
        activityDetailsPage.clickOnSharing()

        sharingPage = SharingPage(self, self.driver, self.logger)
        sharingPage.validSelf()
        for tempText in (u"微信", u"朋友圈", u"QQ好友", u"新浪微博"):
            sharingPage.validKeywords(tempText)
        sharingPage.clickOnCancel()

        activityDetailsPage.validSelf()
        activityDetailsPage.clickBackKey()

        activityAndPrivilegeCouponPage.validSelf()
        activityAndPrivilegeCouponPage.clickBackKey()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(ActivitySharingCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report', description='Result for test')
    runner.run(suite)
