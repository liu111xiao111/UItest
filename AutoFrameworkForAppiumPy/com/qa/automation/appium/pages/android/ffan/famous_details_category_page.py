# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.famous_details_category_page_configs import FamousDetailsCategoryPageConfigs


#   首页点击推荐，显示详情页
class FamousDetailsCategoryPage(SuperPage):

    def __init__(self,testcase,driver,logger):
        self.a = 12;
        super(FamousDetailsCategoryPage, self).__init__(testcase = testcase , driver = driver,logger = logger);

    def validSelf(self):
        '''
        usage : Check "推荐" details whether loading correctly.
        '''
        API().assert_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                          text=FamousDetailsCategoryPageConfigs.text_dashboardpage, seconds=10);
        API().assert_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                          text=FamousDetailsCategoryPageConfigs.text_goods, seconds=10);
        API().assert_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                          text=FamousDetailsCategoryPageConfigs.text_store, seconds=10)

if __name__ == '__main__':
    pass;