# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))))

from time import sleep
import unittest

from appium import webdriver

from com.qa.automation.appium.api.api import *

from com.qa.automation.appium.pages.ios.common.ios_super_page import *
from com.qa.automation.appium.pages.ios.ffan.dashboard_page_configs import *

'''
    usage :  进入应用的首页
'''


class DashboardPage(IosSuperPage):
    def __init__(self, testcase, driver, logger):
        super(DashboardPage, self).__init__(testcase=testcase, driver=driver, logger=logger)

    '''
        usage : 进入到应用首页,检查ffan logo
    '''
    def valid_self(self):
        # name_home_title_icon = API().get_view_by_resourceID(driver=self.driver,logger=self.logger,resource_id=DashboardPageConfigs.name_home_title_icon);
        API().assert_view_by_resourceID_Until(testcase=self.testcase,driver=self.driver,logger=self.logger,resource_id=DashboardPageConfigs.name_home_title_icon,seconds=10);


    def click_aiguangjie(self):
        API.click_view_by_resourceID_android()

if __name__ == '__main__':
    print("path %s" % (sys.path))
