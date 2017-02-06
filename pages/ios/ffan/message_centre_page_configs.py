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
    name_message_centre_title_st = "消息中心"

    # Fei fan Activity
    text_fei_fan_activity = u"飞凡活动"
    name_fei_fan_activity_st = u"飞凡活动"

    # Square dynamic
    text_square_dynamic = u"广场动态"
    name_square_dynamic_st = u"广场动态"

    # Brand activity
    text_brand_activity = u"品牌活动"
    name_brand_activity_st = u"品牌活动"

    # Store message
    text_store_message = u"门店消息"
    name_store_message_st = u"门店消息"

    # Settings button
    text_settings_button = u"设置"
    name_settings_st = u"设置"

    def __init__(self):
        pass
