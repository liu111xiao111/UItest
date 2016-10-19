# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.shopping_details_category_page_configs import \
    ShoppingDetailsCategoryPageConfigs as SDCPC


class ShoppingDetailsCategoryPage(SuperPage):
    '''
    作者 刘涛
    首页=>购物=>详情页
    '''
    def __init__(self,testcase,driver,logger):
        super(ShoppingDetailsCategoryPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 验证详情页
        '''
        API().assertElementByText(self.testcase, self.driver, self.logger,
                                    SDCPC.text_goods,
                                    10)
