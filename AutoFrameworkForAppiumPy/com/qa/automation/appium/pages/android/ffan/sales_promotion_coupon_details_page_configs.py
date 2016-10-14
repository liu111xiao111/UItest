# -*- coding: utf-8 -*-


from com.qa.automation.appium.utility.device_info_util import DeviceInfoUtil

class SalesPromotionCouponDetailsPageConfigs():


    # Sales promotion
    #resource_id_tv_coupon_details_tv = "com.wanda.app.wanhui:id/common_title_view_layout_title"

    text_tv_coupon_details = u"免费领取"

    '''if int(DeviceInfoUtil().getBuildVersion().split(".")[0]) < 5:
        text_receive_free_button = u"免费领取 Link"
    else:
        text_receive_free_button = u"免费领取"'''
    text_receive_free_button = u"免费领取"
    text_receive_free_link_button = u"免费领取 Link"
    xpath_get_free_ticket = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.wanda.sliding.SlidingLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.view.View[1]/android.view.View[14]/android.view.View[1]"

    def __init__(self):
        pass;

