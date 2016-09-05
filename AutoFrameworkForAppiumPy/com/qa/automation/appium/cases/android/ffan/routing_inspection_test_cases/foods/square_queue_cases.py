# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.pages.android.ffan.my_ffan_my_queue_page import MyFfanMyQueuePage
from com.qa.automation.appium.pages.android.ffan.square_module_page import SquareModulePage
from com.qa.automation.appium.pages.android.ffan.square_queue_page import SquareQueuePage
from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.android.ffan.my_ffan_page import MyFfanPage
from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.utility.logger import Logger;
from com.qa.automation.appium.utility.device_info_util import DeviceInfoUtil
from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData


class SquareQueueCases(TestCase):
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
        myQueuePage = MyFfanMyQueuePage(self, self.driver, self.logger)
        myFfanPage = MyFfanPage(self, self.driver, self.logger)
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        squarePage = SquareModulePage(self, self.driver, self.logger)
        queuePage = SquareQueuePage(self, self.driver, self.logger)

        # Load square page
        dashboardPage.validSelf();
        dashboardPage.clickOnSquareModule()
        squarePage.waitBySeconds(3)
        squarePage.validSelf();

        # Click "排队取号"， load "排队取号" page.
        squarePage.clicOnQueue();
        queuePage.validSelf();

        # Click "取号"
        if (queuePage.validGetQueue()):
            queuePage.clicOnQueueNumber()
            queuePage.waitBySeconds(10)
            queuePage.inputNumberOfMeals()
            queuePage.clicOnGetQueueNumber()
            queuePage.validQueueSuccess()

            for _ in range(3):
                queuePage.clickBackKey()

            dashboardPage.clickOnMy()
            myFfanPage.validSelf()
            myFfanPage.clickOnMyQueue()
            myQueuePage.validSelf()
            myQueuePage.clickOnCancelQueue()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(SquareQueueCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)
