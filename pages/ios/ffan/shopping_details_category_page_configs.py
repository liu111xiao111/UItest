# -*- coding: utf-8 -*-


class ShoppingDetailsCategoryPageConfigs():

    # Assert view time out
    assert_view_timeout = 10

    # Click button time out
    click_on_button_timeout = 10

    # Get text time out
    get_text_timeout = 10

    # Goods button
    name_goods_st = u"商品"

    # My favorite button
    name_my_favorite_st = u"喜欢"
    xpath_my_favorite_st = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIAStaticText[1]"

    # the shop name
    xpath_shop_name_st = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIAStaticText[11]"

    text_dashboard = u"首页";
    text_store = u"门店";

    def __init__(self):
        pass;
