#!/usr/bin/env python
# -*- coding:utf-8 -*-


class SwitchCityPageConfigs(object):
    '''
    This is a configuration class for SwitchCityPage class.
    '''

    # Assert view time out
    assert_view_timeout = 10

    # Verify view time out
    verify_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Switch city cancel button
    resource_id_switch_city_cancel_button = u"否"

    # Switch city switch button
    resource_id_switch_city_switch_button = u"是"

    def __init__(self):
        pass