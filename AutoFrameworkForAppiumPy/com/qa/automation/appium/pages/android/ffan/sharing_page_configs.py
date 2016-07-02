#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Title: sharing_page_configs.py
Package: com.qa.automation.appium.pages.android.ffan
Description: This is a configuration class for SharingPage class.
Company: Neusoft
All rights Reserved, Designed By Zhaosheng Liu
@copyright: Copyright(C) 2016-2017
@author: Zhaosheng Liu
@date Jun 17, 2016 02:57:50 PM
Modification  History:
Date                Author                Version                Description
Jun 17, 2016        liuzhsh               V0.0.0.1               New file
Why & What is modified: TODO
'''


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

    # Sharing title
    resource_id_sharing_title = "com.wanda.app.wanhui:id/common_title_view_layout_title"

    def __init__(self):
        pass
