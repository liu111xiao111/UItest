# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.le_pay_page_configs import LePayPageConfigs


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
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = LePayPageConfigs.xpath_le_pay)


if __name__ == '__main__':
    pass;
