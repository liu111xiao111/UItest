# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage;
from com.qa.automation.appium.pages.android.ffan.square_module_page import SquareModulePage;
from com.qa.automation.appium.pages.android.ffan.square_indoor_map_page import SquareIndoorMapPage;
from com.qa.automation.appium.pages.android.ffan.location_bluetooth_page import LocationBluetoothPage;
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url
from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.configs.driver_configs import platformVersion
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.utility.logger import Logger;

from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData


class SquareIndoorMapCases(TestCase):
    '''
		巡检checklist #25
		自动化测试 #25
		广场详情页点击室内地图，正常进入室内地图模块
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

        # Login & update version
        testPrepare = TestPrepare(testcase=self, driver=self.driver, logger=self.logger)
        testPrepare.prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(testcase=self, driver=self.driver, logger=self.logger)
        squarePage = SquareModulePage(testcase=self, driver=self.driver, logger=self.logger)
        locationBluetoothPage = LocationBluetoothPage(testcase=self, driver=self.driver, logger=self.logger)
        indoormapPage = SquareIndoorMapPage(testcase=self, driver=self.driver, logger=self.logger)

        # Load square page
        dashboardPage.validSelf();
        dashboardPage.clickOnSquareModule()
        squarePage.validSelf();

        # Click "室内地图", cancle bluetooth setting, load "室内地图" page.
        squarePage.clicOnIndoorMap();
        locationBluetoothPage.clickOnCancleBtn()
        indoormapPage.validSelf();
        indoormapPage.clickOnFoodMap();
        indoormapPage.validSelfFood();

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(SquareIndoorMapCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)