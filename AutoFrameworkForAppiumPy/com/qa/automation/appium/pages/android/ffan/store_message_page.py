# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.store_message_page_configs import StoreMessagePageConfigs

class StoreMessagePage(SuperPage):
    '''
    This is store message page operation class.
    '''


    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(StoreMessagePage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct.
        '''

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger, StoreMessagePageConfigs.resource_id_store_message_title, StoreMessagePageConfigs.assert_view_timeout)

if __name__ == '__main__':
    pass