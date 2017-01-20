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
from pages.ios.ffan.square_module_page import SquareModulePage
from utility.logger import Logger
from pages.ios.ffan.search_page import SearchPage
from cases.logger import logger


class YouHuiQuanTestCase(TestCase):
    '''
    作者 宋波
    巡检checklist #Anonymous
    自动化测试 #Anonymous
    广场详情页点击优惠可以进入优惠券并可以成功领取优惠券在我的票券中显示
    '''

    @classmethod
    def setUpClass(cls):
        '''
        初始化Appium driver
        '''

        cls.driver = AppiumDriver(None,
                                  None,
                                  IDC.platformName,
                                  IDC.platformVersion,
                                  IDC.deviceName,
                                  IDC.driverUrl,
                                  IDC.bundleId,
                                  IDC.udid).getDriver()
        logger.info("Appium client init completed")


    def setUp(self):
        self.logger = logger
        self.reset = ClearAppData(self.driver)
        self.reset.clearData()
        TestPrepare(self, self.driver, self.logger).prepare()

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        searchPage = SearchPage(self, self.driver, self.logger)
        dashboardPage.validSelf()

        # dashboardPage.clickOnSquareModule()
        dashboardPage.clickOnSearchAll()
        searchPage.inputKeywords(u"北京通州万达广场")
        searchPage.clickOnSearch()
        searchPage.clickOnSpecificSquare()

        squareModulePage = SquareModulePage(self, self.driver, self.logger)
        squareModulePage.validSelf()
        squareModulePage.clickOnPrivilege()

        #squareModulePage.waitBySeconds(8)
        # salesPromotionPage = SalesPromotionPage(self, self.driver, self.logger)
        # salesPromotionPage.validSelf()
        # salesPromotionPage.clickOnCouponTab()
        # couponListItemName = salesPromotionPage.getItemName()
        # salesPromotionPage.clickOnCouponDetails()
        #
        # salesPromotionCouponDetailsPage = SalesPromotionCouponDetailsPage(self, self.driver, self.logger)
        # salesPromotionCouponDetailsPage.waitBySeconds(10)
        # salesPromotionCouponDetailsPage.validSelf(couponListItemName)
        # salesPromotionCouponDetailsPage.clickOnFreeOfChargeBtn()
        #
        # salesPromotionCouponSuccessPage = SalesPromotionCouponSuccessPage(self, self.driver, self.logger)
        # salesPromotionCouponSuccessPage.validSelf()
        # salesPromotionCouponSuccessPage.clickOnCheckMyTicketBtn()
        #
        # myOrderDetailsPage = MyFfanMyOrderDetailsPage(self, self.driver, self.logger)
        # myOrderDetailsPage.waitBySeconds(5)
        # couponNo = myOrderDetailsPage.getMyCouponNumber()
        # myOrderDetailsPage.clickBackKey()
        #
        # salesPromotionCouponDetailsPage.validSelf(couponListItemName)
        # salesPromotionCouponDetailsPage.clickBackKey()
        #
        # salesPromotionPage.validSelf()
        # salesPromotionPage.clickBackKey()
        #
        # squareModulePage.validSelf()
        # squareModulePage.clickBackKey()
        #
        # dashboardPage.validSelf()
        # dashboardPage.clickOnMy()
        #
        # myFfanPage = MyFfanPage(self, self.driver, self.logger)
        # myFfanPage.validSelf()
        # myFfanPage.clickOnMyTicket()
        #
        # myFfanMyTicketPage = MyFfanMyTicketPage(self, self.driver, self.logger)
        # myOrderNo = myFfanMyTicketPage.getTicketNo()
        # myFfanMyTicketPage.validSelf(couponNo[3:], myOrderNo)
        # myFfanMyTicketPage.clickBackKey()
        #
        # myFfanPage.validSelf()

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(YouHuiQuanTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
