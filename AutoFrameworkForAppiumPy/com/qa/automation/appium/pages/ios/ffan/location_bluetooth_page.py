# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.location_bluetooth_page_configs import LocationBluetoothPageConfigs


class LocationBluetoothPage(SuperPage):
    '''
    作者 刘涛
    首页=>广场=>室内地图=>是否开启蓝牙设置提示
    '''

    def __init__(self, testcase, driver, logger):
        super(LocationBluetoothPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def clickOnOkBtn(self):
        '''
            usage : 点击 "好" button
        '''
        API().click_view_by_xpath(testcase = self.testcase, driver = self.driver, logger = self.logger,
                                  xpath = LocationBluetoothPageConfigs.xpath_ok_button)


if __name__ == '__main__':
    pass;