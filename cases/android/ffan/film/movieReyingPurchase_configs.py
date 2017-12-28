# -*- coding: utf-8 -*-

class dianyingReyingGoupiao_configs():
    # 常量命名规则 resource_id指明资源类型是resource id;iv_center_tab view id name;iv指明view类型image view

    # Click button time out
    click_on_button_timeout = 10
    assert_button_timeout = 10

    # Case 层的使用开发状态 1 /线上状态 0
    is_dev = 1

    # 切换城市，首选芜湖
    resource_id_city_switch_button = "com.wanda.app.wanhui:id/tv_city"
    resource_id_city_seek = "com.wanda.app.wanhui:id/et_search"
    city_text = u"芜湖市"
    resource_id_city_result = "com.wanda.app.wanhui:id/civ_common_item_city"

    # 电影首页，影片icon
    resource_id_movies_icon = "com.wanda.app.wanhui:id/movie_left_title_button"
    # 电影首页，选座购票
    resource_id_select_button = "com.wanda.app.wanhui:id/tv_buy_ticket"

    # 影城列表，影城title
    resource_id_cinema = "com.wanda.app.wanhui:id/common_title_view_layout_title"
    # 影城列表，某一影城名称
    resource_id_cinema_name = "com.wanda.app.wanhui:id/tv_name"

    # 场次列表页title
    resource_id_changci_title = "com.wanda.app.wanhui:id/common_title_view_layout_title"
    # 场次列表页，影片轮播背景
    resource_id_movie_circleBG = "com.wanda.app.wanhui:id/rl_movie_gallery_bg"
    # 场次列表页，点击选座
    resource_id_select_buy = "com.wanda.app.wanhui:id/buy_button"

    # 座位图title
    resource_id_seat_title = "com.wanda.app.wanhui:id/common_title_view_layout_title"
    # 座位图，影城信息
    resource_id_movie_seat_info = "com.wanda.app.wanhui:id/movie_seat_info_container"
    # 座位图，选择座位
    resource_id_seat_select = "com.wanda.app.wanhui:id/ssv_movie_select_seat"
    # 座位图，点击选好了
    resource_id_seat_submit = "com.wanda.app.wanhui:id/buy_movie_select_seat"
    # 座位图，已选座位的总价
    resource_id_seat_price = "com.wanda.app.wanhui:id/price_movie_seat_select"

    # 确认订单页，影城影片信息
    resource_id_confirm_goods = "com.wanda.app.wanhui:id/movie_confirm_goods_detail"
    # 确认订单页，使用优惠区域
    resource_id_preferental = "com.wanda.app.wanhui:id/rl_preferential_detail"
    # 确认订单页，点击提交订单
    resource_id_order_submit = "com.wanda.app.wanhui:id/tv_movie_confirm_in_real_pay"

    # 待支付页，订单号
    resource_id_order_number = "com.wanda.app.wanhui:id/tv_order_number"
    # 待支付页，确认支付按钮
    resource_id_confirm_button = "com.wanda.app.wanhui:id/tv_confirm"

    def __init__(self):
        pass;
