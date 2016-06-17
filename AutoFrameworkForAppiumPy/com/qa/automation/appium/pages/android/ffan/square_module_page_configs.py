# -*- coding: utf-8 -*-

import os, sys


class SquareModulePageConfigs():
    
    
    # 常量命名规则 resource_id指明资源类型是resource id;iv_center_tab view id name;iv指明view类型image view
    
    # 搜索按钮
    resource_id_iv_search_iv = "com.wanda.app.wanhui:id/iv_search_entry"
    
    # xpath
    xpath_recommend_store = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.wanda.sliding.SlidingLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]"    
    # text指明类型为text label,后面是文字的拼音
    text_sign_on = u"签到";
    text_find_store = u"找店";
    text_parking = u"停车";
    text_member = u"会员";
    text_food = u"美食汇";
    text_shopping = u"爱购物";
    text_find_store = u"找店";
    text_indoor_map = u"室内地图";
    text_lefu_pay = u"乐付买单";
    text_queue = u"排队取号";
    text_coupon = u"优惠券"

    # Click button time out
    click_on_button_timeout = 10

    # Movie button
    text_movie_button = u"电影"

    # Resource niche
    resource_id_resource_niche_button = "com.wanda.app.wanhui:id/film_gallery_item_poster"

    def __init__(self):
        pass;

