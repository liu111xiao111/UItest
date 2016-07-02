# -*- coding: utf-8 -*-

import os, sys

# sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from time import sleep
import unittest
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.pages.android.ffan.square_indoor_map_page_configs import *
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.pages.android.common.super_page import *

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class SquareIndoorMapPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(SquareIndoorMapPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        '''
        usage : Load "室内地图" page， according to textview in "室内地图", check "室内地图" page whether load correctly.
        '''
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                                      resource_id=SquareIndoorMapPageConfigs.resource_id_indoor_map,
                                                      seconds=18);

	def clickOnFoodMap(self):
        '''
        usage : Click "美食地图" page.
        '''
        API().click_view_by_resourceID(testcase = self.testcase, driver=self.driver,logger=self.logger,resource_id=SquareIndoorMapPageConfigs.resource_id_food_map)

    def validSelfFood(self):
        '''
        usage : Load "美食地图" page.
        '''
        API().assert_view_by_resourceID_Until(testcase = self.testcase, driver = self.driver,logger = self.logger ,
                                                resource_id = SquareIndoorMapPageConfigs.resource_id_food_map,seconds=18);

if __name__ == '__main__':
    pass;