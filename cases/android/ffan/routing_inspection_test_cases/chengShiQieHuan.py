# -*- coding:utf-8 -*-

import os
import time
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
    回归用例： No.1
    用例名: 城市切换
    定位到当前城市，确认弹出切换城市对话框，切换完，首页显示当前城市下的数据
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

    def testChengShiQieHuan(self):
        switchCityPage = SwitchCityPage(self, self.driver, self.logger)
        # 如果弹出切换城市Popup，点击取消按钮
        if switchCityPage.validSelf():
            switchCityPage.screenShot("chengShiQieHuan")
            switchCityPage.cancelSwitchCity()
        switchCityPage.waitBySeconds(2)
        # 验证当前城市为北京
        switchCityPage.validSelfCity()
        switchCityPage.screenShot("chengShiQieHuan")


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(ChengShiQieHuanTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report', description='Result for test')
    runner.run(suite)
