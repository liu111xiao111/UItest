# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.brand_activity_page_configs import BrandActivityPageConfigs as BAPC


class BrandActivityPage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>消息中心=>品牌活动
    '''
    def __init__(self, testcase, driver, logger):
        super(BrandActivityPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证品牌活动页面.
        '''
        API().assertElementByResourceId(self.testcase, self.driver, self.logger,
                                        BAPC.resource_id_square_dynamic_title,
                                        BAPC.assert_view_timeout)
