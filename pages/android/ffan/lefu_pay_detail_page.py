# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.lefu_pay_detail_page_configs import LefuPayDetailPageConfigs as LPDPC


class LefuPayDetailPage(SuperPage):
    '''
    作者 刘涛
    首页=>乐付=>输入乐付消费金额页
    '''
    def __init__(self, testcase, driver, logger):
        super(LefuPayDetailPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 验证乐付消费输入页
        '''
        API().assertElementByResourceId(self.testcase, self.driver, self.logger,
                                        LPDPC.resource_id_store_title,
                                        18)

    def inputMoney(self):
        '''
        usage : 输入金额
        '''
        API().inputStringByResourceId(self.testcase, self.driver, self.logger,
                                      LPDPC.resource_id_total_money,
                                      LPDPC.total_money,
                                      10)

    def clickOnPay(self):
        '''
        usage : 点击 "确认购买"
        '''
        API().clickElementByResourceId(self.testcase, self.driver, self.logger,
                                       LPDPC.resource_id_pay,
                                       10)
