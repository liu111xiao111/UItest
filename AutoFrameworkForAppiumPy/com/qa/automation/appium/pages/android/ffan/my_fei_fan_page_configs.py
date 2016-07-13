# -*- coding:utf-8 -*-

class MyFeiFanPageConfigs(object):
    '''
    This is a configuration class for MyFeiFanPage class.
    '''

    # Assert view time out
    assert_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    # My FeiFan title
    resource_id_my_fei_fan_title = "com.wanda.app.wanhui:id/txt_title"

    # Login button
    resource_id_login_button = "com.wanda.app.wanhui:id/tv_login"

    # Message centre button
    resource_id_message_centre_button = "layout_title_right" #"com.wanda.app.wanhui:id/image_icon_message_entry" image_icon_message_entry有多个重复控件

    # Membership card package button
    text_membership_card_package_button = u"会员卡包"

    # Nickname button
    resource_id_nickname_button = "com.wanda.app.wanhui:id/txt_user_nick_name"

    # Settings button
    text_settings = u"设置";

    # Login button
    text_login = u"登录"

    # My fei fan card
    text_my_fei_fan_card = u"我的飞凡卡"

    def __init__(self):
        pass