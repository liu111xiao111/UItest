# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.login_page_configs import LoginPageConfigs as LPC
from pages.logger import logger

#
#   进入应用的首页,是进入其他页面的入口
class LoginPage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>登录
    '''
    def __init__(self, testcase, driver, logger):
        super(LoginPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 进入到登录页,检查登录按钮
        '''
        logger.info("Check 登录页面 begin")
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        LPC.resource_id_login_button,
                                        10)
        logger.info("Check 登录页面 end")

    def switchToNormalLogin(self):
        '''
        usage: 切换到正常登陆
        '''
        logger.info("Click 密码登录 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                LPC.text_normal_login,
                                10)
        logger.info("Click 密码登录 end")

    def validNormalLogin(self):
        '''
        usage: 验证密码登录
        '''
        logger.info("Check 密码登录页面 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                LPC.text_normal_login,
                                10)
        logger.info("Check 密码登录页面 end")

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
                                      10)
        logger.debug(LPC.account_name)
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
                                      10)
        logger.debug(LPC.account_passwd)
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
