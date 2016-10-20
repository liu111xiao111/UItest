# -*- coding: utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.verification_page_configs import VerificationPageConfigs


class VerificationPage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>登录=>验证
    '''

    def __init__(self, testcase, driver, logger):
        super(VerificationPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  VerificationPageConfigs.name_title_st,
                                  VerificationPageConfigs.assert_view_timeout)

    def clickOnSkip(self):
        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 VerificationPageConfigs.name_skip_bt,
                                 VerificationPageConfigs.click_on_button_timeout)


if __name__ == '__main__':
    pass;
