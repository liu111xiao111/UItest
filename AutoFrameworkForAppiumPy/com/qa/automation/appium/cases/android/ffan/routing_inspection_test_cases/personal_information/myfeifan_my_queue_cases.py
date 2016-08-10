# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.android.ffan.my_ffan_page import MyFfanPage
from com.qa.automation.appium.pages.android.ffan.my_ffan_my_queue_page import MyFfanMyQueuePage
from com.qa.automation.appium.pages.android.ffan.square_queue_page import SquareQueuePage
from com.qa.automation.appium.pages.android.ffan.square_module_page import SquareModulePage
from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.utility.logger import Logger
from com.qa.automation.appium.utility.device_info_util import DeviceInfoUtil
from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData


class MyfeifanMyQueueCases(TestCase):
    '''
    巡检checklist: No.55
    自动化测试: No.55
    点击我的排队，成功进入并显示正确数据
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
        myFfanPage = MyFfanPage(self, self.driver, self.logger)
        myQueuePage = MyFfanMyQueuePage(self, self.driver, self.logger)
        queuePage = SquareQueuePage(self, self.driver, self.logger)
        squarePage = SquareModulePage(self, self.driver, self.logger)

        # Load square page
        dashboardPage.validSelf();
        dashboardPage.clickOnSquareModule()
        squarePage.validSelf();

        # Click "排队取号"， load "排队取号" page.
        squarePage.clicOnQueue();
        queuePage.validSelf();

        # Click "取号"
        queuePage.clicOnQueueNumber()
        queuePage.waitBySeconds(10)
        queuePage.inputNumberOfMeals()
        queuePage.waitBySeconds(10)
        queuePage.clicOnGetQueueNumber()
        queuePage.validQueueSuccess()
        queuePage.clickOnCancelQueue()

        myFfanPage.clickBackKey()
        myFfanPage.clickBackKey()
        myFfanPage.clickBackKey()

        # Click "我的排队"， load "我的排队" page.
        dashboardPage.validSelf()
        dashboardPage.clickOnMy()
        myFfanPage.validSelf()
        myFfanPage.clickOnMyQueue()
        myQueuePage.validSelf()


if __name__ == "__main__":
    log = Logger()
    caseName = 'myfeifan_my_queue_cases'
    suite = TestLoader().loadTestsFromTestCase(MyfeifanMyQueueCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + caseName + now + '.html'
    log.d("report file name ==== %s", filename)
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=caseName,
                                           description='Result for test')
    runner.run(suite)