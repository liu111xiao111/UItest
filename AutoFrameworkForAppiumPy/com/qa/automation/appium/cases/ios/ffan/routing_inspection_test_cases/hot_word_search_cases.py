#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from com.qa.automation.appium.cases.ios.ffan.common.clear_app_data import ClearAppData
# from com.qa.automation.appium.cases.ios.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.configs.ios_driver_configs import IosDriverConfigs as IDC
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.ios.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.ios.ffan.search_page import SearchPage
from com.qa.automation.appium.pages.ios.ffan.store_info_page import StoreInfoPage
from com.qa.automation.appium.utility.logger import Logger


sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
                os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
                os.path.dirname(sys.path[0]))))))))))



class HotWordSearchCases(TestCase):
    '''
    巡检checklist No.: 04
    自动化测试case No.: 04
    查看搜索中的热词并点击，热词显示正常点击进入内容无误
    '''

    def tearDown(self):
        self.driver.quit()
        ClearAppData().clearData()

    def setUp(self):
        ClearAppData().clearData()
        self.logger = Logger()
        self.driver = AppiumDriver(None, None, IDC.platformName, IDC.platformVersion,
                                   IDC.deviceName, IDC.driverUrl, IDC.bundleId, IDC.udid).getDriver()

#         TestPrepare(self, self.driver, self.logger).prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.valid_self()
        dashboardPage.clickOnSearchAll()

        searchPage = SearchPage(self, self.driver, self.logger)
        searchPage.validSelf()
        searchPage.clickOnMovie()
        searchPage.validSearchResult(u"电影", "//UIAApplication[1]/UIAWindow[1]/UIATableView[2]/UIATableCell[1]/UIAStaticText[1]")
        searchPage.clickOnSpecificMovie()

        storeInfoPage = StoreInfoPage(self, self.driver, self.logger)
        storeInfoPage.validSelf()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(HotWordSearchCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
