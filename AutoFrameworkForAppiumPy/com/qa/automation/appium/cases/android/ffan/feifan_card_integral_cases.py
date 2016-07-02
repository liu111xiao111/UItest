# -*- coding: utf-8 -*-

import sys, os

sys.path.append(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))))

from com.qa.automation.appium.pages.android.ffan.dashboard_page import *;
from com.qa.automation.appium.pages.android.ffan.feifan_card_page import *;
from com.qa.automation.appium.pages.android.ffan.feifan_card_integral_page import *;
from com.qa.automation.appium.configs.driver_configs import *;
from com.qa.automation.appium.driver.appium_driver import *;
from com.qa.automation.appium.utility.logger import Logger;

from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData

import unittest
import HTMLTestRunner


class FeiFanCardIntegralCases(unittest.TestCase):
    '''
    	巡检checklist #45
    	自动化测试 #45
    	首页-飞凡卡点击积分，确认显示积分主页页面
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

        # Login & update version
        testPrepare = TestPrepare(testcase=self, driver=self.driver, logger=self.logger)
        testPrepare.prepare()

    def test_case(self):
        dashboardPage = DashboardPage(testcase=self, driver=self.driver, logger=self.logger)
        ffanCardPage = FeiFanCardPage(testcase=self, driver=self.driver, logger=self.logger)
        ffanCardIntegralPage = FeiFanCardIntegralPage(testcase=self, driver=self.driver, logger=self.logger)

        # Click "飞凡卡", load Feifan card page.
        dashboardPage.validSelf();
        dashboardPage.clickOnFeiFanCard();
        ffanCardPage.validSelf();

        # Click "积分", load "积分主页"
        ffanCardPage.clickOnIntegral();
        ffanCardIntegralPage.validSelf();


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(FeiFanCardIntegralCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)