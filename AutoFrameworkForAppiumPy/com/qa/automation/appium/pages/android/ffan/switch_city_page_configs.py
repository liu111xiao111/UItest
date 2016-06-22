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
    resource_id_switch_city_cancel_button = "com.wanda.app.wanhui:id/tv_left_common_dialog"

    # Switch city switch button
    resource_id_switch_city_switch_button = "com.wanda.app.wanhui:id/tv_right_common_dialog"

    def __init__(self):
        pass
