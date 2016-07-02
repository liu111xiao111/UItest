# -*- coding:utf-8 -*-

class MyFeiFanCardPageConfigs(object):
    '''
    This is a configuration class for MyFeiFanCardPage class.
    '''


    # Assert view time out
    assert_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    # My Fei fan card title
    resource_id_my_fei_fan_card_title = "com.wanda.app.wanhui:id/common_title_view_layout_title"

    # Transaction record button
    text_transaction_record_button = u"交易记录"

    # Payments settings button
    text_payments_settings_button = u"支付设置"

    def __init__(self):
        pass
