# -*- coding: utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.login_page_configs import LoginPageConfigs
from pages.logger import logger


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
        logger.info("Check 登录页面 begin")
        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  LoginPageConfigs.resource_id_login_title_st,
                                  LoginPageConfigs.assert_view_timeout)
        logger.info("Check 登录页面 end")
        API().screenShot(self.driver, "login")

    def switchToNormalLogin(self):
        logger.info("Switch 普通登录 begin")
        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 LoginPageConfigs.text_normal_login,
                                 LoginPageConfigs.click_on_button_timeout)
        logger.info("Switch 普通登录 end")
        API().screenShot(self.driver, "puTongDengLu")

    def validNormalLogin(self):
        '''
        验证普通登录,以"忘记密码?"文字,作为验证
        '''
        logger.info("Check 普通登录 begin")
        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  LoginPageConfigs.name_forget_password,
                                  LoginPageConfigs.assert_view_timeout)
        logger.info("Check 普通登录 end")

    def inputUserName(self):
        logger.info("Input 用户名 begin")
        API().inputStringByXpath(self.testcase, self.driver, self.logger,
                                 LoginPageConfigs.xpath_mobile_number_tf,
                                 LoginPageConfigs.text_mobile_number,
                                 LoginPageConfigs.input_timeout)
        logger.info("Input 用户名 end")
        API().screenShot(self.driver, "username")


    def inputPassWord(self):
        logger.info("Input 密码 begin")
        API().inputStringByXpath(self.testcase, self.driver, self.logger,
                                 LoginPageConfigs.xpath_password_tf,
                                 LoginPageConfigs.text_password,
                                 LoginPageConfigs.input_timeout)
        logger.info("Input 密码 end")
        API().screenShot(self.driver, "password")

    def clickOnLoginBtn(self):
        logger.info("Click 登录 begin")
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  LoginPageConfigs.xpath_login_bt,
                                  LoginPageConfigs.click_on_button_timeout)
        logger.info("Click 登录 end")


if __name__ == '__main__':
    pass;
