# -*- coding: utf-8 -*-

from __init__ import *

from time import sleep
import unittest
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.pages.android.ffan.lefu_cancel_order_configs import *
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.pages.android.common.super_page import *


class LefuCancelOrderPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(LefuCancelOrderPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def clickOnConfirmBtn(self):
        '''
        usage : Click "确认"
        '''
        API().click_view_by_resourceID(testcase = self.testcase, driver = self.driver, logger = self.logger, resource_id = LefuCancelOrderPageConfigs.resource_id_confirm_button)
            
if __name__ == '__main__':
    pass;