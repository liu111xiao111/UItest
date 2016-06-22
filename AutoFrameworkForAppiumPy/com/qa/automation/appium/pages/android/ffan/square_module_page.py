# -*- coding: utf-8 -*-

import os, sys
from time import sleep
import unittest

from appium import webdriver

from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.pages.android.common.super_page import *
from com.qa.automation.appium.pages.android.ffan.square_module_page_configs import SquareModulePageConfigs

# sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

'''
    usage ： 主页，点击广场模块（高新万达广场）
'''


class SquareModulePage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(SquareModulePage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    '''
        usage : 进入广场模块，检查是否加载出来
    '''

    def validSelf(self):
        API().assert_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                          text=SquareModulePageConfigs.text_find_store);

    '''
        usage: 点击签到
    '''

    def clickOnSignOn(self):
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=SquareModulePageConfigs.text_sign_on);

    '''
        usage: 点击停车类目
    '''

    def clickOnParking(self):
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=SquareModulePageConfigs.text_parking);

    '''
        usage: 点击停车类目
    '''

    def clickOnMember(self):
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=SquareModulePageConfigs.text_member);

    '''
        usage: 点击美食汇
    '''

    def clickOnFood(self):
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=SquareModulePageConfigs.text_food);

    '''
        usage: 点击爱购物
    '''

    def clickOnShopping(self):
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=SquareModulePageConfigs.text_shopping);

    '''
        usage: 点击找店
    '''

    def clicOnFindStore(self):
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=SquareModulePageConfigs.text_find_store);

    '''
        usage: 点击搜索
    '''

    def clickOnSearch(self):
        API().click_view_by_resourceID_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                               resource_id=SquareModulePageConfigs.resource_id_iv_search_iv);

    '''
        usage: 点击达人推荐店
    '''

    def clickOnRecommmendStore(self):
        API().click_view_by_xpath(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                  xpath=SquareModulePageConfigs.xpath_recommend_store)

    def scrollToFood(self):
        API().scroll_to_text(driver=self.driver, logger=self.logger, text=SquareModulePageConfigs.text_food)
        # API().scrollFromElToEl(driver = self.driver, logger = self.logger , el1 = SquareModulePageConfigs.text_find_store , el2 = SquareModulePageConfigs.text_food)   

    def clicOnIndoorMap(self):
        '''
        usage: Click "室内地图"
        '''
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=SquareModulePageConfigs.text_indoor_map);

    def clicOnLefuPay(self):
        '''
        usage: Click "乐付买单"
        '''
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=SquareModulePageConfigs.text_lefu_pay);

    def clicOnQueue(self):
        '''
        usage: Click "排队取号"
        '''
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=SquareModulePageConfigs.text_queue);

    def clickOnCoupon(self):
        '''
            usage: click coupon category
        '''
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=SquareModulePageConfigs.text_coupon)

    def clickOnMovie(self):
        '''
            usage: click movie button
        '''

        API().scroll_to_text(self.driver, self.logger, SquareModulePageConfigs.text_movie_button)
        API().click_view_by_text_android(self.testcase, self.driver, self.logger,
                                         SquareModulePageConfigs.text_movie_button,
                                         SquareModulePageConfigs.click_on_button_timeout)

    def clickOnResourceNiche(self):
        '''
        usage: click on resource niche.
        '''

        API().click_view_by_resourceID_android(self.testcase, self.driver, self.logger,
                                               SquareModulePageConfigs.resource_id_resource_niche_button,
                                               SquareModulePageConfigs.click_on_button_timeout)


if __name__ == '__main__':
    pass;
