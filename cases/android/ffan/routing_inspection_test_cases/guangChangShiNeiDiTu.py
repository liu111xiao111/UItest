# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.square_module_page import SquareModulePage
from pages.android.ffan.square_indoor_map_page import SquareIndoorMapPage
from pages.android.ffan.location_bluetooth_page import LocationBluetoothPage
from pages.android.ffan.search_page import SearchPage
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from configs.driver_configs import platformName_andr
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil
from cases.android.ffan.common.test_prepare import TestPrepare
from cases.logger import logger


class GuangChangShiNeiDiTuTestCase(TestCase):
    '''
	巡检 No.28
	用例名: 广场室内地图
	广场详情页点击室内地图，正常进入室内地图模块
    '''
    @classmethod
    def setUpClass(cls):
        '''
        初始化Appium driver
        '''
        cls.driver = AppiumDriver(appPackage_ffan,
                                   appActivity_ffan,
                                   platformName_andr,
                                   DeviceInfoUtil().getBuildVersion(),
                                   deviceName_andr,
                                   driver_url).getDriver()
        logger.info("Appium client init completed")

    def tearDown(self):
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        TestPrepare(self, self.driver, self.logger).prepare(False)

    def testGuangChangShiNeiDiTu(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        squarePage = SquareModulePage(self, self.driver, self.logger)
        locationBluetoothPage = LocationBluetoothPage(self, self.driver, self.logger)
        indoormapPage = SquareIndoorMapPage(self, self.driver, self.logger)
        searchPage = SearchPage(self, self.driver, self.logger)

        # Load square page
        dashboardPage.validSelf()
        dashboardPage.screenShot("aiGuangJie")
        dashboardPage.clickOnSearchView()
        searchPage.validSelf()
        searchPage.screenShot("souSuo")
        searchPage.inputText("北京通州万达广场")
        searchPage.screenShot("souSuo")
        searchPage.clickOnSearch()
        searchPage.waitBySeconds(10)
        searchPage.screenShot("souSuoJieGuo")
        searchPage.clickOnSearchResultFirstItem()
        squarePage.waitBySeconds(10)
        squarePage.validSelf()
        squarePage.screenShot("guangChang")
        squarePage.waitBySeconds(5)

        # Click "室内地图", cancle bluetooth setting, load "室内地图" page.
        squarePage.clicOnIndoorMap();
        locationBluetoothPage.clickOnCancleBtn()
        indoormapPage.validSelf();
        indoormapPage.screenShot("shiNeiDiTu")
        '''indoormapPage.clickOnFoodMap();
        indoormapPage.validSelfFood();'''

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(GuangChangShiNeiDiTuTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)