# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader
from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.android.ffan.square_module_page import SquareModulePage
from com.qa.automation.appium.pages.android.ffan.square_sign_on_page import SignOnPage
from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import platformVersion
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.utility.logger import Logger


class SquareSignOnCases(TestCase):
    '''
        usage:　 No.29 广场详情页点击签到可以正常签到
    '''

    def tearDown(self):
        self.driver.quit()

        clearAppData = ClearAppData()
        clearAppData.clearData()

    def setUp(self):
        clearAppData = ClearAppData()
        clearAppData.clearData()

        self.logger = Logger()
        self.driver = AppiumDriver(appPackage_ffan,
                                   appActivity_ffan,
                                   platformName_andr,
                                   platformVersion,
                                   deviceName_andr,
                                   driver_url).getDriver()
        # 登陆　升级
        TestPrepare(self, self.driver, self.logger).prepare()

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger);
        dashboardPage.validSelf()
        dashboardPage.clickOnSquareModule()

        squareModulePage = SquareModulePage(self, self.driver, self.logger);
        squareModulePage.validSelf()
        squareModulePage.clickOnSignOn()

        signOnPage = SignOnPage(self, self.driver, self.logger);
        signOnPage.validSelf()
        if not signOnPage.validChickedInStatus(False):
            signOnPage.clickOnSignIn()
        signOnPage.validChickedInStatus()
        signOnPage.clickBackKey()

        squareModulePage.validSelf()
        squareModulePage.clickBackKey()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(SquareSignOnCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'food-test_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='food-test',
                                           description='Result for test')
    runner.run(suite)
