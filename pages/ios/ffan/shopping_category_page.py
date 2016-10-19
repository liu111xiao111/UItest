# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.shopping_category_page_configs import ShoppingCategoryPageConfigs


class ShoppingCategoryPage(SuperPage):
    '''
    作者 刘涛
    首页=>购物
    '''

    def __init__(self,testcase,driver,logger):
        self.a = 12;
        super(ShoppingCategoryPage, self).__init__(testcase = testcase , driver = driver,logger = logger);

    def validSelf(self):
        '''
        usage : 判断“购物”标题显示是否正确
        '''
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name=ShoppingCategoryPageConfigs.name_shopping)

    def clickOnGoodsDetails(self):
        '''
        usage : 点击商品，进入商品详情页
        '''
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = ShoppingCategoryPageConfigs.xpath_goods_details)


if __name__ == '__main__':
    pass;