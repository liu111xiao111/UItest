# -*- coding:utf-8 -*-


from pages.ios.common.superPage import SuperPage
from api.api import API
from pages.ios.shanghu.shanghuPageConfig import Xpath
from pages.ios.shanghu.shanghuPageConfig import Name
from pages.ios.shanghu.shanghuPageConfig import Text
from pages.logger import logger

class HomePage(SuperPage):


   def __init__(self, testcase, driver, logger):

        super(HomePage, self).__init__(testcase, driver, logger)


   def validSelf(self):
       '''
        验证主页
       '''
       logger.info('Check 主页 begin')
       API.assertElementByName(self.testcase,self.driver,self.logger, Name.test_store_name)
       logger.info('Check 主页 end')
       API().screenShot(self.driver, 'homePage')


   def clickOnPersonalInfo(self):
       '''
       点击右上角登录信息按钮
       :return:
       '''
       logger.info('Click 登录信息 begin')
       API().clickElementByXpath(self.testcase,self.driver,self.driver,Xpath.personalInfo)
       logger.info('Click 登录信息 end')
       API().screenShot(self.driver,'loginInfo')

   def validPersonalInfo(self):
        '''
        验证个人登录信息
        :return:
        '''
        logger.info('Check 登录信息 begin')
        API().assertElementByName(self.testcase, self.driver, self.logger, Name.userName)
        API().assertElementByName(self.testcase, self.driver, self.logger, Name.userIdentity)
        API().assertElementByName(self.testcase, self.driver, self.logger, Name.userStore)
        API().assertElementByName(self.testcase, self.driver, self.logger, Text.phoneNumber)
        logger.info('Check 登录信息 end')

        API().screenShot(self.driver, 'checkInfo')

   def clickOnEmployeeModule(self):
       '''
       点击员工管理模块
       :return:
       '''
       logger.info('Click 员工管理 begin')
       API().clickElementByName(self.testcase, self.driver, self.logger, Name.employeeManager, 30)
       logger.info('Click 员工管理 begin')
       API().screenShot(self.driver, 'employeeModule')

   def clickOnRoleManagement(self):
       '''
       点击角色管理
       :return:
       '''
       logger.info('Click 角色管理 begin')
       API().clickElementByName(self.testcase, self.driver, self.logger, Name.role_management)
       logger.info('Click 角色管理 end')
       API().screenShot(self.driver,'roleManagement')

   def clickOnOrderFormManagement(self):
       '''
       点击订单管理
       :return:
       '''
       logger.info('Click 订单管理 begin')
       API().clickElementByName(self.testcase, self.driver, self.logger, Name.order_form_management)
       logger.info('Click 订单管理 end')
       API().screenShot(self.driver,'orderManagement')

   def clickOnBusinessSchool(self):
       '''
       点击商学院
       '''
       logger.info('Click 商学院 begin')
       API().clickElementByName(self.testcase, self.driver, self.logger, Name.bussinessSchool)
       logger.info('Click 商学院 end')
       API().screenShot(self.driver,'bussinessSchool')
