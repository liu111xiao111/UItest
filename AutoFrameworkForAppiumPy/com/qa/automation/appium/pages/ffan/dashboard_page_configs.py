#! /Library/Frameworks/Python.framework/Versions/2.7/bin/python
# -*- coding: utf-8 -*-

import os,sys


class SafariActivityConfigs():

    # 常量命名规则 resource_id指明资源类型是resource id;iv_center_tab view id name;iv指明view类型image view
    # 首页中间摇一摇图标
    resource_id__iv_center_tab__iv = "iv_center_tab";

    #城市text view
    resource_id__tv_city__tv = "tv_city";

    # ffan logo图标
    resource_id__iv_logo__iv = "iv_logo";

    # 更多图标
    resource_id__iv_right_icon__iv = "iv_right_icon";


    # 广场列表按钮resource id
    resource_id_plaza_list_fab = "plaza_list_fab";

    # text指明类型为text label,后面是文字的拼音
    text_aiguangjie = "爱逛街";
    text_huishenghuo = "慧生活";
    text_ffancard = "飞凡卡";
    text_mine = "我的";

    # 搜索框默认字段
    text_quanchengsousuo = "全城搜索";

    def __init__(self):
        pass;

