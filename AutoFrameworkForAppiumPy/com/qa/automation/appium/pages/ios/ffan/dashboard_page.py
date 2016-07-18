# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.ios_super_page import IosSuperPage
from com.qa.automation.appium.pages.ios.ffan.dashboard_page_configs import DashboardPageConfigs


'''
    usage :  进入应用的首页
'''
class DashboardPage(IosSuperPage):

    def __init__(self, testcase, driver, logger):
        super(DashboardPage, self).__init__(testcase=testcase, driver=driver, logger=logger)

    '''
        usage : 进入到应用首页,检查ffan logo
    '''
    def valid_self(self):
        # name_home_title_icon = API().get_view_by_resourceID(driver=self.driver,logger=self.logger,resource_id=DashboardPageConfigs.name_home_title_icon);
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver, logger=self.logger, resource_id=DashboardPageConfigs.name_home_title_icon, seconds=10);

    """
        点击爱逛街icon
    """
    def click_aiguangjie(self):
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver, logger=self.logger, resource_id=DashboardPageConfigs.name_app_tabbar_home_normal)


    """
        点击慧生活icon
    """
    def click_huishenghuo(self):
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                             resource_id=DashboardPageConfigs.name_app_tabbar_life_normal)


    """
        点击飞凡卡icon
    """
    def click_ffan_card(self):
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                             resource_id=DashboardPageConfigs.name_app_tabbar_card_normal)


    """
        点击我的icon
    """
    def click_my(self):
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                             resource_id=DashboardPageConfigs.name_app_tabbar_user_normal)

    def clickOnSearchAll(self):
        '''
        usage: click on search in city.
        '''
        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                       DashboardPageConfigs.resource_id_search_all_tv,
                                       DashboardPageConfigs.click_on_button_timeout)

    def clickOnMovie(self):
        '''
        usage: click on movie button
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                       DashboardPageConfigs.resource_id_movie_st,
                                       DashboardPageConfigs.click_on_button_timeout)

    def clickOnPrivilege(self):
        '''
        usage: click privilege button
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                       DashboardPageConfigs.resource_id_movieprivilege_st,
                                       DashboardPageConfigs.click_on_button_timeout)

    def validSelf(self):
        '''
        usage: verify whether the current page is conrrect.
        '''

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger,
                                              DashboardPageConfigs.name_home_title_icon,
                                              DashboardPageConfigs.assert_view_timeout)

    def waitBySeconds(self, seconds=1):
        self.wait_by_seconds(seconds)

    def clickOnHuiLife(self):
        self.click_huishenghuo()

    def clickOnFeiFanCard(self):
        self.click_ffan_card()

    def clickOnMy(self):
        self.click_my()

    def clickOnSquareModule(self):
        '''
        usage: click on the nearby business circle.
        '''

        API().click_view_by_xpath(self.testcase, self.driver, self.logger,
                                  DashboardPageConfigs.xpath_square_module_st,
                                  DashboardPageConfigs.click_on_button_timeout)

    def click_parking(self):
        '''
        usage: 点击"停车"
        '''
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                       resource_id=DashboardPageConfigs.name_parking);

    def click_shopping(self):
        '''
        usage: 点击"购物"
        '''
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                       resource_id=DashboardPageConfigs.name_shopping);

    def click_lePay(self):
        '''
        usage: 点击"乐付"
        '''
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                       resource_id=DashboardPageConfigs.name_le_pay);

    def click_brand(self):
        '''
        usage: 点击"品牌街"
        '''
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                       resource_id=DashboardPageConfigs.name_brand);

    def clickOnSalesPromotion(self):
        '''
            usage: 点击"优惠活动"
        '''
        '''        start_x = API().get_width_of_device(self.driver, self.logger)/2
        end_x = API().get_width_of_device(self.driver, self.logger)/2
        start_y = API().get_height_of_device(self.driver, self.logger)/2
        end_y = API().get_height_of_device(self.driver, self.logger)/7

        API().scroll(self.driver,
                     self.logger,
                     start_x, start_y, end_x, end_y)'''

        API().click_view_by_resourceID(self.testcase,
                                         self.driver,
                                         self.logger,
                                         DashboardPageConfigs.name_sales_promotion)


if __name__ == '__main__':
    pass
