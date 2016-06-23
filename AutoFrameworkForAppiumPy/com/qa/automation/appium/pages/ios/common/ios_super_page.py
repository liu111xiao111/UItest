# -*- coding: utf-8 -*-

import os, sys
# reload(sys)
# sys.setdefaultencoding('utf8')
# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import unittest
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.utility.logger import *


class IosSuperPage(object):

    def __init__(self, testcase, driver, logger):
        self.testcase = testcase
        self.driver = driver
        self.logger = logger

    def wait_by_seconds(self, seconds=1):
        API().wait_by_seconds(seconds);

if __name__ == '__main__':
    pass
