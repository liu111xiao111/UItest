# -*- coding: utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.location_bluetooth_page_configs import LocationBluetoothPageConfigs


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
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = LocationBluetoothPageConfigs.xpath_ok_button)


if __name__ == '__main__':
    pass;