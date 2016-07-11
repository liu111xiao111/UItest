# -*- coding: utf-8 -*-

from com.qa.automation.appium.pages.android.ffan.parking_category_page_configs import ParkingCategoryPageConfigs
from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage

#   首页点击 停车
class ParkingCategoryPage(SuperPage):

    def __init__(self,testcase,driver,logger):
        self.a = 12;
        super(ParkingCategoryPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        '''
        usage : Load "停车" page
        '''
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                                      resource_id=ParkingCategoryPageConfigs.resource_id_tv_parking_tv,
                                                      seconds=18);

    def clickOnParkingLot(self):
        '''
        usage : Click "附近停车场"， load "停车场列表" page
        '''
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                               resource_id=ParkingCategoryPageConfigs.resource_id_tv_parking_lot_tv);

    def clickOnParkingPayment(self):
        '''
        usage : Click "停车交费"， load "停车交费" page
        '''
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                                resource_id=ParkingCategoryPageConfigs.resource_id_tv_parking_payment_tv);    


if __name__ == '__main__':
    pass;