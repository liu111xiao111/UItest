#!/usr/bin/env python
# -*- coding:utf-8 -*-


class ResourceNicheDetailsPageConfigs(object):
    '''
    This is a configuration class for ResourceNicheDetailsPage class.
    '''

    # Assert view time out
    assert_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    # Resource Niche Details title
    resource_id_reource_niche_details_title = "com.wanda.app.wanhui:id/common_title_view_layout_title"

    # 分享按钮图标resource id
    resource_id_common_title_view_layout_right_container = "common_title_view_layout_right_container"


    """
        class name of web view
    """
    class_name_android_webkit_WebView = "android.webkit.WebView"

    # Resource niche title
    xpath_resource_niche_st = "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAStaticText[1]"

    def __init__(self):
        pass
