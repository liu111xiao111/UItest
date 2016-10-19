# -*- coding:utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.update_payments_password_page_configs import UpdatePaymentsPasswordPageConfigs as UPPPC


class UpdatePaymentsPasswordPage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>我的飞凡卡=>支付设置=>更新支付密码
    '''
    def __init__(self, testcase, driver, logger):
        super(UpdatePaymentsPasswordPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证更新支付密码页面
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        UPPPC.resource_id_update_payments_password_title,
                                        UPPPC.assert_view_timeout)
