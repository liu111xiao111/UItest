# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.android.ffan.my_ffan_page import MyFfanPage
from com.qa.automation.appium.pages.android.ffan.my_ffan_my_order_page import MyFfanMyOrderPage
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url
from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.utility.logger import Logger
from com.qa.automation.appium.utility.device_info_util import DeviceInfoUtil


class MyfeifanMyOrderCases(TestCase):
    '''
    作者 乔佳溪
    巡检checklist #52
    自动化测试 #52
    查看我的订单信息及状态是否正确 
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
        myFfanPage = MyFfanPage(self, self.driver, self.logger)
        myOrderPage = MyFfanMyOrderPage(self, self.driver, self.logger)

        # 查看我的订单状态
        dashboardPage.clickOnMy()
        myFfanPage.validSelf()
        myFfanPage.clickOnMyOrder()
        myOrderPage.validSelf()
        myOrderPage.clickBackKey()
        myFfanPage.validSelf()

        # 查看我的订单 -- 点击我的订单待付款
        myFfanPage.clickOnToBePaid()
        myFfanPage.validSelfToBePaid()
        myFfanPage.clickBackKey()

        # 查看我的订单 -- 点击我的订单可使用
        myFfanPage.clickOnUse()
        myFfanPage.validSelfUse()
        myFfanPage.clickBackKey()

        # 查看我的订单 -- 点击我的订单我的点评
        myFfanPage.clickOnComments()
        myFfanPage.validSelfCommets()
        myFfanPage.clickBackKey()

        # 查看我的订单 -- 点击我的订单退货退款
        myFfanPage.clickOnReturnRefund()
        myFfanPage.validSelfReturnRefund()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(MyfeifanMyOrderCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)