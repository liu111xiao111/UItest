# -*- coding: utf-8 -*-

import os, sys


class FeiFanCardBillPageConfigs():
    # 常量命名规则 resource_id指明资源类型是resource id;iv_center_tab view id name;iv指明view类型image view

    # 账号列表
    resource_id_tv_bill_list_tv = "android:id/list"

    # Click button time out
    click_on_button_timeout = 10

    # Filter button
    resource_id_filter_button = "com.wanda.app.wanhui:id/title_settings"

    # text指明类型为text label,后面是文字的拼音

    def __init__(self):
        pass;
