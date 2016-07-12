# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.ffan.parking_page_configs import ParkingPageConfigs
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage


#   首页点击 停车
class ParkingPage(SuperPage):

    def __init__(self, testcase, driver, logger):
        super(ParkingPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        navigation = API().find_view_by_uia_string_until_ios(driver=self.driver,logger=self.logger,uia_string=".navigationBars()[0]")
        API().assert_equal(test_case=self.testcase,driver=self.driver,logger=self.logger,
                           actual_text=navigation.get_attribute("name"),expect_text=ParkingPageConfigs.name_parking_navigation_bar)

    def clickOnParkingPayment(self):
        '''
        usage: 点击"停车交费".
        '''
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                       resource_id=ParkingPageConfigs.name_parking_payment);

if __name__ == '__main__':
    pass;
