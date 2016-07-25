# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.famous_details_category_page_configs import FamousDetailsCategoryPageConfigs


class FamousDetailsCategoryPage(SuperPage):
    '''
    作者 刘涛
    首页＝>品牌(推荐)=>详情页
    '''

    def __init__(self,testcase,driver,logger):
        self.a = 12;
        super(FamousDetailsCategoryPage, self).__init__(testcase = testcase , driver = driver,logger = logger);

    def validSelf(self):
        '''
        usage : Check "推荐" details whether loading correctly.
        '''
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                          resource_id=FamousDetailsCategoryPageConfigs.text_dashboardpage, seconds=10);
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                          resource_id=FamousDetailsCategoryPageConfigs.text_goods, seconds=10);
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                          resource_id=FamousDetailsCategoryPageConfigs.text_store, seconds=10)

if __name__ == '__main__':
    pass;