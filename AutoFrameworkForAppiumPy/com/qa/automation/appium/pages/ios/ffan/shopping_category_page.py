# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.shopping_category_page_configs import ShoppingCategoryPageConfigs


#   首页点击购物
class ShoppingCategoryPage(SuperPage):

    def __init__(self,testcase,driver,logger):
        self.a = 12;
        super(ShoppingCategoryPage, self).__init__(testcase = testcase , driver = driver,logger = logger);

    def validSelf(self):
        '''
        usage : 判断“购物”标题显示是否正确
        '''
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                                      resource_id=ShoppingCategoryPageConfigs.name_shopping,
                                                      seconds=18)

    def clickOnGoodsDetails(self):
        '''
        usage : 点击商品，进入商品详情页
        ''' 
        API().click_view_by_xpath(testcase = self.testcase, driver = self.driver, logger = self.logger,
                                  xpath = ShoppingCategoryPageConfigs.xpath_goods_details)


if __name__ == '__main__':
    pass;