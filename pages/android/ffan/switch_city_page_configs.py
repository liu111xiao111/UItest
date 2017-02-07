# -*- coding:utf-8 -*-


class SwitchCityPageConfigs(object):
    '''
    This is a configuration class for SwitchCityPage class.
    '''

    # Assert view time out
    assert_view_timeout = 10

    # Verify view time out
    verify_view_timeout = 90

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Get view time out
    get_view_timeout = 20

    # Switch city cancel button
    resource_id_switch_city_cancel_button = "com.wanda.app.wanhui:id/tv_left_common_dialog"

    # Switch city switch button
    resource_id_switch_city_switch_button = "com.wanda.app.wanhui:id/tv_right_common_dialog"

    # Hint content
    xpath_hint_content_st = "//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]"

    # Beijing
    text_city_name = u"北京市"
    xpath_city_name = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"

    def __init__(self):
        pass