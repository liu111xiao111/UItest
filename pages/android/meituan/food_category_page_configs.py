# -*- coding: utf-8 -*-

class FoodCategoryPageConfigs():
    # 常量命名规则 resource_id指明资源类型是resource id;iv_center_tab view id name;iv指明view类型image view

    # 餐厅
    resource_id_bt_restaurant_bt = "com.wanda.app.wanhui:id/food_home_gridview_item"
    # 优惠打折
    resource_id_bt_coupon_bt = "com.wanda.app.wanhui:id/coupon_campaign_container"
    # 抢券
    resource_id_bt_grab_bt = "com.wanda.app.wanhui:id/food_home_coupon"
    # 乐付
    resource_id_bt_pay_bt = "com.wanda.app.wanhui:id/pic"
    xpath_maidan = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.wanda.sliding.SlidingLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]"

    resource_id_tv_restaurant_tv = "com.wanda.app.wanhui:id/multiple_headers_dropdown_listview_header_item_text"

    # text指明类型为text label,后面是文字的拼音

    view_text_tiltle = u"自助餐"

    verify_view_timeout = 90
    click_view_timeout = 90

    def __init__(self):
        pass
