#!/usr/bin/env python
# -*- coding:utf-8 -*-


class CinemaPageConfigs(object):
    '''
    This is a configuration class for CinemaPage class.
    '''

    # Assert view time out
    assert_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    # Cinema title
    resource_id_cinema_title = "com.wanda.app.wanhui:id/common_title_view_layout_title"

    # 影片未上映
    text_film_run = u"影片未上映"

    # Movie name
    resource_id_movie_name_button = "com.wanda.app.wanhui:id/tv_name_movie_home"

    # Buy ticket button
    resource_id_buy_ticket_button = "com.wanda.app.wanhui:id/buy_button"

    # tomorrow's date button
    xpath_tomorrows_date_button = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.wanda.sliding.SlidingLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.HorizontalScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]"

    # Popup title
    resource_id_popup_title = "android:id/alertTitle"

    # Yes button
    resource_id_yes_button = "android:id/button1"

    def __init__(self):
        pass
