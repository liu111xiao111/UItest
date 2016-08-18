#!/usr/bin/env python
# -*- coding:utf-8 -*-


class PersonalInformationPageConfigs(object):
    '''
    This is a configuration class for PersonalInformationPage class.
    '''

    # Assert view time out
    assert_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    # Personal information title
    resource_id_personal_information_title = "com.wanda.app.wanhui:id/common_title_view_layout_title"

    # Nickname button
    text_nickname_button = u"ffan6140"

    def __init__(self):
        pass
