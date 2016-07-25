# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.square_food_category_page_configs import SquareFoodPageConfigs as SFPC


class SquareFoodPage(SuperPage):
    '''
    作者 刘涛
    首页=>广场=>美食汇
    '''
    def __init__(self, testcase, driver, logger):
        super(SquareFoodPage, self).__init__(testcase, driver, logger);

    def clickOnFindRestaurant(self):
        '''
        usage : 进入找餐厅界面
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SFPC.resource_id_ll_find_restaurant_id,
                                       SFPC.click_child_module_timeout)

    def clickOnFindFavourable(self):
        '''
        usage : 进入找优惠界面
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SFPC.resource_id_ll_find_favourable_id,
                                       SFPC.click_child_module_timeout)

    def clickOnQueue(self):
        '''
        usage : 进入智能排队界面
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SFPC.resource_id_ll_intelligent_queuing_id,
                                       SFPC.click_child_module_timeout)

    def clickOnStochastic(self):
        '''
        usage : 进入帮你选界面
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SFPC.resource_id_ll_stochastic_id,
                                       SFPC.click_child_module_timeout)

    def validFindRestaurant(self):
        '''
        usage : 检查找餐饮页面是否加载出来.
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SFPC.verify_find_restaurant_resourceID,
                                        SFPC.verify_assert_timeout)

    def validFindFavourable(self):
        '''
        usage : 检查找优惠页面是否加载出来.
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SFPC.verify_find_favourable_resourceID,
                                        SFPC.verify_assert_timeout)

    def validQueue(self):
        '''
        usage : 检查智能排队页面是否加载出来.
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SFPC.verify_intelligent_queuing_resourceID,
                                        SFPC.verify_assert_timeout)

    def validStochastic(self):
        '''
        usage : 检查找餐饮页面是否加载出来.
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SFPC.verify_stochastic_resourceID,
                                        SFPC.verify_assert_timeout)

    def validSelf(self):
        '''
        usage : 进入广场模块，检查是否加载出来
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SFPC.verify_food_home_page_resourceID,
                                        SFPC.verify_assert_timeout)
