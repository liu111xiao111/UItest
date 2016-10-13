#!/usr/bin/env python
# -*- coding:utf-8 -*-


class XianchangyaoPageConfigs(object):
    # Assert view time out
    assert_view_timeout = 10
    click_on_button_timeout = 10

    '''
        xpath
    '''
    #标题栏xpath
    xpath_title = "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAStaticText[1]"

    #点击摇动图标xpath
    xpath_shaking_image = "//UIAApplication[1]/UIAWindow[1]/UIAButton[1]"


    #现场摇结果
    xpath_shaking_result = "//UIAApplication[1]/UIAWindow[1]/UIAStaticText[1]"

    def __init__(self):
        pass
