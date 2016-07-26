# -*- coding: utf-8 -*-

from com.qa.automation.appium.pages.ios.ffan.le_pay_cancel_order_configs import LePayCancelOrderPageConfigs
from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage


class LePayCancelOrderPage(SuperPage):
    '''
    作者 刘涛
    首页=>乐付=>输入乐付消费金额页=>选择支付方式页=>取消订单提示确定页
    '''

    def __init__(self, testcase, driver, logger):
        super(LePayCancelOrderPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def clickOnConfirmBtn(self):
        '''
            usage : 点击 "确定" button
        '''
        API().clickElementByName(testCase = self.testcase,
                                 driver = self.driver,
                                 logger = self.logger,
                                 name = LePayCancelOrderPageConfigs.name_confirm_button)

if __name__ == '__main__':
    pass;