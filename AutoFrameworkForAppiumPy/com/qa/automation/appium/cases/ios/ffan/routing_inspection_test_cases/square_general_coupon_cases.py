# -*- coding: utf-8 -*-

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
from com.qa.automation.appium.pages.ios.ffan.general_coupon_page import GeneralCouponPage
from com.qa.automation.appium.pages.ios.ffan.receive_success_page import ReceiveSuccessPage
from com.qa.automation.appium.pages.ios.ffan.square_module_page import SquareModulePage
from com.qa.automation.appium.utility.logger import Logger


class SquareGeneralCouponCases(TestCase):
    '''
    作者 宋波
    巡检checklist #36
    自动化测试 #36
    广场详情页点击通用券可以进入通用券并可以成功领取通用券在我的票券中显示
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
        dashboardPage = DashboardPage(self , self.driver , self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnSquareModule()

        squareModulePage = SquareModulePage(self, self.driver, self.logger)
        squareModulePage.validSelf()
        squareModulePage.clickOnGeneralCoupon()

        generalCouponPage = GeneralCouponPage(self, self.driver, self.logger)
        generalCouponPage.validSelf()
        generalCouponPage.clickOnImmediatelyToReceive()

        receiveSuccessPage = ReceiveSuccessPage(self, self.driver, self.logger)
        receiveSuccessPage.validSelf()
        receiveSuccessPage.waitBySeconds(2)
#         tempText = receiveSuccessPage.getPrivilegeCouponCode()
#         receiveSuccessPage.clickBackKey()
#
#         generalCouponPage.validSelf()
#         generalCouponPage.clickBackKey()
#
#         squareModulePage.validSelf()
#         squareModulePage.clickBackKey()
#
#         dashboardPage.validSelf()
#         dashboardPage.clickOnMy()
#
#         myFfanPage = MyFfanPage(self, self.driver, self.logger)
#         myFfanPage.validSelf()
#         myFfanPage.clickOnMyTicket()
#
#         myFfanMyTicketPage = MyFfanMyTicketPage(self, self.driver, self.logger)
#         myFfanMyTicketPage.validSelf()
# #         myFfanMyTicketPage.validCouponCode(tempText)
#         myFfanMyTicketPage.clickBackKey()
#
#         myFfanPage.validSelf()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(SquareGeneralCouponCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'food-test_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'food-test', 'Result for test')
    runner.run(suite)
