# -*- coding:utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.account_management_page_configs import AccountManagementPageConfigs


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

        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  AccountManagementPageConfigs.name_account_management_title_st,
                                  AccountManagementPageConfigs.assert_view_timeout)

    def clickOnUpdatePassword(self):
        '''
        usage: click on the update password button.
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 AccountManagementPageConfigs.name_update_login_password_st,
                                 AccountManagementPageConfigs.click_on_button_timeout)

    def clickOnSmallAmountPasswordLessPayments(self):
        '''
        usage: click on the small account password-less payments button.
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 AccountManagementPageConfigs.name_small_amount_password_less_payments,
                                 AccountManagementPageConfigs.click_on_button_timeout)


if __name__ == '__main__':
    pass
