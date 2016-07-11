# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.brand_activity_page_configs import BrandActivityPageConfigs


class BrandActivityPage(SuperPage):
    '''
    This is square dynamic page operation class.
    '''


    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(BrandActivityPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct.
        '''

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger, BrandActivityPageConfigs.resource_id_square_dynamic_title, BrandActivityPageConfigs.assert_view_timeout)

if __name__ == '__main__':
    pass
