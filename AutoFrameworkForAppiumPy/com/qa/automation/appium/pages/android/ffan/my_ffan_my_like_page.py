# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.my_ffan_my_like_page_configs import MyFfanMyLikePageConfigs as MLPC


class MyFfanMyLikePage(SuperPage):
    '''
    作者 刘涛
    首页=>我的=>我的喜欢
    '''
    def __init__(self, testcase, driver, logger):
        super(MyFfanMyLikePage, self).__init__(testcase, driver, logger);

    def validSelf(self):
        '''
        usage : 验证我的喜欢
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        MLPC.resource_id_tv_my_like_tv,
                                        MLPC.verify_view_timeout)

    def clickOnLikeGoods(self):
        '''
        usage : 点击商品
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MLPC.text_like_goods,
                                 MLPC.verify_view_timeout)

    def clickOnLikeDissertation(self):
        '''
        usage : 点击专题
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MLPC.text_like_dissertation,
                                 MLPC.verify_view_timeout)

    def clickOnLikeBrand(self):
        '''
        usage : 点击品牌 
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MLPC.text_like_brand,
                                 MLPC.verify_view_timeout)

    def validSelfGoods(self):
        '''
        usage : 验证商品
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        MLPC.verify_goods_view_resourceId,
                                        MLPC.verify_view_timeout)

    def validSelfDissertation(self):
        '''
        usage : 验证专题
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        MLPC.verify_dissertation_view_resourceId,
                                        MLPC.verify_view_timeout)

    def validSelfBrand(self):
        '''
        usage : 验证品牌
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        MLPC.verify_brand_view_resourceId,
                                        MLPC.verify_view_timeout)
