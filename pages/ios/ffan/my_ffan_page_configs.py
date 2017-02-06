# -*- coding: utf-8 -*-

class MyFfanPageConfigs():

    # Click button time out
    click_on_button_timeout = 10

    #验证页面超时
    valid_page_timeout = 10

    # 常量命名规则 resource_id指明资源类型是resource id;iv_center_tab view id name;iv指明view类型image view
    # 注册 textview
    name_tv_registration_tv = "tv_registration";
    # 登录 textview
    name_tv_login_tv = "tv_login";

    # 设置relativelayout
    name_my_settings_rl = "my_settings";

    # 个人中心 头像旁昵称的ID
    name_txt_user_nick_name_tv = "txt_user_nick_name";

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
    text_my_like = u"我的喜欢";
    text_parking_payment = u"停车缴费";
    text_wodefeifantong = u"我的飞凡通"
    text_linghuaqian = u"我的零花钱"
    text_linghuaqianyue = u"零花钱余额"

    xpath_parking_paymeng = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[13]/UIAStaticText[1]"
    xpath_my_ticket_first_item = "//UIAApplication[1]/UIAWindow[1]/UIAImage[1]/UIAImage[2]"
    #我的飞凡通
    xpath_myfeitongtong = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[11]/UIAStaticText[1]"
    #我的零花钱
    xpath_linghuaqian = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]"
    #付款码
    xpath_fukuanma = "// UIAApplication[1] / UIAWindow[1] / UIATableView[1] / UIAButton[1]"

    def __init__(self):
        pass;
