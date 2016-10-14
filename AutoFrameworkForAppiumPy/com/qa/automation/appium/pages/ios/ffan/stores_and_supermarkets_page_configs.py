#!/usr/bin/env python
# -*- coding:utf-8 -*-

class StoresAndSupermarketsPageConfigs(object):
    '''
    This is a configuration class for StoresAndSupermarketsPageConfigs class.
    '''

    # Assert view time out
    assert_view_timeout = 10

    # Click button time out
    click_on_button_timeout = 10

    # Get text time out
    get_text_timeout = 10

    # Shopping mall title
    name_stores_and_spuermarkets_title_st = u"商店超市"

    # First store or supermarket
    xpath_first_store_or_supermarket_st = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]"


    def __init__(self):
        pass
