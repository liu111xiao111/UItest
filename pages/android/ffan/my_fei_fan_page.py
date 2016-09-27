# -*- coding:utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.my_fei_fan_page_configs import MyFeiFanPageConfigs as MFPC


class MyFeiFanPage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡
    '''
    def __init__(self, testcase, driver, logger):
        super(MyFeiFanPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证我的飞凡
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        MFPC.resource_id_my_fei_fan_title,
                                        MFPC.assert_view_timeout)

    def validLoginStatus(self):
        '''
        usage: 验证登陆状态
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        MFPC.resource_id_nickname_button,
                                        MFPC.assert_view_timeout)

    def validLogoutStatus(self):
        '''
        usage: 验证退出登陆状态
        '''
        API().scrollToText(self.testcase,
                           self.driver,
                           self.logger,
                           MFPC.text_login)
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        MFPC.resource_id_login_button,
                                        MFPC.assert_view_timeout)

    def clickOnLogin(self):
        '''
        usage: 点击登陆
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       MFPC.resource_id_login_button,
                                       MFPC.click_on_button_timeout)

    def clickOnSettings(self):
        '''
        usage: 点击设置
        '''
        API().scrollToText(self.testcase,
                           self.driver,
                           self.logger,
                           MFPC.text_settings)
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MFPC.text_settings,
                                 MFPC.click_on_button_timeout)

    def clickOnMessageCentre(self):
        '''
        usage: 点击消息中心
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       MFPC.resource_id_message_centre_button,
                                       MFPC.click_on_button_timeout)

    def clickOnMembershipCardPackage(self):
        '''
        usage: 点击会员卡包
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MFPC.text_membership_card_package_button,
                                 MFPC.click_on_button_timeout)

    def clickOnNickname(self):
        '''
        usage: 点击昵称
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       MFPC.resource_id_nickname_button,
                                       MFPC.click_on_button_timeout)

    def clickOnMyFeiFanCard(self):
        '''
        usage: 点击我的飞凡卡
        '''
        API().scrollToText(self.testcase,
                           self.driver,
                           self.logger,
                           MFPC.text_my_fei_fan_card)
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MFPC.text_my_fei_fan_card,
                                 MFPC.click_on_button_timeout)
