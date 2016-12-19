# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.square_module_page_configs import SquareModulePageConfigs as SMPC
from pages.logger import logger


class SquareModulePage(SuperPage):
    '''
    作者 陈诚
    主页=>广场模块（高新万达广场）
    '''
    def __init__(self, testcase, driver, logger):
        super(SquareModulePage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 进入广场模块，检查是否加载出来
        '''
        # tempWidth = API().getWidthOfDevice(self.driver, self.logger)
        # tempHight = API().getHeightOfDevice(self.driver, self.logger)
        # for _ in range(10):
        #     API().scroll(self.driver, self.logger,
        #                  tempWidth / 2, tempHight / 5, tempWidth / 2, tempHight * 4 / 5)
        #
        # API().scrollToText(self.testcase,
        #                    self.driver,
        #                    self.logger,
        #                    SMPC.text_find_store)
        logger.info("Check 广场页面 begin")
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SMPC.resource_id_square_title,
                                        SMPC.get_view_timeout)
        logger.info("Check 广场页面 end")

    def validSelfDetails(self):
        '''
        usage : 进入广场模块，检查是否加载出来
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SMPC.resource_id_title,
                                        SMPC.get_view_timeout)

    def clickOnSignOn(self):
        '''
        usage: 点击签到
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SMPC.text_sign_on,
                                 SMPC.click_on_button_timeout)

    def clickOnParking(self):
        '''
        usage: 点击停车类目
        '''
        logger.info("Click 停车 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SMPC.text_parking,
                                 SMPC.click_on_button_timeout)
        logger.info("Click 停车 end")

    def clickOnMember(self):
        '''
        usage: 点击会员类目
        '''
        logger.info("Click 会员 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SMPC.text_member,
                                 SMPC.click_on_button_timeout)
        logger.info("Click 会员 end")

    def clickOnFood(self):
        '''
        usage: 点击美食汇
        '''
        logger.info("Click 美食汇 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SMPC.text_food,
                                 SMPC.click_on_button_timeout)
        logger.info("Click 美食汇 end")

    def clickOnFoodRecommend(self):
        '''
        usage: 点击美食推荐
        '''
        logger.info("Click 美食推荐 begin")
        width = API().getWidthOfDevice(self.driver, self.logger)
        hight = API().getHeightOfDevice(self.driver, self.logger)
        for _ in range(9):
            API().scroll(self.driver, self.logger, width / 2, hight / 2, width / 2, hight / 3)
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SMPC.text_food_recommend_more,
                                 SMPC.click_on_button_timeout)
        logger.info("Click 美食推荐 end")

    def clickOnShopping(self):
        '''
        usage: 点击爱购物
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SMPC.text_shopping,
                                 SMPC.click_on_button_timeout)

    def clicOnFindStore(self):
        '''
        usage: 点击找店
        '''
        logger.info("Click 找店 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SMPC.text_find_store,
                                 SMPC.click_on_button_timeout)
        logger.info("Click 找店 end")

    def clickOnSearch(self):
        '''
        usage: 点击搜索
        '''
        logger.info("Click 搜索 icon begin")
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SMPC.resource_id_iv_search_iv,
                                       SMPC.click_on_button_timeout)
        logger.info("Click 搜索 icon end")

    def clickOnRecommmendStore(self):
        '''
        usage: 点击达人推荐店
        '''
        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SMPC.xpath_recommend_store,
                                  SMPC.click_on_button_timeout)

    def scrollToFood(self):
        '''
        usage: 滑动到美食入口
        '''
        API().scrollToText(self.testcase,
                           self.driver,
                           self.logger,
                           SMPC.text_food)

    def clicOnIndoorMap(self):
        '''
        usage: 点击"室内地图"
        '''
        logger.info("Click 室内地图 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SMPC.text_indoor_map,
                                 SMPC.click_on_button_timeout)
        logger.info("Click 室内地图 end")

    def clicOnLefuPay(self):
        '''
        usage: 点击"乐付买单"
        '''
        logger.info("Click 买单 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SMPC.text_lefu_pay,
                                 SMPC.click_on_button_timeout)
        logger.info("Click 买单 end")

    def clicOnShake(self):
        '''
        usage: 点击"现场摇"
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SMPC.text_shake,
                                 SMPC.click_on_button_timeout)

    def clicOnQueue(self):
        '''
        usage: 点击 "排队取号"
        '''
        logger.info("Click 排队取号 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SMPC.text_queue,
                                 SMPC.click_on_button_timeout)
        logger.info("Click 排队取号 end")

    def clickOnCoupon(self):
        '''
        usage: 点击优惠券类目
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SMPC.text_coupon,
                                 SMPC.click_on_button_timeout)

    def clickOnSales(self):
        '''
        usage: 点击页面下方的优惠券
        '''
        tempWidth = API().getWidthOfDevice(self.driver, self.logger)
        tempHight = API().getHeightOfDevice(self.driver, self.logger)
        for _ in range(7):
            API().scroll(self.driver, self.logger, tempWidth / 2,
                         tempHight * 4 / 5, tempWidth / 2, tempHight / 5)

        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SMPC.text_sales,
                                 SMPC.click_on_button_timeout)

    def clickOnMovie(self):
        '''
        usage: 点击电影类目
        '''
        '''API().scrollToText(self.testcase,
                           self.driver,
                           self.logger,
                           SMPC.text_movie_button)'''
        '''width = API().getWidthOfDevice(self.driver, self.logger)
        hight = API().getHeightOfDevice(self.driver, self.logger)
        API().scroll(self.driver, self.logger, width/2, hight/2, width/2, hight/3)'''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SMPC.text_movie_button,
                                 SMPC.click_on_button_timeout)

    def clickOnResourceNiche(self):
        '''
        usage: 点击资源位
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SMPC.resource_id_resource_niche_button,
                                       SMPC.click_on_button_timeout)

    def clickOnFlashSales(self):
        '''
        usage: 点击限时抢购
        '''
        API().scrollToText(self.testcase,
                           self.driver,
                           self.logger,
                           SMPC.text_flash_sales)
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SMPC.text_flash_sales,
                                 SMPC.click_on_button_timeout)

    def clickOnStaffPicks(self):
        '''
        usage: 点击达人推荐
        '''
        API().scrollToText(self.testcase,
                           self.driver,
                           self.logger,
                           SMPC.text_staff_picks_button)
        tempText = API().getTextByXpath(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SMPC.xpath_sub_staff_picks_button,
                                        SMPC.get_view_timeout)
        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SMPC.xpath_recommend_store,
                                  SMPC.click_on_button_timeout)

        return tempText

    def clickOnBornToShop(self):
        '''
        usage: 点击爱购物
        '''
        '''tempWidth = API().getWidthOfDevice(self.driver, self.logger)
        tempHight = API().getHeightOfDevice(self.driver, self.logger)
        for _ in range(3):
            API().scroll(self.driver, self.logger, tempWidth / 2,
                         tempHight * 4 / 5, tempWidth / 2, tempHight / 5)'''

        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SMPC.xpath_liking_shopping,
                                  SMPC.click_on_button_timeout)

    def clickOnGeneralCoupon(self):
        '''
        usage: 点击通用券
        '''
        tempWidth = API().getWidthOfDevice(self.driver, self.logger)
        tempHight = API().getHeightOfDevice(self.driver, self.logger)
        for _ in range(10):
            API().scroll(self.driver, self.logger, tempWidth / 2,
                         tempHight * 4 / 5, tempWidth / 2, tempHight / 5)

        API().scrollToText(self.testcase,
                           self.driver,
                           self.logger,
                           SMPC.text_general_coupon_button)
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  SMPC.xpath_general_coupon_button,
                                  SMPC.click_on_button_timeout)
