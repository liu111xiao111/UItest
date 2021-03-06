# -*- coding:utf-8 -*-

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
from pages.ios.ffan.fei_fan_membership_page import FeiFanMembershipPage
from pages.ios.ffan.my_fei_fan_page import MyFeiFanPage
from pages.ios.ffan.my_membership_card_package_page import MyMembershipCardPackagePage
from cases.logger import logger

class WoDeHuiYuanKaBaoTestCase(TestCase):
    '''
    作者 宋波
    巡检checklist #52
    自动化测试 #52
    点击进入我的会员卡包，查看数据是否显示正常并可进入会员页
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

        TestPrepare(self, self.driver, self.logger).prepare()

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnMy()

        myFeiFanPage = MyFeiFanPage(self, self.driver, self.logger)
        myFeiFanPage.validSelf()
        #点击会员卡包
        myFeiFanPage.clickOnMembershipCardPackage()

        myMembershipCardPackagePage = MyMembershipCardPackagePage(self, self.driver, self.logger)
        myMembershipCardPackagePage.validSelf()
        #点击进入飞凡会员
        myMembershipCardPackagePage.clickOnLeHuoKa()

        feiFanMembershipPage = FeiFanMembershipPage(self, self.driver, self.logger)
        #验证会员卡包
        feiFanMembershipPage.validSelf()
        feiFanMembershipPage.waitBySeconds(10)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(WoDeHuiYuanKaBaoTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
