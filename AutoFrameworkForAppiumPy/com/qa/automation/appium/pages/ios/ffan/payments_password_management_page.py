# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.payments_password_management_page_configs import PaymentsPasswordManagementPageConfigs


class PaymentsPasswordManagementPage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>我的飞凡卡=>支付设置=>支付密码管理
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(PaymentsPasswordManagementPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct page.
        '''

        API().assertElementByResourceId(self.testcase, self.driver, self.logger,
                                        PaymentsPasswordManagementPageConfigs.resource_id_update_payments_password_title_st,
                                        PaymentsPasswordManagementPageConfigs.assert_view_timeout)


if __name__ == '__main__':
    pass
