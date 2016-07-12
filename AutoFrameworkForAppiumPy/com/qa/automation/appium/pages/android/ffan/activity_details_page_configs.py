#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
    活动详情页
'''
class ActivityDetailsPageConfigs(object):
    '''
    This is a configuration class for ActivityDetailsPage class.
    '''
    
    content_desc_activity_detail = "活动详情"

    # Assert view time out
    assert_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    # Activity details title
    resource_id_activity_details_title = "com.wanda.app.wanhui:id/common_title_view_layout_title"

    # Sharing button
    xpath_sharing_button = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.wanda.sliding.SlidingLayout[1]/android.widget.RelativeLayout[1]/android.view.View[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.ImageView[1]"

    def __init__(self):
        pass
