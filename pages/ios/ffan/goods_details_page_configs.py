#!/usr/bin/env python
# -*- coding:utf-8 -*-


class GoodsDetailsPageConfigs(object):
    '''
    This is a configuration class for GoodsDetailsPage class.
    '''

    # Assert view time out
    assert_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    # Flash Sales Square title
    resource_id_reource_goods_details_title_st = u"商品详情"

    # Commodity name
    xpath_commodity_name_st = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIAStaticText[5]"

    # Shopping trolley
    xpath_shopping_trolley_st = "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[3]"

    def __init__(self):
        pass
