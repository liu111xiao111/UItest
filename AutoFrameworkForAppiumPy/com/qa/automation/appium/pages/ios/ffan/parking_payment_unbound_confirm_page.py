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


class ParkingPaymentUnboundConfirmPage(SuperPage):
    '''
    作者 刘涛
    首页=>停车=>停车交费=>输入车牌号码页=>更多=>解绑车牌确认提示页
    '''

    def __init__(self, testcase, driver, logger):
        super(ParkingPaymentUnboundConfirmPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger,
                                              ParkingPaymentUnboundConfirmPageConfigs.name_popup_title)

    def clickOnConfirm(self):
        '''
        usage: 点击"确认".
        '''
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                       resource_id=ParkingPaymentUnboundConfirmPageConfigs.name_confirm);

if __name__ == '__main__':
    pass;
