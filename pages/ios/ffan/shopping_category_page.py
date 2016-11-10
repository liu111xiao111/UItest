# -*- coding: utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.shopping_category_page_configs import ShoppingCategoryPageConfigs
from pages.logger import logger

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
        logger.info("Check 购物 begin")
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name=ShoppingCategoryPageConfigs.name_shopping)
        logger.info("Check 购物 end")
        API().screenShot(self.driver, "gouWu")


    def clickOnGoodsDetails(self):
        '''
        usage : 点击商品，进入商品详情页
        '''
        logger.info("Click 商品详情 begin")
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = ShoppingCategoryPageConfigs.xpath_goods_details)
        logger.info("Click 商品详情 end")


if __name__ == '__main__':
    pass;