# -*- coding:utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.update_login_password_page_configs import UpdateLoginPasswordPageConfigs


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

        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  UpdateLoginPasswordPageConfigs.name_update_login_password_title_st,
                                  UpdateLoginPasswordPageConfigs.assert_view_timeout)

    def inputOldLoginPassword(self, oldPassword):
        '''
        usage: input the old login password.
        '''

        API().inputStringByXpath(self.testcase, self.driver, self.logger,
                                 UpdateLoginPasswordPageConfigs.xpath_input_old_password_stf,
                                 oldPassword, UpdateLoginPasswordPageConfigs.input_timeout)

    def inputNewLoginPassword(self, newPassword):
        '''
        usage: input the new login password.
        '''

        API().inputStringByXpath(self.testcase, self.driver, self.logger,
                                 UpdateLoginPasswordPageConfigs.xpath_input_new_password_stf,
                                 newPassword, UpdateLoginPasswordPageConfigs.input_timeout)

    def inputNewLoginPasswordAgain(self, newPasswordAgain):
        '''
        usage: input the new login password again.
        '''

        API().inputStringByXpath(self.testcase, self.driver, self.logger,
                                 UpdateLoginPasswordPageConfigs.xpath_input_new_password_again_stf,
                                 newPasswordAgain, UpdateLoginPasswordPageConfigs.input_timeout)

    def clickOnConfirm(self):
        '''
        usage: click on the confirm button.
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 UpdateLoginPasswordPageConfigs.resource_id_confirm_bt,
                                 UpdateLoginPasswordPageConfigs.click_on_button_timeout)


if __name__ == '__main__':
    pass
