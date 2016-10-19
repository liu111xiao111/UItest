#!/usr/bin/env python
# -*- coding:utf-8 -*-


class ActivityDetailsPageConfigs(object):
    '''
    This is a configuration class for ActivityDetailsPage class.
    '''

    # Assert view time out
    assert_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    # Activity details title
    resource_id_activity_details_title_st = u"活动详情"

    # Sharing button
    xpath_sharing_bt = "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[3]"

    def __init__(self):
        pass
