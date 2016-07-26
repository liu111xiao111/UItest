# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.square_dynamic_page_configs import SquareDynamicPageConfigs


class SquareDynamicPage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>消息中心=>飞凡活动
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(SquareDynamicPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct.
        '''

        API().assertElementByResourceId(self.testcase, self.driver, self.logger,
                                        SquareDynamicPageConfigs.resource_id_square_dynamic_title_st,
                                        SquareDynamicPageConfigs.assert_view_timeout)


if __name__ == '__main__':
    pass
