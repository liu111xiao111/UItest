# -*- coding: utf-8 -*-

class LePayPageConfigs():

    """
        *********************************iOS 控件name*****************************

    """
    # 标题"乐付买单"
    name_le_pay_navigation_bar = u"买单"
    # 商品活动详情"乐付买单"
    # xpath_le_pay = "//UIAApplication[1]/UIAWindow[1]/UIATableView[2]/UIATableCell[1]/UIAButton[1]"
    xpath_le_pay = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAButton[1]"

    xpath_sum_of_consumption = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATextField[1]"
    sum_of_consumption = "10"
    xpath_confirm_purchase = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIAButton[1]"
    xpath_confirm_cancel = "//UIAApplication[1]/UIAWindow[4]/UIAAlert[1]/UIACollectionView[1]/UIACollectionCell[1]"

    """
        *********************************iOS 控件 xpath*****************************
    """

    """
        *********************************iOS 控件 class name*****************************
    """

    def __init__(self):
        pass;
