#!/usr/bin/env python
# -*- coding:utf-8 -*-


class PopupPageConfigs(object):
    '''
    This is a configuration class for PopupPage class.
    '''


    # Assert view time out
    assert_view_timeout = 10

    # Verify view time out
    verify_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    # Switch city cancel button
    resource_id_switch_city_cancel_button = "com.wanda.app.wanhui:id/tv_left_common_dialog"

    # Switch city switch button
    resource_id_switch_city_switch_button = "com.wanda.app.wanhui:id/tv_right_common_dialog"

    def __init__(self):
        pass
