#!/usr/bin/env python
# -*- coding:utf-8 -*-


class MyMembershipCardPackagePageConfigs(object):
    '''
    This is a configuration class for MyMembershipCardPackagePage class.
    '''

    # Assert view time out
    assert_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    # My membership card package title
    resource_id_my_membership_card_package_title = "com.wanda.app.wanhui:id/common_title_view_layout_title"

    # LeHuoKa button
    resource_id_le_huo_ka_button = "com.wanda.app.wanhui:id/rl_card_logo"

    def __init__(self):
        pass
