# -*- coding:utf-8 -*-

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
from com.qa.automation.appium.pages.android.ffan.my_ffan_my_ticket_page import MyFfanMyTicketPage
from com.qa.automation.appium.pages.android.ffan.my_ffan_page import MyFfanPage
from com.qa.automation.appium.pages.android.ffan.sales_promotion_coupon_details_page import SalesPromotionCouponDetailsPage
from com.qa.automation.appium.pages.android.ffan.sales_promotion_coupon_success_page import SalesPromotionCouponSuccessPage
from com.qa.automation.appium.pages.android.ffan.sales_promotion_page import SalesPromotionPage
from com.qa.automation.appium.pages.android.ffan.square_module_page import SquareModulePage
from com.qa.automation.appium.pages.android.ffan.search_page import SearchPage
from com.qa.automation.appium.utility.logger import Logger
from com.qa.automation.appium.utility.device_info_util import DeviceInfoUtil

class SquareSalesCases(TestCase):
    '''
    作者 乔佳溪
    巡检checklist No.: 38
    自动化测试case No.: 38
    广场详情页点击优惠券可以进入优惠券并可以成功领取优惠券在我的票券中显示 
    '''

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.platVersion = DeviceInfoUtil().getBuildVersion()
        self.driver = AppiumDriver(appPackage_ffan,
                                   appActivity_ffan,
                                   platformName_andr,
                                   self.platVersion, 
                                   deviceName_andr,
                                   driver_url).getDriver()

        self.reset = ClearAppData(self.driver)
        self.reset.clearData()

        TestPrepare(self, self.driver, self.logger).prepare()

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        searchPage = SearchPage(self, self.driver, self.logger)
        squareModulePage = SquareModulePage(self, self.driver, self.logger)

        dashboardPage.validSelf()
        dashboardPage.clickOnSearchView()
        searchPage.validSelf()
        searchPage.inputText("北京通州万达广场")
        searchPage.clickOnSearch()
        searchPage.clickOnSearchResultFirstItem()
        squareModulePage.validSelf()
        squareModulePage.clickOnSales()

        salesPromotionPage = SalesPromotionPage(self, self.driver, self.logger)
        salesPromotionPage.validSelf()
        salesPromotionPage.clickOnCouponTab()
        couponListItemName = salesPromotionPage.getItemNameByXpath()
        salesPromotionPage.clickOnSquareCouponDetails()

        salesPromotionCouponDetailsPage = SalesPromotionCouponDetailsPage(self, self.driver, self.logger)
        salesPromotionCouponDetailsPage.validSelf(couponListItemName)
        if int(self.platVersion.split(".")[0]) >= 5:
                salesPromotionCouponDetailsPage.clickOnFreeOfChargeBtn()
        else:
                salesPromotionCouponDetailsPage.clickOnFreeOfChargeLinkBtn()

        salesPromotionCouponSuccessPage = SalesPromotionCouponSuccessPage(self, self.driver, self.logger)
        salesPromotionCouponSuccessPage.validSelf()
        TempText = salesPromotionCouponSuccessPage.getCouponDetails()
        salesPromotionCouponSuccessPage.clickBackKey()

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
    suite = TestLoader().loadTestsFromTestCase(SquareSalesCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)