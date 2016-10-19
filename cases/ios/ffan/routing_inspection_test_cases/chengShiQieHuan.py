#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import time
import logging
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from cases.ios.ffan.common.clearAppData import ClearAppData
from configs.iosDriverConfig import IosDriverConfigs as IDC
from driver.appium_driver import AppiumDriver
from pages.ios.ffan.love_shopping_page import LoveShoppingPage
from pages.ios.ffan.switch_city_page import SwitchCityPage
from utility.logger import Logger
from cases.ios.ffan.common.testPrepare import TestPrepare
from pages.ios.ffan.dashboard_page import DashboardPage


class ChenShiQieHuan(TestCase):
    '''
    作者 宋波
    巡检checklist #2
    自动化测试 #2
    启动APP，城市切换正常
    '''

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(None, None, IDC.platformName, IDC.platformVersion,
                                   IDC.deviceName, IDC.driverUrl, IDC.bundleId, IDC.udid).getDriver()
        self.reset = ClearAppData(self.driver)
        self.reset.clearData()
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

    '''
    def test_case_step_1(self):
        switchCityPage = SwitchCityPage(self, self.driver, self.logger)
        for tempTimes in range(5):
            logging.info("ATTEMPTS: %d" % (tempTimes + 1))
            if switchCityPage.validSelf(False):
                return
            switchCityPage.waitBySeconds(2)

        loveShoppingPage = LoveShoppingPage(self, self.driver, self.logger)
        loveShoppingPage.validSelf()
        tempCityName = loveShoppingPage.getCurrentCityName()
        loveShoppingPage.clickOnCityName()
        loveShoppingPage.waitBySeconds()
        loveShoppingPage.switchCity(tempCityName)
        loveShoppingPage.validSelf()

    def test_case_step_2(self):
        switchCityPage = SwitchCityPage(self, self.driver, self.logger)
        for tempTimes in range(5):
            logging.info("ATTEMPTS: %d" % (tempTimes + 1))
            if switchCityPage.validSelf(False):
                switchCityPage.cancelSwitchCity()
                break
            switchCityPage.waitBySeconds(2)
        switchCityPage.invalidSelf()
    '''


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(ChenShiQieHuan)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
