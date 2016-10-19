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
from pages.ios.ffan.feifan_card_page import FeiFanCardPage
from pages.ios.ffan.open_card_page import OpenCardPage
from utility.logger import Logger


class FeiFanTongShiminGongjiaokaTestCase(TestCase):
    '''
    飞凡通市民公交卡
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
    suite = TestLoader().loadTestsFromTestCase(FeiFanTongShiminGongjiaokaTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='feifan-card-test',
                                           description='Result for test')
    runner.run(suite)
