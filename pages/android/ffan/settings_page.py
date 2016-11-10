# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.settings_page_configs import SettingsPageConfigs as SPC
from pages.logger import logger


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
        logger.info("Check 设置页面 begin")
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SPC.resource_id_setting_account_management_rl,
                                        SPC.assert_view_timeout)
        logger.info("Check 设置页面 end")

    def clickOnQuitAccountBtn(self, confirmQuit=True):
        '''
        usage: 点击退出当前账号
        '''
        logger.info("Click 退出当前账号 begin")
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
        logger.info("Click 退出当前账号 end")

    def clickOnAccountManagement(self):
        '''
        usage: 点击账户管理
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SPC.text_account_management,
                                 SPC.assert_view_timeout)

    def clickOnPaymentManagement(self):
        '''
        usage: 点击支付设置
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SPC.text_payment_management,
                                 SPC.assert_view_timeout)
