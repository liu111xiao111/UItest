# -*- coding:utf-8 -*-

class Xpath:
    # 用户名xpath
    username = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATextField[1]"
    # 密码xpath
    password = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIASecureTextField[1]"
    # 登录按钮xpath
    login = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAButton[2]"
    # 退出登录
    logout = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableGroup[2]/UIAButton[1]"
    #清除文本
    clearUserName = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATextField[1]/UIAButton[1]"
    #选择门店,确定按钮
    button_select_store_submit = "//UIAApplication[1]/UIAWindow[1]/UIAButton[1]"
    #首页,登录信息按钮
    personalInfo = "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[4]"

    #员工管理,正常状态,员工姓名
    employee_module_normal_name = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]"
    employee_module_normal_store_name = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[2]"
    employee_module_normal_role = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[4]"
    employee_module_normal_phone = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[8]"
    employee_module_normal_chuangjianren = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[6]"
    employee_module_normal_date = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[10]"

    #新增加员工,选择角色
    new_employee_please_selected_role = "//UIAApplication[1]/UIAWindow[1]/UIAButton[2]"
    #新增加员工,选择角色列表,最后一个
    new_employee_select_role_radio_button = " //UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[9]/UIAButton[1]"
    #新增加员工,输入姓名
    new_employee_input_name = "//UIAApplication[1]/UIAWindow[1]/UIATextField[2]"
    #新增加员工,输入电话号
    new_employee_input_phone_name = "//UIAApplication[1]/UIAWindow[1]/UIATextField[3]"





class Name:
    login = u"登录"
    settings = u"设置"
    logout = u"退出登录"
    test_store_name = u"QA线上测试购物类门店1(快易花专用)_10011651"
    clearUserName = u"清除文本"

    userName = u"商户下的员工"
    userIdentity = u"QA线上验证专用权限组"
    userStore = u"QA线上测试用普通商户"
    employeeManager = u"员工管理"

    add_new_employee = u"新增员工"


    save_button = u"保存"
    please_input_name = u"请输入姓名"

class Text:
    phoneNumber = u"15624958068"
    password = u"wanda123"
    #密码框初始文字
    initial_password = u"请输入密码(长度8-20位)"

    #默认密码
    default_password = u"Abc123456"
    #新增员工名字
    new_employee_name = u"王Test"
    new_employee_phone = "13504286090"




