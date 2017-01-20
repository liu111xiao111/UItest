# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from cases.android.ffan.common.test_prepare import TestPrepare
from pages.android.ffan.dashboard_page import DashboardPage;
from pages.android.ffan.square_module_page import SquareModulePage
from pages.android.ffan.lefu_pay_detail_page import LefuPayDetailPage
from pages.android.ffan.square_lefu_pay_page import SquareLefuPayPage
from pages.android.ffan.lefu_pay_way_page import LefuPayWayPage
from pages.android.ffan.search_page import SearchPage
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from configs.driver_configs import platformName_andr
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil
from cases.logger import logger


class GuangChangMaiDanTestCase(TestCase):
    '''
    巡检checklist #27
    自动化测试 #27
    广场详情页点击进入乐付买单
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
        TestPrepare(self, self.driver, self.logger).prepare()

    def testGuangChangMaiDan(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        squarePage = SquareModulePage(self, self.driver, self.logger)
        searchPage = SearchPage(self, self.driver, self.logger)
        lefuPayPage = SquareLefuPayPage(self, self.driver, self.logger)
        lefuPayDetailPage = LefuPayDetailPage(self, self.driver, self.logger)
        lefuPayWayPage = LefuPayWayPage(self, self.driver, self.logger)

        # 绑定北京通州万达广场
        dashboardPage.validSelf()
        dashboardPage.screenShot("aiGuangJie")
        dashboardPage.clickOnSearchView()
        searchPage.validSelf()
        searchPage.screenShot("souSuo")
        searchPage.inputText("北京通州万达广场")
        searchPage.screenShot("souSuo")
        searchPage.clickOnSearch()
        searchPage.waitBySeconds(5)
        searchPage.screenShot("souSuoJieGuo")
        searchPage.clickOnSearchResultFirstItem()
        squarePage.validSelf()
        squarePage.waitBySeconds(5)
        squarePage.screenShot("guangChang")

        # Click "乐付买单"， load "乐付买单" page.
        squarePage.clicOnLefuPay()
        lefuPayPage.waitBySeconds(5)
        lefuPayPage.validSelf()
        lefuPayPage.waitBySeconds(5)
        lefuPayPage.screenShot("maiDan")
        # Click "乐付买单"， load detail pay page.
        lefuPayPage.clickOnLefuPay();
        lefuPayDetailPage.validSelf();
        lefuPayDetailPage.screenShot("maiDanXiangXi")

        # Input money, click "确认买单".
        lefuPayDetailPage.inputMoney();
        lefuPayDetailPage.waitBySeconds(seconds=10)
        lefuPayDetailPage.screenShot("maiDanXiangXi")
        lefuPayDetailPage.clickOnPay();
        lefuPayWayPage.validSelf();
        lefuPayWayPage.screenShot("maiDanFangShi")

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(GuangChangMaiDanTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)