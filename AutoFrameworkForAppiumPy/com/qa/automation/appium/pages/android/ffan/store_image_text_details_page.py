#!/usr/bin/env python
# -*- coding: utf-8 -*-


from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.store_image_text_details_page_configs import StoreImageTextDetailsPageConfigs


class StoreImageTextDetailsPage(SuperPage):
    '''
    This is a store image text details page operation class.
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(StoreImageTextDetailsPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct.
        '''

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger, StoreImageTextDetailsPageConfigs.resource_id_store_image_text_details, StoreImageTextDetailsPageConfigs.assert_view_timeout)

    def validKeywords(self, keywords):
        '''
        usage: verify whether the keyword is correct.
        '''

        print("KEYWORDS: %s" % keywords)

        API().assert_view_by_content_desc_android(self.testcase, self.driver, self.logger, keywords, StoreImageTextDetailsPageConfigs.assert_view_timeout)

if __name__ == '__main__':
    pass
