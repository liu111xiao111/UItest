# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.store_message_page_configs import StoreMessagePageConfigs

class StoreMessagePage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>消息中心=>店消息
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

        API().assertElementByResourceId(self.testcase, self.driver, self.logger,
                                        StoreMessagePageConfigs.resource_id_store_message_title_st,
                                        StoreMessagePageConfigs.assert_view_timeout)


if __name__ == '__main__':
    pass
