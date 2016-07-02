# -*- coding: utf-8 -*-

import sys,os
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))))

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

import unittest
import HTMLTestRunner


class LefuCancelCatergoryCases(unittest.TestCase):
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
        self.driver = AppiumDriver(app_package=appPackage_ffan, app_activity=appActivity_ffan,
                                   platform_name=platformName_andr, platform_version=platformVersion,
                                   device_name=deviceName_andr, driver_url=driver_url
                                   ).getDriver()

        # Login & update version
        testPrepare = TestPrepare(testcase=self, driver=self.driver, logger=self.logger)
        testPrepare.prepare()

    def test_case(self):
        dashboardPage = DashboardPage(testcase=self, driver=self.driver, logger=self.logger)
        lefuPage = SquareLefuPayPage(testcase=self, driver=self.driver, logger=self.logger)
        lefuPayDetailPage = LefuPayDetailPage(testcase=self, driver=self.driver, logger=self.logger)
        lefuPayWayPage = LefuPayWayPage(testcase=self, driver=self.driver, logger=self.logger)
        lefuCancelOrderPage = LefuCancelOrderPage(testcase=self, driver=self.driver, logger=self.logger)
        myFfanPage = MyFfanPage(testcase=self, driver=self.driver, logger=self.logger)
        myOrderPage = MyFfanMyOrderPage(testcase=self, driver=self.driver, logger=self.logger)

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
            print("Order display correctly!")
        else:
            print("Not find new order number!")

        myOrderPage.clickOnOrderNoPay();
        #myOrderNumberNoPay = myOrderPage.getOrderNumber();
        #Judge order number
        '''if lefuOrderNumber != myOrderNumberNoPay[5:]:
            print("Order display correctly!")
        else:
            print("Order error!")'''
        myOrderPage.clickOnOrderPaid();
        myOrderNumberPaid = myOrderPage.getOrderNumber();
        #Judge order number
        if lefuOrderNumber != myOrderNumberPaid[5:]:
            print("Order display correctly!")
        else:
            print("Order error!")


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(LefuCancelCatergoryCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)