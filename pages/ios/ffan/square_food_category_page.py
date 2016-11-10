# -*- coding: utf-8 -*-

from pages.ios.ffan.square_food_category_page_configs import SquareFoodPageConfigs
from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.logger import logger

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
        logger.info("Click 找餐厅 begin")
        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SFPC.xpath_find_restaurant,
                                  SFPC.verify_assert_timeout)
        logger.info("Click 找餐厅 end")

    '''
        usage : 进入找优惠界面
    '''
    def clickOnFindFavourable(self):
        logger.info("Click 找优惠 begin")
        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SFPC.xpath_find_favourable,
                                  SFPC.verify_assert_timeout)
        logger.info("Click 找优惠 end")

    '''
        usage : 进入智能排队界面
    '''
    def clickOnQueue(self):
        logger.info("Click 智能排队 begin")
        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SFPC.xpath_intelligent_queuing,
                                  SFPC.verify_assert_timeout)
        logger.info("Click 智能排队 end")
    '''
        usage : 进入帮你选界面
    '''
    def clickOnStochastic(self):
        logger.info("Click 帮你选 begin")
        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SFPC.xpath_stochastic,
                                  SFPC.verify_assert_timeout)
        logger.info("Click 帮你选 end")


    '''
        usage : 检查找餐饮页面是否加载出来.
    '''
    def validFindRestaurant(self):
        logger.info("Check 餐饮页面 begin")
        API().assertElementByName(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SFPC.verify_find_restaurant_resourceID,
                                  SFPC.verify_assert_timeout);
        logger.info("Check 餐饮页面 end")
        API().screenShot(self.driver, "chanYin")

    '''
        usage : 检查找优惠页面是否加载出来.
    '''
    def validFindFavourable(self):
        logger.info("Check 优惠 begin")
        API().assertElementByName(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SFPC.verify_find_favourable_resourceID,
                                  SFPC.verify_assert_timeout);
        logger.info("Check 优惠 end")
        API().screenShot(self.driver, "youHui")

    '''
        usage : 检查智能排队页面是否加载出来.
    '''
    def validQueue(self):
        logger.info("Check 智能排队 begin")
        API().assertElementByName(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SFPC.verify_intelligent_queuing_resourceID,
                                  SFPC.verify_assert_timeout);
        logger.info("Check 智能排队 end")
        API().screenShot(self.driver, "zhiNengPaiDui")

    '''
        usage : 检查找餐饮页面是否加载出来.
    '''
    def validStochastic(self):
        logger.info("Check 餐饮页面 begin")
        API().assertElementByName(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SFPC.verify_stochastic_resourceID,
                                  SFPC.verify_assert_timeout);
        logger.info("Check 餐饮页面 end")
        API().screenShot(self.driver, "chanYin")

    '''
        usage : 进入广场模块，检查是否加载出来
    '''
    def validSelf(self):
        logger.info("Check 广场 begin")
        API().assertElementByName(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SFPC.verify_food_home_page_title,
                                  SFPC.verify_assert_timeout);
        logger.info("Check 广场 end")
        API().screenShot(self.driver, "guangChang")


if __name__ == '__main__':
    pass;