# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.square_module_page_configs import SquareModulePageConfigs as SquareModulePageConfigs


class SquareModulePage(SuperPage):
    '''
    作者 宋波
    首页=>广场
    '''

    def __init__(self, testcase, driver, logger):
        super(SquareModulePage, self).__init__(testcase,
                                               driver,
                                               logger);

    '''
        usage : 进入广场模块，检查是否加载出来
    '''
    def validSelf(self):
        for _ in range(10):
            if API().validElementByName(self.driver, self.logger,
                                        SquareModulePageConfigs.text_find_store,
                                        SquareModulePageConfigs.get_view_timeout):
                break
            self.scrollAsScreenPercent(0.5, 0.2, 0.5, 0.8)

        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  SquareModulePageConfigs.resource_id_find_store_st,
                                  SquareModulePageConfigs.assert_view_timeout)

    '''
        usage: 点击签到
    '''
    def clickOnSignOn(self):
        API().clickElementByName(self.testcase, self.driver, self.logger,
                                       SquareModulePageConfigs.resource_id_sign_in_st,
                                       SquareModulePageConfigs.assert_view_timeout)

    def clickOnParking(self):
        '''
        usage: click on the parking button.
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 SquareModulePageConfigs.resource_id_parking_cc,
                                 SquareModulePageConfigs.click_on_button_timeout)

    '''
        usage: 点击美食汇
    '''
    def clickOnFood(self):
        API().clickElementByName(self.testcase,
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
        API().clickElementByName(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SquareModulePageConfigs.text_find_store,
                                 SquareModulePageConfigs.click_on_button_timeout)

    '''
        usage: 点击搜索
    '''
    def clickOnSearch(self):
        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 SquareModulePageConfigs.resource_id_search_bt,
                                 SquareModulePageConfigs.click_on_button_timeout)

    '''
        usage: 点击达人推荐店
    '''
    def clickOnRecommmendStore(self):
        API().clickElementByXpath(self.testcase,
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
        API().clickElementByName(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SquareModulePageConfigs.text_indoor_map)

    '''
        usage: Click "乐付买单"
    '''
    def clicOnLefuPay(self):
        API().clickElementByName(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SquareModulePageConfigs.text_lefu_pay)

    '''
        usage: Click "排队取号"
    '''
    def clicOnQueue(self):
        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 SquareModulePageConfigs.text_queue,
                                 SquareModulePageConfigs.click_on_button_timeout)

    def clickOnCoupon(self):
        '''
        usage: click on privilege coupon.
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 SquareModulePageConfigs.resource_id_privilege_coupon_st,
                                 SquareModulePageConfigs.click_on_button_timeout)

    def clickOnPrivilege(self):
        '''
        usage: click on privilege.
        '''

        API().iosScrollToElement(self.driver, self.logger, '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]', '优惠')
#         API().waitBySeconds(3)
#         API().clickElementByXpath(self.testcase, self.driver, self.logger,
#                                   SquareModulePageConfigs.xpath_ckeck_all_st,
#                                   SquareModulePageConfigs.click_on_button_timeout)
        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 SquareModulePageConfigs.name_privilege_st,
                                 SquareModulePageConfigs.click_on_button_timeout)

    def clickOnMovie(self):
        '''
        usage: click on movie button
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 SquareModulePageConfigs.resource_id_movie_st,
                                 SquareModulePageConfigs.click_on_button_timeout)

    def clickOnResourceNiche(self):
        '''
        usage: click on resource niche.
        '''

        API().clickElementByXpath(self.testcase, self.driver, self.logger,
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

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 SquareModulePageConfigs.resource_id_born_to_shop_st,
                                 SquareModulePageConfigs.click_on_button_timeout)

    def clickOnGeneralCoupon(self):
        '''
        usage: click on the general coupon button.
        '''

        API().iosScrollToElement(self.driver, self.logger, '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]', '通用券')

        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  SquareModulePageConfigs.xpath_general_coupon_button,
                                  SquareModulePageConfigs.click_on_button_timeout)

    def clickOnXianchangyao(self):
        '''
        usage:点击现场摇
        '''
        API().clickElementByName(self.testcase,
                                     self.driver,
                                     self.logger,
                                     SquareModulePageConfigs.text_xianchangyao)


    def clickOnSquareMembers(self):
        '''
        usage:点击广场会员
        '''
        API().clickElementByName(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SquareModulePageConfigs.text_members)
    def validMembers(self):
        '''
        验证会员页面
        '''
        API().validElementByName(self.driver, self.logger,
                                 SquareModulePageConfigs.text_members_privilege,
                                 SquareModulePageConfigs.get_view_timeout)


if __name__ == '__main__':
    pass;
