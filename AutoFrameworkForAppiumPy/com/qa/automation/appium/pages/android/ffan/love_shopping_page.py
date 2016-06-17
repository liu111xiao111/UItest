# -*- coding: utf-8 -*-

import os, sys

from time import sleep
import unittest
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.pages.android.common.super_page import *
from com.qa.automation.appium.pages.android.ffan.love_shopping_page_configs import *

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


#
#
class LoveShoppingPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(LoveShoppingPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    '''
        usage : 进入到爱逛街页,检查购物中心按钮
    '''

    def validSelf(self):
        API().assert_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                          text=LoveShoppingPageConfigs.text_shopping_mall,
                                          seconds=10);

    # 点击购物中心按钮
    def clickOnShoppingMall(self):
        API().click_view_by_text_android(testcase = self.testcase, driver=self.driver, logger=self.logger,
                                         text=LoveShoppingPageConfigs.text_shopping_mall);

    # 点击电影按钮
    def clickOnFilm(self):
        API().click_view_by_text_android(testcase = self.testcase, driver=self.driver, logger=self.logger,
                                         text=LoveShoppingPageConfigs.text_film
                                         );

    # 点击美食按钮
    def clickOnFood(self):
        API().click_view_by_text_android(testcase = self.testcase, driver=self.driver, logger=self.logger,
                                          text=LoveShoppingPageConfigs.text_food
                                          );
    # 点击品牌按钮
    def clickOnBrand(self):
        API().click_view_by_text_android(testcase = self.testcase, driver=self.driver, logger=self.logger,
                                         text=LoveShoppingPageConfigs.text_brand
                                         );

    # 点击亲子按钮
    def clickOnChlidren(self):
        API().click_view_by_text_android(testcase = self.testcase, driver=self.driver, logger=self.logger,
                                         text=LoveShoppingPageConfigs.text_children
                                         );

    # 点击优惠按钮
    def clickOnPreferential(self):
        API().click_view_by_text_android(testcase = self.testcase, driver=self.driver, logger=self.logger,
                                         text=LoveShoppingPageConfigs.text_preferential
                                         );
    # 点击购物按钮
    def clickOnShopping(self):
        API().click_view_by_text_android(testcase = self.testcase, driver=self.driver, logger=self.logger,
                                         text=LoveShoppingPageConfigs.text_shopping
                                         );

    # 点击限时抢购按钮
    def clickOnFlashSale(self):
        API().click_view_by_text_android(testcase = self.testcase, driver=self.driver, logger=self.logger,
                                         text=LoveShoppingPageConfigs.text_flash_sale
                                         );

    # 点击停车按钮
    def clickOnParking(self):
        API().click_view_by_text_android(testcase = self.testcase, driver=self.driver, logger=self.logger,
                                         text=LoveShoppingPageConfigs.text_parking
                                         );

    # 点击乐付按钮
    def clickOnLePays(self):
        API().click_view_by_text_android(testcase = self.testcase, driver=self.driver, logger=self.logger,
                                         text=LoveShoppingPageConfigs.text_le_pays
                                         );

if __name__ == '__main__':
    pass;
