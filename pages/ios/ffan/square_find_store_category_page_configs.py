# -*- coding: utf-8 -*-

class SquareFindStoreConfigs():
    # 常量命名规则 resource_id指明资源类型是resource id;iv_center_tab view id name;iv指明view类型image view

    # 全部分类text id
    resource_id_tv_category_tv = u"找店"

    name_store_page = u"门店详情"

    # 找店 search image view
    xpath_iv_search_iv = "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[3]"
    
    #页面list第一个店
    xpath_store_first_item = "//UIAApplication[1]/UIAWindow[1]/UIATableView[2]/UIATableCell[1]"

    verify_view_timeout = 10


    def __init__(self):
        pass;
