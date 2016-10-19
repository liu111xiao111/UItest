# -*- coding: utf-8 -*-

from com.qa.automation.appium.pages.ios.ffan.food_category_page_configs import FoodCategoryPageConfigs
from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage


FCPC = FoodCategoryPageConfigs()

class FoodCategoryPage(SuperPage):
    '''
    作者 刘涛
    首页＝>美食汇
    '''

    def __init__(self, testcase, driver, logger):
        super(FoodCategoryPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        navigation = API().validElementByIosUiautomation(driver=self.driver,
                                                         logger=self.logger,uiaString=".navigationBars()[0]")
        API().assertEqual(testCase=self.testcase,
                          logger=self.logger,
                          actualText=navigation.get_attribute("name"),
                          expectText=FoodCategoryPageConfigs.name_food_category_navigation_bar)

    def validModules(self):
        '''
        usage: 点击美食主界面的所有入口并验证
        '''
        restaurantList = API().getElementsByClassName(self.driver,
                                                       self.logger,
                                                       FCPC.resource_id_bt_restaurant_bt)
        for restaurant in restaurantList:
            restaurant.click()
            self.validRestaurant()
            self.clickBackKey()

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

    def validLePay(self):
        '''
        usage: 进入乐付界面，根据餐饮的textview, 检查抢券界面是否加载出来.
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        FCPC.resource_id_tv_restaurant_tv,
                                        FCPC.verify_view_timeout)

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

    def clickOnLePay(self):
        '''
        usage : 点击乐付
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       FCPC.resource_id_bt_pay_bt,
                                       FCPC.click_view_timeout)

if __name__ == '__main__':
    pass;
