# -*- coding:utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.payments_settings_page_configs import PaymentsSettingsPageConfigs


class PaymentsSettingsPage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>我的飞凡卡=>支付设置
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(PaymentsSettingsPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct page.
        '''

        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  PaymentsSettingsPageConfigs.name_payments_settings_title_st,
                                  PaymentsSettingsPageConfigs.assert_view_timeout)

    def clickOnPaymentsPasswordManagement(self):
        '''
        usage: click on the payments password management button.
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 PaymentsSettingsPageConfigs.name_update_payments_password_st,
                                 PaymentsSettingsPageConfigs.click_on_button_timeout)

    def clickOnSmallAmountPasswordLessPayments(self):
        '''
        usage: click on the small amount password less payment button.
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 PaymentsSettingsPageConfigs.name_small_amount_password_less_payments_st,
                                 PaymentsSettingsPageConfigs.click_on_button_timeout)


if __name__ == '__main__':
    pass
