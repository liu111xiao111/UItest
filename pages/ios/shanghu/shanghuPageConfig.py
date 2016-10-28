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



class Name:
    login = u"登录"
    settings = u"设置"
    logout = u"退出登录"
    test_store_name = u"QA线上测试购物类门店1(快易花专用)_10011651"
    clearUserName = u"清除文本"

    userName = u"商户下的员工"
    userIdentity = u"QA线上验证专用权限组"
    userStore = u"QA线上测试用普通商户"


class Text:
    phoneNumber = u"15624958068"
    password = u"wanda123"



