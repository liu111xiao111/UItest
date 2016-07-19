# -*- coding: utf-8 -*-

class SquareQueuePageConfigs():
    # "排队取号"
    resource_id_queue = u"排队取号"
    resource_id_cancel_queue = "cancel_queue"

    xpath_number_of_meals = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIATextField[1]"
    xpath_get_queue_number = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIALink[2]"
    xpath_cancel_queue = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIALink[2]"
    text_queue_number = u"取号"
    text_cancel_queue = u"取消排队"
    number_of_meals = "5"

    xpath_view_text = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAWebView[1]/UIAStaticText[7]"
    verify_view_text = u"取号成功"
    verify_view_timeout = 10
    verify_input_timeout = 10
    verify_click_timeout = 10

    def __init__(self):
        pass;
