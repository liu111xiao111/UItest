#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader


from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare

from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url
from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.configs.driver_configs import platformVersion
from com.qa.automation.appium.driver.appium_driver import AppiumDriver

from com.qa.automation.appium.pages.android.ffan.resource_niche_details_page import ResourceNicheDetailsPage
from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.android.ffan.hui_life_page import HuiLifePage
from com.qa.automation.appium.utility.logger import Logger


class SpecialOfferCases(TestCase):
    '''
    巡检checklist No.: 39
    自动化测试case No.: 39
    首页-慧生活，查看资源位，点击资源位可以进入详情页
    '''
    def tearDown(self):
        self.driver.quit()
        ClearAppData().clearData()

    def setUp(self):
        ClearAppData().clearData()
        self.logger = Logger()
        self.driver = AppiumDriver(appPackage_ffan,
                                   appActivity_ffan,
                                   platformName_andr,
                                   platformVersion,
                                   deviceName_andr,
                                   driver_url).getDriver()

        TestPrepare(self, self.driver, self.logger).prepare()

    def test_case(self):
        resourceNicheDetailsPage = ResourceNicheDetailsPage(self, self.driver, self.logger)
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        huiLifePage = HuiLifePage(self, self.driver, self.logger)

        dashboardPage.validSelf()
        dashboardPage.clickOnSmartLife()

        huiLifePage.validSelf()
        huiLifePage.clickOnResourceNiche()

        resourceNicheDetailsPage.validSelf()
        resourceNicheDetailsPage.clickBackKey()

        huiLifePage.validSelf()

        huiLifePage.validModules()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(SpecialOfferCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
