# -*- coding:utf-8 -*-

from __init__ import *

from selenium.common.exceptions import TimeoutException

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage

from com.qa.automation.appium.pages.android.ffan.small_amount_password_less_payments_page_configs import SmallAmountPasswordLessPaymentsPageConfigs

class SmallAmountPasswordLessPaymentsPage(SuperPage):
    '''
    This is small amount password-less payments page operation class.
    '''


    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(SmallAmountPasswordLessPaymentsPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct.
        '''

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger, SmallAmountPasswordLessPaymentsPageConfigs.resource_id_square_dynamic_title, SmallAmountPasswordLessPaymentsPageConfigs.assert_view_timeout)

    def clickOnSmallAmountPasswordLessPaymentsSwitch(self):
        '''
        usage: click on the small amount password-less payment switch button.
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger, SmallAmountPasswordLessPaymentsPageConfigs.resource_id_small_amount_password_less_payment_switch, SmallAmountPasswordLessPaymentsPageConfigs.click_on_button_timeout)

    def validSmallAmountPasswordLessPaymentsStatus(self):
        '''
        usage: verify whether the small amount password-lsee payment is opened.
        '''

        try:
            API().find_view_by_text_Until_android(self.driver, self.logger, SmallAmountPasswordLessPaymentsPageConfigs.text_choose_small_amount_password_less_quota, SmallAmountPasswordLessPaymentsPageConfigs.click_on_button_timeout)
            return True
        except TimeoutException:
            return False

if __name__ == '__main__':
    pass
