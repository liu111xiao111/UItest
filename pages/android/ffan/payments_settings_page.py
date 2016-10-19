# -*- coding:utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.payments_settings_page_configs import PaymentsSettingsPageConfigs as PSPC


class PaymentsSettingsPage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>我的飞凡卡=>支付设置
    '''
    def __init__(self, testcase, driver, logger):
        super(PaymentsSettingsPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证支付设置页面
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        PSPC.resource_id_payments_settings_title,
                                        PSPC.assert_view_timeout)

    def clickOnUpdatePaymentsPassword(self):
        '''
        usage: 点击更新支付密码
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 PSPC.text_update_payments_password_button,
                                 PSPC.click_on_button_timeout)

    def clickOnSmallAmountPasswordLessPayments(self):
        '''
        usage: 点击小额免密支付
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 PSPC.text_small_amount_password_less_payments_button,
                                 PSPC.click_on_button_timeout)
