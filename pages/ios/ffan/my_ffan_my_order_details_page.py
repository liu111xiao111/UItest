# -*- coding: utf-8 -*-

from com.qa.automation.appium.pages.ios.ffan.my_ffan_my_order_details_page_configs import MyFfanMyOrderDetailsPageConfigs
from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage


class MyFfanMyOrderDetailsPage(SuperPage):
    '''
    作者 刘涛
    首页=>我的=>我的订单=>详情页
    '''

    def __init__(self, testcase, driver, logger):
        super(MyFfanMyOrderDetailsPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelfAllOrders(self, lePayOrderNumber, myOrderNumber):
        '''
        usage : 判断"全部订单"显示是否正确
        '''
        API().assertEqual(testCase=self.testcase,
                          logger=self.logger,
                          actualText=lePayOrderNumber,
                          expectText=myOrderNumber)

    def validSelfFilmOrders(self, lePayOrderNumber, myOrderNumber):
        '''
        usage : 判断"电影娱乐"显示是否正确
        '''
        API().assertNotEqual(testCase=self.testcase,
                          logger=self.logger,
                          actualText=lePayOrderNumber,
                          expectText=myOrderNumber)

    def validSelfLePayOrders(self, lePayOrderNumber, myOrderNumber):
        '''
        usage : 判断"乐付买单"显示是否正确
        '''
        API().assertEqual(testCase=self.testcase,
                          logger=self.logger,
                          actualText=lePayOrderNumber,
                          expectText=myOrderNumber)

    def validSelfParkingPaymentOrders(self, lePayOrderNumber, myOrderNumber):
        '''
        usage : 判断"停车缴费"显示是否正确
        '''
        API().assertNotEqual(testCase=self.testcase,
                          logger=self.logger,
                          actualText=lePayOrderNumber,
                          expectText=myOrderNumber)

    def getMyOrderNumber(self):
        '''
        usage : 点击我的全部订单中的第一条订单，进入详情页，取得订单号
        '''
        orderNumber = API().getTextByXpath(self.testcase,
                                           self.driver,
                                           self.logger,
                                           MyFfanMyOrderDetailsPageConfigs.xpath_order_number)
        return MyFfanMyOrderDetailsPageConfigs.name_order_number + orderNumber;

    def getMyFilmOrderNumber(self):
        '''
        usage : 点击我的电影娱乐订单中的第一条订单，进入详情页，取得订单号
        '''
        orderNumber = API().getTextByXpath(self.testcase,
                                           self.driver,
                                           self.logger,
                                           MyFfanMyOrderDetailsPageConfigs.xpath_film_order_number)
        return orderNumber;


    def getMyLePayOrderNumber(self):
        '''
        usage : 点击我的乐付买单订单中的第一条订单，进入详情页，取得订单号
        '''
        orderNumber = API().getTextByXpath(self.testcase,
                                           self.driver,
                                           self.logger,
                                           MyFfanMyOrderDetailsPageConfigs.xpath_le_pay_order_number)
        return MyFfanMyOrderDetailsPageConfigs.name_order_number + orderNumber;

    def getMyCouponNumber(self):
        '''
        usage : 进入详情页，取得优惠券号
        '''
        couponNumber = API().getTextByXpath(self.testcase,
                                           self.driver,
                                           self.logger,
                                           MyFfanMyOrderDetailsPageConfigs.xpath_coupon_number)
        return couponNumber;

    def getMyParkingPaymentOrderNumber(self):
        '''
        usage : 点击我的停车缴费订单中的第一条订单，进入详情页，取得订单号
        '''
        orderNumber = API().getTextByXpath(self.testcase,
                                           self.driver,
                                           self.logger,
                                           MyFfanMyOrderDetailsPageConfigs.xpath_payment_order_number)
        return orderNumber;

if __name__ == '__main__':
    pass;
