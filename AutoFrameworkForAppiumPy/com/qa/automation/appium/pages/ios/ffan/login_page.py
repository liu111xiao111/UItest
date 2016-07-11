# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.ios_super_page import IosSuperPage
from com.qa.automation.appium.pages.ios.ffan.login_page_configs import LoginPageConfigs


class LoginPage(IosSuperPage):
    '''
    This is a test case for login.
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
                                                      LoginPageConfigs.text_login,
                                                      LoginPageConfigs.assert_view_timeout)

    def switchToNormalLogin(self):
        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                       LoginPageConfigs.text_normal_login)

    def inputUserName(self):
        API().input_view_by_xpath_ios(self.driver, self.logger, LoginPageConfigs.xpath_user_name,
                                      LoginPageConfigs.account_name)

    def inputPassWord(self):
        API().input_view_by_xpath_ios(self.driver, self.logger, LoginPageConfigs.xpath_password,
                                      LoginPageConfigs.account_passwd)

    def clickOnLoginBtn(self):
        API().click_view_by_xpath(self.testcase, self.driver, self.logger,
                                       LoginPageConfigs.xpath_login_button)

if __name__ == '__main__':
    pass;
