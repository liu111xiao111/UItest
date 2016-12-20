# -*- coding: utf-8 -*-

class DashboardPageConfigs():

    """
        *********************************iOS 控件name*****************************

    """

    """
        摇一摇图标name
    """
    name_app_tabbar_shake = "app tabbar shake";

    """
        首页ffan logo图标name
    """
    name_home_title_icon = "home_title_icon"

    '''
        左上角，北京市
    '''
    name_beijing = "北京市"

    """
        爱逛街icon name
    """
    name_app_tabbar_home_normal = 'app_tabbar_home_normal'

    """
        慧生活icon name
    """
    name_app_tabbar_life_normal = "app_tabbar_life_normal"

    """
        飞凡卡icon name
    """
    name_app_tabbar_card_normal = "app_tabbar_card_normal"

    """
        我的icon name
    """
    name_app_tabbar_user_normal = "app_tabbar_user_normal"

    # "购物中心"
    name_shopping_mall = u"购物中心"

    # "停车"
    name_parking = u"停车"

    # "购物"
    name_shopping = u"名店优品"

    # "乐付"
    name_le_pay = u"买单";

    # "品牌街"
    name_brand = u"品牌街";

    # "美食汇"
    name_food = u"美食汇";

    # "优惠"
    name_sales_promotion = "home_activity";

    # "亲子"
    name_child = u"亲子";


    # 全城搜索输入框
    resource_id_tv_search_tv = "全城搜索"

    """
        *********************************iOS text label*****************************

    """
    text_aiguangjie = "爱逛街";
    text_huishenghuo = "慧生活";
    text_ffan_card = "飞凡卡";
    text_my = "我的";
    text_valid_beijing = "北京"

    # Assert view time out
    assert_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 20

    get_timeout = 10

    # Movie button
    resource_id_movie_st = "电影"

    # Stores button
    name_movie_st = "商超"

    # Privilege button
    resource_id_movieprivilege_st = u"优惠"

    # Square module
    xpath_square_module_st = "//UIAApplication[1]/UIAWindow[1]/UIACollectionView[1]/UIACollectionCell[3]/UIACollectionView[1]/UIACollectionCell[1]"

    # Main page
    xpath_main_page = "//UIAApplication[1]/UIAWindow[1]/UIACollectionView[1]"
    xpath_sales_promotion = "//UIAApplication[1]/UIAWindow[1]/UIACollectionView[1]/UIAButton[3]"

    # Switch city
    xpath_city = "//UIAApplication[1]/UIAWindow[1]/UIAStaticText[1]"

    # square
    xpath_guangchang = "//UIAApplication[1]/UIAWindow[1]/UIACollectionView[1]/UIACollectionCell[3]/UIACollectionView[1]/UIACollectionCell[1]/UIAStaticText[1]"

    #摇一摇
    xpath_yaoyiyao = "//UIAApplication[1]/UIAWindow[1]/UIATabBar[1]/UIAButton[1]"

    # Search all
    resource_id_search_all_tv = "全城搜索"

    # Sign in
    name_sign_in_st = u"签到"


    name_activities_deleate_icon = "popUp delete"


    def __init__(self):
        pass;
