# -*- coding:utf-8 -*-
#hupi
from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.account_management_page_configs import AccountManagementPageConfigs as AMPC


class AccountManagementPage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>设置=>账号管理
    '''
    def __init__(self, testcase, driver, logger):
        super(AccountManagementPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证账号管理页面
        '''
        API().assertElementByResourceId(self.testcase, self.driver, self.logger,
                                        AMPC.resource_id_account_management_title,
                                        AMPC.assert_view_timeout)

    def clickOnUpdatePassword(self):
        '''
        usage: 点击更新密码
        '''
        API().clickElementByText(self.testcase, self.driver, self.logger,
                                 AMPC.text_update_login_password_button,
                                 AMPC.click_on_button_timeout)

    def clickOnPaymentPasswordSetting(self):
        '''
        usage: 点击支付密码管理
        '''
        API().clickElementByText(self.testcase, self.driver, self.logger, 
                                 AMPC.text_payment_code_setting, 
                                 AMPC.click_on_button_timeout)

    def clickOnSmallAmountPasswordLessPayments(self):
        '''
        usage: 点击小额免密支付
        '''
        API().clickElementByText(self.testcase, self.driver, self.logger, 
                                 AMPC.text_small_amount_password_less_payments, 
                                 AMPC.click_on_button_timeout)
