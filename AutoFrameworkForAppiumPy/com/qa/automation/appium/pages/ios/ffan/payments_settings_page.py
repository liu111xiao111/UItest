# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.payments_settings_page_configs import PaymentsSettingsPageConfigs


class PaymentsSettingsPage(SuperPage):
    '''
    This is a payments settings page operation class.
    '''


    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(PaymentsSettingsPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct page.
        '''

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger,
                                              PaymentsSettingsPageConfigs.resource_id_payments_settings_title_st,
                                              PaymentsSettingsPageConfigs.assert_view_timeout)

    def clickOnPaymentsPasswordManagement(self):
        '''
        usage: click on the payments password management button.
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                       PaymentsSettingsPageConfigs.resource_id_update_payments_password_st,
                                       PaymentsSettingsPageConfigs.click_on_button_timeout)

    def clickOnSmallAmountPasswordLessPayments(self):
        '''
        usage: click on the small amount password less payment button.
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                       PaymentsSettingsPageConfigs.resource_id_small_amount_password_less_payments_st,
                                       PaymentsSettingsPageConfigs.click_on_button_timeout)

if __name__ == '__main__':
    pass
