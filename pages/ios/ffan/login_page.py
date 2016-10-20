# -*- coding: utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.login_page_configs import LoginPageConfigs


class LoginPage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>登录
    '''

    def __init__(self, testcase, driver, logger):
        '''
        constructor
        '''

        super(LoginPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is the switch city page.
        '''

        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  LoginPageConfigs.resource_id_login_title_st,
                                  LoginPageConfigs.assert_view_timeout)

    def switchToNormalLogin(self):
        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 LoginPageConfigs.text_normal_login,
                                 LoginPageConfigs.click_on_button_timeout)

    def inputUserName(self):
        API().inputStringByXpath(self.testcase, self.driver, self.logger,
                                 LoginPageConfigs.xpath_mobile_number_tf,
                                 LoginPageConfigs.text_mobile_number,
                                 LoginPageConfigs.input_timeout)

    def inputPassWord(self):
        API().inputStringByXpath(self.testcase, self.driver, self.logger,
                                 LoginPageConfigs.xpath_password_tf,
                                 LoginPageConfigs.text_password,
                                 LoginPageConfigs.input_timeout)

    def clickOnLoginBtn(self):
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  LoginPageConfigs.xpath_login_bt,
                                  LoginPageConfigs.click_on_button_timeout)


if __name__ == '__main__':
    pass;
