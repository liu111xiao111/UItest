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
    resource_id_my_fei_fan_title_st = "我的飞凡"

    # Login button
    resource_id_login_button = "com.wanda.app.wanhui:id/tv_login"
    resource_id_login_bt = "登录"

    # Message centre button
    resource_id_message_centre_button = "com.wanda.app.wanhui:id/image_icon_message_entry"

    # Membership card package button
    text_membership_card_package_button = u"会员卡包"

    # Nickname
    resource_id_nickname_button = "com.wanda.app.wanhui:id/txt_user_nick_name"
    resource_id_nickname_st = "ffan8742"

    # Settings button
    resource_id_settings_st = u"设置"

    # Login button
    text_login = u"登录"

    # My fei fan card
    text_my_fei_fan_card = u"我的飞凡卡"

    def __init__(self):
        pass