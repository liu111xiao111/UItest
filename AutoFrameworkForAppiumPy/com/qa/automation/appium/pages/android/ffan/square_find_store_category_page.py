# -*- coding: utf-8 -*-

import os, sys

# sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from time import sleep
import unittest
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.pages.android.ffan.square_find_store_category_page_configs import *
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.pages.android.common.super_page import *

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

'''
    usage : 广场模块，找店类目
'''


class SquareFindStorePage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(SquareFindStorePage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                                      resource_id=SquareFindStoreConfigs.resource_id_tv_category_tv,
                                                      seconds=10);

    '''
        usage : 点击search
    '''

    def clickOnSearch(self):
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                               resource_id=SquareFindStoreConfigs.resource_id_iv_search_iv)


if __name__ == '__main__':
    pass;