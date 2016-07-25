# -*- coding: utf-8 -*-

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
from com.qa.automation.appium.pages.ios.ffan.square_module_page import SquareModulePage
from com.qa.automation.appium.pages.ios.ffan.store_image_text_details_page import StoreImageTextDetailsPage
from com.qa.automation.appium.pages.ios.ffan.store_info_page import StoreInfoPage
from com.qa.automation.appium.utility.logger import Logger


class SquareRecommendCases(TestCase):
    '''
    作者 宋波
    巡检checklist #35
    自动化测试 #35
    广场详情页点击达人推荐可以进入门店详情页
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
        dashboardPage = DashboardPage(self , self.driver , self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnSquareModule()

        squareModulePage = SquareModulePage(self, self.driver, self.logger)
        squareModulePage.validSelf()
        tempText = squareModulePage.clickOnStaffPicks()

        storeInfoPage = StoreInfoPage(self, self.driver, self.logger)
        storeInfoPage.validSelf()
        storeInfoPage.clickOnStoreImageTextDetails()

        storeImageTextDetailsPage = StoreImageTextDetailsPage(self , self.driver , self.logger)
        storeImageTextDetailsPage.validSelf()
        storeImageTextDetailsPage.validKeywords(tempText)
        storeImageTextDetailsPage.clickBackKey()

        storeInfoPage.validSelf()
        storeInfoPage.clickBackKey()

        squareModulePage.validSelf()
        squareModulePage.clickBackKey()

        dashboardPage.validSelf()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(SquareRecommendCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'food-test_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'food-test', 'Result for test')
    runner.run(suite)
