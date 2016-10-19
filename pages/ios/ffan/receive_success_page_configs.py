#!/usr/bin/env python
# -*- coding:utf-8 -*-


class ReceiveSuccessPageConfigs(object):
    '''
    This is a configuration class for ReceiveSuccessPage class.
    '''


    # Assert view time out
    assert_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    # Receive success title
    resource_id_recieve_success_title = "com.wanda.app.wanhui:id/common_title_view_layout_title"
    
    text_receive_success = "领取成功"
    
    content_desc_limit_dialog_text = "您已经超出了限制，每个用户每天只能领取1次"

    def __init__(self):
        pass
