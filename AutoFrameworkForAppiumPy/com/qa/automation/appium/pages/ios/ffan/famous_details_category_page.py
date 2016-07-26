# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
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
        usage : 判断 品牌"推荐"页显示是否正确
        '''
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name=FamousDetailsCategoryPageConfigs.text_dashboardpage)
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name=FamousDetailsCategoryPageConfigs.text_goods)

if __name__ == '__main__':
    pass;