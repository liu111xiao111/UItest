# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.my_ffan_my_order_page_configs import MyFfanMyOrderPageConfigs as MOPC


class MyFfanMyOrderPage(SuperPage):
    '''
    作者 刘涛
    首页=>我的=>我的订单
    '''
    def __init__(self, testcase, driver, logger):
        super(MyFfanMyOrderPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 验证我的订单
        '''
        API().assertElementByResourceId(self.testcase, self.driver, self.logger,
                                        MOPC.resource_id_tv_my_order_tv,
                                        10)

    def clickOnOrderAll(self):
        '''
        usage : 点击全部
        '''
        API().clickElementByText(self.testcase, self.driver, self.logger,
                                 MOPC.text_order_all,
                                 10)

    def clickOnOrderNoPay(self):
        '''
        usage : 点击待付款
        '''
        API().clickElementByText(self.testcase, self.driver, self.logger,
                                 MOPC.text_order_no_pay,
                                 10)

    def clickOnOrderPaid(self):
        '''
        usage : 点击已付款
        '''
        API().clickElementByText(self.testcase, self.driver, self.logger,
                                 MOPC.text_order_paid,
                                 10)

    def validSelfNoPay(self):
        '''
        usage : 验证待付款
        '''
        API().assertElementByText(self.testcase, self.driver, self.logger,
                                  MOPC.text_order_no_pay,
                                  10)

    def validSelfPaid(self):
        '''
        usage : 验证已付款
        '''

        API().assertElementByText(self.testcase, self.driver, self.logger,
                                  MOPC.text_order_paid,
                                  10)

    def getOrderNumber(self):
        '''
        usage : 获取数值
        '''
        orderNumber = API().getTextByResourceId(self.testcase, self.driver, self.logger, 
                                                MOPC.resource_id_tv_order_number_tv,
                                                10)
        return orderNumber
