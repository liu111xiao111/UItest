# -*- coding: utf-8 -*-

from api.api import API
from pages.ios.ffan.parking_payment_unbound_confirm_page_configs import ParkingPaymentUnboundConfirmPageConfigs
from pages.ios.common.superPage import SuperPage


class ParkingPaymentUnboundConfirmPage(SuperPage):
    '''
    作者 刘涛
    首页=>停车=>停车交费=>输入车牌号码页=>更多=>解绑车牌确认提示页
    '''

    def __init__(self, testcase, driver, logger):
        super(ParkingPaymentUnboundConfirmPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name=ParkingPaymentUnboundConfirmPageConfigs.name_popup_title)

    def clickOnConfirm(self):
        '''
        usage: 点击"确认".
        '''
        API().clickElementByName(testCase = self.testcase,
                                 driver = self.driver,
                                 logger = self.logger,
                                 name = ParkingPaymentUnboundConfirmPageConfigs.name_confirm)

if __name__ == '__main__':
    pass;
