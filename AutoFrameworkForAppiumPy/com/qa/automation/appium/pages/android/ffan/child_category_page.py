# -*- coding: utf-8 -*-

import os,sys

#sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from time import sleep
import unittest
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.pages.android.ffan.child_category_page_configs import *
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.pages.android.common.super_page import *

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


#   首页点击 美食
class ChildCategoryPage(SuperPage):

    def __init__(self,testcase,driver,logger):
        super(ChildCategoryPage, self).__init__(testcase = testcase , driver = driver,logger = logger);

    '''
        usage : 进入美食页面，根据餐饮的textview,检查找餐饮页面是否加载出来.
    '''
    def validSelf(self):
        API().assert_view_by_resourceID_Until_android(testcase = self.testcase , driver = self.driver,logger = self.logger ,
                                                resource_id = ChildCategoryPageConfigs.resource_id_ll_child_play_ll,seconds=18);
                                           
    '''
        usage : 点击亲子游乐
    '''
    def clickOnChildPlay(self):
        API().click_view_by_resourceID_android(testcase = self.testcase, driver=self.driver,logger=self.logger,resource_id=ChildCategoryPageConfigs.resource_id_ll_child_play_ll);
        
    '''
        usage : 点击门店的listView
    ''' 
    def clickListFirstItem(self):
        API().click_view_by_xpath(testcase = self.testcase, driver=self.driver, logger=self.logger, xpath=ChildCategoryPageConfigs.xpath_store_list_1);    
        
    '''
        usage : 点击儿童教育
    '''
     
    def clickOnChildEducation(self):
        API().click_view_by_resourceID_android(testcase = self.testcase, driver=self.driver,logger=self.logger,resource_id=ChildCategoryPageConfigs.resource_id_ll_child_education_ll);
        
    '''
        usage : 点击亲子购物
    '''        
     
    def clickOnChildShopping(self):
        API().click_view_by_resourceID_android(testcase = self.testcase, driver=self.driver,logger=self.logger,resource_id=ChildCategoryPageConfigs.resource_id_ll_child_shopping_ll);
        
    '''
        usage : 点击亲子购物
    '''        
     
    def clickOnOtherStore(self):
        API().click_view_by_resourceID_android(testcase = self.testcase, driver=self.driver,logger=self.logger,resource_id=ChildCategoryPageConfigs.resource_id_ll_other_store_ll);
            
if __name__ == '__main__':
    pass;