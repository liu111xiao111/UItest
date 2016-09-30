# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.recommend_details_category_page_configs import RecommendDetailsCategoryPageConfigs as RDCPC


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
        API().clickElementByXpath(self.testcase,
                                        self.driver,
                                        self.logger,
                                        RDCPC.xpath_recommend_subscriber,
                                        10)

    def clickCancelSubsciber(self):
        '''
        usage : 点击 "取消喜欢"
        '''
        API().clickElementByXpath(self.testcase,
                                        self.driver,
                                        self.logger,
                                        RDCPC.xpath_recommend_subscriber,
                                        10)

    def validSelfSubsciberLike(self):
        '''
        usage : 新型状态是否被选中
        '''
        API().assertElementByContentDesc(self.testcase,
                                        self.driver,
                                        self.logger,
                                        RDCPC.desc_like_button,
                                        10)

    def validSelfSubsciberUnlike(self):
        '''
        usage : 新型状态是否未被选中
        '''
        API().assertElementByContentDesc(self.testcase,
                                        self.driver,
                                        self.logger,
                                        RDCPC.desc_unlike_button,
                                        10)
