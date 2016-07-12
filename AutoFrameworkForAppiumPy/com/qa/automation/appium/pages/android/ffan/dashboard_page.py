# -*- coding: utf-8 -*-
import sys,os
from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.dashboard_page_configs import DashboardPageConfigs

'''
    usage :  进入应用的首页
'''
class DashboardPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(DashboardPage, self).__init__(testcase=testcase, driver=driver, logger=logger)

    '''
        usage : 进入到应用首页,检查ffan logo
    '''

    def validSelf(self):
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                                      resource_id=DashboardPageConfigs.resource_id__iv_logo__iv, seconds=30)

    def validSelfByText(self, text=DashboardPageConfigs.text_city_beijing):
        '''
            usage: verify whether the current page is valid by the text.
        '''

        API().assert_view_by_text_android(self.testcase, self.driver, self.logger, text,
                                          DashboardPageConfigs.verify_view_timeout)

    '''
        usage： 点击我的个人信息
    '''

    def clickOnMy(self):
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=DashboardPageConfigs.text_mine)

    def clickOnSmartLife(self):
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=DashboardPageConfigs.text_huishenghuo)

    '''
       usage: 点击美食类目
    '''

    def clickOnFood(self):
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=DashboardPageConfigs.text_food)

    '''
       usage: 点击亲子类目
    '''

    def clickOnChildCategory(self):
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=DashboardPageConfigs.text_child)

    '''
       usage: 点击广场模块
    '''

    def clickOnSquareModule(self):
        API().click_view_by_xpath(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                  xpath=DashboardPageConfigs.xpath_square_module)

    '''
        usage: 点击飞凡卡
    '''

    def clickOnFeiFanCard(self):
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=DashboardPageConfigs.text_feifan_card)

    '''
        usage: 点击返回dashboardpage
    '''
    def clickLikeShopping(self):
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=DashboardPageConfigs.text_aiguangjie)

    def clickOnHomeShakeTips(self):
        '''
            usage: 点击摇一摇提示框
        '''
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                               resource_id=DashboardPageConfigs.resource_id_iv_home_shake_tips)

    def clickOnLefuCategory(self):
        '''
            usage: 点击"乐付"类目
        '''
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=DashboardPageConfigs.text_lefu)

    def clickOnFlashSalesMore(self):
        '''
        usage: click flash sales more button
        '''

        tempWidth = API().get_width_of_device(self.driver, self.logger)
        tempHeight = API().get_height_of_device(self.driver, self.logger)
        API().scroll(self.driver, self.logger, tempWidth / 2, tempHeight * 2 / 3, tempWidth / 2, tempHeight / 3)
        API().scroll_to_text(self.driver, self.logger, DashboardPageConfigs.text_flash_sales_more_button)

    def clickOnParkingCategory(self):
        '''
            usage: 点击"停车"类目
        '''
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger, text=DashboardPageConfigs.text_parking);

    def clickOnPrivilege(self):
        '''
        usage: click privilege button
        '''

        API().click_view_by_text_android(self.testcase, self.driver, self.logger, DashboardPageConfigs.text_privilege_button, DashboardPageConfigs.click_on_button_timeout)

    def clickOnShoppingMall(self):
        '''
        usage: click shopping mall button
        '''

        API().click_view_by_text_android(self.testcase, self.driver, self.logger, DashboardPageConfigs.text_shopping_mall_button, DashboardPageConfigs.click_on_button_timeout)

    def clickOnSearchAll(self):
        '''
        usage: click on search all button
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger, DashboardPageConfigs.resource_id_search_all_button, DashboardPageConfigs.click_on_button_timeout)

    def clickOnSearchView(self):
        '''
            usage:点击全城搜索
        '''
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver, logger=self.logger, resource_id=DashboardPageConfigs.resource_id_tv_search_tv)

    def clickOnBrandCategory(self):
        '''
            usage: 点击"品牌"类目
        '''
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger, text=DashboardPageConfigs.text_brand);

    def clickOnSalesPromotion(self):
        '''
            usage: 点击"优惠活动"
        '''
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger, text=DashboardPageConfigs.text_sales_promotion);

    def clickOnSales(self):
        '''
            usage: 点击"优惠"类目
        '''

        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger, text=DashboardPageConfigs.text_sales);

    def clickOnMovie(self):
        '''
        usage: click on movie button
        '''

        API().click_view_by_text_android(self.testcase, self.driver, self.logger, DashboardPageConfigs.text_movie_button, DashboardPageConfigs.click_on_button_timeout)

    def clickOnShoppingCategory(self):
        '''
            usage: 点击"购物"类目
        '''
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=DashboardPageConfigs.text_shopping);


if __name__ == '__main__':
    print("path %s" % (sys.path))
