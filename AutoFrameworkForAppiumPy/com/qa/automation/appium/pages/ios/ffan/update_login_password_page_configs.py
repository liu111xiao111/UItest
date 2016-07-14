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
    resource_id_update_login_password_title_st = u"修改登录密码"

    # Input the old password
    resource_id_input_old_password = "com.wanda.app.wanhui:id/et_input_old_pwd"
    xpath_input_old_password_stf = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIASecureTextField[1]"

    # Input the new password
    resource_id_input_new_password = "com.wanda.app.wanhui:id/et_input_new_pwd"
    xpath_input_new_password_stf = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIASecureTextField[1]"

    # Input the new password again
    resource_id_input_new_password_again = "com.wanda.app.wanhui:id/et_input_new_pwd_again"
    xpath_input_new_password_again_stf = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[3]/UIASecureTextField[1]"

    # Confirm button
    resource_id_confirm_bt = u"确定"

    def __init__(self):
        pass
