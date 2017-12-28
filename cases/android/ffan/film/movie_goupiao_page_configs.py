# -*- coding: utf-8 -*-

class moviegoupiaoConfigs():
    # 常量命名规则 resource_id指明资源类型是resource id;iv_center_tab view id name;iv指明view类型image view

        # Movie 选座 button
    text_movie_xuanzuo_button = u"选座"

        # 首页切换城市
    resource_id_iv_chengshi = 'com.wanda.app.wanhui:id/tv_city'

    resource_id_iv_sousuochengshi = 'com.wanda.app.wanhui:id/et_search'

    chengshi_name = u'包头'

    text_baotoushi = u'包头市'

    resource_id_iv_xuanzechengshi = 'com.wanda.app.wanhui:id/civ_common_item_city'
        #切换到安阳市
    resource_id_iv_anyang= 'com.wanda.app.wanhui:id/name'

    text_movie_beijingshi_button = u'北京市'

    text_movie_yingyuan_button = u'影院'

    resource_id_iv_fanhuishouye = 'com.wanda.app.wanhui:id/movie_title_left_arrow'

    text_movie_pingpai_button = u'品牌'

    text_movie_hengdian_button = u'横店电影城'

    text_movie_qita_button = u'其它'
    
    
    
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

    assert_button_timeout = 60

    # 确认订单页，影城影片信息
    resource_id_confirm_goods = "com.wanda.app.wanhui:id/movie_confirm_goods_detail"

    text_movie_quanyeyingyuan_button = u'劝业影院'


        # Movie 列表的价格 button
    resource_id_iv_yingyuan_jiage='com.wanda.app.wanhui:id/tv_price'

        # 影院详情，选座/特惠按钮，跳转下单流程
    resource_id_iv_buy='com.wanda.app.wanhui:id/buy_button'

        # 选座页面，选好了按钮
    resource_id_iv_xuanhaole = 'com.wanda.app.wanhui:id/buy_movie_select_seat'

        #点击提交订单按钮
    resource_id_iv_tijiaodingdan = 'com.wanda.app.wanhui:id/tv_movie_confirm_in_real_pay'

    resource_id_iv_xuanzuo = 'com.wanda.app.wanhui:id/ssv_movie_select_seat'

    resource_id_iv_fanhui = 'com.wanda.app.wanhui:id/common_title_view_layout_left_arrow'


    resource_id_iv_dingdanqueren = 'com.wanda.app.wanhui:id/common_title_view_layout_title'

    click_on_button_timeout = 60


    def __init__(self):
        pass;