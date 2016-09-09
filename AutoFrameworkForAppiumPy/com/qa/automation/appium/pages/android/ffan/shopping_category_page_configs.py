# -*- coding: utf-8 -*-


class ShoppingCategoryPageConfigs():

    # 常量命名规则 resource_id指明资源类型是resource id;iv_center_tab view id name;iv指明view类型image view

    #  "商品" page
    text_goods = u"购物";
    resource_id_tv_goods_details_tv = "com.wanda.app.wanhui:id/bt_gooods_item2"
    xpath_goods_details = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.wanda.sliding.SlidingLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[4]/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]"
    resource_id_tv_shopping_trolley_tv = "com.wanda.app.wanhui:id/shopping_cart_titile_bt"
    
    def __init__(self):
        pass;

