# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.love_shopping_page_configs import LoveShoppingPageConfigs as LSPC

#
class LoveShoppingPage(SuperPage):
    '''
    作者 宋波
    首页=>爱逛街
    '''
    def __init__(self, testcase, driver, logger):
        super(LoveShoppingPage, self).__init__(testcase, driver, logger);

    def validSelf(self):
        '''
        usage : 进入到爱逛街页,检查购物中心按钮
        '''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  LSPC.text_shopping_mall,
                                  10)

    def clickOnShoppingMall(self):
        '''
        usage : 点击购物中心
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 LSPC.text_shopping_mall,
                                 10)

    def clickOnFilm(self):
        '''
        usage : 点击电影
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 LSPC.text_film,
                                 10)

    def clickOnFood(self):
        '''
        usage : 点击美食
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 LSPC.text_food,
                                 10)

    def clickOnBrand(self):
        '''
        usage : 点击品牌
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 LSPC.text_brand,
                                 10)

    def clickOnChlidren(self):
        '''
        usage : 点击亲子
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 LSPC.text_children,
                                 10)

    def clickOnPreferential(self):
        '''
        usage : 点击优惠
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 LSPC.text_preferential,
                                 10)

    def clickOnShopping(self):
        '''
        usage : 点击购物
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 LSPC.text_shopping,
                                 10)

    def clickOnFlashSale(self):
        '''
        usage : 点击限时抢购
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 LSPC.text_flash_sale,
                                 10)

    def clickOnParking(self):
        '''
        usage : 点击停车
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 LSPC.text_parking,
                                 10)

    def clickOnLePays(self):
        '''
        usage : 点击乐付
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 LSPC.text_le_pays,
                                 10)

    def clickCityTextView(self):
        '''
        usage : 点击城市
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       LSPC.resource_id_id_tv_city,
                                       10)
        
    def selectCity(self,city_name):
        '''
        usage : 选择城市
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 "安康市",
                                 10)
