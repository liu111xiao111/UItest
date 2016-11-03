#!/usr/bin/env python
# -*- coding:utf-8 -*-


class SupermarketPageConfigs(object):
    '''
    This is a configuration class for ShoppingMallPage class.
    '''

    # Assert view time out
    assert_view_timeout = 60

    # 商店超市页面标题
    text_supermarket_title = u"商店超市"

    # 商店超市页面（tab）标题
    text_supermarket_tab_title = u"便利店"
    text_supermarket_tab_beijing_title = u"超市"

    # 商店超市列表数量
    SUPERMARKETNUMBER = 15

    # 商店超市列表项目
    type_supermarket = "android.widget.RelativeLayout"

    view_text_distance = "公里"

    # "北京通州万达广场"
    text_beijing_tongzou_mall = u"北京通州万达广场"

    def __init__(self):
        pass
