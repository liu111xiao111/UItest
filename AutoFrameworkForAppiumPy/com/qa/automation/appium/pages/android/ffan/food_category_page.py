# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.food_category_page_configs import FoodCategoryPageConfigs as FCPC


class FoodCategoryPage(SuperPage):
    '''
    作者 刘涛
    首页＝>美食汇
    '''
    def __init__(self, testcase, driver, logger):
        super(FoodCategoryPage, self).__init__(testcase, driver, logger)

    '''
        usage: 美食主界面，根据美食种类button入口，检查美食主页面是否加载出来.
    '''
    def validFoodHomePage(self):
        '''
        usage: 美食主界面，根据美食种类button入口，检查美食主页面是否加载出来.
        '''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  FCPC.view_text_tiltle,
                                  FCPC.verify_view_timeout)

    def validRestaurant(self):
        '''
        usage : 进入美食子页面，根据餐饮的textview, 检查找餐饮页面是否加载出来.
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        FCPC.resource_id_tv_restaurant_tv,
                                        FCPC.verify_view_timeout)

    def validCoupon(self):
        '''
        usage : 进入优惠打折界面，根据餐饮的textview, 检查找优惠页面是否加载出来.
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        FCPC.resource_id_tv_restaurant_tv,
                                        FCPC.verify_view_timeout)

    def validGrabCoupons(self):
        '''
        usage: 进入抢券界面，根据餐饮的textview, 检查抢券界面是否加载出来.
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        FCPC.resource_id_tv_restaurant_tv,
                                        FCPC.verify_view_timeout)

    def validModules(self):
        '''
        usage: 点击美食主界面的所有入口并验证
        '''
        restaurantList = API().getElementsByResourceId(self.testcase,
                                                       self.driver,
                                                       self.logger,
                                                       FCPC.resource_id_bt_restaurant_bt,
                                                       FCPC.verify_view_timeout)
        for restaurant in restaurantList:
            restaurant.click()
            self.validRestaurant()
            self.clickBackKey()

    def clickOnCoupon(self):
        '''
        usage : 点击优惠打折
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       FCPC.resource_id_bt_coupon_bt,
                                       FCPC.click_view_timeout)

    def clickOnGrabCoupons(self):
        '''
        usage : 点击抢券
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       FCPC.resource_id_bt_grab_bt,
                                       FCPC.click_view_timeout)
