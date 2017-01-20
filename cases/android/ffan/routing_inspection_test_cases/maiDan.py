# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from cases.android.ffan.common.test_prepare import TestPrepare
from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.square_lefu_pay_page import SquareLefuPayPage
from pages.android.ffan.lefu_pay_detail_page import LefuPayDetailPage
from pages.android.ffan.lefu_pay_way_page import LefuPayWayPage
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from configs.driver_configs import platformName_andr
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil
from cases.logger import logger


class MaiDanTestCase(TestCase):
    '''
    巡检 No.17
    用例名 买单
    首页进入乐付买单（城市维度），并下单，取消订单，支付（虚拟城市），并查看相应订单状态
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

    def testMaiDan(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        lefuPage = SquareLefuPayPage(self, self.driver, self.logger)
        lefuPayDetailPage = LefuPayDetailPage(self, self.driver, self.logger)
        lefuPayWayPage = LefuPayWayPage(self, self.driver, self.logger)

        # Load square page
        dashboardPage.validSelf();
        dashboardPage.screenShot("aiGuangJie")
        dashboardPage.clickOnLefuCategory()
        lefuPage.validSelf();
        lefuPage.screenShot("maiDan")

        # Click "乐付买单"， load detail pay page.
        lefuPage.clickOnLefuPay();
        lefuPayDetailPage.validSelf();
        lefuPayDetailPage.screenShot("maiDanFuKuan")

        # Input money, click "确认买单".
        lefuPayDetailPage.inputMoney();
        lefuPayDetailPage.screenShot("maiDanFuKuan")
        lefuPayDetailPage.waitBySeconds(seconds=5)
        lefuPayDetailPage.clickOnPay();
        lefuPayWayPage.validSelf();
        lefuPayWayPage.screenShot("maiDanFuKuanFangShi")


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(MaiDanTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)