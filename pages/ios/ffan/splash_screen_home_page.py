# -*- coding:utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.splash_screen_home_page_configs import SplashScreenHomePageConfigs


class SplashScreenHomePage(SuperPage):
    '''
    作者 宋波
    闪屏首页
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(SplashScreenHomePage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct.
        '''

        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  SplashScreenHomePageConfigs.resource_id_skip_st,
                                  SplashScreenHomePageConfigs.assert_view_timeout)

if __name__ == '__main__':
    pass
