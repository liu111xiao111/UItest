# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.meituan.my_meituan_my_order_page_configs import MyMTuanMyOrderPageConfigs as MTMOPC
from pages.logger import logger


class MyMTuanMyOrderPage(SuperPage):
    '''
    作者 刘涛
    首页=>我的=>我的订单
    '''
    def __init__(self, testcase, driver, logger):
        super(MyMTuanMyOrderPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 验证我的订单
        '''
        logger.info("Check 我的订单页面 begin")
        API().assertElementByText(self.testcase, self.driver, self.logger,
                                        MTMOPC.text_comment_title,
                                        60)
        logger.info("Check 我的订单页面 end")
