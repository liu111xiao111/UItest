#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import time
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from com.qa.automation.appium.cases.ios.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.configs.ios_driver_configs import IosDriverConfigs as IDC
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.ios.ffan.love_shopping_page import LoveShoppingPage
from com.qa.automation.appium.pages.ios.ffan.switch_city_page import SwitchCityPage
from com.qa.automation.appium.utility.logger import Logger


class SwitchCityCases(TestCase):
    '''
    作者 宋波
    飞凡No. FFAPP-59
    自动化测试 FFAPP-59
    首页=>城市切换
    '''

    cityName = None
    commercialDistrictName = None

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(None, None, IDC.platformName, IDC.platformVersion,
                                   IDC.deviceName, IDC.driverUrl, IDC.bundleId, IDC.udid).getDriver()
        self.reset = ClearAppData(self.driver)
        self.reset.clearData()

    def test_case_step_1(self):
        switchCityPage = SwitchCityPage(self, self.driver, self.logger)
        for tempTimes in range(5):
            print("ATTEMPTS: %d" % (tempTimes + 1))
            if switchCityPage.validSelf(False):
                switchCityPage.cancelSwitchCity()
                break
            switchCityPage.waitBySeconds(2)

        loveShoppingPage = LoveShoppingPage(self, self.driver, self.logger)
        loveShoppingPage.validSelf()
        tempCityName = loveShoppingPage.getCurrentCityName()
        loveShoppingPage.clickOnCityName()
        loveShoppingPage.waitBySeconds()
        tempCityName = loveShoppingPage.switchCity(tempCityName)
        loveShoppingPage.validSelf()
        loveShoppingPage.validCurrentCityName(tempCityName)
        SwitchCityCases.cityName = tempCityName
        SwitchCityCases.commercialDistrictName = loveShoppingPage.getCurrentCommercialDistrictName()

    def test_case_step_2(self):
        switchCityPage = SwitchCityPage(self, self.driver, self.logger)
        for tempTimes in range(5):
            print("ATTEMPTS: %d" % (tempTimes + 1))
            if switchCityPage.validSelf(False):
                switchCityPage.cancelSwitchCity()
                break
            switchCityPage.waitBySeconds(2)

        loveShoppingPage = LoveShoppingPage(self, self.driver, self.logger)
        loveShoppingPage.validSelf()
        loveShoppingPage.validCurrentCityName(self.cityName)
        loveShoppingPage.validCurrentCommercialDistrictName(self.commercialDistrictName)

    def test_case_step_3(self):
        switchCityPage = SwitchCityPage(self, self.driver, self.logger)
        for tempTimes in range(5):
            print("ATTEMPTS: %d" % (tempTimes + 1))
            if switchCityPage.validSelf(False):
                tempText = switchCityPage.getCityOrientation()
                switchCityPage.confirmSwitchCity()
                break
            switchCityPage.waitBySeconds(2)
        switchCityPage.invalidSelf()

        loveShoppingPage = LoveShoppingPage(self, self.driver, self.logger)
        loveShoppingPage.validSelf()
        loveShoppingPage.validCurrentCityName(tempText)

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(SwitchCityCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
