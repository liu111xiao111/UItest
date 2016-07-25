# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.recommend_details_category_page_configs import RecommendDetailsCategoryPageConfigs

RDCPC = RecommendDetailsCategoryPageConfigs()

class RecommendDetailsCategoryPage(SuperPage):
    '''
    作者 刘涛
    首页＝>品牌(大牌)=>详情页
    '''

    def __init__(self,testcase,driver,logger):
        self.a = 12;
        super(RecommendDetailsCategoryPage, self).__init__(testcase = testcase , driver = driver,logger = logger);

    def validSelf(self):
        '''
        usage : Check "推荐" details whether loading correctly.
        '''
        API().assert_view_by_resourceID_Until(self.testcase,
                                              self.driver,
                                              self.logger,
                                              RDCPC.resource_id_tv_recommend_details_tv,
                                              seconds = 10)

    def clickOnSubsciber(self):
        '''
        usage : Click "喜欢"
        '''   
        API().click_view_by_content_desc(self.testcase,
                                         self.driver,
                                         self.logger,
                                         RDCPC.desc_like_button,
                                         seconds = 10)

    def clickCancelSubsciber(self):
        '''
        usage : Click "取消喜欢"
        '''   
        API().click_view_by_content_desc(self.testcase,
                                         self.driver,
                                         self.logger,
                                         RDCPC.desc_unlike_button,
                                         seconds = 10)


if __name__ == '__main__':
    pass;