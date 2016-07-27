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

    # Get time out
    get_timeout = 10

    # Valid time out
    valid_timeout = 10

    # Cinema title
    resource_id_cinema_title = "com.wanda.app.wanhui:id/common_title_view_layout_title"
    xpath_cinema_title_st = "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAStaticText[1]"

    # Movie name
    resource_id_movie_name_button = "com.wanda.app.wanhui:id/tv_name_movie_home"
    xpath_movie_name_st = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[3]/UIAStaticText[1]"

    # Buy ticket button
    resource_id_buy_ticket_bt = u"选座"

    # tomorrow's date button
    xpath_tomorrows_date_bt = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[6]/UIAButton[2]"

    # Popup title
    resource_id_popup_title = "android:id/alertTitle"

    # Yes button
    resource_id_yes_button = "android:id/button1"

    def __init__(self):
        pass
