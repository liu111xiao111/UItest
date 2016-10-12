#!/usr/bin/env python
# -*- coding:utf-8 -*-


class ShoppingMallPageConfigs(object):
    '''
    This is a configuration class for ShoppingMallPage class.
    '''

    # Assert view time out
    assert_view_timeout = 60

    # Click button time out
    click_on_button_timeout = 60

    # Shopping mall title
    resource_id_shopping_mall_title = "com.wanda.app.wanhui:id/txt_common_title"
    
    # Plaza view id
    resource_id_plaza_id = "com.wanda.app.wanhui:id/txt_item_name"
    
    # Shopping mall tab id
    resource_id_tab_id = "com.wanda.app.wanhui:id/txt_tab_name"
    
    view_text_distance = "公里"

    # "北京通州万达广场"
    text_beijing_tongzou_mall = u"北京通州万达广场"

    def __init__(self):
        pass
