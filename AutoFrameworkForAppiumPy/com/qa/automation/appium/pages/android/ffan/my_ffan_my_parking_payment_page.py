# -*- coding: utf-8 -*-

import os

#sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.my_ffan_my_parking_payment_page_configs import MyFfanMyParkingPaymentPageConfigs

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class MyFfanMyParkingPaymentPage(SuperPage):

    def __init__(self,testcase,driver,logger):
        super(MyFfanMyParkingPaymentPage, self).__init__(testcase = testcase , driver = driver,logger = logger);


    def validSelf(self):
        '''
        usage : Click "停车交费" in my Feifan page， and load "停车交费" page correctly. 
        ''' 
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                              resource_id=MyFfanMyParkingPaymentPageConfigs.resource_id_tv_parking_payment_tv
                                              );

    def inputVIN(self):
        '''
        usage : Input VIN 
        ''' 
        API().input_view_by_resourceID_android(driver=self.driver, logger=self.logger,
                                               resource_id = MyFfanMyParkingPaymentPageConfigs.resource_id_tv_VIN_tv, string = MyFfanMyParkingPaymentPageConfigs.input_VIN
                                               );

    def clickOnNextBtn(self):
        '''
            usage: 点击"下一步" button
        ''' 
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text = MyFfanMyParkingPaymentPageConfigs.text_next_btn);


if __name__ == '__main__':
    pass;