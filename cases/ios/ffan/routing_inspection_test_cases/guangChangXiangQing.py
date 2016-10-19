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


class GuangChangXiangQing(TestCase):
    '''
    作者 宋波
    巡检checklist #Anonymous
    自动化测试 #Anonymous
    首页=>广场详情页
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
        TestPrepare(self, self.driver, self.logger).prepare()

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnSquareModule()

        squareModulePage = SquareModulePage(self, self.driver, self.logger)
        squareModulePage.validSelf()
        squareModulePage.clickBackKey()

        dashboardPage.validSelf()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(GuangChangXiangQing)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
