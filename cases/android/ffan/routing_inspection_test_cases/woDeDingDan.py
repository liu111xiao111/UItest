# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from cases.android.ffan.common.test_prepare import TestPrepare
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
from cases.logger import logger


class WoDeDingDanTestCase(TestCase):
    '''
    回归用例： No.24
    用例名: 我的订单
    查看我的订单信息及状态是否正确
    '''
    @classmethod
    def setUpClass(cls):
        '''
        初始化Appium driver
        '''
        cls.driver = AppiumDriver(appPackage_ffan,
                                   appActivity_ffan,
                                   platformName_andr,
                                   DeviceInfoUtil().getBuildVersion(),
                                   deviceName_andr,
                                   driver_url).getDriver()
        logger.info("Appium client init completed")

    def tearDown(self):
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        TestPrepare(self, self.driver, self.logger).prepare()

    def testWoDeDingDan(self):
        # 验证首页
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.screenShot("aiGuangJie")

        # 点击我的，查看我的订单状态
        dashboardPage.clickOnMy()
        myFfanPage = MyFfanPage(self, self.driver, self.logger)
        myFfanPage.validSelf()
        myFfanPage.screenShot("woDe")
        myFfanPage.clickOnMyOrder()
        myOrderPage = MyFfanMyOrderPage(self, self.driver, self.logger)
        myOrderPage.validSelf()
        myOrderPage.screenShot("woDeDingDan")
        myOrderPage.clickBackKey()
        myFfanPage.validSelf()
        myFfanPage.screenShot("woDe")

        # 查看我的订单 -- 点击我的订单待付款
        myFfanPage.clickOnToBePaid()
        myFfanPage.validSelfToBePaid()
        myFfanPage.screenShot("woDeDaiFuKuan")
        myFfanPage.clickBackKey()
        myFfanPage.validSelf()
        myFfanPage.screenShot("woDe")

        # 查看我的订单 -- 点击我的订单可使用
        myFfanPage.clickOnUse()
        myFfanPage.validSelfUse()
        myFfanPage.screenShot("woDeKeShiYong")
        myFfanPage.clickBackKey()
        myFfanPage.validSelf()
        myFfanPage.screenShot("woDe")

        # 查看我的订单 -- 点击我的订单我的点评
        myFfanPage.clickOnComments()
        myFfanPage.validSelfCommets()
        myFfanPage.screenShot("woDeDianPing")
        myFfanPage.clickBackKey()
        myFfanPage.validSelf()
        myFfanPage.screenShot("woDe")

        # 查看我的订单 -- 点击我的订单退货退款
        myFfanPage.clickOnReturnRefund()
        myFfanPage.validSelfReturnRefund()
        myFfanPage.screenShot("woDeTuiHuoTuiKuan")


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(WoDeDingDanTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)