# -*- coding: utf-8 -*-

import os

# sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.ffan.parking_payment_more_page_configs import ParkingPaymentMorePageConfigs
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage


# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


#    停车交费“更多”详细页
class ParkingPaymentMorePage(SuperPage):

    def __init__(self, testcase, driver, logger):
        super(ParkingPaymentMorePage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger,
                                              ParkingPaymentMorePageConfigs.name_parking_payment_my_license_plate)

    def clickOnUnbundLicensePlate(self):
        '''
        usage: 点击"解除绑定".
        '''
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                       resource_id=ParkingPaymentMorePageConfigs.name_unbound_license_plate);

if __name__ == '__main__':
    pass;
