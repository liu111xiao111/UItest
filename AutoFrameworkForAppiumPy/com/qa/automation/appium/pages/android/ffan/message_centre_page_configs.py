#!/usr/bin/env python
# -*- coding:utf-8 -*-


class MessageCentrePageConfigs(object):
    '''
    This is a configuration class for MessageCentrePage class.
    '''

    # Assert view time out
    assert_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    # Message centre title
    resource_id_message_centre_title = "com.wanda.app.wanhui:id/common_title_view_layout_title"

    # Settings button
    text_settings_button = u"设置"

    def __init__(self):
        pass
