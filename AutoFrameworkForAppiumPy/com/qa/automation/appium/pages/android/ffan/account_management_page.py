#!/usr/bin/env python
# -*- coding:utf-8 -*-


from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.account_management_page_configs import AccountManagementPageConfigs


class AccountManagementPage(SuperPage):
    '''
    This is a version update page operation class.
    '''


    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(AccountManagementPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is the version upgrade page.
        '''

        API().assert_view_by_resourceID_Until_android(self.testcase, self.driver, self.logger, AccountManagementPageConfigs.resource_id_account_management_title, AccountManagementPageConfigs.assert_view_timeout)

    def clickOnUpdatePassword(self):
        '''
        usage: click on the update password button.
        '''

        API().click_view_by_text_android(self.testcase, self.driver, self.logger, AccountManagementPageConfigs.text_update_login_password_button, AccountManagementPageConfigs.click_on_button_timeout)

if __name__ == '__main__':
    pass
