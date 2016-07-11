# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.sharing_page_configs import SharingPageConfigs

class SharingPage(SuperPage):
    '''
    This is sharing page operation class.
    '''


    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(SharingPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct page.
        '''

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger,
                                              SharingPageConfigs.resource_id_cancel_bt,
                                              SharingPageConfigs.assert_view_timeout)

    def validKeywords(self, keywords):
        '''
        usage: verify whether the keyword is correct.
        '''

        print("KEYWORDS: %s" % keywords)

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger, keywords,
                                              SharingPageConfigs.assert_view_timeout)

    def clickOnCancel(self):
        '''
        usage: click cancel button
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                       SharingPageConfigs.resource_id_cancel_bt,
                                       SharingPageConfigs.click_on_button_timeout)

if __name__ == '__main__':
    pass
