# -*- coding: utf-8 -*-


"""
    爱逛街页面配置
"""
class LoveShoppingPageConfigs():


    """
        *********************************iOS 控件name*****************************

    """
    name_shopping_mall = "购物中心";
    name_film = "电影";
    name_food = "美食";
    name_brand = "品牌";
    name_children = "亲子";
    name_preferential = "优惠";
    name_shopping = "购物";
    name_flash_sale = "限时抢购";
    name_parking = "停车";
    name_le_pays = "乐付";

    name_search_all_city = "全城搜索";


    """
        *********************************iOS 控件xpath*****************************

    """
    xpath_flash_sale = "//UIAApplication[1]/UIAWindow[1]/UIACollectionView[1]/UIACollectionCell[1]/UIACollectionView[1]/UIACollectionCell[6]"

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

    # City name
    xpath_city_name_st = "//UIAApplication[1]/UIAWindow[1]/UIAStaticText[1]"
    xpath_city_name_bt = "//UIAApplication[1]/UIAWindow[1]/UIAButton[1]"

    # Commercial District Name
    xpath_commercial_district_name_st = "//UIAApplication[1]/UIAWindow[1]/UIACollectionView[1]/UIACollectionCell[3]/UIACollectionView[1]/UIACollectionCell[1]/UIAStaticText[1]"

    def __init__(self):
        pass;
