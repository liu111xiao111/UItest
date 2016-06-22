#!/usr/bin/env python
# -*- coding:utf-8 -*-


class MessageSettingsPageConfigs(object):
    '''
    This is a configuration class for MessageSettingsPage class.
    '''

    # Assert view time out
    assert_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    # Message settings title
    resource_id_message_settings_title = "com.wanda.app.wanhui:id/common_title_view_layout_title"

    resource_id_activity_push_compound_button = "com.wanda.app.wanhui:id/push_switch"

    def __init__(self):
        pass
