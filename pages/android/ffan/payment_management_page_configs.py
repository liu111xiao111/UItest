#!/usr/bin/env python
# -*- coding:utf-8 -*-

class PaymentManagementPageConfigs(object):
    '''
    This is a configuration class for AccountManagement class.
    '''

    # Assert view time out
    assert_view_timeout = 90

    # Click button time out
    click_on_button_timeout = 120

    # Account management title
    resource_id_payment_management_title = "com.wanda.app.wanhui:id/common_title_view_layout_title"

    # Small amount password-less payment switch
    resource_id_small_amount_password_less_payment_switch = "com.wanda.app.wanhui:id/sb_free_password_switch"

    # Change login password button
    text_update_payment_password_button = u"修改支付密码";

    # Change login password button
    text_no_password_payment_button = u"免密支付";
    resource_no_password_id = "com.wanda.app.wanhui:id/minor_text"

    # 支付密码管理
    text_payment_code_setting = u"支付密码管理"

    def __init__(self):
        pass