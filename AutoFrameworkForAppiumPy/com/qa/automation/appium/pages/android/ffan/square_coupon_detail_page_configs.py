# -*- coding: utf-8 -*-

import os, sys


class SquareCouponDetailPageConfigs():
    # 常量命名规则 resource_id指明资源类型是resource id;iv_center_tab view id name;iv指明view类型image view



    # xpath
    xpath_free_take = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.wanda.sliding.SlidingLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[2]"

    content_desc_free_take = "免费领取 Link"

    # text指明类型为text label,后面是文字的拼音

    text_coupon_detail = u"券详情"

    def __init__(self):
        pass;
