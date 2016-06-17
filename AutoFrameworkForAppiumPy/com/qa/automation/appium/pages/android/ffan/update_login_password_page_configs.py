#!/usr/bin/env python
# -*- coding:utf-8 -*-


class UpdateLoginPasswordPageConfigs(object):
    '''
    This is a configuration class for UpdateLoginPassword class.
    '''


    # Assert view time out
    assert_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    # Update login password title
    resource_id_update_login_password_title = "com.wanda.app.wanhui:id/common_title_view_layout_title"

    # Input the old password
    resource_id_input_old_password = "com.wanda.app.wanhui:id/et_input_old_pwd"

    # Input the new password
    resource_id_input_new_password = "com.wanda.app.wanhui:id/et_input_new_pwd"

    # Input the new password again
    resource_id_input_new_password_again = "com.wanda.app.wanhui:id/et_input_new_pwd_again"

    # Confirm button
    resource_id_confirm_button = "com.wanda.app.wanhui:id/btn_ok"

    def __init__(self):
        pass
