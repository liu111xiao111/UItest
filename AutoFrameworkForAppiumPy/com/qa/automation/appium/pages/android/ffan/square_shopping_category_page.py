# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.square_shopping_category_page_configs import SquareShoppingPageConfigs as SSPC


class SquareShoppingPage(SuperPage):
    '''
    作者 宋波
    首页=>广场=>爱购物
    '''
    def __init__(self, testcase, driver, logger):
        super(SquareShoppingPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 进入广场模块，检查是否加载出来
        '''
        API().assertElementByResourceId(self.testcase, self.driver, self.logger,
                                        SSPC.resource_id_iv_find_iv,
                                        10)

    def clickOnSubCommodity(self):
        '''
        usage: 点击商品
        '''
        tempText = API().getTextByResourceId(self.testcase, self.driver, self.logger,
                                             SSPC.resource_id_sub_commodity_button,
                                             10)
        API().clickElementByResourceId(self.testcase, self.driver, self.logger,
                                       SSPC.resource_id_sub_commodity_button,
                                       SSPC.click_on_button_timeout)

        return tempText
