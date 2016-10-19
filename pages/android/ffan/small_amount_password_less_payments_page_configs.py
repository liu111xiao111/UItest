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

    # Small amount password-less payment title
    resource_id_square_dynamic_title = "com.wanda.app.wanhui:id/common_title_view_layout_title"

    # Small amount password-less payment switch
    resource_id_small_amount_password_less_payment_switch = "com.wanda.app.wanhui:id/sb_free_password_switch"

    # Choose small amount password-less quota
    text_choose_small_amount_password_less_quota = u"选择支付免密限额（元/日）"

    def __init__(self):
        pass
