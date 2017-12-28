# -*- coding:utf-8 -*-

import os
import time
import HTMLTestRunner
import requests

from unittest import TestCase
from unittest import TestLoader
from utility.logger import Logger
from driver.appium_driver import AppiumDriver
from configs.iosDriverConfig import IosDriverConfigs as IDC
from pages.ios.ffan.dashboard_page import DashboardPage

from utility.device_info_util import DeviceInfoUtil

class InspectorTimeout(TestCase):


    def test_case(self):
        self.logger = Logger()
        self.driver = AppiumDriver(None,
                                   None,
                                   IDC.platformName,
                                   IDC.platformVersion,
                                   IDC.deviceName,
                                   IDC.driverUrl,
                                   IDC.bundleId,
                                   IDC.udid).getDriver()
        dashboardPage = DashboardPage(testcase=self, driver=self.driver, logger=self.logger)

        DeviceInfoUtil.getIPhoneType(self)

        dashboardPage.waitBySeconds(60000)
        pass;


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(InspectorTimeout)


