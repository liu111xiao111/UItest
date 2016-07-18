# -*- coding:utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.configs.ios_driver_configs import IosDriverConfigs as IDC
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.ios.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.ios.ffan.square_module_page import SquareModulePage
from com.qa.automation.appium.pages.ios.ffan.square_indoor_map_page import SquareIndoorMapPage
from com.qa.automation.appium.pages.ios.ffan.location_bluetooth_page import LocationBluetoothPage
from com.qa.automation.appium.utility.logger import Logger


class SquareIndoorMapCases(TestCase):
    '''
        巡检checklist #25
        自动化测试 #25
        广场详情页点击室内地图，正常进入室内地图模块
    '''

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(None,
                                   None,
                                   IDC.platformName,
                                   IDC.platformVersion,
                                   IDC.deviceName,
                                   IDC.driverUrl,
                                   IDC.bundleId,
                                   IDC.udid).getDriver()

        self.reset = ClearAppData(self.driver)
        self.reset.clearData()

    def test_case(self):
        dashboardPage = DashboardPage(testcase=self, driver=self.driver, logger=self.logger)
        squarePage = SquareModulePage(testcase=self, driver=self.driver, logger=self.logger)
        locationBluetoothPage = LocationBluetoothPage(testcase=self, driver=self.driver, logger=self.logger)
        indoormapPage = SquareIndoorMapPage(testcase=self, driver=self.driver, logger=self.logger)

        # 首页进入广场页
        dashboardPage.validSelf();
        dashboardPage.clickOnSquareModule()
        squarePage.validSelf();

        # 点击室内地图
        squarePage.clicOnIndoorMap();
        locationBluetoothPage.clickOnOkBtn()
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