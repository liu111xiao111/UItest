# -*- coding: utf-8 -*-


class ParkingCategoryPageConfigs():
    # 常量命名规则 resource_id指明资源类型是resource id;iv_center_tab view id name;iv指明view类型image view

    #  附件停车场
    resource_id_tv_parking_lot_tv = "com.wanda.app.wanhui:id/parking_image_near_park";
    #  停车
    resource_id_tv_parking_tv = "com.wanda.app.wanhui:id/common_title_view_layout_title";
    #  停车交费
    resource_id_tv_parking_payment_tv = "com.wanda.app.wanhui:id/parking_image_pay";
    text_add_license_plate = u"添加车牌"
    xpath_add_license_plate = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.wanda.sliding.SlidingLayout[1]/android.view.View[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ScrollView[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]"

    def __init__(self):
        pass;
