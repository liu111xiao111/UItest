# -*- coding: utf-8 -*-

import os,sys

#sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from time import sleep
import unittest
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.pages.android.ffan.feifan_card_integral_page_configs import *
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.pages.android.common.super_page import *

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)



class FeiFanCardIntegralPage(SuperPage):

    def __init__(self,testcase,driver,logger):
        super(FeiFanCardIntegralPage, self).__init__(testcase = testcase , driver = driver, logger = logger);

    def validSelf(self):
        '''
        usage : Check "积分主页" whether loading correctly.
        '''
        API().assert_view_by_resourceID_Until_android(testcase = self.testcase, driver = self.driver, logger = self.logger, resource_id = FeiFanCardIntegralPageConfigs.resource_id_tv_integral_tv, seconds = 10)
        #API().assert_view_by_resourceID_Until_android(testcase = self.testcase, driver = self.driver, logger = self.logger, resource_id = FeiFanCardIntegralPageConfigs.resource_id_tv_myIntegral_tv, seconds = 10)
     
if __name__ == '__main__':
    pass;