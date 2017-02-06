#!/usr/bin/env python
# -*- coding: utf-8 -*-


class StoreImageTextDetailsPageConfigs():

    # Click button time out
    click_on_button_timeout = 10

    # Assert view time out
    assert_view_timeout = 10

    # Store image text details title
    resource_id_store_image_text_details = "com.wanda.app.wanhui:id/common_title_view_layout_title"

    # Store image text details button
    xpath_store_image_text_details_button = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.wanda.sliding.SlidingLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]"

    def __init__(self):
        pass;
