# -*- coding: utf-8 -*-

class SquareQueuePageConfigs():
    # "排队取号"
    resource_id_queue = "com.wanda.app.wanhui:id/common_title_view_layout_title"
    resource_id_cancel_queue = "cancel_queue"
    
    class_name_number_of_meals = "android.widget.EditText"
    xpath_get_queue_number = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.wanda.sliding.SlidingLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[2]/android.view.View[1]/android.view.View[2]"
    xpath_cancel_queue = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.wanda.sliding.SlidingLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[2]/android.view.View[2]"
    text_queue_number = u"取号"
    text_cancel_queue = u"取消排队"
    text_get_queue_number = u"一键取号"
    number_of_meals = "5"

    verify_view_text_1 = u"取号成功"
    verify_view_text_2 = u"取号中"
    verify_view_timeout = 10
    verify_input_timeout = 10
    verify_click_timeout = 10

    def __init__(self):
        pass;
