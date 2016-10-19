# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.square_find_store_category_page_configs import SquareFindStoreConfigs

SFSC = SquareFindStoreConfigs()

class SquareFindStorePage(SuperPage):
    '''
    作者 刘涛
    首页=>广场=>找店
    '''

    def __init__(self, testcase, driver, logger):
        super(SquareFindStorePage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        API().assertElementByName(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SFSC.resource_id_tv_category_tv,
                                  SFSC.verify_view_timeout)

    '''
        usage : 点击search
    '''
    def clickOnSearch(self):
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = SFSC.xpath_iv_search_iv)

    '''
        usage :点击第一个门店
    '''   
    def clickFirstItem(self):
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = SFSC.xpath_store_first_item)

if __name__ == '__main__':
    pass;