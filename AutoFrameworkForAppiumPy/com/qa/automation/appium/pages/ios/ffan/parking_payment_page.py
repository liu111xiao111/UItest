# -*- coding: utf-8 -*-

import os
import sys

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.parking_payment_page_configs import ParkingPaymentPageConfigs


sys.path.append(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))))


class ParkingPaymentPage(SuperPage):
    '''
    作者 刘涛
    首页=>停车=>停车交费
    '''

    def __init__(self,testcase,driver,logger):
        super(ParkingPaymentPage, self).__init__(testcase = testcase , driver = driver,logger = logger);


    def validSelf(self):
        '''
        usage : 判断“付停车费”是否正确显示
        '''
        API().assert_view_by_resourceID_Until(testcase = self.testcase, driver = self.driver, logger = self.logger,
                                              resource_id=ParkingPaymentPageConfigs.name_parking_payment)

    def clickOnMore(self):
        '''
        usage: 点击右上角“更多”的图标
        '''
        API().click_view_by_xpath(testcase = self.testcase, driver = self.driver, logger = self.logger,
                                  xpath = ParkingPaymentPageConfigs.xpath_more)

if __name__ == '__main__':
    pass;