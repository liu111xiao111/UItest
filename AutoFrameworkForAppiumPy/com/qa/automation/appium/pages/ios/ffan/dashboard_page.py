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

    def clickOnSearchView(self):
        '''
        usage: click on search in city.
        '''
        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                       DashboardPageConfigs.resource_id_tv_search_tv,
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

    def clickOnSquareModule(self):
        '''
        usage: click on the nearby business circle.
        '''

        API().click_view_by_xpath(self.testcase, self.driver, self.logger,
                                  DashboardPageConfigs.xpath_square_module_st,
                                  DashboardPageConfigs.click_on_button_timeout)

    def click_Parking(self):
        '''
        usage: click on "停车".
        '''
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                       resource_id=DashboardPageConfigs.name_parking);

if __name__ == '__main__':
    pass
