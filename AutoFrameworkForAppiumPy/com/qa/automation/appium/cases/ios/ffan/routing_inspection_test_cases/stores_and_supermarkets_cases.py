#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import time
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from com.qa.automation.appium.cases.ios.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.ios.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.configs.ios_driver_configs import IosDriverConfigs as IDC
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.ios.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.ios.ffan.store_info_page import StoreInfoPage
from com.qa.automation.appium.pages.ios.ffan.stores_and_supermarkets_page import StoresAndSupermarketsPage
from com.qa.automation.appium.pages.ios.ffan.switch_city_page import SwitchCityPage
from com.qa.automation.appium.utility.logger import Logger


class StoresAndSupermarketsCases(TestCase):
    '''
    作者 宋波
    巡检checklist #Anonymous
    自动化测试 #Anonymous
    启动APP，商超显示正常。
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
        dashboardPage.validSelf()
        dashboardPage.clickOnCity()

        switchCityPage = SwitchCityPage(self, self.driver, self.logger)
        switchCityPage.inputCities(u"厦门市")
        switchCityPage.clickOnCityListFirst()

        dashboardPage.validCities(u"厦门市")
        dashboardPage.clickOnStores()

        storesAndSupermarketsPage = StoresAndSupermarketsPage(self, self.driver, self.logger)
        storesAndSupermarketsPage.validSelf()
        tempText = storesAndSupermarketsPage.clickOnStoreOrSupermarket()

        storeInfoPage = StoreInfoPage(self, self.driver, self.logger)
        storeInfoPage.validKeywords(tempText)
        storeInfoPage.clickBackKey()

        storesAndSupermarketsPage.validSelf()
        storesAndSupermarketsPage.clickBackKey()

        dashboardPage.validSelf()
        dashboardPage.clickOnCity()

        switchCityPage.inputCities(u"北京市")
        switchCityPage.clickOnCityListFirst()

        dashboardPage.validCities(u"北京市")


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(StoresAndSupermarketsCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
