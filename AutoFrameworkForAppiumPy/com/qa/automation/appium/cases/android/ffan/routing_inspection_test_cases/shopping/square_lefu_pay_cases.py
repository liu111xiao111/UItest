# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage;
from com.qa.automation.appium.pages.android.ffan.square_module_page import SquareModulePage
from com.qa.automation.appium.pages.android.ffan.lefu_pay_detail_page import LefuPayDetailPage
from com.qa.automation.appium.pages.android.ffan.square_lefu_pay_page import SquareLefuPayPage
from com.qa.automation.appium.pages.android.ffan.lefu_pay_way_page import LefuPayWayPage
from com.qa.automation.appium.pages.android.ffan.search_page import SearchPage
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url
from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.utility.logger import Logger
from com.qa.automation.appium.utility.device_info_util import DeviceInfoUtil


class SquareLefuPayCases(TestCase):
    '''
    巡检checklist #27
    自动化测试 #27
    广场详情页点击进入乐付买单
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

        TestPrepare(self, self.driver, self.logger).prepare()

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        squarePage = SquareModulePage(self, self.driver, self.logger)
        searchPage = SearchPage(self, self.driver, self.logger)
        lefuPayPage = SquareLefuPayPage(self, self.driver, self.logger)
        lefuPayDetailPage = LefuPayDetailPage(self, self.driver, self.logger)
        lefuPayWayPage = LefuPayWayPage(self, self.driver, self.logger)

        # 绑定北京通州万达广场
        dashboardPage.validSelf()
        dashboardPage.clickOnSearchView()
        searchPage.validSelf()
        searchPage.inputText("北京通州万达广场")
        searchPage.clickOnSearch()
        searchPage.waitBySeconds(5)
        searchPage.clickOnSearchResultFirstItem()
        squarePage.validSelf()
        squarePage.waitBySeconds(5)

        # Click "乐付买单"， load "乐付买单" page.
        squarePage.clicOnLefuPay()
        lefuPayPage.waitBySeconds(5)
        lefuPayPage.validSelf()
        lefuPayPage.waitBySeconds(2)
        # Click "乐付买单"， load detail pay page.
        lefuPayPage.clickOnLefuPay();
        lefuPayDetailPage.validSelf();

        # Input money, click "确认买单".
        lefuPayDetailPage.inputMoney();
        lefuPayDetailPage.waitBySeconds(seconds=5)
        lefuPayDetailPage.clickOnPay();
        lefuPayWayPage.validSelf();

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(SquareLefuPayCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)