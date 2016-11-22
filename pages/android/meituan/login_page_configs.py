# -*- coding: utf-8 -*-


class LoginPageConfigs():
    # 普通登录手机号码输入框
    text_login = u"登录"

    resource_id_user_name = "com.sankuai.meituan:id/username";
    # 普通登录密码输入框
    resource_id_pass_word = "com.sankuai.meituan:id/password";

    # 登录按钮
    resource_id_login_button = "com.sankuai.meituan:id/login";

    # text指明类型为text label,后面是文字的拼音
    text_quick_login = "快捷登录";
    text_normal_login = u"普通登录";
    text_forget_password = "忘记密码?"

    account_name = "15642668143"
    account_passwd = "Neu1234!"

    assert_timeout = 90

    def __init__(self):
        pass;