# -*- coding:utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from cases.android.ffan.common.test_prepare import TestPrepare
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from configs.driver_configs import platformName_andr
from driver.appium_driver import AppiumDriver
from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.my_ffan_page import MyFfanPage
from pages.android.ffan.my_fei_fan_page import MyFeiFanPage
from pages.android.ffan.settings_page import SettingsPage
from pages.android.ffan.login_page import LoginPage
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil
from cases.logger import logger


class WoDeTuiChuTestCase(TestCase):
    '''
    回归用例： No.30
    用例名: 我的退出
    退出登录，正常退出APP 
    '''
    @classmethod
    def setUpClass(cls):
        '''
        初始化Appium driver
        '''
        cls.driver = AppiumDriver(appPackage_ffan,
                                   appActivity_ffan,
                                   platformName_andr,
                                   DeviceInfoUtil().getBuildVersion(),
                                   deviceName_andr,
                                   driver_url).getDriver()
        logger.info("Appium client init completed")

    def tearDown(self):
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        TestPrepare(self, self.driver, self.logger).prepare()

    def testWoDeTuiChu(self):
        # 验证首页
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.waitBySeconds()
        dashboardPage.validSelf()
        dashboardPage.screenShot("aiGuangJie")

        # 点击我的，退出App
        dashboardPage.clickOnMy()
        myFeiFanPage = MyFeiFanPage(self, self.driver, self.logger)
        myFeiFanPage.validSelf()
        myFeiFanPage.screenShot("woDe")
        if not myFeiFanPage.validLoginStatusForExit():
            myFfanPage = MyFfanPage(self, self.driver, self.logger)
            myFfanPage.clickOnLogin()
            loginPage = LoginPage(self, self.driver, self.logger)
            loginPage.validSelf()
            loginPage.screenShot("dengLu")
            loginPage.switchToNormalLogin()
            loginPage.validNormalLogin()
            loginPage.screenShot("puTongDengLu")
            loginPage.inputUserName()
            loginPage.screenShot("shuRuYongHuMing")
            loginPage.inputPassWord()
            loginPage.screenShot("shuRuMiMa")
            loginPage.clickOnLoginBtn()
            myFfanPage.validSelf()
            myFfanPage.screenShot("woDe")
        myFeiFanPage.clickOnSettings()
        settingPage = SettingsPage(testcase=self, driver=self.driver, logger=self.logger)
        settingPage.validSelf()
        settingPage.screenShot("sheZhi")
        settingPage.clickOnQuitAccountBtn()
        myFeiFanPage.validLogoutStatusForStability()
        myFeiFanPage.screenShot("woDe")


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(WoDeTuiChuTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title='Feifan_automation_test_report', description='Result for test')
    runner.run(suite)
