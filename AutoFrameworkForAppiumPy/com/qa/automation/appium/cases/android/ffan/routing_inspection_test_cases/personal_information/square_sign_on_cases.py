# -*- coding: utf-8 -*-

from __init__ import *

import unittest

import HTMLTestRunner

from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare

from com.qa.automation.appium.pages.android.ffan.dashboard_page import *;
from com.qa.automation.appium.pages.android.ffan.square_module_page import *;
from com.qa.automation.appium.pages.android.ffan.square_sign_on_page import *;
from com.qa.automation.appium.pages.android.ffan.square_module_page import *;
from com.qa.automation.appium.pages.android.ffan.my_ffan_page import *;
from com.qa.automation.appium.configs.driver_configs import *;
from com.qa.automation.appium.driver.appium_driver import *;
from com.qa.automation.appium.utility.logger import Logger;




class SquareSignOnCases(unittest.TestCase):
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
        self.driver = AppiumDriver(app_package=appPackage_ffan, app_activity=appActivity_ffan,
                                   platform_name=platformName_andr, platform_version=platformVersion,
                                   device_name=deviceName_andr, driver_url=driver_url
                                   ).getDriver()
        # 登陆　升级
        testPrepare = TestPrepare(testcase=self, driver=self.driver, logger=self.logger)
        testPrepare.prepare()

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
    suite = unittest.TestLoader().loadTestsFromTestCase(SquareSignOnCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'food-test_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='food-test',
                                           description='Result for test')
    runner.run(suite)
