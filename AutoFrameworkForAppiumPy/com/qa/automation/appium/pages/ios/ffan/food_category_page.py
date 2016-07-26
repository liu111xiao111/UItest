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
        navigation = API().validElementByIosUiautomation(driver=self.driver,logger=self.logger,uia_string=".navigationBars()[0]")
        API().assertEqual(testCase=self.testcase,
                          logger=self.logger,
                          actualText=navigation.get_attribute("name"),
                          expectText=FoodCategoryPageConfigs.name_food_category_navigation_bar)

    def validModules(self):
        '''
        usage: 点击美食主界面的所有入口并验证
        '''
        restaurantList = API().get_views_by_resourceID(self.driver,
                                                       self.logger,
                                                       FCPC.resource_id_bt_restaurant_bt)
        for restaurant in restaurantList:
            restaurant.click()
            self.validRestaurant()
            self.clickBackKey()

if __name__ == '__main__':
    pass;
