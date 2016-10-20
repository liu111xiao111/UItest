# -*- coding: utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.le_pay_page_configs import LePayPageConfigs


class LePayPage(SuperPage):
    '''
    作者 刘涛
    首页=>乐付
    '''

    def __init__(self, testcase, driver, logger):
        super(LePayPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        API().assertElementByName(self.testcase,
                                  self.driver,
                                  self.logger,
                                  LePayPageConfigs.name_le_pay_navigation_bar)

    def clickOnDetailsLePay(self):
        '''
        usage: 点击"乐付买单"
        '''
        API().clickElementByXpath(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  xpath=LePayPageConfigs.xpath_le_pay)

    def inputSumOfConsumption(self):
        '''
        usage : 输入消费金额
        '''
        API().inputStringByXpath(self.testcase,
                                 self.driver,
                                 self.logger,
                                 LePayPageConfigs.xpath_sum_of_consumption,
                                 LePayPageConfigs.sum_of_consumption)


    def clickOnConfirmPurchase(self):
        '''
        usage: 点击"确认购买"
        '''
        API().clickElementByXpath(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  xpath=LePayPageConfigs.xpath_confirm_purchase)

    def clickOnConfirmCancel(self):
        '''
        usage: 点击"确认"
        '''
        API().clickElementByXpath(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  xpath=LePayPageConfigs.xpath_confirm_cancel)

if __name__ == '__main__':
    pass;
