# -*- coding: utf-8 -*-
from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.dashboard_page_configs import DashboardPageConfigs
from pages.logger import logger

class DashboardPage(SuperPage):
    '''
    作者 宋波
    首页
    '''

    def __init__(self, testcase, driver, logger):
        super(DashboardPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 进入到应用首页,检查ffan logo
        '''
        logger.info("Check 爱逛街页面 begin")

        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  DashboardPageConfigs.name_home_title_icon,
                                  DashboardPageConfigs.assert_view_timeout)
        API().screenShot(self.driver, "aiGuangJie")
        logger.info("Check 爱逛街页面 end")

    def validBeijing(self):
        '''
        usage:验证北京市
        '''
        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  DashboardPageConfigs.name_beijing,
                                  DashboardPageConfigs.assert_view_timeout)


    def validCities(self, cityName):
        '''
        usage: Verify whether the current city is correct.
        '''

        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  cityName, DashboardPageConfigs.assert_view_timeout)

    def validCityData(self, textContains="default", xpath="default"):
        '''
            usage: 验证切换城市后的数据是否为北京市的
        '''
        # textContains = DashboardPageConfigs.text_valid_beijing
        # xpath = DashboardPageConfigs.xpath_guangchang
        #
        # tempText = API().getTextByXpath(self.testcase, self.driver, self.logger,
        #                                 xpath, DashboardPageConfigs.get_timeout)
        # print(tempText)
        # print(textContains)
        # API().assertTrue(self.testcase, self.logger, textContains in tempText)
        API().assertElementByName(self.testcase, self.driver, self.logger,DashboardPageConfigs.name_beijing)

    def clickOnBornToShop(self):
        """
        点击爱逛街icon
        """

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 DashboardPageConfigs.name_app_tabbar_home_normal,
                                 DashboardPageConfigs.click_on_button_timeout)

    def clickOnHuiLife(self):
        """
        点击慧生活icon
        """

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 DashboardPageConfigs.name_app_tabbar_life_normal,
                                 DashboardPageConfigs.click_on_button_timeout)

    def clickOnFeiFanCard(self):
        """
        点击飞凡卡icon
        """

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 DashboardPageConfigs.name_app_tabbar_card_normal,
                                 DashboardPageConfigs.click_on_button_timeout)

    def clickOnMy(self):
        """
        点击我的icon
        """

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 DashboardPageConfigs.name_app_tabbar_user_normal,
                                 DashboardPageConfigs.click_on_button_timeout)

    def clickOnSearchAll(self):
        '''
        usage: click on search in city.
        '''
        logger.info("Click 全城搜索 begin")
        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 DashboardPageConfigs.resource_id_search_all_tv,
                                 DashboardPageConfigs.click_on_button_timeout)
        logger.info("Click 全城搜索 end")

    def clickOnMovie(self):
        '''
        usage: click on movie button
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 DashboardPageConfigs.resource_id_movie_st,
                                 DashboardPageConfigs.click_on_button_timeout)

    def clickOnStores(self):
        '''
        usage: click on stores button
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 DashboardPageConfigs.name_movie_st,
                                 DashboardPageConfigs.click_on_button_timeout)

    def clickOnPrivilege(self):
        '''
        usage: click privilege button
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 DashboardPageConfigs.resource_id_movieprivilege_st,
                                 DashboardPageConfigs.click_on_button_timeout)

    def clickOnSquareModule(self):
        '''
        usage: 点击"广场"
        '''
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  DashboardPageConfigs.xpath_square_module_st,
                                  DashboardPageConfigs.click_on_button_timeout)

    def clickOnParking(self):
        '''
        usage: 点击"停车"
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 DashboardPageConfigs.name_parking,
                                 DashboardPageConfigs.click_on_button_timeout)

    def clickOnShopping(self):
        '''
        usage: 点击"购物"
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 DashboardPageConfigs.name_shopping,
                                 DashboardPageConfigs.click_on_button_timeout)

    def clickOnLePay(self):
        '''
        usage: 点击"乐付"
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 DashboardPageConfigs.name_le_pay,
                                 DashboardPageConfigs.click_on_button_timeout)

    def clickOnBrand(self):
        '''
        usage: 点击"品牌"
        '''
        logger.info("Click 品牌 begin")
        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 DashboardPageConfigs.name_brand,
                                 DashboardPageConfigs.click_on_button_timeout)
        logger.info("Click 品牌 end")

    def clickOnFood(self):
        '''
        usage: 点击"美食汇"
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 DashboardPageConfigs.name_food,
                                 DashboardPageConfigs.click_on_button_timeout)

    def clickOnShoppingMall(self):
        '''
        usage: 点击"购物中心"
        '''
        logger.info("Click 购物中心 bengin")
        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 DashboardPageConfigs.name_shopping_mall,
                                 DashboardPageConfigs.click_on_button_timeout)
        logger.info("Click 购物中心 end")

    def clickOnSalesPromotion(self):
        '''
         usage: 点击"优惠活动"
        '''
        API().iosScrollToElement(self.driver, self.logger,
                                 DashboardPageConfigs.xpath_main_page,
                                 DashboardPageConfigs.name_sales_promotion)

        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  DashboardPageConfigs.xpath_sales_promotion,
                                  DashboardPageConfigs.click_on_button_timeout)

    def clickOnChildCategory(self):
        '''
        usage: 点击"亲子"
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 DashboardPageConfigs.name_child,
                                 DashboardPageConfigs.click_on_button_timeout)

    def clickOnSignOn(self):
        '''
        usage: 点击签到
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 DashboardPageConfigs.name_sign_in_st,
                                 DashboardPageConfigs.click_on_button_timeout)

    def clickOnCity(self):
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  DashboardPageConfigs.xpath_city,
                                  DashboardPageConfigs.click_on_button_timeout)

    def clickOnYaoyiyao(self):
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  DashboardPageConfigs.xpath_yaoyiyao,
                                  DashboardPageConfigs.click_on_button_timeout)



    def dealAcitivities(self):
        hasActivities = API().validElementByName(self.driver,self.logger,DashboardPageConfigs.name_activities_deleate_icon)
        if hasActivities:
            API().clickElementByName(self.testcase,self.driver,self.logger,DashboardPageConfigs.name_activities_deleate_icon)


if __name__ == '__main__':
    pass
