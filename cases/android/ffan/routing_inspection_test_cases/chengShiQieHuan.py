# -*- coding:utf-8 -*-

import os
import time
import logging
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from configs.driver_configs import platformName_andr
from driver.appium_driver import AppiumDriver
from pages.android.ffan.switch_city_page import SwitchCityPage
from utility.device_info_util import DeviceInfoUtil
from utility.logger import Logger
from cases.logger import logger


class ChengShiQieHuanTestCase(TestCase):
    '''
    巡检 No.02
    用例名: 城市切换
    启动APP，城市切换正常
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

    def testChengShiQieHuan_2(self):
        switchCityPage = SwitchCityPage(self, self.driver, self.logger)
        for tempTimes in range(5):
            logging.info("ATTEMPTS: %d" % (tempTimes + 1))
            if switchCityPage.validSelf(False):
                switchCityPage.screenShot("chengShiQieHuan")
                switchCityPage.cancelSwitchCity()
                break
            switchCityPage.waitBySeconds(2)
        switchCityPage.invalidSelf()
        switchCityPage.screenShot("chengShiQieHuan")


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(ChengShiQieHuanTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report', description='Result for test')
    runner.run(suite)
