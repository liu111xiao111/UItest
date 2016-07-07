# -*- coding: utf-8 -*-

from __init__ import *

from com.qa.automation.appium.pages.android.ffan.food_category_page_configs import FoodCategoryPageConfigs
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.api.api import API

FCPC = FoodCategoryPageConfigs()

#   首页点击 美食
class FoodCategoryPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(FoodCategoryPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    '''
        usage: 美食主界面，根据美食种类button入口，检查美食主页面是否加载出来.
    '''
    def validFoodHomePage(self):
        API().assert_view_by_text_android(self.testcase,
                                          self.driver,
                                          self.logger,
                                          FCPC.view_text_tiltle,
                                          FCPC.verify_view_timeout);

    '''
        usage : 进入美食子页面，根据餐饮的textview, 检查找餐饮页面是否加载出来.
    '''
    def validRestaurant(self):
        API().assert_view_by_resourceID_Until(self.testcase,
                                              self.driver,
                                              self.logger,
                                              FCPC.resource_id_tv_restaurant_tv,
                                              FCPC.verify_view_timeout);

    '''
        usage : 进入优惠打折界面，根据餐饮的textview, 检查找优惠页面是否加载出来.
    '''
    def validCoupon(self):
        API().assert_view_by_resourceID_Until(self.testcase,
                                              self.driver,
                                              self.logger,
                                              FCPC.resource_id_tv_restaurant_tv,
                                              FCPC.verify_view_timeout);
    
    '''
        usage: 进入抢券界面，根据餐饮的textview, 检查抢券界面是否加载出来.
    '''
    def validGrabCoupons(self):
        API().assert_view_by_resourceID_Until(self.testcase,
                                              self.driver,
                                              self.logger,
                                              FCPC.resource_id_tv_restaurant_tv,
                                              FCPC.verify_view_timeout);

    '''
        usage: 点击美食主界面的所有入口并验证
    '''
    def validModules(self):
        restaurantList = API().get_views_by_resourceID(self.driver,
                                                       self.logger,
                                                       FCPC.resource_id_bt_restaurant_bt)
        for restaurant in restaurantList:
            restaurant.click()
            self.validRestaurant()
            self.clickBackKey()

    '''
        usage : 点击优惠打折
    '''
    def clickOnCoupon(self):
        API().click_view_by_resourceID(self.testcase,
                                       self.driver,
                                       self.logger,
                                       FCPC.resource_id_bt_coupon_bt);

    '''
        usage : 点击抢券
    '''
    def clickOnGrabCoupons(self):
        API().click_view_by_resourceID(self.testcase,
                                       self.driver,
                                       self.logger,
                                       FCPC.resource_id_bt_grab_bt);


if __name__ == '__main__':
    pass;