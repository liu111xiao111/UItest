# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.recommend_details_category_page_configs import RecommendDetailsCategoryPageConfigs as RDCPC


class RecommendDetailsCategoryPage(SuperPage):
    '''
    作者 刘涛
    首页＝>品牌(大牌)=>详情页
    '''
    def __init__(self,testcase,driver,logger):
        super(RecommendDetailsCategoryPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 验证大牌详情页
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        RDCPC.resource_id_tv_recommend_details_tv,
                                        10)

    def clickOnSubsciber(self):
        '''
        usage : 点击 "喜欢"
        '''   
        API().clickElementByContentDesc(self.testcase,
                                        self.driver,
                                        self.logger,
                                        RDCPC.desc_like_button,
                                        10)

    def clickCancelSubsciber(self):
        '''
        usage : 点击 "取消喜欢"
        '''   
        API().clickElementByContentDesc(self.testcase,
                                        self.driver,
                                        self.logger,
                                        RDCPC.desc_unlike_button,
                                        10)
