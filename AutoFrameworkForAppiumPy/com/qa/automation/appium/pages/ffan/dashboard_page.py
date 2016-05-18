# -*- coding: utf-8 -*-

import os,sys

#sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from time import sleep
import unittest
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.pages.ffan.dashboard_page_configs import *
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.pages.common.super_page import *

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

#
#   进入应用的首页,是进入其他页面的入口
class DashboardPage(SuperPage):

    def __init__(self,testcase,driver,logger):
        super(DashboardPage, self).__init__(testcase = testcase , driver = driver,logger = logger);

    '''
        usage : 进入到应用首页,检查ffan logo
    '''
    def validSelf(self):
        API().assert_view_by_resourceID_Until_android(testcase = self.testcase , driver = self.driver,logger = self.logger ,
                                                resource_id = DashboardPageConfigs.resource_id__iv_logo__iv,seconds=18);

    def clickOnMy(self):
        API().click_view_by_text_android(driver=self.driver,logger=self.logger,text=DashboardPageConfigs.text_mine);


    def clickOnSmartLife(self):
        API().click_view_by_text_android(driver=self.driver,logger=self.logger,text=DashboardPageConfigs.text_huishenghuo);

if __name__ == '__main__':
    pass;