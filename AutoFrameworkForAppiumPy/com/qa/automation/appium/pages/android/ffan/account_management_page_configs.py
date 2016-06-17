#!/usr/bin/env python
# -*- coding:utf-8 -*-



class AccountManagementPageConfigs(object):
    '''
    This is a configuration class for AccountManagement class.
    '''

    # Assert view time out
    assert_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    # Account management title
    resource_id_account_management_title = "com.wanda.app.wanhui:id/common_title_view_layout_title"

    # Change login password button
    text_update_login_password_button = u"修改登录密码";

    def __init__(self):
        pass