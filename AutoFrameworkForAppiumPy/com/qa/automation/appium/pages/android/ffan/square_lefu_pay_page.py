# -*- coding: utf-8 -*-

import os, sys

# sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from time import sleep
import unittest
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.pages.android.ffan.square_lefu_pay_page_configs import *
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.pages.android.common.super_page import *

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class SquareLefuPayPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(SquareLefuPayPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        '''
        usage : Click "乐付买单" in square page, and load "乐付买单" correctly.
        '''
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                                      resource_id=SquareLefuPayPageConfigs.resource_id_lefu_pay_title,
                                                      seconds=18);

    def clickOnLefuPay(self):
        '''
        usage : Click "乐付买单"
        '''
        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                               SquareLefuPayPageConfigs.resource_id_lefu_pay, seconds=18);
        # API().click_view_by_resourceID_android(testcase = self.testcase, driver = self.driver,logger = self.logger, resource_id = SquareLefuPayPageConfigs.resource_id_lefu_pay)


if __name__ == '__main__':
    pass;
