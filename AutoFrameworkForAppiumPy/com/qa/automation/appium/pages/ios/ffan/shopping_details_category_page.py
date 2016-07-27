# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.shopping_details_category_page_configs import ShoppingDetailsCategoryPageConfigs


class ShoppingDetailsCategoryPage(SuperPage):
    '''
    作者 刘涛
    首页=>购物=>详情页
    '''

    def __init__(self,testcase,driver,logger):
        self.a = 12;
        super(ShoppingDetailsCategoryPage, self).__init__(testcase = testcase , driver = driver,logger = logger);

    def validSelf(self):
        '''
        usage : 判断商品详情页中“首页”、“商品”、“门店”显示是否正确
        '''
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name=ShoppingDetailsCategoryPageConfigs.text_dashboard)
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name=ShoppingDetailsCategoryPageConfigs.text_goods)
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name=ShoppingDetailsCategoryPageConfigs.text_store)


if __name__ == '__main__':
    pass;