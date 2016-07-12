# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.location_bluetooth_page_configs import LocationBluetoothPageConfigs


class LocationBluetoothPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(LocationBluetoothPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    '''
        usage : Click "好"
    '''

    def clickOnOkBtn(self):
        API().click_view_by_xpath(testcase = self.testcase, driver = self.driver, logger = self.logger,
                                  xpath = LocationBluetoothPageConfigs.xpath_ok_button)


if __name__ == '__main__':
    pass;