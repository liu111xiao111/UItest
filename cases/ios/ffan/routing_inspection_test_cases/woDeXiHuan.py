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
from pages.ios.ffan.my_ffan_my_like_page import MyFfanMyLikePage
from pages.ios.ffan.my_ffan_page import MyFfanPage
from cases.logger import logger


class WoDeXiHuanTestCase(TestCase):
    '''
    作者 刘涛
    巡检checklist: No.54
    自动化测试: No.54
    查看我的喜欢信息及状态是否正确
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

        self.reset = ClearAppData(self.driver)
        self.reset.clearData()

        testPrepare = TestPrepare(testcase = self , driver = self.driver , logger = self.logger)
        testPrepare.prepare()

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        myFfanPage = MyFfanPage(self, self.driver, self.logger)
        myLikePage = MyFfanMyLikePage(self, self.driver, self.logger)

        # 我的点击 "我的喜欢"
        dashboardPage.validSelf()
        dashboardPage.clickOnMy()
        myFfanPage.validSelf()
        myFfanPage.clickOnMyLike()
        myLikePage.validSelf()
        myLikePage.waitBySeconds(3)
        myLikePage.clickOnLikeDissertation()
        myLikePage.validSelf()
        myLikePage.waitBySeconds(3)
        myLikePage.clickOnLikeBrand()
        myLikePage.validSelf()

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

if __name__ == "__main__":
    log = Logger()
    caseName = 'myfeifan_my_lick_cases'
    suite = TestLoader().loadTestsFromTestCase(WoDeXiHuanTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + caseName + now + '.html'
    log.d("report file name ==== %s", filename)
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=caseName,
                                           description='Result for test')
    runner.run(suite)