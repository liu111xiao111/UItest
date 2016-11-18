# -*- coding:utf-8 -*-

from pages.ios.common.superPage import SuperPage
from api.api import API
from pages.ios.shanghu.shanghuPageConfig import Xpath
from pages.ios.shanghu.shanghuPageConfig import Name
from pages.ios.shanghu.shanghuPageConfig import Text
from pages.logger import logger

class EmployeeModulePage(SuperPage):


    def checkEmployeeList(self):
        '''
        检查员工列表,员工姓名,手机号等是否为空
        :return:
        '''
        logger.info('Check 工列表,员工姓名,手机号 begin')
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
        logger.info('Check 工列表,员工姓名,手机号 end')
        API().screenShot(self.driver, 'employeeList')

    def clickAddEmployeeButton(self):
        '''
        点击新增员工按钮
        :return:
        '''
        logger.info('Click ' + Name.add_new_employee + ' begin')
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.add_new_employee)
        logger.info('Click ' + Name.add_new_employee + ' end')
        API().screenShot(self.driver, 'addEmployee')

    def selectRole(self):
        '''
        新增员工,选择角色
        :return:
        '''
        logger.info('Select 角色 begin')
        API().clickElementByXpath(self.testcase, self.driver, self.logger, Xpath.new_employee_please_selected_role)
        #选择店长角色
        API().clickElementByXpath(self.testcase, self.driver, self.logger, Xpath.new_employee_select_role_radio_button)
        API().screenShot(self.driver, 'selectStoreManagerRole')
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.save_button)
        logger.info('Select 角色 end')
        API().screenShot(self.driver, 'selectRole')

    def inputUserNameAndPassword(self):
        '''
        输入姓名和电话号
        :return:
        '''
        logger.info('Input 姓名,电话号 begin')
        API().inputStringByXpath(self.testcase, self.driver, self.logger, Xpath.new_employee_input_name, Text.new_employee_name)
        API().inputStringByXpath(self.testcase, self.driver, self.logger, Xpath.new_employee_input_phone_name,Text.new_employee_phone)
        logger.info('Input 姓名,电话号 end')
        API().screenShot(self.driver,'inputUser&password')
        logger.info('Click 保存 begin')
        #保存
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.save_button)
        logger.info('Click 保存 end')

    def checkNewUserStatus(self):
        '''
        检查是否添加新员工成功
        :return:
        '''
        logger.info('Check 添加新员工 begin')
        name = API().getTextByXpath(self.testcase, self.driver, self.logger, Xpath.employee_module_normal_name)

        API().assertTrue(self.testcase, self.logger, name==Text.new_employee_name)
        logger.info('Check 添加新员工 end')
        API().screenShot(self.driver,'checkUser')


    def editEmployee(self):
        logger.info('Edit 员工 begin')
        '''
        编辑员工
        :return:
        '''
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.edit_button)
        logger.info('Click 选择角色 begin')

        #点击选择角色按钮
        API().clickElementByXpath(self.testcase, self.driver, self.logger, Xpath.edit_employee_select_role)
        logger.info('Click 选择角色 end')
        API().screenShot(self.driver, 'clickSelectRole')

        logger.info('Click 商户店长 begin')
        #点击商户店长角色
        API().clickElementByXpath(self.testcase, self.driver, self.logger, Xpath.edit_employee_select_store_manager_radio_button)
        logger.info('Click 商户店长 end')

        logger.info('Click 保存 begin')
        #保存
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.save_button)
        logger.info('Click 保存 end')

        #输入姓名前按一次删除键
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  Xpath.edit_employee_name)
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.keyboard_delete)

        logger.info('Input ' + Text.edit_employee_name_text + ' begin')
        #输入姓名
        API().inputStringByXpath(self.testcase, self.driver, self.logger, Xpath.edit_employee_name,
                                  Text.edit_employee_name_text)
        API().screenShot(self.driver, 'inputName')

        # 获取编辑员工页面中,姓名
        name = API().getTextByXpath(self.testcase, self.driver, self.logger, Xpath.edit_employee_name)
        logger.info('Click 保存 begin')
        #点击保存
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.save_button)
        logger.info('Click 保存 end')
        API().screenShot(self.driver, 'save')
        logger.info('Click Dialog确定, begin')
        #点击弹出的Dialog的确定button
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.confirm_button)
        logger.info('Click Dialog确定, end')

        logger.info('Check ' + name + ' begin')
        API().assertElementByName(self.testcase, self.driver, self.logger, name)
        logger.info('Check ' + name + ' end')


        logger.info('Edit 员工 end')



    def dongjieEmployee(self):
        '''
        冻结员工
        :return:
        '''
        #取得被冻结员工名字
        name = API().getTextByXpath(self.testcase, self.driver, self.logger, Xpath.employee_module_normal_name)
        logger.info('Begin 冻结员工 ' + name)

        logger.info('Click 冻结 begin')
        #点击冻结Button
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.dongjie_button)
        logger.info('Click 冻结 end')
        API().screenShot(self.driver, 'blocked')
        logger.info('Click 确定 begin')
        #确定
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.confirm_button)
        logger.info('Click 确定 end')

        API().waitBySeconds(10)
        #点击冻结状态,查看是否冻结成功
        logger.info('Click 冻结状态 end')
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.dongjiezhuangtai)
        logger.info('Click 冻结状态 end')

        self.logger.info(name)
        logger.info('Check 冻结状态 begin')
        API().assertElementByName(self.testcase, self.driver, self.logger, name)
        logger.info('Check 冻结状态 end')
        API().screenShot(self.driver, 'checkBlocked')

        logger.info('Begin 冻结员工 ' + name)


    def jieDongEmployee(self):
        '''
        解冻员工
        :return:
        '''
        logger.info('Click 冻结状态 begin')
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.dongjiezhuangtai)
        logger.info('Click 冻结状态 end')
        API().screenShot(self.driver, 'blockedStatus')
        #检查是否存在冻结员工,如果不存在,冻结一个员工
        logger.info('Check 是否存在冻结员工 begin')
        isExist = API().validElementByName(self.driver, self.logger,
                                                  Name.jiedong_button)
        logger.info('Check 是否存在冻结员工 end')
        #logger.info('isExist' + isExist)

        if not isExist:
            logger.info('Check 冻结员工不存在,冻结一个员工 begin')
            API().clickElementByName(self.testcase, self.driver, self.logger, Name.zhengchangzhuangtai)
            self.dongjieEmployee()
            API().clickElementByName(self.testcase, self.driver, self.logger, Name.dongjiezhuangtai)
            logger.info('Check 冻结员工不存在,冻结一个员工 end')

        # 取得被冻结员工名字
        name = API().getTextByXpath(self.testcase, self.driver, self.logger, Xpath.dongjie_employee_name)

        #点击解冻
        logger.info('Click 解冻 begin')
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.jiedong_button)
        API().screenShot(self.driver, 'releaseEmployee')
        logger.info('Click 解冻 end')

        #点击确定
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.confirm_button)

        API().waitBySeconds(10)
        logger.info('Click  正常状态 begin')
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.zhengchangzhuangtai)
        logger.info('Click  正常状态 end')

        API().assertElementByName(self.testcase, self.driver, self.logger, name)
        API().screenShot(self.driver, 'checkRelease')


    def deleteEmployee(self):
        '''
        删除员工
        :return:
        '''
        #取得删除员工名字
        logger.info('Click 取得删除员工名字 begin')
        name = API().getTextByXpath(self.testcase, self.driver, self.logger, Xpath.dongjie_employee_name)
        logger.info('Click 取得删除员工名字 end')

        #删除员工
        logger.info('Click 删除 begin')
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.delete_button)
        API().screenShot(self.driver, 'delete')
        #点击确定
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.confirm_button)
        logger.info('Click 删除 begin')

        API().waitBySeconds(10)

        isExist = API().validElementByName(self.driver, self.logger,name)

        #如果不存在则删除成功
        logger.info('Check 删除 begin')
        API().assertFalse(self.testcase, self.logger, isExist)
        logger.info('Check 删除 begin')
        API().screenShot(self.driver, 'deleteStatus')