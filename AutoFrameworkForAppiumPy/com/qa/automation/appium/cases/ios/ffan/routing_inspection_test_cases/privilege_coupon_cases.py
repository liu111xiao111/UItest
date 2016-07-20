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
from com.qa.automation.appium.pages.ios.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.ios.ffan.my_ffan_my_order_details_page import MyFfanMyOrderDetailsPage
from com.qa.automation.appium.pages.ios.ffan.my_ffan_my_ticket_page import MyFfanMyTicketPage
from com.qa.automation.appium.pages.ios.ffan.my_ffan_page import MyFfanPage
from com.qa.automation.appium.pages.ios.ffan.sales_promotion_coupon_details_page import SalesPromotionCouponDetailsPage
from com.qa.automation.appium.pages.ios.ffan.sales_promotion_coupon_success_page import SalesPromotionCouponSuccessPage
from com.qa.automation.appium.pages.ios.ffan.sales_promotion_page import SalesPromotionPage
from com.qa.automation.appium.pages.ios.ffan.square_module_page import SquareModulePage
from com.qa.automation.appium.utility.logger import Logger


class PrivilegeCouponCases(TestCase):
    '''
    巡检checklist No.: 37
    自动化测试case No.: 37
    广场详情页点击优惠券可以进入通用券并可以成功领取优惠券在我的票券中显示
    '''

    def tearDown(self):
        ClearAppData(self.driver).clearData()
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(None, None, IDC.platformName, IDC.platformVersion,
                                   IDC.deviceName, IDC.driverUrl, IDC.bundleId, IDC.udid).getDriver()
        ClearAppData(self.driver).clearData()
        TestPrepare(self, self.driver, self.logger).prepare()

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnSquareModule()

        squareModulePage = SquareModulePage(self, self.driver, self.logger)
        squareModulePage.validSelf()
        squareModulePage.clickOnCoupon()

        salesPromotionPage = SalesPromotionPage(self, self.driver, self.logger)
        salesPromotionPage.validSelf()
        salesPromotionPage.clickOnCouponTab()
        couponListItemName = salesPromotionPage.getItemName()
        salesPromotionPage.clickOnCouponDetails()

        salesPromotionCouponDetailsPage = SalesPromotionCouponDetailsPage(self, self.driver, self.logger)
        salesPromotionCouponDetailsPage.waitBySeconds(10)
        salesPromotionCouponDetailsPage.validSelf(couponListItemName)
        salesPromotionCouponDetailsPage.clickOnFreeOfChargeBtn()

        salesPromotionCouponSuccessPage = SalesPromotionCouponSuccessPage(self, self.driver, self.logger)
        salesPromotionCouponSuccessPage.validSelf()
        salesPromotionCouponSuccessPage.clickOnCheckMyTicketBtn()

        myOrderDetailsPage = MyFfanMyOrderDetailsPage(self, self.driver, self.logger)
        myOrderDetailsPage.waitBySeconds(5)
        couponNo = myOrderDetailsPage.getMyCouponNumber()
        myOrderDetailsPage.clickBackKey()

        salesPromotionCouponDetailsPage.validSelf(couponListItemName)
        salesPromotionCouponDetailsPage.clickBackKey()

        salesPromotionPage.validSelf()
        salesPromotionPage.clickBackKey()

        squareModulePage.validSelf()
        squareModulePage.clickBackKey()

        dashboardPage.validSelf()
        dashboardPage.clickOnMy()

        myFfanPage = MyFfanPage(self, self.driver, self.logger)
        myFfanPage.validSelf()
        myFfanPage.clickOnMyTicket()

        myFfanMyTicketPage = MyFfanMyTicketPage(self, self.driver, self.logger)
        myOrderNo = myFfanMyTicketPage.getTicketNo()
        myFfanMyTicketPage.validSelf(couponNo, myOrderNo)
        myFfanMyTicketPage.clickBackKey()

        myFfanPage.validSelf()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(PrivilegeCouponCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
