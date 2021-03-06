# -*- coding: utf-8 -*-


class SearchPageConfigs():
    # 常量命名规则 resource_id指明资源类型是resource id;iv_center_tab view id name;iv指明view类型image view

    # 搜索 id
    resource_tv_search_tv = "com.wanda.app.wanhui:id/tv_search_btn";
    # 搜索 输入框
    resource_et_search_input_et = "com.wanda.app.wanhui:id/et_search";

    # xpath　搜索出来的店铺第一个
    xpath_search_result_first_item = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.wanda.sliding.SlidingLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[1]";

    # Click button time out
    click_on_button_timeout = 10

    # Movie button
    text_movie_button = u"电影"

    # 百货按钮
    text_shopping_mall = u"百货"

    # 检索出的百货列表中的第一项条目
    resource_id_first_item = "com.wanda.app.wanhui:id/title"

    # Specific movie button
    resource_id_specific_movie_button = "com.wanda.app.wanhui:id/iv_icon"

    # Specific movie button
    resource_id_specific_square_button = "com.wanda.app.wanhui:id/icon"

    text_store_detail = u"通州"

    text_store_details = u"门店详情"

    text_shop_name_description = u"木槿生活店（北京南苑路店）"

    text_searching_store_name = u"北京通州店"

    text_searching_brand_name = "adidas"

    text_searching_goods_name = "MU8600"

    # Specific store button
    resource_id_specific_store_button = "com.wanda.app.wanhui:id/title"

    # Assert view time out
    assert_view_timeout = 10

    # Valid view time out
    valid_view_timeout = 10

    # Get view time out
    get_view_timeout = 10

    # Hot word module
    resource_id_hot_word_module_tv = "com.wanda.app.wanhui:id/tv_hot_word"
    xpath_hot_word_module_tv = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.wanda.sliding.SlidingLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.LinearLayout[1]/android.widget.GridView[1]/android.widget.RelativeLayout[%d]/android.widget.TextView[1]"

    # 期待列表长度
    expectLenth = 0


    def __init__(self):
        pass;
