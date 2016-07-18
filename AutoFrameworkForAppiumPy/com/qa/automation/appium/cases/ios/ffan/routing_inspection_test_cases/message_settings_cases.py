# -*- coding:utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.cases.ios.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.ios.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.configs.ios_driver_configs import IosDriverConfigs as IDC
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.ios.ffan.brand_activity_page import BrandActivityPage
from com.qa.automation.appium.pages.ios.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.ios.ffan.fei_fan_activity_page import FeiFanActivityPage
from com.qa.automation.appium.pages.ios.ffan.message_centre_page import MessageCentrePage
from com.qa.automation.appium.pages.ios.ffan.message_settings_page import MessageSettingsPage
from com.qa.automation.appium.pages.ios.ffan.my_fei_fan_page import MyFeiFanPage
from com.qa.automation.appium.pages.ios.ffan.square_dynamic_page import SquareDynamicPage
from com.qa.automation.appium.pages.ios.ffan.store_message_page import StoreMessagePage
from com.qa.automation.appium.utility.logger import Logger

class MessageSettingsCases(TestCase):
    '''
    巡检checklist No.: 58
    自动化测试case No.: 58
    在我的飞凡页面点击进入消息中心，查看各类消息数据显示正确，并可以在设置中设置
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
        messageCentrePage.clickOnFeiFanActivity()

        feiFanActivityPage = FeiFanActivityPage(self, self.driver, self.logger)
        feiFanActivityPage.validSelf()
        feiFanActivityPage.clickBackKey()

        messageCentrePage.validSelf()
        messageCentrePage.clickOnSquareDynamic()

        squareDynamicPage = SquareDynamicPage(self, self.driver, self.logger)
        squareDynamicPage.validSelf()
        squareDynamicPage.clickBackKey()

        messageCentrePage.validSelf()
        messageCentrePage.clickOnBrandActivity()

        brandActivityPage = BrandActivityPage(self, self.driver, self.logger)
        brandActivityPage.validSelf()
        brandActivityPage.clickBackKey()

        messageCentrePage.validSelf()
        messageCentrePage.clickOnStoreMessage()

        storeMessagePage = StoreMessagePage(self, self.driver, self.logger)
        storeMessagePage.validSelf()
        storeMessagePage.clickBackKey()

        messageCentrePage.validSelf()
        messageCentrePage.clickOnSettings()

        messageSettingsPage = MessageSettingsPage(self, self.driver, self.logger)
        messageSettingsPage.validSelf()
        messageSettingsPage.clickOnActivityPush()
        messageSettingsPage.clickBackKey()

        messageCentrePage.validSelf()
        messageCentrePage.clickBackKey()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(MessageSettingsCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
