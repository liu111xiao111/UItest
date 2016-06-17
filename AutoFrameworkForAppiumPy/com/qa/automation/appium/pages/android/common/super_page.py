# -*- coding: utf-8 -*-

import os,sys
# reload(sys)
# sys.setdefaultencoding('utf8')
#sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import unittest
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.utility.logger import *

class SuperPage(object):

    def __init__(self,testcase,driver,logger):
        self.testcase = testcase
        self.driver = driver
        self.logger = logger

    def waitBySeconds(self,seconds=1):
        API().wait_by_seconds(seconds);
        
    def clickBackKey(self):
        API().click_back_key(driver=self.driver, logger=self.logger);
        
    
    '''
        Description : scroll as screen percent
        orientation: if orientation is down,scroll to bootom of screen
    '''
        
    def scrollAsScreenPercent(self,xPercent,yPercent,orientation):
        x = API().get_width_of_device(driver = self.driver, logger = self.logger)
        y = API().get_height_of_device(driver = self.driver, logger = self.logger)
        
        if orientation == "down":    
            API().scroll(driver = self.driver, logger = self.logger,start_x = x*10/xPercent,start_y = y*10/xPercent, end_x = x*10/xPercent, end_y = y*10/yPercent, duration = 1);
            API().wait_by_seconds(seconds = 2)
        elif orientation == "up": 
            API().scroll(driver = self.driver, logger = self.logger,start_x = x*10/xPercent,start_y =y*10/yPercent, end_x = x*10/xPercent, end_y = y*10/xPercent, duration = 1);
            API().wait_by_seconds(seconds = 2)   
            
            
if __name__ == '__main__':
    pass