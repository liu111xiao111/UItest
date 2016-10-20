# -*- coding: utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.my_ffan_my_like_page_configs import MyFfanMyLikePageConfigs


MLPC = MyFfanMyLikePageConfigs()

class MyFfanMyLikePage(SuperPage):
    '''
    作者 刘涛
    首页=>我的=>我的喜欢
    '''

    def __init__(self, testcase, driver, logger):
        super(MyFfanMyLikePage, self).__init__(testcase,
                                               driver,
                                               logger);

    def validSelf(self):
        '''
        usage : 判断“我的喜欢”navigation bar显示是否正确
        '''
        navigation = API().validElementByIosUiautomation(driver=self.driver,
                                                         logger=self.logger, uiaString=".navigationBars()[0]")
        API().assertEqual(testCase=self.testcase,
                          logger=self.logger,
                          actualText=navigation.get_attribute("name"),
                          expectText=MyFfanMyLikePageConfigs.name_tv_my_like_tv)

    def clickOnLikeGoods(self):
        '''
        usage : Click "商品" in my order page， and load "商品" tab correctly.
        '''
        API().clickElementByIosUiautomation(self.testcase,
                                             self.driver,
                                             self.logger,
                                             MLPC.uia_string_like_goods)

    def clickOnLikeDissertation(self):
        '''
        usage : Click "专题" in my order page， and load "专题" tab correctly.
        '''
        API().clickElementByIosUiautomation(self.testcase,
                                             self.driver,
                                             self.logger,
                                             MLPC.uia_string_like_dissertation)

    def clickOnLikeBrand(self):
        '''
        usage : Click "品牌" in my order page， and load "品牌" tab correctly.
        '''
        API().clickElementByIosUiautomation(self.testcase,
                                             self.driver,
                                             self.logger,
                                             MLPC.uia_string_like_brand)

    def validKeyword(self, keyword):
        '''
        usage: verify whether the keyword is in the list.
        '''

#         API.iosScrollToElement(self, driver, logger, elementFullXpath, elementName, direction)

if __name__ == '__main__':
    pass;
