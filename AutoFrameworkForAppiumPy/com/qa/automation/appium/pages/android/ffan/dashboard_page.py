# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.dashboard_page_configs import DashboardPageConfigs as DPC


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
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        DPC.resource_id__iv_logo__iv,
                                        30)

    def clickOnMy(self):
        '''
        usage： 点击我的个人信息
        '''
        API().clickElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  DPC.text_mine,
                                  DPC.click_on_button_timeout)

    def clickOnSmartLife(self):
        '''
        usage: 点击惠生活
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 DPC.text_huishenghuo,
                                 DPC.click_on_button_timeout)

    def clickOnFood(self):
        '''
        usage: 点击美食类目
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 DPC.text_food,
                                 DPC.click_on_button_timeout)

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
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 DPC.text_feifan_card,
                                 DPC.verify_view_timeout)

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
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 DPC.text_parking,
                                 DPC.click_on_button_timeout)

    def clickOnPrivilege(self):
        '''
        usage: 点击优惠按钮
        '''
        API().scrollToText(self.testcase,
                           self.driver,
                           self.logger,
                           DPC.text_privilege_button)
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 DPC.text_privilege_button,
                                 DPC.click_on_button_timeout)

    def clickOnShoppingMall(self):
        '''
        usage: 点击购物中心按钮
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 DPC.text_shopping_mall_button,
                                 DPC.click_on_button_timeout)

    def clickOnSearchAll(self):
        '''
        usage: 点击搜索按钮
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       DPC.resource_id_search_all_button,
                                       DPC.click_on_button_timeout)

    def clickOnSearchView(self):
        '''
        usage:点击全城搜索
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       DPC.resource_id_tv_search_tv,
                                       DPC.click_on_button_timeout)

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
        API().scrollToText(self.testcase,
                           self.driver,
                           self.logger,
                           DPC.text_sales_promotion)
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 DPC.text_sales_promotion,
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
        for _ in range(6):
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
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 DPC.text_movie_button,
                                 DPC.click_on_button_timeout)

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
