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

    # Buy ticket button
    resource_id_buy_ticket_button = "com.wanda.app.wanhui:id/buy_button"

    def __init__(self):
        pass
