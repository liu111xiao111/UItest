# -*- coding: utf-8 -*-


class LoveShoppingPageConfigs():
    # text指明类型为text label,后面是文字的拼音
    text_search_all_city = "全城搜索"
    text_shopping_mall = "购物中心"
    text_film = "电影"
    text_food = "美食"
    text_brand = "品牌"
    text_children = "亲子"
    text_preferential = "优惠"
    text_shopping = "购物"
    text_flash_sale = "限时抢购"
    text_parking = "停车"
    text_le_pays = "乐付"

    resource_id_id_tv_city = "tv_city"

    # Click button time out
    click_on_button_timeout = 10

    # Get view time out
    get_view_timeout = 10

    # City name
    xpath_city_name_tv = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"

    # Commercial District Name
    xpath_commercial_district_name_st = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"

    # Hint content
    xpath_hint_content_st = "//UIAApplication[1]/UIAWindow[5]/UIAAlert[1]/UIAScrollView[1]/UIAStaticText[2]"


    def __init__(self):
        pass
