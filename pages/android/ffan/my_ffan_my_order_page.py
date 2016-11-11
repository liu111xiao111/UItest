# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.my_ffan_my_order_page_configs import MyFfanMyOrderPageConfigs as MOPC
from pages.logger import logger


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
        logger.info("Check 我的订单页面 begin")
        API().assertElementByResourceId(self.testcase, self.driver, self.logger,
                                        MOPC.resource_id_tv_my_order_tv,
                                        10)
        logger.info("Check 我的订单页面 end")

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

    def clickOnAllOrdersTitle(self):
        '''
        usage : 点击"全部订单"标题
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MOPC.name_order_title)

    def clickOnAllOrders(self):
        '''
        usage : 点击"全部订单"
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MOPC.name_order_title)

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
