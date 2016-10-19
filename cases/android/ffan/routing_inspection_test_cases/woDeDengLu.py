# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.my_ffan_page import MyFfanPage
from pages.android.ffan.my_fei_fan_page import MyFeiFanPage
from configs.driver_configs import platformName_andr
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil
from pages.android.ffan.login_page import LoginPage
from pages.android.ffan.login_verify_page import LoginVerifyPage
from cases.android.ffan.common.test_prepare import TestPrepare
from cases.android.ffan.common.clear_app_data import ClearAppData
from pages.android.ffan.settings_page import SettingsPage


class WoDeDengLuTestCase(TestCase):
    '''
    巡检 No.49
    用例名 我的登录
    启动app，能够正常登陆
    '''
    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(appPackage_ffan,
                                   appActivity_ffan,
                                   platformName_andr,
                                   DeviceInfoUtil().getBuildVersion(),
                                   deviceName_andr,
                                   driver_url).getDriver()

        self.reset = ClearAppData(self.driver)
        self.reset.clearData()

        TestPrepare(self, self.driver, self.logger).prepare(False)

    def testWoDeDengLu(self):
        dashboardPage = DashboardPage(self , self.driver , self.logger)
        myFfanPage = MyFfanPage(self, self.driver, self.logger)

        dashboardPage.clickOnMy()
        if myFfanPage.isLoginStatus():
            myFeiFanPage = MyFeiFanPage(self, self.driver, self.logger)
            myFeiFanPage.clickOnSettings()

            settingPage = SettingsPage(testcase=self, driver=self.driver, logger=self.logger)
            dashboardPage.waitBySeconds()
            settingPage.validSelf()
            settingPage.clickOnQuitAccountBtn()

            myFeiFanPage.waitBySeconds()
            myFeiFanPage.validLogoutStatus()
        myFfanPage.clickOnLogin()
        loginPage = LoginPage(self, self.driver, self.logger)
        loginPage.validSelf()
        loginPage.switchToNormalLogin()
        loginPage.inputUserName()
        loginPage.inputPassWord()
        loginPage.clickOnLoginBtn()
        # loginVerifyPage = LoginVerifyPage(self, self.driver, self.logger)
        # loginVerifyPage.validSelf()
        # loginVerifyPage.clickOnSkip()
        myFfanPage.validSelf()
        dashboardPage.waitBySeconds(seconds=2)


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(WoDeDengLuTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)