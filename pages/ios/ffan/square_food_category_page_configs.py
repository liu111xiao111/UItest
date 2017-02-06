# -*- coding: utf-8 -*-

class SquareFoodPageConfigs():
    # 常量命名规则 resource_id指明资源类型是resource id;iv_center_tab view id name;iv指明view类型image view

    # 找餐厅
    name_ll_find_restaurant_id = u"找餐厅"
    xpath_find_restaurant = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]"

    # 找优惠
    name_ll_find_favourable_id = u"找优惠"
    xpath_find_favourable = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[2]"

    # 智能排队
    name_ll_intelligent_queuing_id = u"智能排队"
    xpath_intelligent_queuing = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[3]"

    # 帮你挑
    name_ll_stochastic_id = u"帮你挑"
    xpath_stochastic = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[4]"

    # 验证美食主界面
    verify_food_home_page_title = u"餐饮"

    # 验证找餐厅界面
    verify_find_restaurant_resourceID = u"餐饮门店"

    # 验证找优惠界面
    verify_find_favourable_resourceID = u"餐饮优惠"

    # 验证智能排队界面
    verify_intelligent_queuing_resourceID = u"排队取号"

    # 验证帮你挑界面
    verify_stochastic_resourceID = u"换一家"


    verify_assert_timeout = 10
    click_child_module_timeout = 10

    text_food = u"美食汇"

    def __init__(self):
        pass;
