# -*- coding:utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.change_payment_password_page_configs import \
ChangePaymentPasswordPageConfigs as CPPPC


class ChangePaymentPasswordPage(SuperPage):
    '''
    作者 乔佳溪
    首页=>我的飞凡=>设置=>账号管理=>支付密码管理=>修改支付密码
    '''
    def __init__(self, testcase, driver, logger):
        super(ChangePaymentPasswordPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证支付密码管理
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        CPPPC.resource_id_change_payment_password_title,
                                        CPPPC.assert_view_timeout)

    def inputOriPaymentPassword(self):
        '''
        usage: 输入原支付密码
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 '1',
                                 CPPPC.assert_view_timeout)
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 '6',
                                 CPPPC.assert_view_timeout)
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 '1',
                                 CPPPC.assert_view_timeout)
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 '0',
                                 CPPPC.assert_view_timeout)
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 '1',
                                 CPPPC.assert_view_timeout)
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 '4',
                                 CPPPC.assert_view_timeout)

    def inputNewPaymentPassword(self):
        '''
        usage: 输入新支付密码
        '''
        API().inputStringByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      CPPPC.resource_id_change_payment_password,
                                      CPPPC.string_new_payment_password,
                                      CPPPC.assert_view_timeout)

    def clickOnCompleteBtn(self):
        '''
        usage: 点击完成
        '''
        API().clickElementByText(self.testcase, self.driver, self.logger, 
                                 CPPPC.text_complete_btn, 
                                 CPPPC.click_on_button_timeout)
