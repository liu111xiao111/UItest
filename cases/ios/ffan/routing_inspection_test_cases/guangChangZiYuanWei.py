# -*- coding:utf-8 -*-

import os
import time
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from cases.ios.ffan.common.clearAppData import ClearAppData
from cases.ios.ffan.common.testPrepare import TestPrepare
from configs.iosDriverConfig import IosDriverConfigs as IDC
from driver.appium_driver import AppiumDriver
from pages.ios.ffan.dashboard_page import DashboardPage
from pages.ios.ffan.resource_niche_details_page import ResourceNicheDetailsPage
from pages.ios.ffan.square_module_page import SquareModulePage
from utility.logger import Logger


class GuangChangZiYuanWei(TestCase):
    '''
    作者 宋波
    巡检checklist #20
    自动化测试 #20
    广场详情页查看资源位，点击资源位可进入详情页
    '''

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(None, None, IDC.platformName, IDC.platformVersion,
                                   IDC.deviceName, IDC.driverUrl, IDC.bundleId, IDC.udid).getDriver()
        self.reset = ClearAppData(self.driver)
        self.reset.clearData()
        TestPrepare(self, self.driver, self.logger).prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnSquareModule()

        squareModulePage = SquareModulePage(self, self.driver, self.logger)
        squareModulePage.validSelf()
        squareModulePage.screen_shot("square_resource_niche_square")
        squareModulePage.clickOnResourceNiche()

        resourceNicheDetailsPage = ResourceNicheDetailsPage(self, self.driver, self.logger)
        resourceNicheDetailsPage.validSelf()
        resourceNicheDetailsPage.screen_shot("square_resource_niche")
        resourceNicheDetailsPage.waitBySeconds()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(GuangChangZiYuanWei)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
