#!/usr/bin/env python
# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.square_module_page_configs import SquareModulePageConfigs

SMPC = SquareModulePageConfigs()

'''
    usage ： 主页，点击广场模块（高新万达广场）
'''
class SquareModulePage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(SquareModulePage, self).__init__(testcase,
                                               driver,
                                               logger);

    '''
        usage : 进入广场模块，检查是否加载出来
    '''
    def validSelf(self):
        API().wait_by_seconds(10)
        API().scroll_to_text(self.driver, self.logger, SMPC.text_find_store)
        API().assert_view_by_text_android(self.testcase,
                                          self.driver,
                                          self.logger,
                                          SMPC.text_find_store);

    '''
        usage: 点击签到
    '''
    def clickOnSignOn(self):
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         SMPC.text_sign_on);

    '''
        usage: 点击停车类目
    '''
    def clickOnParking(self):
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         SMPC.text_parking);

    '''
        usage: 点击停车类目
    '''
    def clickOnMember(self):
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         SMPC.text_member);

    '''
        usage: 点击美食汇
    '''
    def clickOnFood(self):
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         SMPC.text_food);

    '''
        usage: 点击爱购物
    '''
    def clickOnShopping(self):
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         SMPC.text_shopping);

    '''
        usage: 点击找店
    '''
    def clicOnFindStore(self):
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         SMPC.text_find_store);

    '''
        usage: 点击搜索
    '''
    def clickOnSearch(self):
        API().click_view_by_resourceID(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SMPC.resource_id_iv_search_iv);

    '''
        usage: 点击达人推荐店
    '''
    def clickOnRecommmendStore(self):
        API().click_view_by_xpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SMPC.xpath_recommend_store)

    '''
        usage: scroll to food.
    '''
    def scrollToFood(self):
        API().scroll_to_text(self.driver,
                             self.logger,
                             SMPC.text_food)

    '''
        usage: Click "室内地图"
    '''
    def clicOnIndoorMap(self):
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         SMPC.text_indoor_map);

    '''
        usage: Click "乐付买单"
    '''
    def clicOnLefuPay(self):
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         SMPC.text_lefu_pay);

    '''
        usage: Click "排队取号"
    '''
    def clicOnQueue(self):
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         SMPC.text_queue);

    '''
        usage: click coupon category
    '''
    def clickOnCoupon(self):
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         SMPC.text_coupon)

    '''
        usage: click movie button
    '''
    def clickOnMovie(self):
        API().scroll_to_text(self.driver, self.logger, SMPC.text_movie_button)
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         SMPC.text_movie_button,
                                         SMPC.click_on_button_timeout)

    '''
        usage: click on resource niche.
    '''
    def clickOnResourceNiche(self):
        API().click_view_by_resourceID(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SMPC.resource_id_resource_niche_button,
                                       SMPC.click_on_button_timeout)

    '''
        usage: click flash sales
    '''
    def clickOnFlashSales(self):
        API().scroll_to_text(self.driver, self.logger, SMPC.text_flash_sales)
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         SMPC.text_flash_sales)

    '''
        usage: click on the staff picks button.
    '''
    def clickOnStaffPicks(self):
        API().scroll_to_text(self.driver, self.logger, SMPC.text_staff_picks_button)
        tempText = API().get_view_by_resourceID(self.driver,
                                                self.logger,
                                                "com.wanda.app.wanhui:id/tv_title").text
        API().click_view_by_xpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SMPC.xpath_recommend_store,
                                  SMPC.click_on_button_timeout)
        return tempText

    '''
        usage: click on the born to shop button.
    '''
    def clickOnBornToShop(self):
        API().scroll_to_text(self.driver, self.logger, SMPC.text_born_to_shop)
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         SMPC.text_born_to_shop,
                                         SMPC.click_on_button_timeout)


if __name__ == '__main__':
    pass;
