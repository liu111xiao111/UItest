# -*- coding: utf-8 -*-

import os,sys

#sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from time import sleep
import unittest
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.pages.android.ffan.sales_promotion_page_configs import *
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.pages.android.common.super_page import *

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)



class SalesPromotionPage(SuperPage):

    def __init__(self,testcase,driver,logger):
        super(SalesPromotionPage, self).__init__(testcase = testcase , driver = driver, logger = logger);

    def validSelf(self):
        '''
            usage : Check "优惠活动" whether loading correctly.
        '''
        API().assert_view_by_resourceID_Until(testcase = self.testcase, driver = self.driver, logger = self.logger, resource_id = SalesPromotionPageConfigs.resource_id_tv_active_tv, seconds = 10)
 
    def clickOnActiveTab(self):
        '''
            usage : Check active tab
        '''     
        API().click_view_by_resourceID(testcase = self.testcase, driver = self.driver, logger = self.logger, resource_id = SalesPromotionPageConfigs.resource_id_tv_active_tv)

    def clickOnCouponTab(self):
        '''
            usage : Check coupon tab
        '''     
        API().click_view_by_resourceID(testcase = self.testcase, driver = self.driver, logger = self.logger, resource_id = SalesPromotionPageConfigs.resource_id_tv_coupon_tv)
    
    def clickOnActiveDetails(self):
        '''
            usage : Check active details
        '''     
        API().click_view_by_resourceID(testcase = self.testcase, driver = self.driver, logger = self.logger, resource_id = SalesPromotionPageConfigs.resource_id_tv_active_details_tv)

    def clickOnCouponDetails(self):
        '''
            usage : Check coupon details
        '''     
        API().click_view_by_resourceID(testcase = self.testcase, driver = self.driver, logger = self.logger, resource_id = SalesPromotionPageConfigs.resource_id_tv_coupon_details_tv)
     
if __name__ == '__main__':
    pass;