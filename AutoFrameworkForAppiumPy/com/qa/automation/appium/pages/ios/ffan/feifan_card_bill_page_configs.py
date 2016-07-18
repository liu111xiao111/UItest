# -*- coding: utf-8 -*-

class FeiFanCardBillPageConfigs():
    # 常量命名规则 resource_id指明资源类型是resource id;iv_center_tab view id name;iv指明view类型image view

    # 账号列表
    resource_id_tv_bill_list_tv = "android:id/list"

    # Assert view time out
    assert_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    # Filter button
    resource_id_filter_bt = u"筛选"

    # Pocket money bill
    resource_id_pocket_money_bill_st = u"零花钱账单"

    def __init__(self):
        pass;
