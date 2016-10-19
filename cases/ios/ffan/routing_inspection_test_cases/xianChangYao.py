# -*- coding:utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from cases.ios.ffan.common.testPrepare import TestPrepare
from cases.ios.ffan.common.clearAppData import ClearAppData
from configs.iosDriverConfig import IosDriverConfigs as IDC
from driver.appium_driver import AppiumDriver
from pages.ios.ffan.dashboard_page import DashboardPage
from pages.ios.ffan.square_module_page import SquareModulePage
from pages.ios.ffan.xianchangyao_page import XianchangyaoPage
from utility.logger import Logger

class XianChangYao(TestCase):
    '''
    作者 刘涛
    广场现场摇
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

        testPrepare = TestPrepare(testcase = self , driver = self.driver , logger = self.logger)
        testPrepare.prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        squarePage = SquareModulePage(self, self.driver, self.logger)
        xianchangyao = XianchangyaoPage(self, self.driver, self.logger)

        # 首页进入广场页
        dashboardPage.validSelf()
        dashboardPage.clickOnSquareModule()
        squarePage.validSelf()
        squarePage.clickOnXianchangyao()
        xianchangyao.validSelf()
        xianchangyao.clickOnShakingImage()
        xianchangyao.waitBySeconds(10)
        xianchangyao.validShakingResult()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(XianChangYao)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'food-test_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='food-test',
                                           description='Result for test')
    runner.run(suite)




