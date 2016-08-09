# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.login_verify_page_configs import LoginVerifyPageConfigs as LVPC


class LoginVerifyPage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>登录=>验证
    '''
    def __init__(self, testcase, driver, logger):
        super(LoginVerifyPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 验证页,检查验证标题
        '''
        API().assertElementByText(self.testcase,
                                        self.driver,
                                        self.logger,
                                        LVPC.text_verify,
                                        10)

    def clickOnSkip(self):
        '''
        usage: 点击跳过
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       LVPC.resource_id_skip,
                                       10)
