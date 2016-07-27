#!/usr/bin/env python
# -*- coding:utf-8 -*-


class GeneralCouponPageConfigs(object):
    '''
    This is a configuration class for GeneralCouponPage class.
    '''


    # Assert view time out
    assert_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    # General coupon title
    resource_id_general_coupon_title = "com.wanda.app.wanhui:id/common_title_view_layout_title"

    # Immediately to receive
    text_immediately_to_receive = u"马上领取 Link"
    xpath_immediately_to_receive = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.wanda.sliding.SlidingLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]"

    def __init__(self):
        pass
