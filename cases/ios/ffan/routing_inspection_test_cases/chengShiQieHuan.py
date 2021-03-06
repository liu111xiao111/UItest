#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import time
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from configs.iosDriverConfig import IosDriverConfigs as IDC
from driver.appium_driver import AppiumDriver
from pages.ios.ffan.switch_city_page import SwitchCityPage
from cases.ios.ffan.common.testPrepare import TestPrepare
from pages.ios.ffan.dashboard_page import DashboardPage
from cases.logger import logger


class ChenShiQieHuanTestCase(TestCase):
    '''
    作者 宋波
    巡检checklist #2
    自动化测试 #2
    启动APP，城市切换正常
    '''

    @classmethod
    def setUpClass(cls):
        '''
        初始化Appium driver
        '''

        cls.driver = AppiumDriver(None,
                                  None,
                                  IDC.platformName,
                                  IDC.platformVersion,
                                  IDC.deviceName,
                                  IDC.driverUrl,
                                  IDC.bundleId,
                                  IDC.udid).getDriver()
        logger.info("Appium client init completed")

    def setUp(self):
        self.logger = logger

        logger.info("Clear data completed")
        TestPrepare(self, self.driver, self.logger).prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        switchCityPage = SwitchCityPage(self, self.driver, self.logger)

        dashboardPage.validSelf()

        dashboardPage.clickOnCity()
        dashboardPage.waitBySeconds(2)

        switchCityPage.inputBeijing()
        dashboardPage.waitBySeconds(2)

        switchCityPage.clickOnCityListFirst()
        dashboardPage.waitBySeconds(2)

        dashboardPage.validBeijing()

        dashboardPage.validCityData()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(ChenShiQieHuanTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
