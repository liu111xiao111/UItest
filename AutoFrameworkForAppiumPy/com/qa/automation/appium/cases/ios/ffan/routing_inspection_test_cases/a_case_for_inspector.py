# -*- coding:utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader
from com.qa.automation.appium.utility.logger import Logger
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.configs.ios_driver_configs import IosDriverConfigs as IDC
from com.qa.automation.appium.pages.ios.ffan.dashboard_page import DashboardPage

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
        dashboardPage.waitBySeconds(100000)




if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(InspectorTimeout)
