# -*- coding:utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from cases.ios.ffan.common.testPrepare import TestPrepare
from cases.ios.ffan.common.clearAppData import ClearAppData
from configs.iosDriverConfig import IosDriverConfigs as IDC
from driver.appium_driver import AppiumDriver
from pages.ios.ffan.dashboard_page import DashboardPage
from pages.ios.ffan.my_ffan_my_queue_page import MyFfanMyQueuePage
from pages.ios.ffan.square_module_page import SquareModulePage
from pages.ios.ffan.square_queue_page import SquareQueuePage
from pages.ios.ffan.my_ffan_page import MyFfanPage
from utility.logger import Logger


class PaiDui(TestCase):
    '''
    作者 刘涛
    巡检checklist: No.55
    自动化测试: No.55
    点击我的排队，成功进入并显示正确数据
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
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        myFfanPage = MyFfanPage(self, self.driver, self.logger)
        myQueuePage = MyFfanMyQueuePage(self, self.driver, self.logger)
        queuePage = SquareQueuePage(self, self.driver, self.logger)
        squarePage = SquareModulePage(self, self.driver, self.logger)

        # # 首页进入广场页
        # dashboardPage.validSelf();
        # dashboardPage.clickOnSquareModule()
        # squarePage.validSelf();
        #
        # # 点击 "排队取号"
        # squarePage.clicOnQueue();
        # queuePage.validSelf();
        #
        # # 点击 "取号"
        # queuePage.waitBySeconds(10)
        # queuePage.clicOnQueueNumber()
        # queuePage.waitBySeconds(10)
        # queuePage.inputNumberOfMeals()
        # queuePage.waitBySeconds(5)
        # queuePage.clicOnGetQueueNumber()
        # queuePage.waitBySeconds(10)
        # queuePage.validQueueSuccess()
        # queuePage.waitBySeconds(10)
        # queuePage.clickOnCancelQueue()
        #
        # myFfanPage.clickBackKey()
        # myFfanPage.clickBackKey()
        # myFfanPage.clickBackKey()

        # 点击 "我的排队"
        dashboardPage.validSelf()
        dashboardPage.clickOnMy()
        myFfanPage.validSelf()
        myFfanPage.clickOnMyQueue()
        myQueuePage.validSelf()

        myQueuePage.clickMoreRestaurant()

        myQueuePage.waitBySeconds(9)


if __name__ == "__main__":
    caseName = 'myfeifan_my_queue_cases'
    suite = TestLoader().loadTestsFromTestCase(PaiDui)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, caseName + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=caseName,
                                           description='Result for test')
    runner.run(suite)