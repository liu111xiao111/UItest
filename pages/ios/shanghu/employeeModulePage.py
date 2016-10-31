# -*- coding:utf-8 -*-

from pages.ios.common.superPage import SuperPage
from api.api import API
from pages.ios.shanghu.shanghuPageConfig import Xpath
from pages.ios.shanghu.shanghuPageConfig import Name
from pages.ios.shanghu.shanghuPageConfig import Text


class EmployeeModulePage(SuperPage):


    def checkEmployeeList(self):
        '''
        检查员工列表,员工姓名,手机号等是否为空
        :return:
        '''

        name = API().getTextByXpath(self.testcase, self.driver, self.logger, Xpath.employee_module_normal_name)
        sotreName = API().getTextByXpath(self.testcase, self.driver, self.logger, Xpath.employee_module_normal_store_name)
        role = API().getTextByXpath(self.testcase, self.driver, self.logger, Xpath.employee_module_normal_role)
        phone = API().getTextByXpath(self.testcase, self.driver, self.logger, Xpath.employee_module_normal_phone)
        chuangjianren = API().getTextByXpath(self.testcase, self.driver, self.logger, Xpath.employee_module_normal_chuangjianren)
        date = API().getTextByXpath(self.testcase, self.driver, self.logger, Xpath.employee_module_normal_date)

        API().assertTrue(self.testcase, self.logger, not name is None)
        API().assertTrue(self.testcase, self.logger, not sotreName is None)
        API().assertTrue(self.testcase, self.logger, not role is None)
        API().assertTrue(self.testcase, self.logger, not phone is None)
        API().assertTrue(self.testcase, self.logger, not chuangjianren is None)
        API().assertTrue(self.testcase, self.logger, not date is None)

    def clickAddEmployeeButton(self):
        '''
        点击新增员工按钮
        :return:
        '''
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.add_new_employee)

    def selectRole(self):
        '''
        新增员工,选择角色
        :return:
        '''
        API().clickElementByXpath(self.testcase, self.driver, self.logger, Xpath.new_employee_please_selected_role)
        #选择店长角色
        API().clickElementByXpath(self.testcase, self.driver, self.logger, Xpath.new_employee_select_role_radio_button)
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.save_button)

    def inputUserNameAndPassword(self):
        '''
        输入姓名和电话号
        :return:
        '''
        API().inputStringByXpath(self.testcase, self.driver, self.logger, Xpath.new_employee_input_name, Text.new_employee_name)
        API().inputStringByXpath(self.testcase, self.driver, self.logger, Xpath.new_employee_input_phone_name,Text.new_employee_phone)

        #保存
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.save_button)

    def checkNewUserStatus(self):
        '''
        检查是否添加新员工成功
        :return:
        '''
        name = API().getTextByXpath(self.testcase, self.driver, self.logger, Xpath.employee_module_normal_name)

        API().assertTrue(self.testcase, self.logger, name==Text.new_employee_name)

