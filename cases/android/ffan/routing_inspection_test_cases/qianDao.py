# -*- coding: utf-8 -*-

import os
import time
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from cases.android.ffan.common.clear_app_data import ClearAppData
from cases.android.ffan.common.test_prepare import TestPrepare
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from configs.driver_configs import platformName_andr
from driver.appium_driver import AppiumDriver
from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.square_sign_on_page import SignOnPage
from utility.device_info_util import DeviceInfoUtil
from utility.logger import Logger

TESTCITY = u"沈阳市"
DESCITY = u"北京市"

class QianDaoTestCase(TestCase):
    '''
    巡检 No.10
    用例名: 签到
    点击签到可以正常签到
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

    def testQiandao(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        tempCityName = dashboardPage.getCityName()
        if tempCityName != TESTCITY:
            dashboardPage.clickOnSwithCith()
            dashboardPage.switchCity(TESTCITY)
        dashboardPage.waitBySeconds(2)
        dashboardPage.clickOnSignOn()

        signOnPage = SignOnPage(self, self.driver, self.logger)
        signOnPage.waitBySeconds(2)
        signOnPage.validSelf()

        if not signOnPage.validChickedInStatus(False):
            signOnPage.clickOnSignIn()

            signOnPage.clickBackKey()

            dashboardPage.clickOnSignOn()

            signOnPage.waitBySeconds(2)
            signOnPage.validChickedInStatus()
            signOnPage.clickBackKey()
        else:
            signOnPage.clickBackKey()
        dashboardPage.clickOnSwithCith()
        dashboardPage.switchCity(DESCITY)


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(QianDaoTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)
