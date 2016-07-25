# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.recommend_details_category_page_configs import RecommendDetailsCategoryPageConfigs

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
        usage : 进入推荐商品详细页
        '''
        API().assert_view_by_xpath_android(self.testcase, self.driver, self.logger,
                                           RDCPC.xpath_recommend_subscriber,
                                           seconds = 10)

    def clickOnSubsciber(self):
        '''
        usage : 点击 "喜欢"
        '''   
        API().click_view_by_xpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  RDCPC.xpath_recommend_subscriber,
                                  seconds = 10)

    def getSubsciberNumber(self):
        '''
        usage : 取得 "喜欢"数
        '''   
        subsciberNumber = API().get_view_by_xpath_ios(self.driver,
                                                      self.logger,
                                                      RDCPC.xpath_subcriber_number).text
        return subsciberNumber

    def validSelfSubsciberNumber(self, originalNumber, newNumber):
        '''
        usage : 判断 "喜欢"数是否正确
        '''   
        API().assert_equal(self.testcase,
                                         self.driver,
                                         self.logger,
                                         originalNumber,
                                         newNumber)


if __name__ == '__main__':
    pass;