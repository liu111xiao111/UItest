# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.square_parking_payment_category_configs import ParkingPaymengConfigs


class ParkingPaymentPage(SuperPage):
    '''
    作者 刘涛
    首页=>停车=>停车交费
    '''
    def __init__(self, testcase, driver, logger):
        super(ParkingPaymentPage, self).__init__(testcase, driver, logger);

    def validSelf(self):
        '''
        usage : 进入停车付费，检查是否加载出来
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        ParkingPaymengConfigs.resource_id__et_input_license_plate_et,
                                        10)
