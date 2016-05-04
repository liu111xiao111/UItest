#! /Library/Frameworks/Python.framework/Versions/2.7/bin/python
# -*- coding: utf-8 -*-

import os,sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))



from time import sleep
import unittest
from configs.driver_configs import *
from pages.ffan.dashboard_page_configs import *
from api.api import *
from common.super_page import *

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

    def validSelf(self):
        self.logger.d("SafariActivityConfigs.resource_id__iv_logo__iv : %s",SafariActivityConfigs.resource_id__iv_logo__iv);
        API().assert_view_by_resourceID_Until_android(testcase = self.testcase , driver = self.driver,logger = self.logger ,
                                                resource_id = SafariActivityConfigs.resource_id__iv_logo__iv,seconds=18);


if __name__ == '__main__':
    pass;