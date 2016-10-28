# -*- coding:utf-8 -*-
#hupi
from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.payment_management_page_configs import PaymentManagementPageConfigs as PMPC


class PaymentManagementPage(SuperPage):
    '''
    作者 乔佳溪
    首页=>我的飞凡=>设置=>支付设置
    '''
    def __init__(self, testcase, driver, logger):
        super(PaymentManagementPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证支付设置页面
        '''
        API().assertElementByResourceId(self.testcase, self.driver, self.logger,
                                        PMPC.resource_id_payment_management_title,
                                        PMPC.assert_view_timeout)

    def clickOnNoPasswordPyament(self):
        '''
        usage: 点击免密支付
        '''
        API().clickElementByResourceId(self.testcase, self.driver, self.logger,
                                 PMPC.resource_no_password_id,
                                 PMPC.click_on_button_timeout)

    def clickOnUpdatePassword(self):
        '''
        usage: 点击修改支付密码密码
        '''
        API().clickElementByText(self.testcase, self.driver, self.logger,
                                 PMPC.text_update_payment_password_button,
                                 PMPC.click_on_button_timeout)

