# -*- coding: utf-8 -*-

import os,sys

#sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from time import sleep
import unittest
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.pages.android.ffan.feifan_card_bill_page_configs import *
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.pages.android.common.super_page import *

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


'''
    usage: 飞凡卡
'''

class FeiFanCardBillPage(SuperPage):

    def __init__(self,testcase,driver,logger):
        super(FeiFanCardBillPage, self).__init__(testcase = testcase , driver = driver, logger = logger);

    '''
        usage : 检查是否加载出来
    '''
    def validSelf(self):
        API().assert_view_by_resourceID_Until_android(testcase = self.testcase, driver = self.driver, logger = self.logger, resource_id = FeiFanCardBillPageConfigs.resource_id_tv_bill_list_tv, seconds = 10)
     
if __name__ == '__main__':
    pass;