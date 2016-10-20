# -*- coding:utf-8 -*-

import os
import time
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from cases.ios.ffan.common.clearAppData import ClearAppData
from cases.ios.ffan.common.testPrepare import TestPrepare
from configs.iosDriverConfig import IosDriverConfigs as IDC
from driver.appium_driver import AppiumDriver
from pages.ios.ffan.dashboard_page import DashboardPage
from pages.ios.ffan.my_ffan_my_order_details_page import MyFfanMyOrderDetailsPage
from pages.ios.ffan.my_ffan_my_ticket_page import MyFfanMyTicketPage
from pages.ios.ffan.my_ffan_page import MyFfanPage
from pages.ios.ffan.sales_promotion_coupon_details_page import SalesPromotionCouponDetailsPage
from pages.ios.ffan.sales_promotion_coupon_success_page import SalesPromotionCouponSuccessPage
from pages.ios.ffan.sales_promotion_page import SalesPromotionPage
from utility.logger import Logger


class PiaoQuanTestCase(TestCase):
    '''
    作者 刘涛
    巡检checklist #50
    自动化测试 #50
    查看我的票券里数据显示正常
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

        testPrepare = TestPrepare(testcase=self , driver=self.driver , logger=self.logger)
        testPrepare.prepare()

    def test_case(self):
        dashboardPage = DashboardPage(testcase=self , driver=self.driver , logger=self.logger)
        salesPromotionPage = SalesPromotionPage(testcase=self , driver=self.driver , logger=self.logger)
        salesPromotionCouponDetailsPage = SalesPromotionCouponDetailsPage(testcase=self , driver=self.driver , logger=self.logger)
        myFfanPage = MyFfanPage(testcase=self, driver=self.driver, logger=self.logger)
        myTicketPage = MyFfanMyTicketPage(testcase=self, driver=self.driver, logger=self.logger)
        salesPromotionCouponSuccessPage = SalesPromotionCouponSuccessPage(testcase=self , driver=self.driver , logger=self.logger)
        myOrderDetailsPage = MyFfanMyOrderDetailsPage(self, self.driver, self.logger)

        # # 点击 "优惠活动"
        # dashboardPage.validSelf();
        # dashboardPage.clickOnSalesPromotion();
        # salesPromotionPage.validSelf();
        # salesPromotionPage.waitBySeconds(2);
        #
        # # 点击 "优惠券"
        # salesPromotionPage.clickOnCouponTab();
        # salesPromotionPage.waitBySeconds(2);
        #
        # # 点击进入优惠券详情页
        # couponListItemName = salesPromotionPage.getItemName();
        # salesPromotionPage.clickOnCouponDetails();
        # salesPromotionCouponDetailsPage.waitBySeconds(10);
        # salesPromotionCouponDetailsPage.validSelf(couponListItemName);
        #
        # # 领取优惠券
        # salesPromotionCouponDetailsPage.waitBySeconds(1);
        # salesPromotionCouponDetailsPage.clickOnFreeOfChargeBtn();
        # salesPromotionCouponSuccessPage.validSelf();
        # salesPromotionCouponSuccessPage.waitBySeconds(1);
        # salesPromotionCouponSuccessPage.clickOnCheckMyTicketBtn();
        # myOrderDetailsPage.waitBySeconds(seconds=5);
        # couponNo = myOrderDetailsPage.getMyCouponNumber();
        #
        # # 查看我的票券
        # myOrderDetailsPage.clickBackKey();
        # salesPromotionCouponDetailsPage.clickBackKey();
        # salesPromotionPage.clickBackKey();
        dashboardPage.clickOnMy();
        myFfanPage.validSelf();
        myFfanPage.clickOnMyTicket();
        #myOrderNo = myTicketPage.getTicketNo();
        #myTicketPage.validSelf(couponNo[3:], myOrderNo);
        myFfanPage.validMyTicketsPage()


if __name__ == "__main__":
    log = Logger()
    caseName = 'myfeifan_my_queue_cases'
    suite = TestLoader().loadTestsFromTestCase(PiaoQuanTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + caseName + now + '.html'
    log.d("report file name ==== %s", filename)
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=caseName,
                                           description='Result for test')
    runner.run(suite)
