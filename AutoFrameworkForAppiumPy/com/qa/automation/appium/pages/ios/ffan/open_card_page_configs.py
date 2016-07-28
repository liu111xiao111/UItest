# -*- coding: utf-8 -*-

class OpenCardPageConfigs():
    # 常量命名规则 resource_id指明资源类型是resource id;iv_center_tab view id name;iv指明view类型image view

    # 开卡text
    text_bus_card = u"市民/公交卡"
    xpath_bus_card = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIAStaticText[1]"
    text_joint_card = u"一卡通飞凡联名卡"
    xpath_joint_card = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]"

    verify_view_resourceId= u"我的市民/公交卡"
    verify_view_timeout = 10

    def __init__(self):
        pass;
