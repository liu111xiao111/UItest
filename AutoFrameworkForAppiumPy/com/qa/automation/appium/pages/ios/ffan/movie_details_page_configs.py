#!/usr/bin/env python
# -*- coding:utf-8 -*-


class MovieDetailsPageConfigs(object):
    '''
    This is a configuration class for MovieDetailsPage class.
    '''


    # Assert view time out
    assert_view_timeout = 10

    # Verify view time out
    verify_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    # Movie details title
    resource_id_movie_details_title = "com.wanda.app.wanhui:id/common_title_view_layout_title"
    xpath_movie_details_title_st = "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAStaticText[1]"

    # tomorrow's date button
    xpath_tomorrows_date_button = " //android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.wanda.sliding.SlidingLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.HorizontalScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]"

    # Sub-cinema button
    resource_id_sub_cinema_button = "com.wanda.app.wanhui:id/tv_name"
    xpath_sub_cinema_st = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]"

    def __init__(self):
        pass