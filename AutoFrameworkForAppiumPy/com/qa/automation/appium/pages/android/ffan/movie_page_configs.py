#!/usr/bin/env python
# -*- coding:utf-8 -*-


class MoviePageConfigs(object):
    '''
    This is a configuration class for MoviePage class.
    '''


    # Assert view time out
    assert_view_timeout = 10

    # Verify view time out
    verify_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    # Movie title
    text_movie_title = u"电影"

    # Seat picking and buying ticket button
    resource_id_seat_picking_and_buying_ticket_button = "com.wanda.app.wanhui:id/movie_buy_ticket"

    def __init__(self):
        pass