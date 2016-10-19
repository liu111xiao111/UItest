# -*- coding:utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.message_settings_page_configs import MessageSettingsPageConfigs as MSPC


class MessageSettingsPage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>消息中心=>设置
    '''
    def __init__(self, testcase, driver, logger):
        super(MessageSettingsPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证设置页面
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        MSPC.resource_id_message_settings_title,
                                        MSPC.assert_view_timeout)

    def clickOnActivityPush(self):
        '''
        usage: 点击活动推广
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       MSPC.resource_id_activity_push_compound_button,
                                       MSPC.click_on_button_timeout)
