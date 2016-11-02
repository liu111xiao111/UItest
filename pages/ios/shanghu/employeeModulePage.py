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


    def editEmployee(self):
        '''
        编辑员工
        :return:
        '''
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.edit_button)
        #点击选择角色按钮
        API().clickElementByXpath(self.testcase, self.driver, self.logger, Xpath.edit_employee_select_role)
        #点击商户店长角色
        API().clickElementByXpath(self.testcase, self.driver, self.logger, Xpath.edit_employee_select_store_manager_radio_button)
        #保存
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.save_button)

        #输入姓名前按一次删除键
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  Xpath.edit_employee_name)
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.keyboard_delete)

        #输入姓名
        API().inputStringByXpath(self.testcase, self.driver, self.logger, Xpath.edit_employee_name,
                                  Text.edit_employee_name_text)

        # 获取编辑员工页面中,姓名
        name = API().getTextByXpath(self.testcase, self.driver, self.logger, Xpath.edit_employee_name)

        #点击保存
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.save_button)
        #点击弹出的Dialog的确定button
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.confirm_button)

        self.logger.i(name)
        API().assertElementByName(self.testcase, self.driver, self.logger, name)



    def dongjieEmployee(self):
        '''
        冻结员工
        :return:
        '''
        #取得被冻结员工名字
        name = API().getTextByXpath(self.testcase, self.driver, self.logger, Xpath.employee_module_normal_name)

        #点击冻结Button
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.dongjie_button)
        #确定
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.confirm_button)

        API().waitBySeconds(10)
        #点击冻结状态,查看是否冻结成功
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.dongjiezhuangtai)

        self.logger.i(name)
        API().assertElementByName(self.testcase, self.driver, self.logger, name)


    def jieDongEmployee(self):
        '''
        解冻员工
        :return:
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger, Name.dongjiezhuangtai)

        #检查是否存在冻结员工,如果不存在,冻结一个员工
        isExist = API().validElementByName(self.driver, self.logger,
                                                  Name.jiedong_button)

        self.logger.i(isExist)

        if not isExist:
            API().clickElementByName(self.testcase, self.driver, self.logger, Name.zhengchangzhuangtai)
            self.dongjieEmployee()
            API().clickElementByName(self.testcase, self.driver, self.logger, Name.dongjiezhuangtai)

        # 取得被冻结员工名字
        name = API().getTextByXpath(self.testcase, self.driver, self.logger, Xpath.dongjie_employee_name)

        #点击解冻
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.jiedong_button)

        #点击确定
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.confirm_button)

        API().waitBySeconds(10)

        API().clickElementByName(self.testcase, self.driver, self.logger, Name.zhengchangzhuangtai)

        API().assertElementByName(self.testcase, self.driver, self.logger, name)











