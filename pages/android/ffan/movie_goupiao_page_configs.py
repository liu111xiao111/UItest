# -*- coding: utf-8 -*-

class moviegoupiaoConfigs():
    # 常量命名规则 resource_id指明资源类型是resource id;iv_center_tab view id name;iv指明view类型image view

        # Movie 选座 button
    text_movie_xuanzuo_button = u"选座"

        # 首页切换城市
    resource_id_iv_chengshi = 'com.wanda.app.wanhui:id/tv_city'

        #切换到安阳市
    resource_id_iv_anyang= 'com.wanda.app.wanhui:id/name'

    text_movie_beijingshi_button = u'北京市'

    text_movie_yingyuan_button = u'影院'

    text_movie_pingpai_button = u'品牌'

    text_movie_hengdian_button = u'横店电影城'


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