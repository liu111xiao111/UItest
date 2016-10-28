# -*- coding: utf-8 -*-

import os
import time
from unittest import TestCase
from unittest import TestLoader
from configs.iosDriverConfig import IosDriverConfigs as IDC
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from pages.ios.shanghu.dengLuPage import DengLuPage
from pages.ios.shanghu.homePage import HomePage


class TuiChuDengLuCase(TestCase):
    '''
    退出登录验证
    '''

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(None, None, IDC.platformName, IDC.platformVersion,
                                   IDC.deviceName, IDC.driverUrl, IDC.bundleId, IDC.udid).getDriver()

    def test_case(self):
        pass

    def tearDown(self):
        self.driver.quit()



