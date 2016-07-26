# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.update_login_password_page_configs import \
    UpdateLoginPasswordPageConfigs as UPPC


class UpdateLoginPasswordPage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>设置=>账号管理=>修改登录密码
    '''
    def __init__(self, testcase, driver, logger):
        super(UpdateLoginPasswordPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证修改登录密码页面
        '''
        API().assertElementByResourceId(self.testcase, self.driver, self.logger,
                                        UPPC.resource_id_update_login_password_title,
                                        UPPC.assert_view_timeout)

    def inputOldLoginPassword(self, oldPassword):
        '''
        usage: 输入旧密码
        '''
        API().inputStringByResourceId(self.testcase, self.driver, self.logger,
                                      UPPC.resource_id_input_old_password,
                                      oldPassword,
                                      UPPC.assert_view_timeout)

    def inputNewLoginPassword(self, newPassword):
        '''
        usage: 输入新密码
        '''
        API().inputStringByResourceId(self.testcase, self.driver, self.logger,
                                      UPPC.resource_id_input_new_password,
                                      newPassword,
                                      UPPC.assert_view_timeout)

    def inputNewLoginPasswordAgain(self, newPasswordAgain):
        '''
        usage: 再次输入新密码
        '''
        API().inputStringByResourceId(self.testcase, self.driver, self.logger,
                                      UPPC.resource_id_input_new_password_again,
                                      newPasswordAgain,
                                      UPPC.assert_view_timeout)

    def clickOnConfirm(self):
        '''
        usage: 点击确认
        '''
        API().clickElementByResourceId(self.testcase, self.driver, self.logger,
                                       UPPC.resource_id_confirm_button,
                                       UPPC.click_on_button_timeout)
