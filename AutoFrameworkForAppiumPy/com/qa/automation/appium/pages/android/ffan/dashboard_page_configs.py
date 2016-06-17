# -*- coding: utf-8 -*-

import os,sys


class DashboardPageConfigs():

    # 常量命名规则 resource_id指明资源类型是resource id;iv_center_tab view id name;iv指明view类型image view
    # 首页中间摇一摇图标
    resource_id__iv_center_tab__iv = "iv_center_tab";

    #城市text view
    resource_id__tv_city__tv = "tv_city";

    # ffan logo图标
    resource_id__iv_logo__iv = "iv_logo";

    # 更多图标
    resource_id__iv_right_icon__iv = "iv_right_icon";


    # 广场列表按钮resource id
    resource_id_plaza_list_fab = "plaza_list_fab";
    
    # 首页摇一摇对话框
    resource_id_iv_home_shake_tips = "com.wanda.app.wanhui:id/iv_shake_off"
    
    #全城搜索输入框
    resource_id_tv_search_tv = "com.wanda.app.wanhui:id/tv_text"
    
    #xpath
    #广场模块
    xpath_square_module = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.RelativeLayout[1]";

    # text指明类型为text label,后面是文字的拼音
    text_aiguangjie = u"爱逛街";
    text_huishenghuo = u"慧生活";
    text_ffancard = u"飞凡卡";
    text_mine = u"我的";
    # Home pannel, shopping, film, food and so on.
    text_food = u"美食";
    text_child = u"亲子"
    
    text_lefu = u"乐付";
    text_parking = u"停车";

    # 搜索框默认字段
    text_quanchengsousuo = u"全城搜索";
    
    text_feifan_card = u"飞凡卡"
    
    text_search_text = u"adidas"

    # Verify view time out
    verify_view_timeout = 10

    # Beijing Text identify
    text_city_beijing = "北京市"

    # Verify view time out
    verify_view_timeout = 10

    # Beijing Text identify
    text_city_beijing = "北京市"

    # Click button time out
    click_on_button_timeout = 10

    # Flash sales more
    resource_id_flash_sales_more_button = "com.wanda.app.wanhui:id/tv_more"
    text_flash_sales_more_button = u"更多"

    def __init__(self):
        pass;

