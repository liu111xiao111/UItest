# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.shopping_details_category_page_configs import \
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
        valid_text_list = [SDCPC.text_dashboard, SDCPC.text_goods, SDCPC.text_store]
        API().assertElementsByTexts(self.testcase, self.driver, self.logger,
                                    valid_text_list,
                                    10)
