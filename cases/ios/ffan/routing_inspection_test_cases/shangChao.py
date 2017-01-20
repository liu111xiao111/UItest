#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import time
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from cases.ios.ffan.common.clearAppData import ClearAppData
from cases.ios.ffan.common.testPrepare import TestPrepare
from configs.iosDriverConfig import IosDriverConfigs as IDC
from driver.appium_driver import AppiumDriver
from pages.ios.ffan.dashboard_page import DashboardPage
from pages.ios.ffan.store_info_page import StoreInfoPage
from pages.ios.ffan.stores_and_supermarkets_page import StoresAndSupermarketsPage
from pages.ios.ffan.switch_city_page import SwitchCityPage
from cases.logger import logger


class ShangChaoTestCase(TestCase):
    '''
    作者 宋波
    巡检checklist #Anonymous
    自动化测试 #Anonymous
    启动APP，商超显示正常。
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
        self.reset = ClearAppData(self.driver)
        self.reset.clearData()
        logger.info("Clear data completed")
        TestPrepare(self, self.driver, self.logger).prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        #dashboardPage.clickOnCity()

        #switchCityPage = SwitchCityPage(self, self.driver, self.logger)
        #switchCityPage.inputCities(u"厦门市")
        #switchCityPage.clickOnCityListFirst()

        #dashboardPage.validCities(u"厦门市")
        dashboardPage.clickOnStores()

        storesAndSupermarketsPage = StoresAndSupermarketsPage(self, self.driver, self.logger)
        storesAndSupermarketsPage.validSelf()
        tempText = storesAndSupermarketsPage.clickOnStoreOrSupermarket()

        storeInfoPage = StoreInfoPage(self, self.driver, self.logger)
        storeInfoPage.validKeywords(tempText)
        storeInfoPage.clickBackKey()

        storesAndSupermarketsPage.validSelf()
        storesAndSupermarketsPage.clickBackKey()

        #dashboardPage.validSelf()
        #dashboardPage.clickOnCity()

        #switchCityPage.inputCities(u"北京市")
        #switchCityPage.clickOnCityListFirst()

        #dashboardPage.validCities(u"北京市")

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(ShangChaoTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
