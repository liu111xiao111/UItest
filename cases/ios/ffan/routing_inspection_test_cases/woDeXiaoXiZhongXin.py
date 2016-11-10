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

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

    def setUp(self):
        self.logger = logger
        self.driver = AppiumDriver(None, None, IDC.platformName, IDC.platformVersion,
                                   IDC.deviceName, IDC.driverUrl, IDC.bundleId, IDC.udid).getDriver()
        logger.info("Appium client init completed")
        self.reset = ClearAppData(self.driver)
        self.reset.clearData()
        logger.info("Clear data completed")
        TestPrepare(self, self.driver, self.logger).prepare()

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnMy()

        myFeiFanPage = MyFeiFanPage(self, self.driver, self.logger)
        myFeiFanPage.validSelf()
        myFeiFanPage.clickOnMessageCentre()

        messageCentrePage = MessageCentrePage(self, self.driver, self.logger)
#         messageCentrePage.validSelf()
#         messageCentrePage.clickOnFeiFanActivity()
#
#         feiFanActivityPage = FeiFanActivityPage(self, self.driver, self.logger)
#         feiFanActivityPage.validSelf()
#         feiFanActivityPage.clickBackKey()
#
#         messageCentrePage.validSelf()
#         messageCentrePage.clickOnSquareDynamic()
#
#         squareDynamicPage = SquareDynamicPage(self, self.driver, self.logger)
#         squareDynamicPage.validSelf()
#         squareDynamicPage.clickBackKey()
#
#         messageCentrePage.validSelf()
#         messageCentrePage.clickOnBrandActivity()
#
#         brandActivityPage = BrandActivityPage(self, self.driver, self.logger)
#         brandActivityPage.validSelf()
#         brandActivityPage.clickBackKey()
#
#         messageCentrePage.validSelf()
#         messageCentrePage.clickOnStoreMessage()
#
#         storeMessagePage = StoreMessagePage(self, self.driver, self.logger)
#         storeMessagePage.validSelf()
#         storeMessagePage.clickBackKey()

        messageCentrePage.validSelf()
        messageCentrePage.clickOnSettings()

        messageSettingsPage = MessageSettingsPage(self, self.driver, self.logger)
        messageSettingsPage.validSelf()
        messageSettingsPage.clickOnActivityPush()
        messageSettingsPage.clickBackKey()

        messageCentrePage.validSelf()
        messageCentrePage.clickBackKey()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(WoDeXiaoXiZhongXinTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
