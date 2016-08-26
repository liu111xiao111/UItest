# -*- coding: utf-8 -*-


class RecommendDetailsCategoryPageConfigs():

    # 常量命名规则 resource_id指明资源类型是resource id;iv_center_tab view id name;iv指明view类型image view

    #  推荐&品牌 details page
    resource_id_tv_recommend_details_tv = "com.wanda.app.wanhui:id/common_title_view_layout_title"
    resource_id_tv_brand_details_tv = "com.wanda.app.wanhui:id/common_title_view_layout_title"
    resource_id_tv_subscriber_tv = "com.wanda.app.wanhui:id/iv_approval"
    xpath_recommend_subscriber = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.wanda.sliding.SlidingLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.view.View[1]/android.view.View[81]/android.widget.Image[1]"
    desc_like_button = "heartSelectNo@2x"
    desc_unlike_button = "heartSelect@2x"

    def __init__(self):
        pass;

