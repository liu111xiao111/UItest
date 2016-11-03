# -*- coding: utf-8 -*-


class LeFuZhangDanPageConfigs():
    xpath_order_status = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[2]"
    text_lefu_pay = u"乐付交易"
    text_calendar_start = u"开始日期"
    text_calendar_end = u"结束日期"
    text_user_defined = u"自定义"
    text_confirm = u"确定"
    text_pay_type = u"交易方式"
    resource_id_type = "com.feifan.bp:id/receipts_pay_type"
    resouce_id_search_date = "com.feifan.bp:id/query_time"

    verify_timeout = 30

    def __init__(self):
        pass;