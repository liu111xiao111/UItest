# -*- coding: utf-8 -*-

from pages.ios.ffan.my_ffan_my_order_page_configs import MyFfanMyOrderPageConfigs
from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.logger import logger

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
        logger.info("Check 我的订单 begin")
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name=MyFfanMyOrderPageConfigs.name_order_all)
        logger.info("Check 我的订单 end")
        API().screenShot(self.driver, "myOrderForm")

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

    def clickOnDaifukuan(self):
        '''
        usage : 点击待付款
        '''
        '''
        API().clickElementByName(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MyFfanMyOrderPageConfigs.name_daifukuan)
        '''
        '''
        API().clickElementByIosUiautomation(self.testcase, self.driver, self.logger,
                                            MyFfanMyOrderPageConfigs.ios_uiautomation_daifukuan_bt,
                                            MyFfanMyOrderPageConfigs.click_on_button_timeout)
        '''
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  MyFfanMyOrderPageConfigs.xpath_daifukuan,
                                  MyFfanMyOrderPageConfigs.click_on_button_timeout)
if __name__ == '__main__':
    pass;