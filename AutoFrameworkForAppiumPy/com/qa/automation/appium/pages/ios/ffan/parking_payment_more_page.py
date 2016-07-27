# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.ffan.parking_payment_more_page_configs import ParkingPaymentMorePageConfigs
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage


class ParkingPaymentMorePage(SuperPage):
    '''
    作者 刘涛
    首页=>停车=>停车交费=>输入车牌号码页=>更多
    '''

    def __init__(self, testcase, driver, logger):
        super(ParkingPaymentMorePage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name=ParkingPaymentMorePageConfigs.name_parking_payment_my_license_plate)

    def clickOnUnbundLicensePlate(self):
        '''
        usage: 点击"解除绑定".
        '''
        API().clickElementByName(testCase = self.testcase,
                                 driver = self.driver,
                                 logger = self.logger,
                                 name = ParkingPaymentMorePageConfigs.name_unbound_license_plate)

if __name__ == '__main__':
    pass;
