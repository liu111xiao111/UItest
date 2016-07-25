# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.splash_screen_home_page_configs import SplashScreenHomePageConfigs


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

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger,
                                              SplashScreenHomePageConfigs.resource_id_skip_st,
                                              SplashScreenHomePageConfigs.assert_view_timeout)

if __name__ == '__main__':
    pass
