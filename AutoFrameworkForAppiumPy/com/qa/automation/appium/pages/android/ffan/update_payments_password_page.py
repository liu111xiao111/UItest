# -*- coding:utf-8 -*-

from __init__ import *

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.update_payments_password_page_configs import UpdatePaymentsPasswordPageConfigs


class UpdatePaymentsPasswordPage(SuperPage):
    '''
    This is a update payments password page operation class.
    '''


    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(UpdatePaymentsPasswordPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct page.
        '''

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger, UpdatePaymentsPasswordPageConfigs.resource_id_update_payments_password_title, UpdatePaymentsPasswordPageConfigs.assert_view_timeout)

if __name__ == '__main__':
    pass
