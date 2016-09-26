# -*- coding: utf-8 -*-


class ParkingPageConfigs():

    """
        *********************************iOS 控件name*****************************

    """
    name_parking_navigation_bar = "停车"
    # 停车交费
    name_parking_payment = "停车交费"
    name_zhaoche = "反向寻车"
    name_fujintingche = "停车场列表"
    name_tingchequan = "停车优惠券"
    name_help = "停车帮助"
    name_tingchejilu = "停车记录"
    
    name_zhaoche_yanzheng = u""
    
    # Click button time out
    click_on_button_timeout = 10

    """
        *********************************iOS 控件 xpath*****************************
    """
    
    xpath_tingchezhaoche = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[3]/UIAButton[1]"
    xpath_fujintingchechang = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[3]/UIAButton[2]"
    xpath_tingchequan = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[3]/UIAButton[3]"
    xpath_tingchejilu = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[3]/UIAButton[4]"
    xpath_bangzhu = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[3]/UIAButton[5]"

    """
        *********************************iOS 控件 class name*****************************
    """

    def __init__(self):
        pass;
