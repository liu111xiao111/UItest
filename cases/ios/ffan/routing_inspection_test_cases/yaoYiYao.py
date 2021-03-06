# -*- coding:utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader
from utility.logger import Logger
from driver.appium_driver import AppiumDriver
from cases.ios.ffan.common.clearAppData import ClearAppData
from pages.ios.ffan.dashboard_page import DashboardPage
from pages.ios.ffan.yaoyiyao_page import YaoyiyaoPage
from cases.ios.ffan.common.testPrepare import TestPrepare
from configs.iosDriverConfig import IosDriverConfigs as IDC
from cases.logger import logger

class YaoYiYaoTestCase(TestCase):
    '''
    作者 刘涛
    摇一摇
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

        self.reset = ClearAppData(self.driver)
       #self.reset.clearData()

        testPrepare = TestPrepare(testcase=self, driver=self.driver, logger=self.logger)
        testPrepare.prepare()

    def test_case(self):
        dashboardPage = DashboardPage(testcase=self, driver=self.driver, logger=self.logger)
        yaoyiyaoPage = YaoyiyaoPage(testcase=self, driver=self.driver, logger=self.logger)


        # 点击摇一摇
        dashboardPage.clickOnYaoyiyao()
        dashboardPage.waitBySeconds(5)
        yaoyiyaoPage.validSelf()

    def tearDown(self):
        # self.reset.clearData()
        self.driver.quit()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(YaoYiYaoTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)

