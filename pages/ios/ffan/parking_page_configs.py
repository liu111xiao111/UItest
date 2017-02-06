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
    name_not_gps_square = u"没有定位到您当前所在广场"
    name_know_text = u"知道了"
    # Click button time out

    name_add_plate_number = "添加车牌"
    #车牌管理
    name_plate_nmuber_management = "park license manage"
    name_plate_nmuber_management_ch = "车牌管理"
    name_parking_record = "park record"
    name_parking_record_cn = "停车记录"
    name_parking_coupon = "park coupon"
    name_parking_coupon_cn = "停车优惠券"
    name_parking_help = "park help"
    name_parking_help_ch = "停车帮助"
    #附近停车场
    name_nearby_parking = "park right arrow"
    name_nearby_parking_cn = "停车场列表"

    click_on_button_timeout = 10

    name_find_car = "park find car button"

    """
        *********************************iOS 控件 xpath*****************************
    """
    xpath_parking_coupon = "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAStaticText[1]"
    xpath_tingchezhaoche = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[3]/UIAButton[1]"
    xpath_fujintingchechang = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[3]/UIAButton[2]"
    xpath_tingchequan = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[3]/UIAButton[3]"
    xpath_tingchejilu = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[3]/UIAButton[4]"
    xpath_bangzhu = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[3]/UIAButton[5]"
    #停车优惠券
    xpath_parking_coupon = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[3]/UIAButton[4]"

    """
        *********************************iOS 控件 class name*****************************
    """

    def __init__(self):
        pass;
