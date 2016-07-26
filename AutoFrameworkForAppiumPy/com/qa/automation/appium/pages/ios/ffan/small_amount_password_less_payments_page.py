# -*- coding:utf-8 -*-

from selenium.common.exceptions import TimeoutException

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.small_amount_password_less_payments_page_configs import SmallAmountPasswordLessPaymentsPageConfigs


class SmallAmountPasswordLessPaymentsPage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>我的飞凡卡=>支付设置=>小额免密支付
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(SmallAmountPasswordLessPaymentsPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct.
        '''

        API().assertElementByResourceId(self.testcase, self.driver, self.logger,
                                        SmallAmountPasswordLessPaymentsPageConfigs.resource_id_small_amount_password_less_payments_title_st,
                                        SmallAmountPasswordLessPaymentsPageConfigs.assert_view_timeout)

    def clickOnSmallAmountPasswordLessPaymentsSwitch(self):
        '''
        usage: click on the small amount password-less payment switch button.
        '''

        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  SmallAmountPasswordLessPaymentsPageConfigs.xpath_small_amount_password_less_payments_sc,
                                  SmallAmountPasswordLessPaymentsPageConfigs.click_on_button_timeout)

    def validSmallAmountPasswordLessPaymentsStatus(self):
        '''
        usage: verify whether the small amount password-lsee payment is opened.
        '''

        return API().validElementByResourceId(self.driver, self.logger,
                                              SmallAmountPasswordLessPaymentsPageConfigs.resource_id_choose_small_amount_password_less_quota_st,
                                              SmallAmountPasswordLessPaymentsPageConfigs.find_view_timeout)


if __name__ == '__main__':
    pass
