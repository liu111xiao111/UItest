# -*- coding: utf-8 -*-

from __init__ import *

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.shopping_category_page_configs import ShoppingCategoryPageConfigs


#   首页点击购物，显示商品页
class ShoppingCategoryPage(SuperPage):

    def __init__(self,testcase,driver,logger):
        self.a = 12;
        super(ShoppingCategoryPage, self).__init__(testcase = testcase , driver = driver,logger = logger);

    def validSelf(self):
        '''
        usage : Check "商品" details whether loading correctly.
        '''
        API().assert_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                          text=ShoppingCategoryPageConfigs.text_goods, seconds=10);

    def clickOnGoodsDetails(self):
        '''
        usage : Enter recommend details page
        ''' 
        API().click_view_by_resourceID(testcase = self.testcase, driver = self.driver, logger = self.logger,
                                       resource_id = ShoppingCategoryPageConfigs.resource_id_tv_goods_details_tv); 


if __name__ == '__main__':
    pass;