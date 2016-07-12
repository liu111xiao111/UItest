# -*- coding: utf-8 -*-

'''
    usage : 广场模块，停车付费类目
'''
from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.square_parking_payment_page_configs import ParkingPaymentPageConfigs


class ParkingPaymentPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(ParkingPaymentPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    '''
        usage : 进入停车付费，检查是否加载出来
    '''

    def validSelf(self):
        '''
        usage: verify whether the current page is correct.
        '''

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger,
                                              ParkingPaymentPageConfigs.resource_id_parking_and_payment_st,
                                              ParkingPaymentPageConfigs.assert_view_timeout)

if __name__ == '__main__':
    pass;
