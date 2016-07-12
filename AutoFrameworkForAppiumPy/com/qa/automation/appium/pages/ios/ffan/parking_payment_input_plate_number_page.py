# -*- coding: utf-8 -*-

import os
import sys

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.parking_payment_input_plate_number_page_configs import ParkingPaymentInputPlateNumberPageConfigs


sys.path.append(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))))


class ParkingPaymentInputPlateNumberPage(SuperPage):

    def __init__(self,testcase,driver,logger):
        super(ParkingPaymentInputPlateNumberPage, self).__init__(testcase = testcase , driver = driver,logger = logger);


    def validSelf(self):
        '''
        usage : 判断"停车交费"标题显示是否正确 
        '''
        API().assert_view_by_resourceID_Until(testcase = self.testcase, driver = self.driver, logger = self.logger,
                                              resource_id=ParkingPaymentInputPlateNumberPageConfigs.name_parking_payment_title)

    def inputPlateNumber(self):
        '''
        usage : 输入要绑定的车牌号
        '''
        API().input_view_by_xpath_ios(self.driver, self.logger, ParkingPaymentInputPlateNumberPageConfigs.xpath_plate_number,
                                      ParkingPaymentInputPlateNumberPageConfigs.plate_number)
        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                               ParkingPaymentInputPlateNumberPageConfigs.name_return)

    def clickOnNextStep(self):
        '''
        usage: 点击下一步
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                               ParkingPaymentInputPlateNumberPageConfigs.name_next_step)

if __name__ == '__main__':
    pass;