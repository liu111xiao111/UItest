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
    resource_id_my_fei_fan_card_title_st = u"我的飞凡通"

    # Transaction record button
    resource_id_transaction_record_st = u"交易记录"

    # Payments settings button
    resource_id_payments_settings_st = u"支付设置"

    def __init__(self):
        pass
