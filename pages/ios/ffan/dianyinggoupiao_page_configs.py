#!/usr/bin/env python
# -*- coding:utf-8 -*-


class dianyinggoupiaoconfigs(object):
    '''
    This is a configuration class for GoodsDetailsPage class.
    '''

    # Assert view time out
    assert_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 20

    # Flash Sales Square title
    name_reource_goods_details_title_st = u"商品详情"

    # Commodity name
    xpath_xuanzuo = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAButton[1]"

    xpath_yingcheng = '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]'

    xpath_qiehuanchengshi = '//UIAApplication[1]/UIAWindow[1]/UIAStaticText[1]'

    xpath_shuruchengshi = '//UIAApplication[1]/UIAWindow[1]/UIATextField[1]'

    chengshiname = u'包头'

    baotoushi = u'包头市'

    input_timeout = 10

    # Shopping trolley
    xpath_shopping_trolley_st = "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[3]"

    def __init__(self):
        pass
