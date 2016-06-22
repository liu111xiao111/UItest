#!/usr/bin/env python
# -*- coding:utf-8 -*-


class HuiLifePageConfigs(object):
    '''
    This is a configuration class for HuiLifePage class.
    '''

    # Assert view time out
    assert_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    # Activity button
    text_activity_button = u"活动"

    # Privilege button
    text_privilege_button = u"优惠"

    # Specific activity button
    resource_id_specific_activity_button = "com.wanda.app.wanhui:id/activities_img"

    # Specific privilege button
    resource_id_specific_privilege_button = "com.wanda.app.wanhui:id/activities_img"
    xpath_specific_privilege_button = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.FrameLayout[1]/android.view.View[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[3]/android.widget.LinearLayout[1]"

    # Specific activity title
    resource_id_specific_activity_title = "com.wanda.app.wanhui:id/activities_title"
    text_specific_activity_title = u"水云间满额赠礼活动"

    def __init__(self):
        pass
