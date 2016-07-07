# -*- coding: utf-8 -*-

from __init__ import *

from time import sleep
import unittest
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.pages.android.ffan.square_parking_payment_category_configs import *
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.pages.android.common.super_page import *


'''
    usage : 广场模块，停车付费类目
'''


class ParkingPaymentPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(ParkingPaymentPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    '''
        usage : 进入停车付费，检查是否加载出来
    '''

    def validSelf(self):
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                                      resource_id=ParkingPaymengConfigs.resource_id__et_input_license_plate_et,
                                                      seconds=5);


if __name__ == '__main__':
    pass;