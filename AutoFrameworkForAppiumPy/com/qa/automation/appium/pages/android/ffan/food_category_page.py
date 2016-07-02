# -*- coding: utf-8 -*-

import os, sys

# sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from time import sleep
import unittest
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.pages.android.ffan.food_category_page_configs import *
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.pages.android.common.super_page import *

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


#   首页点击 美食
class FoodCategoryPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        self.a = 12;
        super(FoodCategoryPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    '''
        usage : 进入美食页面，根据餐饮的textview,检查找餐饮页面是否加载出来.
    '''

    def validFindRestaurant(self):
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                                      resource_id=FoodCategoryPageConfigs.resource_id_tv_restaurant_tv,
                                                      seconds=18);

    '''
        usage : 进入美食页面，根据餐饮的textview,检查找优惠页面是否加载出来.
    '''

    def validFindCoupon(self):
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                                      resource_id=FoodCategoryPageConfigs.resource_id_tv_restaurant_tv,
                                                      seconds=18);

    '''
        usage : 点击找优惠
    '''

    def clickOnFindCoupon(self):
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                               resource_id=FoodCategoryPageConfigs.resource_id_bt_find_coupon_bt);

    '''
        usage : 点击找餐厅
    '''

    def clickOnFindRestaurant(self):
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                               resource_id=FoodCategoryPageConfigs.resource_id_bt_find_restaurant_bt);


if __name__ == '__main__':
    pass;