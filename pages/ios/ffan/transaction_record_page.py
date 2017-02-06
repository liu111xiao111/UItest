# -*- coding:utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.transaction_record_page_configs import TransactionRecordPageConfigs


class TransactionRecordPage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>我的飞凡卡=>交易记录
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(TransactionRecordPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct page.
        '''

        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  TransactionRecordPageConfigs.name_transaction_record_title_st,
                                  TransactionRecordPageConfigs.assert_view_timeout)


if __name__ == '__main__':
    pass
