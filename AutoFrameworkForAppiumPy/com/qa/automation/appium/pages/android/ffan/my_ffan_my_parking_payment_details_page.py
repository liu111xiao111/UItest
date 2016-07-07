# -*- coding: utf-8 -*-

from __init__ import *

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.my_ffan_my_parking_payment_details_page_configs import MyFfanMyParkingPaymentDetailsPageConfigs

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class MyFfanMyParkingPaymentDetailsPage(SuperPage):

    def __init__(self,testcase,driver,logger):
        super(MyFfanMyParkingPaymentDetailsPage, self).__init__(testcase = testcase , driver = driver,logger = logger);


    def validSelf(self):
        '''
        usage : Load "停车交费" details page correctly. 
        ''' 
        API().assert_view_by_resourceID_Until(testcase = self.testcase, driver = self.driver, logger = self.logger,
                                              resource_id=MyFfanMyParkingPaymentDetailsPageConfigs.resource_id_tv_parking_VIN_tv)                             

    def clickOnMore(self):
        '''
            usage: 点击"更多"
        '''
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=MyFfanMyParkingPaymentDetailsPageConfigs.text_more)

if __name__ == '__main__':
    pass;