#!/usr/bin/env python
# -*- coding: utf-8 -*-


class StoreInfoPageConfigs():
    # 常量命名规则 resource_id指明资源类型是resource id;iv_center_tab view id name;iv指明view类型image view


    # text指明类型为text label,后面是文字的拼音

    text_store_detail = u"门店详情"
    text_store_info = u"门店信息";

    xpath_store_info = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.wanda.sliding.SlidingLayout[1]/android.widget.RelativeLayout[1]/android.view.View[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"

    # Click button time out
    click_on_button_timeout = 10

    # Assert view time out
    assert_view_timeout = 10

    # Store image text details button
    xpath_store_image_text_details_button = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.wanda.sliding.SlidingLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]"
#                                             "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.wanda.sliding.SlidingLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]"
    def __init__(self):
        pass;
