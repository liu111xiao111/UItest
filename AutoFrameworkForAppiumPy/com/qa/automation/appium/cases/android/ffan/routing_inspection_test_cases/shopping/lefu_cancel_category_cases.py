# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage;
from com.qa.automation.appium.pages.android.ffan.square_lefu_pay_page import SquareLefuPayPage;
from com.qa.automation.appium.pages.android.ffan.lefu_pay_detail_page import LefuPayDetailPage
from com.qa.automation.appium.pages.android.ffan.lefu_pay_way_page import LefuPayWayPage
from com.qa.automation.appium.pages.android.ffan.lefu_cancel_order_page import LefuCancelOrderPage
from com.qa.automation.appium.pages.android.ffan.my_ffan_page import MyFfanPage
from com.qa.automation.appium.pages.android.ffan.my_ffan_my_order_page import MyFfanMyOrderPage
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url
from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.configs.driver_configs import platformVersion
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.utility.logger import Logger;


class LefuCancelCatergoryCases(TestCase):
    '''
        巡检checklist #15
        自动化测试 #15-2
        首页进入乐付买单（城市维度），并下单，取消订单，支付（虚拟城市），并查看相应订单状态
    '''

    def tearDown(self):
        self.driver.quit()

        clearAppData = ClearAppData()
        clearAppData.clearData()

    def setUp(self):
        clearAppData = ClearAppData()
        clearAppData.clearData()

        self.logger = Logger()
        self.driver = AppiumDriver(appPackage_ffan,
                                   appActivity_ffan,
                                   platformName_andr,
                                   platformVersion,
                                   deviceName_andr,
                                   driver_url).getDriver()

        # Login & update version
        TestPrepare(self, self.driver, self.logger).prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        lefuPage = SquareLefuPayPage(self, self.driver, self.logger)
        lefuPayDetailPage = LefuPayDetailPage(self, self.driver, self.logger)
        lefuPayWayPage = LefuPayWayPage(self, self.driver, self.logger)
        lefuCancelOrderPage = LefuCancelOrderPage(self, self.driver, self.logger)
        myFfanPage = MyFfanPage(self, self.driver, self.logger)
        myOrderPage = MyFfanMyOrderPage(self, self.driver, self.logger)

        # Load square page
        dashboardPage.validSelf();
        dashboardPage.clickOnLefuCategory()
        lefuPage.validSelf();

        # Click "乐付买单"， load detail pay page.
        lefuPage.clickOnLefuPay();
        lefuPayDetailPage.validSelf();

        # Input money, click "确认买单".
        lefuPayDetailPage.inputMoney();
        lefuPayDetailPage.waitBySeconds(seconds=3);
        lefuPayDetailPage.clickOnPay();
        lefuPayWayPage.validSelf();
        lefuPayWayPage.waitBySeconds(2);
        lefuOrderNumber = lefuPayWayPage.getOrderNumber();

        # Cancel the order
        lefuPayWayPage.clickBackKey();
        lefuCancelOrderPage.clickOnConfirmBtn();
        lefuPayDetailPage.clickBackKey();
        lefuPage.clickBackKey();

        dashboardPage.clickOnMy();
        myFfanPage.validSelf();
        myFfanPage.clickOnMyOrder();
        myOrderPage.validSelf();
        myOrderPage.waitBySeconds(seconds=2);
        myOrderNumber = myOrderPage.getOrderNumber();

        #Judge order number
        if lefuOrderNumber == myOrderNumber[5:]:
            print("Order display correctly in ALL Orders tab!")
        else:
            print("Not find new order number!")

        myOrderPage.clickOnOrderNoPay();
        print("Order display correctly in To be Paid Orders tab!")
        #myOrderNumberNoPay = myOrderPage.getOrderNumber();
        #Judge order number
        '''if lefuOrderNumber != myOrderNumberNoPay[5:]:
            print("Order display correctly in To be Paid Orders tab!")
        else:
            print("Order error!")'''
        myOrderPage.clickOnOrderPaid();
        myOrderNumberPaid = myOrderPage.getOrderNumber();
        #Judge order number
        if lefuOrderNumber != myOrderNumberPaid[5:]:
            print("Order display correctly in Have Been Paid Orders tab!")
        else:
            print("Order error!")


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(LefuCancelCatergoryCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)