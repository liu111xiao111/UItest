# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.meituan.login_page_configs import LoginPageConfigs as LPC
from pages.logger import logger


#   进入应用的首页,是进入其他页面的入口
class LoginPage(SuperPage):
    '''
    作者 乔佳溪
    首页=>我的=>登录
    '''
    def __init__(self, testcase, driver, logger):
        super(LoginPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        logger.info("Check 登录页面 begin")
        API().assertElementByText(self.testcase,
                                        self.driver,
                                        self.logger,
                                        LPC.text_login,
                                        LPC.assert_timeout)
        logger.info("Check 登录页面 end")

    def inputUserName(self):
        '''
        usage: 输入用户名
        '''
        logger.info("Input 用户名 begin")
        API().inputStringByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      LPC.resource_id_user_name,
                                      LPC.account_name,
                                      LPC.assert_timeout)
        logger.info("Input 用户名 end")

    def inputPassWord(self):
        '''
        usage: 输入密码
        '''
        logger.info("Input 密码 begin")
        API().inputStringByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      LPC.resource_id_pass_word,
                                      LPC.account_passwd,
                                      LPC.assert_timeout)
        logger.info("Input 密码 end")

    def clickOnLoginBtn(self):
        '''
        usage: 点击登陆按钮
        '''
        logger.info("Click 登录 button begin")
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       LPC.resource_id_login_button,
                                       10)
        logger.info("Click 登录 button end")
