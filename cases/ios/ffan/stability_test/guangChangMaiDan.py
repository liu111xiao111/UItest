# -*- coding:utf-8 -*-

import os
import time
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from cases.ios.ffan.common.testPrepare import TestPrepare
from configs.iosDriverConfig import IosDriverConfigs as IDC
from driver.appium_driver import AppiumDriver
from pages.ios.ffan.dashboard_page import DashboardPage
from pages.ios.ffan.le_pay_page import LePayPage
from pages.ios.ffan.search_page import SearchPage
from pages.ios.ffan.square_module_page import SquareModulePage
from cases.logger import logger
from pages.ios.ffan.search_page_configs import SearchPageConfigs


class GuangChangMaiDanTestCase(TestCase):
    '''
    作者 刘涛
    巡检checklist #27
    自动化测试 #27
    广场详情页点击进入乐付买单
    '''

    @classmethod
    def setUpClass(cls):
        '''
        初始化Appium driver
        '''

        cls.driver = AppiumDriver(None,
                                  None,
                                  IDC.platformName,
                                  IDC.platformVersion,
                                  IDC.deviceName,
                                  IDC.driverUrl,
                                  IDC.bundleId,
                                  IDC.udid).getDriver()
        logger.info("Appium client init completed")

    def setUp(self):
        self.logger = logger

        testPrepare = TestPrepare(testcase=self , driver=self.driver , logger=self.logger)
        testPrepare.prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        searchPage = SearchPage(self, self.driver, self.logger)
        squareModulePage = SquareModulePage(self, self.driver, self.logger)
        lePayPage = LePayPage(self, self.driver, self.logger)

        # 首页选择北京通州万达广场
        dashboardPage.validSelf()
        dashboardPage.clickOnSearchAll()
        searchPage.validSelf()
        searchPage.inputKeywords(SearchPageConfigs.text_searching_store_name)
        searchPage.clickOnSearch()
        searchPage.clickOnSpecificSquare()
        squareModulePage.validSelf()

        # 点击 "乐付买单"
        squareModulePage.clicOnLefuPay()
        lePayPage.validSelf()
        lePayPage.clickOnDetailsLePay()
        #验证买单详情页面
        lePayPage.validMaiDanPage()
        #输入金额
        lePayPage.inputSumOfConsumption()
        #点击确认购买
        lePayPage.clickOnConfirmPurchase()
        #验证飞凡收银台
        lePayPage.validFeiFanShouYinTai()

        lePayPage.clickBackKey()
        #点击返回弹出对话框
        lePayPage.clickOnConfirmCancel()

        # 返回验证买单页面
        lePayPage.validMaiDanPage()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(GuangChangMaiDanTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)
