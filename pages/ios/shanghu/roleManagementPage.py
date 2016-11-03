# -*- coding:utf-8 -*-

from pages.ios.common.superPage import SuperPage
from api.api import API
from pages.ios.shanghu.shanghuPageConfig import Xpath
from pages.ios.shanghu.shanghuPageConfig import Name
from pages.ios.shanghu.shanghuPageConfig import Text

class RoleManagementPage(SuperPage):

    def checkRoleList(self):
        '''
        检查角色列表是否为空
        :return:
        '''
        name = API().getTextByXpath(self.testcase, self.driver, self.logger, Xpath.role_management_name)
        creator = API().getTextByXpath(self.testcase, self.driver, self.logger, Xpath.role_management_creator)
        date = API().getTextByXpath(self.testcase, self.driver, self.logger, Xpath.role_management_date)

        API().assertTrue(self.testcase, self.logger, not name is None)
        API().assertTrue(self.testcase, self.logger, not creator is None)
        API().assertTrue(self.testcase, self.logger, not date is None)


    def createNewRole(self):
        '''
        新增加角色
        :return:
        '''
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.add_new_role_button)

        #输入名字,角色说明
        API().inputStringByXpath(self.testcase, self.driver, self.logger, Xpath.new_role_name,Text.new_role_name)
        API().inputStringByXpath(self.testcase, self.driver, self.logger, Xpath.new_role_explanation, Text.new_role_explanation_context)

        #点击请选择
        API().clickElementByXpath(self.testcase, self.driver, self.logger, Xpath.new_role_select_permissions_button)
        # 选择第一个RadioButton
        API().clickElementByXpath(self.testcase, self.driver, self.logger, Xpath.new_role_permissions_first_item)

