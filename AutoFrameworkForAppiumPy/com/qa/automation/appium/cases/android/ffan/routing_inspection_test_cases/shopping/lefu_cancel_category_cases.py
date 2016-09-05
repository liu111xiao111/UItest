# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.android.ffan.square_lefu_pay_page import SquareLefuPayPage
from com.qa.automation.appium.pages.android.ffan.lefu_pay_detail_page import LefuPayDetailPage
from com.qa.automation.appium.pages.android.ffan.lefu_pay_way_page import LefuPayWayPage
from com.qa.automation.appium.pages.android.ffan.lefu_cancel_order_page import LefuCancelOrderPage
from com.qa.automation.appium.pages.android.ffan.my_ffan_page import MyFfanPage
from com.qa.automation.appium.pages.android.ffan.my_ffan_my_order_page import MyFfanMyOrderPage
from com.qa.automation.appium.pages.android.ffan.my_ffan_my_order_details_page import MyFfanMyOrderDetailsPage
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url
from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.utility.logger import Logger
from com.qa.automation.appium.utility.device_info_util import DeviceInfoUtil


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
        self.driver = AppiumDriver(appPackage_ffan,
                                   appActivity_ffan,
                                   platformName_andr,
                                   DeviceInfoUtil().getBuildVersion(),
                                   deviceName_andr,
                                   driver_url).getDriver()

        self.reset = ClearAppData(self.driver)
        self.reset.clearData()

        TestPrepare(self, self.driver, self.logger).prepare()

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        lefuPage = SquareLefuPayPage(self, self.driver, self.logger)
        lefuPayDetailPage = LefuPayDetailPage(self, self.driver, self.logger)
        lefuPayWayPage = LefuPayWayPage(self, self.driver, self.logger)
        lefuCancelOrderPage = LefuCancelOrderPage(self, self.driver, self.logger)
        myFfanPage = MyFfanPage(self, self.driver, self.logger)
        myOrderPage = MyFfanMyOrderPage(self, self.driver, self.logger)
        myOrderDetailsPage = MyFfanMyOrderDetailsPage(self, self.driver, self.logger)

        # 首页点击乐付
        dashboardPage.validSelf()
        dashboardPage.clickOnLefuCategory()
        lefuPage.validSelf()

        # 点击第一条乐付买单.
        lefuPage.clickOnLefuPay()
        lefuPayDetailPage.validSelf()

        # 下单
        lefuPayDetailPage.inputMoney()
        lefuPayDetailPage.waitBySeconds(seconds=3)
        lefuPayDetailPage.clickOnPay()
        lefuPayWayPage.validSelf()
        lefuPayWayPage.waitBySeconds(2)
        lePayOrderNumber = lefuPayWayPage.getOrderNumber()

        # 取消订单
        lefuPayWayPage.clickBackKey()
        lefuCancelOrderPage.clickOnConfirmBtn()
        lefuPayDetailPage.clickBackKey()
        lefuPage.clickBackKey()

        # 查看我的订单状态
        dashboardPage.clickOnMy()
        myFfanPage.validSelf()
        myFfanPage.clickOnMyOrder()
        myOrderPage.validSelf()
        myOrderPage.waitBySeconds(seconds=3)

        # 查看我的订单 -- 全部订单状态
        myOrderPage.clickOnOrderDetails()
        myOrderDetailsPage.waitBySeconds(seconds=5)
        myOrderDetailsPage.validSelfAllOrders(lePayOrderNumber)

        # 查看我的订单 -- 乐付买单订单状态
        myOrderDetailsPage.clickBackKey()
        myOrderPage.clickOnOrderList()
        myOrderPage.clickOnLePay()
        myOrderPage.clickOnOrderDetails()
        myOrderDetailsPage.waitBySeconds(seconds=5)
        myOrderDetailsPage.validSelfLePayOrders(lePayOrderNumber)

        # 查看我的订单 -- 电影娱乐订单状态
        myOrderDetailsPage.clickBackKey()
        myOrderPage.clickOnOrderList()
        myOrderPage.clickOnFilm()
        myOrderPage.clickOnOrderDetails()
        myOrderDetailsPage.waitBySeconds(seconds=5)
        myOrderDetailsPage.validSelfFilmOrders(lePayOrderNumber)

        # 查看我的订单 -- 停车缴费订单状态
        myOrderDetailsPage.clickBackKey()
        myOrderPage.clickOnOrderList()
        myOrderPage.clickOnParkingPayment()
        myOrderPage.clickOnOrderDetails()
        myOrderDetailsPage.waitBySeconds(seconds=5)
        myOrderDetailsPage.validSelfParkingPaymentOrders(lePayOrderNumber,)


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(LefuCancelCatergoryCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)