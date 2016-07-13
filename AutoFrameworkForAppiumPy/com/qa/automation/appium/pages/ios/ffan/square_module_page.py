# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.square_module_page_configs import SquareModulePageConfigs as SquareModulePageConfigs


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
        tempWidth = API().get_width_of_device(self.driver, self.logger)
        tempHight = API().get_height_of_device(self.driver, self.logger)
        for _ in range(10):
            API().scroll(self.driver, self.logger,
                         tempWidth / 2, tempHight / 5, tempWidth / 2, tempHight * 4 / 5)

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger,
                                          SquareModulePageConfigs.resource_id_find_store_st,
                                          SquareModulePageConfigs.assert_view_timeout)

    '''
        usage: 点击签到
    '''
    def clickOnSignOn(self):
        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                       SquareModulePageConfigs.resource_id_sign_in_st,
                                       SquareModulePageConfigs.assert_view_timeout)

    def clickOnParking(self):
        '''
        usage: click on the parking button.
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                       SquareModulePageConfigs.resource_id_parking_cc,
                                       SquareModulePageConfigs.click_on_button_timeout)

    '''
        usage: 点击停车类目
    '''
    def clickOnMember(self):
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         SquareModulePageConfigs.text_member);

    '''
        usage: 点击美食汇
    '''
    def clickOnFood(self):
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         SquareModulePageConfigs.text_food);

    '''
        usage: 点击爱购物
    '''
    def clickOnShopping(self):
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         SquareModulePageConfigs.text_shopping);

    '''
        usage: 点击找店
    '''
    def clicOnFindStore(self):
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         SquareModulePageConfigs.text_find_store);

    '''
        usage: 点击搜索
    '''
    def clickOnSearch(self):
        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                       SquareModulePageConfigs.resource_id_search_bt,
                                       SquareModulePageConfigs.click_on_button_timeout)

    '''
        usage: 点击达人推荐店
    '''
    def clickOnRecommmendStore(self):
        API().click_view_by_xpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SquareModulePageConfigs.xpath_recommend_store)

    '''
        usage: scroll to food.
    '''
    def scrollToFood(self):
        API().scroll_to_text(self.driver,
                             self.logger,
                             SquareModulePageConfigs.text_food)

    '''
        usage: Click "室内地图"
    '''
    def clicOnIndoorMap(self):
        API().click_view_by_resourceID(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SquareModulePageConfigs.text_indoor_map)

    '''
        usage: Click "乐付买单"
    '''
    def clicOnLefuPay(self):
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         SquareModulePageConfigs.text_lefu_pay);

    '''
        usage: Click "排队取号"
    '''
    def clicOnQueue(self):
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         SquareModulePageConfigs.text_queue);

    '''
        usage: click coupon category
    '''
    def clickOnCoupon(self):
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         SquareModulePageConfigs.text_coupon)

    def clickOnMovie(self):
        '''
        usage: click on movie button
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                       SquareModulePageConfigs.resource_id_movie_st,
                                       SquareModulePageConfigs.click_on_button_timeout)

    def clickOnResourceNiche(self):
        '''
        usage: click on resource niche.
        '''

        API().click_view_by_xpath(self.testcase, self.driver, self.logger,
                                       SquareModulePageConfigs.xpath_resource_niche_tc,
                                       SquareModulePageConfigs.click_on_button_timeout)

    def clickOnFlashSales(self):
        '''
        usage: click on flash sales button.
        '''

        API().scroll_to_text(self.driver, self.logger, SquareModulePageConfigs.text_flash_sales)
        API().click_view_by_text_android(self.testcase, self.driver, self.logger,
                                         SquareModulePageConfigs.text_flash_sales,
                                         SquareModulePageConfigs.click_on_button_timeout)

    def clickOnStaffPicks(self):
        '''
        usage: click on the staff picks button.
        '''

        API().scroll_to_text(self.driver, self.logger, SquareModulePageConfigs.text_staff_picks_button)
        tempText = API().get_view_by_xpath_android(self.testcase, self.driver, self.logger,
                                                   SquareModulePageConfigs.xpath_sub_staff_picks_button,
                                                   SquareModulePageConfigs.get_view_timeout).text
        API().click_view_by_xpath(self.testcase, self.driver, self.logger,
                                  SquareModulePageConfigs.xpath_recommend_store,
                                  SquareModulePageConfigs.click_on_button_timeout)

        return tempText


    def clickOnBornToShop(self):
        '''
        usage: click on the born to shop button.
        '''

        API().scroll_to_text(self.driver, self.logger, SquareModulePageConfigs.text_born_to_shop)
        API().click_view_by_text_android(self.testcase, self.driver, self.logger,
                                         SquareModulePageConfigs.text_born_to_shop,
                                         SquareModulePageConfigs.click_on_button_timeout)

    def clickOnGeneralCoupon(self):
        '''
        usage: click on the general coupon button.
        '''

        tempWidth = API().get_width_of_device(self.driver, self.logger)
        tempHight = API().get_height_of_device(self.driver, self.logger)
        for _ in range(10):
            API().scroll(self.driver, self.logger, tempWidth / 2, tempHight * 4 / 5, tempWidth / 2, tempHight / 5)

        API().scroll_to_text(self.driver, self.logger,
                             SquareModulePageConfigs.text_general_coupon_button)
        API().click_view_by_xpath(self.testcase, self.driver, self.logger,
                                  SquareModulePageConfigs.xpath_general_coupon_button,
                                  SquareModulePageConfigs.click_on_button_timeout)

if __name__ == '__main__':
    pass;
