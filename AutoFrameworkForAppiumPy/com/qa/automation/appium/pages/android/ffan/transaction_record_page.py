# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.transaction_record_page_configs import TransactionRecordPageConfigs


class TransactionRecordPage(SuperPage):
    '''
    This is a transaction record page operation class.
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

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger, TransactionRecordPageConfigs.resource_id_transaction_record_title, TransactionRecordPageConfigs.assert_view_timeout)

if __name__ == '__main__':
    pass
