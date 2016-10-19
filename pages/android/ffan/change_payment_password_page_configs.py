#!/usr/bin/env python
# -*- coding:utf-8 -*-


class ChangePaymentPasswordPageConfigs(object):
    '''
    This is a configuration class for ChangePaymentPasswordPage class.
    '''


    # Assert view time out
    assert_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    resource_id_change_payment_password_title = "com.wanda.app.wanhui:id/common_title_view_layout_title"
    resource_id_change_payment_password = "com.wanda.app.wanhui:id/et_password_content"
    string_ori_payment_password = "161014"
    string_new_payment_password = "161014"
    # 修改支付密码
    text_change_payment_passwork = u"修改支付密码"
    text_complete_btn = u"完成"

    def __init__(self):
        pass
