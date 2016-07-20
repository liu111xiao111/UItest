# -*- coding: utf-8 -*-

from com.qa.automation.appium.pages.ios.ffan.my_ffan_my_like_page_configs import MyFfanMyLikePageConfigs
from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage

MLPC = MyFfanMyLikePageConfigs()

class MyFfanMyLikePage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(MyFfanMyLikePage, self).__init__(testcase,
                                               driver,
                                               logger);

    def validSelf(self):
        '''
        usage : 判断“我的喜欢”navigation bar显示是否正确
        '''
        navigation = API().find_view_by_uia_string_until_ios(driver=self.driver,logger=self.logger,uia_string=".navigationBars()[0]")
        API().assert_equal(test_case=self.testcase,driver=self.driver,logger=self.logger,
                           actual_text=navigation.get_attribute("name"),expect_text=MyFfanMyLikePageConfigs.name_tv_my_like_tv)

    def clickOnLikeGoods(self):
        '''
        usage : Click "商品" in my order page， and load "商品" tab correctly. 
        '''
        API().click_view_by_ios_uiautomation(self.testcase,
                                             self.driver,
                                             self.logger,
                                             MLPC.uia_string_like_goods)

    def clickOnLikeDissertation(self):
        '''
        usage : Click "专题" in my order page， and load "专题" tab correctly. 
        '''
        API().click_view_by_ios_uiautomation(self.testcase,
                                             self.driver,
                                             self.logger,
                                             MLPC.uia_string_like_dissertation)

    def clickOnLikeBrand(self):
        '''
        usage : Click "品牌" in my order page， and load "品牌" tab correctly. 
        '''
        API().click_view_by_ios_uiautomation(self.testcase,
                                             self.driver,
                                             self.logger,
                                             MLPC.uia_string_like_brand)


if __name__ == '__main__':
    pass;