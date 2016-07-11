# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.android.ffan.my_ffan_page import MyFfanPage
from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import platformVersion
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.utility.logger import Logger
from com.qa.automation.appium.pages.android.ffan.login_page import LoginPage
from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData


class LoginCases(TestCase):
    '''
        usage: 登陆case
    '''

    def tearDown(self):
        self.driver.quit()
        ClearAppData().clearData()

    def setUp(self):
        ClearAppData().clearData()
        
        self.logger = Logger()
        self.driver = AppiumDriver(appPackage_ffan,
                                   appActivity_ffan,
                                   platformName_andr,
                                   platformVersion,
                                   deviceName_andr,
                                   driver_url).getDriver()
        # 登陆　升级
        TestPrepare(self, self.driver, self.logger).prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(self , self.driver , self.logger)
        myFfanPage = MyFfanPage(self, self.driver, self.logger)
        
        dashboardPage.clickOnMy()
        myFfanPage.clickOnLogin()
        loginPage = LoginPage(self, self.driver, self.logger)
        loginPage.validSelf()
        #loginPage.waitBySeconds(seconds=2)
        loginPage.switchToNormalLogin()
        loginPage.inputUserName();
        #loginPage.waitBySeconds(seconds=1)
        loginPage.inputPassWord()
        #loginPage.waitBySeconds(seconds=1)
        loginPage.clickOnLoginBtn();
        #loginPage.waitBySeconds(seconds=3)
        #dashboardPage.validSelf()
        #dashboardPage.clickOnMy()
        myFfanPage.validSelf()
        #myFfanPage.validLoginStatus()
        dashboardPage.waitBySeconds(seconds=2);


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(LoginCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)