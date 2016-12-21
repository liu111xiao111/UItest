# -*- coding: utf-8 -*-

class SquareFoodPageConfigs():
    # 常量命名规则 resource_id指明资源类型是resource id;iv_center_tab view id name;iv指明view类型image view

    # 找餐厅id
    resource_id_ll_find_restaurant_id = "com.wanda.app.wanhui:id/food_circle_item_text"

    # 找优惠id
    resource_id_ll_find_favourable_id = "com.wanda.app.wanhui:id/home_enter_favourable"

    # 智能排队id
    resource_id_ll_intelligent_queuing_id = "com.wanda.app.wanhui:id/home_enter_queue"

    # 帮你挑id
    resource_id_ll_stochastic_id = "com.wanda.app.wanhui:id/home_enter_stochastic"

    # 验证美食主界面id
    verify_food_home_page_resourceID = "com.wanda.app.wanhui:id/common_title_view_layout_title"
    verify_text_food = u"美食汇"

    # 验证找餐厅界面id
    verify_find_restaurant_resourceID = "com.wanda.app.wanhui:id/pic"

    # 验证找优惠界面id
    verify_find_favourable_resourceID = "com.wanda.app.wanhui:id/pic"

    # 验证智能排队界面id
    verify_intelligent_queuing_resourceID = "com.wanda.app.wanhui:id/common_title_view_layout_title"

    # 验证帮你挑界面id
    verify_stochastic_resourceID = "com.wanda.app.wanhui:id/layout_middle"
    #verify_stochastic_resourceID = "com.wanda.app.wanhui:layout_middle"


    verify_assert_timeout = 90
    click_child_module_timeout = 30

    def __init__(self):
        pass;
