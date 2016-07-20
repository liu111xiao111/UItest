# -*- coding: utf-8 -*-

class ChildCategoryPageConfigs():
    # 常量命名规则 resource_id指明资源类型是resource id;iv_center_tab view id name;iv指明view类型image view

    # 亲子儿童
    name_child_title = u"亲子儿童"
    # 亲自游乐
    resource_id_ll_child_play_ll = u"亲子游乐"
    # 儿童教育
    resource_id_ll_child_education_ll = u"儿童教育"
    # 亲子购物
    resource_id_ll_child_shopping_ll = u"亲子购物"
    # 其它门店
    resource_id_ll_other_store_ll = u"其他门店"

    #xpath
    # 亲自游乐 儿童教育 亲子购物 其他门店 点击进去后的listview 的第一个的xpath
    xpath_store_list_1 = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]"
    # 门店详情界面
    xpath_store_list_2 = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIALink[1]"
    # 门店详情界面标题
    xpath_store_title = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIAStaticText[1]"
    click_on_button_timeout = 10

