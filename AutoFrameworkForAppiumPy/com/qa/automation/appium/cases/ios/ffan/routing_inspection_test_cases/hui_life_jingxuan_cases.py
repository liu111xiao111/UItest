# -*- coding:utf-8 -*-

import os
import time
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from com.qa.automation.appium.cases.ios.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.ios.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.configs.ios_driver_configs import IosDriverConfigs as IDC
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.ios.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.ios.ffan.hui_life_page import HuiLifePage
from com.qa.automation.appium.utility.logger import Logger


class HuiLifeJingXuanCases(TestCase):
    '''
    慧生活精选/荐店
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

    def testHuiLifeScreenShot(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnHuiLife()

        huiLifePage = HuiLifePage(self, self.driver, self.logger)
        huiLifePage.validSelf()

        huiLifePage.clickOnJingxuan()
        huiLifePage.clickOnJiandian()





if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(HuiLifeJingXuanCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + '/' + 'Hui_life_resource_niche_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report', description='Result for test')
    runner.run(suite)