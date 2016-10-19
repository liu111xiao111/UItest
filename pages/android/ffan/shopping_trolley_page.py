# -*- coding:utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.shopping_trolley_page_configs import ShoppingTrolleyPageConfigs as STPC


class ShoppingTrolleyPage(SuperPage):
    '''
    作者 刘涛
    首页＝>名店优品＝>购物车
    '''
    def __init__(self, testcase, driver, logger):
        super(ShoppingTrolleyPage, self).__init__(testcase , driver, logger)

    def validSelf(self):
        '''
        usage : 进入购物车页面，根据购物车的textview,检查找购物车页面是否加载出来.
        '''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  STPC.text_shopping_trolley,
                                  STPC.verify_button_timeout)
