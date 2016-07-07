# -*- coding:utf-8 -*-

from __init__ import *

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.square_dynamic_page_configs import SquareDynamicPageConfigs

class SquareDynamicPage(SuperPage):
    '''
    This is square dynamic page operation class.
    '''


    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(SquareDynamicPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct.
        '''

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger, SquareDynamicPageConfigs.resource_id_square_dynamic_title, SquareDynamicPageConfigs.assert_view_timeout)

if __name__ == '__main__':
    pass
