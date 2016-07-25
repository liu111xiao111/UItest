# -*- coding: utf-8 -*-

from com.qa.automation.appium.pages.ios.ffan.square_food_category_page_configs import SquareFoodPageConfigs
from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage

SFPC = SquareFoodPageConfigs()

class SquareFoodPage(SuperPage):
    '''
    作者 刘涛
    首页=>广场=>美食汇
    '''

    def __init__(self, testcase, driver, logger):
        super(SquareFoodPage, self).__init__(testcase,
                                             driver,
                                             logger);

    '''
        usage : 进入找餐厅界面
    '''
    def clickOnFindRestaurant(self):
        API().click_view_by_xpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SFPC.xpath_find_restaurant,
                                  SFPC.verify_assert_timeout)

    '''
        usage : 进入找优惠界面
    '''
    def clickOnFindFavourable(self):
        API().click_view_by_xpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SFPC.xpath_find_favourable,
                                  SFPC.verify_assert_timeout)

    '''
        usage : 进入智能排队界面
    '''
    def clickOnQueue(self):
        API().click_view_by_xpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SFPC.xpath_intelligent_queuing,
                                  SFPC.verify_assert_timeout)
    '''
        usage : 进入帮你选界面
    '''
    def clickOnStochastic(self):
        API().click_view_by_xpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SFPC.xpath_stochastic,
                                  SFPC.verify_assert_timeout)


    '''
        usage : 检查找餐饮页面是否加载出来.
    '''
    def validFindRestaurant(self):
        API().assert_view_by_resourceID_Until(self.testcase,
                                              self.driver,
                                              self.logger,
                                              SFPC.verify_find_restaurant_resourceID,
                                              SFPC.verify_assert_timeout);

    '''
        usage : 检查找优惠页面是否加载出来.
    '''
    def validFindFavourable(self):
        API().assert_view_by_resourceID_Until(self.testcase,
                                              self.driver,
                                              self.logger,
                                              SFPC.verify_find_favourable_resourceID,
                                              SFPC.verify_assert_timeout);

    '''
        usage : 检查智能排队页面是否加载出来.
    '''
    def validQueue(self):
        API().assert_view_by_resourceID_Until(self.testcase,
                                              self.driver,
                                              self.logger,
                                              SFPC.verify_intelligent_queuing_resourceID,
                                              SFPC.verify_assert_timeout);

    '''
        usage : 检查找餐饮页面是否加载出来.
    '''
    def validStochastic(self):
        API().assert_view_by_resourceID_Until(self.testcase,
                                              self.driver,
                                              self.logger,
                                              SFPC.verify_stochastic_resourceID,
                                              SFPC.verify_assert_timeout);

    '''
        usage : 进入广场模块，检查是否加载出来
    '''
    def validSelf(self):
        API().assert_view_by_resourceID_Until(self.testcase,
                                              self.driver,
                                              self.logger,
                                              SFPC.verify_food_home_page_title,
                                              SFPC.verify_assert_timeout);


if __name__ == '__main__':
    pass;