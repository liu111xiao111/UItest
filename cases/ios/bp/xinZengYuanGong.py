# -*- coding: utf-8 -*-

from unittest import TestCase
from configs.iosDriverConfig import IosDriverConfigs as IDC
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from cases.ios.bp.common.prepare import Prepare
from pages.ios.shanghu.homePage import HomePage
from pages.ios.shanghu.employeeModulePage import EmployeeModulePage
from cases.logger import logger

class XinZengYuanGongCase(TestCase):
    '''
    新增员工检查
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
        employeeModulePage = EmployeeModulePage(self, self.driver, self.logger)

        homePage.validSelf()

        homePage.clickOnEmployeeModule()

        employeeModulePage.validSelf()
        #点击新增员工
        employeeModulePage.clickAddEmployeeButton()

        #验证新增员工页面
        employeeModulePage.validNewEmployeePage()

        #选择角色
        employeeModulePage.selectRole()

        # 验证选择角色页面
        employeeModulePage.validSelectRolePage()

        # 点击保存
        employeeModulePage.clickOnSaveButton()


        #输入姓名电话号,保存
        employeeModulePage.inputUserNameAndPassword()

        #点击保存
        employeeModulePage.clickOnSaveButton()

        #检查是否添加员工成功
        employeeModulePage.checkNewUserStatus()

        #创建完成后,删除员工,以便下一次创建员工
        employeeModulePage.deleteEmployee()


    def tearDown(self):
        self.driver.quit()