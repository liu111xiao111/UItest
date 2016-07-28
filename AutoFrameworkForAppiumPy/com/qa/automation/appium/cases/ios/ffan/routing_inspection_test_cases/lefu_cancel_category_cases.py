# -*- coding:utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.cases.ios.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.cases.ios.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.configs.ios_driver_configs import IosDriverConfigs as IDC
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.ios.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.ios.ffan.le_pay_details_page import LePayDetailsPage
from com.qa.automation.appium.pages.ios.ffan.le_pay_way_page import LePayWayPage
from com.qa.automation.appium.pages.ios.ffan.le_pay_page import LePayPage
from com.qa.automation.appium.pages.ios.ffan.le_pay_cancel_order_page import LePayCancelOrderPage
from com.qa.automation.appium.pages.ios.ffan.my_ffan_page import MyFfanPage
from com.qa.automation.appium.pages.ios.ffan.my_ffan_my_order_page import MyFfanMyOrderPage
from com.qa.automation.appium.pages.ios.ffan.my_ffan_my_order_details_page import MyFfanMyOrderDetailsPage
from com.qa.automation.appium.utility.logger import Logger


class LefuCancelCatergoryCases(TestCase):
    '''
    作者 刘涛
    巡检checklist #15
    自动化测试 #15-2
    首页进入乐付买单（城市维度），并下单，取消订单，支付（虚拟城市），并查看相应订单状态
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

        self.reset = ClearAppData(self.driver)
        self.reset.clearData()

        testPrepare = TestPrepare(testcase = self , driver = self.driver , logger = self.logger)
        testPrepare.prepare()

    def test_case(self):
        dashboardPage = DashboardPage(testcase=self, driver=self.driver, logger=self.logger)
        lePayPage = LePayPage(testcase=self,driver=self.driver,logger=self.logger)
        lePayDetailPage = LePayDetailsPage(self, self.driver, self.logger)
        lePayWayPage = LePayWayPage(self, self.driver, self.logger)
        lePayCancelOrderPage = LePayCancelOrderPage(self, self.driver, self.logger)
        myFfanPage = MyFfanPage(self, self.driver, self.logger)
        myOrderPage = MyFfanMyOrderPage(self, self.driver, self.logger)
        myOrderDetailsPage = MyFfanMyOrderDetailsPage(self, self.driver, self.logger)

        # 首页点击乐付
        dashboardPage.wait_by_seconds(seconds=1)
        dashboardPage.validSelf()
        dashboardPage.clickOnLePay()
        lePayPage.validSelf()

        # 点击第一条乐付买单
        lePayPage.clickOnDetailsLePay()
        lePayDetailPage.validSelf()

        # 下单
        lePayDetailPage.waitBySeconds(seconds=2)
        lePayDetailPage.inputMoney()
        lePayDetailPage.waitBySeconds(seconds=5)
        lePayDetailPage.clickOnPay()
        lePayWayPage.validSelf()
        lePayWayPage.waitBySeconds(2)

        # 获取订单号
        lePayOrderNumber = lePayWayPage.getOrderNumber()

        # 取消订单
        lePayWayPage.clickOnCancelIcon()
        lePayCancelOrderPage.waitBySeconds(seconds=1)
        lePayCancelOrderPage.clickOnConfirmBtn()
        lePayDetailPage.clickBackKey()
        lePayPage.clickBackKey()

        # 查看我的订单状态
        dashboardPage.clickOnMy()
        myFfanPage.validSelf()
        myFfanPage.clickOnMyOrder()
        myOrderPage.validSelf()

        # 查看我的订单 -- 全部订单状态
        myOrderPage.waitBySeconds(seconds=3)
        myOrderPage.clickOnOrderDetails()
        myOrderDetailsPage.waitBySeconds(seconds=5)
        myAllOrderNumber = myOrderDetailsPage.getMyOrderNumber();
        myOrderDetailsPage.validSelfAllOrders(lePayOrderNumber, myAllOrderNumber)

        # 查看我的订单 -- 电影娱乐订单状态
        myOrderDetailsPage.clickBackKey()
        myOrderPage.clickOnOrderList()
        myOrderPage.clickOnFilm()
        myOrderPage.clickOnOrderDetails()
        myOrderDetailsPage.waitBySeconds(seconds=5)
        myFilmOrderNumber = myOrderDetailsPage.getMyFilmOrderNumber();
        myOrderDetailsPage.validSelfFilmOrders(lePayOrderNumber, myFilmOrderNumber)

        # 查看我的订单 -- 乐付买单订单状态
        myOrderDetailsPage.clickBackKey()
        myOrderPage.clickOnOrderList()
        myOrderPage.clickOnLePay()
        myOrderPage.clickOnOrderDetails()
        myOrderDetailsPage.waitBySeconds(seconds=5)
        myLePayOrderNumber = myOrderDetailsPage.getMyLePayOrderNumber();
        myOrderDetailsPage.validSelfLePayOrders(lePayOrderNumber, myLePayOrderNumber)

        # 查看我的订单 -- 停车缴费订单状态
        '''myOrderDetailsPage.clickBackKey()
        myOrderPage.clickOnAllOrders()
        myOrderPage.clickOnParkingPayment()
        myOrderPage.clickOnOrderDetails()
        myOrderDetailsPage.waitBySeconds(seconds=2)
        myParkingPaymentOrderNumber = myOrderDetailsPage.getMyParkingPaymentOrderNumber();
        myOrderDetailsPage.validSelfParkingPaymentOrders(lePayOrderNumber, myParkingPaymentOrderNumber)'''


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(LefuCancelCatergoryCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)