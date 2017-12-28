#!/usr/bin/env python
# -*- coding: utf-8 -*-


class LoginPageConfigs():
    # 普通登录手机号码输入框
    resource_id_user_name = "com.wanda.app.wanhui:id/edit_login_name";

    # 普通登录密码输入框
    resource_id_pass_word = "com.wanda.app.wanhui:id/widget_input";

    # 登录按钮
    resource_id_login_button = "com.wanda.app.wanhui:id/btn_login";

    # text指明类型为text label,后面是文字的拼音
    text_quick_login = "快捷登录";
    text_normal_login = u"密码登录";
    text_forget_password = "忘记密码?"

    # account_name = "13601138742"
    # account_passwd = "9875321mgw"

    # Assert view time out
    assert_view_timeout = 10

    # Verify view time out
    verify_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    # Input time out
    input_timeout = 10

    # Login title
    text_login = "登录"
    name_login_title_st = u"登录"
    name_forget_password = u"忘记密码？"

    # Mobile number
    xpath_mobile_number_tf = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIATextField[1]"
#    text_mobile_number = u"15840985905"
    text_mobile_number = u'18217310992'

    # Password
    xpath_password_tf = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIASecureTextField[1]"
#    text_password = "liutao-123qwe"
    text_password = u'aaaAAA111'
    # Login
    xpath_login_bt = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAButton[1]"

    def __init__(self):
        pass;
