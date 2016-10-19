# -*- coding: utf-8 -*-


from com.qa.automation.appium.api.api_new import API
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
        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  LoveShoppingPageConfigs.name_shopping_mall,
                                  LoveShoppingPageConfigs.assert_view_timeout)

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

    def clickOnCityName(self):
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  LoveShoppingPageConfigs.xpath_city_name_bt,
                                  LoveShoppingPageConfigs.click_on_button_timeout)

    def switchCity(self, cityName):
        startPoint = 2
        tempXpath = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[%d]/UIAStaticText[1]"
        goalXpath = tempXpath % startPoint
        tempText = API().getTextByXpath(self.testcase, self.driver, self.logger,
                                        goalXpath, LoveShoppingPageConfigs.get_view_timeout)
        while(cityName == tempText):
            startPoint += 1
            goalXpath = tempXpath % startPoint
            tempText = API().getTextByXpath(self.testcase, self.driver, self.logger,
                                            goalXpath, LoveShoppingPageConfigs.get_view_timeout)
        API().clickElementByXpath(self.testcase, self.driver, self.logger, goalXpath,
                                  LoveShoppingPageConfigs.click_on_button_timeout)
        return tempText

    def getCurrentCityName(self):
        return API().getTextByXpath(self.testcase, self.driver, self.logger,
                                    LoveShoppingPageConfigs.xpath_city_name_st,
                                    LoveShoppingPageConfigs.get_view_timeout)

    def validCurrentCityName(self, cityName):
        API().assertTrue(self.testcase, self.logger, cityName == self.getCurrentCityName)

    def getCurrentCommercialDistrictName(self):
        return API().getTextByXpath(self.testcase, self.driver, self.logger,
                                    LoveShoppingPageConfigs.xpath_commercial_district_name_st,
                                    LoveShoppingPageConfigs.get_view_timeout)

    def validCurrentCommercialDistrictName(self, commercialDistrictName):
        API().assertTrue(self.testcase, self.logger,
                         commercialDistrictName == self.getCurrentCommercialDistrictName)


if __name__ == '__main__':
    pass;
