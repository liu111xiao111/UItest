# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from cases.android.ffan.common.test_prepare import TestPrepare
from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.my_ffan_page import MyFfanPage
from pages.android.ffan.my_ffan_my_parking_payment_page import MyFfanMyParkingPaymentPage
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from configs.driver_configs import platformName_andr
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil
from cases.logger import logger


class WoDeTingCheJiaoFeiTestCase(TestCase):
    '''
    回归用例： No.28
    用例名: 我的停车缴费
    点击停车缴费，成功进入并显示正确数据
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

    def testWoDeTingCheJiaoFei(self):
        # 验证首页
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        myFfanPage = MyFfanPage(self, self.driver, self.logger)
        parkingPaymentPage = MyFfanMyParkingPaymentPage(self, self.driver, self.logger)

        # 点击我的，进入 "停车交费"页面
        dashboardPage.validSelf();
        dashboardPage.screenShot("aiGuangJie")
        dashboardPage.clickOnMy();
        myFfanPage.validSelf();
        myFfanPage.screenShot("woDe")
        myFfanPage.clickOnParkingPayment();
        parkingPaymentPage.validSelf();
        parkingPaymentPage.screenShot("tingChe")


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(WoDeTingCheJiaoFeiTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report', description='Result for test')
    runner.run(suite)