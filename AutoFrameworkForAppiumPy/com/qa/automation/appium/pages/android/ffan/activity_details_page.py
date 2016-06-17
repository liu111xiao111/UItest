#!/usr/bin/env python
# -*- coding:utf-8 -*-


from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.activity_details_page_configs import ActivityDetailsPageConfigs

class ActivityDetailsPage(SuperPage):
    '''
    This is hui life page operation class.
    '''


    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(ActivityDetailsPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct page.
        '''

        API().assert_view_by_resourceID_Until_android(self.testcase, self.driver, self.logger, ActivityDetailsPageConfigs.resource_id_activity_details_title, ActivityDetailsPageConfigs.assert_view_timeout)

if __name__ == '__main__':
    pass