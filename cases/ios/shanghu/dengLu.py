# -*- coding: utf-8 -*-

from unittest import TestCase
from configs.iosDriverConfig import IosDriverConfigs as IDC
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from pages.ios.shanghu.dengLuPage import DengLuPage
from pages.ios.shanghu.homePage import HomePage


class DenggLuCase(TestCase):
    '''
    登录验证
    '''

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(None, None, IDC.platformName, IDC.platformVersion,
                                   IDC.deviceName, IDC.driverUrl, IDC.bundleId, IDC.udid).getDriver()

    def test_case(self):
        dengLuPage = DengLuPage(self,self.driver,self.logger)
        homePage = HomePage(self,self.driver,self.logger)

        #检查是否登录,如果已经登录,点击退出登录
        loginStatus = dengLuPage.validLoginStatus()
        #self.logger.i(loginStatus)
        if not loginStatus:
            dengLuPage.clickOnSettings()
            dengLuPage.clickOnLogout()


        dengLuPage.validSelf()
        dengLuPage.inputUserName()
        dengLuPage.inputPassword()
        dengLuPage.clickOnLoginButton()

        dengLuPage.clickOnTestStoreItem()

        homePage.clickOnPersonalInfo()
        homePage.validPersonalInfo()


    def tearDown(self):
        self.driver.quit()





