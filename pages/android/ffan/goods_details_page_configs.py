#!/usr/bin/env python
# -*- coding:utf-8 -*-


class GoodsDetailsPageConfigs(object):
    '''
    This is a configuration class for GoodsDetailsPage class.
    '''

    # Assert view time out
    assert_view_timeout = 90

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 90

    # Flash Sales Square title
    resource_id_reource_goods_details_title = "com.wanda.app.wanhui:id/common_title_view_layout_title"

    def __init__(self):
        pass
