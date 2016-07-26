# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.square_lefu_pay_page_configs import SquareLefuPayPageConfigs as SLPPC


class SquareLefuPayPage(SuperPage):
    '''
    作者 刘涛
    首页=>乐付
    '''
    def __init__(self, testcase, driver, logger):
        super(SquareLefuPayPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 验证乐付买单
        '''
        API().assertElementByResourceId(self.testcase, self.driver, self.logger,
                                        SLPPC.resource_id_lefu_pay_title,
                                        18)

    def clickOnLefuPay(self):
        '''
        usage : 点击 "乐付买单"
        '''
        API().clickElementByResourceId(self.testcase, self.driver, self.logger,
                                       SLPPC.resource_id_lefu_pay,
                                       18)
