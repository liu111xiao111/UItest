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
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.utility.logger import Logger
from com.qa.automation.appium.utility.device_info_util import DeviceInfoUtil
from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData


class SquareIndoorMapCases(TestCase):
    '''
    作者 刘涛
	巡检checklist #25
	自动化测试 #25
	广场详情页点击室内地图，正常进入室内地图模块
    '''

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(appPackage_ffan,
                                   appActivity_ffan,
                                   platformName_andr,
                                   DeviceInfoUtil().getBuildVersion(),
                                   deviceName_andr,
                                   driver_url).getDriver()

        self.reset = ClearAppData(self.driver)
        self.reset.clearData()

        TestPrepare(self, self.driver, self.logger).prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        squarePage = SquareModulePage(self, self.driver, self.logger)
        locationBluetoothPage = LocationBluetoothPage(self, self.driver, self.logger)
        indoormapPage = SquareIndoorMapPage(self, self.driver, self.logger)

        # Load square page
        dashboardPage.validSelf()
        dashboardPage.clickOnSquareModule()
        squarePage.validSelf()

        # Click "室内地图", cancle bluetooth setting, load "室内地图" page.
        squarePage.clicOnIndoorMap()
        locationBluetoothPage.clickOnCancleBtn()
        indoormapPage.validSelf()
        indoormapPage.clickOnSwitchMap()
        indoormapPage.clickOnFoodMap()
        indoormapPage.validSelfFood()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(SquareIndoorMapCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)