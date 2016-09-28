# -*- coding: utf-8 -*-

import os
import time
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url
from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage
# from com.qa.automation.appium.pages.android.ffan.popup_page import ClickActivityKeywordsType
# from com.qa.automation.appium.pages.android.ffan.popup_page import PopupPage
# from com.qa.automation.appium.pages.android.ffan.popup_page import VerifyActivityKeywordsType
from com.qa.automation.appium.pages.android.ffan.square_sign_on_page import SignOnPage
from com.qa.automation.appium.utility.device_info_util import DeviceInfoUtil
from com.qa.automation.appium.utility.logger import Logger


class SquareSignOnCases(TestCase):
    '''
        usage:　 No.29 广场详情页点击签到可以正常签到
    '''

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(appPackage_ffan,
                                   appActivity_ffan,
                                   platformName_andr,
                                   DeviceInfoUtil().getBuildVersion(),
                                   deviceName_andr,
                                   driver_url).getDriver()

        self.reset = ClearAppData(self.driver)
        self.reset.clearData()

        TestPrepare(self, self.driver, self.logger).prepare()

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.waitBySeconds(10)
        dashboardPage.clickOnSignOn()

        signOnPage = SignOnPage(self, self.driver, self.logger)
        signOnPage.waitBySeconds(10)
        signOnPage.validSelf()

        if not signOnPage.validChickedInStatus(False):
            signOnPage.clickOnSignIn()

            signOnPage.clickBackKey()

            dashboardPage.clickOnSignOn()

            signOnPage.waitBySeconds(10)
            signOnPage.validChickedInStatus()
            signOnPage.clickBackKey()
        else:
            signOnPage.clickBackKey()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(SquareSignOnCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'food-test_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='food-test',
                                           description='Result for test')
    runner.run(suite)
