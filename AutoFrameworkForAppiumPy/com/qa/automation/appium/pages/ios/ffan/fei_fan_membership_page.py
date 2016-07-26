# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.fei_fan_membership_page_configs import FeiFanMembershipPageConfigs


class FeiFanMembershipPage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>我的会员卡包=>飞凡会员
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(FeiFanMembershipPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct page.
        '''

        API().assertElementByResourceId(self.testcase, self.driver, self.logger,
                                        FeiFanMembershipPageConfigs.resource_id_fei_fan_membership_title_st,
                                        FeiFanMembershipPageConfigs.assert_view_timeout)


if __name__ == '__main__':
    pass
