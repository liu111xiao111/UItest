# -*- coding:utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.personal_information_page_configs import PersonalInformationPageConfigs as PIPC


class PersonalInformationPage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>个人信息
    '''
    def __init__(self, testcase, driver, logger):
        super(PersonalInformationPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证个人信息
        '''
        API().assertElementByText(self.testcase, self.driver, self.logger,
                                  PIPC.text_nickname_button,
                                  PIPC.assert_view_timeout)
