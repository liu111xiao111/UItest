# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.fei_fan_activity_page_configs import FeiFanActivityPageConfigs

class FeiFanActivityPage(SuperPage):
    '''
    This is fei fan activity page operation class.
    '''


    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(FeiFanActivityPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct.
        '''

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger, FeiFanActivityPageConfigs.resource_id_fei_fan_activity_title, FeiFanActivityPageConfigs.assert_view_timeout)

if __name__ == '__main__':
    pass
