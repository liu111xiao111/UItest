# -*- coding: utf-8 -*-

class SquareShoppingPageConfigs():
    # 常量命名规则 resource_id指明资源类型是resource id;iv_center_tab view id name;iv指明view类型image view
    # 商品图片id
    resource_id_iv_find_iv = "com.wanda.app.wanhui:id/common_title_view_layout_title";

    # text指明类型为text label,后面是文字的拼音

    # Click button time out
    click_on_button_timeout = 10

    # Sub-commodity button
    resource_id_sub_commodity_button = "com.wanda.app.wanhui:id/tv_name"
    xpath_sub_commodity_button = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.wanda.sliding.SlidingLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.FrameLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]"

    def __init__(self):
        pass;
