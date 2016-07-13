# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage;
from com.qa.automation.appium.pages.android.ffan.my_ffan_page import MyFfanPage;
from com.qa.automation.appium.pages.android.ffan.my_ffan_my_ticket_page import MyFfanMyTicketPage;
from com.qa.automation.appium.pages.android.ffan.sales_promotion_page import SalesPromotionPage
from com.qa.automation.appium.pages.android.ffan.sales_promotion_coupon_details_page import SalesPromotionCouponDetailsPage
from com.qa.automation.appium.pages.android.ffan.sales_promotion_coupon_success_page import SalesPromotionCouponSuccessPage
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url
from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.configs.driver_configs import platformVersion
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.utility.logger import Logger
from com.qa.automation.appium.utility.device_info_util import DeviceInfoUtil


class MyfeifanMyTicketCases(TestCase):
    '''
    	巡检checklist #50
    	自动化测试 #50
    	查看我的票券里数据显示正常
    '''

    def tearDown(self):
        self.driver.quit()

        clearAppData = ClearAppData()
        clearAppData.clearData()

    def setUp(self):
        clearAppData = ClearAppData()
        clearAppData.clearData()

        self.logger = Logger()
        self.driver = AppiumDriver(app_package=appPackage_ffan, app_activity=appActivity_ffan,
                                   platform_name=platformName_andr, platform_version=DeviceInfoUtil().getBuildVersion(),
                                   device_name=deviceName_andr, driver_url=driver_url
                                   ).getDriver()

        # Login & update version
        testPrepare = TestPrepare(testcase=self, driver=self.driver, logger=self.logger)
        testPrepare.prepare()

    def test_case(self):
        dashboardPage = DashboardPage(testcase = self , driver = self.driver , logger = self.logger)
        salesPromotionPage = SalesPromotionPage(testcase = self , driver = self.driver , logger = self.logger)
        salesPromotionCouponDetailsPage = SalesPromotionCouponDetailsPage(testcase = self , driver = self.driver , logger = self.logger)
        myFfanPage = MyFfanPage(testcase = self,driver = self.driver,logger = self.logger)
        myTicketPage = MyFfanMyTicketPage(testcase = self,driver = self.driver,logger = self.logger)
        salesPromotionCouponSuccessPage = SalesPromotionCouponSuccessPage(testcase = self , driver = self.driver , logger = self.logger)
        
        # Click "优惠" and get ticket.
        dashboardPage.validSelf();
        dashboardPage.clickOnSales();
        salesPromotionPage.validSelf();
        salesPromotionPage.clickOnCouponTab();
        salesPromotionPage.clickOnCouponDetails();
        salesPromotionCouponDetailsPage.waitBySeconds(10);
        salesPromotionCouponDetailsPage.clickOnFreeOfChargeBtn();
        salesPromotionCouponSuccessPage.validSelf();
        couponName = salesPromotionCouponSuccessPage.getCouponDetails();
        salesPromotionCouponSuccessPage.clickBackKey();
        salesPromotionCouponDetailsPage.clickBackKey();
        salesPromotionPage.clickBackKey();

        # Click "我的票券"
        dashboardPage.clickOnMy();
        myFfanPage.validSelf();
        myFfanPage.clickOnMyTicket();
        myTicketPage.validSelf();
        myTicketPage.validSelfTicketName(couponName);


if __name__ == "__main__":
    log = Logger()
    caseName = 'myfeifan_my_queue_cases'
    suite = TestLoader().loadTestsFromTestCase(MyfeifanMyTicketCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + caseName + now + '.html'
    log.d("report file name ==== %s", filename)
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=caseName,
                                           description='Result for test')
    runner.run(suite)