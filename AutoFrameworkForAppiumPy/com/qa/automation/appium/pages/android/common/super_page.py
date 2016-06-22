# -*- coding: utf-8 -*-

import os, sys
# reload(sys)
# sys.setdefaultencoding('utf8')
# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import unittest
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.utility.logger import *


class SuperPage(object):
    def __init__(self, testcase, driver, logger):
        self.testcase = testcase
        self.driver = driver
        self.logger = logger

    def waitBySeconds(self, seconds=1):
        API().wait_by_seconds(seconds);

    def clickBackKey(self):
        API().click_back_key(driver=self.driver, logger=self.logger);
        
    def scrollAsScreenPercent(self,start_x_percent,start_y_percent,end_x_percent,end_y_percent,duration=800):
        '''
            Description : scroll as screen percent
        '''
        x = API().get_width_of_device(driver = self.driver, logger = self.logger)
        y = API().get_height_of_device(driver = self.driver, logger = self.logger)
        
        API().scroll(driver = self.driver, logger = self.logger,start_x = x*start_x_percent,start_y = y*start_y_percent, end_x = x*end_x_percent, end_y = y*end_y_percent, duration = duration);
        API().wait_by_seconds(seconds = 2)
            
            
if __name__ == '__main__':
    pass
