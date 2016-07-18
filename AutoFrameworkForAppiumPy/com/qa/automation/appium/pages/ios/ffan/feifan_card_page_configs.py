# -*- coding: utf-8 -*-

class FeiFanCardPageConfigs():
    # 常量命名规则 resource_id指明资源类型是resource id;iv_center_tab view id name;iv指明view类型image view

    # 开卡text
    text_tv_open_tv = u"开卡"

    # 飞凡卡　账单
    resource_id_tv_bill_tv = "com.wanda.app.wanhui:id/tv_feifan_change_detail"

    # 零花钱
    resource_id_tv_pocket_money_tv = "com.wanda.app.wanhui:id/tv_feifan_change"
    resource_id_tv_bill_tv = "com.wanda.app.wanhui:id/tv_feifan_change_detail"
    text_integral = u"积分"

    verify_view_timeout = 10
    verify_click_timeout = 10

    # Assert view time out
    assert_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    # Score
    resource_id_score_st = u"积分"

    # Bill
#     xpath_bill_bt = "//UIAApplication[1]/UIAWindow[1]/UIAButton[4]"
#     xpath_bill_bt = "//UIAApplication[1]/UIAWindow[1]/UIAImage[4]"
    xpath_bill_bt = "//UIAApplication[1]/UIAWindow[1]/UIAStaticText[5]"
    resource_id_bill_st = u"账单"

    def __init__(self):
        pass;
