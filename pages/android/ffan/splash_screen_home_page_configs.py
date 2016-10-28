#!/usr/bin/env python
# -*- coding:utf-8 -*-


class SplashScreenHomePageConfigs(object):
    '''
    This is a configuration class for SplashScreenHomePage class.
    '''

    # Assert view time out
    assert_view_timeout = 20

    # Verify view time out
    verify_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Skip button
    resource_id_skip_button = "com.wanda.app.wanhui:id/tv_skip"

    def __init__(self):
        pass