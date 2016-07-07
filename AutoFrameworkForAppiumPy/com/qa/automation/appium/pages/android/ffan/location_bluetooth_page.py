# -*- coding: utf-8 -*-

from __init__ import *

from time import sleep
import unittest
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.pages.android.ffan.location_bluetooth_page_configs import *
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.pages.android.common.super_page import *


class LocationBluetoothPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(LocationBluetoothPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    '''
        usage : Click "取消"
    '''

    def clickOnCancleBtn(self):
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                               resource_id=LocationBluetoothPageConfigs.resource_id_cancle_button)


if __name__ == '__main__':
    pass;