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


class YaoYiYao(TestCase):
    '''
    作者 刘涛
    摇一摇
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

        self.reset = ClearAppData(self.driver)
        self.reset.clearData()

        testPrepare = TestPrepare(testcase=self, driver=self.driver, logger=self.logger)
        testPrepare.prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(testcase=self, driver=self.driver, logger=self.logger)
        yaoyiyaoPage = YaoyiyaoPage(testcase=self, driver=self.driver, logger=self.logger)


        # 点击摇一摇
        dashboardPage.clickOnYaoyiyao()
        dashboardPage.waitBySeconds(5)
        yaoyiyaoPage.validSelf()





if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(YaoYiYao)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)

