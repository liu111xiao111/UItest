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
from com.qa.automation.appium.pages.ios.ffan.open_card_page import OpenCardPage
from com.qa.automation.appium.utility.logger import Logger


class FeiFanCardOpenCases(TestCase):
    '''
    作者 刘涛
    巡检checklist No.: 44
    自动化测试case No.: 44
    首页飞凡卡界面，点击开卡，验证飞凡标准卡及一卡通飞凡联名卡
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
        testPrepare.prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        feifanCardPage = FeiFanCardPage(self, self.driver, self.logger)
        openCardPage = OpenCardPage(self, self.driver, self.logger)

        # 首页点击"飞凡卡"
        dashboardPage.validSelf();
        dashboardPage.clickOnFeiFanCard();
        feifanCardPage.validSelf();

        # 点击"市民/公交卡"
        feifanCardPage.clickOnOpenCard()
        openCardPage.validSelf()

        openCardPage.validJointCard()
        openCardPage.validBusCard()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(FeiFanCardOpenCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='feifan-card-test',
                                           description='Result for test')
    runner.run(suite)
