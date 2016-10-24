# -*- coding: utf-8 -*-

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
from pages.ios.ffan.popup_page import ClickActivityKeywordsType
from pages.ios.ffan.popup_page import PopupPage
from pages.ios.ffan.popup_page import VerifyActivityKeywordsType
from pages.ios.ffan.square_sign_on_page import SignOnPage
from utility.logger import Logger


class QianDaoTestCase(TestCase):
    '''
    签到
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
        dashboardPage.clickOnSignOn()

        signOnPage = SignOnPage(self, self.driver, self.logger)
        signOnPage.validSelf()

        if not signOnPage.validChickedInStatus(False):
            signOnPage.clickOnSignIn()

            # popupPage = PopupPage(self, self.driver, self.logger)
            # if popupPage.validSelf("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIAStaticText[61]",
            #                        VerifyActivityKeywordsType.XPATH, False):
            #     popupPage.clickOnButton("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIAImage[13]",
            #                             ClickActivityKeywordsType.XPATH)

        signOnPage.validChickedInStatus()
        signOnPage.clickBackKey()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(QianDaoTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'food-test_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='food-test',
                                           description='Result for test')
    runner.run(suite)
