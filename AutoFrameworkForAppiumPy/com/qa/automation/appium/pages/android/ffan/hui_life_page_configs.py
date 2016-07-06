#!/usr/bin/env python
# -*- coding:utf-8 -*-


class HuiLifePageConfigs(object):
    '''
    This is a configuration class for HuiLifePage class.
    '''

    # Assert view time out
    assert_view_timeout = 20

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    # Activity button
    text_activity_button = u"活动"

    # Privilege button
    text_privilege_button = u"优惠"

    # Modules entry
    text_express_train        = u"快车"
    text_taxi                 = u"出租车"
    text_special_train        = u"专车"
    text_designated_driving   = u"代驾"
    text_fly_yue              = u"飞悦"
    text_prepaid_recharge     = u"话费充值"
    text_traffic_recharge     = u"流量充值"
    text_qq_recharge          = u"QQ充值"
    text_online_game_recharge = u"网游充值"
    text_stock_information    = u"股票资讯"

    # Verify modules entry
    verify_text_didi_travel          = u"滴滴出行"
    verify_text_fly_yue              = u"飞悦"
    verify_text_prepaid_recharge     = u"话费充值"
    verify_text_traffic_recharge     = u"流量充值"
    verify_text_qq_recharge          = u"QQ充值"
    verify_text_online_game_recharge = u"网游充值"
    verify_text_stock_information    = u"自选股"

    # Specific activity button
    resource_id_specific_activity_button = "com.wanda.app.wanhui:id/activities_img"

    # Specific privilege button
    resource_id_specific_privilege_button = "com.wanda.app.wanhui:id/activities_img"
    xpath_specific_privilege_button = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.FrameLayout[1]/android.view.View[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[3]/android.widget.LinearLayout[1]"

    # Specific activity title
    resource_id_specific_activity_title = "com.wanda.app.wanhui:id/activities_title"
    # Resource niche
    resource_id_resource_niche_button = "com.wanda.app.wanhui:id/film_gallery_item_poster"
    text_specific_activity_title = u"水云间满额赠礼活动"

    def __init__(self):
        pass
