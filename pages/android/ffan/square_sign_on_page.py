# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.square_sign_on_page_configs import SignOnPageConfigs as SOPC


class SignOnPage(SuperPage):
    '''
    作者 陈诚
    首页=>广场=>签到
    '''
    def __init__(self, testcase, driver, logger):
        super(SignOnPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 进入广场模块，检查是否加载出来
        '''
        API().assertElementByText(self.testcase, self.driver, self.logger,
                                  SOPC.text_title_ttj,
                                  SOPC.assert_view_timeout)

    def validChickedInStatus(self, assertable=True):
        '''
        usage: 验证选中状态
        '''
        if assertable:
            API().assertElementByContentDesc(self.testcase, self.driver, self.logger,
                                      SOPC.content_desc_sign_in_button,
                                      SOPC.assert_view_timeout)
            return True
        else:
            if API().validElementByContentDesc(self.driver, self.logger,
                                        SOPC.content_desc_sign_in_button,
                                        SOPC.assert_view_timeout):
                return True
            return False

    def clickOnSignIn(self):
        '''
        usage: 点击签到
        '''
        API().clickElementByContentDesc(self.testcase, self.driver, self.logger,
                                        SOPC.content_desc_sign_on,
                                        SOPC.assert_view_timeout)
