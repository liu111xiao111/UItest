# -*- coding: utf-8 -*-


class MyFfanMyOrderPageConfigs():
    click_on_button_timeout = "10"

    # "我的订单"
    name_order_all = u"全部订单";
    name_order_film = u"电影娱乐";
    name_order_le_pay = u"乐付买单";
    name_order_parking_payment = u"停车缴费";
    name_daifukuan = u"待付款"
    name_wodedianping = u"我的点评"
    name_keshiyong = u"可使用"
    name_order_details = u"订单详情"



    xpath_order_list = "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[3]"
    xpath_order_details = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]"
    #代付款
    xpath_daifukuan = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[6]/UIAButton[1]"
    xpath_keshiyong = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[6]/UIAButton[2]"
    xpath_wodedianping = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[6]/UIAButton[3]"
    xpath_tuihuotuikuan = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[6]/UIAButton[4]"

    ios_uiautomation_daifukuan_bt = ".tableViews()[0]"

    def __init__(self):
        pass;
