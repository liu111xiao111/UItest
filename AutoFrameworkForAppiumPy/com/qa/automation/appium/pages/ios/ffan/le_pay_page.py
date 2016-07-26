# -*- coding: utf-8 -*-

from com.qa.automation.appium.pages.ios.ffan.le_pay_page_configs import LePayPageConfigs
from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage


class LePayPage(SuperPage):
    '''
    作者 刘涛
    首页=>乐付
    '''

    def __init__(self, testcase, driver, logger):
        super(LePayPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        navigation = API().validElementByIosUiautomation(driver=self.driver,
                                                         logger=self.logger,uiaString=".navigationBars()[0]")
        API().assertEqual(testCase=self.testcase,
                          logger=self.logger,
                          actualText=navigation.get_attribute("name"),
                          expectText=LePayPageConfigs.name_le_pay_navigation_bar)

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
