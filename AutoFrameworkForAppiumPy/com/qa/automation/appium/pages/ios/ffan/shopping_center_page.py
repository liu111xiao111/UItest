# -*- coding: utf-8 -*-

import os, sys

from time import sleep
import unittest
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.pages.ios.common.ios_super_page import *
from com.qa.automation.appium.pages.ios.ffan.shopping_center_page_configs import *

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


#
#   购物中心页面
class ShoppingCenterPage(IosSuperPage):

    def __init__(self, testcase, driver, logger):
        super(ShoppingCenterPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    """
        验证购物中心页面navigation bar name是否正确
    """
    def validSelf(self):
        self.logger.d("shopping center navigation bar name is %s",ShoppingCenterPageConfigs.name_shopping_center_navigation_bar)
        API().assert_view_by_resourceID_Until(testcase=self.testcase,
                                                      driver=self.driver,
                                                      logger=self.logger,
                                                      resource_id=ShoppingCenterPageConfigs.name_shopping_center_navigation_bar,
                                                      seconds=90)


if __name__ == '__main__':
    pass;
