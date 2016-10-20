# -*- coding: utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.famous_details_category_page_configs import FamousDetailsCategoryPageConfigs


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
                                  name=FamousDetailsCategoryPageConfigs.text_store)

if __name__ == '__main__':
    pass;