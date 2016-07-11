#!/usr/bin/env python
# -*- coding:utf-8 -*-


class FlashSalesSquarePageConfigs(object):
    '''
    This is a configuration class for FlashSalesSquarePage class.
    '''

    # Assert view time out
    assert_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    # Flash Sales Square title
    resource_id_reource_flash_sales_square_title = "com.wanda.app.wanhui:id/common_title_view_layout_title"

    # Goods button
    resource_id_goods_button = "com.wanda.app.wanhui:id/goods_picture"

    def __init__(self):
        pass
