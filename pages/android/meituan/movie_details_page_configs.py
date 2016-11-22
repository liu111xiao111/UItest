#!/usr/bin/env python
# -*- coding:utf-8 -*-


class MovieDetailsPageConfigs(object):
    '''
    This is a configuration class for MovieDetailsPage class.
    '''


    # Assert view time out
    assert_view_timeout = 90

    # Verify view time out
    verify_view_timeout = 90

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 90

    # Movie details title
    resource_id_movie_details_title = "com.wanda.app.wanhui:id/common_title_view_layout_title"
    text_all_film = u"全部热映"
    text_details_film = u"上映影院和购票"

    # tomorrow's date button
    xpath_tomorrows_date_button = " //android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.wanda.sliding.SlidingLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.HorizontalScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]"
    text_buy_ticket = u"购票"
    # Sub-cinema button
    resource_id_sub_cinema_button = "com.wanda.app.wanhui:id/tv_name"

    def __init__(self):
        pass