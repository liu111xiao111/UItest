# -*- coding:utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.my_fei_fan_page_configs import MyFeiFanPageConfigs as MFPC
from pages.logger import logger


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
        logger.info("Check 我的页面 begin")
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        MFPC.resource_id_my_fei_fan_title,
                                        MFPC.assert_view_timeout)
        logger.info("Check 我的页面 end")

    def validLoginStatus(self):
        '''
        usage: 验证登陆状态
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        MFPC.resource_id_nickname_button,
                                        MFPC.assert_view_timeout)

    def validLoginStatusForStability(self):
        '''
        usage: 验证登陆状态
        '''
        return API().validElementByResourceId(self.driver,
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
        logger.info("Click 设置 begin")
        API().scrollToText(self.testcase,
                           self.driver,
                           self.logger,
                           MFPC.text_settings)
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MFPC.text_settings,
                                 MFPC.click_on_button_timeout)
        logger.info("Click 设置 end")

    def clickOnMessageCentre(self):
        '''
        usage: 点击消息中心
        '''
        logger.info("Click 消息中心 begin")
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       MFPC.resource_id_message_centre_button,
                                       MFPC.click_on_button_timeout)
        logger.info("Click 消息中心 end")

    def clickOnMembershipCardPackage(self):
        '''
        usage: 点击会员卡包
        '''
        logger.info("Click 会员卡包 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MFPC.text_membership_card_package_button,
                                 MFPC.click_on_button_timeout)
        logger.info("Click 会员卡包 end")

    def clickOnNickname(self):
        '''
        usage: 点击昵称
        '''
        logger.info("Click 昵称 begin")
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       MFPC.resource_id_nickname_button,
                                       MFPC.click_on_button_timeout)
        logger.info("Click 昵称 end")

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

    def clickOnDashboard(self):
        '''
        usage: 点击爱逛街
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MFPC.text_dashboard,
                                 MFPC.click_on_button_timeout)

