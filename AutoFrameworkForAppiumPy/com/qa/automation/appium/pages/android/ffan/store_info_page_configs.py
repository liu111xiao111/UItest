# -*- coding: utf-8 -*-

import os, sys


class StoreInfoPageConfigs():
    # 常量命名规则 resource_id指明资源类型是resource id;iv_center_tab view id name;iv指明view类型image view


    # text指明类型为text label,后面是文字的拼音

    text_store_detail = u"门店详情"
    text_store_info = u"门店信息";

    xpath_store_info = "//*[@content-desc='门店信息']"

    def __init__(self):
        pass;
