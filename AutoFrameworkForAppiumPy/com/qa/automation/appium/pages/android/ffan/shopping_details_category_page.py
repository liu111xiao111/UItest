# -*- coding: utf-8 -*-

import os

#sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.shopping_details_category_page_configs import ShoppingDetailsCategoryPageConfigs

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(_), p)
)


#   购物点击商品详情页
class ShoppingDetailsCategoryPage(SuperPage):

    def __init__(self,testcase,driver,logger):
        self.a = 12;
        super(ShoppingDetailsCategoryPage, self).__init__(testcase = testcase , driver = driver,logger = logger);

    def validSelf(self):
        '''
        usage : Check "商品" details whether loading correctly.
        '''
        API().assert_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                          text=ShoppingDetailsCategoryPageConfigs.text_dashboard, seconds=10);
        API().assert_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                          text=ShoppingDetailsCategoryPageConfigs.text_goods, seconds=10);
        API().assert_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                          text=ShoppingDetailsCategoryPageConfigs.text_store, seconds=10);


if __name__ == '__main__':
    pass;