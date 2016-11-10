# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.shanghu.denglu_page_configs import DengLuPageConfigs as DLPC
from pages.logger import logger


class DengLuPage(SuperPage):
    '''
    作者 乔佳溪
    登录
    '''
    def __init__(self, testcase, driver, logger):
        super(DengLuPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 进入到登录页,检查登录标题
        '''
        logger.info("Check 登录页面 begin")
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        DLPC.resource_id_title,
                                        DLPC.assert_timeout)
        logger.info("Check 登录页面 end")

    def inputUserName(self):
        '''
        usage: 输入用户名
        '''
        logger.info("Input 用户名 begin")
        API().inputStringByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      DLPC.resource_id_user_name,
                                      DLPC.account_name,
                                      DLPC.assert_timeout)
        logger.info("Input 用户名 end")

    def inputPassWord(self):
        '''
        usage: 输入密码
        '''
        logger.info("Input 密码 begin")
        API().inputStringByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      DLPC.resource_id_pass_word,
                                      DLPC.account_passwd,
                                      DLPC.assert_timeout)
        logger.info("Input 密码 end")

    def clickOnLoginBtn(self):
        '''
        usage: 点击登录按钮
        '''
        logger.info("Click 登录 button begin")
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       DLPC.resource_id_login_button,
                                       DLPC.assert_timeout)
        logger.info("Click 登录 button end")

    def validPassword(self):
        '''
        usage : 验证密码为空
        '''
        logger.info("Check 验证密码为空 begin")
        password = API().getTextByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        DLPC.resource_id_pass_word,
                                        DLPC.assert_timeout)

        API().assertEqual(self.testcase, self.logger, password, DLPC.default_passwd)
        logger.info("Check 验证密码为空 end")

    def inputMemberPhoneNumber(self):
        '''
        usage: 输入手机号
        '''
        logger.info("Input 手机号 begin")
        API().inputStringByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      DLPC.resource_id_user_name,
                                      DLPC.member_phone,
                                      DLPC.assert_timeout)
        logger.info("Input 手机号 end")

    def inputMemberDefaultPassword(self):
        '''
        usage: 输入默认密码
        '''
        logger.info("Input 默认密码 begin")
        API().inputStringByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      DLPC.resource_id_pass_word,
                                      DLPC.member_password,
                                      DLPC.assert_timeout)
        logger.info("Input 默认密码 end")
