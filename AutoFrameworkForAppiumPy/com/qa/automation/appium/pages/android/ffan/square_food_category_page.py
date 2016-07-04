# -*- coding: utf-8 -*-

from com.qa.automation.appium.pages.android.ffan.square_food_category_page_configs import SquareFoodPageConfigs
from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage

SFPC = SquareFoodPageConfigs()

'''
    usage : 广场模块，向下滑动美食汇界面
'''
class SquareFoodPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(SquareFoodPage, self).__init__(testcase,
                                             driver,
                                             logger);

    '''
        usage : 进入找餐厅界面
    '''
    def clickOnFindRestaurant(self):
        API().click_view_by_resourceID(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SFPC.resource_id_ll_find_restaurant_id,
                                       SFPC.click_child_module_timeout)

    '''
        usage : 进入找优惠界面
    '''
    def clickOnFindFavourable(self):
        API().click_view_by_resourceID(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SFPC.resource_id_ll_find_favourable_id,
                                       SFPC.click_child_module_timeout)

    '''
        usage : 进入智能排队界面
    '''
    def clickOnQueue(self):
        API().click_view_by_resourceID(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SFPC.resource_id_ll_intelligent_queuing_id,
                                       SFPC.click_child_module_timeout)

    '''
        usage : 进入帮你选界面
    '''
    def clickOnStochastic(self):
        API().click_view_by_resourceID(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SFPC.resource_id_ll_stochastic_id,
                                       SFPC.click_child_module_timeout)


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
                                              SFPC.verify_food_home_page_resourceID,
                                              SFPC.verify_assert_timeout);


if __name__ == '__main__':
    pass;