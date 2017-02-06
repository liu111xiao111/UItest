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
    name_login_bt = "登录"

    # Message centre button
    resource_id_message_centre_button = "com.wanda.app.wanhui:id/image_icon_message_entry"
    xpath_message_centre_bt = "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[2]"

    # Membership card package button
    text_membership_card_package_button = u"会员卡包"
    xpath_membership_card_package_st = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAButton[1]"

    # Nickname
    resource_id_nickname_button = "com.wanda.app.wanhui:id/txt_user_nick_name"
    name_nickname_st = "ffan5905"

    # Settings button
    name_settings_st = u"设置"

    # Login button
    text_login = u"登录"

    # My fei fan card
    text_my_fei_fan_card = u"我的飞凡通"
    name_my_fei_fan_card_st = u"我的飞凡通"

    def __init__(self):
        pass