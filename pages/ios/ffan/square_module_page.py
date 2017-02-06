# -*- coding: utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.square_module_page_configs import SquareModulePageConfigs as SquareModulePageConfigs
from pages.logger import logger

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
        logger.info("Check 广场 begin")
        for _ in range(10):
            if API().validElementByName(self.driver, self.logger,
                                        SquareModulePageConfigs.text_find_store,
                                        SquareModulePageConfigs.get_view_timeout):
                break
            self.scrollAsScreenPercent(0.5, 0.2, 0.5, 0.8)

        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  SquareModulePageConfigs.name_find_store_st,
                                  SquareModulePageConfigs.assert_view_timeout)
        logger.info("Check 广场 end")
        API().screenShot(self.driver, "guangChang")

    '''
        usage: 点击签到
    '''
    def clickOnSignOn(self):
        logger.info("Click 签到 begin")
        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 SquareModulePageConfigs.name_sign_in_st,
                                 SquareModulePageConfigs.assert_view_timeout)
        logger.info("Click 签到 end")
        API().screenShot(self.driver, "qianDao")

    def clickOnParking(self):
        '''
        usage: click on the parking button.
        '''
        logger.info("Click 停车 begin")
        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 SquareModulePageConfigs.name_parking_cc,
                                 SquareModulePageConfigs.click_on_button_timeout)
        logger.info("Click 停车 end")

    '''
        usage: 点击美食汇
    '''
    def clickOnFood(self):
        logger.info("Click 美食汇 begin")
        # API().clickElementByName(self.testcase,
        #                          self.driver,
        #                          self.logger,
        #                          SquareModulePageConfigs.text_food);
        logger.info("Scroll to 美食推荐 begin")

        for _ in range(3):
            self.scrollAsScreenPercent(0.5, 0.2, 0.5, 0.8)
        logger.info("Scroll to 美食推荐 end")

        logger.info("Click 更多 begin")
        API().clickElementByXpath(self.testcase, self.driver, self.logger, xpath = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[4]/UIAButton[1]")
        logger.info("Click 更多 end")



    '''
        usage: 点击爱购物
    '''
    def clickOnShopping(self):
        logger.info("Click 爱购物 begin")
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         SquareModulePageConfigs.text_shopping);
        logger.info("Click 爱购物 end")

    '''
        usage: 点击找店
    '''
    def clicOnFindingStore(self):
        logger.info("Click 找店 begin")
        API().clickElementByName(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SquareModulePageConfigs.text_find_store,
                                 SquareModulePageConfigs.click_on_button_timeout)
        logger.info("Click 找店 end")

    '''
        usage: 点击搜索
    '''
    def clickOnSearch(self):
        logger.info("Click 搜索 begin")
        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 SquareModulePageConfigs.name_search_bt,
                                 SquareModulePageConfigs.click_on_button_timeout)
        logger.info("Click 搜索 end")
        API().screenShot(self.driver, "zhaoDian")

    '''
        usage: 点击达人推荐店
    '''
    def clickOnRecommmendStore(self):
        logger.info("Click 达人推荐店 begin")
        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SquareModulePageConfigs.xpath_recommend_store)
        logger.info("Click 达人推荐店 end")

    '''
        usage: scroll to food.
    '''
    def scrollToFood(self):
        logger.info("Scroll to 美食汇 begin")
        API().scroll_to_text(self.driver,
                             self.logger,
                             SquareModulePageConfigs.text_food)
        logger.info("Scroll to 美食汇 end")

    '''
        usage: Click "室内地图"
    '''
    def clicOnShiNeiDitu(self):
        logger.info("Click 室内地图 begin")
        API().clickElementByName(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SquareModulePageConfigs.text_indoor_map)
        logger.info("Click 室内地图 end")

    '''
        usage: Click "乐付买单"
    '''
    def clicOnLefuPay(self):
        logger.info("Click 乐付买单 begin")
        API().clickElementByName(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SquareModulePageConfigs.text_lefu_pay)
        logger.info("Click 乐付买单 end")

    '''
        usage: Click "排队取号"
    '''
    def clicOnPaiDui(self):
        logger.info("Click 排队取号 begin")
        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 SquareModulePageConfigs.text_queue,
                                 SquareModulePageConfigs.click_on_button_timeout)
        logger.info("Click 排队取号 end")

    def clickOnCoupon(self):
        '''
        usage: click on privilege coupon.
        '''
        logger.info("Click 优惠券 begin")
        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 SquareModulePageConfigs.name_privilege_coupon_st,
                                 SquareModulePageConfigs.click_on_button_timeout)
        logger.info("Click 优惠券 end")

    def clickOnPrivilege(self):
        '''
        usage: click on privilege.
        '''
        logger.info("Click 优惠 begin")
        API().iosScrollToElement(self.driver, self.logger, '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]', '优惠')
#         API().waitBySeconds(3)
#         API().clickElementByXpath(self.testcase, self.driver, self.logger,
#                                   SquareModulePageConfigs.xpath_ckeck_all_st,
#                                   SquareModulePageConfigs.click_on_button_timeout)
        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 SquareModulePageConfigs.name_privilege_st,
                                 SquareModulePageConfigs.click_on_button_timeout)
        logger.info("Click 优惠 end")

    def clickOnMovie(self):
        '''
        usage: click on movie button
        '''
        logger.info("Click 电影 begin")
        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 SquareModulePageConfigs.resource_id_movie_st,
                                 SquareModulePageConfigs.click_on_button_timeout)
        logger.info("Click 电影 end")

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
                                 SquareModulePageConfigs.name_born_to_shop_st,
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
        logger.info("Click 现场摇 begin")
        API().clickElementByName(self.testcase,
                                     self.driver,
                                     self.logger,
                                     SquareModulePageConfigs.text_xianchangyao)
        logger.info("Click 现场摇 end")


    def clickOnSquareMembers(self):
        '''
        usage:点击广场会员
        '''
        logger.info("Click 广场会员 begin")
        API().clickElementByName(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SquareModulePageConfigs.text_members)
        logger.info("Click 广场会员 end")
    def validMembers(self):
        '''
        验证会员页面
        '''
        logger.info("Check 会员页面 begin")
        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  SquareModulePageConfigs.text_members_privilege,
                                  SquareModulePageConfigs.assert_view_timeout)
        logger.info("Check 会员页面 end")
        API().screenShot(self.driver, "huiYuanJieMian")


if __name__ == '__main__':
    pass;
