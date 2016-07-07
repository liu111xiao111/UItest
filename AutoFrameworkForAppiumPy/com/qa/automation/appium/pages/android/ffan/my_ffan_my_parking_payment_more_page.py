# -*- coding: utf-8 -*-

from __init__ import *

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.my_ffan_my_parking_payment_more_page_configs import MyFfanMyParkingPaymentMorePageConfigs


class MyFfanMyParkingPaymentMorePage(SuperPage):

    def __init__(self,testcase,driver,logger):
        super(MyFfanMyParkingPaymentMorePage, self).__init__(testcase=testcase , driver=driver, logger=logger);


    def validSelf(self):
        '''
        usage : Load "停车交费" details page correctly. 
        ''' 
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                              resource_id=MyFfanMyParkingPaymentMorePageConfigs.text_unbunding)

    def clickOnUnbundingBtn(self):
        '''
            usage: 点击"更多"
        ''' 
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text = MyFfanMyParkingPaymentMorePageConfigs.text_unbunding);

if __name__ == '__main__':
    pass;