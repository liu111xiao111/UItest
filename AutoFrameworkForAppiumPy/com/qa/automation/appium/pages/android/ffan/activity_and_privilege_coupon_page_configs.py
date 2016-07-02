#!/usr/bin/env python
# -*- coding:utf-8 -*-

class ActivityAndPrivilegeCouponPageConfigs(object):
    '''
    This is a configuration class for ActivityAndPrivilegeCouponPage class.
    '''


    # Assert view time out
    assert_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    # Activity title
    resource_id_activity_title = "com.wanda.app.wanhui:id/id_tab_left"

    # Specific activity button
    resource_id_specific_activity_button = "com.wanda.app.wanhui:id/iv_image"

    # Privilege coupon title
    resource_id_privilege_coupon_title = "com.wanda.app.wanhui:id/id_tab_right"

    # Specific privilege coupon button
    resource_id_specific_privilege_coupon_button = "com.wanda.app.wanhui:id/iv_icon"

    def __init__(self):
        pass
