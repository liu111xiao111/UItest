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

    # Click button time out
    click_on_button_timeout = 10

    # Get view time out
    get_view_timeout = 10

    # Switch city cancel button
    resource_id_switch_city_cancel_bt = u"否"

    # Switch city switch button
    resource_id_switch_city_switch_bt = u"是"

    # Hint content
    xpath_hint_content_st = "//UIAApplication[1]/UIAWindow[5]/UIAAlert[1]/UIAScrollView[1]/UIAStaticText[2]"
    
    #Input for city
    xpath_city_input = "//UIAApplication[1]/UIAWindow[1]/UIATextField[1]"
    
    #City list 1
    xpath_city_list_one = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]"
    
    name_city_beijing = "北京市"

    def __init__(self):
        pass
