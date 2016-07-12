# -*- coding: utf-8 -*-

import os

# sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.ffan.parking_payment_unbound_confirm_page_configs import ParkingPaymentUnboundConfirmPageConfigs
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage


# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


#   首页点击 停车
class ParkingPaymentUnboundConfirmPage(SuperPage):

    def __init__(self, testcase, driver, logger):
        super(ParkingPaymentUnboundConfirmPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger,
                                              ParkingPaymentUnboundConfirmPageConfigs.name_popup_title)

    def clickOnConfirm(self):
        '''
        usage: click on "确认".
        '''
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                       resource_id=ParkingPaymentUnboundConfirmPageConfigs.name_confirm);

if __name__ == '__main__':
    pass;
