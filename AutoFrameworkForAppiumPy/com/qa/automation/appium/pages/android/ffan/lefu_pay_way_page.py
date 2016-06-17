# -*- coding: utf-8 -*-

import os,sys

#sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from time import sleep
import unittest
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.pages.android.ffan.lefu_pay_way_page_configs import *
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.pages.android.common.super_page import *

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)



class LefuPayWayPage(SuperPage):

    def __init__(self,testcase,driver,logger):
        super(LefuPayWayPage, self).__init__(testcase = testcase , driver = driver,logger = logger);
                                           
    def validSelf(self):
        '''
        usage : Click "确认买单" in lefu pay page, and load "选择支付方式" page correctly.
        '''
        API().assert_view_by_resourceID_Until_android(testcase = self.testcase , driver = self.driver,logger = self.logger ,
                                                resource_id = LefuPayWayPageConfigs.resource_id_pay_way,seconds=18);
        '''API().assert_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                          text=LefuPayWayPageConfigs.text_pay_way,
                                          seconds=10);'''


if __name__ == '__main__':
    pass;