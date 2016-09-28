# -*- coding: utf-8 -*-


class FoodCategoryPageConfigs():
    # 常量命名规则 resource_id指明资源类型是resource id;iv_center_tab view id name;iv指明view类型image view

    # 餐厅
    resource_id_bt_restaurant_bt = "com.wanda.app.wanhui:id/food_home_gridview_item"
    # 优惠活动
    resource_id_bt_coupon_bt = "com.wanda.app.wanhui:id/coupon_campaign"
    # 抢券
    resource_id_bt_grab_bt = "com.wanda.app.wanhui:id/food_home_coupon"
    # 买单
    resource_id_bt_pay_bt = "com.wanda.app.wanhui:id/pay_bill"

    resource_id_tv_restaurant_tv = "com.wanda.app.wanhui:id/multiple_headers_dropdown_listview_header_item_text"

    # text指明类型为text label,后面是文字的拼音

    view_text_tiltle = u"美食汇"

    verify_view_timeout = 10
    click_view_timeout = 10

    def __init__(self):
        pass
