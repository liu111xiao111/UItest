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
    name_general_coupon_title = u"通用券"

    # Immediately to receive
    text_immediately_to_receive = u"马上领取"
    xpath_immediately_to_receive = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIALink[1]/UIAStaticText[1]"

    def __init__(self):
        pass
