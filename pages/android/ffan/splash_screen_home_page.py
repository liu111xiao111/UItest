# -*- coding:utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.splash_screen_home_page_configs import SplashScreenHomePageConfigs as SSHPC


class SplashScreenHomePage(SuperPage):
    '''
    作者 宋波
    闪屏首页
    '''

    def __init__(self, testcase, driver, logger):
        super(SplashScreenHomePage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证闪屏首页
        '''

        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SSHPC.resource_id_skip_button,
                                        SSHPC.assert_view_timeout)
