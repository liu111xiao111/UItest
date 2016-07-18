# -*- coding:utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.cases.ios.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.configs.ios_driver_configs import IosDriverConfigs as IDC
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.ios.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.ios.ffan.sales_promotion_page import SalesPromotionPage
from com.qa.automation.appium.pages.ios.ffan.sales_promotion_coupon_details_page import SalesPromotionCouponDetailsPage
from com.qa.automation.appium.pages.ios.ffan.sales_promotion_coupon_success_page import SalesPromotionCouponSuccessPage
from com.qa.automation.appium.utility.logger import Logger


COUPONNUMBER = 2

class SalesPromotionCouponCases(TestCase):
    '''
        巡检checklist #18
        自动化测试 #18-2
        首页查看优惠活动，包含4个优惠券，2个活动（城市维度）并选择一个优惠券领取在我的票券中显示，选择一个活动查看门店
    '''

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(None,
                                   None,
                                   IDC.platformName,
                                   IDC.platformVersion,
                                   IDC.deviceName,
                                   IDC.driverUrl,
                                   IDC.bundleId,
                                   IDC.udid).getDriver()

        self.reset = ClearAppData(self.driver)
        self.reset.clearData()

    def test_case(self):
        dashboardPage = DashboardPage(testcase = self , driver = self.driver , logger = self.logger)
        salesPromotionPage = SalesPromotionPage(testcase = self , driver = self.driver , logger = self.logger)
        salesPromotionCouponDetailsPage = SalesPromotionCouponDetailsPage(testcase = self , driver = self.driver , logger = self.logger)
        salesPromotionCouponSuccessPage = SalesPromotionCouponSuccessPage(testcase = self , driver = self.driver , logger = self.logger)

        # 点击 "优惠活动"
        dashboardPage.validSelf();
        dashboardPage.clickOnSalesPromotion();
        salesPromotionPage.validSelf();
        salesPromotionPage.waitBySeconds(2);

        # 点击 "优惠券"
        salesPromotionPage.clickOnCouponTab();
        salesPromotionPage.waitBySeconds(2);

        # 判断优惠券大于2个
        salesPromotionPage.validSelfListNumber(COUPONNUMBER);

        # 点击进入优惠券详情页
        couponListItemName = salesPromotionPage.getItemName();
        salesPromotionPage.clickOnCouponDetails();
        salesPromotionCouponDetailsPage.waitBySeconds(2);
        salesPromotionCouponDetailsPage.validSelf(couponListItemName);

        # 领取优惠券
        salesPromotionCouponDetailsPage.waitBySeconds(1);
        salesPromotionCouponDetailsPage.clickOnFreeOfChargeBtn();
        salesPromotionCouponSuccessPage.validSelf();
        '''salesPromotionCouponSuccessPage.clickOnCheckMyTicketBtn();
        myOrderDetailsPage.waitBySeconds(seconds=5)
        couponNo = myOrderDetailsPage.getMyCouponNumber();
        
        myOrderNo = salesPromotionCouponSuccessPage.getCouponDetails();
        myTicketPage.validSelfTicketName(myOrderNo, couponNo);'''


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(SalesPromotionCouponCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
