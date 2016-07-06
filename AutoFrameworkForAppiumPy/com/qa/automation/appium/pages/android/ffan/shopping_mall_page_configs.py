#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Title: shopping_mall_page_configs.py
Package: com.qa.automation.appium.pages.android.ffan
Description: This is a configuration class for ShoppingMallPage class.
Company: Neusoft
All rights Reserved, Designed By Zhaosheng Liu
@copyright: Copyright(C) 2016-2017
@author: Zhaosheng Liu
@date Jun 17, 2016 04:47:50 PM
Modification  History:
Date                Author                Version                Description
Jun 17, 2016        liuzhsh               V0.0.0.1               New file
Why & What is modified: TODO
'''


class ShoppingMallPageConfigs(object):
    '''
    This is a configuration class for ShoppingMallPage class.
    '''

    # Assert view time out
    assert_view_timeout = 10

    # Click button time out
    click_on_button_timeout = 10

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
