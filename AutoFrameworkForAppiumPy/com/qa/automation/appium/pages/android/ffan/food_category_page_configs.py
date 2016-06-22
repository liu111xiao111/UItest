# -*- coding: utf-8 -*-

import os, sys


class FoodCategoryPageConfigs():
    # 常量命名规则 resource_id指明资源类型是resource id;iv_center_tab view id name;iv指明view类型image view

    # 找餐厅
    resource_id_bt_find_restaurant_bt = "com.wanda.app.wanhui:id/id_tab_left";
    # 找优惠
    resource_id_bt_find_coupon_bt = "com.wanda.app.wanhui:id/id_tab_right";

    resource_id_tv_restaurant_tv = "com.wanda.app.wanhui:id/multiple_headers_dropdown_listview_header_item_text";

    # text指明类型为text label,后面是文字的拼音

    text_restaurant = "餐饮";

    def __init__(self):
        pass;
