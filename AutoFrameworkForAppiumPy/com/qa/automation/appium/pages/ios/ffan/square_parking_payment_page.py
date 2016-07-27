# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.square_parking_payment_page_configs import ParkingPaymentPageConfigs


class ParkingPaymentPage(SuperPage):
    '''
    作者 宋波
    首页=>广场=>停车缴费
    '''

    def __init__(self, testcase, driver, logger):
        super(ParkingPaymentPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        '''
        usage: verify whether the current page is correct.
        '''

        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  ParkingPaymentPageConfigs.resource_id_parking_and_payment_st,
                                  ParkingPaymentPageConfigs.assert_view_timeout)


if __name__ == '__main__':
    pass;
