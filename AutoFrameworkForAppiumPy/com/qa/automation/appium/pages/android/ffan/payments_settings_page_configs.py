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
    resource_id_payments_settings_title = "com.wanda.app.wanhui:id/common_title_view_layout_title"

    # Transaction record button
    text_update_payments_password_button = u"修改支付密码"

    # Small amount password less payments button
    text_small_amount_password_less_payments_button = u"小额免密支付"

    def __init__(self):
        pass
