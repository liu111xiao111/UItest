# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from cases.android.ffan.common.test_prepare import TestPrepare
from cases.android.ffan.common.clear_app_data import ClearAppData
from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.my_ffan_page import MyFfanPage
from pages.android.ffan.my_ffan_my_order_page import MyFfanMyOrderPage
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from configs.driver_configs import platformName_andr
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil


class WoDeDingDanTestCase(TestCase):
    '''
    巡检 No.52
    用例名 我的订单
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

    def testWoDeDingDanTestCase(self):
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
    suite = TestLoader().loadTestsFromTestCase(WoDeDingDanTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)