# -*- coding:utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.my_membership_card_package_page_configs import \
    MyMembershipCardPackagePageConfigs as MCPPC


class MyMembershipCardPackagePage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>我的会员卡包
    '''
    def __init__(self, testcase, driver, logger):
        super(MyMembershipCardPackagePage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证我的会员卡包页面
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        MCPPC.resource_id_my_membership_card_package_title,
                                        MCPPC.assert_view_timeout)

    def clickOnLeHuoKa(self):
        '''
        usage: 点击乐活卡
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       MCPPC.resource_id_le_huo_ka_button,
                                       MCPPC.click_on_button_timeout)
