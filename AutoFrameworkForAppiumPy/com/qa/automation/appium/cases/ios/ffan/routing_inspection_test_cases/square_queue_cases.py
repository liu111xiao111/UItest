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
from com.qa.automation.appium.pages.ios.ffan.square_module_page import SquareModulePage
from com.qa.automation.appium.pages.ios.ffan.square_queue_page import SquareQueuePage
from com.qa.automation.appium.utility.logger import Logger


class SquareLefuPayCases(TestCase):
    '''
    作者 刘涛
    巡检checklist: No.24
    自动化测试: No.24
    广场详情页点击排队取号进入排队取号页面，可以成功排队
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
        squarePage = SquareModulePage(self, self.driver, self.logger)
        queuePage = SquareQueuePage(self, self.driver, self.logger)

        # 首页进入广场页
        dashboardPage.validSelf();
        dashboardPage.clickOnSquareModule()
        squarePage.validSelf();

        # 点击 "排队取号"
        squarePage.clicOnQueue();
        queuePage.validSelf();

        # 点击 "取号"
        queuePage.clicOnQueueNumber()
        queuePage.waitBySeconds(10)
        queuePage.inputNumberOfMeals()
        queuePage.waitBySeconds(5)
        queuePage.clicOnGetQueueNumber()
        queuePage.validQueueSuccess()
        queuePage.clickOnCancelQueue()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(SquareLefuPayCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)
