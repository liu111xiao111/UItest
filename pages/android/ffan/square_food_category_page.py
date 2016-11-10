# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.square_food_category_page_configs import SquareFoodPageConfigs as SFPC
from api.logger import logger
from pages.logger import logger


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
        logger.info("Click 找餐厅 begin")
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SFPC.resource_id_ll_find_restaurant_id,
                                       SFPC.click_child_module_timeout)
        logger.info("Click 找餐厅 end")

    def clickOnFindFavourable(self):
        '''
        usage : 进入找优惠界面
        '''
        logger.info("Click 找优惠 begin")
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SFPC.resource_id_ll_find_favourable_id,
                                       SFPC.click_child_module_timeout)
        logger.info("Click 找优惠 end")

    def clickOnQueue(self):
        '''
        usage : 进入智能排队界面
        '''
        logger.info("Click 智能排队 begin")
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SFPC.resource_id_ll_intelligent_queuing_id,
                                       SFPC.click_child_module_timeout)
        logger.info("Click 智能排队 end")

    def clickOnStochastic(self):
        '''
        usage : 进入帮你选界面
        '''
        logger.info("Click 帮你挑 begin")
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SFPC.resource_id_ll_stochastic_id,
                                       SFPC.click_child_module_timeout)
        logger.info("Click 帮你挑 end")

    def validFindRestaurant(self):
        '''
        usage : 检查找餐饮页面是否加载出来.
        '''
        logger.info("Check 找餐饮页面 begin")
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SFPC.verify_find_restaurant_resourceID,
                                        SFPC.verify_assert_timeout)
        logger.info("Check 找餐饮页面 end")

    def validFindFavourable(self):
        '''
        usage : 检查找优惠页面是否加载出来.
        '''
        logger.info("Check 找优惠页面 begin")
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SFPC.verify_find_favourable_resourceID,
                                        SFPC.verify_assert_timeout)
        logger.info("Check 找优惠页面 end")

    def validQueue(self):
        '''
        usage : 检查智能排队页面是否加载出来.
        '''
        logger.info("Check 智能排队页面 begin")
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SFPC.verify_intelligent_queuing_resourceID,
                                        SFPC.verify_assert_timeout)
        logger.info("Check 智能排队页面 end")

    def validStochastic(self):
        '''
        usage : 检查帮你挑页面是否加载出来.
        '''
        logger.info("Check 帮你挑页面 begin")
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SFPC.verify_stochastic_resourceID,
                                        SFPC.verify_assert_timeout)
        logger.info("Check 帮你挑页面 end")

    def validSelf(self):
        '''
        usage : 进入美食汇页面，检查是否加载出来
        '''
        logger.info("Check 美食汇页面 begin")
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SFPC.verify_food_home_page_resourceID,
                                        SFPC.verify_assert_timeout)
        logger.info("Check 美食汇页面 end")
