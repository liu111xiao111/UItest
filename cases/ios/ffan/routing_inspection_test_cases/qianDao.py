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
from pages.ios.ffan.square_sign_on_page import SignOnPage
from cases.logger import logger

from pages.ios.ffan.switch_city_page import SwitchCityPage


class QianDaoTestCase(TestCase):
    '''
    签到
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
        self.reset.clearData()
        TestPrepare(self, self.driver, self.logger).prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        switchCityPage = SwitchCityPage(self, self.driver, self.logger)
        dashboardPage.validSelf()

        #签到,此版本只有沈阳城市可以签到,故先切换城市到沈阳,签到后,再切换城市回北京
        dashboardPage.clickOnCity()
        switchCityPage.inputShenyang()
        switchCityPage.clickOnCityListFirst()

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

        #签到结束后切换到北京
        dashboardPage.clickOnCity()
        switchCityPage.inputBeijing()
        switchCityPage.clickOnCityListFirst()

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(QianDaoTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'food-test_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='food-test',
                                           description='Result for test')
    runner.run(suite)
