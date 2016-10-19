# -*- coding: utf-8 -*-

class FeiFanCardPageConfigs():
    # 常量命名规则 resource_id指明资源类型是resource id;iv_center_tab view id name;iv指明view类型image view

    # 开卡text
    text_tv_open_tv = u"市民/公交卡"

    # 飞凡通 付款
    resource_id_tv_payment_tv = "com.wanda.app.wanhui:id/tv_payment_code"
    # 飞凡通 卡管家
    resource_id_tv_card_manager_tv = "com.wanda.app.wanhui:id/tv_bank_card"
    # 飞凡通 零花钱
    resource_id_tv_charge_tv = "com.wanda.app.wanhui:id/tv_feifan_change"
    # 飞凡卡　账单
    resource_id_tv_bill_tv = "com.wanda.app.wanhui:id/tv_feifan_change_detail"
    # 飞凡卡　扫码图标
    resource_id_tv_code_icon_tv = "com.wanda.app.wanhui:id/iv_right_icon"
    # 飞凡卡 付款码
    text_tv_payment_code_tv = u"付    款"

    # 零花钱
    resource_id_tv_pocket_money_tv = "com.wanda.app.wanhui:id/tv_feifan_change"
    resource_id_tv_bill_tv = "com.wanda.app.wanhui:id/tv_feifan_change_detail"
    text_integral = u"积分"

    verify_view_timeout = 90
    verify_click_timeout = 90

    def __init__(self):
        pass;
