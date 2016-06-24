# -*- coding: utf-8 -*-

import os, sys

# sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from time import sleep
import unittest
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.pages.android.ffan.lefu_cancel_order_configs import *
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.pages.android.common.super_page import *

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class LefuCancelOrderPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(LefuCancelOrderPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    '''
        usage : Click "确认"
    '''

    def clickOnConfirmBtn(self):
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                               resource_id=LefuCancelOrderPageConfigs.resource_id_confirm_button)


if __name__ == '__main__':
    pass;
