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
from pages.ios.ffan.message_centre_page import MessageCentrePage
from pages.ios.ffan.message_settings_page import MessageSettingsPage
from pages.ios.ffan.my_fei_fan_page import MyFeiFanPage
from cases.logger import logger


class WoDeXiaoXiZhongXinTestCase(TestCase):
    '''
    作者 宋波
    巡检checklist #58
    自动化测试 #58
    在我的飞凡页面点击进入消息中心，查看各类消息数据显示正确，并可以在设置中设置
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
        myFeiFanPage.clickOnMessageCentre()

        messageCentrePage = MessageCentrePage(self, self.driver, self.logger)

        messageCentrePage.validSelf()
        messageCentrePage.clickOnSettings()

        messageSettingsPage = MessageSettingsPage(self, self.driver, self.logger)
        messageSettingsPage.validSelf()
        messageSettingsPage.clickOnActivityPush()
        messageSettingsPage.clickBackKey()

        messageCentrePage.validSelf()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(WoDeXiaoXiZhongXinTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
