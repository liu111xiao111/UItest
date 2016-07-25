# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.account_management_page_configs import AccountManagementPageConfigs


class AccountManagementPage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>设置=>账号管理
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

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger,
                                              AccountManagementPageConfigs.resource_id_account_management_title_st,
                                              AccountManagementPageConfigs.assert_view_timeout)

    def clickOnUpdatePassword(self):
        '''
        usage: click on the update password button.
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                       AccountManagementPageConfigs.resource_id_update_login_password_st,
                                       AccountManagementPageConfigs.click_on_button_timeout)

    def clickOnSmallAmountPasswordLessPayments(self):
        '''
        usage: click on the small account password-less payments button.
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                       AccountManagementPageConfigs.resource_id_small_amount_password_less_payments,
                                       AccountManagementPageConfigs.click_on_button_timeout)


if __name__ == '__main__':
    pass
