# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url
from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.android.ffan.my_ffan_my_ticket_page import MyFfanMyTicketPage;
from com.qa.automation.appium.pages.android.ffan.sales_promotion_page import SalesPromotionPage
from com.qa.automation.appium.pages.android.ffan.sales_promotion_coupon_details_page import SalesPromotionCouponDetailsPage
from com.qa.automation.appium.pages.android.ffan.sales_promotion_coupon_success_page import SalesPromotionCouponSuccessPage
from com.qa.automation.appium.utility.logger import Logger
from com.qa.automation.appium.utility.device_info_util import DeviceInfoUtil

COUPONNUMBER = 2

class SalesPromotionCouponCases(TestCase):
    '''
    作者 刘涛
    巡检checklist #18
    自动化测试 #18-2
    首页查看优惠活动，包含4个优惠券，2个活动（城市维度）并选择一个优惠券领取在我的票券中显示，选择一个活动查看门店
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

        TestPrepare(self, self.driver, self.logger).prepare()

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        salesPromotionPage = SalesPromotionPage(self, self.driver, self.logger)
        salesPromotionCouponDetailsPage = SalesPromotionCouponDetailsPage(self, self.driver, self.logger)
        salesPromotionCouponSuccessPage = SalesPromotionCouponSuccessPage(self, self.driver, self.logger)
        myTicketPage = MyFfanMyTicketPage(self, self.driver, self.logger)

        # Click "优惠活动"
        dashboardPage.validSelf();
        dashboardPage.clickOnSalesPromotion();
        salesPromotionPage.validSelf();

        # Click "优惠券", load "优惠券" details page
        salesPromotionPage.clickOnCouponTab();
        salesPromotionPage.waitBySeconds(2);
        couponListNum = salesPromotionPage.getCouponListNumber();
        if len(couponListNum) < COUPONNUMBER:
            print("Sales Promotion Coupon Error!")

        # Click "优惠券" details, load "优惠券" details page
        salesPromotionPage.clickOnCouponDetails();
        salesPromotionCouponDetailsPage.waitBySeconds(3);
        salesPromotionCouponDetailsPage.clickOnFreeOfChargeBtn();
        salesPromotionCouponSuccessPage.validSelf();
        couponName = salesPromotionCouponSuccessPage.getCouponDetails();
        salesPromotionCouponSuccessPage.clickOnCheckMyTicketBtn();
        myTicketPage.validSelfTicketName(couponName);


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(SalesPromotionCouponCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
