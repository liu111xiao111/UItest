# -*- coding:utf-8 -*-

import os
import time
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from cases.android.ffan.common.test_prepare import TestPrepare
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from configs.driver_configs import platformName_andr
from driver.appium_driver import AppiumDriver
from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.supermarket_page import SupermarketPage
from utility.device_info_util import DeviceInfoUtil
from utility.logger import Logger
from cases.logger import logger


class ShangChaoTestCase(TestCase):
    '''
    回归用例： No.6
    用例名: 商超
    首页进入签到可以正常签到，如城市沈阳（有便利店的城市显示商超，点击进入商超列表，如城市北京）
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
        TestPrepare(self, self.driver, self.logger).prepare(False)

    def testShangChao(self):
        # 验证首页
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.screenShot("aiGuangJie")

        # 首页(爱逛街页面)点击商超，进入商店超市页面
        dashboardPage.clickOnSupermarket()
        supermarketPage = SupermarketPage(self, self.driver, self.logger)
        supermarketPage.validSelf()
        supermarketPage.screenShot("shangChao")


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(ShangChaoTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)