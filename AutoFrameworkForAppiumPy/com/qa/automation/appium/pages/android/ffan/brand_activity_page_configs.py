#!/usr/bin/env python
# -*- coding:utf-8 -*-


class BrandActivityPageConfigs(object):
    '''
    This is a configuration class for BrandActivityPage class.
    '''


    # Assert view time out
    assert_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    # Square dyname title
    resource_id_square_dynamic_title = "com.wanda.app.wanhui:id/common_title_view_layout_title"

    def __init__(self):
        pass
