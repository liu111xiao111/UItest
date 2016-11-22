# -*- coding: utf-8 -*-

import time
from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.meituan.food_category_page_configs import FoodCategoryPageConfigs as FCPC
from pages.logger import logger


class FoodCategoryPage(SuperPage):
    '''
    作者 刘涛
    首页＝>美食汇
    '''
    def __init__(self, testcase, driver, logger):
        super(FoodCategoryPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证美食页面
        '''
        logger.info("Check 美食页面 begin")
        API().assertElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 FCPC.view_text_tiltle,
                                 FCPC.verify_view_timeout)
        logger.info("Check 美食页面 begin")

    def validModules(self):
        '''
        usage: 点击美食主界面的所有入口并验证
        '''
        restaurantList = (u"自助餐", u"火锅", u"小吃快餐", u"烧烤烤肉",
                          u"生日蛋糕", u"日韩料理", u"甜点饮品")
        for restaurant in restaurantList:
            logger.info("Check 入口(%s) begin" % restaurant)
            API().clickElementByText(self.testcase,
                                     self.driver,
                                     self.logger,
                                     restaurant,
                                     FCPC.click_view_timeout)
            API().waitBySeconds(3)
            self.validRestaurant(restaurant)
            API().screenShot(self.driver, "meiShiRuKou")
            self.clickBackKey()
            API().screenShot(self.driver, "meiShi")
            logger.info("Check 入口(%s) end" % restaurant)

    def validRestaurant(self, restaurant = "default"):
        '''
        usage : 进入美食子页面，根据餐饮的textview, 检查找餐饮页面是否加载出来.
        '''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  restaurant,
                                  FCPC.verify_view_timeout)
