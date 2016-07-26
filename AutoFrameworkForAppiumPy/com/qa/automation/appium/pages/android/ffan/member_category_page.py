# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.member_category_page_configs import MemberPageConfigs as MPC


class MemberPage(SuperPage):
    '''
    作者 陈诚
    首页=>广场=>会员
    '''
    def __init__(self, testcase, driver, logger):
        super(MemberPage, self).__init__(testcase, driver, logger);

    def validSelf(self):
        '''
        usage : 检查会员类目是否加载出来
        '''
        API().assertElementByResourceId(self.testcase, self.driver, self.logger,
                                        resource_id=MPC.resource_id__tv_member_tv,
                                        seconds=5);
