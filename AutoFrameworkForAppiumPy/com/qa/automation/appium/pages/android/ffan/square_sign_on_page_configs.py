# -*- coding: utf-8 -*-


class SignOnPageConfigs():
    # 常量命名规则 resource_id指明资源类型是resource id;iv_center_tab view id name;iv指明view类型image view


    # text指明类型为text label,后面是文字的拼音
    content_desc_sign_on = u"签到";

    # Assert view time out
    assert_view_timeout = 10

    # Click button time out
    click_on_button_timeout = 10

    # Sign in button
    xpath_sign_in_button = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.wanda.sliding.SlidingLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[2]/android.view.View[2]"
    content_desc_sign_in_button = u"已签到"

    def __init__(self):
        pass;
