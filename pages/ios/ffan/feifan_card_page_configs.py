# -*- coding: utf-8 -*-

class FeiFanCardPageConfigs():
    # 常量命名规则 resource_id指明资源类型是resource id;iv_center_tab view id name;iv指明view类型image view

    # 开卡text
    text_tv_open_tv = u"市民/公交卡"

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
    ios_uiautomation_bill_bt = ".buttons()[3]"

    name_linghuaqian_chongzhi = u"零花钱充值"
    name_linghuaqian_tixian = u"零花钱提现"
    name_jifen = u"积分"
    name_gongjiaoka = u"市民/公交卡"
    name_feifandai = u"飞凡贷"
    name_kuaiyihua = u"快易花"
    name_kuaililai = u"快利来"
    name_yuyuelicai = u"预约理财"

    #资源位
    xpath_ziyuanwei = "//UIAApplication[1]/UIAWindow[1]/UIACollectionView[1]/UIACollectionView[1]"
    #资源位page
    xpath_ziyuanwei_page = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]"

    def __init__(self):
        pass;
