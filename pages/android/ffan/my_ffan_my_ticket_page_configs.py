# -*- coding: utf-8 -*-


class MyFfanMyTicketPageConfigs():
    # "我的票券"
    resource_id_tv_my_ticket_tv = "com.wanda.app.wanhui:id/common_title_view_layout_title"
    resource_id_tv_my_ticket_no_tv = "com.wanda.app.wanhui:id/item_state"
    text_ticket_unused = u"未使用"
    text_ticket_used = u"已使用"
    text_ticket_out_of_date = u"已过期"
    text_ticket_return_refund = u"退货退款"

    # Assert view time out
    assert_view_timeout = 10

    click_view_timeout = 10

    # Coupon code button
    xpath_coupon_code_button = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.wanda.sliding.SlidingLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"

    def __init__(self):
        pass
