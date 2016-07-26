# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.lefu_cancel_order_configs import LefuCancelOrderPageConfigs as LCOPC


class LefuCancelOrderPage(SuperPage):
    '''
    作者 刘涛
    首页=>乐付=>输入乐付消费金额页=>选择支付方式页=>取消订单提示确定页
    '''
    def __init__(self, testcase, driver, logger):
        super(LefuCancelOrderPage, self).__init__(testcase, driver, logger);

    def clickOnConfirmBtn(self):
        '''
        usage : 点击 "确认"
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       LCOPC.resource_id_confirm_button,
                                       10)
