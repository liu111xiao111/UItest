# -*- coding:utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.small_amount_password_less_payments_page_configs import \
 SmallAmountPasswordLessPaymentsPageConfigs as SPLPPC


class SmallAmountPasswordLessPaymentsPage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>我的飞凡卡=>支付设置=>小额免密支付
    '''
    def __init__(self, testcase, driver, logger):
        super(SmallAmountPasswordLessPaymentsPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证小额免密支付
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SPLPPC.resource_id_square_dynamic_title,
                                        SPLPPC.assert_view_timeout)

    def clickOnSmallAmountPasswordLessPaymentsSwitch(self):
        '''
        usage: 点击小额免密支付开关按钮
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SPLPPC.resource_id_small_amount_password_less_payment_switch,
                                       SPLPPC.click_on_button_timeout)

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
