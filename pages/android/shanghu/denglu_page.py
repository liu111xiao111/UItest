# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.shanghu.denglu_page_configs import DengLuPageConfigs as DLPC


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
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        DLPC.resource_id_title,
                                        DLPC.assert_timeout)

    def inputUserName(self):
        '''
        usage: 输入用户名
        '''
        API().inputStringByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      DLPC.resource_id_user_name,
                                      DLPC.account_name,
                                      DLPC.assert_timeout)

    def inputPassWord(self):
        '''
        usage: 输入密码
        '''
        API().inputStringByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      DLPC.resource_id_pass_word,
                                      DLPC.account_passwd,
                                      DLPC.assert_timeout)

    def clickOnLoginBtn(self):
        '''
        usage: 点击登陆按钮
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       DLPC.resource_id_login_button,
                                       DLPC.assert_timeout)

    def validPassword(self):
        '''
        usage : 验证密码为空
        '''
        password = API().getTextByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        DLPC.resource_id_pass_word,
                                        DLPC.assert_timeout)

        API().assertEqual(self.testcase, self.logger, password, DLPC.default_passwd)

    def inputMemberPhoneNumber(self):
        '''
        usage: 输入手机号
        '''
        API().inputStringByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      DLPC.resource_id_user_name,
                                      DLPC.member_phone,
                                      DLPC.assert_timeout)

    def inputMemberDefaultPassword(self):
        '''
        usage: 输入默认密码
        '''
        API().inputStringByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      DLPC.resource_id_pass_word,
                                      DLPC.member_password,
                                      DLPC.assert_timeout)