# -*- coding: utf-8 -*-

import os,sys

#sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from time import sleep
import unittest
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.pages.android.ffan.sales_promotion_coupon_details_page_configs import *
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.pages.android.common.super_page import *

from appium import webdriver
from com.qa.automation.appium.pages.android.ffan.sales_promotion_active_details_page_configs import SalesPromotionActiveDetailsPageConfigs

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)



class SalesPromotionActiveDetailsPage(SuperPage):

    def __init__(self,testcase,driver,logger):
        super(SalesPromotionActiveDetailsPage, self).__init__(testcase = testcase , driver = driver, logger = logger);

    def validSelf(self):
        '''
            usage : "活动详情" whether loading correctly.
        '''
        API().assert_view_by_resourceID_Until(testcase = self.testcase, driver = self.driver, logger = self.logger, resource_id = SalesPromotionActiveDetailsPageConfigs.resource_id_tv_active_details_title_tv, seconds = 10)
 
     
if __name__ == '__main__':
    pass;