# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.fei_fan_activity_page_configs import FeiFanActivityPageConfigs as FAPC

class FeiFanActivityPage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>消息中心=>飞凡活动
    '''
    def __init__(self, testcase, driver, logger):
        super(FeiFanActivityPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证飞凡活动页面
        '''
        API().assertElementByResourceId(self.testcase, self.driver, self.logger,
                                        FAPC.resource_id_fei_fan_activity_title,
                                        FAPC.assert_view_timeout)
