# -*- coding:utf-8 -*-

from __init__ import *

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.update_login_password_page_configs import \
    UpdateLoginPasswordPageConfigs


class UpdateLoginPasswordPage(SuperPage):
    '''
    This is a version update page operation class.
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(UpdateLoginPasswordPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is the version upgrade page.
        '''

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger,
                                                      UpdateLoginPasswordPageConfigs.resource_id_update_login_password_title,
                                                      UpdateLoginPasswordPageConfigs.assert_view_timeout)

    def inputOldLoginPassword(self, oldPassword):
        '''
        usage: input the old login password.
        '''

        API().input_view_by_resourceID_android(self.driver, self.logger,
                                               UpdateLoginPasswordPageConfigs.resource_id_input_old_password,
                                               oldPassword)

    def inputNewLoginPassword(self, newPassword):
        '''
        usage: input the new login password.
        '''

        API().input_view_by_resourceID_android(self.driver, self.logger,
                                               UpdateLoginPasswordPageConfigs.resource_id_input_new_password,
                                               newPassword)

    def inputNewLoginPasswordAgain(self, newPasswordAgain):
        '''
        usage: input the new login password again.
        '''

        API().input_view_by_resourceID_android(self.driver, self.logger,
                                               UpdateLoginPasswordPageConfigs.resource_id_input_new_password_again,
                                               newPasswordAgain)

    def clickOnConfirm(self):
        '''
        usage: click on the confirm button.
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                               UpdateLoginPasswordPageConfigs.resource_id_confirm_button,
                                               UpdateLoginPasswordPageConfigs.click_on_button_timeout)


if __name__ == '__main__':
    pass
