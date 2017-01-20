# -*- coding: utf-8 -*-

import os
import time
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from cases.ios.ffan.common.clearAppData import ClearAppData
from cases.ios.ffan.common.testPrepare import TestPrepare
from configs.iosDriverConfig import IosDriverConfigs as IDC
from driver.appium_driver import AppiumDriver
from pages.ios.ffan.dashboard_page import DashboardPage
from pages.ios.ffan.feifan_card_page import FeiFanCardPage
from cases.logger import logger

class FeiFanTongQitaRukouTestCase(TestCase):
    '''
    飞凡通其它入口
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
        self.logger = logger()

        self.reset = ClearAppData(self.driver)
        self.reset.clearData()
        TestPrepare(self, self.driver, self.logger).prepare()

    def test_case(self):
        dashboardPage = DashboardPage(self , self.driver , self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnFeiFanCard()

        feifanCardPage = FeiFanCardPage(self , self.driver , self.logger)
        feifanCardPage.validSelf()

        otherEntranceName = (u"零花钱充值", u"零花钱提现", u"积分", u"市民/公交卡",
                                u"快易花", u"快利来", u"预约理财",u"意外险")
        otherEntrancePageName = (u"零花钱现金充值", u"零花钱现金提现", u"我的飞凡积分", u"市民/公交卡", u"飞凡贷",
                             u"快易花", u"快利来", u"预约理财")
        count = 0;
        for tempNum in range(8):
            feifanCardPage.validFeiFanTongOtherEntrance(otherEntrancePageName[count], otherEntranceName[count])
            count = count + 1

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(FeiFanTongQitaRukouTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'food-test', 'Result for test')
    runner.run(suite)
