# -*- coding: utf-8 -*-

from pages.ios.ffan.le_pay_way_page_configs import LePayWayPageConfigs
from api.api import API
from pages.ios.common.superPage import SuperPage

class LePayWayPage(SuperPage):
    '''
    作者 刘涛
    首页=>乐付=>输入乐付消费金额页=>选择支付方式页
    '''

    def __init__(self, testcase, driver, logger):
        super(LePayWayPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        '''
        usage : 判断"选择支付方式"页标题显示是否正确
        '''
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name=LePayWayPageConfigs.name_choose_pay_way)

    def clickOnCancelIcon(self):
        '''
        usage : 点击"X"标示
        '''
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = LePayWayPageConfigs.xpath_cancle_icon)

    def getOrderNumber(self):
        '''
        usage : 取得乐付订单号
        '''
        orderNumber = API().getTextByXpath(testCase = self.testcase,
                                           driver = self.driver,
                                           logger = self.logger,
                                           xpath = LePayWayPageConfigs.xpath_order_number)
        return orderNumber;

if __name__ == '__main__':
    pass;