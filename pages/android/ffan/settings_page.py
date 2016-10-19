# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.settings_page_configs import SettingsPageConfigs as SPC


class SettingsPage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>设置
    '''
    def __init__(self, testcase, driver, logger):
        super(SettingsPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证设置页面
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SPC.resource_id_setting_account_management_rl,
                                        SPC.assert_view_timeout)

    def clickOnQuitAccountBtn(self, confirmQuit=True):
        '''
        usage: 点击退出当前账号
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SPC.resource_id_setting_btn_logout_rl,
                                       SPC.assert_view_timeout)
        '''API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SPC.text_exit_btn,
                                 SPC.assert_view_timeout)'''
        if confirmQuit:
            API().clickElementByText(self.testcase,
                                     self.driver,
                                     self.logger,
                                     SPC.text_confirm_btn,
                                     SPC.assert_view_timeout)
        else:
            API().clickElementByText(self.testcase,
                                     self.driver,
                                     self.logger,
                                     SPC.text_cancel_btn,
                                     SPC.assert_view_timeout)

    def clickOnAccountManagement(self):
        '''
        usage: 点击账户管理
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SPC.text_account_management,
                                 SPC.assert_view_timeout)
