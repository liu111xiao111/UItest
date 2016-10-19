#!/usr/bin/env python
# -*- coding:utf-8 -*-


class PaymentPasswordSettingPageConfigs(object):
    '''
    This is a configuration class for SPaymentPasswordSettingPage class.
    '''


    # Assert view time out
    assert_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    resource_id_payment_password_title = "com.wanda.app.wanhui:id/common_title_view_layout_title"
    # 修改支付密码
    text_change_payment_passwork = u"修改支付密码"

    def __init__(self):
        pass
