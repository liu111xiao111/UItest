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
    resource_id_message_settings_title_st = u"设置"

    xpath_activity_push_compound_sc = "//UIAApplication[1]/UIAWindow[1]/UIASwitch[1]"

    def __init__(self):
        pass
