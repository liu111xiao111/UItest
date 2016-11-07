# -*- coding: utf-8 -*-


class DingDanGuanLiPageConfigs():
    xpath_order_status = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[2]"
    content_desc_order_status = u"全部状态"
    content_desc_closed_order = u"交易关闭"
    text_order_manager = u"订单管理"

    verify_timeout = 30

    def __init__(self):
        pass;