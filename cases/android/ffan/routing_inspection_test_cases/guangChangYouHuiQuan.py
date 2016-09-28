# -*- coding:utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from cases.android.ffan.common.clear_app_data import ClearAppData
from cases.android.ffan.common.test_prepare import TestPrepare
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from configs.driver_configs import platformName_andr
from driver.appium_driver import AppiumDriver
from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.my_ffan_my_ticket_page import MyFfanMyTicketPage
from pages.android.ffan.my_ffan_page import MyFfanPage
from pages.android.ffan.sales_promotion_coupon_details_page import SalesPromotionCouponDetailsPage
from pages.android.ffan.sales_promotion_coupon_success_page import SalesPromotionCouponSuccessPage
from pages.android.ffan.sales_promotion_page import SalesPromotionPage
from pages.android.ffan.square_module_page import SquareModulePage
from pages.android.ffan.search_page import SearchPage
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil


class GuangChangYouHuiQuanTestCase(TestCase):
    '''
    巡检 No.37
    用例名: 广场优惠券
    广场详情页点击优惠券可以进入通用券并可以成功领取优惠券在我的票券中显示
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

    def testYouHuiQuan(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        searchPage = SearchPage(self, self.driver, self.logger)
        squareModulePage = SquareModulePage(self, self.driver, self.logger)

        dashboardPage.validSelf()
        dashboardPage.clickOnSearchView()
        searchPage.validSelf()
        searchPage.inputText("北京通州万达广场")
        searchPage.clickOnSearch()
        searchPage.waitBySeconds(10)
        searchPage.clickOnSearchResultFirstItem()
        squareModulePage.waitBySeconds(10)
        squareModulePage.validSelf()
        squareModulePage.waitBySeconds(10)
        squareModulePage.clickOnCoupon()

        salesPromotionPage = SalesPromotionPage(self, self.driver, self.logger)
        salesPromotionPage.waitBySeconds(5)
        salesPromotionPage.validSelf()
        salesPromotionPage.clickOnCouponTab()
        salesPromotionPage.waitBySeconds(5)
        couponListItemName = salesPromotionPage.getItemNameByXpath()
        salesPromotionPage.clickOnSquareCouponDetails()

        salesPromotionCouponDetailsPage = SalesPromotionCouponDetailsPage(self, self.driver, self.logger)
        salesPromotionCouponDetailsPage.waitBySeconds(20)
        salesPromotionCouponDetailsPage.validSelf(couponListItemName)
        salesPromotionCouponDetailsPage.waitBySeconds(10)
        salesPromotionCouponDetailsPage.clickOnFreeOfChargeBtn()

        salesPromotionCouponSuccessPage = SalesPromotionCouponSuccessPage(self, self.driver, self.logger)
        salesPromotionCouponSuccessPage.waitBySeconds(5)
        salesPromotionCouponSuccessPage.validSelf()
        TempText = salesPromotionCouponSuccessPage.getCouponDetails()
        salesPromotionCouponSuccessPage.clickBackKey()

        salesPromotionCouponDetailsPage.waitBySeconds(20)
        salesPromotionCouponDetailsPage.validSelf(couponListItemName)
        salesPromotionCouponDetailsPage.clickBackKey()

        salesPromotionPage.validSelf()
        salesPromotionPage.clickBackKey()

        squareModulePage.validSelf()
        squareModulePage.clickBackKey()

        searchPage.clickBackKey()

        dashboardPage.validSelf()
        dashboardPage.clickOnMy()

        myFfanPage = MyFfanPage(self, self.driver, self.logger)
        myFfanPage.validSelf()
        myFfanPage.clickOnMyTicket()

        myFfanMyTicketPage = MyFfanMyTicketPage(self, self.driver, self.logger)
        myFfanMyTicketPage.waitBySeconds(5)
        myFfanMyTicketPage.validSelf()
        myFfanMyTicketPage.validSelfTicketName(TempText)
        myFfanMyTicketPage.clickBackKey()

        myFfanPage.validSelf()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(GuangChangYouHuiQuanTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report', description='Result for test')
    runner.run(suite)
