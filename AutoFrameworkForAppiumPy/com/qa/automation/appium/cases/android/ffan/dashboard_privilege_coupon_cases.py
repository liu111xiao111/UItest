#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Title: dashboard_privilege_coupon_cases.py
Package: com.qa.automation.appium.cases.android.ffan
Description: This is a test case for checking privilege coupon.
Company: Neusoft
All rights Reserved, Designed By Zhaosheng Liu
@copyright: Copyright(C) 2016-2017
@author: Zhaosheng Liu
@date Jun 17, 2016 03:27:25 PM
Modification  History:
Date                Author                Version                Description
Jun 17, 2016        liuzhsh               V0.0.0.1               New file
Why & What is modified: TODO
'''

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
from com.qa.automation.appium.pages.android.ffan.activity_and_privilege_coupon_page import ActivityAndPrivilegeCouponPage
from com.qa.automation.appium.pages.android.ffan.coupon_details_page import CouponDetailsPage
from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.android.ffan.sharing_page import SharingPage
from com.qa.automation.appium.utility.logger import Logger


sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))))


class ActivitySharingCases(TestCase):
    '''
    巡检checklist No.: 10
    自动化测试case No.: 10
    首页进入优惠简单浏览优惠券内容，城市维度，且按距离排序，点击验证优惠券可以进入通用券并可以成功领取优惠券在我的票券中显示
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
        dashboardPage.clickOnPrivilege()

        activityAndPrivilegeCouponPage = ActivityAndPrivilegeCouponPage(self, self.driver, self.logger)
        activityAndPrivilegeCouponPage.validSelf()
        activityAndPrivilegeCouponPage.clickOnPrivilegeCoupon()
        activityAndPrivilegeCouponPage.clickOnSpecificPrivilegeCoupon()

        couponDetailsPage = CouponDetailsPage(self, self.driver, self.logger)
        couponDetailsPage.validSelf()
        couponDetailsPage.clickOnSharing()

        sharingPage = SharingPage(self, self.driver, self.logger)
        sharingPage.validSelf()
        sharingPage.clickBackKey()

        couponDetailsPage.validSelf()
        couponDetailsPage.clickBackKey()

        activityAndPrivilegeCouponPage.validSelf()
        activityAndPrivilegeCouponPage.clickBackKey()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(ActivitySharingCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
