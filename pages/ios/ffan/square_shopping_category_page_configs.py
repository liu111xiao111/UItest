# -*- coding: utf-8 -*-

class SquareShoppingPageConfigs():
    # 常量命名规则 resource_id指明资源类型是resource id;iv_center_tab view id name;iv指明view类型image view
    # 商品图片id
    resource_id_iv_find_iv = "com.wanda.app.wanhui:id/goods_list_item_image";

    # text指明类型为text label,后面是文字的拼音

    # Click button time out
    click_on_button_timeout = 10

    # Get time out
    get_timeout = 10

    # Sub-commodity button
    resource_id_sub_commodity_button = "com.wanda.app.wanhui:id/goods_list_item_name"
    xpath_sub_commodity_st = "//UIAApplication[1]/UIAWindow[1]/UIACollectionView[1]/UIACollectionCell[1]/UIAStaticText[1]"

    # Commodity title
    name_commodity_title_st = u"爱购物"

    def __init__(self):
        pass;
