# -*- coding: utf-8 -*-

import os, sys

# sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from time import sleep
import unittest
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.pages.ios.ffan.parent_children_page_configs import *
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.pages.ios.common.ios_super_page import *

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


#   首页 亲子
class ParentChildrenPage(IosSuperPage):

    def __init__(self, testcase, driver, logger):
        super(ParentChildrenPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        navigation = API().find_view_by_uia_string_until_ios(driver=self.driver,logger=self.logger,uia_string=".navigationBars()[0]")
        API().assert_equal(test_case=self.testcase,driver=self.driver,logger=self.logger,
                           actual_text=navigation.get_attribute("name"),
                           expect_text=ParentChildrenPageConfigs.name_navagation_bar)


if __name__ == '__main__':
    pass;
