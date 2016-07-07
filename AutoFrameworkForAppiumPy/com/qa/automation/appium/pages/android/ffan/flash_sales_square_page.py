# -*- coding:utf-8 -*-

from __init__ import *

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.flash_sales_square_page_configs import FlashSalesSquarePageConfigs


class FlashSalesSquarePage(SuperPage):
    '''
    This is flash sales square page operation class.
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(FlashSalesSquarePage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct page.
        '''

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger,
                                                      FlashSalesSquarePageConfigs.resource_id_reource_flash_sales_square_title,
                                                      FlashSalesSquarePageConfigs.assert_view_timeout)

    def clickOnGoods(self):
        '''
        usage: click goods button
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                               FlashSalesSquarePageConfigs.resource_id_goods_button,
                                               FlashSalesSquarePageConfigs.click_on_button_timeout)


if __name__ == '__main__':
    pass
