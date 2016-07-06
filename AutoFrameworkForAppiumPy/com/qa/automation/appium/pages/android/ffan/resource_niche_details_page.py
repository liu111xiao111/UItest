#!/usr/bin/env python
# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.resource_niche_details_page_configs import ResourceNicheDetailsPageConfigs

RNDPC = ResourceNicheDetailsPageConfigs()

class ResourceNicheDetailsPage(SuperPage):
    '''
    This is resource niche page operation class.
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''
        super(ResourceNicheDetailsPage, self).__init__(testcase,
                                                       driver,
                                                       logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct page.
        '''
        API().assert_view_by_resourceID_Until(self.testcase,
                                              self.driver,
                                              self.logger,
                                              RNDPC.resource_id_reource_niche_details_title,
                                              RNDPC.assert_view_timeout)


if __name__ == '__main__':
    pass
