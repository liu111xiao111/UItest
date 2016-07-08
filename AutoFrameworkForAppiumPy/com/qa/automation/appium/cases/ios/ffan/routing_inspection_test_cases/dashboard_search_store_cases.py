# -*- coding: utf-8 -*-

import sys, os
import time
import unittest

import HTMLTestRunner

from com.qa.automation.appium.cases.ios.ffan.common.clear_app_data import ClearAppData
# from com.qa.automation.appium.cases.ios.ffan.common.test_prepare import TestPrepare


sys.path.append(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))))

from com.qa.automation.appium.pages.ios.ffan.dashboard_page import DashboardPage;
from com.qa.automation.appium.pages.ios.ffan.search_page import SearchPage;
from com.qa.automation.appium.configs.ios_driver_configs import IosDriverConfigs as IDC
from com.qa.automation.appium.pages.ios.ffan.my_ffan_page import *;
from com.qa.automation.appium.configs.driver_configs import *;
from com.qa.automation.appium.driver.appium_driver import AppiumDriver;
from com.qa.automation.appium.utility.logger import Logger;


class DashboardSearchStoreCases(unittest.TestCase):
    '''
        巡检checklist No.: 3
        自动化测试case No.: 5
        全城搜索商品
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
        dashboardPage.clickOnSearchView()

        searchPage = SearchPage(self, self.driver, self.logger)
        searchPage.validSelf()
        searchPage.inputStoreName()
        searchPage.clickOnSearch()
        searchPage.wait_by_seconds(10)
        searchPage.validSearchResult(u"北京石景山店", u"//UIAApplication[1]/UIAWindow[1]/UIATableView[2]/UIATableCell[1]/UIAStaticText[1]")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(DashboardSearchStoreCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'food-test_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='food-test',
                                           description='Result for test')
    runner.run(suite)