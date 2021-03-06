# -*- coding: utf-8 -*-

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
from com.qa.automation.appium.pages.ios.ffan.popup_page import ClickActivityKeywordsType
from com.qa.automation.appium.pages.ios.ffan.popup_page import PopupPage
from com.qa.automation.appium.pages.ios.ffan.popup_page import VerifyActivityKeywordsType
from com.qa.automation.appium.pages.ios.ffan.square_sign_on_page import SignOnPage
from com.qa.automation.appium.utility.logger import Logger


class SquareSignOnCases(TestCase):
    '''
    作者 宋波
    巡检checklist #29
    自动化测试 #29
    广场详情页点击签到可以正常签到
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
        TestPrepare(self, self.driver, self.logger).prepare()

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnSignOn()

        signOnPage = SignOnPage(self, self.driver, self.logger)
        signOnPage.validSelf()

        if not signOnPage.validChickedInStatus(False):
            signOnPage.clickOnSignIn()

            popupPage = PopupPage(self, self.driver, self.logger)
            if popupPage.validSelf("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIAStaticText[61]",
                                   VerifyActivityKeywordsType.XPATH, False):
                popupPage.clickOnButton("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIAImage[13]",
                                        ClickActivityKeywordsType.XPATH)

        signOnPage.validChickedInStatus()
        signOnPage.clickBackKey()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(SquareSignOnCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'food-test_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='food-test',
                                           description='Result for test')
    runner.run(suite)
