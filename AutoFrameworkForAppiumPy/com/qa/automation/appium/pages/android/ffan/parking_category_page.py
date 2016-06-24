# -*- coding: utf-8 -*-

import os, sys

# sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from time import sleep
import unittest
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.pages.android.ffan.parking_category_page_configs import *
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.pages.android.common.super_page import *

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


#   首页点击 停车
class ParkingCategoryPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        self.a = 12;
        super(ParkingCategoryPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        '''
        usage : Load "停车" page
        '''
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                                      resource_id=ParkingCategoryPageConfigs.resource_id_tv_parking_tv,
                                                      seconds=18);

    def clickOnParkingLot(self):
        '''
        usage : Click "附近停车场"， load "停车场列表" page
        '''
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                               resource_id=ParkingCategoryPageConfigs.resource_id_tv_parking_lot_tv);


if __name__ == '__main__':
    pass;
