# -*- coding: utf-8 -*-

import os,sys

#sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from time import sleep
import unittest
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.pages.android.ffan.store_info_page_configs import *
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.pages.android.common.super_page import *

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


'''
    usage: 门店详情
'''

class StoreInfoPage(SuperPage):

    def __init__(self,testcase,driver,logger):
        super(StoreInfoPage, self).__init__(testcase = testcase , driver = driver, logger = logger);

    '''
        usage : 检查是否加载出来
    '''
    def validSelf(self):
        #API().assert_view_by_xpath_android(testcase = self.testcase, driver = self.driver, logger = self.logger, xpath=StoreInfoPageConfigs.xpath_store_info)
        API().assert_view_by_text_android(testcase = self.testcase, driver = self.driver, logger = self.logger, text = StoreInfoPageConfigs.text_store_detail)                                   
            
if __name__ == '__main__':
    pass;