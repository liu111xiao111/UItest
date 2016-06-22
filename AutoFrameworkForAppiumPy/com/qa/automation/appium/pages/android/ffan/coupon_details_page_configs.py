#!/usr/bin/env python
# -*- coding:utf-8 -*-


class CouponDetailsPageConfigs(object):
    '''
    This is a configuration class for CouponDetailsPage class.
    '''

    # Assert view time out
    assert_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    # Coupon details title
    resource_id_coupon_details_title = "com.wanda.app.wanhui:id/common_title_view_layout_title"

    # Receive free button
    text_receive_free_button = u"免费领取"

    def __init__(self):
        pass
