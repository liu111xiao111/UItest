# -*- coding: utf-8 -*-

class MyFfanMyOrderDetailsPageConfigs():
    # "订单详情"页
    name_order_details = u"订单详情";
    xpath_order_number = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIAStaticText[14]"
    xpath_film_order_number = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIAStaticText[5]"
    xpath_le_pay_order_number = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIAStaticText[14]"
    xpath_coupon_number = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIALink[1]/UIAStaticText[1]"
    xpath_payment_order_number = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIAStaticText[14]"

    def __init__(self):
        pass;
