#!/usr/bin/env python
# -*- coding:utf-8 -*-


class SeatPickingPageConfigs(object):
    '''
    This is a configuration class for SeatPickingPage class.
    '''


    # Assert view time out
    assert_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    # SeatPicking title
    resource_id_seat_picking_title = "com.wanda.app.wanhui:id/common_title_view_layout_title"

    def __init__(self):
        pass
