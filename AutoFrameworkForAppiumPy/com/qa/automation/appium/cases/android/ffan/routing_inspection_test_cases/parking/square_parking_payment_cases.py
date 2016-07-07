# -*- coding: utf-8 -*-

from __init__ import *
import unittest
import unittest

import HTMLTestRunner
import HTMLTestRunner

from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare

from com.qa.automation.appium.pages.android.ffan.dashboard_page import *;
from com.qa.automation.appium.pages.android.ffan.square_module_page import *;
from com.qa.automation.appium.pages.android.ffan.square_parking_payment_page import *;
from com.qa.automation.appium.pages.android.ffan.my_ffan_page import *;
from com.qa.automation.appium.configs.driver_configs import *;
from com.qa.automation.appium.driver.appium_driver import *;
from com.qa.automation.appium.utility.logger import Logger;
from com.qa.automation.appium.pages.android.ffan.search_page import SearchPage


class SquareParkingPaymentCases(unittest.TestCase):
    '''
        usage: No.26 广场详情页点击停车，正常进入停车模块
    '''

    def tearDown(self):
        self.driver.quit()

        clearAppData = ClearAppData()
        clearAppData.clearData()

    def setUp(self):
        clearAppData = ClearAppData()
        clearAppData.clearData()

        self.logger = Logger()
        self.driver = AppiumDriver(app_package=appPackage_ffan, app_activity=appActivity_ffan,
                                   platform_name=platformName_andr, platform_version=platformVersion,
                                   device_name=deviceName_andr, driver_url=driver_url
                                   ).getDriver()
        # 登陆　升级
        testPrepare = TestPrepare(testcase=self, driver=self.driver, logger=self.logger)
        testPrepare.prepare()

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnSearchAll()

        searchPage = SearchPage(self, self.driver, self.logger)
        searchPage.validSelf()
        searchPage.inputKeywords(u"北京通州万达广场")
        searchPage.clickOnSearch()
        searchPage.clickOnSpecificSquare()

        squareModulePage = SquareModulePage(self, self.driver, self.logger)
        squareModulePage.validSelf()
        squareModulePage.clickOnParking()

        parkingPaymentPage = ParkingPaymentPage(self, self.driver, self.logger)
        parkingPaymentPage.validSelf()
        parkingPaymentPage.clickBackKey()

        squareModulePage.validSelf()
        squareModulePage.clickBackKey()

        searchPage.clickBackKey()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(SquareParkingPaymentCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'food-test_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='food-test',
                                           description='Result for test')
    runner.run(suite)
