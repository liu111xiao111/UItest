# -*- coding: utf-8 -*-

from unittest import TestCase
from configs.iosDriverConfig import IosDriverConfigs as IDC
from driver.appium_driver import AppiumDriver
from cases.logger import logger
from pages.ios.shanghu.dengLuPage import DengLuPage
from pages.ios.shanghu.homePage import HomePage
from pages.ios.shanghu.settingsPage import SettingsPage

class DenggLu(TestCase):
    '''
    登录验证
    '''

    @classmethod
    def setUpClass(cls):
        '''
        初始化Appium driver
        '''
        cls.driver = AppiumDriver(None,
                                  None,
                                  IDC.platformName,
                                  IDC.deviceName,
                                  IDC.driverUrl,
                                  IDC.bundleId_sh,
                                  IDC.udid).getDriver()
        logger.info("Appium client init completed")


    def setUp(self):
        self.logger = logger


    def test_case(self):
        dengLuPage = DengLuPage(self,self.driver,self.logger)
        homePage = HomePage(self,self.driver,self.logger)
        settingsPage = SettingsPage(self,self.driver,self.logger)

        #检查是否登录,如果已经登录,点击退出登录
        loginStatus = dengLuPage.validLoginStatus()
        if not loginStatus:
            dengLuPage.clickOnSettings()
            #验证设置页面
            settingsPage.validSelf()
            #点击退出登录
            dengLuPage.clickOnLogout()


        dengLuPage.validSelf()
        dengLuPage.inputUserName()
        dengLuPage.inputPassword()
        dengLuPage.clickOnLoginButton()

        dengLuPage.clickOnTestStoreItem()
        #验证进入首页
        homePage.validSelf()

        homePage.clickOnPersonalInfo()
        homePage.validPersonalInfo()


    def tearDown(self):
        self.driver.quit()





