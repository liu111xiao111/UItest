# -*- coding:utf-8 -*-

import os
import time
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from cases.ios.ffan.common.testPrepare import TestPrepare
from configs.iosDriverConfig import IosDriverConfigs as IDC
from driver.appium_driver import AppiumDriver
from pages.ios.ffan.dashboard_page import DashboardPage
from pages.ios.ffan.my_fei_fan_page import MyFeiFanPage
from pages.ios.ffan.settings_page import SettingsPage
from cases.logger import logger


class WoDeTuiChuTestCase(TestCase):
    '''
    作者 宋波
    巡检checklist #59
    自动化测试 #59
    退出登录，正常退出APP
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
        dashboardPage.waitBySeconds()
        dashboardPage.validSelf()
        dashboardPage.clickOnMy()

        myFeiFanPage = MyFeiFanPage(self, self.driver, self.logger)
        myFeiFanPage.waitBySeconds()
        myFeiFanPage.validSelf()
        myFeiFanPage.validLoginStatus()
        myFeiFanPage.clickOnSettings()

        settingPage = SettingsPage(self, self.driver, self.logger)
        settingPage.waitBySeconds()
        settingPage.validSelf()
        settingPage.clickOnQuitAccountBtn()

        myFeiFanPage.waitBySeconds()
        myFeiFanPage.validLogoutStatus()

    def tearDown(self):
        pass
#    self.driver.quit()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(WoDeTuiChuTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
