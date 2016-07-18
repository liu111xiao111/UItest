#!/usr/bin/env python
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
    text_flash_sales = u"限时抢购"

    # Click button time out
    click_on_button_timeout = 10

    # Movie button
    text_movie_button = u"电影"
    resource_id_movie_st = u"电影"

    # Resource niche
    resource_id_resource_niche_button = "com.wanda.app.wanhui:id/film_gallery_item_poster"
    xpath_resource_niche_tc = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]"

    # Staff picks button
    text_staff_picks_button = u"达人推荐"
    xpath_staff_picks_button = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.wanda.sliding.SlidingLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[1]"

    # Sub staff picks button
    xpath_sub_staff_picks_button = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.wanda.sliding.SlidingLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]"

    # Born to shop
    resource_id_born_to_shop_st = u"爱购物"

    # Get view time out
    get_view_timeout = 10

    # Find store button
    xpath_find_store_button = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.wanda.sliding.SlidingLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]"

    # General coupon button
    text_general_coupon_button = u"通用券"
    xpath_general_coupon_button = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.wanda.sliding.SlidingLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ImageView[1]"

    # Assert view time out
    assert_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    # Find store
    resource_id_find_store_st = u"找店"

    # Search
    resource_id_search_bt = "home nav search"

    # Parking
    resource_id_parking_cc = u"停车"

    # Sign in
    resource_id_sign_in_st = u"签到"

    # Privilege coupon
    resource_id_privilege_coupon_st = u"优惠券"

    def __init__(self):
        pass;
