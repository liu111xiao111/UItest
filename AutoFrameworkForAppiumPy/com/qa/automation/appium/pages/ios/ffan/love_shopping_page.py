# -*- coding: utf-8 -*-

"""
    爱逛街tab对应页面实现
"""

from sys import api_version

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.love_shopping_page_configs import LoveShoppingPageConfigs


class LoveShoppingPage(SuperPage):
    '''
    作者 宋波
    首页=>爱逛街
    '''

    def __init__(self, test_case, driver, logger):
        super(LoveShoppingPage, self).__init__(testcase=test_case, driver=driver, logger=logger);

    '''
        usage : 进入到爱逛街页,检查购物中心按钮
    '''

    def validSelf(self):
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver,
                                              logger=self.logger, resource_id=LoveShoppingPageConfigs.name_shopping_mall)


    # 点击购物中心按钮
    def clickOnShoppingMall(self):
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver,
                                               logger=self.logger, resource_id=LoveShoppingPageConfigs.name_shopping_mall)

    # 点击电影按钮
    def clickOnFilm(self):
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver,
                                               logger=self.logger,
                                               resource_id=LoveShoppingPageConfigs.name_film)

    # 点击美食按钮
    def clickOnFood(self):
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver,
                                               logger=self.logger,
                                               resource_id=LoveShoppingPageConfigs.name_food)

    # 点击品牌按钮
    def clickOnBrand(self):
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver,
                                               logger=self.logger,
                                               resource_id=LoveShoppingPageConfigs.name_brand)

    # 点击亲子按钮
    def clickOnChlidren(self):
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver,
                                               logger=self.logger,
                                               resource_id=LoveShoppingPageConfigs.name_children)

    # 点击优惠按钮
    def clickOnPreferential(self):
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver,
                                               logger=self.logger,
                                               resource_id=LoveShoppingPageConfigs.name_preferential)

    # 点击购物按钮
    def clickOnShopping(self):
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver,
                                               logger=self.logger,
                                               resource_id=LoveShoppingPageConfigs.name_shopping)

    # 点击限时抢购按钮
    def clickOnFlashSale(self):
        API().click_view_by_xpath(testcase=self.testcase, driver=self.driver, logger=self.logger, xpath=LoveShoppingPageConfigs.xpath_flash_sale)

    # 点击停车按钮
    def clickOnParking(self):
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver,
                                               logger=self.logger,
                                               resource_id=LoveShoppingPageConfigs.name_parking)

    # 点击乐付按钮
    def clickOnLePays(self):
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver,
                                               logger=self.logger,
                                               resource_id=LoveShoppingPageConfigs.name_le_pays)

    def getCurrentCityName(self):
        return API.get_view_by_xpath_ios(self.testcase, self.driver, self.logger,
                                         LoveShoppingPageConfigs.xpath_city_name_st).text

    def clickOnCityName(self):
        API().click_view_by_xpath(self.testcase, self.driver, self.logger,
                                  LoveShoppingPageConfigs.xpath_city_name_bt,
                                  LoveShoppingPageConfigs.click_on_button_timeout)

    def switchCity(self, cityName):
        startPoint = 2
        tempXpath = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[%d]"
        goalXpath = tempXpath % startPoint
        while(cityName == API().get_view_by_xpath_ios(self.driver, self.logger, goalXpath).text):
            startPoint += 1
            goalXpath = tempXpath % startPoint
        API().click_view_by_xpath(self.testcase, self.driver, self.logger, goalXpath,
                                  LoveShoppingPageConfigs.click_on_button_timeout)

if __name__ == '__main__':
    pass;
