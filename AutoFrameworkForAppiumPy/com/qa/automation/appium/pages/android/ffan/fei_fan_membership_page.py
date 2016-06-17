#!/usr/bin/env python
# -*- coding:utf-8 -*-


from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.fei_fan_membership_page_configs import FeiFanMembershipPageConfigs

class FeiFanMembershipPage(SuperPage):
    '''
    This is fei fan membership page operation class.
    '''


    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(FeiFanMembershipPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct page.
        '''

        API().assert_view_by_resourceID_Until_android(self.testcase, self.driver, self.logger, FeiFanMembershipPageConfigs.fei_fan_membership_title, FeiFanMembershipPageConfigs.assert_view_timeout)

if __name__ == '__main__':
    pass
