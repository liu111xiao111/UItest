# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.payment_password_setting_page_configs import \
PaymentPasswordSettingPageConfigs as PPSPC


class PaymentPasswordSettingPage(SuperPage):
    '''
    作者 乔佳溪
    首页=>我的飞凡=>设置=>账号管理=>支付密码管理
    '''
    def __init__(self, testcase, driver, logger):
        super(PaymentPasswordSettingPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证支付密码管理
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        PPSPC.resource_id_payment_password_title,
                                        PPSPC.assert_view_timeout)

    def clickOnChangePaymentPassword(self):
        '''
        usage: 点击修改支付密码
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 PPSPC.text_change_payment_passwork,
                                 PPSPC.assert_view_timeout)

    def validSmallAmountPasswordLessPaymentsStatus(self):
        '''
        usage: 验证小额免密支付是否打开
        '''
        if API().validElementByText(self.driver,
                                    self.logger,
                                    SPLPPC.text_choose_small_amount_password_less_quota,
                                    SPLPPC.click_on_button_timeout):
            return True
        return False
