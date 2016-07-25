# -*- coding:utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.cases.ios.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.cases.ios.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.configs.ios_driver_configs import IosDriverConfigs as IDC
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.ios.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.ios.ffan.feifan_card_page import FeiFanCardPage
from com.qa.automation.appium.pages.ios.ffan.feifan_card_integral_page import FeiFanCardIntegralPage
from com.qa.automation.appium.utility.logger import Logger


class FeiFanCardIntegralCases(TestCase):
    '''
    作者 刘涛
    巡检checklist #45
    自动化测试 #45
    首页-飞凡卡点击积分，确认显示积分主页页面
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
        testPrepare.prepare()

    def test_case(self):
        dashboardPage = DashboardPage(testcase=self,driver=self.driver,logger=self.logger)
        ffanCardPage = FeiFanCardPage(testcase=self, driver=self.driver, logger=self.logger)
        ffanCardIntegralPage = FeiFanCardIntegralPage(testcase=self, driver=self.driver, logger=self.logger)

        # 首页点击"飞凡卡"
        dashboardPage.validSelf();
        dashboardPage.click_ffan_card();
        ffanCardPage.validSelf();

        # 点击"积分"
        ffanCardPage.clickOnIntegral();
        ffanCardIntegralPage.validSelf();


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(FeiFanCardIntegralCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)