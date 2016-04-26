#! /Library/Frameworks/Python.framework/Versions/2.7/bin/python
# -*- coding: utf-8 -*-

import os,sys
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append(os.path.dirname(os.path.dirname(__file__)))



from time import sleep
import unittest
from configs.driver_configs import *
from safari_activity_configs import *
from api.api import *
from common.super_page import *

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class SafariActivity(SuperPage):

    def __init__(self,driver):
        self.driver = driver;

    def clickOnTitleProfileIV(self):
        API.clickViewByResourceID(self.driver,SafariActivityConfigs.resource_id_title_profile);

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidDriver)
    unittest.TextTestRunner(verbosity=2).run(suite)