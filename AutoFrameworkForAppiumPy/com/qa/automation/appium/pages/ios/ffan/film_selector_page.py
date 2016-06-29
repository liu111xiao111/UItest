# -*- coding: utf-8 -*-

import os, sys

from time import sleep
import unittest
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.pages.ios.common.ios_super_page import *
from com.qa.automation.appium.pages.ios.ffan.film_selector_page_configs import *

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


#
#   电影选择页面,入口:首页 -> 电影
class FilmSelectorPage(IosSuperPage):

    def __init__(self, test_case, driver, logger):
        super(FilmSelectorPage, self).__init__(testcase=test_case, driver=driver, logger=logger);

    """
        验证购物中心页面navigation bar name是否正确
    """
    def valid_self(self):
        navigation_bar = API().find_view_by_class_name_both(driver=self.driver,logger=self.logger,className=FilmSelectorPageConfigs.class_NavigationBar)
        API().assert_equal(test_case=self.testcase,driver=self.driver,logger=self.logger,
                           expect_text=FilmSelectorPageConfigs.name_film_selector_navigation_bar,
                           actual_text=navigation_bar.get_attribute("name"))

if __name__ == '__main__':
    pass;
