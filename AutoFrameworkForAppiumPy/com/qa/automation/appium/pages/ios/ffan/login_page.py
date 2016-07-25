# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.ios_super_page import IosSuperPage
from com.qa.automation.appium.pages.ios.ffan.login_page_configs import LoginPageConfigs


class LoginPage(IosSuperPage):
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

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger,
                                              LoginPageConfigs.resource_id_login_title_st,
                                              LoginPageConfigs.assert_view_timeout)

    def switchToNormalLogin(self):
        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                       LoginPageConfigs.text_normal_login,
                                       LoginPageConfigs.click_on_button_timeout)

    def inputUserName(self):
        API().input_view_by_xpath_ios(self.driver, self.logger, LoginPageConfigs.xpath_mobile_number_tf,
                                      LoginPageConfigs.text_mobile_number)

    def inputPassWord(self):
        API().input_view_by_xpath_ios(self.driver, self.logger, LoginPageConfigs.xpath_password_tf,
                                      LoginPageConfigs.text_password)

    def clickOnLoginBtn(self):
        API().click_view_by_xpath(self.testcase, self.driver, self.logger,
                                       LoginPageConfigs.xpath_login_bt,
                                       LoginPageConfigs.click_on_button_timeout)


if __name__ == '__main__':
    pass;
