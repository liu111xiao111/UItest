# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.dashboard_page_configs import DashboardPageConfigs as DPC
from pages.logger import logger


class DashboardPage(SuperPage):
    '''
    作者： 刘涛
    首页
    '''
    def __init__(self, testcase, driver, logger):
        super(DashboardPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 进入到应用首页,检查ffan logo
        '''
        logger.info("Check 首页(爱逛街页面) begin")
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        DPC.resource_id__iv_logo__iv,
                                        90)
        logger.info("Check 首页(爱逛街页面) end")

    def clickOnMy(self):
        '''
        usage： 点击我的个人信息
        '''
        logger.info("Click 我的 begin")
        API().clickElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  DPC.text_mine,
                                  DPC.click_on_button_timeout)
        logger.info("Click 我的 end")

    def clickOnSmartLife(self):
        '''
        usage: 点击慧生活
        '''
        logger.info("Click 慧生活 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 DPC.text_huishenghuo,
                                 DPC.click_on_button_timeout)
        logger.info("Click 慧生活 end")

    def clickOnFood(self):
        '''
        usage: 点击美食类目
        '''
        logger.info("Click 美食汇 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 DPC.text_food,
                                 DPC.click_on_button_timeout)
        logger.info("Click 美食汇 end")

    def clickOnChildCategory(self):
        '''
        usage: 点击亲子类目
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 DPC.text_child,
                                 DPC.click_on_button_timeout)

    def clickOnSquareModule(self):
        '''
        usage: 点击广场模块
        '''
        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  DPC.xpath_square_module,
                                  DPC.click_on_button_timeout)

    def clickOnFeiFanCard(self):
        '''
        usage: 点击飞凡卡
        '''
        logger.info("Click 飞凡通 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 DPC.text_feifan_card,
                                 DPC.verify_view_timeout)
        logger.info("Click 飞凡通 end")

    def clickLikeShopping(self):
        '''
        usage: 点击返回首页
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 DPC.text_aiguangjie,
                                 DPC.click_on_button_timeout)

    def clickOnHomeShakeTips(self):
        '''
        usage: 点击摇一摇提示框
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       DPC.resource_id_iv_home_shake_tips,
                                       DPC.click_on_button_timeout)

    def clickOnHomeShake(self):
        '''
        usage: 点击摇一摇图标
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       DPC.resource_id_iv_home_shake,
                                       DPC.click_on_button_timeout)

    def clickOnLefuCategory(self):
        '''
        usage: 点击"乐付"类目
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 DPC.text_lefu,
                                 DPC.click_on_button_timeout)

    def clickOnParkingCategory(self):
        '''
        usage: 点击"停车"类目
        '''
        logger.info("Click 停车 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 DPC.text_parking,
                                 DPC.click_on_button_timeout)
        logger.info("Click 停车 end")

    def clickOnPrivilege(self):
        '''
        usage: 点击优惠按钮
        '''
        '''API().scrollToText(self.testcase,
                           self.driver,
                           self.logger,
                           DPC.text_privilege_button)
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 DPC.text_privilege_button,
                                 DPC.click_on_button_timeout)'''
        width = API().getWidthOfDevice(self.driver, self.logger)
        hight = API().getHeightOfDevice(self.driver, self.logger)
        for _ in range(5):
            API().scroll(self.driver, self.logger, width / 2, hight / 2, width / 2, hight / 3)
        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  DPC.xpath_sales,
                                  DPC.click_on_button_timeout)

    def clickOnShoppingMall(self):
        '''
        usage: 点击购物中心按钮
        '''
        logger.info("Click 购物中心 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 DPC.text_shopping_mall_button,
                                 DPC.click_on_button_timeout)
        logger.info("Click 购物中心 end")

    def clickOnSupermarket(self):
        '''
        usage: 点击商超
        '''
        logger.info("Click 商超 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 DPC.text_supermarket_button,
                                 DPC.click_on_button_timeout)
        logger.info("Click 商超 end")

    def clickOnSearchAll(self):
        '''
        usage: 点击搜索按钮
        '''
        logger.info("Click 搜索 icon begin")
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       DPC.resource_id_search_all_button,
                                       DPC.click_on_button_timeout)
        logger.info("Click 搜索 icon end")

    def clickOnSearchView(self):
        '''
        usage:点击全城搜索
        '''
        logger.info("Click 全城搜索 begin")
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       DPC.resource_id_tv_search_tv,
                                       DPC.click_on_button_timeout)
        logger.info("Click 全城搜索 end")

    def clickOnBrandCategory(self):
        '''
        usage: 点击"品牌"类目
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 DPC.text_brand,
                                 DPC.click_on_button_timeout)

    def clickOnSalesPromotion(self):
        '''
        usage: 点击"优惠活动"
        '''
        '''API().scrollToText(self.testcase,
                           self.driver,
                           self.logger,
                           DPC.text_sales_promotion)
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 DPC.text_sales_promotion,
                                 DPC.click_on_button_timeout)'''
        width = API().getWidthOfDevice(self.driver, self.logger)
        hight = API().getHeightOfDevice(self.driver, self.logger)
        for _ in range(5):
            API().scroll(self.driver, self.logger, width / 2, hight / 2, width / 2, hight / 3)
        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  DPC.xpath_sales,
                                  DPC.click_on_button_timeout)

    def clickOnSales(self):
        '''
        usage: 点击"优惠"类目
        '''
        # API().scrollToText(self.testcase,
        #                    self.driver,
        #                    self.logger,
        #                    DPC.text_sales)
        width = API().getWidthOfDevice(self.driver, self.logger)
        hight = API().getHeightOfDevice(self.driver, self.logger)
        for _ in range(5):
            API().scroll(self.driver, self.logger, width / 2, hight / 2, width / 2, hight / 3)
        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  DPC.xpath_sales,
                                  DPC.click_on_button_timeout)

    def clickOnMovie(self):
        '''
        usage: 点击"电影"类目
        '''
        logger.info("Click 电影 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 DPC.text_movie_button,
                                 DPC.click_on_button_timeout)
        logger.info("Click 电影 end")

    def clickOnShoppingCategory(self):
        '''
        usage: 点击"购物"类目
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 DPC.text_shopping,
                                 DPC.click_on_button_timeout)

    def clickOnSignOn(self):
        '''
        usage: 点击签到
        '''
        API().clickElementByText(self.testcase, self.driver, self.logger,
                                 DPC.text_sign_in_tv, DPC.click_on_button_timeout)

    def ClickOlympicCancleBtn(self):
        '''
        usage: 判断是否存在奥运抽奖页面
        '''
        if (API().validElementByResourceId(self.driver, self.logger, DPC.resource_id_iv_olympic_iv)):
            API().clickElementByResourceId(self.testcase,
                                           self.driver,
                                           self.logger,
                                           DPC.resource_id_iv_olympic_cancle_iv,
                                           DPC.click_on_button_timeout)

    def ClickDoubleElevenCancleBtn(self):
        '''
        usage: 判断是否存在双十一抽奖页面
        '''
        if (API().validElementByResourceId(self.driver, self.logger, DPC.resource_id_iv_double_eleven_iv)):
            API().clickElementByResourceId(self.testcase,
                                           self.driver,
                                           self.logger,
                                           DPC.resource_id_iv_double_eleven_cancle_iv,
                                           DPC.click_on_button_timeout)
    def ClickLuckBugCancleBtn(self):
        '''
        usage: 判断是否存圣诞抢福袋页面
        '''
        if (API().validElementByResourceId(self.driver, self.logger, DPC.resource_id_iv_lucky_bug_iv, DPC.get_popup_timeout)):
            API().clickElementByResourceId(self.testcase,
                                           self.driver,
                                           self.logger,
                                           DPC.resource_id_iv_lucky_bug_iv,
                                           DPC.click_on_button_timeout)

    def getCityName(self):
        return API().getTextByXpath(self.testcase, self.driver, self.logger,
                                    DPC.xpath_city_name, DPC.get_view_timeout)

    def clickOnSwithCith(self):
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  DPC.xpath_city_name, DPC.click_on_button_timeout)

    def switchCity(self, cityName):
        API().scrollToText(self.testcase,
                           self.driver,
                           self.logger,
                           cityName)

        API().waitBySeconds(2)
        API().clickElementByText(self.testcase, self.driver, self.logger,
                                 cityName, DPC.click_on_button_timeout)

    def scrollOnPage(self):
        '''
        usage: 页面内滑动
        '''
        width = API().getWidthOfDevice(self.driver, self.logger)
        hight = API().getHeightOfDevice(self.driver, self.logger)
        for i in range(20):
            if i % 2 == 0:
                API().scroll(self.driver, self.logger, width / 2, hight / 2, width / 2, hight / 3)
            else:
                API().scroll(self.driver, self.logger, width / 2, hight / 3, width / 2, hight / 2)

    def clickOnTwoBarCodeIcon(self):
        '''
        usage： 点击首页二维码图标
        '''
        logger.info("Click 首页二维码图标 begin")
        API().clickElementByResourceId(self.testcase,
                                           self.driver,
                                           self.logger,
                                           DPC.resource_id_two_bar_code_icon,
                                           DPC.click_on_button_timeout)
        logger.info("Click 首页二维码图标 end")

    def clickOnPayment(self):
        '''
        usage: 点击付款
        '''
        logger.info("Click 付款 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 DPC.text_payment_button,
                                 DPC.click_on_button_timeout)
        logger.info("Click 付款 end")
