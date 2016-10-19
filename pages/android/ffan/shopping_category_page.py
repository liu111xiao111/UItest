# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.shopping_category_page_configs import ShoppingCategoryPageConfigs as SCPC


class ShoppingCategoryPage(SuperPage):
    '''
    作者 刘涛
    首页=>购物
    '''
    def __init__(self,testcase,driver,logger):
        super(ShoppingCategoryPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 验证购物页面
        '''
        API().assertElementByText(self.testcase, self.driver, self.logger,
                                  SCPC.text_goods,
                                  10)

    def clickOnGoodsDetails(self):
        '''
        usage : 点击商品详情
        '''
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                       SCPC.xpath_goods_details,
                                       10)

    def clickOnShoppingTrolley(self):
        '''
        usage : 点击商品详情
        ''' 
        API().clickElementByResourceId(self.testcase, self.driver, self.logger,
                                       SCPC.resource_id_tv_shopping_trolley_tv,
                                       10)
