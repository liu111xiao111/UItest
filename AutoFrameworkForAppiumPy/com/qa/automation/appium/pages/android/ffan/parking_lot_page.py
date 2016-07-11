# -*- coding: utf-8 -*-

from com.qa.automation.appium.pages.android.ffan.parking_lot_page_configs import ParkingLotPageConfigs
from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage


class ParkingLotPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        self.a = 12;
        super(ParkingLotPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        '''
        usage : Load "停车场列表" page
        '''
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                                      resource_id=ParkingLotPageConfigs.resource_id_tv_parking_list_tv,
                                                      seconds=18);


if __name__ == '__main__':
    pass;