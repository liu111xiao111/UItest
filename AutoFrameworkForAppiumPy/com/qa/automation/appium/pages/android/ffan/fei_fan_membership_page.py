# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.fei_fan_membership_page_configs import FeiFanMembershipPageConfigs as FMPC


class FeiFanMembershipPage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>我的会员卡包=>飞凡会员
    '''
    def __init__(self, testcase, driver, logger):
        super(FeiFanMembershipPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证飞凡会员页面
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        FMPC.fei_fan_membership_title,
                                        FMPC.assert_view_timeout)
