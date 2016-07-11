# -*- coding: utf-8 -*-

from com.qa.automation.appium.pages.android.ffan.my_ffan_my_like_page_configs import MyFfanMyLikePageConfigs
from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage

MLPC = MyFfanMyLikePageConfigs()

class MyFfanMyLikePage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(MyFfanMyLikePage, self).__init__(testcase,
                                               driver,
                                               logger);

    def validSelf(self):
        '''
        usage : Load "我的喜欢" page， according to textview in "我的喜欢", check "我的喜欢" page whether load correctly.
        '''
        API().assert_view_by_resourceID_Until(self.testcase,
                                              self.driver,
                                              self.logger,
                                              MLPC.resource_id_tv_my_like_tv)

    def clickOnLikeGoods(self):
        '''
        usage : Click "商品" in my order page， and load "商品" tab correctly. 
        '''
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         MLPC.text_like_goods)

    def clickOnLikeDissertation(self):
        '''
        usage : Click "专题" in my order page， and load "专题" tab correctly. 
        '''
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         MLPC.text_like_dissertation)

    def clickOnLikeBrand(self):
        '''
        usage : Click "品牌" in my order page， and load "品牌" tab correctly. 
        '''
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         MLPC.text_like_brand)

    def validSelfGoods(self):
        '''
        usage : Load "商品" correctly.
        '''
        API().assert_view_by_resourceID_Until(self.testcase,
                                                self.driver,
                                                self.logger,
                                                MLPC.verify_goods_view_resourceId,
                                                MLPC.verify_view_timeout);

    def validSelfDissertation(self):
        '''
        usage : Load "专题" correctly.
        '''
        API().assert_view_by_resourceID_Until(self.testcase,
                                                self.driver,
                                                self.logger,
                                                MLPC.verify_dissertation_view_resourceId,
                                                MLPC.verify_view_timeout);

    def validSelfBrand(self):
        '''
        usage : Load "品牌" correctly.
        '''

        API().assert_view_by_resourceID_Until(self.testcase,
                                                self.driver,
                                                self.logger,
                                                MLPC.verify_brand_view_resourceId,
                                                MLPC.verify_view_timeout);

if __name__ == '__main__':
    pass;