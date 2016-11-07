# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from cases.android.ffan.common.clear_app_data import ClearAppData
from cases.android.ffan.common.test_prepare import TestPrepare
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from configs.driver_configs import platformName_andr
from driver.appium_driver import AppiumDriver
from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.square_module_page import SquareModulePage
from pages.android.ffan.search_page import SearchPage
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil


class GuangChangXiangQingTestCase(TestCase):
    '''
    巡检 No.21
    用例名 广场详情
    首页进入广场详情页
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

    def testGuangChangXiangQing(self):
        '''dashboardPage = DashboardPage(self, self.driver, self.logger)
        squarePage = SquareModulePage(self, self.driver, self.logger)

        # 爱逛街首页在附近那点击任意广场，进入广场详情页，查看页面显示
        dashboardPage.validSelf()
        dashboardPage.clickOnSquareModule()
        squarePage.validSelfDetails()'''
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        searchPage = SearchPage(self, self.driver, self.logger)
        squareModulePage = SquareModulePage(self, self.driver, self.logger)

        dashboardPage.validSelf()
        dashboardPage.clickOnSearchView()
        searchPage.validSelf()
        searchPage.inputText("北京通州万达广场")
        searchPage.clickOnSearch()
        searchPage.clickOnSearchResultFirstItem()
        squareModulePage.validSelf()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(GuangChangXiangQingTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)