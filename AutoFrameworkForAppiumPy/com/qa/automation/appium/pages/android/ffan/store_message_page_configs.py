#!/usr/bin/env python
# -*- coding:utf-8 -*-


class StoreMessagePageConfigs(object):
    '''
    This is a configuration class for StoreMessagePage class.
    '''


    # Assert view time out
    assert_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    # Store message title
    resource_id_store_message_title = "com.wanda.app.wanhui:id/common_title_view_layout_title"

    def __init__(self):
        pass
