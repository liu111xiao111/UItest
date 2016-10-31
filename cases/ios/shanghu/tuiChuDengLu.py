# -*- coding: utf-8 -*-

from unittest import TestCase
from configs.iosDriverConfig import IosDriverConfigs as IDC
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from cases.ios.shanghu.common.prepare import Prepare
from pages.ios.shanghu.dengLuPage import DengLuPage
from pages.ios.shanghu.homePage import HomePage

class TuiChuDengLuCase(TestCase):
    '''
    退出登录验证
    '''

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(None, None, IDC.platformName, IDC.platformVersion,
                                   IDC.deviceName, IDC.driverUrl, IDC.bundleId, IDC.udid).getDriver()

        prepare = Prepare(self, self.driver, self.logger)
        prepare.login()

    def test_case(self):
        dengLuPage = DengLuPage(self, self.driver, self.logger)
        homePage = HomePage(self, self.driver, self.logger)

        dengLuPage.clickOnSettings()
        dengLuPage.clickOnLogout()

        dengLuPage.validPassWord()



    def tearDown(self):
        self.driver.quit()



