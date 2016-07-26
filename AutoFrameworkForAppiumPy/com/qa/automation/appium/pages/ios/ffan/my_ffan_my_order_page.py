# -*- coding: utf-8 -*-

from com.qa.automation.appium.pages.ios.ffan.my_ffan_my_order_page_configs import MyFfanMyOrderPageConfigs
from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage


class MyFfanMyOrderPage(SuperPage):
    '''
    作者 刘涛
    首页=>我的=>我的订单
    '''

    def __init__(self, testcase, driver, logger):
        super(MyFfanMyOrderPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        '''
        usage : 判断"全部订单"标题显示是否正确
        '''
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name=MyFfanMyOrderPageConfigs.name_order_all)

    def clickOnOrderDetails(self):
        '''
        usage : 点击我的订单中的第一条订单，进入详情页
        '''
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = MyFfanMyOrderPageConfigs.xpath_order_details)

    def clickOnOrderList(self):
        '''
        usage : 点击我的订单中的第一条订单，进入详情页
        '''
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = MyFfanMyOrderPageConfigs.xpath_order_list)

    def clickOnAllOrders(self):
        '''
        usage : 点击"全部订单"
        '''
        API().clickElementByName(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MyFfanMyOrderPageConfigs.name_order_all)

    def clickOnFilm(self):
        '''
        usage : 点击"电影娱乐"
        '''
        API().clickElementByName(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MyFfanMyOrderPageConfigs.name_order_film)

    def clickOnLePay(self):
        '''
        usage : 点击"乐付买单"
        '''
        API().clickElementByName(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MyFfanMyOrderPageConfigs.name_order_le_pay)

    def clickOnParkingPayment(self):
        '''
        usage : 点击"停车缴费"
        '''
        API().clickElementByName(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MyFfanMyOrderPageConfigs.name_order_parking_payment)

if __name__ == '__main__':
    pass;