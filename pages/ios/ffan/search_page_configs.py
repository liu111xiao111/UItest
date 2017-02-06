# -*- coding: utf-8 -*-


class SearchPageConfigs():
    # 常量命名规则 resource_id指明资源类型是resource id;iv_center_tab view id name;iv指明view类型image view

    # 搜索 id
    name_search_bt = u"Search"

    # 搜索 输入框
    resource_et_search_input_et = "com.wanda.app.wanhui:id/et_search"
    xpath_search_tf = "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIATextField[1]"

    # xpath　搜索出来的店铺第一个
    xpath_search_result_first_item_tv = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]"

    # Click button time out
    click_on_button_timeout = 20

    # Input time out
    input_timeout = 10

    # Get time out
    get_timeout = 10

    # Movie button
    text_movie_button = u"电影"

    # Specific movie button
    resource_id_specific_movie_button = "com.wanda.app.wanhui:id/iv_icon"
    xpath_specific_movie_st = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]"

    # Specific movie button
    resource_id_specific_square_button = "com.wanda.app.wanhui:id/icon"
    xpath_specific_square_st = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]"

    text_store_detail = u"门店详情"
    name_store_details_st = u"门店详情"

    text_shop_name_description = u"木槿生活店（北京南苑路店）"

    text_searching_store_name = u"北京通州万达广场"

    text_searching_brand_name = u"adidas"

    text_city = u"北京通州"

    xpath_brand_name = u"//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIAStaticText[1]"

    text_searching_goods_name = "MU8600"
    xpath_goods_name = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIAStaticText[2]"

    # Specific store button
    resource_id_specific_store_button = "com.wanda.app.wanhui:id/title"
    xpath_specific_store_tv = "//UIAApplication[1]/UIAWindow[1]/UIATableView[2]/UIATableCell[1]/UIAStaticText[1]"

    # Assert view time out
    assert_view_timeout = 10

    xpath_moview = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIAScrollView[1]/UIAButton[3]"

    xpath_first_result = "//UIAApplication[1]/UIAWindow[1]/UIATableView[2]/UIATableCell[1]"

    xpaht_city = u"//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIAStaticText[3]"

    xpath_movie_text = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]"

    def __init__(self):
        pass;
