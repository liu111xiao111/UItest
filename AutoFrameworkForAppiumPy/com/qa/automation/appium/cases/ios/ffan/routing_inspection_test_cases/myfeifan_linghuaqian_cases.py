# -*- coding:utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader
from com.qa.automation.appium.utility.logger import Logger
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.cases.ios.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.configs.ios_driver_configs import IosDriverConfigs as IDC
from com.qa.automation.appium.cases.ios.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.pages.ios.ffan.my_ffan_page import MyFfanPage
from com.qa.automation.appium.pages.ios.ffan.my_ffan_my_order_page import MyFfanMyOrderPage
from com.qa.automation.appium.pages.ios.ffan.dashboard_page import DashboardPage


class MyLinghuaqianCases(TestCase):
    '''
    作者 刘涛
    我的订单
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
        myFfanPage = MyFfanPage(self, self.driver, self.logger)


        #点击我的
        dashboardPage.clickOnMy()
        myFfanPage.validSelf()

        #进入我的飞凡通
        myFfanPage.gotoWodefeifantong()
        #验证零花钱
        myFfanPage.validLinghuaqian()






if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(MyLinghuaqianCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)