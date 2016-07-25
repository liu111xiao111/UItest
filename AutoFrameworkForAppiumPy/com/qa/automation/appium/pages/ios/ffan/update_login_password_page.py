# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.update_login_password_page_configs import UpdateLoginPasswordPageConfigs


class UpdateLoginPasswordPage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>设置=>账号管理=>修改登录密码
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
                                              UpdateLoginPasswordPageConfigs.resource_id_update_login_password_title_st,
                                              UpdateLoginPasswordPageConfigs.assert_view_timeout)

    def inputOldLoginPassword(self, oldPassword):
        '''
        usage: input the old login password.
        '''

        API().input_view_by_xpath_ios(self.driver, self.logger,
                                      UpdateLoginPasswordPageConfigs.xpath_input_old_password_stf,
                                      oldPassword)

    def inputNewLoginPassword(self, newPassword):
        '''
        usage: input the new login password.
        '''

        API().input_view_by_xpath_ios(self.driver, self.logger,
                                      UpdateLoginPasswordPageConfigs.xpath_input_new_password_stf,
                                      newPassword)

    def inputNewLoginPasswordAgain(self, newPasswordAgain):
        '''
        usage: input the new login password again.
        '''

        API().input_view_by_xpath_ios(self.driver, self.logger,
                                      UpdateLoginPasswordPageConfigs.xpath_input_new_password_again_stf,
                                      newPasswordAgain)

    def clickOnConfirm(self):
        '''
        usage: click on the confirm button.
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                       UpdateLoginPasswordPageConfigs.resource_id_confirm_bt,
                                       UpdateLoginPasswordPageConfigs.click_on_button_timeout)


if __name__ == '__main__':
    pass
