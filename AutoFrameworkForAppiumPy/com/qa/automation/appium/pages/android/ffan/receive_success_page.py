# -*- coding:utf-8 -*-

from __init__ import *

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.receive_success_page_configs import ReceiveSuccessPageConfigs


class ReceiveSuccessPage(SuperPage):
    '''
    This is receive success page operation class.
    '''


    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(ReceiveSuccessPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct.
        '''

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger,
                                              ReceiveSuccessPageConfigs.resource_id_recieve_success_title,
                                              ReceiveSuccessPageConfigs.assert_view_timeout)

    def getPrivilegeCouponCode(self):
        '''
        usage: get the privilege coupon code.
        '''

        return None

if __name__ == '__main__':
    pass
