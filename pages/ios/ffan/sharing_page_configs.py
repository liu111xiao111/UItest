#!/usr/bin/env python
# -*- coding:utf-8 -*-

class SharingPageConfigs(object):
    '''
    This is a configuration class for SharingPage class.
    '''


    # Assert view time out
    assert_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    # Cancel
    resource_id_cancel_bt = "取消"

    def __init__(self):
        pass
