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

    def clickOnOrderDetails(self):
        '''
        usage : 点击我的订单中的第一条订单，进入详情页
        '''
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = MOPC.xpath_order_details)

    def clickOnOrderList(self):
        '''
        usage : 点击我的订单中的第一条订单，进入详情页
        '''
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = MOPC.xpath_order_list)

    def clickOnAllOrders(self):
        '''
        usage : 点击"全部订单"
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MOPC.name_order_all)

    def clickOnFilm(self):
        '''
        usage : 点击"电影娱乐"
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MOPC.name_order_film)

    def clickOnLePay(self):
        '''
        usage : 点击"乐付买单"
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MOPC.name_order_le_pay)

    def clickOnParkingPayment(self):
        '''
        usage : 点击"停车缴费"
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MOPC.name_order_parking_payment)
