# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.square_dynamic_page_configs import SquareDynamicPageConfigs


class SquareDynamicPage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>消息中心=>飞凡活动
    '''
    def __init__(self, testcase, driver, logger):
        super(SquareDynamicPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证飞凡活动页面
        '''
        API().assertElementByResourceId(self.testcase, self.driver, self.logger,
                                        SquareDynamicPageConfigs.resource_id_square_dynamic_title,
                                        SquareDynamicPageConfigs.assert_view_timeout)
