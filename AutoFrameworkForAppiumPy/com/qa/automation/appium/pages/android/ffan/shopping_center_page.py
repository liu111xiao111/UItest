# -*- coding: utf-8 -*-

import os, sys

from time import sleep
import unittest
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.pages.common.super_page import *
from com.qa.automation.appium.pages.ffan.shopping_center_page_configs import *

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


#
#   购物中心
class ShoppingCenterPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(ShoppingCenterPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    '''
        usage :
    '''

    def validSelf(self):
        API().assert_view_by_resourceID_Until_android(testcase=self.testcase,
                driver=self.driver,
                logger=self.logger,
                resource_id=ShoppingCenterPageConfigs.resource_id_image_zone_logo_iv,
                seconds=90)


if __name__ == '__main__':
    pass;