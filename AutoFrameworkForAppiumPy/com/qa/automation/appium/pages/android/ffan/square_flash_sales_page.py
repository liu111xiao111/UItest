# -*- coding: utf-8 -*-

from com.qa.automation.appium.pages.android.ffan.square_flash_sales_page_configs import SquareFlashSalesPageConfigs
from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage


class SquareFlashSalesPage(SuperPage):

    def __init__(self,testcase,driver,logger):
        super(SquareFlashSalesPage, self).__init__(testcase = testcase , driver = driver,logger = logger);
                                           
    def validSelf(self):
        '''
        usage : Load "限时抢购" page
        '''
        API().assert_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                          text=SquareFlashSalesPageConfigs.text_flash_sales,
                                          seconds=10);

    def clickOnBuy(self):
        '''
            usage: click “立即抢购”
        '''    
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger, text=SquareFlashSalesPageConfigs.text_buy)

if __name__ == '__main__':
    pass;