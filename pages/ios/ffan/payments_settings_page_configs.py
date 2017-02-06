# -*- coding:utf-8 -*-

class PaymentsSettingsPageConfigs(object):
    '''
    This is a configuration class for PaymentsSettingsPage class.
    '''


    # Assert view time out
    assert_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    # Payments settings title
    name_payments_settings_title_st = u"支付设置"

    # Transaction record button
    name_update_payments_password_st = u"修改支付密码"

    # Small amount password less payments button
    name_small_amount_password_less_payments_st = u"小额免密支付"

    def __init__(self):
        pass
