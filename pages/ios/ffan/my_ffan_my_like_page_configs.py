# -*- coding: utf-8 -*-

class MyFfanMyLikePageConfigs():
    # "我的喜欢"
    name_tv_my_like_tv = u"我的喜欢"
    xpath_like_goods = "//UIAApplication[1]/UIAWindow[1]/UIAStaticText[1]"
    xpath_like_dissertation = "//UIAApplication[1]/UIAWindow[1]/UIAStaticText[2]"
    xpath_like_brand = "//UIAApplication[1]/UIAWindow[1]/UIAStaticText[3]"

    xpath_goods_details_title = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]"

    # "商品"
    uia_string_like_goods = ".segmentedControls()[0].buttons()['商品']"

    # "专题"
    uia_string_like_dissertation = ".segmentedControls()[0].buttons()['专题']"

    # "品牌"
    uia_string_like_brand = ".segmentedControls()[0].buttons()['品牌']"

    verify_view_timeout = 10

    def __init__(self):
        pass;
