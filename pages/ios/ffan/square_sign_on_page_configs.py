# -*- coding: utf-8 -*-


class SignOnPageConfigs():
    # 常量命名规则 resource_id指明资源类型是resource id;iv_center_tab view id name;iv指明view类型image view


    # text指明类型为text label,后面是文字的拼音
    text_sign_on = u"签到";

    # Assert view time out
    assert_view_timeout = 10

    # Click button time out
    click_on_button_timeout = 10

    # Sign in
    xpath_sign_in_st = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIAStaticText[2]"

    # Daily see
    name_daily_see_st = u"天天见"

    # Checked in
    name_chicked_in_st = u"已签到"

    def __init__(self):
        pass;
