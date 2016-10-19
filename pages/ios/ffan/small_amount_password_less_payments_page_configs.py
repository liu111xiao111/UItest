#!/usr/bin/env python
# -*- coding:utf-8 -*-


class SmallAmountPasswordLessPaymentsPageConfigs(object):
    '''
    This is a configuration class for SmallAmountPasswordLessPaymentsPage class.
    '''


    # Assert view time out
    assert_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    # Find view time out
    find_view_timeout = 10

    # Small amount password-less payments title
    resource_id_small_amount_password_less_payments_title_st = u"小额免密支付"

    # Small amount password-less payments switch
    resource_id_small_amount_password_less_payment_switch = "com.wanda.app.wanhui:id/sb_free_password_switch"
    xpath_small_amount_password_less_payments_sc = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIASwitch[1]"

    # Choose small amount password-less quota
    text_choose_small_amount_password_less_quota = u"选择支付免密限额（元/日）"
    resource_id_choose_small_amount_password_less_quota_st = u"选择支付免密限额（元/日）"

    def __init__(self):
        pass
