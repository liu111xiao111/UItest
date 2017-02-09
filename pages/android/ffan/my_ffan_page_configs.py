# -*- coding: utf-8 -*-

class MyFfanPageConfigs():
    # 常量命名规则 resource_id指明资源类型是resource id;iv_center_tab view id name;iv指明view类型image view
    # 注册 textview
    resource_id_tv_registration_tv = "tv_registration";
    # 登录 textview
    resource_id_tv_login_tv = "tv_login";

    # 设置relativelayout
    resource_id_my_settings_rl = "my_settings";

    # 个人中心 头像旁昵称的ID
    resource_id_txt_user_nick_name_tv = "txt_user_nick_name";

    # 我的票券数量
    resource_id_txt_ticket_number_tv = "com.wanda.app.wanhui:id/unpay_count"

    # text指明类型为text label
    text_my_ffan = u"我的飞凡";
    text_register = "注册";
    text_login = "登录";
    text_welcome_2_ffan = "欢迎来到飞凡";
    text_my_favorite = "我的喜欢";
    text_member_card_bag = "会员卡包";
    text_settins = "设置";
    text_my_queue = u"我的排队";
    text_my_ticket = u"我的票券";
    text_my_order = u"我的订单";
    text_my_bill = u"零花钱";
    text_to_be_paid = u"待付款"
    text_use = u"可使用"
    text_comments = u"我的点评"
    text_return_refund = u"退货退款"
    xpath_to_be_paid = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[4]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]";
    xpath_use = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[4]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]";
    xpath_comments = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[4]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]";
    xpath_return_refund = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[4]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[4]";
    xpath_return_refund_scroll = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[4]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[4]";
    xpath_use_fail = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.wanda.sliding.SlidingLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]"
    text_my_like = u"我的喜欢";
    text_parking_payment = u"停车交费";

    verify_view_timeout = 60

    click_view_timeout = 90
