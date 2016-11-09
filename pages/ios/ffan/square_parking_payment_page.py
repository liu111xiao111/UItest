# -*- coding: utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.square_parking_payment_page_configs import ParkingPaymentPageConfigs
from pages.logger import logger

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
        logger.info("Check 广场停车 begin")
        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  ParkingPaymentPageConfigs.resource_id_parking_and_payment_st,
                                  ParkingPaymentPageConfigs.assert_view_timeout)
        logger.info("Check 广场停车 end")
        API().screenShot(self.driver, "guangChangTingChe")

if __name__ == '__main__':
    pass;
