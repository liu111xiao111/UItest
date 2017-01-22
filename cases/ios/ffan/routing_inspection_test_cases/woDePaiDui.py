# -*- coding:utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from cases.ios.ffan.common.testPrepare import TestPrepare
from configs.iosDriverConfig import IosDriverConfigs as IDC
from driver.appium_driver import AppiumDriver
from pages.ios.ffan.dashboard_page import DashboardPage
from pages.ios.ffan.my_ffan_my_queue_page import MyFfanMyQueuePage
from pages.ios.ffan.my_ffan_page import MyFfanPage
from cases.logger import logger


class PaiDuiTestCase(TestCase):
    '''
    作者 刘涛
    巡检checklist: No.55
    自动化测试: No.55
    点击我的排队，成功进入并显示正确数据
    '''

    @classmethod
    def setUpClass(cls):
        '''
        初始化Appium driver
        '''

        cls.driver = AppiumDriver(None,
                                  None,
                                  IDC.platformName,
                                  IDC.platformVersion,
                                  IDC.deviceName,
                                  IDC.driverUrl,
                                  IDC.bundleId,
                                  IDC.udid).getDriver()
        logger.info("Appium client init completed")

    def setUp(self):
        self.logger = logger

        testPrepare = TestPrepare(testcase = self , driver = self.driver , logger = self.logger)
        testPrepare.prepare()

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        myFfanPage = MyFfanPage(self, self.driver, self.logger)
        myQueuePage = MyFfanMyQueuePage(self, self.driver, self.logger)

        # 点击 "我的排队"
        dashboardPage.validSelf()
        dashboardPage.clickOnMy()
        myFfanPage.validSelf()
        myFfanPage.clickOnMyQueue()
        myQueuePage.validSelf()

        myQueuePage.clickMoreRestaurant()


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    caseName = 'myfeifan_my_queue_cases'
    suite = TestLoader().loadTestsFromTestCase(PaiDuiTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, caseName + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=caseName,
                                           description='Result for test')
    runner.run(suite)