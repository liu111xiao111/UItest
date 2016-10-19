# -*- coding:utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.transaction_record_page_configs import TransactionRecordPageConfigs as TRPC


class TransactionRecordPage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>我的飞凡卡=>交易记录
    '''
    def __init__(self, testcase, driver, logger):
        super(TransactionRecordPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证交易记录页面
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        TRPC.resource_id_transaction_record_title,
                                        TRPC.assert_view_timeout)

