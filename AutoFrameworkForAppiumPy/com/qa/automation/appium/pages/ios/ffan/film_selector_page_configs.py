# -*- coding: utf-8 -*-

import os, sys

from time import sleep
import unittest
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.pages.ios.common.ios_super_page import *

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

"""
    电影选择页面配置类
"""
class FilmSelectorPageConfigs(IosSuperPage):

    """
        *********************************iOS 控件name*****************************

    """
    name_film_selector_navigation_bar = "电影"

    """
        *********************************iOS 控件 xpath*****************************
    """

    """
        *********************************iOS 控件 class name*****************************
    """
    class_NavigationBar = "UIANavigationBar"

if __name__ == '__main__':
    pass;
