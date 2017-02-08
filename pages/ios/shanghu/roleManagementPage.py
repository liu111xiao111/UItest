# -*- coding:utf-8 -*-

from pages.ios.common.superPage import SuperPage
from api.api import API
from pages.ios.shanghu.shanghuPageConfig import Xpath
from pages.ios.shanghu.shanghuPageConfig import Name
from pages.ios.shanghu.shanghuPageConfig import Text
from pages.logger import logger

class RoleManagementPage(SuperPage):


    def validSelf(self):
        '''
        验证角色列表页面
        :return:
        '''
        logger.info('Check 角色管理 begin')
        API().assertElementByName(self.testcase,
                                  self.driver,
                                  self.logger,
                                  Name.role_management)
        logger.info('Check 角色管理 end')


    def checkRoleList(self):
        '''
        检查角色列表是否为空
        :return:
        '''
        logger.info('Check 角色列表 begin')
        name = API().getTextByXpath(self.testcase, self.driver, self.logger, Xpath.role_management_name)
        creator = API().getTextByXpath(self.testcase, self.driver, self.logger, Xpath.role_management_creator)
        date = API().getTextByXpath(self.testcase, self.driver, self.logger, Xpath.role_management_date)
        logger.info("name, creator, date %s, %s, %s " % (name, date, creator))

        API().assertTrue(self.testcase, self.logger, not name is None)
        API().assertTrue(self.testcase, self.logger, not creator is None)
        API().assertTrue(self.testcase, self.logger, not date is None)
        logger.info('Check 角色列表 end')
        API().screenShot(self.driver,'roleList')


    def clickOnNewRoleButton(self):
        '''
        点击新建角色按钮
        :return:
        '''
        logger.info('Click 新增角色 begin')
        API().clickElementByXpath(self.testcase, self.driver, self.logger, Xpath.add_new_role_button)
        logger.info('Click 新增角色 end')

    def validNewRolePage(self):
        '''
        验证新增角色页面
        :return:
        '''
        logger.info('Check 新增角色 begin')
        API().assertElementByName(self.testcase,
                                  self.driver,
                                  self.logger,
                                  Name.new_role)
        logger.info('Check 新增角色 end')


    def createNewRole(self):
        '''
        新增加角色
        :return:
        '''
        logger.info('Begin 增加新角色')

        #输入名字,角色说明
        logger.info('Input 角色 begin')
        API().inputStringByXpath(self.testcase, self.driver, self.logger, Xpath.new_role_name,Text.new_role_name)
        logger.info('Input 角色 end')
        API().screenShot(self.driver,'roleName')
        #得到输入的名字

        logger.info('Input 说明 begin')
        name = API().getTextByXpath(self.testcase, self.driver, self.logger, Xpath.new_role_name)
        API().inputStringByXpath(self.testcase, self.driver, self.logger, Xpath.new_role_explanation, Text.new_role_explanation_context)
        logger.info('Input 说明 end')
        API().screenShot(self.driver,'explanation')

        #点击请选择
        API().clickElementByXpath(self.testcase, self.driver, self.logger, Xpath.new_role_select_permissions_button)
        # 选择第一个RadioButton
        API().clickElementByXpath(self.testcase, self.driver, self.logger, Xpath.new_role_permissions_first_item)
        # 点击保存
        API().clickElementByName(self.testcase, self.driver, self.logger,Name.save_button)

        #新建角色页面点击保存
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.save_button)
        #检查是否添加角色成功
        API().assertElementByName(self.testcase, self.driver, self.logger, name)
        logger.info('End 增加新角色')
        API().screenShot(self.driver,'createRoleSuccess')
        #删除角色, 下一次才可以创建这个角色
        API().clickElementByXpath(self.testcase, self.driver, self.logger, Xpath.delete_role)
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.confirm_button)


