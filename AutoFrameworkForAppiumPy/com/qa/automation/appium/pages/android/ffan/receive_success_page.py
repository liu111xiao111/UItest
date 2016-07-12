# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.receive_success_page_configs import ReceiveSuccessPageConfigs
from selenium.common.exceptions import TimeoutException

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

#         API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger,
#                                               ReceiveSuccessPageConfigs.resource_id_recieve_success_title,
#                                               ReceiveSuccessPageConfigs.assert_view_timeout)

        try:
            received_suc = API().find_view_by_text_Until_android(driver=self.driver, logger=self.logger, text=ReceiveSuccessPageConfigs.text_receive_success,seconds=45)
            if received_suc:
                API().assert_true(test_case=self.testcase, driver = self.driver, logger = self.logger, result=True)
        except TimeoutException as e:
            API().assert_view_by_content_desc_android(testcase=self.testcase, driver = self.driver, logger = self.logger, 
                                                       content_desc = ReceiveSuccessPageConfigs.content_desc_limit_dialog_text, seconds = 45)
            
        
    def getPrivilegeCouponCode(self):
        '''
        usage: get the privilege coupon code.
        '''

        return None

if __name__ == '__main__':
    pass
