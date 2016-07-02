# -*- coding: utf-8 -*-

import os, sys

from time import sleep
import unittest
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.pages.common.super_page import *
from com.qa.automation.appium.pages.ffan.love_shopping_page_configs import *

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

"""
    购物中心页面配置项
"""
class ShoppingCenterPageConfigs(SuperPage):

    # 购物中心列表对应的image logo
    resource_id_image_zone_logo_iv = "image_zone_logo";


if __name__ == '__main__':
    pass;
