# -*- coding: utf-8 -*-

import os
import time
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from cases.ios.ffan.common.testPrepare import TestPrepare
from configs.iosDriverConfig import IosDriverConfigs as IDC
from driver.appium_driver import AppiumDriver
from pages.ios.ffan.dashboard_page import DashboardPage
from pages.ios.ffan.search_page import SearchPage
from cases.logger import logger
from pages.ios.ffan.search_page_configs import SearchPageConfigs


class QuanChengSouSuoPinPaiTestCase(TestCase):
    '''
    作者 宋波
    巡检checklist #3
    自动化测试 #3-1
    全城搜索品牌
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
        logger.info("Clear data completed")
        TestPrepare(self, self.driver, self.logger).prepare(False)


    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnSearchAll()

        searchPage = SearchPage(self, self.driver, self.logger)
        searchPage.validSelf()
        #输入品牌名
        searchPage.inputBrandName()
        #点击搜索出来的结果
        searchPage.clickPullDownListOfSearching()
        #验证adidas
        searchPage.validSearchResult(SearchPageConfigs.text_searching_brand_name,
                                     SearchPageConfigs.xpath_brand_name)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(QuanChengSouSuoPinPaiTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='food-test',
                                           description='Result for test')
    runner.run(suite)
