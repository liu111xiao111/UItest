#!/usr/bin/env python
# -*- coding:utf-8 -*-

class HuiLifePageConfigs(object):
    '''
    This is a configuration class for HuiLifePage class.
    '''

    # Assert view time out
    assert_view_timeout = 30

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    # Activity button
    text_activity_button = u"活动"

    # Privilege button
    text_privilege_button = u"优惠"

    # TakingTaxi
    resource_id_taking_taxi_st = u"火车票"

    # Modules entry
    text_taxi = u"打车"
    text_designated_driving = u"代驾"
    text_bus = u"公交查询"
    text_stock_information = u"股票资讯"
    text_feifan_read = u"飞凡阅读"
    text_prepaid_recharge = u"话费充值"
    text_traffic_recharge = u"流量充值"
    text_qq_recharge = u"QQ充值"
    text_online_game_recharge = u"网游充值"
    text_fly_yue = u"飞悦"
    text_refuel = u"加油"
    text_concert = u"演唱会"
    text_drama = u"话剧"
    text_philharmonic = u"音乐会"
    text_illegal_inquiry = u"违章查询"

    name_jingxuan = u"精选"
    name_jiandian = u"荐店"

    # Verify modules entry
    verify_resource_didi_travel = "com.wanda.app.wanhui:id/didi_webview_title"  # 滴滴出行
    verify_text_stock_information = u"自选股"
    verify_text_feifan_read = u"书架"
    verify_text_prepaid_recharge = u"话费充值"
    verify_text_traffic_recharge = u"流量充值"
    verify_text_qq_recharge = u"QQ充值"
    verify_text_online_game_recharge = u"网游充值"
    verify_text_fly_yue = u"飞悦"
    verify_text_refuel = u"加油"
    verify_text_concert = u"演唱会"
    verify_text_drama = u"话剧"
    verify_text_philharmonic = u"音乐会"
    verify_text_illegal_inquiry = u"违章查询"

    # Specific activity button
    resource_id_specific_activity_button = "com.wanda.app.wanhui:id/activities_img"

    """
        底部导航栏tab resource id

    """
    resource_id_ll_bottom_bar = "ll_bottom_bar"

    # Specific privilege button
    resource_id_specific_privilege_button = "com.wanda.app.wanhui:id/activities_img"
    xpath_specific_privilege_button = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.FrameLayout[1]/android.view.View[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[3]/android.widget.LinearLayout[1]"

    # Specific activity title
    resource_id_specific_activity_title = "com.wanda.app.wanhui:id/activities_title"
    # Resource niche
    resource_id_resource_niche_button = "com.wanda.app.wanhui:id/film_gallery_item_poster"
    text_specific_activity_title = u"水云间满额赠礼活动"

    '''
        class name find by
    '''
    class_name_android_widget_FrameLayout = "android.widget.FrameLayout"

    xpath_jiayou = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[1]"
    #精选title
    xpath_jingxuan_title = "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAImage[1]"
    # 荐店title
    xpath_jiandian_title = "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAImage[1]"

    def __init__(self):
        pass
