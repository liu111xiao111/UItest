# -*- coding: utf-8 -*-

from unittest import TestCase
from configs.iosDriverConfig import IosDriverConfigs as IDC
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from cases.ios.bp.common.prepare import Prepare
from pages.ios.shanghu.homePage import HomePage
from pages.ios.shanghu.roleManagementPage import RoleManagementPage
from cases.logger import logger


class XinZengJueSe(TestCase):
    '''
    角色列表检查
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
        self.logger = Logger()
        prepare = Prepare(self, self.driver, self.logger)
        prepare.login()


    def test_case(self):
        homePage = HomePage(self, self.driver, self.logger)
        roleManagementPage = RoleManagementPage(self, self.driver, self.logger)

        homePage.validSelf()

        homePage.clickOnRoleManagement()

        roleManagementPage.validSelf()

        #点击新增角色按钮
        roleManagementPage.clickOnNewRoleButton()

        #进入新增角色页面,验证
        roleManagementPage.validNewRolePage()

        roleManagementPage.createNewRole()



    def tearDown(self):
        self.driver.quit()