# -*- coding: utf-8 -*-

from unittest import TestCase
from configs.iosDriverConfig import IosDriverConfigs as IDC
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from cases.ios.shanghu.common.prepare import Prepare
from pages.ios.shanghu.homePage import HomePage
from pages.ios.shanghu.roleManagementPage import RoleManagementPage


class XinZengJueSe(TestCase):
    '''
    角色列表检查
    '''
    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(None, None, IDC.platformName, IDC.platformVersion,
                                   IDC.deviceName, IDC.driverUrl, IDC.bundleId_sh, IDC.udid).getDriver()

        prepare = Prepare(self, self.driver, self.logger)
        prepare.login()


    def test_case(self):
        homePage = HomePage(self, self.driver, self.logger)
        roleManagementPage = RoleManagementPage(self, self.driver, self.logger)

        homePage.clickOnRoleManagement()

        roleManagementPage.createNewRole()

        roleManagementPage.waitBySeconds(10)


    def tearDown(self):
        self.driver.quit()